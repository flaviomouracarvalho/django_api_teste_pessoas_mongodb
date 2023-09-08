# Projeto Django com Banco de Dados MongoDB - Novas Tecnologia para Banco de Dados

Este é um projeto Django que utiliza o banco de dados MongoDB como armazenamento de dados. Abaixo, você encontrará informações sobre como configurar o ambiente de desenvolvimento, instalar as dependências necessárias e exemplos de consultas usando o Postman.

## Configuração do Ambiente

Certifique-se de ter o Python instalado em seu sistema. Recomenda-se o uso de um ambiente virtual para isolar as dependências do projeto. Siga os passos abaixo para configurar o ambiente:

1. Clone este repositório:
    https://github.com/flaviomouracarvalho/django_api_teste_pessoas_mongodb.git
    * cd nome-projeto
2. Crie e ative um ambiente virtual (opcional, mas recomendado):
    * Ex:
    python -m venv venv
source venv/bin/activate # No Windows: venv\Scripts\activate

3. Instale as dependências do projeto:
   * pip install -r requirements.tx

4. Configure as variáveis de ambiente necessárias, como as credenciais do MongoDB, em um arquivo `.env`. Você pode copiar o arquivo `.env.example` e preencher as informações necessárias.

5. Execute as migrações do Django para criar as tabelas no MongoDB:
   * python3.x manage.py makemigrations
   * python3.x manage.py migrate

6. Inicie o servidor de desenvolvimento:


Agora, seu ambiente de desenvolvimento está configurado e o servidor está em execução.

## Dependências

- asgiref==3.7.2
- Django==4.0.1
- djangorestframework==3.14.0
- djongo==1.3.6
- dnspython==2.4.2
- pymongo==4.5.0
- python-decouple==3.8
- pytz==2023.3
- sqlparse==0.2.4
- typing_extensions==4.7.1

## Exemplos de Consultas usando o Postman

Você pode importar os exemplos de consultas no formato Postman JSON fornecidos neste projeto para testar as APIs. Certifique-se de ter o Postman instalado em seu sistema.

1. Abra o Postman.

2. Clique em "Import" e selecione os arquivos de coleção JSON no diretório `postman-examples`.

3. Agora você terá as consultas de exemplo importadas. Você pode executar essas consultas para interagir com as APIs do projeto.

## Link de exemplo de teste da API
https://documenter.getpostman.com/view/26816632/2s9YC1VtvB 

