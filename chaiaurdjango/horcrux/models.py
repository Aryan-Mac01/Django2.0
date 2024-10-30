from django.db import models
from django.utils import timezone

# Create your models here.

class ChaiVariety(models.Model):
    CHAI_TYPE_CHOICE = [
        ('ML', 'MASALA'),
        ('GR', 'GINGER'),
        ('PL', 'PLAIN'),
        ('KL', 'KIWI'),
        ('EL', 'ELAICHI')
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='horcrux/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)
    description = models.TextField(default='')
    pricing = models.IntegerField(default=0)

    

    def __str__(self):
        return self.name
