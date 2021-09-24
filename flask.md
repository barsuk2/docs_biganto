### FLASK
####
Bluprint - позволяет создавть модули в приложении

1. Создается папка или пакет.
2. Создатеся экземпляр класса Blueprint
from flask import Blueprint
modul=Blueprint('myapp',__name__)
   или
modul=Blueprint('myapp',__name__, url_prefix='/myapp')   


3. Регистрация модуля 
app.py
app.register_blueprint(modul, url_prefix='/myapp')
или
app.register_blueprint(modul, admin,adads)

### [JINJA2]
https://jinja.palletsprojects.com/en/2.11.x/

from jinja2 import Template

name = {'a': 10}
class Test():
    def __init__(self, a, b):
        self.a = a
        self.b = b

exem = Test(15,20)

template = Template(' Привет {{ name.a}} {{ name.b}} {{ name2.a}}')
print(template.render(name=exem, name2=name))

>Елси у класса есть геттер, то {{ name.getter() }} 
>Если передаем словарь, то {{name['key']}}

#### Экранирование
{% raw %} {% endraw %}

#### Экранирование HTML тегов используется фильтр e [|e]
template = Template( '{{ name| e}}' )
>или через класс escape

from jinja2 import Template, escape
data = """ <a href="">test</a>"""
msg= escape(data)
print(msg)
#### Цикл
tm=Template('{% for car in cars%} {{car.model }} {{car.price }} {% endfor %}')

#### Фильтры 
https://jinja.palletsprojects.com/en/2.11.x/templates/?highlight=sum#sum
cars = [
    {'model': 'Ауди', 'price': 23000},
{{cars | sum(attribute="price") }} - суммирование по 'price'

##### БЛок фильтр
{% filter [ название фильтра] %}
Применяетсяко всему что внутри
{% endfilter %}
#### Макро определения

{% macro input1(name, value='', type='text', size=20) -%}
    <input type="{{ type }}" name="{{ name }}" value="{{ value|e }}" size="{{ size }}">
{%- endmacro %}


### 
Правила для URL, работающие в Flask, основаны на модуле маршрутизации Werkzeug


#### РАБОТА С ФОРМАМИ

класс Form

Методы 

data - словарь со всеми данными формы
populate_obj - метод переносит данные в модель

form_member.city_id.data - доступ к значению поля формы

Алгроритм
1. Создаем форму, наследуясь от FlaskForm
2. В endpoit создаем экземпляр формы и передаем ее в шаблон.
3. В шаблоне размещаем форму
4. 


### Создание manage_script
1. Создаем в папке manage - файл скрипта
2. импортируем из flask_script Command
3. Создаем класс , наследуясь от Command
3.1 Создается метод run(self):
4. Регистрируем в /manage/__init__.py
5. В py.py регистрируем наш класс
>manager.add_command('псевдоним', "Наш класс")
6. Для создания свойств
6.1 В файле скрипта импортируется из flask_script Options.
6.2 Создаем кортеж options-list = (Options(название опции str, help='Справка по опции',[action='store_true'],[default='parametr_default]),)
6.3 В методе run обрабатываем аргумент "название опции". Название опции без "--" Воспринимается как обязательный параметр, c "--" как не обязательный и можно ему установить параметр поумолчанию default='parametr_default'
6.4 Параметр action='store_true' указывает на необязательность аргумента. ТО есть не --del=10, а --del
