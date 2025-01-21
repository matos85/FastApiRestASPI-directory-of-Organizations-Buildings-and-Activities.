FROM postgres:13

# Копируем скрипт инициализации базы данных в контейнер
COPY init_db.py /docker-entrypoint-initdb.d/

# Убедитесь, что скрипт имеет права на выполнение
RUN chmod +x /docker-entrypoint-initdb.d/init_db.py