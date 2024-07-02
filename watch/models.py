from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class BestSelling(models.Model):
    frontImg = models.ImageField(upload_to='bestselling')
    backImg = models.ImageField(upload_to='bestselling')
    brand = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    rating = models.DecimalField(validators=[MinValueValidator(0),
                                       MaxValueValidator(5)],max_digits=3, decimal_places=1)
    
    def __str__(self) -> str:
        return self.title