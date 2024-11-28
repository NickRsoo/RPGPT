# Basis-Image: Python mit minimalem Setup
FROM python:3.10-slim

# Arbeitsverzeichnis innerhalb des Containers
WORKDIR /app

# Kopiere alle Projektdateien in das Arbeitsverzeichnis
COPY . /app

# Installiere die notwendigen Python-Pakete
RUN pip install --no-cache-dir -r requirements.txt

# Exponiere den Standard-Port für NiceGUI (8080)
EXPOSE 8080

# Starte die NiceGUI-App
CMD ["python", "main.py"]
