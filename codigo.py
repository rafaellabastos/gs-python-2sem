import oracledb
import pwinput
import json
#from tabulate import tabulate 

def inserir():
    """
    Função que insere os dados da vacina
    """
    inserido = False
    while not inserido:
        try:
            print("\n----- CADASTRAR STATUS DA VACINA -----\n")

            # Recebe os valores para cadastro
            usuario = input("Digite o nome do usuário: ")
            idVacina = int(input("Escolha um ID: "))
            statusVacina = input("Digite o status da vacina (sim ou não): ").lower()
            if (statusVacina) not in ["sim", "não"]:
                raise ValueError("Digite apenas 'sim' ou 'não' para o status da vacina")

            # Monta a instrução SQL de cadastro em uma string
            cadastro = f"""INSERT INTO VacinasUsuario (usuario, idVacina, statusVacina) VALUES (:usuario, :idVacina, :statusVacina) """

            # Executa e grava o registro na Tabela
            cursor.execute(cadastro, {"usuario": usuario, "idVacina": idVacina, "statusVacina": statusVacina})
            conn.commit()

            inserido = True

        except ValueError as ve:
            print(f"Erro de valor: {ve}!")
            conn.rollback()
        except Exception as e:
            print(f"Erro na transação do BD: {e}")
            conn.rollback()
        else:
            print("\nDados GRAVADOS com sucesso.")
            conn.commit()


def excluir():
    """
    Função que exclui os dados de uma vacina e define o statusVacina como NULL
    """
    try:
        print("\n----- EXCLUIR STATUS DA VACINA -----\n")

        # Nome do usuário e ID da vacina que será excluído
        usuario = input("Digite o nome do usuário: ")
        vac_id = int(input("Escolha um ID: "))

        # Constrói a instrução SQL de exclusão
        exclusao = f"""
            DELETE FROM VACINASUSUARIO
            WHERE usuario = '{usuario}' AND idVacina = {vac_id}
        """

        # Executa a instrução de exclusão
        cursor.execute(exclusao)
        conn.commit()

        # Verifica se a exclusão foi bem-sucedida
        if cursor.rowcount == 0:
            print(f"Não há uma vacina cadastrada para o usuário {usuario} com o ID = {vac_id}")
        else:
            # Constrói a instrução SQL de atualização
            status_nulo = f"""
                UPDATE VACINASUSUARIO
                SET statusVacina = NULL
                WHERE usuario = '{usuario}' AND idVacina = {vac_id}
            """

            # Executa a instrução de atualização
            cursor.execute(status_nulo)
            conn.commit()

            print(f"Informação da vacina EXCLUÍDA com sucesso e status atualizado para NULL.")

    except ValueError:
        print("Digite um número inteiro para o ID!")
    except Exception as erro:
        print(f"Erro na transação do BD: {erro}")


def alterar():
    """
    Função que altera os dados de uma vacina
    """
    try:
        print("\n----- ALTERAR INFORMAÇÕES -----\n")

        # ID da vacina que será alterado
        usuario = input("Digite o nome do usuário: ")
        vac_id = int(input("Escolha um ID: "))

        # Constroi a instrução de consulta para verificar a existencia ou não do id
        consulta = f"""SELECT * FROM VACINASUSUARIO WHERE usuario = '{usuario}' AND idVacina = {vac_id}"""

        # Executa o script SQL no banco de dados
        cursor.execute(consulta)

        # Captura os dados de retorno da consulta
        lista_dados = cursor.fetchall()

        # Verifica se o registro está cadastrado
        if len(lista_dados) == 0:
            print(f"Não há uma vacina cadastrada para o usuário {usuario} com o ID = {vac_id}")
        else:
            # Captura os novos dados
            novo_statusVacina = input("Digite o novo status da vacina: (sim ou não) ").lower()
            if (novo_statusVacina) not in ["sim", "não"]:
                raise ValueError("Digite apenas 'sim' ou 'não' para o status da vacina")

            # Constroi a instrução de edição do registro com os novos dados
            alteracao = f"""UPDATE vacinasUsuario SET
                            statusVacina = '{novo_statusVacina}'
                            WHERE usuario = '{usuario}' AND idVacina = {vac_id}"""

            # Executa e altera o registro na Tabela
            cursor.execute(alteracao)
            conn.commit()
            print("Status da vacina ATUALIZADOS com sucesso!")
    
    except ValueError:
        print("Informação incorreta!")
    except Exception:
        print("Erro na transação do BD")


