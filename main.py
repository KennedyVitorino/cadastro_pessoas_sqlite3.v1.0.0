from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from banco_de_dados import criar_banco_de_dados
from interacao_usuario import (
    alterar_dados_usuario,
    cadastrar_usuario,
    excluir_usuario,
    listar_usuarios,
    recuperar_usuario,
)


def main():
    criar_banco_de_dados()

    engine = create_engine('sqlite:///cadastro_pessoas.db')

    Session = sessionmaker(bind=engine)
    session = Session()

    print('Bem-vindo ao cadastro de usuários!')

    while True:
        print('\nEscolha uma opção:')
        print('1. Cadastrar usuário 👤')
        print('2. Listar usuários 📋')
        print('3. Excluir usuário ❌')
        print('4. Alterar dados do usuário 🔄')
        print('5. Recuperar dados do usuário 🔍')
        print('6. Sair 🚪')
        opcao = input('Digite o número correspondente à sua escolha: ').strip()

        if opcao == '1':
            print('\nCadastrando novo usuário... 👤')
            cadastrar_usuario(session)
        elif opcao == '2':
            listar_usuarios(session)
        elif opcao == '3':
            print('\nExcluindo usuário... ❌')
            excluir_usuario(session)
        elif opcao == '4':
            print('\nAlterando dados do usuário... 🔄')
            alterar_dados_usuario(session)
        elif opcao == '5':
            print('\nRecuperando dados do usuário... 🔍')
            recuperar_usuario(session)
        elif opcao == '6':
            print('\nSaindo do programa... 👋')
            break
        else:
            print('\nOpção inválida. Por favor, escolha uma opção válida.')

    session.close()


if __name__ == "__main__":
    main()
