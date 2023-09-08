from rest_framework import serializers
from .models import Pessoa
class PessoaSerializer(serializers.ModelSerializer):
    ## Converte uma classe models em json, para ser entregue
    class Meta:
        model = Pessoa
        fields = (
            'id',
            'nome',
            'sobrenome',
            'data_nascimento',
            'cpf'
        )
