while True:
    numero = int(input("Digite um número entre 1 e 10: "))
    
    if 1 <= numero <= 10:
        print(f"Você digitou um número válido: {numero}")
        break
    else:
        print("Número inválido! Por favor, digite um número entre 1 e 10.")
