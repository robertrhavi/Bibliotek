
from crud_base import CRUD
from models.autor import AutorModel
from models.categoria import CategoriaModel
from models.editora import EditoraModel
from models.emprestimo import EmprestimoModel
from models.exemplar import ExemplarModel
from models.livro import LivroModel
from models.usuario import UsuariosModel

crud_autor = CRUD(AutorModel)
crud_categoria = CRUD(CategoriaModel)
crud_editora = CRUD(EditoraModel)
crud_exemplar = CRUD(ExemplarModel)
crud_livro = CRUD(LivroModel)
crud_usuario = CRUD(UsuariosModel)
crud_emprestimo = CRUD(EmprestimoModel)