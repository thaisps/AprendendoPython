
# Exercício 10

# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

n1 = int(input("Digite um número inteiro!"))
n2 = n1
while n1>=n2:
    n2 = int(input("Digite um número inteiro maior que o anterior!"))
    if n1<n2:
        for i in range(n1,n2):
            if (i != n1):
                print(i)