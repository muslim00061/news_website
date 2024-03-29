from django.db import models
from datetime import datetime

class Post(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    image = models.CharField("Ссылка на изображения", max_length=788)
    description = models.TextField("Описание")
    post_date = models.DateTimeField("Дата публикации", default=datetime.now)

    def __str__(self):
        return self.title
