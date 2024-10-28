# Função para operações
def soma(x, y):
    return x + y


def subtracao(x, y):
    return x - y


def divisao(x, y):
    if y == 0:
        return "Erro: Divisão por zero"
    return x / y


def multiplicacao(x, y):
    return x * y


# Função principal
def calculadora():
    historico = [] # Lista para armazenar o histórico das operações

    while True:
        print("Escolha a operação: ")
        print("1. Soma")
        print("2. Subtração")
        print("3. Divisão")
        print("4. Multiplicação")
        print("5. Ver Histórico")
        print("6. Sair")

        escolha = input("Digite o número da operação (1/2/3/4/5/6): ")

        if escolha == '5':
            if not historico:
                print("Nenhuma operação realizada ainda.")
            else:
                print("\nHistórico de Operações:")
                for operacao in historico:
                    print(operacao)
            continue
        if escolha == '6':
            print("Encerrar a calculadora")
            break

        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))

        if escolha == '1':
            print(f"Resultado: {num1} + {num2} = {soma(num1, num2)}")
        elif escolha == '2':
            print(f"Resultado: {num1} - {num2} = {subtracao(num1, num2)}")
        elif escolha == '3':
            print(f"Resultado: {num1} / {num2} = {divisao(num1, num2)}")
        elif escolha == '4':
            print(f"Resultado: {num1} * {num2} = {multiplicacao(num1, num2)}")
        else:
            print("Escolha inválida")
            continue

        # Exibir o resultado e adicionar a operação ao histórico
        print(f"Resultado: {operacao}")
        historico.append(operacao)

# Executar a calculadora:
calculadora()