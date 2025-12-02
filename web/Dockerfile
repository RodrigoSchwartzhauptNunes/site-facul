FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

# Expõe a porta interna que o Gunicorn usará
EXPOSE 8080

# Comando final
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]