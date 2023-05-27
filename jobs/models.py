from django.db import models

# Create your models here.
class Jobs(models.Model):
    activity=models.CharField(max_length=100)
    description=models.TextField(max_length=100,null=True)

    def __str__(self):
        word = f'{self.activity}: {self.description}'
        return word