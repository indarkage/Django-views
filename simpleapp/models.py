from django.db import models
from django.core.validators import MinValueValidator
 
 
# Создаём модель товара 
class New(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True, # названия товаров не должны повторяться
    )
    text = models.TextField()
    # поле категории будет ссылаться на модель категории
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='news', # все продукты в категории будут доступны через поле products
    )
    rate = models.FloatField(
        validators=[MinValueValidator(0.0)],
    )
 
    def __str__(self):
        return f'{self.name.title()}: {self.text[:20]}'
 
 
#  создаём категорию, к которой будет привязываться товар
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  # названия категорий тоже не должны повторяться
 
    def __str__(self):
        return f'{self.name.title()}'

# class New(models.Model):
#     text = models.TextField()  # названия категорий тоже не должны повторяться
 
#     def __str__(self):
#         return f'{self.text.title()}'