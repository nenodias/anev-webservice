from xml.etree.ElementTree import Element, tostring

def dict_to_xml(tag, d):
    '''
    Turn a simple dict of key/value pairs into XML
    '''
    elem = Element(tag)
    for key, val in d.items():
        child = Element(key)
        child.text = str(val)
        elem.append(child)
    return elem

def serialize_xml(data, alias='root', element='element'):
    alunos = Element(alias)
    for item in data:
        alunos.append( dict_to_xml(element, item) )
    return tostring(alunos)