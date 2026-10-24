from fastapi import APIRouter
from routes.autores import router as autores_router
from routes.categorias import router as categorias_router
from routes.editoras import router as editoras_router
from routes.livros import router as livros_router
from routes.exemplares import router as exemplares_router
from routes.usuarios import router as usuarios_router
from routes.emprestimos import router as emprestimos_router

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(autores_router, prefix="/autores", tags=["Autores"])
api_router.include_router(categorias_router, prefix="/categorias", tags=["Categorias"])
api_router.include_router(editoras_router, prefix="/editoras", tags=["Editoras"])
api_router.include_router(livros_router, prefix="/livros", tags=["Livros"])
api_router.include_router(exemplares_router, prefix="/exemplares", tags=["Exemplares"])
api_router.include_router(usuarios_router, prefix="/usuarios", tags=["Usuários"])
api_router.include_router(emprestimos_router, prefix="/emprestimos", tags=["Empréstimos"])