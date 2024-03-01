from rest_framework.generics import ListAPIView
from .models import Test, VideoFile, PDFFile
from .serializer import PdfFileSerializer, TestSerializer, VideoFileSerializer
from django.http import HttpResponse


def HomePage(request):
    return HttpResponse("Saparbayev Zafarbek")

class TestViews(ListAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    
    
class PdfViews(ListAPIView):
    queryset = PDFFile.objects.all()
    serializer_class = PdfFileSerializer
    
    
class VideosViews(ListAPIView):
    queryset = VideoFile.objects.all()
    serializer_class = VideoFileSerializer