# crud.py
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from models import Usuario, Projeto, Tarefa

# Funções de Usuário
def criar_usuario(db: Session, nome: str, email: str, senha: str):
    try:
        usuario = Usuario(nome=nome, email=email, senha=senha)
        db.add(usuario)
        db.commit()
        db.refresh(usuario)
        return {"success": True, "message": "Usuário criado com sucesso!", "usuario": usuario}
    except SQLAlchemyError as e:
        db.rollback()
        return {"success": False, "message": f"Erro ao criar usuário: {str(e)}"}

def listar_usuarios(db: Session):
    try:
        usuarios = db.query(Usuario).all()
        return {"success": True, "usuarios": usuarios}
    except SQLAlchemyError as e:
        return {"success": False, "message": f"Erro ao listar usuários: {str(e)}"}

# Funções de Projeto
def criar_projeto(db: Session, titulo: str, descricao: str, id_usuario: int):
    try:
        projeto = Projeto(titulo=titulo, descricao=descricao, id_usuario=id_usuario)
        db.add(projeto)
        db.commit()
        db.refresh(projeto)
        return {"success": True, "message": "Projeto criado com sucesso!", "projeto": projeto}
    except SQLAlchemyError as e:
        db.rollback()
        return {"success": False, "message": f"Erro ao criar projeto: {str(e)}"}

# Funções de Tarefa
def criar_tarefa(db: Session, titulo: str, descricao: str, id_projeto: int, id_usuario: int):
    try:
        tarefa = Tarefa(titulo=titulo, descricao=descricao, id_projeto=id_projeto, id_usuario=id_usuario)
        db.add(tarefa)
        db.commit()
        db.refresh(tarefa)
        return {"success": True, "message": "Tarefa criada com sucesso!", "tarefa": tarefa}
    except SQLAlchemyError as e:
        db.rollback()
        return {"success": False, "message": f"Erro ao criar tarefa: {str(e)}"}
def listar_tarefas(db: Session):
    try:
        tarefas = db.query(Tarefa).all()
        return {"success": True, "tarefas": tarefas}
    except SQLAlchemyError as e:
        return {"success": False, "message": f"Erro ao listar tarefas: {str(e)}"}

def atualizar_tarefa(db: Session, tarefa_id: int, titulo: str = None, descricao: str = None): 
    try:
        tarefa = db.query(Tarefa).filter(Tarefa.id == tarefa_id).first()
        if tarefa:
            if titulo:
                tarefa.titulo = titulo
            if descricao:
                tarefa.descricao = descricao
            db.commit()
            db.refresh(tarefa)
            return {"success": True, "message": "Tarefa atualizada com sucesso!", "tarefa": tarefa}
        else:
            return {"success": False, "message": "Tarefa não encontrada."}
    except SQLAlchemyError as e:
        db.rollback()
        return {"success": False, "message": f"Erro ao atualizar tarefa: {str(e)}"}

def excluir_tarefa(db: Session, tarefa_id: int):
    try:
        tarefa = db.query(Tarefa).filter(Tarefa.id == tarefa_id).first()
        if tarefa:
            db.delete(tarefa)
            db.commit()
            return {"success": True, "message": "Tarefa excluída com sucesso!"}
        else:
            return {"success": False, "message": "Tarefa não encontrada."}
    except SQLAlchemyError as e:
        db.rollback()
        return {"success": False, "message": f"Erro ao excluir tarefa: {str(e)}"}