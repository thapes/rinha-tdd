FROM python:3

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY src .
EXPOSE 80
CMD uvicorn main:app --host 0.0.0.0 --port 80