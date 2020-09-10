# -*- coding: utf-8 -*-
# Exercício 01
nota = int(input("Digite a sua nota!"))
while nota<0 or nota>10:
    nota = int(input("Valor inválido! Digite a sua nota entre 0 e 10!"))
if nota >= 0 and nota <= 10:
    print("Ok!")