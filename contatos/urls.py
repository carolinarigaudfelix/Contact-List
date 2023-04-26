from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'), #página principal
    path('busca/', views.busca, name = 'busca'),
    path('<int:contato_id>', views.ver_contato, name = 'ver_contato'),
]


