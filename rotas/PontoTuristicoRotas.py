from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from factories.database import SessionLocal
from modelos.PontoTuristico import PontoTuristico
from repositorios.PontoTuristicoRepositorio import PontoTuristicoRepositorio


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class PontoTuristicoRotas:
    ponto_turistico_repositorio: PontoTuristicoRepositorio
    router: APIRouter = APIRouter()

    def __init__(self, ponto_turistico_repositorio):
        self.ponto_turistico_repositorio = ponto_turistico_repositorio
        self.router.add_api_route(
            '/local/{nome_local}', self.get_ponto_turistico, methods=['GET']
        )
        self.router.add_api_route(
            '/local', self.insert_ponto_turistico, methods=['POST']
        )
        self.router.add_api_route(
            '/local', self.update_ponto_turistico, methods=['PUT']
        )
        self.router.add_api_route(
            '/locais', self.lista_todos_pontos_turisticos, methods=['GET']
        )
        self.router.add_api_route(
            '/local/{nome_local}',
            self.delete_ponto_turistico,
            methods=['DELETE'],
            status_code=204
        )

    def get_ponto_turistico(
        self, nome_local: str, db: Session = Depends(get_db)
    ):
        return self.ponto_turistico_repositorio.get_ponto_turistico(
            db, nome_local
        )

    def insert_ponto_turistico(
        self, ponto_turistico: PontoTuristico, db: Session = Depends(get_db)
    ):
        return self.ponto_turistico_repositorio.insert_ponto_turistico(
            db, ponto_turistico
        )

    def lista_todos_pontos_turisticos(self, db: Session = Depends(get_db)):
        return self.ponto_turistico_repositorio.lista_todos_pontos_turisticos(
            db
        )

    def update_ponto_turistico(
        self, ponto_turistico: PontoTuristico, db: Session = Depends(get_db)
    ):
        return self.ponto_turistico_repositorio.update_ponto_turistico(
            db, ponto_turistico=ponto_turistico
        )

    def delete_ponto_turistico(
        self, nome_local: str, db: Session = Depends(get_db)
    ):
        return self.ponto_turistico_repositorio.delete_ponto_turistico(
            db, nome_local
        )
