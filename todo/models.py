from django.db import models

class TodoItem(models.Model):
    name = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now_add=True)
    priority = models.IntegerField(default=0)
    done = models.BooleanField(default=False)
