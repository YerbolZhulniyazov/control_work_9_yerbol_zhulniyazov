from django.contrib.auth import get_user_model
from django.db import models


class Image(models.Model):
    image = models.ImageField(
        verbose_name='Фотография',
        default='default_image',
        null=False,
        blank=False
    )
    sign = models.CharField(
        verbose_name='Подпись',
        max_length=150,
        null=False,
        blank=False
    )
    author = models.ForeignKey(
        verbose_name='Автор',
        to=get_user_model(),
        related_name='images',
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    users = models.ManyToManyField(
        to=get_user_model(),
        related_name='favorites'
    )
    created_at = models.DateTimeField(
        verbose_name='Время создания',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Время изменения',
        auto_now=True
    )

    def __str__(self):
        return f"{self.image} - {self.sign} - {self.author}"

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
