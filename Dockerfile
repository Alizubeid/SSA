FROM python:3.10.17-alpine3.21
RUN mkdir /app
WORKDIR /app
COPY ./app /app
RUN pip install --no-cache-dir -r requirements.txt --upgarde
CMD ["python", "main.py"]