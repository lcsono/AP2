
# Documentação de Uso - Gerenciamento de Tarefas
Este é um sistema simples para gerenciar usuários, projetos e tarefas, com uma interface de linha de comando. Abaixo estão as instruções para o uso do sistema.

##  **Como Usar o Sistema de Gerenciamento de Tarefas**
1. Acesse o sistema: 
  Ao abrir o sistema, você verá um menu com as seguintes opções:
   ```
    --- Gerenciamento de Tarefas ---
    1. Criar Usuário
    2. Listar Usuários
    3. Criar Projeto
    4. Listar Projetos
    5. Editar Projeto
    6. Excluir Projeto
    7. Criar Tarefa
    8. Listar Tarefas
    9. Atualizar Tarefa
    10. Excluir Tarefa
    11. Sair
   ```
2. Escolha uma opção no menu:
   - Digite o número correspondente à ação que deseja realizar (por exemplo, 1 para Criar Usuário) e pressione Enter.

3. Preencha os dados solicitados:
   - O sistema pedirá algumas informações dependendo da funcionalidade escolhida. Por exemplo:
   - Para Criar Usuário, informe o nome, e-mail e senha.
   - Para Criar Projeto, forneça o título do projeto, uma descrição, e o ID do usuário responsável.
     
4. Confira os resultados:
   ```
      Usuário criado com sucesso!
   ```
5. Repita o processo:
   - Após cada operação, o sistema retornará ao menu principal para que você possa escolher outra funcionalidade.
     
7. Finalizando o uso:
   - Quando quiser sair do sistema, escolha a opção 11 (Sair) no menu principal e pressione Enter. Isso encerrará o sistema.

## **Observações**
  💡 Dicas para Usuários:

  - Organização: Antes de excluir um projeto, verifique se não há tarefas vinculadas a ele.
  - Consulta de IDs: Utilize as opções Listar Usuários (2), Listar Projetos (4) ou Listar Tarefas (8) para verificar IDs necessários em outras operações, como criar ou atualizar tarefas e projetos.
  - Prioridades: Ao criar ou atualizar uma tarefa, você pode escolher a prioridade digitando:
    - 1 para Baixa
    - 2 para Média
    - 3 para Alta
  - Criar Usuário e Criar Projeto requerem informações específicas como nome, e-mail e ID de usuário (no caso de projetos).
  - O sistema não deixará criar um projeto sem antes vincular a um usuário.
  - O sistema não deixará criar uma tarefa sem antes vincular a um projeto e a um usuário.
  - Ao criar o Projeto, os usuário cadastrados serão listados no console, assim o usuário visualizara as opções para vinvular o seu projeto
  - Ao criar Tarefa, os usuário e projeto cadastrados serão listados no console, assim o usuário visualizara as opções para vinvular a sua tarefa.

## Funcionalidades do Sistema de Gerenciamento de Tarefas

### 1. Criar Usuário
  - Objetivo: Adicionar um novo usuário ao projeto.
  - Ação: Escolha a opção 1 no menu principal. Você será solicitado a fornecer o nome, e-mail e senha do novo usuário. Após preencher as informações, o sistema criará o usuário.

### 2. Listar Usuários
  - Objetivo: Visualizar todos os usuários cadastrados .
  - Ação: Irá trazer uma lista de todos os usuários cadastrados.
    
### 3. Criar Projeto
  - Objetivo: Criar um novo projeto.
  - Ação: Será necessário fornecer o título, a descrição do projeto e o ID do usuário responsável por ele. Após preencher essas informações, o sistema criará o projeto.

### 4. Listar Projetos
  - Objetivo: Criar um novo projeto cadastrados .
  - Ação: Irá trazer uma lista com todos os projetos cadastrados.

### 5. Editar Projeto
  - Objetivo: Atualizar um novo projeto.
  - Ação: Essa ação ira atualizar um projeto, conforme os novos dados que o usuário ira fornecer.

### 6. Excluir Projeto
  - Objetivo: Excluir projetos existentes.
  - Ação: Essa ação ira excluir a tarefa cuja id foi passado na ação, conforme as validações corretas.

### 7. Criar tarefa
  - Objetivo: Criar tarefa
  - Ação: Essa ação irá criar tarefa vinculada ao projeto, irá solicitar o ID do projeto, ID do usuário, o título da tarefa, descrição e sua prioridade.

### 8. Listar Tarefa
  - Objetivo: Listar as tarefas
  - Ação: Irá trazer uma lista de todas as tarefas cadastradas.

### 9. Atualizar Tarefa
  - Objetivo: Atualizar informações da tarefa
  - Ação: Irá solicitar o ID da tarefa a ser alterada, logo ira atualizar a tarefa conforme os dados fornecido.

### 10. Excluir Tarefa
  - Objetivo: Excluir tarefa
  - Ação: Irá solicitar o ID da tarefa e irá excluir.

### 11. Sair
  - Objetivo: Finalizar o uso do sistema.
  - Ação: Escolha a opção 11. O sistema será encerrado e você voltará para o prompt de comando.

### Requisitos
- Python 3.8+
- SQLAlchemy
- SQLite ou outro banco configurado
