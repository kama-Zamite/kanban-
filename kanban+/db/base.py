 # Sessão e conexão à Base de Dados
from sqlalchemy.orm import (
    DeclarativeBase, MappedAsDataclass
)

class Base(DeclarativeBase, MappedAsDataclass):
    pass