# Task Tracker API

## 📌 Описание
Backend-приложение для управления задачами с использованием FastAPI.

Функционал:
- регистрация и авторизация (JWT)
- управление задачами
- роли пользователей (admin)
- Redis-кэширование

---

## 📁 Структура проекта

- core — конфигурация и безопасность
- models — модели базы данных
- schemas — Pydantic-схемы
- repositories — работа с БД
- services — бизнес-логика
- api — маршруты

![alt text](image-1.png)

---
## Фото работающего функционала

![alt text](image.png)

![alt text](image-2.png)

![alt text](image-3.png)

---

## 🚀 Запуск

```bash
docker-compose up --build