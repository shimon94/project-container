FROM python:latest


WORKDIR C:\Users\swagabit\Documents\GitHub\test reposetry\src\project-container

COPY main.py
COPY package.jason
CMD ["python", "./main.py"]

RUN make /main.py
CMD python C:\Users\swagabit\Documents\GitHub\test reposetry\src\project-container\main.py

