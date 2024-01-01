from django.db import models

# Create your models here.
class Todo(models):
    title = models.CharField(max_length=1000)
    is_complete = models.BooleanField(default=False)