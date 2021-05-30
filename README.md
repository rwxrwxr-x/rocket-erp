# Rocket-ERM

**Система складского учета для "Rocket Manufacture"**

---

 ### [Техническое задание на минимально жизнеспособный продукт](docs/MVP.md)

---

### Документация

[Описание продукта](docs/Specification.md)<br>
[Схема взаимных связей объектов](docs/uml/rocket-erp-diagram.png)<br>
[Диаграмма последовательности](docs/uml/rocket-erp-sequence-diagram.png)<br>

### Установка
Чтобы развернуть проект локально, выполните следующие команды в консоли:
```shell
git clone https://github.com/dimmy2000/rocket-erp.git
cd rocket-erp
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pre-commit install
```
