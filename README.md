
## Задача

Нужно сделать django app, который будет реализовывать древовидное меню, соблюдая следующие условия:

1. Вносить в БД меню через админку Django.
2. Отображать меню на любой нужной странице по названию с использованием template tag.

## Особенности реализации

1. Меню реализовано через template tag
2. Все, что над выделенным пунктом - развернуто. Первый уровень вложенности под выделенным пунктом тоже развернут.
3. Хранится в БД.
4. Редактируется в стандартной админке Django
5. Активный пункт меню определяется исходя из URL текущей страницы
6. Меню на одной странице может быть несколько. Они определяются по названию.
7. При клике на меню происходит переход по заданному в нем URL. URL может быть задан как явным образом, так и через named url.
8. На отрисовку каждого меню требуется ровно 1 запрос к БД
9. Нужен django-app, который позволяет вносить в БД меню (одно или несколько) через админку, и нарисовать на любой нужной странице меню по названию.
 {% draw_menu 'main_menu' %}
10. При выполнении задания из библиотек следует использовать только Django и стандартную библиотеку Python.
11. При решении тестового задания у вас не должно возникнуть вопросов. Если появляются вопросы, вероятнее всего, у вас недостаточно знаний.


## Стек

1. Django
2. Python стандартная библиотека

## Инструкции по запуску

1. Клонируйте репозиторий и перейдите в каталог проекта: git clone https://github.com/vinglivskt/TreeMenu.git
2. Активируйте виртуальное окружение с помощью: `venv\Scripts\activate`
3. Установите все зависимости: `pip install -r requirements.txt`
4. Выполните миграции: `python manage.py migrate`
5. Создайте суперпользователя БД `python manage.py createsuperuser`
6. Загрузите данные с помощью `python manage.py loaddata data.json`
7. Запустите сервер: `python manage.py runserver`
8. Для перехода в административную панель http://127.0.0.1:8000/admin/
9. Для перехода в меню http://127.0.0.1:8000/

Запуск Docker
-------------

```
git clone https://github.com/vinglivskt/TreeMenu.git
cd DjangoStripeAPI
docker-compose up -d
```
Главная страница: http://localhost:8000/
#### Остановка Docker:
```
docker-compose stop
```