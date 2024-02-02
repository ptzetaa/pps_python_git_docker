# Dockerfile

# Fase de resolución de dependencias
FROM python:3.8-slim as base

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Fase de ejecución
FROM python:3.8-slim as runtime

WORKDIR /app

COPY --from=base /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages

COPY . .

# Comando para inicializar la base de datos
CMD ["python", "moodle.py"]

# Comando para ejecutar la aplicación después de la inicialización
CMD ["python", "app.py"]
