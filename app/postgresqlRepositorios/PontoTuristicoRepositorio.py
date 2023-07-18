from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

from app.modelos import PontoTuristico
from app.postgresqlRepositorios import models
from app.repositorios import (
    PontoTuristicoRepositorio as base_repositorio,
)
from sqlalchemy.orm import Session
from sqlalchemy import update, delete


class PontoTuristicoRepositorio(base_repositorio):
    def get_ponto_turistico(self, db: Session, nome_local: str):
        return (
            db.query(models.PontoTuristico)
            .filter(models.PontoTuristico.nome == nome_local)
            .first()
        )

    def insert_ponto_turistico(
        self, db: Session, ponto_turistico: PontoTuristico
    ):
        db_local = models.PontoTuristico(**ponto_turistico.dict())
        try:
            db.add(db_local)
            db.commit()
            db.refresh(db_local)
        except IntegrityError:
            raise HTTPException(
                status_code=400, detail='Erro ao inserir registro'
            )
        return ponto_turistico

    def lista_todos_pontos_turisticos(self, db: Session):
        return db.query(models.PontoTuristico).all()

    def update_ponto_turistico(
        self, db: Session, ponto_turistico: PontoTuristico
    ):
        try:
            ponto_turistico_dict = ponto_turistico.dict()
            ponto_turistico_dict_clean = {}
            for k, v in ponto_turistico_dict.items():
                if ponto_turistico_dict[k]:
                    ponto_turistico_dict_clean[k] = v

            query = (
                update(models.PontoTuristico)
                .where(models.PontoTuristico.nome == ponto_turistico.nome)
                .values(**ponto_turistico_dict_clean)
            )

            db.execute(query)
            db.commit()
        except IntegrityError:
            raise HTTPException(
                status_code=400, detail='Erro ao atualizar registro'
            )
        return ponto_turistico_dict_clean

    def delete_ponto_turistico(self, db: Session, nome_local: str):
        query = delete(models.PontoTuristico).where(
            models.PontoTuristico.nome == nome_local
        )
        db.execute(query)
        db.commit()
