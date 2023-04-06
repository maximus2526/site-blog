from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('solo-page/', views.solo_page, name='solo-page'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
]
