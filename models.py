# *-* coding: utf-8 *-*
from datetime import date

from sqlalchemy import  Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

''' Session '''
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()
engine = create_engine('sqlite:///banco.sqlite')
Session = sessionmaker(bind=engine)

session = Session()

class Aluno(Base):
    __tablename__ = 'alunos'

    aluno = Column('aluno',Integer, primary_key=True)
    nome = Column('nome',String)
    cpf = Column('cpf',String)
    rg = Column('rg',String)
    data_Nascimento = Column('data_nasc',Date() )
    
    def columns_to_dict(self):
        dict_ = {}
        for key in self.__mapper__.c.keys():
            value = getattr(self, key)
            if isinstance(value, date):
                value = value.strftime('%d/%m/%Y')
            dict_[key] = value
        return dict_

if __name__ == '__main__':
    Base.metadata.create_all(engine)