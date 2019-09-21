from django.db import models

STATUS_CHOICES = [('active', 'Активно'), ('blocked', 'Заблокировано')]


class Record(models.Model):
    author = models.CharField(max_length=40, default='Unknown', verbose_name='Автор')
    email_author = models.EmailField(max_length=60, verbose_name='Почта автора')
    text = models.TextField(max_length=3000, verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    status = models.CharField(max_length=40, verbose_name='Status', default=STATUS_CHOICES[0][0], choices=STATUS_CHOICES)

    def __str__(self):
        return self.author