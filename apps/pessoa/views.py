from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Pessoa
from .serializers import PessoaSerializer
import json

@api_view(['GET'])
def index(request):
    try:
        pessoas = Pessoa.objects.all()
        filtro = None
        if request.data:
            filtro = filtros(request)
        if filtro:
            pessoas = pessoas.filter(**filtro)
        if pessoas:
            serializer = PessoaSerializer(pessoas, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response("Pessoa não cadastrada", status=status.HTTP_200_OK)
    except Exception as e:
        return Response("Erro ao buscar {}".format(e), status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_pessoa(request):
    try:
        dados = json.dumps(request.data[0])
        dados = json.loads(dados)
        serializer = PessoaSerializer(data=dados)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response("Falta dados para criar inserir pessoa", status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response("Erro ao buscas pessoa", status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_pessoa(request):
    try:
        dados = json.dumps(request.data[1])
        dados = json.loads(dados)
        filtro = filtros(request)
        if filtro:
            pessoa = Pessoa.objects.get(**filtro)
            if pessoa:
                pessoa.nome = dados.get('nome')
                pessoa.sobrenome = dados.get('sobrenome')
                pessoa.data_nascimento = dados.get('data_nascimento')
                pessoa.cpf = dados.get('cpf')
                pessoa.save()
                return Response("Atualizado com sucesso", status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response("Erro ao atualizar - Pessoa não encontrada - {}".format(e), status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_pessoa(request):
    try:
        filtro = None
        if request.data:
            filtro = filtros(request)
        if filtro:
            pessoa = Pessoa.objects.filter(**filtro)
            if pessoa:
                pessoa.delete()
                return Response("Deletado com sucesso", status=status.HTTP_200_OK)
            else:
                return Response("Pessoa não encontrada!")
        return Response("Ocorreu um erro ao deletar cliente", status=status.HTTP_200_OK)
    except:
        return Response("Erro ao Deletar", status=status.HTTP_400_BAD_REQUEST)

def filtros(request):
    # fields = {
    #     u'id',
    #     u'nome',
    #     u'sobrenome',
    #     u'data_nascimento',
    #     u'cpf'
    # }
    # filtros = {}
    data = json.dumps(request.data[0])
    data = json.loads(data)
    return data
    # for value in fields:
    #     val = request.data[0].get(value, None) or None
    #     if val:
    #         filtros[value] = val
    # return filtros

def filtro_id(request):
    fields = {
        u'id'
    }
    for value in fields:
        val = request.data[0].get(value, None) or None
        if val:
            filtros[value] = val
    return filtros