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
    print('\n')
    print('-' * 30)
    print(f'Nome: {contato}')
    print("Telefone: ", AGENDA[contato]['tel'])
    print("Email: ", AGENDA[contato]['email'])
    print("Endereço: ", AGENDA[contato]['endereco'])

def inclur_editar_contato(nome, telefone, email, endereco):
    AGENDA[nome] = {
        'tel': telefone,
        'email': email,
        'endereco': endereco,
    }
    print(f'--> Contato {nome}, adicionado com sucesso!')

def excluir_contato(contato):
    AGENDA.pop(contato)
    print(f'{contato}, excluido com sucesso!')


def opcoes_menu():
    opcao = int(input('Qual  Opção: '))
    if opcao == 1:
        exibir_agenda()
    elif opcao == 2:
        contato = input('Buscar: ')
        buscar_contato(contato)
    elif opcao == 3 or 4:
        nome = input('Nome: ')
        telefone = input('Telefone: ')
        email = input('Email: ')
        endereco = input('Endereço: ')
        inclur_editar_contato(nome, telefone, email, endereco)
    elif opcao == 4:
        inclur_editar_contato()
    elif opcao == 5:
        contato = input('Contato: ')
        excluir_contato(contato)
    elif opcao == 0:
        pass

def exibir_menu():
    while True:
        print('\n')
        print('1 - EXIBIR TODOS CONTATOS')
        print('2 - BUSCAR CONTATO')
        print('3 - ADICIONAR CONTATO')
        print('4 - EDITAR CONTATO')
        print('5 - EXCLUIR CONTATO')
        print('0 - FECHAR AGENDA')
        opcoes_menu()





exibir_menu()
opcoes_menu()