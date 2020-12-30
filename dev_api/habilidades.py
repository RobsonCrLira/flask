from flask_restful import Resource

habilidades = ['Python', 'Java', 'Flask', 'BI']


class Habilidades(Resource):
    def get(self):
        return habilidades