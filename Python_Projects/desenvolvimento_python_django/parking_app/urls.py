from django.urls import path

#O arquivo views.py manipula quais urls queremos exibir ao nosso cliente
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:carro_id>', views.carro, name='carro')
]