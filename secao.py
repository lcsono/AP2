from sqlalchemy.orm import Session
from models import Usuario

usuario_logado = None  # Variável global para rastrear a sessão

def login(db: Session, nome: str):
    global usuario_logado
    usuario = db.query(Usuario).filter(Usuario.nome == nome).first()
    if usuario:
        usuario_logado = True
        print(f"Bem-vindo, {usuario.nome}!")
    else:
        print("Usuário não encontrado, por favor faça o cadastre...")
    return usuario_logado

def logout():
    global usuario_logado
    usuario_logado = None
    print("Logout realizado com sucesso.")
