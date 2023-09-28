## Cadastro de Usuários

### Descrição do Programa

O programa "Cadastro de Usuários" é uma aplicação de linha de comando desenvolvida em Python que permite cadastrar, listar e excluir usuários em um banco de dados SQLite. Ele foi projetado para ser uma ferramenta simples e eficaz para gerenciar informações de usuários, incluindo nome e CPF.

### Funcionalidades

O programa oferece as seguintes funcionalidades:

1. **Cadastrar Usuário:** Permite inserir novos usuários no banco de dados, incluindo validação de CPF.
2. **Listar Usuários:** Exibe a lista de todos os usuários cadastrados no banco de dados.
3. **Excluir Usuário:** Permite excluir um usuário com base no CPF fornecido.

### Pré-requisitos

Antes de executar o programa, certifique-se de ter instalado as seguintes dependências:

- Python 3.x
- SQLAlchemy (biblioteca para manipulação do banco de dados)
- SQLite (banco de dados integrado ao programa)

### Como Executar o Programa

1. Clone o repositório do programa para o seu computador:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   ```
   
2. Crie um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   ```

3. Ative o ambiente virtual:
   - No windows:
   ```bash
   source venv/bin/activate
   ```
   - No macOS ou Linux:
   ```bash
   source venv/bin/activate
   ```

4. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

5. Execute o programa:
    ```bash
    python main.py
    ```
   
### Como Usar o Programa

Ao executar o programa, você terá um menu com as opções:

- **Cadastrar usuário**
- **Listar usuários**
- **Excluir usuário**
- **Sair**

Siga as instruções na tela para realizar as operações desejadas.

### Contribuições

Contribuições são bem-vindas! Se você deseja melhorar ou adicionar recursos ao programa, sinta-se à vontade para fazer um fork do repositório, implementar suas alterações e enviar um pull request.

### Licença

Este programa é distribuído sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para obter detalhes.

**Nota:** Este é um exemplo de README.md para fins ilustrativos. Certifique-se de personalizar este arquivo de acordo com as necessidades do seu projeto.
