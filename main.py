from db_config import SessionLocal, Base, engine
from crud import criar_usuario, criar_projeto, criar_tarefa, listar_tarefas, listar_usuarios, listar_projetos, atualizar_tarefa, excluir_tarefa, atualizar_projeto, excluir_projeto, solicitar_id

Base.metadata.create_all(bind=engine)

def main():
    db = SessionLocal()
    while True:
        print("\n \033[32m--- Gerenciamento de Tarefas ---\033[0m")
        print("\033[32m1.\033[0m Criar Usuário")
        print("\033[32m2.\033[0m Listar Usuários")
        print("\033[32m3.\033[0m Criar Projeto")
        print("\033[32m4.\033[0m Listar Projetos")
        print("\033[32m5.\033[0m Editar Projeto") 
        print("\033[32m6.\033[0m Excluir Projeto")
        print("\033[32m7.\033[0m Criar Tarefa")
        print("\033[32m8.\033[0m Listar Tarefas")
        print("\033[32m9.\033[0m Atualizar Tarefa")
        print("\033[32m10.\033[0m Excluir Tarefa")
        print("\033[32m11.\033[0m Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Digite o seu Nome: ")
            email = input("Digite o seu melhor Email: ")
            senha = input("Digite uma senha: ")
            resultado = criar_usuario(db, nome, email, senha)
            print("-----------------------------------")
            print(f"|   {resultado['message']}    |")
            print("-----------------------------------")

        elif escolha == "2":
            resultado = listar_usuarios(db)
            if resultado["success"] and resultado["usuarios"]:
                print("\n         \033[34m--- Lista de Usuários ---\033[0m     ")
                for usuario in resultado["usuarios"]:
                    print(f"ID Usuário: {usuario.id}, Nome: {usuario.nome}, Email: {usuario.email}")
                    print("\033[34m-------------------------------------------------\033[0m")
            else:
                print("\033[34m--------------------------------------------------------------\033[0m")
                print("\033[33mNenhum registro encontrado. Por favor, cadastre um usuário.\033[0m")
                print("\033[34m--------------------------------------------------------------\033[0m")


        elif escolha == "3":          
            usuarios = listar_usuarios(db)
            if not usuarios:
                print("\033[33mNenhum usuário disponível. Não é possível criar o projeto.\033[0m")
            else:
                print("\n     \033[34m--- Usuários Disponíveis ---\033[0m  ")
                for usuario in usuarios["usuarios"]:
                    print(f"ID: {usuario.id} - Nome: {usuario.nome} - Email: {usuario.email}")
                    print("\033[34m----------------------------------------------------\033[0m")
                
                criador_id = solicitar_id("Digite o ID do usuário que deseja vincular ao projeto: ")
                titulo = input("Título do Projeto: ")
                descricao = input("Descrição: ")
                
                resultado = criar_projeto(db, titulo, descricao, criador_id)

                print("-----------------------------------")
                print(f"|   {resultado['message']}   |")
                print("-----------------------------------")

        elif escolha == "4":
            resultado = listar_projetos(db)
            if resultado["success"] and resultado["projetos"]:
                print("\n        \033[34m--- Lista de Projetos ---\033[0m       ")
                for projeto in resultado["projetos"]:
                    print(f"Projeto ID: {projeto.id}, Título: {projeto.titulo}, Descrição: {projeto.descricao}")
                    print("\033[34m-------------------------------------------------\033[0m")
            else:
                print("\033[34m--------------------------------------------------------------\033[0m")
                print("| \033[33mNenhum registro encontrado. Por favor, cadastre um projeto.| \033[0m")
                print("\033[34m--------------------------------------------------------------\033[0m")


        elif escolha == "5":
            id_projeto = solicitar_id("Digite o ID do Projeto que deseja editar: ")
            novo_titulo = input("Novo Título (deixar em branco para não alterar): ")
            nova_descricao = input("Nova Descrição (deixar em branco para não alterar): ")
            resultado = atualizar_projeto(db, id_projeto, novo_titulo or None, nova_descricao or None)
            print(resultado["message"])

        elif escolha == "6":
            id_projeto = solicitar_id("Digite o ID do Projeto que deseja excluir: ")
            resultado = excluir_projeto(db, id_projeto)  
            print("-----------------------------------")
            print(f"{resultado['message']}")
            print("-----------------------------------")

        elif escolha == "7":            
            usuarios = listar_usuarios(db)
            projetos = listar_projetos(db)
            
            if not usuarios:
                print("\033[33mNenhum usuário disponível. Não é possível criar a tarefa.\033[0m")
            elif not projetos:
                print("\033[33mNenhum projeto disponível. Não é possível criar a tarefa.\033[0m")
            else:
                print("\033[34m     --- Usuários Disponíveis ---    \033[0m")
                for usuario in usuarios["usuarios"]:
                    print(f"ID: {usuario.id} - Nome: {usuario.nome} - Email: {usuario.email}")
                print("\033[34m----------------------------------------=---\033[0m")

                print("\033[34m    --- Projetos Disponíveis ---    \033[0m")
                for projeto in projetos["projetos"]:
                    print(f"ID: {projeto.id} - Título: {projeto.titulo} - Descrição: {projeto.titulo}")
                print("\033[34m------------------------------------------\033[0m")
                
                id_projeto = solicitar_id("ID do Projeto: ")
                id_usuario = solicitar_id("ID do Usuário a ser vinculado: ")
                titulo = input("Título da Tarefa: ")
                descricao = input("Descrição: ")
                prioridade_input = solicitar_id("Prioridade (1: para Baixa, 2: para Média, 3: para Alta): ")

                try:
                    prioridade = int(prioridade_input)
                    if prioridade not in [1, 2, 3]:
                        raise ValueError
                except ValueError:
                    print("\033[33mPrioridade inválida. A tarefa não foi criada.\033[0m")
                else:
                    resultado = criar_tarefa(db, titulo, descricao, id_projeto, id_usuario, prioridade)
                    print("-----------------------------------")
                    print(f"|   {resultado['message']}     |")
                    print("-----------------------------------")

        elif escolha == "8":
            resultado = listar_tarefas(db)
            if resultado["success"] and resultado["tarefas"]:
                print("\n       \033[34m--- Lista de Tarefas ---\033[0m      ")
                for tarefa in resultado["tarefas"]:
                    print(f"Tarefa ID: {tarefa.id}, Título: {tarefa.titulo}, Descrição: {tarefa.descricao}, Status: {tarefa.status}, Prioridade: {tarefa.prioridade}")
                    print("\033[34m-------------------------------------------------------\033[0m")
            else:
                print("\033[34m--------------------------------------------------------------\033[0m")
                print("| \033[33mNenhum registro encontrado. Por favor, cadastre uma tarefa.| \033[0m")
                print("\033[34m--------------------------------------------------------------\033[0m")


        elif escolha == "9":
            tarefa_id = solicitar_id("ID da Tarefa que será atualizada: ")
            novo_titulo = input("Novo Título (deixar em branco pra não alterar): ")
            nova_descricao = input("Nova Descrição (deixar em branco pra não alterar): ")
            novo_status = input("Novo Status (Em_andamento, Finalizada, deixe em branco pra não alterar): ")
            
            nova_prioridade = input("Nova Prioridade (1: Baixa, 2: Média, 3: Alta, deixe em branco para não alterar): ").strip()
            if nova_prioridade not in ['1', '2', '3']:
                nova_prioridade = None
            else:
                nova_prioridade = int(nova_prioridade)  
            
            resultado = atualizar_tarefa(db, tarefa_id, novo_titulo or None, nova_descricao or None, novo_status or None, nova_prioridade)
            print("-----------------------------------")
            print(f"|   {resultado['message']}     |")
            print("-----------------------------------")

        elif escolha == "10":
            tarefa_id = solicitar_id("ID da Tarefa a ser excluída: ")
            resultado = excluir_tarefa(db, tarefa_id)
            print("-----------------------------------")
            print(f"|   {resultado['message']}     |")
            print("-----------------------------------")

        elif escolha == "11":
            print("Saindo...")
            break

        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    main()
