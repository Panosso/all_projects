from django.urls import path, include
from .views import home, cadastro_pessoas, cadastro_veiculos, rot_hora

urlpatterns = [
    path('', home, name="core_home"),
    path('cadastros', cadastro_pessoas, name="pessoas"),
    path('veiculos', cadastro_veiculos, name="veiculos"),
    path('rothora', rot_hora, name="rotativos_hora"),
]
