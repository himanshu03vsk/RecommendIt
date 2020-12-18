from django.db import models

# Create your models here.
class Submit(models.Model):
    """
    docstring
    """
    genre = models.CharField(max_length=200, null= True, blank=True)
    Release_year =models.CharField(max_length=50)
    rating = models.IntegerField()
    cast = models.CharField(max_length=40)

    def __str__(self):
        return self.cast
