from flask import Flask
from decouple import config as env

app = Flask(__name__)

from main import routes #Se nao carregar os arquivos de rotas aqui a aplicacao
# nao consegue identificar as rotas.