# main.py
from db_config import SessionLocal, Base, engine
from crud import criar_usuario,  criar_projeto, criar_tarefa, listar_tarefas, atualizar_tarefa, excluir_tarefa
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
        print("5. Listar Tarefas")
        print("6. Atualizar Tarefa")
        print("7. Excluir Tarefa")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            email = input("Digite seu email: ")
            login(db, email)
        
        elif escolha == "2":
            nome = input("Digite o seu Nome: ")
            email = input("Digite o seu melhor Email: ")
            senha = input("Digite uma senha: ")
            resultado = criar_usuario(db, nome, email, senha)
            print(resultado["message"])
        
        elif escolha == "3":
            titulo = input("Título do Projeto: ")
            descricao = input("Descrição: ")
            criador_id = int(input("ID do Usuário a ser vinculado: "))
            resultado = criar_projeto(db, titulo, descricao, criador_id)
            print(resultado["message"])
        
        elif escolha == "4":
            titulo = input("Título da Tarefa: ")
            descricao = input("Descrição: ")
            id_projeto = int(input("ID do Projeto: "))
            id_usuario = int(input("ID do Usuário a ser vinculado: "))
            resultado = criar_tarefa(db, titulo, descricao, id_projeto, id_usuario)
            print(resultado["message"])
        
        elif escolha == "5":
            resultado = listar_tarefas(db)
            if resultado["success"]:
                for tarefa in resultado["tarefas"]:
                    print(f"Tarefa ID: {tarefa.id}, Título: {tarefa.titulo}, Descrição: {tarefa.descricao}, Status: {tarefa.status}")
            else:
                print(resultado["message"])
        
        elif escolha == "6":
            tarefa_id = int(input("ID da Tarefa que será atualizada: ")) #
            novo_titulo = input("Novo Título (deixar em branco pra não alterar): ") #
            novo_descricao = input("Nova Descrição (deixar em branco pra não alterar): ") #
            resultado = atualizar_tarefa(db, tarefa_id, novo_titulo or None, novo_descricao or None) #
            print(resultado["message"])
        
        elif escolha == "7":
            tarefa_id = int(input("ID da Tarefa a ser excluída: "))
            resultado = excluir_tarefa(db, tarefa_id)
            print(resultado["message"]) #
        
        elif escolha == "8":
            print("Saindo...")
            break
        
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
