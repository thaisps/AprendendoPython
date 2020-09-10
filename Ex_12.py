

# Exercício 12

# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
# O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
# Tabuada de 5:
# 5 X 1 = 5
# 5 X 2 = 10
# ...
# 5 X 10 = 50

numero = 0
while numero < 1 or numero >10:
    numero = int(input("Digite um número de 1 a 10 para ver a sua tabuada!"))
    if numero >= 1 and numero <=10:
        print("Tabuada de " + str(numero) + ":")
        for i in range(1,11):
            print(str(numero) + " X " + str(i) + " = " + str(numero*i))