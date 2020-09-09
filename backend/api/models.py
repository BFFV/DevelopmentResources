from django.db import models


class Text(models.Model):
    author = models.CharField(max_length=60)
    content = models.TextField()

    objects = models.Manager()

    def __str__(self):
        return self.content
