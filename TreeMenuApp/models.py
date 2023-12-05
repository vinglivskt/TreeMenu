from django.db import models


class Menu(models.Model):

    """ Меню содержащее несколько пунктов меню """

    title = models.CharField(max_length=255, unique=True, verbose_name='title')
    slug = models.SlugField(max_length=255, verbose_name="slug")

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.title


class MenuItem(models.Model):

    """ Представляет пункт меню, который может быть вложен в иерархическую структуру """

    title = models.CharField(max_length=255, verbose_name='title')
    slug = models.SlugField(max_length=255, verbose_name="slug")

    menu = models.ForeignKey(
        Menu, blank=True, related_name='items', on_delete=models.CASCADE
    )
    parent = models.ForeignKey(
        'self', blank=True, null=True, related_name='childrens', on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

    def __str__(self):
        return self.title
