import oracledb
import pwinput
from tabulate import tabulate 

def inserir():
    """
    Função que insere os dados da vacina
    """
    try:
        print("----- CADASTRAR VACINA -----\n")

        # Recebe os valores para cadastro
        a = input("VALORES PRA CADASTRO...:")
        a = input("VALORES PRA CADASTRO...:")
        a = int(input("VALORES PRA CADASTRO...:"))
        a = int(input("VALORES PRA CADASTRO...: "))
        

        # Monta a instrução SQL de cadastro em uma string
        cadastro = f"""INSERT INTO () VALUES ()"""

        # Executa e grava o registro na Tabela
        cursor.execute(cadastro)
        conn.commit()

    except ValueError:
        print("Digite um número inteiro!")
    except:
        print("Erro na transação do BD")
    else:
        print("\nDados GRAVADOS com sucesso.")


def excluir():
    """
    Função que exclui os dados de uma vacina
    """
    try:
        print("----- EXCLUIR VACINA -----\n")

        # ID da vacina que será excluído

        vac_id = int(input("Escolha um Id: ")) 

        # Monta a instrução SQL de consulta

        consulta = f"""SELECT * FROM  WHERE id = {vac_id}"""

        # Executa o script SQL no banco de dados

        cursor.execute(consulta)

        # captura os dados de retorno da consulta

        lista_dados = cursor.fetchall()

        # Verifica se o registro está cadastrado
        if len(lista_dados) == 0:
            print(f"Não há uma vacina cadastrada com o ID = {vac_id}")
        else:
            # Cria a instrução SQL de exclusão
            exclusao = f"""DELETE FROM  WHERE id = {vac_id}""" 

            # Executa a instrução e atualiza a tabela
            cursor.execute(exclusao)
            conn.commit()
    except ValueError:
        print("Digite um número inteiro para o id!")
    except Exception:
        print("Erro na transação do BD")
    else:
        print("\nVacina EXCLUÍDA com sucesso.")


def alterar():
    """
    Função que altera os dados de uma vacina
    """
    try:
        print("----- ALTERAR INFORMAÇÕES -----\n")

        # ID da vacina que será alterado
        vac_id = int(input("Escolha um Id: "))

        # Constroi a instrução de consulta para verificar a existencia ou não do id
        consulta = f"""SELECT * FROM  WHERE ID = {vac_id}"""

        # Executa o script SQL no banco de dados
        cursor.execute(consulta)

        # captura os dados de retorno da consulta
        lista_dados = cursor.fetchall()

        # Verifica se o registro está cadastrado
        if len(lista_dados) == 0:
            print(f"Não há uma vacinas cadastrada com o ID = {vac_id}")
        else:
            # Captura os novos dados
            novo_ = input("NOVOS DADOS....: ")
            novo_ = input("NOVOS DADOS....: ")
            nova_ = int(input("NOVOS DADOS..: "))

            # Constroi a instrução de edição do registro com os novos dados
            alteracao = f"""UPDATE  SET
                            a = '{"NOVOS DADOS"}',
                            a = '{"NOVOS DADOS"}',
                            a = '{"NOVOS DADOS"}'
                            WHERE id = {vac_id}"""

            # Executa e altera o registro na Tabela
            cursor.execute(alteracao)
            conn.commit()
            print("\nDados ATUALIZADOS com sucesso!")
    except ValueError:
        print("Digite um valor inteiro.")
    except Exception:
        print("Erro na transação do BD")


def consultar():
    """
    Função que permite o usuário verificar suas vacinas
    """
    try:
        print("----- CONSULTAR VACINAS -----\n")

        # Monta a instrução SQL de consulta
        consulta = f"""SELECT * FROM """

        # Executa o script SQL no banco de dados
        cursor.execute(consulta)

        # captura os dados de retorno da consulta (lista de tuplas)
        lista_dados = cursor.fetchall()

        # ordena a lista
        lista_dados.sort()

        # Verifica se há vacinas cadastradas
        if len(lista_dados) == 0:
            print(f"Não há vacinas cadastradas!")
        else:
            # exibe os itens da lista
            for item in lista_dados:
                print(item)
    except:
        print("Erro na transação do BD...")


