# Imagen base Python
FROM python:3.11-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar archivo de dependencias
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código fuente
COPY . .

# Crear carpetas necesarias
RUN mkdir -p data logs

# Exponer puerto de la API
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]