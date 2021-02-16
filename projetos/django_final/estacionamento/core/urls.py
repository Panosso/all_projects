from django.urls import path, include
from .views import (home,
                    cadastro_pessoas,
                    cadastro_pessoa,
                    cadastro_veiculos,
                    rot_hora,
                    rot_mes,
                    cadastro_novo,
                    novo_veiculo,
                    mov_rot_hora,
                    mov_rot_mes
                    )

urlpatterns = [
    path('', home, name="core_home"),
    path('cadastros', cadastro_pessoas, name="pessoas"),
    path('cadastro/<int:id_cadastro>', cadastro_pessoa, name="pessoas"),
    path('cadastros_novo', cadastro_novo, name="pessoas_novo"),
    path('veiculos', cadastro_veiculos, name="veiculos"),
    path('veiculo_novo', novo_veiculo, name="veiculo_novo"),
    path('rothora', rot_hora, name="rotativos_hora"),
    path('mov_rot_hora', mov_rot_hora, name="mov_rot_hora"),
    path('rotmes', rot_mes, name="rotativos_mes"),
    path('mov_rot_mes', mov_rot_mes, name="mov_rot_mes"),
]
