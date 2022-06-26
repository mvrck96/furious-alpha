FROM python:3.9-slim-buster

ARG folder=/backend

WORKDIR ${folder}

COPY requirements.txt requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY /main.py ${folder}
CMD gunicorn main:app\
    --workers 4\
    --worker-class uvicorn.workers.UvicornWorker\
    --bind 0.0.0.0:9999
