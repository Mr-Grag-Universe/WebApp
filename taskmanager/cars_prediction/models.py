from django.db import models
from django.forms import ChoiceField, Select


class Car(models.Model):
    NAMES = [
        (1, "bmw"),
        (2, "honda"),
    ]
    # name = models.CharField('Название', max_length=50, choices=NAMES, default='ражавое корыто')
    mark = models.CharField('Марка машины', max_length=250)
    # text = models.TextField('Статья')
    # data = models.DateTimeField('Дата публикации')
    # name = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    mileage = models.CharField(max_length=50)
    # rent = models.CharField(max_length=50)
    box = models.BooleanField()
    drive = models.BooleanField()
    rul = models.BooleanField()
    condition = models.BooleanField()
    owners = models.CharField(max_length=50)
    PTS = models.BooleanField()
    # tamozna = models.BooleanField()
    # barter = models.BooleanField()
    V = models.CharField(max_length=50)
    P = models.CharField(max_length=50)
    toplivo = models.BooleanField()
    # garant = models.BooleanField(max_length=50)

    def __str__(self):
        pass
        return self.mileage

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'
