FROM python:3

EXPOSE 8000

WORKDIR /Lab_3_ID_Web/Lab3idweb/testsuperapi

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . ./


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
#CMD ["python", "manage.py", "runserver"]
