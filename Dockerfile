FROM python:latest


WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY chromedriver
COPY /app .
CMD ["python", "main.py"]


