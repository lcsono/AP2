from db_config import SessionLocal, Base, engine
from crud import criar_usuario, criar_projeto, criar_tarefa, listar_tarefas, listar_usuarios, listar_projetos, atualizar_tarefa, excluir_tarefa
from secao import login, usuario_logado

Base.metadata.create_all(bind=engine)

def main():
    db = SessionLocal()
    while True:
        print("\n--- Gerenciamento de Tarefas ---")
        print("1. Criar Usuário")
        print("2. Listar Usuários")
        print("3. Criar Projeto")
        print("4. Listar Projetos")
        print("5. Criar Tarefa")
        print("6. Listar Tarefas")
        print("7. Atualizar Tarefa")
        print("8. Excluir Tarefa")
        print("9. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Digite o seu Nome: ")
            email = input("Digite o seu melhor Email: ")
            senha = input("Digite uma senha: ")
            resultado = criar_usuario(db, nome, email, senha)
            print(resultado["message"])

        elif escolha == "2":
            resultado = listar_usuarios(db)
            if resultado["success"]:
                print("\n--- Lista de Usuários ---")
                for usuario in resultado["usuarios"]:
                    print(f"Usuário ID: {usuario.id}, Nome: {usuario.nome}, Email: {usuario.email}")
            else:
                print(resultado["message"])

        elif escolha == "3":
            titulo = input("Título do Projeto: ")
            descricao = input("Descrição: ")
            criador_id = int(input("ID do Usuário a ser vinculado: "))
            resultado = criar_projeto(db, titulo, descricao, criador_id)
            print(resultado["message"])
        
        elif escolha == "4":
            resultado = listar_projetos(db)
            if resultado["success"]:
                print("\n--- Lista de Projetos ---")
                for projeto in resultado["projetos"]:
                    print(f"Projeto ID: {projeto.id}, Título: {projeto.titulo}, Descrição: {projeto.descricao}")
            else:
                print(resultado["message"])    

        elif escolha == "5":
            titulo = input("Título da Tarefa: ")
            descricao = input("Descrição: ")
            id_projeto = int(input("ID do Projeto: "))
            id_usuario = int(input("ID do Usuário a ser vinculado: "))
            resultado = criar_tarefa(db, titulo, descricao, id_projeto, id_usuario)
            print(resultado["message"])

        elif escolha == "6":
            resultado = listar_tarefas(db)
            if resultado["success"]:
                print("\n--- Lista de Tarefas ---")
                for tarefa in resultado["tarefas"]:
                    print(f"Tarefa ID: {tarefa.id}, Título: {tarefa.titulo}, Descrição: {tarefa.descricao}, Status: {tarefa.status}")
            else:
                print(resultado["message"])

        elif escolha == "7":
            tarefa_id = int(input("ID da Tarefa que será atualizada: "))
            novo_titulo = input("Novo Título (deixar em branco pra não alterar): ")
            novo_descricao = input("Nova Descrição (deixar em branco pra não alterar): ")
            resultado = atualizar_tarefa(db, tarefa_id, novo_titulo or None, novo_descricao or None)
            print(resultado["message"])

        elif escolha == "8":
            tarefa_id = int(input("ID da Tarefa a ser excluída: "))
            resultado = excluir_tarefa(db, tarefa_id)
            print(resultado["message"])

        elif escolha == "9":
            print("Saindo...")
            break

        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
