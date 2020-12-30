from flask import Flask, jsonify, request
import json

app = Flask(__name__)

developers = [
    {'id': '0',
     'nome': 'Robson',
     'habilidade': ['Python', 'Java']
     },
    {'id': '1',
     'nome': 'Lucas',
     'habilidade': ['Python', 'BI']}
]


@app.route('/dev/<int:id>/', methods=['GET', 'PUT','DELETE'])
def developer(id):

    if request.method == 'GET':
        try:
            response = developer = developers[id]
        except IndexError:
            mensagem = f'Desenvolvedor de {id} não encontrado'
            response = {'status': 'Erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro descoconhecido. Contate o Administrador da API'
            response = {'status': 'Erro', 'mensagem': mensagem}
        return jsonify(response)

    elif request.method == 'PUT':
        dados = json.loads(request.data)
        developers[id] = dados
        return jsonify(dados)

    elif request.method == 'DELETE':
        developers.pop(id)
        return jsonify({'status': 'Sucess', 'mensagem': 'Registro deletado'})

#Inserir um novo dev e consultar todos devs
@app.route('/dev/', methods=['POST', 'GET'])
def list_developer():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(developers)
        dados['id'] = posicao
        developers.append(dados)
        return jsonify(developers[posicao])

    elif request.method == 'GET':
        return jsonify(developers)


if __name__ == '__main__':
    app.run(debug=True)
