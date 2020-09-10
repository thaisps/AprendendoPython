# -*- coding: utf-8 -*-
# Exercício 05

# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
# Valide a entrada e permita repetir a operação.


pop_a = int(input("Qual a população do país A?"))
pop_b = int(input("Qual a população do país B?"))
pop_a_ano = pop_a
pop_b_ano = pop_b
tx_a=1.03
tx_b=1.015

ano = 1
while pop_a_ano < pop_b_ano:
    pop_a_ano = int(pop_a*(tx_a**ano))
    pop_b_ano = int(pop_b*(tx_b**ano))
    ano+=1
if pop_a_ano >= pop_b_ano:
    print("A população do país A será maior que a população do país B em " + str(ano) + " anos." + " Quando elas serão, respectivamente, " + str(pop_a_ano) + " e "+ str(pop_b_ano) + ".")