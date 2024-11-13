
# Documentação de Uso - Gerenciamento de Tarefas
Este é um sistema simples para gerenciar usuários, projetos e tarefas, com uma interface de linha de comando. Abaixo estão as instruções para o uso do sistema.

 1. Criar Usuário
  - Objetivo: Adicionar um novo usuário ao projeto.
  - Ação: Escolha a opção 1 no menu principal. Você será solicitado a fornecer o nome, e-mail e senha do novo usuário. Após preencher as informações, o sistema criará o usuário.

 2. Listar Usuários
  - Objetivo: Visualizar todos os usuários cadastrados .
  - Ação: O sistema irá listar todos os usuários cadastrados com seus respectivos IDs, nomes e e-mails.
 3. Criar Projeto
  - Objetivo: Criar um novo projeto.
  - Ação: Será necessário fornecer o título, a descrição do projeto e o ID do usuário responsável por ele. Após preencher essas informações, o sistema criará o projeto.

 4. Listar Projetos
  - Objetivo: Criar um novo projeto cadastrados .
  - Ação: O sistema irá listar todos os projetos cadastrados.

5. Atualizar Projeto
  - Objetivo: Criar um novo projeto.
  - Ação: Está ação ira atualizar o seu projeto, conforme os novos dados que o usuário ira fornecer.

 6. Excluir Projeto
  - Objetivo: Excluir projetos existentes.
  - Ação: Essa ação ira excluir a atrefa cuja id foi passado na ação, conforme as validações corretas.

 11. Sair
  - Objetivo: Finalizar o uso do sistema.
  - Ação: Escolha a opção 11. O sistema será encerrado e você voltará para o prompt de comando.


##  Como Usar
1. Execute o script ```python ./main.py```.
2. O sistema exibirá o menu com opções numeradas
   ```
    print("\n--- Gerenciamento de Tarefas ---")
    print("1. Criar Usuário")
    print("2. Listar Usuários")
   ...
   ```
   .
4. Escolha uma opção digitando o número correspondente e siga as instruções que aparecem no terminal.
5. Para sair, basta escolher a opção 11.

- **Observações**
  - Criar Usuário e Criar Projeto requerem informações específicas como nome, e-mail e ID de usuário (no caso de projetos).
  - Ao Excluir um Projeto, o sistema verificará se há tarefas vinculadas a ele. Se houver, será necessário primeiro excluir ou finalizar as tarefas para poder remover o projeto.
  - A Prioridade das Tarefas pode ser configurada para "Baixa", "Média" ou "Alta", sendo representada pelos números 1, 2 e 3, respectivamente.
