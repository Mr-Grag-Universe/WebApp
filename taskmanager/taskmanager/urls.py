from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('news', include('news.urls')),
    path('prediction', include('cars_prediction.urls')),
]