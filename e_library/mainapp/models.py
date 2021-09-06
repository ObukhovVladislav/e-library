from django.db import models


class Author(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=30)
    surname = models.CharField(verbose_name='Фамилия', max_length=40)
    desk = models.TextField(verbose_name='Описание')
    img_author = models.ImageField(verbose_name='Название жанра', upload_to='img_author', blank=True)

    def __str__(self):
        return f'{self.name}: {self.surname}'

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    title = models.CharField(verbose_name='Название книги', max_length=100)
    book_author = models.ManyToManyField('authapp.UserProfile', related_name='book_authors')
    book_date = models.CharField(verbose_name='Дата книги', max_length=5)

    def __str__(self):
        return f'{self.author}: {self.title}'

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class Genre(models.Model):
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    name = models.CharField(verbose_name='Название жанра', max_length=30)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
