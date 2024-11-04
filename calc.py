# Função para operações
def soma(x, y):
    return x + y


def subtrair(x, y):
    return x - y


def multiplicar(x, y):
    return x * y


def dividir(x, y):
    if y == 0:
        return "Erro: Divisão por zero!"
    return x / y

# Função principal da calculadora
def calculadora():
    while True:
        print("\nEscolha a operação:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Ver histórico")
        print("6. Sair")
    
        escolha = input("Digite o número da operação (1/2/3/4/5/6): ")
