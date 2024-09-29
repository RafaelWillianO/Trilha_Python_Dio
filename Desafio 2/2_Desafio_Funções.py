import textwrap


def menu():  # DEF uma função. Menu e o nome dado a função. Na linha abaixo vemos a variavel 'menu' recebendo uma string
    menu = """\n                
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))  # Return esta retornando o valor da função menu, depois que ela pega as informações ela vai para a proxima parte do codigo
# input esta sendo utilizada para  solicitar a entrada do valor do usuario
# textwrap.dedentA função dedent() da biblioteca textwrap remove qualquer indentação comum nas linhas de uma string.
# Isso é útil quando você quer formatar strings de maneira clara no código, mas não deseja que o texto seja exibido com indentação extra quando impresso.


# Aki temos uma função que esta atribuida a depositar e os seguinte argumentos. saldo, valor e estrato
def depositar(saldo, valor, extrato, /):
    if valor > 0:    # primeira condição a ser atendida, se o 'valor' for maior que 0
        saldo += valor  # aqui esta sendo receber SALDO + VALOR
        # aqui esta adicionando 'extrato' ao valor, pois o operador '+=' esta concatenando o valor a direita de extrato
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        # aki retorna o texto sujerido
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        # caso nenhuma condição a cima tenha sido atendida
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato  # Return esta retornando o valor da função depositar, depois que ela pega as informações ela vai para a proxima parte do codigo


# função atribuida a sacar. O * Antes da lista de argumentos força a utilização de argumentos nomeados.
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    # isso significa que, ao chamar a função, o chamador deverá especificar o nome de cada parâmetro.
    # Primeira verificação, se o saque excedeu o valor de saldo em conta
    excedeu_saldo = valor > saldo
    # Segunda verificação, Se o saque excedeu o valor permitido pra saque, que e de 500 reais(criterio do exercicio)
    excedeu_limite = valor > limite
    # Terceira verificação,Se excedeu a quantiodade de saque permitido, que e de 3(criterio do exercicio)
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        # Caso a verificação de saque exceda o valor em conta
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

    elif excedeu_limite:
        # Caso a segunda verificação, tenha excedido o valor de saque de 500 reais
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

    elif excedeu_saques:
        # Caso a terceira verificação, tenha excedido a quantidade de saque permitida, que e de 3
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

    elif valor > 0:  # Aki colocamos o elif, para uma outra verificaçao, que o valor sacado tem que ser > 0, pois nao tem como sacar um valor negativo
        saldo -= valor  # Subtraimos o valor sacado do saldo da conta
        # E concatenamos o valor do saldo, para o extrado, assim mostrando o valor correto em extrado
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1  # Numero de saques ja feito
        # usado para retornar  quando o saque e efetuado com sucesso
        print("\n=== Saque realizado com sucesso! ===")

    else:
        # Quando nenhuma verificaçao e correta
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato  # Return esta retornando o valor da função saque, depois que ela pega as informações ela vai para a proxima parte do codigo


# função exibir extrato. *server para todos os valores apos eles serem argumentos nomeados, e temos 2 valores
def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")  # cabeçalho
    # mostrando que caso nao tenha feito movimentaçoes, o exztrato começa vazio
    print("Não foram realizadas movimentações." if not extrato else extrato)
    # mostrando o valor de saldo, seguindo regra de negocios
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")  # roda pe


def criar_usuario(usuarios):  # função cria a variavel usuarios
    # da o valor cpf e retornar para o usuario inserir o cpf
    cpf = input("Informe o CPF (somente número): ")
    # aki criamos a variavel usuario e damos o valor de filtrar usuarios, usando o cpf e usuarios, para casos onde ja existir um cpf cadastrado
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        # para casos onde ja existir um cpf cadastrado
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return  # retornar a função

    # variavel e retornar para o usuario informar o nome
    nome = input("Informe o nome completo: ")
    # variavel e retornar para o usuario informar o data de nascimento
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    # variavel e retornar para o usuario informar o endereço
    endereco = input(
        "Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    # aki criamos um dicionario com todas as informaçoes que o cliente cadastra
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento,
                    "cpf": cpf, "endereco": endereco})

    # retorno quando o cadastro e efetuado com sucesso
    print("=== Usuário criado com sucesso! ===")


# função filtrar usuario e criada e usada na função de criação
def filtrar_usuario(cpf, usuarios):
    # aki verfica a função usuarios e valida o cpf, pois caso o cpf ja tenha sido usado
    usuarios_filtrados = [
        usuario for usuario in usuarios if usuario["cpf"] == cpf]
    # retorna a função. if caso de certo o filtro e o else caso a validação de errado
    return usuarios_filtrados[0] if usuarios_filtrados else None


# cria a função criar conta, que vem com as variaveis, agencia e numero de conta
def criar_conta(agencia, numero_conta, usuarios):
    # usa o cpf do usuario que foi, fazendo verificação das funções anteriores
    cpf = input("Informe o CPF do usuário: ")
    # pega o usuario das funçoes anteriores, e pega a função de filtrar usuarios, que sao atribuidas a cpf e usuarios
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:  # condição usada com usuario
        # retorna que a conta foi criada com uscesso
        print("\n=== Conta criada com sucesso! ===")
        # cria um dicionario e retorna a função
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    # caso tenha uma conta encerrada
    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas(contas):
    for conta in contas:  # e utilizado para fazer uma contagem de repetição e verificar a presença de uma conta
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)  # retorna o valor
        print(textwrap.dedent(linha))  # retorna o valor


def main():  # função criada para atribuir os criterios das funçoes  e das opçoes de menu, como saldo, limite de saque e numero de saque, e tambem tras informaçoes como usario e contas

    # aqui temos a estrutura funcional e a junçao de todas as funçoes para a funcionalidade do programa

    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()
