FROM python:3.12.2-slim

# Install system tools if needed
RUN apt-get update && apt-get install -y git && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose Gradio default port
EXPOSE 7860

CMD ["python3", "app.py"]
