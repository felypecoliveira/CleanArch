from src.infra.db.base_settings import Base
from src.domain.entities.contatos import Contatos
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Date, Integer
from sqlalchemy.orm import relationship
from datetime import date
from typing import List


class Clientes(Base):
    __tablename__ = 'clientes'

    id: Mapped[int] = mapped_column(Integer,primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    telefone: Mapped[str] = mapped_column(String(15), nullable=False)
    cpf: Mapped[str] = mapped_column(String(20), unique=True,nullable=False)
    endereco: Mapped[str] = mapped_column(String(100))
    data_nascimento: Mapped[date] = mapped_column(Date,nullable=False)
    contatos: Mapped[List["Contatos"]] = relationship("Contatos",
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
        return f"Cliente < ID = {self.id}, Nome completo = {self.nome}," \
               f" Telefone = {self.telefone}," \
               f" CPF = {self.cpf}" \
               f" Endereco = {self.endereco}," \
               f" Data de nascimento = {self.data_nascimento}>" \



