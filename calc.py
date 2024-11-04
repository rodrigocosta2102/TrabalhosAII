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

  num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))

        if escolha == '1':
            resultado = soma(num1, num2)
            operacao = "soma"
        elif escolha == '2':
            resultado = subtrair(num1, num2)
            operacao = "subtração"
        elif escolha == '3':
            resultado = multiplicar(num1, num2)
            operacao = "multiplicação"
        elif escolha == '4':
            resultado = dividir(num1, num2)
            operacao = "divisão"
        elif escolha == '6':
            print("Encerrando a calculadora...")
            break
        else:
            print("Escolha inválida")
            continue



