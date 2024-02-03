# Etapa de construcción para resolver dependencias
FROM python:3.10-slim AS builder

WORKDIR /app

# Transferir solo los archivos necesarios para resolver dependencias
COPY requirements.txt .

# Instalar dependencias en un entorno virtual
RUN python -m venv venv && \
    venv/bin/pip install --no-cache-dir -r requirements.txt

# Etapa de ejecución
FROM python:3.10-slim AS runner

WORKDIR /app

# Transferir el entorno virtual y la aplicación desde la etapa de construcción
COPY --from=builder /app/venv venv
COPY . .

# Transferir archivos esenciales para la aplicación
COPY bayeta.py .
COPY frases.txt .
COPY moodle.py .

COPY panda.png /app/static/panda.png

# Comando para ejecutar la aplicación
CMD ["venv/bin/python", "app.py"]
