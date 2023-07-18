from sqlalchemy import Column, String, Float
from app.factories.database import Base


class PontoTuristico(Base):
    __tablename__ = 'ponto_turistico'

    nome = Column(String, primary_key=True, index=True)
    endereco = Column(String)
    nota = Column(Float)
    descricao = Column(String)
    instrucoes = Column(String)
    preco = Column(Float)
    nivel_dificuldade = Column(Float)
    tipo_atividade = Column(String)
    url_video = Column(String)
    url_local_info = Column(String)
