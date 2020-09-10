

# Exercício 11
# Altere o programa anterior para mostrar no final a soma dos números.

n1 = int(input("Digite um número inteiro!"))
n2 = n1
soma=0
while n1>=n2:
    n2 = int(input("Digite um número inteiro maior que o anterior!"))
    if n1<n2:
        for i in range(n1,n2+1):
            soma+=i
print("A soma dos números no intervalo dos números inseridos é "+ str(soma))