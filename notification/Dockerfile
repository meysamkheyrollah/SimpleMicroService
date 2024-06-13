FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirments.txt /app/
RUN pip install --upgrade pip && pip install -r requirments.txt
COPY . /app/


