from sqlalchemy.exc import IntegrityError

from usuario import Usuario
from validacoes import validar_cpf, validar_email, validar_nome


def cadastrar_usuario(session):
    while True:
        nome = input(
            'Digite o nome do usuário (ou deixe em branco para sair): ').strip()
        if not nome:
            break
        nome = validar_nome(nome)
        if not nome:
            continue

        cpf = input('Digite o cpf do usuário: ').strip()
        cpf = cpf.replace('.', '').replace('-', '')
        if not validar_cpf(cpf):
            print('CPF inválido. Por favor, insira um CPF válido.')
            continue

        email = input('Digite o e-mail: ')
        if not validar_email(email):
            print('E-mail inválido. Por favor, insira um e-mail válido.')
            continue

        novo_usuario = Usuario(nome=nome, cpf=cpf, email=email)

        try:
            session.add(novo_usuario)
            session.commit()
            print(f'Usuário {nome} cadastrado com sucesso!\n')
        except IntegrityError:
            session.rollback()
            print(f'O CPF {cpf} já está cadastrado. Insira um CPF diferente.')
        except Exception as e:
            session.rollback()
            print(f'Ocorreu um erro ao cadastrar o usuário: {e}')

        opcao_continuar = input(
            'Deseja continuar cadastrando usuários? '
            '(S para Sim, qualquer outra tecla para voltar ao menu): ').strip(
        ).lower()
        if opcao_continuar != 's':
            break


def excluir_usuario(session):
    cpf = input('Digite o CPF do usuário que deseja excluir: ').strip()
    cpf = cpf.replace('.', '').replace('-', '')

    usuario = session.query(Usuario).filter_by(cpf=cpf).first()
    if usuario:
        session.delete(usuario)
        session.commit()
        print(f'Usuário com CPF {cpf} foi excluído com sucesso!')
    else:
        print(f'Usuário com CPF {cpf} não encontrado.')

    usuarios = Usuario.listar_usuarios(session)
    for index, usuario in enumerate(usuarios, start=1):
        usuario.id = index
    session.commit()


def alterar_dados_usuario(session):
    cpf = input('Digite o CPF do usuário que deseja altear: ').strip()
    cpf = cpf.replace('.', '').replace('-', '')

    usuario = session.query(Usuario).filter_by(cpf=cpf).first()
    if usuario:
        print('Qual dado você gostaria de alterar?')
        print('1. Nome')
        print('2. E-mail')
        print('3. Sair para o menu principal')

        opcao = input('Digite o número correspondente à sua escolha: ')
        if opcao == '1':
            novo_nome = input('Novo nome do usuário (deixe em branco para manter): ').strip()
            if novo_nome and validar_nome(novo_nome):
                usuario.nome = novo_nome

        elif opcao == '2':
            novo_email = input('Novo e-mail (deixe em branco para manter): ')
            if novo_email and validar_email(novo_email):
                usuario.email = novo_email
            else:
                print('E-mail inválido. Mantendo o e-mail antigo.')

        elif opcao == '3':
            return  # Retorna para o menu principal
        else:
            print('Opção inválida.')

        session.commit()
        print(f'Usuário com CPF {cpf} foi atualizado com sucesso!')
    else:
        print(f'Usuário com CPF {cpf} não encontrado.')


def listar_usuarios(session):
    usuarios = Usuario.listar_usuarios(session)
    if usuarios:
        print('\nListando usuários... 📋')
        for usuario in usuarios:
            print(f'ID: {usuario.id}', end=', ')
            print(f'Nome: {usuario.nome}', end=', ')
            print(f'CPF: {usuario.cpf}', end=', ')
            print(f'E-mai: {usuario.email}')
    else:
        print('Nenhum usuário cadastrado.')


def recuperar_usuario(session):
    cpf = input('Digite o CPF do usuario: ').strip()
    cpf = cpf.replace('.', '').replace('-', '')

    usuario = session.query(Usuario).filter_br(cpf=cpf).first()
    if usuario:
        print(f'Nome: {usuario.nome}', end=', ')
        print(f'CPF: {usuario.cpf}', end=', ')
        print(f'E-mail: {usuario.email}')
    else:
        print(f'Usupario com CPF {cpf} não encontrado.')