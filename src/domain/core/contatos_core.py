from src.domain.settings.base_settings import Base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import ForeignKey


class Contatos(Base):
    __tablename__ = 'contatos'

    id_contatos: Mapped[int] = mapped_column(primary_key=True, unique=True)
    nome_contato: Mapped[str] = mapped_column(String(60), unique=True)
    telefone: Mapped[str] = mapped_column(String(15))
    email: Mapped[str] = mapped_column(String(100))
    id_cliente: Mapped[int] = mapped_column(Integer, ForeignKey("clientes.id",
                                                                ondelete='CASCADE'))
    cliente = relationship('Clientes',
                           back_populates='contatos')

    def __init__(self, nome_contato, telefone, email):
        super().__init__()
        self.nome_contato = nome_contato
        self.telefone = telefone
        self.email = email

    def __repr__(self):
        return f"Contatos < ID = {self.id_contatos}, " \
               f"Nome = {self.nome_contato}," \
               f"Telefone = {self.telefone}," \
               f"Email = {self.email}, " \
               f"FK_clientes = {self.id_cliente}>"
