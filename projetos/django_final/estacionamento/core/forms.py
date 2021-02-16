from django.forms import ModelForm
from .models import Pessoa, Veiculo, MovRotativoHora, MovRotativoMes

#Criado os forms que utilizamos no cadastro em suas respectivas paginas html
# as classes precisam dessa sebclasse 'Meta', pois nela que conseguimos pegar
# os tipos dos fields criados no model.

class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'


class VeiculoForm(ModelForm):
    class Meta:
        model = Veiculo
        fields = '__all__'

class MovRotHoraForm(ModelForm):
    class Meta:
        model = MovRotativoHora
        fields = '__all__'

class MovRotMesForm(ModelForm):
    class Meta:
        model = MovRotativoMes
        fields = '__all__'