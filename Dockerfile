FROM python:latest


WORKDIR /app

COPY requirements.txt .
COPY chromedriver .
COPY main .

RUN pip install -r requirements.txt
RUN python main.py
CMD ["python","main"]