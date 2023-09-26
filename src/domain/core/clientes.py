from src.domain.settings.base_settings import Base
from sqlalchemy.orm import Mapped, mapped_column
from src.domain.core.contatos import Contatos
from sqlalchemy.orm import relationship
from sqlalchemy import String, Date
from datetime import date
from typing import List


class Clientes(Base):
    __tablename__ = 'clientes'

    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    nome: Mapped[str] = mapped_column(String(30), unique=True)
    telefone: Mapped[str] = mapped_column(String(15))
    cpf: Mapped[str] = mapped_column(String(20), unique=True)
    endereco: Mapped[str] = mapped_column(String(100))
    data_nascimento: Mapped[date] = mapped_column(Date)
    contatos: Mapped[List['Contatos']] = relationship('Contatos',
                                                      cascade="all, delete-orphan",
                                                      back_populates="cliente", )

    def __init__(self, nome, telefone, cpf, endereco, data_nascimento):
        super().__init__()
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf
        self.endereco = endereco
        self.data_nascimento = data_nascimento

    def __repr__(self) -> str:
        return f"Cliente < ID = {self.id}, " \
               f"Nome completo = {self.nome}," \
               f" Telefone = {self.telefone}," \
               f" CPF = {self.cpf}" \
               f" Endereco = {self.endereco}," \
               f" Data de nascimento = {self.data_nascimento}>" \
               f"\n"