from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.ver_webtoon, name='ver_webtoon'),
    path('agregar/', views.agregar_webtoon, name='agregar_webtoon'),
    path('editar/<int:id>/', views.editar_webtoon, name='editar_webtoon'),
    path('eliminar/<int:id>/', views.eliminar_webtoon, name='eliminar_webtoon'),
]
