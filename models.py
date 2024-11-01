from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db_config import Base

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nome = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=True)
    senha = Column(String, unique=True, nullable=False)

    tarefas = relationship("Tarefa", back_populates="usuario")
    projetos = relationship("Projeto", back_populates="criador")

class Projeto(Base):
    __tablename__ = 'projetos'

    id = Column(Integer, primary_key=True)
    titulo = Column(String, nullable=False)
    descricao = Column(String)
    id_usuario = Column(Integer, ForeignKey('usuarios.id'))

    criador = relationship("Usuario", back_populates="projetos")
    tarefas = relationship("Tarefa", back_populates="projeto")

class Tarefa(Base):
    __tablename__ = 'tarefas'

    id = Column(Integer, primary_key=True)
    titulo = Column(String, nullable=False)
    descricao = Column(String)
    status = Column(String, default="pendente")
    id_projeto = Column(Integer, ForeignKey('projetos.id'))
    id_usuario = Column(Integer, ForeignKey('usuarios.id'))

    projeto = relationship("Projeto", back_populates="tarefas")
    usuario = relationship("Usuario", back_populates="tarefas")
