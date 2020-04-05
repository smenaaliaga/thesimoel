from django.contrib import admin
from django.urls import path
from sitioweb.views import home
from django.conf.urls.static import static

urlpatterns = [
    path('', home),
    path('skynet/', admin.site.urls),
]
