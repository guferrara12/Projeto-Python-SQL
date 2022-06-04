# Biblioteca SQLite3
import sqlite3

# Conexão com o banco de dados
con = sqlite3.connect("my_dbpython")
cursor = con.cursor()

# Criando função para cadastrar usuários
def CadastrarUsuario():
    # Nome do usuário
    nome = input("\nEntre com o nome: ")
    # Senha do usuário
    senha = input("\nEntre com uma senha: ")
    # Inserindo dados no banco
    cursor.execute(f""" INSERT INTO USUARIO VALUES (NULL, "{nome}", "{senha}")
    """)
    # Gravando informação no banco
    con.commit()
    # Confirmando inserção para o usuário do programa
    print("\nDados gravados com sucesso!")
    # Chamando função que retorna o menu do programa
    MenuPrincipal()

# Criando função para cadastrar empréstimos
def CadastrarEmprestimo():
    # Criando uma lista para armazenar os IDS dos usuários
    lista_id_usuario = []

    print("\nVerifique abaixo o ID do usuário:")

    # Selecionando IDS e nomes dos usuários existentes
    cursor.execute(f""" SELECT IDUSUARIO, NOME_USUARIO FROM USUARIO
    """)

    # Ciclo de repetição para buscar cada registro
    for id_usuario, nome_usuario in cursor.fetchall():
        # Mostrando registros
        print(f"\nID USUÁRIO: {id_usuario}\nNOME: {nome_usuario}")
        # Transformando ID do usuário em uma variável do tipo String
        id_usuario = str(id_usuario)
        # Adicionando ID na lista de usuários
        lista_id_usuario.append(id_usuario)

    # Entrando com o ID desejado
    id = input("\nEntre com o ID: ")

    # Comparando se o ID digitado existe na lista de IDS do banco
    if (id in lista_id_usuario):
        # Entrando com o nome do devedor
        nome_devedor = input("\nNome do Devedor: ")
        # Entrando com o valor do empréstimo
        valor = input("\nValor do Empréstimo: ")
        # Entrando com a data do empréstimo
        data = input("\nData do Empréstimo: ")
        # Status do empréstimo definido como "ATIVO"
        status = "ATIVO"
        # Entrando com a senha do devedor
        senha_devedor = input("\nEntre com a senha do devedor: ")
        # Selecionando nome e senha do usuário referentes ao ID escolhido
        cursor.execute(f""" SELECT NOME_USUARIO, SENHA_USUARIO FROM USUARIO WHERE IDUSUARIO = {id}
        """)

        # Ciclo de repetição para inserção de empréstimo no banco
        for nome, senha_bd in cursor.fetchall():
            # Comparando a senha digitada com a senha do respectivo usuário no banco
            if (senha_devedor == senha_bd):
                # Confirmação da senha correta
                print("\nSENHA CORRETA")
                # Inserindo empréstimo no banco
                cursor.execute(f""" INSERT INTO EMPRESTIMO VALUES (NULL, "{nome_devedor}", "{valor}", "{data}", "{id}", "{status}")
                """)
                # Gravando informação no banco
                con.commit()
                # Informação confirmada
                print("Dados gravados com sucesso!")
                # Chamando função para retornar ao menu
                MenuPrincipal()

            # Senha digitada é diferente da senha cadastrada
            else:
                # Informação confirmada
                print("\nSENHA INCORRETA")
                # Chamando função para retornar ao menu
                MenuPrincipal()

    # O ID digitado não corresponde a nenhum usuário
    else:
        # Informação confirmada
        print("\nID Inexistente")
        # Chamando função para retornar ao menu
        MenuPrincipal()

