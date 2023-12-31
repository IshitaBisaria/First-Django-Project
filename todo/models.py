from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    completed = models.BooleanField(False)

    def __str__(self):
        return self.title
