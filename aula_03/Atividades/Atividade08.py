soma_notas = 0
quantidade_notas = 0

while True:
    nota = float(input("Digite a nota do aluno: "))
    
    if nota == -1:
        break
    
    if 0 <= nota <= 10:
        soma_notas += nota
        quantidade_notas += 1
    else:
        print("Nota inválida. Digite uma nota entre 0 e 10.")

if quantidade_notas > 0:
    media = soma_notas / quantidade_notas
    print(f"A média das notas inseridas é: {media:.2f}")
else:
    print("Nenhuma nota válida foi inserida.")
