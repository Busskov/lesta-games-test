# Тестовое задание Леста Игры

Этот проект демонстрирует работу Flask-приложения с Redis в качестве кэша, развернутого через Docker Compose. Приложение предоставляет два эндпоинта:

`/ping — проверка работоспособности сервера.`

`/count — увеличение счетчика посещений (хранится в Redis).`

## Структура проекта

```
Lesta-Games-Test/
├── flask_app/
│   ├── app.py             # Flask-приложение с Redis
│   ├── requirements.txt   # Зависимости Python
│   └── Dockerfile         # Конфигурация образа Flask
├── docker-compose.yaml    # Конфигурация сервисов
└── README.md              # Инструкция
```

## Запуск проекта
Клонируйте репозиторий (если нужно) и перейдите в папку проекта:

```bash
git clone <репозиторий>
cd flask-redis-docker
```

Собрать и запустить сервисы:

```bash
docker-compose up --build
```

## Проверить работу:

```bash
curl http://localhost:5000/ping
```
Ответ: {"status": "ok"}

```bash
curl http://localhost:5000/count
```

Ответ: {"visit_count": 1, "redis_status": "connected"}
(При повторных запросах счетчик будет увеличиваться).
