import uvicorn
from fastapi import FastAPI

from factories.database import engine
from postgresqlRepositorios import models
from postgresqlRepositorios.PontoTuristicoRepositorio import (
    PontoTuristicoRepositorio,
)
from rotas.PontoTuristicoRotas import PontoTuristicoRotas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
ponto_turistico_repositorio = PontoTuristicoRepositorio()

ponto_turistico_rotas = PontoTuristicoRotas(
    ponto_turistico_repositorio=ponto_turistico_repositorio
)
app.include_router(ponto_turistico_rotas.router)

# TODO README
# TODO DOCKERFILE
# TODO CONFIGURAR ENV VARS
# TODO ADD REPOSITÓRIO GITHUB

if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)
