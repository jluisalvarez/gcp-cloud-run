
# file app.py

from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def holamundo():
    platform = os.getenv("PLATFORM") or "World"
    return 'Hola Mundo from jluisalvarez in ' + platform + '!'
    

if __name__ == '__main__':
    #app.run()
    app.run(host='0.0.0.0',
            debug=True,
            port=8080)
