# Exercício 02
# Faça um programa que leia um nome de usuário e a sua senha
# e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
login = str(input("Digite o seu nome de usuário!"))
senha = str(input("Digite a sua senha"))
while login == senha:
    print("Sua senha não pode ser igual ao seu nome de usuário!")
    login = str(input("Digite o seu nome de usuário!"))
    senha = str(input("Digite a sua senha"))
if login != senha:
    print("Ok!")