# Exercício 03
# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;

nome = str(input("Digite seu nome!"))
count = 0
for i in nome:
    count += 1
while count <= 3:
    nome = str(input("Seu nome deve ter mais que 3 caracteres! Digite novamente!"))
    count=0
    for i in nome:
        count += 1
else:
    print("Ok!")

# Idade: entre 0 e 150;

idade= int(input("Qual a sua idade?"))
while idade < 0 or idade > 150:
    idade = int(input("Idade inválida. Ela deve estar entre 0 e 150 anos. Qual a sua idade?"))
else:
    print("Ok!")

# Salário: maior que zero;

salario = float(input("Qual o seu salário?"))
while salario <= 0:
    salario = float(input("Valor inválido. Seu salário deve ser maior que zero! Insira novamente:"))
else:
    print("Ok!")

# Sexo: 'f' ou 'm';

sexo = str(input("Se você for do sexo feminino, digite f, se masculino, digite m"))
while sexo != "f" and sexo != "m":
    sexo = str(input("Inválido! Se você for do sexo feminino, digite f, se masculino, digite m"))
else:
    print("Ok!")

# Estado Civil: 's', 'c', 'v', 'd'

estado_civil = str(input("Qual o seu estado civil?\nSolteiro: digite s \nCasado: digite c \nViúvo: digite v \nDivorciado: digite d"))
while estado_civil != "s" and "c" and "v" and "d":
    estado_civil = str(input("Inválido!\nSolteiro: digite s \nCasado: digite c \nViúvo: digite v \nDivorciado: digite d"))
else:
    print("Ok!")