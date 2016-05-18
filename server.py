import os
import sys
import bottle
import json
from xml_utils import serialize_xml
from bottle import route, template, static_file, run, request, response
from models import session, Aluno

def serializer(accept, data, alias='root', element='element'):
    if 'xml' in accept:
        response.content_type = 'application/xml; charset=utf-8'
        return serialize_xml(data, alias=alias, element=element)
    response.content_type = 'application/json; charset=utf-8'
    return json.dumps(data)

@route('/',['GET'])
def index():
    return template('index.html')

@route('/alunos',['GET'])
def alunos():
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
    accept = request.GET.get('format') or request.headers.get('Accept')
    query = session.query(Aluno)
    if request.GET.get('aluno'):
        filtro = int( request.GET.get('aluno') )
        query = query.filter(Aluno.aluno==(filtro))
    if request.GET.get('nome'):
        filtro = request.GET.get('nome')
        query = query.filter(Aluno.nome.like('%'+filtro+'%'))
    registros = query.all()
    lista = []
    for item in registros:
        lista.append( item.columns_to_dict() )
    return serializer(accept, lista, alias='alunos', element='aluno')

@route('/static/<arquivo:path>')
def static(arquivo):
    return static_file(arquivo, 'static')

if __name__ == '__main__':
    run(host='0.0.0.0', port=8000, debug=True)

app = bottle.default_app()