from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import Habilidades
import json

app = Flask(__name__)
api = Api(app)
developers = [
    {'id': '0',
     'nome': 'Robson',
     'habilidade': ['Python', 'Java']
     },
    {'id': '1',
     'nome': 'Lucas',
     'habilidade': ['Python', 'BI']}
]


class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = developer = developers[id]
        except IndexError:
            mensagem = f'Desenvolvedor de {id} não encontrado'
            response = {'status': 'Erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro descoconhecido. Contate o Administrador da API'
            response = {'status': 'Erro', 'mensagem': mensagem}
        return response

    def put(self):
        pass

    def delete(self,id):
        developers.pop(id)
        return {'status': 'Sucess', 'mensagem': 'Registro deletado'}
        pass


class ListaDevelopers(Resource):
    def get(self):
        return developers

    def post(self):
        dados = json.loads(request.data)
        posicao = len(developers)
        dados['id'] = posicao
        developers.append(dados)
        return developers[posicao]


api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDevelopers, '/dev/')
api.add_resource(Habilidades, '/skill/')


if __name__ == '__main__':
    app.run(debug=True)
