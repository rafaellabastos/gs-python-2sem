def SubMenu():
    """
    Depois que o usuário realiza login, ele pode ter acesso a sua caderneta
    """
    print('\nO que você gostaria de fazer na sua caderneta?'
          '\n1. Inserir vacina'
          '\n2. Excluir vacina'
          '\n3. Alterar informação'
          '\n4. Consultar vacinas')
    
    try:
        opcaomenu = int(input('\nSelecione uma das opções acima: '))
    except ValueError:
        print('O valor deve ser um número inteiro')


    match opcaomenu:

        #Inserir vacina
        case 1:
            print('Só para não marcar erro')


        #Excluir vacina
        case 2:
            print('Só para não marcar erro')


        #Alterar informação
        case 3:
            print('Só para não marcar erro')


        #Consultar vacinas
        case 4:
            print('Só para não marcar erro')

        
        case _:
            print('Opção incorreta')


while True:
    """
    Menu com as funcionalidades do sistema
    """
    print('\nSeja bem vindo! No que podemos te ajudar?'
          '\n1. Realizar cadastro'
          '\n2. Fazer login'
          '\n3. Apenas verificar vacinas'
          '\n4. Sair')
    
    
    try:
        opcaomenu = int(input('\nSelecione uma das opções acima: '))
    except ValueError:
        print('O valor deve ser um número inteiro')
        continue


    match opcaomenu:

        # Realizar cadastro
        case 1:
            print('Só para não marcar erro')


        # Fazer login
        case 2:
            print('Só para não marcar erro')


        #Apenas verificar vacinas
        case 3:
            print('Só para não marcar erro')


        #Sair
        case 4:
            print('\nFim de programa. Até a próxima!')


        case _:
            print('Opção incorreta!')

