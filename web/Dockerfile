FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia tudo para dentro do container (incluindo /static e /templates)
COPY . /app

CMD ["python3", "app.py"]
