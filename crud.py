# crud.py
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from models import Usuario, Projeto, Tarefa

# Funções de Usuário
def criar_usuario(db: Session, nome: str, email: str):
    try:
        usuario = Usuario(nome=nome, email=email)
        db.add(usuario)
        db.commit()
        db.refresh(usuario)
        return {"success": True, "message": "Usuário criado com sucesso!", "usuario": usuario}
    except SQLAlchemyError as e:
        db.rollback()
        return {"success": False, "message": f"Erro ao criar usuário: {str(e)}"}

# Funções de Projeto
def criar_projeto(db: Session, titulo: str, descricao: str, criador_id: int):
    try:
        projeto = Projeto(titulo=titulo, descricao=descricao, criador_id=criador_id)
        db.add(projeto)
        db.commit()
        db.refresh(projeto)
        return {"success": True, "message": "Projeto criado com sucesso!", "projeto": projeto}
    except SQLAlchemyError as e:
        db.rollback()
        return {"success": False, "message": f"Erro ao criar projeto: {str(e)}"}

# Funções de Tarefa
def criar_tarefa(db: Session, titulo: str, descricao: str, projeto_id: int, usuario_id: int):
    try:
        tarefa = Tarefa(titulo=titulo, descricao=descricao, projeto_id=projeto_id, usuario_id=usuario_id)
        db.add(tarefa)
        db.commit()
        db.refresh(tarefa)
        return {"success": True, "message": "Tarefa criada com sucesso!", "tarefa": tarefa}
    except SQLAlchemyError as e:
        db.rollback()
        return {"success": False, "message": f"Erro ao criar tarefa: {str(e)}"}


