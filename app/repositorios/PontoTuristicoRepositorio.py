from sqlalchemy.orm import Session

from app.modelos import PontoTuristico


class PontoTuristicoRepositorio:
    def get_ponto_turistico(self, db: Session, nome_local: str):
        raise NotImplemented

    def insert_ponto_turistico(
        self, db: Session, ponto_turistico: PontoTuristico
    ):
        raise NotImplemented

    def lista_todos_pontos_turisticos(self, db: Session):
        raise NotImplemented

    def update_ponto_turistico(
        self, db: Session, ponto_turistico: PontoTuristico
    ):
        raise NotImplemented

    def delete_ponto_turistico(self, db: Session, nome_local: str):
        raise NotImplemented
