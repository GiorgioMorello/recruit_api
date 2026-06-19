FROM python:3.12-slim

# Diretório interno do container
WORKDIR /app

# Copia dependências
COPY requirements.txt .

# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia projeto
COPY . .

# Garante existência da pasta do SQLite
RUN mkdir -p /data

# Inicializa FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5003"]