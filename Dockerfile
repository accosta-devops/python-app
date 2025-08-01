FROM python:3.12-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt 

COPY ./src/app.py .

CMD ["python", "app.py"]

