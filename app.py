# 1. Funções de conversão de temperatura

def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_para_kelvin(c):
    return c + 273.15

def fahrenheit_para_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_para_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_para_celsius(k):
    return k - 273.15

def kelvin_para_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32


# 2. Estrutura principal do programa

def main():
    while True:
        print("\n--- CONVERSOR DE TEMPERATURAS ---")
        print("1- Celsius para Fahrenheit")
        print("2- Celsius para Kelvin")
        print("3- Fahrenheit para Celsius")
        print("4- Fahrenheit para Kelvin")
        print("5- Kelvin para Celsius")
        print("6- Kelvin para Fahrenheit")
        print("0- Sair")
        
        opcao = input("Escolha uma opção: ").strip()

        if opcao == '0':
            print("Saindo do programa... Até mais!")
            break

        if opcao not in ['1', '2', '3', '4', '5', '6']:
            print("Opção inválida! Por favor, escolha um número de 0 a 6.")
            continue

        try:
            temp = float(input("Digite a temperatura a ser convertida: "))
        except ValueError:
            print("Entrada inválida! Por favor, insira um valor numérico válido.")
            continue

        if opcao == '1':
            res = celsius_para_fahrenheit(temp)
            print(f"\nResultado: {temp:.2f} °C = {res:.2f} °F")
        elif opcao == '2':
            res = celsius_para_kelvin(temp)
            print(f"\nResultado: {temp:.2f} °C = {res:.2f} K")
        elif opcao == '3':
            res = fahrenheit_para_celsius(temp)
            print(f"\nResultado: {temp:.2f} °F = {res:.2f} °C")
        elif opcao == '4':
            res = fahrenheit_para_kelvin(temp)
            print(f"\nResultado: {temp:.2f} °F = {res:.2f} K")
        elif opcao == '5':
            res = kelvin_para_celsius(temp)
            print(f"\nResultado: {temp:.2f} K = {res:.2f} °C")
        elif opcao == '6':
            res = kelvin_para_fahrenheit(temp)
            print(f"\nResultado: {temp:.2f} K = {res:.2f} °F")

if __name__ == "__main__":
    main()