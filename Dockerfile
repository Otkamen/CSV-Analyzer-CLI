FROM python:3.14-slim
WORKDIR /app
COPY requerments.txt .
RUN pip install -r requerments.txt
COPY . .
CMD ["python","main.py"]
