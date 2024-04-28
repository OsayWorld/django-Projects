from django.contrib import admin
from django.urls import path, include
from osay import views  # Import views module

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('osay.urls')),  # Include your app's URLs
]
