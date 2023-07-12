from pydantic import BaseModel, HttpUrl


class PontoTuristico(BaseModel):
    nome: str | None
    endereco: str | None
    nota: float | None
    descricao: str | None
    instrucoes: str | None
    preco: str | None
    nivel_dificuldade: float | None
    tipo_atividade: str | None
    url_video: HttpUrl | None
    url_local_info: HttpUrl | None

    class Config:
        orm_mode = True
