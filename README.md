# Cadastro de Usuários com SQLAlchemy 📚👥

Este projeto é um sistema de cadastro de usuários desenvolvido em Python. Ele utiliza o SQLAlchemy, uma biblioteca SQL Toolkit e Object-Relational Mapping (ORM) para Python, para interagir com o banco de dados SQLite.

## Como usar 🚀

1. Clone o repositório para sua máquina local usando `git clone`.
2. Navegue até a pasta do projeto.
3. Instale as dependências necessárias com o comando `pip install -r requirements.txt`.
4. Execute o script principal com o comando `python main.py`.

## Funcionalidades 🛠️

### Cadastrar usuário 👤

Esta opção permite cadastrar um novo usuário no sistema. Será solicitado que você insira o nome, CPF e e-mail do usuário. O CPF e o e-mail são únicos para cada usuário, ou seja, não podem haver dois usuários com o mesmo CPF ou e-mail.

### Listar usuários 📋

Esta opção lista todos os usuários cadastrados no sistema. Serão exibidos o ID, nome, CPF e e-mail de cada usuário.

### Excluir usuário ❌

Esta opção permite excluir um usuário do sistema. Será solicitado que você insira o CPF do usuário que deseja excluir.

### Alterar dados do usuário 🔄

Esta opção permite alterar o nome e o e-mail de um usuário existente. Será solicitado que você insira o CPF do usuário cujos dados deseja alterar.

## Validações 🛡️

O sistema realiza validações nos dados inseridos pelo usuário:

- **Nome**: Deve conter apenas letras e espaços. Caso contrário, será exibida uma mensagem de erro e será solicitado que você insira o nome novamente.
- **CPF**: Deve conter 11 dígitos e passar pela validação de CPF. Caso contrário, será exibida uma mensagem de erro e será solicitado que você insira o CPF novamente.
- **E-mail**: Deve ser um e-mail válido. Caso contrário, será exibida uma mensagem de erro e será solicitado que você insira o e-mail novamente.

## Banco de Dados 🗃️

O sistema utiliza SQLite como banco de dados. O SQLAlchemy é usado para criar, consultar, atualizar e excluir registros no banco de dados. O banco de dados é criado automaticamente ao iniciar o sistema.

## Contribuições 💡

Contribuições são sempre bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença 📄

Este projeto está licenciado sob a licença MIT.

## Contato 📧

Se você tiver alguma dúvida ou sugestão, não hesite em me contatar!

Espero que você goste deste projeto! 😊
