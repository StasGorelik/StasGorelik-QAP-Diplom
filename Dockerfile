FROM mcr.microsoft.com/playwright/python:v1.49.0

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

ENV BASE_URL=http://host.docker.internal:8000/

COPY . .

CMD ["pytest", "--alluredir=./allure-results"]