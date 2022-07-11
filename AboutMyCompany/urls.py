
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('aboutme.urls')),
    path('', include('accounts.urls')),

]
