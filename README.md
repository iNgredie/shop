Запуск проекта.
 - Скопировать проект с помощью ``` git clone https://github.com/iNgredie/shop.git ```
 - ```docker-compose up --build ```  собрать приложение и сделать его первоначальный запуск
 - ```docker-compose down -v``` – остановить работу приложения
 - ```docker-compose run web python manage.py migrate``` – сделать необходимые миграции
 - ```docker-compose up``` – окончательно запустить приложение.

Стек технологий и требований к ним для реализации веб-приложения 

- Python 3
- Django 
- Django-rest-framework

``` http://localhost:8000/api/v1/city/``` Получение всех городов из базы Method GET    
``` http://localhost:8000/api/v1/city/<id>/street/``` получение всех улиц города Method GET (city_id —
идентификатор города)   
``` http://localhost:8000/api/v1/shop/``` создание магазина; Данный метод получает json объектом магазина, в ответ возвращает id созданной записи.
Ресурс получения статистики Method POST   
``` http://localhost:8000/api/v1/shop/?street=&city=&open=0/1``` получение списка магазинов Method GET
