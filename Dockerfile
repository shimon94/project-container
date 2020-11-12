FROM python:latest


WORKDIR /app/src

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY chromedriver
COPY main
RUN python main.py

CMD ["python","main"]