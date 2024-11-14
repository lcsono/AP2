
# Documentação de Uso - Gerenciamento de Tarefas
Este é um sistema simples para gerenciar usuários, projetos e tarefas, com uma interface de linha de comando. Abaixo estão as instruções para o uso do sistema.

## Funcionalidades

### 1. Criar Usuário
  - Objetivo: Adicionar um novo usuário ao projeto.
  - Ação: Escolha a opção 1 no menu principal. Você será solicitado a fornecer o nome, e-mail e senha do novo usuário. Após preencher as informações, o sistema criará o usuário.
  - O sistema não deixará criar projeto sem o usuário.

### 2. Listar Usuários
  - Objetivo: Visualizar todos os usuários cadastrados .
  - Ação: O sistema irá listar todos os usuários cadastrados com seus respectivos IDs, nomes e e-mails.
    
### 3. Criar Projeto
  - Objetivo: Criar um novo projeto.
  - Ação: Será necessário fornecer o título, a descrição do projeto e o ID do usuário responsável por ele. Após preencher essas informações, o sistema criará o projeto.

### 4. Listar Projetos
  - Objetivo: Criar um novo projeto cadastrados .
  - Ação: O sistema irá listar todos os projetos cadastrados.

### 5. Editar Projeto
  - Objetivo: Atualizar um novo projeto.
  - Ação: Essa ação ira atualizar o seu projeto, conforme os novos dados que o usuário ira fornecer.

### 6. Excluir Projeto
  - Objetivo: Excluir projetos existentes.
  - Ação: Essa ação ira excluir a tarefa cuja id foi passado na ação, conforme as validações corretas.

### Criar tarefa
  - Objetivo: Criar tarefa
  - Ação: Essa ação irá criar tarefa vinculada ao projeto, irá solicitar o ID do projeto, ID do usuário, o título da tarefa, descrição e sua prioridade.

### Listar Tarefa
  - Objetivo: Listar as tarefas
  - Ação: Irá listar as tarefas, com seu ID, o título, descrição e prioridade.

### Atualizar Tarefa
  - Objetivo: Atualizar informações da tarefa
  - Ação: Irá solicitar o ID da tarefa a ser alterada,  seu novo título, nova descrição, o status da tarefa (Em andamento, finalizada) e nova prioridade.

### Excluir Tarefa
  - Objetivo: Excluir tarefa
  - Ação: Irá solicitar o ID da tarefa e irá excluir.

### 11. Sair
  - Objetivo: Finalizar o uso do sistema.
  - Ação: Escolha a opção 11. O sistema será encerrado e você voltará para o prompt de comando.


###  **Como Usar**
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

### **Observações**
  - Criar Usuário e Criar Projeto requerem informações específicas como nome, e-mail e ID de usuário (no caso de projetos).
  - Ao Excluir um Projeto, o sistema verificará se há tarefas vinculadas a ele. Se houver, será necessário primeiro excluir ou finalizar as tarefas para poder remover o projeto. 
  - A Prioridade das Tarefas pode ser configurada para "Baixa", "Média" ou "Alta", sendo representada pelos números 1, 2 e 3, respectivamente.
  - O sistema só deixará criar um Projeto se houver um Usuário criado.
  - Ao criar o usuário, o mesmo deve selecionar a opção 'Listar Usuário' para ter seu ID.
  - Ao criar o Projeto, o usuário precisa selecionar a opção 'Listar Projeto' para ter o ID de seu projeto
  - Ao criar Tarefa, o usuário precisa selecionar a opção 'Listar Tarefa' para ter o ID de sua tarefa.























