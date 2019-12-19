from django.urls import path
from web import views
urlpatterns = [
    path('index/', views.index),
    path('index/check', views.check),
    path('index/index', views.index),

]