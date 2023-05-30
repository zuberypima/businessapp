from django.db import models

# Create your models here.
class BatchNumber(models.Model):
    batch =models.CharField(max_length=255,unique=True)
    startDate =models.DateField()
    endDate =models.DateField()

    def __str__(self):
        return self.batch
    