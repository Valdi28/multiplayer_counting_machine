from typing import Iterable, Optional
from django.db import models
from django.utils import timezone
import datetime

# Create your models here.



# class CustomUser(models.Model):
#     name = models.TextField(max_length=30)
#     password = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

class Seasons(models.Model):
    season_number = models.IntegerField(blank=False, null=False, unique=True)
    count = models.IntegerField(default=0)
    creation_date = models.DateTimeField(null=True, editable=False)

    # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)

    def save(self, *args, **kwargs):
        if(not self.pk):
            self.creation_date = timezone.now()
        
        return super(Seasons, self).save(*args, **kwargs)

    
    def __str__(self):
        return f"Season {self.season_number}"