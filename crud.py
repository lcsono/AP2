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

def listar_projetos(db: Session):
    try:
        projetos = db.query(Projeto).all()
        return {"success": True, "projetos": projetos}
    except SQLAlchemyError as e:
        return {"success": False, "message": f"Erro ao listar projetos: {str(e)}"}

# crud.py (Função de editar projeto)
def atualizar_projeto(db: Session, projeto_id: int, novo_titulo: str = None, nova_descricao: str = None):
    try:
        projeto = db.query(Projeto).filter(Projeto.id == projeto_id).first()
        if projeto:
            if novo_titulo:
                projeto.titulo = novo_titulo
            if nova_descricao:
                projeto.descricao = nova_descricao
            db.commit()
            db.refresh(projeto)
            return {"success": True, "message": "Projeto atualizado com sucesso!", "projeto": projeto}
        else:
            return {"success": False, "message": "Projeto não encontrado."}
    except SQLAlchemyError as e:
        db.rollback()
        return {"success": False, "message": f"Erro ao atualizar projeto: {str(e)}"}

# Funções de Tarefa
def criar_tarefa(db: Session, titulo: str, descricao: str, id_projeto: int, id_usuario: int, prioridade: int = 1):
    try:
        prioridades = {1: 'Baixa', 2: 'Média', 3: 'Alta'}
        
        if prioridade not in prioridades:
            return {"success": False, "message": "Prioridade inválida. Use 1 para Baixa, 2 para Média ou 3 para Alta."}
        
        tarefa = Tarefa(titulo=titulo, descricao=descricao, id_projeto=id_projeto, id_usuario=id_usuario, prioridade=prioridades[prioridade])
        
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


def atualizar_tarefa(db: Session, tarefa_id: int, titulo: str = None, descricao: str = None, status: str = None, prioridade: int = None): 
    try:
        tarefa = db.query(Tarefa).filter(Tarefa.id == tarefa_id).first()
        if tarefa:
            if titulo:
                tarefa.titulo = titulo
            if descricao:
                tarefa.descricao = descricao
            if status:
                status = status.capitalize()  
                if status in ['Pendente', 'Em andamento', 'Finalizada']:  
                    tarefa.status = status
                else:
                    return {"success": False, "message": "Status inválido."}
            if prioridade:
                prioridades = {1: 'Baixa', 2: 'Média', 3: 'Alta'}
                if prioridade in prioridades:
                    tarefa.prioridade = prioridades[prioridade]  # Prioridade é uma string, é ok atribuir diretamente
                else:
                    return {"success": False, "message": "Prioridade inválida. Use 1 para Baixa, 2 para Média ou 3 para Alta."}
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
