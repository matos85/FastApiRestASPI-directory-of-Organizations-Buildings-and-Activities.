# Используем базовый образ Python 3.9
FROM python:3.9

# Установка необходимых системных пакетов
RUN apt-get update && apt-get install -y \
    netcat-openbsd \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Установка рабочей директории
WORKDIR /app

# Копируем файлы зависимостей
COPY requirements.txt .

# Установка зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы приложения
COPY . .

# Команда для запуска приложения
CMD ["sh", "-c", "until nc -z db 5432; do echo waiting for database; sleep 1; done; uvicorn main:app --host 0.0.0.0 --port 8000"]
