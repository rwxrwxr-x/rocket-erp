# Rocket-ERP

**Система складского учета**

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

---

 ### [Техническое задание на минимально жизнеспособный продукт](docs/MVP.md)

---

### Документация

[Описание конечного продукта](docs/Specification.md)<br>
[Схема взаимных связей объектов](docs/uml/rocket-erp-diagram.png)<br>
[Диаграмма последовательности](docs/uml/rocket-erp-sequence-diagram.png)<br>
[Диаграмма отношений базы данных](docs/uml/rocket-erp-db-relationship-diagram.png)<br>

### Установка


**Окружение** Python 3.9, Node 14.7.1
Чтобы развернуть проект локально, выполните следующие команды в консоли:
```bash
git clone https://github.com/dimmy2000/rocket-erp.git
cd rocket-erp
python3 -m pip install --user poetry
poetry shell && poetry install
chmod +x ./manage.sh
./manage.sh postgres
./manage.sh deploy backend
./manage.sh deploy frontend
```

**Запуск сервера**

Создаём администратора: <code>./manage.sh createsuperuser</code>

Запускаем сервер: <code>./manage.sh runserver</code>
Запускаем фронт в режиме разработки: <code>./manage.sh front dev</code>

Сервер должен быть доступен по http://127.0.0.1:8000
Фронт должен быть доступен по http://127.0.0.1:3000

