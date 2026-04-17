# Task Tracker API

## 📌 Описание

Backend-приложение для управления задачами, реализованное на FastAPI.

Функционал:

* регистрация и авторизация пользователей (JWT)
* управление задачами (создание, просмотр, обновление, удаление)
* роли пользователей (admin / user)
* Redis-кэширование списка задач

---

## Архитектура

Проект разделён на слои:

* **core** — конфигурация, подключение к БД, безопасность
* **models** — SQLAlchemy модели
* **schemas** — Pydantic-схемы и валидация данных
* **repositories** — работа с базой данных (CRUD)
* **services** — бизнес-логика приложения
* **api** — маршруты FastAPI (HTTP слой)


---

## Структура проекта

* core — конфигурация и безопасность
* models — модели базы данных
* schemas — Pydantic-схемы
* repositories — работа с БД
* services — бизнес-логика
* api — маршруты

![Структура проекта](image-1.png)

---

## Запуск проекта

```bash
docker-compose up --build
```

После запуска приложение доступно по адресу:

👉 http://localhost:8000/docs

---

## Основные маршруты

### Auth

* POST /auth/register
* POST /auth/login
* GET /auth/me

### Tasks

* POST /tasks/
* GET /tasks/
* GET /tasks/{task_id}
* PATCH /tasks/{task_id}
* DELETE /tasks/{task_id}

### Admin

* GET /admin/users

---

## Фото работающего функционала


### Работа с задачами

![Tasks](image-2.png)

### Админ доступ

![Admin](image-2.png)

### Schemas

![alt text](image-3.png)

---

## Docker

Приложение запускается в Docker-контейнере:

* backend — FastAPI (uvicorn)
* redis — кэширование

---

## Требования выполнены

* монолитный файл разбит на модули
* реализована чистая архитектура
* добавлена JWT-аутентификация
* реализовано Redis-кэширование
* проект запускается через Docker
* Swagger документация доступна

---
