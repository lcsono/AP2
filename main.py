from db_config import SessionLocal, Base, engine
from crud import criar_usuario, criar_projeto, criar_tarefa, listar_tarefas, listar_usuarios, listar_projetos, atualizar_tarefa, excluir_tarefa, atualizar_projeto
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
        print("5. Editar Projeto") 
        print("6. Criar Tarefa")
        print("7. Listar Tarefas")
        print("8. Atualizar Tarefa")
        print("9. Excluir Tarefa")
        print("10. Sair")

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
            projeto_id = int(input("Digite o ID do Projeto que deseja editar: "))
            novo_titulo = input("Novo Título (deixar em branco para não alterar): ")
            nova_descricao = input("Nova Descrição (deixar em branco para não alterar): ")
            resultado = atualizar_projeto(db, projeto_id, novo_titulo or None, nova_descricao or None)
            print(resultado["message"])

        elif escolha == "6":
            titulo = input("Título da Tarefa: ")
            descricao = input("Descrição: ")
            id_projeto = int(input("ID do Projeto: "))
            id_usuario = int(input("ID do Usuário a ser vinculado: "))
            
            prioridade_input = input("Prioridade (1: para Baixa, 2: para Média, 3: para Alta): ")
            
            try:
                prioridade_input = int(prioridade_input)
            except ValueError:
                print("Prioridade inválida! Definindo como 'Baixa'.")
                prioridade_input = 1

            # Passa o valor de prioridade como número inteiro
            resultado = criar_tarefa(db, titulo, descricao, id_projeto, id_usuario, prioridade_input)
            print(resultado["message"])

        elif escolha == "7":
            resultado = listar_tarefas(db)
            if resultado["success"]:
                print("\n--- Lista de Tarefas ---")
                for tarefa in resultado["tarefas"]:
                    print(f"Tarefa ID: {tarefa.id}, Título: {tarefa.titulo}, Descrição: {tarefa.descricao}, Status: {tarefa.status}, Prioridade: {tarefa.prioridade}")
            else:
                print(resultado["message"])

        elif escolha == "8":
            tarefa_id = int(input("ID da Tarefa que será atualizada: "))
            novo_titulo = input("Novo Título (deixar em branco pra não alterar): ")
            nova_descricao = input("Nova Descrição (deixar em branco pra não alterar): ")
            novo_status = input("Novo Status (Em_Andamento, Finalizada, deixe em branco pra não alterar): ")
            
            nova_prioridade = input("Nova Prioridade (1: Baixa, 2: Média, 3: Alta, deixe em branco para não alterar): ").strip()
            if nova_prioridade not in ['1', '2', '3']:
                nova_prioridade = None
            else:
                nova_prioridade = int(nova_prioridade)  
            
            resultado = atualizar_tarefa(db, tarefa_id, novo_titulo or None, nova_descricao or None, novo_status or None, nova_prioridade)
            print(resultado["message"])


        elif escolha == "9":
            tarefa_id = int(input("ID da Tarefa a ser excluída: "))
            resultado = excluir_tarefa(db, tarefa_id)
            print(resultado["message"])

        elif escolha == "10":
            print("Saindo...")
            break

        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
