AGENDA = {'jonas':{
    'tel':'13-997839576',
    'email': 'jonas@email.com',
    'endereco': 'av 1',
}

}


def exibir_agenda():
    if len(AGENDA) == 0:
        print('Nenhum Contato Cadastrado')
    else:
        for contato in AGENDA:
            print("Nome:", contato)
            print("Telefone:", AGENDA[contato]['tel'])
            print("Email:", AGENDA[contato]['email'])
            print("Endereço:", AGENDA[contato]['endereco'])
            print('-' * 30)


exibir_agenda()
