from rest_framework import viewsets
from .serializers import TextSerializer
from .models import Text


class TextViewSet(viewsets.ModelViewSet):
    queryset = Text.objects.all().order_by('author')
    for text in queryset:
        print(text)
    serializer_class = TextSerializer