def consultar():
    """
    Função que permite o usuário verificar suas vacinas
    """
    try:
        print("\n----- CONSULTAR VACINAS -----\n")

        # Monta a instrução SQL de consulta
        consulta = f"""SELECT * FROM VACINASUSUARIO"""

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
        print("Erro na transação do BD.")


def ApenasVerificar():
    print('\nOlá, seja bem vindo ao ImunoCheck!')
    print('\nEstas são as vacinas que todo cidadão brasileiro deve ter: ')

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


def cadastrar():
    UFS = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']
    
    cadastro = False
    while not cadastro:
        try:
            print("\n----- CADASTRAR USUÁRIO -----\n")

            # Recebe os valores para cadastro
            usuario = input("Usuário: ")

            nome = input("Nome completo: ")
            if not nome.replace (" ", "").isalpha():
                raise ValueError("o nome deve conter apenas letras e espaços.")

            idadestr = input("Idade: ")
            if not idadestr.isdigit():
                raise ValueError("a idade deve conter apenas números")
            idade = int(idadestr)

            estado = input("Estado (UF): ")
            if estado.upper() not in UFS:
                raise ValueError("digite uma UF válida")

            senha = pwinput.pwinput("Senha: ")

            # Monta a instrução SQL de cadastro em uma string
            cadastro = f"""INSERT INTO CADASTRO (usuario, nomeCompleto, idade, estado, senha) 
                           VALUES ('{usuario}', '{nome}', '{idade}', '{estado}', '{senha}')"""

            # Executa e grava o registro na Tabela
            cursor.execute(cadastro, {"usuario": usuario, "nome": nome, "idade": idade, "estado": estado, "senha": senha})
            conn.commit()

            cadastro = True

        except Exception as e:
            print(f"Erro na transação do BD: {e}")
        else:
            print("\nUsuário cadastrado com sucesso!")
            
        
            


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

        verificacao = f"""SELECT * FROM CADASTRO WHERE usuario = '{usuario}' AND senha = '{senha}' """
        cursor.execute(verificacao)
        resposta = cursor.fetchall()
        print(resposta)
        
        if resposta:
            print("Logado com sucesso! Entrando...")
            logado = True
        else:
            print("Usuário e/ou senha incorretos! Tente novamente.")
    except:
        print("Erro na transação do BD.")
    return logado, 


