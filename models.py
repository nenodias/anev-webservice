# *-* coding: utf-8 *-*
import hashlib
from datetime import datetime, date

from sqlalchemy import Table, Column, Integer, String, Date, DateTime, Boolean, BigInteger, Numeric, Enum, ForeignKey, UniqueConstraint, Text
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.ext.declarative import declarative_base

''' Session '''
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool

''' Meta '''
from sqlalchemy.schema import MetaData

Base = declarative_base()
engine = create_engine('sqlite:///banco.sqlite')
Session = sessionmaker(bind=engine)

session = Session()

class Aluno(Base):
    __tablename__ = 'alunos'

    aluno = Column(Integer, primary_key=True)
    nome = Column(String)
    cpf = Column(String)
    rg = Column(String)
    data_nasc = Column(Date() )
    
    def columns_to_dict(self):
        dict_ = {}
        for key in self.__mapper__.c.keys():
            value = getattr(self, key)
            if isinstance(value, date):
                value = value.strftime('%d/%m/%Y')
            dict_[key] = value
        return dict_

Base.metadata.create_all(engine)

if __name__ == '__main__':
    Base.metadata.create_all(engine)