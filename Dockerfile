FROM python:3.6

WORKDIR /app

COPY ./app /app

ENV PROVIDER World

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py"]