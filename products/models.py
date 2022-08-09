from django.db import models

# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=25)
    price       = models.DecimalField(decimal_places=2,max_digits=9)
    description = models.TextField()
    active      = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.title}'



