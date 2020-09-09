from rest_framework import viewsets
from .serializers import TextSerializer
from .models import Text


class TextViewSet(viewsets.ModelViewSet):
    queryset = Text.objects.all().order_by('author')
    for text in queryset:
        print(f'Text: {text.content}, Prediction: {text.get_sentiment()}')
    serializer_class = TextSerializer
