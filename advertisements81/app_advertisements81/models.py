from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth import get_user_model

User = get_user_model()

class Advertisements81(models.Model):
    title = models.CharField('Заголовок', max_length=128)# максимум 128 символов
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('Торг', help_text='Отметьте возможен ли торг')
    bu = models.BooleanField('б/у', default=False,help_text='Был ли товар в бывшем использовании')
    created_time = models.DateTimeField(auto_now_add= True) # при создании (1 раз)
    updated_time = models.DateTimeField(auto_now= True) # при изменении (много раз)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    image = models.ImageField('Изображение', upload_to='advertisements/')

    @admin.display(description='Дата создания')
    def created_date(self):
        from django.utils import timezone
        if self.created_time.date() == timezone.now().date():
            created_time_2 = self.created_time.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: green; font-weight: bold;">Сегодня в {}</span>', created_time_2
            )
        return self.created_time.strftime('%d.%m.%Y в %H:%M:%S')

    def __str__(self):
        return f'Advertisements81(id={self.id}, title={self.title}, price={self.price})'

    @admin.display(description='Дата последнего обновления')
    def updated_date(self):
        from django.utils import timezone
        if self.updated_time.date() == timezone.now().date():
            updated_time_2 = self.updated_time.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: green; font-weight: bold;">Сегодня в {}</span>', updated_time_2
            )
        return self.updated_time.strftime('%d.%m.%Y в %H:%M:%S')

    def __str__(self):
        return f'Advertisements81(id={self.id}, title={self.title}, price={self.price})'

    class Meta:
        db_table = 'advertisements'

