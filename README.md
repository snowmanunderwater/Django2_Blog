# Django 2.0 Blog

### Django 2.0.7 + Bootstrap4

### Главная страница с постами:
![Django 2.0 Blog](https://raw.githubusercontent.com/snowmanunderwater/Django2_Blog/master/screenshots/Screenshot_Main.jpg)

### Пагинация:
![Django 2.0 Blog](https://raw.githubusercontent.com/snowmanunderwater/Django2_Blog/master/screenshots/Screenshot_Pagination.png)

Отображается, если постов больше 3.
```Python
blog/Views.py
paginator = Paginator(posts, 3)
```

### Поиск по заголовку и телу поста:
![Django 2.0 Blog](https://raw.githubusercontent.com/snowmanunderwater/Django2_Blog/master/screenshots/Screenshot_Search.png)


### К посту можно прикрепить тег и фильтровать по нему выдачу:
![Django 2.0 Blog](https://raw.githubusercontent.com/snowmanunderwater/Django2_Blog/master/screenshots/Screenshot_Tags.png)