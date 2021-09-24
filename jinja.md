### JINJA шаблонизатор

**include** - позволяет интегрировать html код из одного файла в другой
{% include 'head.html' %}
**extends** - позволяет наследоваться от родительского шаблона. 

{% if item.finish > date_now %} 

{{current_user}} - пользователь зарег на сайте

DATA

ДОбавить форматирование для даты 
tour.created.strftime('%d-%m-%Y')

