from django.db import models
from django.db.models.fields import DateTimeField

class Articles(models.Model):
    title = models.CharField('Title', max_length=50)
    anons = models.CharField('Anons', max_length=250)
    full_text = models.TextField('Article')
    date = models.DateTimeField('Date publication')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

