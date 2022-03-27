from django.contrib import admin
from django.urls import path
from carApp import views
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('IdealWeight',views.IdealWeight)
]