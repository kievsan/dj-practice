from django.db import models
from django.urls import reverse
from datetime import datetime


class Phone(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images', blank=True)
    release_date = models.DateField(default=datetime.now().strftime("%Y-%m-%d"))
    lte_exists = models.BooleanField(default=0)
    slug = models.SlugField(max_length=255, null=False, unique=True, blank=False)

    def get_absolute_url(self):
        return reverse('phone', kwargs={'slug': self.slug})

    class Meta:
        db_table = "Phone"  # сменить стандартное "имя проекта-имя класса" ( phones-phone )
