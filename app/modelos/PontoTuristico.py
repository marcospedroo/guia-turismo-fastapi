from pydantic import BaseModel, HttpUrl

# from app.modelos.Videos import Videos
# from app.modelos.Fotos import Fotos


class PontoTuristico(BaseModel):
    nome: str
    endereco: str | None
    nota: float | None
    descricao: str | None
    instrucoes: str | None
    preco: str | None
    nivel_dificuldade: float | None
    tipo_atividade: str | None
    url_local_info: HttpUrl | None
    # fotos: list[Fotos] | None = []
    # videos: list[Videos] | None = []

    class Config:
        orm_mode = True