def SubMenu():
    """
    Depois que o usuário realiza login, ele pode ter acesso a sua caderneta
    """
    print('\nO que você gostaria de fazer na sua caderneta?'
          '\n1. Inserir status da vacina'
          '\n2. Excluir status da vacina'
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
            inserir()

        #Excluir vacina
        case 2:
            excluir()

        #Alterar informação
        case 3:
            alterar()

        #Consultar vacinas
        case 4:
            consultar()
        
        #Sair
        case 5:
            print('\nVoltando ao menu principal!')
            

        case _:
            print('Opção incorreta')


def exportar_consultas():

    """
    Função que exporta as consultas em JSON
    """

    try:
        print("\n----- EXPORTAR CONSULTAS PARA JSON -----\n")

        # Monta a instrução SQL de consulta
        consulta_nome_vacinas = """SELECT nomeVacina FROM Vacinas"""
        cursor.execute(consulta_nome_vacinas)

        # Monta a instrução SQL de consulta
        consulta_funcao_vacina = """SELECT funcaoVacina FROM Vacinas"""
        cursor.execute(consulta_funcao_vacina)

        # Monta a instrução SQL de consulta
        consulta_idade_tomar = """SELECT idadeAplicacao FROM Vacinas"""
        cursor.execute(consulta_idade_tomar)

        #Criação do dicionário para exportar em JSON
        consultas_json = {
            "Nome das Vacinas": [
                "BCG",
                "Hepatite B",
                "Pentavalente",
                "VIP/VOP",
                "Pneumococica 10-valente",
                "Meningococica C",
                "Rotavirus",
                "Triplice viral",
                "Hepatite A",
                "DTP",
                "Varicela",
                "Febre amarela",
                "HPV",
                "Hepatite B",
                "Triplice viral",
                "Triplice viral",
                "Dupla adulto",
                "Influenza"
            ],
            "Funcao da Vacina": [
                "Tuberculose",
                "Hepatite B",
                "DTP, Hib e HBV",
                "Poliomelite",
                "Doencas pulmonares",
                "Meningococo",
                "Rotavirus",
                "Sarampo, caxumba e rubeola",
                "Hepatite A",
                "Difteria, tetano, coqueluche",
                "Catapora",
                "Febre amarela",
                "HPV",
                "Hepatite B",
                "Sarampo, caxumba e rubeola",
                "Sarampo, caxumba e rubeola",
                "Difteria e tetano",
                "Gripe"
            ],
            "Idade para tomar": [
                "Infancia",
                "Infancia",
                "Infancia",
                "Infancia",
                "Infancia",
                "Infancia",
                "Infancia",
                "Infancia",
                "Infancia",
                "Infancia",
                "Infancia",
                "A partir dos 9 meses",
                "Meninas: 9 anos de idade / Meninos: 11 anos de idade",
                "Adolescencia",
                "Adolescencia",
                "Adulto",
                "Adulto",
                "Anual"
            ]
        }

        with open("consultas.json", "w") as arquivo_json:
            json.dump(consultas_json, arquivo_json, indent=4)

        print("Consultas exportadas para o arquivo 'arquivo.json' com sucesso!")

    except Exception as e:
        print(f"Erro na exportação das consultas para JSON: {e}")

            
# Tentativa de conexão com o banco de dados
conexao = False

while not conexao:
    try:
        usuario = input('Usuário: ')
        senha = pwinput.pwinput('Senha: ')
    
        # Conexão com o banco de dados
        conn = oracledb.connect(user=usuario, password=senha, host='oracle.fiap.com.br', port=1521, service_name='ORCL')
        
        # Criação do cursor
        cursor = conn.cursor()
    except Exception as erro:
        print(f'Erro ao conectar com o banco de dados: ', {erro})
        conexao = False                                        
    
    else:
        print('Conexão realizada com sucesso!')              
        conexao = True                                            


# Menu
while True:
    """
    Menu com as funcionalidades do sistema
    """
    print('\nSeja bem vindo! No que podemos te ajudar?'
          '\n1. Realizar cadastro'
          '\n2. Fazer login'
          '\n3. Apenas verificar vacinas'
          '\n4. Manipular caderneta'
          '\n5. Exportar consultas JSON'
          '\n6. Sair')
    
    try:
        opcaomenu = int(input('\nSelecione uma das opções acima: '))
    except ValueError:
        print('O valor deve ser um número inteiro')
        continue

    match opcaomenu:

        # Realizar cadastro
        case 1:
            cadastrar()

        # Fazer login
        case 2:
            if login():
                SubMenu()
            else:
                print("Você precisa estar logado para acessar esta funcionalidade!")
            continue

        #Apenas verificar vacinas
        case 3:
            ApenasVerificar()
        
        #CRUD
        case 4:
            if login():
                SubMenu()
            else:
                print("Você precisa estar logado para acessar esta funcionalidade!")

        #Exportar consultas JSON
        case 5:
            exportar_consultas()
            
        #Sair
        case 6:
            print('\nFim de programa. Até a próxima!')
            break

        case _:
            print('Opção incorreta!')
