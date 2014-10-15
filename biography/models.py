from django.db import models

# Create your models here.

class Biography(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    career=models.CharField(max_length=255)
    description=models.CharField(max_length=255)

    def __str__(self):
        return self.name