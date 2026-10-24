# src/models/__init__.py

from models.autor import AutorModel
from models.categoria import CategoriaModel
from models.editora import EditoraModel
from models.emprestimo import EmprestimoModel
from models.exemplar import ExemplarModel
from models.livro import LivroModel
from models.livro_autor import LivroAutorModel
from models.usuario import UsuariosModel

__all__ = [
    "AutorModel",
    "CategoriaModel",
    "EditoraModel",
    "EmprestimoModel",
    "ExemplarModel",
    "LivroModel",
    "LivroAutorModel",
    "UsuariosModel",
]