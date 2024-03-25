
from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index),
    path("about/", views.About),
    path("first_app/", include("first_app.urls")),
]
