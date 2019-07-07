from django.urls import path
from . import views
# serve images and files

urlpatterns = [
    path('', views.allblogs, name='allblogs'),
    path('<int:blog_id>/', views.detail, name='detail'),
]
