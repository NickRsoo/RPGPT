# Basis-Image: Python mit minimalem Setup
FROM python:3.12.7

# Arbeitsverzeichnis innerhalb des Containers
WORKDIR /app

# Kopiere alle Projektdateien in das Arbeitsverzeichnis
COPY . /app

# Installiere die notwendigen Python-Pakete
RUN pip install --no-cache-dir -r requirements.txt

# Exponiere den Standard-Port für NiceGUI (3500)
EXPOSE 3500

# Starte die NiceGUI-App
CMD ["python", "app/main.py"]
