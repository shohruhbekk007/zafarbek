from django.urls import path
from .views import HomePage, TestViews, PdfViews, VideosViews


urlpatterns = [
    path('', HomePage, name='home'),
    path('api/list/videos', VideosViews.as_view(), name='videos'),
    path('api/list/Pdf', PdfViews.as_view(), name='Pdf'),
    path('api/list/test', TestViews.as_view(), name='test'),
]
