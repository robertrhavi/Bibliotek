from pydantic import BaseModel, Field, ConfigDict

class BibliotecaCreate(BaseModel):
    nome: str = Field(min_legth=5, max_length = 30)

class BibliotecaUpdate(BaseModel):
    nome: str | None = Field(
        default=None,
        min_length=5,
        max_length=30
    )

class BibliotecaResponse(BaseModel):
    id: int
    nome: str
    model_config =  ConfigDict(from_atributes=True)