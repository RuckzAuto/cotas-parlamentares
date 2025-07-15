# Use uma imagem Python leve e atual
FROM python:3.11-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos do projeto para o container
COPY . .

# Instala as dependências
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Expõe a porta padrão do Gunicorn (ajuste se quiser)
EXPOSE 8000

# Comando de start (Gunicorn com 2 workers para produção)
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8000", "--workers=2"]
