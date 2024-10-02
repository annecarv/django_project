from django.forms import ModelForm
from .models import Servico, CategoriaManutencao

class FormServico(ModelForm): #herança
    class Meta:
        model = Servico
        exclude = ['finalizado', 'protocolo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) ##referenciando a classe pai

        self.fields['titulo'].widget.attrs.update({'placeholder': 'Título'})
        self.fields['data_inicio'].widget.attrs.update({'placeholder': 'Data Início'})
        self.fields['data_entrega'].widget.attrs.update({'placeholder': 'Data Entrega'})

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'}) ##chaves do dicionário

        choices = list()
        for i,j in self.fields['categoria_manutencao'].choices:
            categoria = CategoriaManutencao.objects.get(titulo=j)
            choices.append((i.value, categoria.get_titulo_display()))

        self.fields['categoria_manutencao'].choices=choices