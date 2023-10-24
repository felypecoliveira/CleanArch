from src.domain.infra.db.base_settings import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String


class Contatos(Base):
    __tablename__ = 'contatos'

    id_contatos: Mapped[int] = mapped_column(Integer,primary_key=True, autoincrement=True)
    nome_contato: Mapped[str] = mapped_column(String(60), unique=True,nullable=False)
    telefone_contato: Mapped[str] = mapped_column(String(15),nullable=False)
    email: Mapped[str] = mapped_column(String(100))
    id_cliente: Mapped[int] = mapped_column(Integer, ForeignKey("clientes.id",
                                                                ondelete='CASCADE'))
    cliente = relationship('Clientes',
                           back_populates='contatos')

    def __init__(self, nome_contato, telefone, email):
        super().__init__()
        self.nome_contato = nome_contato
        self.telefone_contato = telefone
        self.email = email

    def __repr__(self):
        return f"Contatos < {self.id_contatos} nome = {self.nome_contato}," \
               f"telefone = {self.telefone_contato}," \
               f"email = {self.email}>"