import json
from flask import *
from model.rodovia import Rodovia
from Service.service import ServiceRodovia
from Server.server import server

service = ServiceRodovia()
app = server.app


def cria_json(json_response):
    concessionaria = json_response.get('concessionaria')
    sp = json_response.get('sp')
    sentido = json_response.get('sentido')
    municipio = json_response.get('municipio')
    latitude = json_response.get('latitude')
    longitude = json_response.get('longitude')
    evento = json_response.get('evento')
    return Rodovia(None, concessionaria, sp, sentido, municipio, latitude, longitude, evento)


@app.route('/rodovia', methods=['POST'])
def post_rodovia():
    json_rod = request.get_json()
    rodovia = cria_json(json_rod)
    service.create_rod(rodovia)
    return Response("Rodovia criada", status=201)


@app.route('/rodovia', methods=['GET'])
def get_rodovias():
    rodovia = service.find()
    return json.dumps(rodovia)


@app.route('/rodovia/<identi>', methods=['GET'])
def get_id(identi):
    rodovia = service.find_id(identi)
    return json.dumps(rodovia)


@app.route('/rodovia/update/<int:id>', methods=['PUT'])
def update_by_id(identi):
    json_rod = request.get_json()
    rodovia = cria_json(json_rod)
    service.update_by_id(rodovia, identi)
    return Response("Rodovia atualizada", status=201)


@app.route('/rodovia/del/<identi>', methods=['DELETE'])
def del_id(identi):
    service.delete_by_id(identi)
    return Response("Rodovia deletada", status=201)
