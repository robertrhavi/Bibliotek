from fastapi import APIRouter, HTTPException, status
from database import SessionDep
from crud import crud_autor
from schemas.autor import AutorCreate, AutorUpdate, AutorResponse

router = APIRouter()
