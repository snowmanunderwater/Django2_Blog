# Django 2.0 Blog


## Главная страница с постами:
![Django 2.0 Blog](https://raw.githubusercontent.com/snowmanunderwater/Django2_Blog/master/screenshots/Screenshot_Main.jpg)

---

## Пагинация:
![Django 2.0 Blog](https://raw.githubusercontent.com/snowmanunderwater/Django2_Blog/master/screenshots/Screenshot_Pagination.png)

Отображается, если постов больше 3.
```Python
blog/Views.py
paginator = Paginator(posts, 3)
```

---

## Поиск по заголовку и телу поста:
![Django 2.0 Blog](https://raw.githubusercontent.com/snowmanunderwater/Django2_Blog/master/screenshots/Screenshot_Search.png)

---

## К посту можно прикрепить тег и фильтровать по нему выдачу:
![Django 2.0 Blog](https://raw.githubusercontent.com/snowmanunderwater/Django2_Blog/master/screenshots/Screenshot_Tags.png)

---

## Меню редактора:

![Django 2.0 Blog](https://raw.githubusercontent.com/snowmanunderwater/Django2_Blog/master/screenshots/Screenshot_Admin_panel.png)

* Позволяет создавать и редактировать посты и теги. 
* При наведении курсора становится непрозрачным.
* Функции удаления и редактирования появляются только на страницах с подробным просмотром:

![Django 2.0 Blog](https://raw.githubusercontent.com/snowmanunderwater/Django2_Blog/master/screenshots/Screenshot_Admin_panel_expand.png)