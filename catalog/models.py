from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'Категория: {self.name}'

    class Meta:

        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']


class Product(models.Model):

    name = models.CharField(max_length=100, verbose_name = 'Наименование')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(verbose_name='Изображение', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', related_name='products')
    buying_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена за покупку')
    created_at = models.DateField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата последнего изменения', auto_now=True)
    publish = models.BooleanField(verbose_name='Статус публикации', default=False)

    def __str__(self):
        return self.name

    class Meta:

        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name']
        permissions = [
            ('can_unpublish_product', 'can unpublished product'),
        ]

