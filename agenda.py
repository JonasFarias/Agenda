AGENDA = {'jonas': {
    'tel': '13-997839576',
    'email': 'jonas@email.com',
    'endereco': 'av 1',},
    'maria': {
        'tel': '13-99999-9999',
        'email': 'maria@email.com',
        'endereco': 'av 2',
    }
}

def exibir_agenda():
    if len(AGENDA) == 0:
        print('Nenhum Contato Cadastrado')
    else:
        for contato in AGENDA:
            buscar_contato(contato)

def buscar_contato(contato):
    try:
        print('\n')
        print('-' * 30)
        print(f'Nome: {contato}')
        print("Telefone: ", AGENDA[contato]['tel'])
        print("Email: ", AGENDA[contato]['email'])
        print("Endereço: ", AGENDA[contato]['endereco'])
    except KeyError:
        print('Contato Inexistente')

def inclur_editar_contato(nome):
    telefone = input('Telefone: ')
    email = input('Email: ')
    endereco = input('Endereço: ')
    inclur_editar_contato(nome, telefone, email, endereco)

    AGENDA[nome] = {
        'tel': telefone,
        'email': email,
        'endereco': endereco,
    }
    print(f'--> Contato {nome}, adicionado com sucesso!')

def excluir_contato(contato):
    try:
       AGENDA.pop(contato)
       print(f'{contato}, excluido com sucesso!')
    except KeyError:
        print('Contato Inexistente')
    except Exception as error:
        print('Um erro Inesperado aconteceu!!')
        print(error)



def menu():
    print('-' * 30)
    print('1 - EXIBIR TODOS CONTATOS')
    print('2 - BUSCAR CONTATO')
    print('3 - ADICIONAR CONTATO')
    print('4 - EDITAR CONTATO')
    print('5 - EXCLUIR CONTATO')
    print('0 - FECHAR AGENDA')
    print('-' * 30)
menu()

while True:
    opcao = int(input('Qual  Opção: '))
    if opcao == 1:
        exibir_agenda()
    elif opcao == 2:
        contato = input('Buscar: ')
        buscar_contato(contato)
    elif opcao == 3:
        try:
            nome = input('Nome: ')
            AGENDA[nome]
            print('Esse contato Já existe')
        except:
            inclur_editar_contato(nome)
    elif opcao == 4:
        try:
            nome = input('Nome: ')
            AGENDA[nome]
            print('Editando contato')
            inclur_editar_contato(nome)
        except:
            print('Contato Não Cadastrado')

    elif opcao == 5:
        contato = input('Contato: ')
        excluir_contato(contato)
    elif opcao == 0:
        print('Fechando Programa')
        break
    else:
        print('Opção Invalida')


