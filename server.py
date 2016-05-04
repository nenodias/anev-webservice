import bottle
import json
from xml_utils import serialize_xml
from bottle import route, template, static_file, run, request, response
from models import session, Aluno

def serializer(accept, data, alias='root', element='element'):
    print('xml' in accept)
    if 'xml' in accept:
        response.content_type = 'application/xml; charset=utf-8'
        return serialize_xml(data, alias=alias, element=element)
    response.content_type = 'application/json; charset=utf-8'
    return json.dumps({alias:data})

@route('/',['GET'])
def index():
    return template('template/index.html')

@route('/alunos',['GET'])
def alunos():
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
        print(item.columns_to_dict())
        lista.append( item.columns_to_dict() )
    return serializer(accept, lista, alias='alunos', element='aluno')

@route('/static/<arquivo:path>')
def static(arquivo):
    return static_file(arquivo, 'static')

if __name__ == '__main__':
    run(host='localhost', port=8001, debug=True)