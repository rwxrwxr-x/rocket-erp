# Rocket-ERP

**Система складского учета для "Rocket Manufacture"**

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

---

 ### [Техническое задание на минимально жизнеспособный продукт](docs/MVP.md)

---

### Документация

[Описание конечного продукта](docs/Specification.md)<br>
[Схема взаимных связей объектов](docs/uml/rocket-erp-diagram.png)<br>
[Диаграмма последовательности](docs/uml/rocket-erp-sequence-diagram.png)<br>

### Установка


**Окружение**
Чтобы развернуть проект локально, выполните следующие команды в консоли:
```bash
git clone https://github.com/dimmy2000/rocket-erp.git
cd rocket-erp
python3 -m pip install --user poetry
poetry shell && poetry install && cp .env.template .env
```

**Запуск сервера**

Создаем БД: <code>python manage.py migrate</code>

Создаём администратора: <code>python manage.py createsuperuser</code>

Запускаем сервер: <code>python manage.py runserver</code>

Сервер должен быть доступен по http://127.0.0.1:8000
Админ-панель http://127.0.0.1:8000/admin
