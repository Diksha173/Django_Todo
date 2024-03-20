from django.db import models

# Create your models here.
class Todo(models.Model):
    sno = models.IntegerField(primary_key=True)
    title=models.CharField(max_length=50)
    des=models.CharField(max_length=100)