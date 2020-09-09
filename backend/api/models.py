from django.db import models
from classifier import SentimentClassifier


class Text(models.Model):
    author = models.CharField(max_length=60)
    content = models.TextField()

    objects = models.Manager()

    def get_sentiment(self):
        clf = SentimentClassifier()
        return clf.predict(self.content)

    def __str__(self):
        return self.content
