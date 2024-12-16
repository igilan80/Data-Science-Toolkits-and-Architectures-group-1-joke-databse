
FROM python:3.12-slim

RUN useradd -m appuser

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --require-hashes -r requirements.txt

COPY src/ /app/src/
COPY .env /app/

RUN chown -R appuser:appuser /app

USER appuser

CMD ["python3", "src/main.py"]