# Criando função para consultar empréstimos
def ConsultarEmprestimo():
    # Mostrando ao usuário do programa as opções existentes
    print("\nEscolha uma opção abaixo:")
    print("\n1 - Todos os empréstimos existentes\n2 - Empréstimos de um usuário")
    # Entrando com uma opção e salvando em uma variável
    opcao = input("\nEntre com a opção desejada: ")
    # Comparando se a escolha foi a primeira opção
    if (opcao == "1"):
        print("\nEmpréstimos Existentes:")
        # Selecionando todos os empréstimos existentes no banco
        cursor.execute(f""" SELECT IDEMPRESTIMO, NOME_DEVEDOR, VALOR_EMPRESTIMO, DATA_EMPRESTIMO, ID_USUARIO, STATUS_EMPRESTIMO FROM EMPRESTIMO
        """)
        # Ciclo de repetição para mostrar aos usuários todos os empréstimos
        for id_emprestimo, nome_devedor, valor, data, id_usuario, status in cursor.fetchall():
            print(f"\nID EMPRÉSTIMO: {id_emprestimo}\nDEVEDOR: {nome_devedor}\nVALOR: {valor}\nDATA: {data}\nSTATUS: {status}")
        # Retornando ao Menu
        MenuPrincipal()

    # Comparando se a escolha foi a primeira opção
    elif (opcao == "2"):
        # Criando lista para salvar IDS dos usuários
        lista_id_usuario = []
        print("\nEscolha um usuário abaixo:")
        # Selecionando IDS e nome dos usuários
        cursor.execute(""" SELECT IDUSUARIO, NOME_USUARIO FROM USUARIO
        """)
        # Ciclo de repetição para mostrar todos os usuários existentes no banco
        for id_usuario, nome_usuario in cursor.fetchall():
            print(f"\nID USUÁRIO: {id_usuario}\nNOME: {nome_usuario}")
            id_usuario = str(id_usuario)
            lista_id_usuario.append(id_usuario)

        # Entrando com o ID desejado
        id = input("\nEntre com o ID do usuário: ")
        # Comparando se o ID escolhido existe no banco
        if (id in lista_id_usuario):
            # Se existir seleciona os empréstimos referentes ao usuário escolhido
            cursor.execute(f""" SELECT IDEMPRESTIMO, NOME_DEVEDOR, VALOR_EMPRESTIMO, DATA_EMPRESTIMO, ID_USUARIO, STATUS_EMPRESTIMO FROM EMPRESTIMO WHERE ID_USUARIO = {id}
            """)
            # Mostrando as informações ao usuário do programa
            for id_emprestimo, nome_devedor, valor, data, id_usuario, status in cursor.fetchall():
                print(f"\nID EMPRÉSTIMO: {id_emprestimo}\nDEVEDOR: {nome_devedor}\nVALOR: {valor}\nDATA: {data}\nSTATUS: {status}")
            MenuPrincipal()

        # Se nenhum ID existir
        else:
            print("\nID Inexistente")
            MenuPrincipal()

    # Se nenhuma opção existente for escolhida
    else:
        print("\nEntrada Inválida")
        MenuPrincipal()


# Criando função para pagar empréstimo
def PagarEmprestimo():
    # Criando lista de IDS de usuários
    lista_id_usuario = []
    # Criando lista de IDS de empréstimos
    lista_id_emprestimo = []
    print("\nEscolha um usuário abaixo:")
    # Selecionando ID e nome dos usuários
    cursor.execute(""" SELECT IDUSUARIO, NOME_USUARIO FROM USUARIO
    """)

    # Ciclo de repetição para mostrar a informação ao usuário
    for id_usuario, nome_usuario in cursor.fetchall():
        print(f"\nID USUÁRIO: {id_usuario}\nNOME: {nome_usuario}")
        id_usuario = str(id_usuario)
        lista_id_usuario.append(id_usuario)

    # Entrando com o ID desejado
    id = input("\nEntre com o ID do usuário: ")

    # Se o ID escolhido existir no banco
    if (id in lista_id_usuario):
        print("\nSelecione o empréstimo que deseja quitar:")
        # Selecionando empréstimos do usuário escolhido
        cursor.execute(f""" SELECT IDEMPRESTIMO, NOME_DEVEDOR, VALOR_EMPRESTIMO, DATA_EMPRESTIMO, ID_USUARIO, STATUS_EMPRESTIMO FROM EMPRESTIMO WHERE ID_USUARIO = {id}
        """)

        # Mostrando informação ao usuário
        for id_emprestimo, nome_devedor, valor, data, id_usuario, status in cursor.fetchall():
            print(f"\nID EMPRÉSTIMO: {id_emprestimo}\nDEVEDOR: {nome_devedor}\nVALOR: {valor}\nDATA: {data}\nSTATUS: {status}")
            id_emprestimo = str(id_emprestimo)
            lista_id_emprestimo.append(id_emprestimo)

        # Entrando com o ID de empréstimo desejado
        emprestimo = input("\nEntre com o ID do empréstimo: ")

        # Se o ID do empréstimo existir no banco
        if (emprestimo in lista_id_emprestimo):
            emprestimo = int(emprestimo)
            # Realizando update no empréstimo escolhido alterando o status para PAGO
            cursor.execute(f""" UPDATE EMPRESTIMO SET STATUS_EMPRESTIMO = "PAGO" WHERE IDEMPRESTIMO = {emprestimo}
            """)
            con.commit()
            print("\nProcedimento efetuado com sucesso")
            MenuPrincipal()

        else:
            print("\nEntrada Inválida")
            MenuPrincipal()

    else:
        print("\nEntrada Inválida")
        MenuPrincipal()

# Criando função para o menu principal
def MenuPrincipal():
    print("\n\nSistema de Empréstimos Bancários\n\nEntre com uma opção abaixo:")
    print("\n1 - Criar Usuário\n2 - Cadastrar Empréstimo\n3 - Consultar Empréstimo\n4 - Pagar Empréstimo\n5 - Sair")

    escolha = input("\nEscolha: ")

    if (escolha == "1"):
        print("\nCadastrar Usuário")
        CadastrarUsuario()
    elif (escolha == "2"):
        print("\nCadastrar Empréstimos")
        CadastrarEmprestimo()
    elif (escolha == "3"):
        print("\nConsultar Empréstimos")
        ConsultarEmprestimo()
    elif (escolha == "4"):
        print("\nPagar Empréstimo")
        PagarEmprestimo()
    elif (escolha == "5"):
        print("\nPrograma Encerrado")
    else:
        print("\nEntrada Inválida")


MenuPrincipal()