def ApenasVerificar():
    print('\nOlá, seja bem vindo ao ImunoCheck!')
    print('\nEstas são as vacinas bases que todo cidadão brasileiro deveria ter: ')

    # Lista com 4 colunas e 19 linhas
    tabela = [["" for _ in range(4)] for _ in range(19)]

    # Primeira linha como cabeçalho
    tabela[0] = ["ID", "Nome da vacina", "Proteção", "Quando tomar"]

    # Conteúdo das outras linhas
    tabela[1] = [1, "BCG", "Tuberculose", "Infância"]
    tabela[2] = [2, "Hepatite B", "Hepatite B", "Infância"]
    tabela[3] = [3, "Pentavalente", "DRP, Hib e HBV", "Infância"]
    tabela[4] = [4, "VIP/VOP", "Poliomelite", "Infância"]
    tabela[5] = [5, "Pneumocócica", "Doenças pulmonares", "Infância"]
    tabela[6] = [6, "Meningocócica", "Meningococo", "Infância"]
    tabela[7] = [7, "Rotavírus", "Rotavírus", "Infância"]
    tabela[8] = [8, "Tríplice viral", "Sarampo, caxumba e rubéola", "Infância"]
    tabela[9] = [9, "Hepatite A", "Hepatite A", "Infância"]
    tabela[10] = [10, "DTP", "Difteria, tétano e coqueluche", "Infância"]
    tabela[11] = [11, "Varicela", "Catapora", "Infância"]
    tabela[12] = [12, "Febre amarela", "Febre amarela", "A partir dos 9 meses"]
    tabela[13] = [13, "HPV", "HPV", "Meninas: 9 anos/ Meninos: 11 anos"]
    tabela[14] = [14, "Hepatite B", "Hepatite B", "Infância"]
    tabela[15] = [15, "Tríplice viral", "Sarampo, caxumba e rubéola", "Infância"]
    tabela[16] = [16, "Tríplice viral", "Sarampo, caxumba e rubéola", "Adulto"]
    tabela[17] = [17, "Dupla adulto", "Difteria e tétano", "Adulto"]
    tabela[18] = [18, "Influenza", "Gripe", "Anual"]

    # Formatação e exibição da tabela
    print(tabulate(tabela, headers="firstrow", tablefmt="fancy_grid"))


def login():
    """
    Login do usuário para poder ter acesso as funcionalidades do sistema
    """
    logado = False
    try:
        print("\nOlá, seja bem vindo ao ImunoCheck!" +
              "\nPor Favor faça o login para continuar:")
        
        usuario = input("\nDigite o seu usuário: ")
        senha = input("Digite sua senha: ")

        verificacao = f"""SELECT * FROM WHERE usuario = '{usuario}' AND senha = '{senha}' """
        cursor.execute(verificacao)
        resposta = cursor.fetchall()
        print(resposta)
        
        if resposta:
            print("Logado com sucesso! Entrando...")
            logado = True
        else:
            print("Usário e/ou senha incorretos! Tente novamente.")
    except:
        print("Erro na transação do BD...")
    return logado


def SubMenu():
    """
    Depois que o usuário realiza login, ele pode ter acesso a sua caderneta
    """
    print('\nO que você gostaria de fazer na sua caderneta?'
          '\n1. Inserir vacina'
          '\n2. Excluir vacina'
          '\n3. Alterar informação'
          '\n4. Consultar vacinas'
          '\n5. Sair')
    
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
        
        
        #Sair
        case 5:
            print('\nFim de programa. Até a próxima!')  

        
        case _:
            print('Opção incorreta')


def cadastrar():
    try:
        print("----- CADASTRAR USUÁRIO -----\n")

        # Recebe os valores para cadastro
        nome = input("Nome completo: ")
        idade = int(input("Idade: "))
        cidade = input("Cidade: ")
        usuario = input("Nome de usuário: ")
        senha = pwinput.pwinput("Senha: ")

        # Monta a instrução SQL de cadastro em uma string
        cadastro = f"""INSERT INTO sua_tabela (nome_completo, idade, cidade, usuario, senha) 
                       VALUES ('{nome}', {idade}, '{cidade}', '{usuario}', '{senha}')"""
        
        # Executa e grava o registro na Tabela
        cursor.execute(cadastro)
        conn.commit()
        
    except ValueError:
        print("Erro: Verifique se a idade foi inserida corretamente.")
    except Exception as e:
        print(f"Erro na transação do BD: {e}")
    else:
        print("\nUsuário cadastrado com sucesso!")


        

            
# Tentativa de conexão com o banco de dados
try:
    usuario = input('Usuário: ')
    senha = pwinput.pwinput('Senha: ')

    # Conexão com o banco de dados
    conn = oracledb.connect(user=usuario, password=senha, host='oracle.fiap.com.br', port=1521, service_name='ORCL')
    
    # Criação do cursor
    cursor = conn.cursor()
except Exception as erro:
    print(f'Erro ao conectar com o banco de dados: ', {erro}) # Exibe o erro
    conexao = False                                           # Mantém a conexão com o banco de dados

else:
    print('Conexão realizada com sucesso!')                   # Exibe a mensagem de sucesso
    conexao = True                                            # Fecha a conexão com o banco de dados


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




        
        # Fazer login
        case 2:
            login()


        #Apenas verificar vacinas
        case 3:
            ApenasVerificar()


        #Sair
        case 4:
            print('\nFim de programa. Até a próxima!')
            break


        case _:
            print('Opção incorreta!')
