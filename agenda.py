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

