from django.contrib import admin
from django.urls import path
from sitioweb.views import home, about, contact
from django.conf.urls.static import static

urlpatterns = [
    path('', home),
    path('about/', about),
    path('contact/', contact),
    path('skynet/', admin.site.urls),
]
