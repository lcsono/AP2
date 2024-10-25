# main.py
from db_config import SessionLocal, Base, engine
from crud import criar_usuario,  criar_projeto, criar_tarefa
from secao import login,  usuario_logado

Base.metadata.create_all(bind=engine)

def main():
    db = SessionLocal()
    while True:
        print("\n--- Gerenciamento de Tarefas ---")
        # print("1. Login")
        print("2. Criar Usuário")
        print("3. Criar Projeto")
        print("4. Criar Tarefa")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            email = input("Digite seu email: ")
            login(db, email)
        
        elif escolha == "2":
            nome = input("Nome: ")
            email = input("Email: ")
            resultado = criar_usuario(db, nome, email)
            print(resultado["message"])
        
        elif escolha == "3":
            # if usuario_logado == True:
                titulo = input("Título do Projeto: ")
                descricao = input("Descrição: ")
                criador_id = input("ID do Usuário a ser vinculado: ")
                resultado = criar_projeto(db, titulo, descricao, criador_id) #, usuario_logado.id
                print(resultado["message"])
            # else:
            #     print("Erro: Você precisa estar logado para criar um projeto.")
        
        elif escolha == "4":
            # if usuario_logado:
                titulo = input("Título da Tarefa: ")
                descricao = input("Descrição: ")
                projeto_id = int(input("ID do Projeto: "))
                usuario_id = int(input("ID do Usuário a ser vinculado: "))
                resultado = criar_tarefa(db, titulo, descricao, projeto_id, usuario_id) #, usuario_logado.id
                print(resultado["message"])
            # else:
            #     print("Erro: Você precisa estar logado para criar uma tarefa.")

if __name__ == "__main__":
    main()
