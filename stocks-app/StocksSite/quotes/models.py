from django.db import models

# Create your models here.
class Stock(models.Model):
    ticker=models.CharField(max_length=5)

    def __str__(self):
        return self.ticker