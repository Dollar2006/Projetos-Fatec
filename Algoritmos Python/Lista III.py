import math

"""
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor 
seja inválido e continue pedindo até que o usuário informe um valor válido.
"""

def ex1():
    while True:
        entrada = input("Insira uma nota para o aluno de zero até dez: ")

        if entrada.isnumeric():
            nota = float(entrada)
            if 0 <= nota <= 10:
                print(f"A nota {nota}, é valida!")
                break
            else:
                print("Valor invalido! A nota deve estar entre 0 a 10")
        else:
            print("Entrada invalida! Por favor insira um numero!")

#ex1()

"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao 
nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações. 
"""

def ex2():
    while True:
        nome = input("Insira o nome para o usuário: ")
        senha = input("Insira uma senha: ")
        if nome == senha:
            print("O nome de usuário não pode ser igual a sua senha!")
        else:
            print("Os dados inseridos são validos!")
            break

#ex2()

"""
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa 
anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de 
crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos 
necessários para que a população do país A ultrapasse ou iguale a população do país B, 
mantidas as taxas de crescimento 
"""
def ex3():
    paisA = 80000
    paisB = 200000
    cresA = 0.03
    cresB = 0.015
    contAno = 0
    while paisA < paisB:
        paisA = paisA + (paisA * cresA)
        paisB = paisB + (paisB * cresB)
        contAno += 1
    print(f"Ano: {contAno}")
    print(f"Pais A: {math.ceil(paisA)} habitantes \nPais B: {math.ceil(paisB)} habitantes")
    print(f"Diferença entre ambos: {math.ceil(paisA - paisB)}")

#ex3()

"""
A seqüência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Sua regra de 
formação é simples: os dois primeiros elementos são 1; a partir de então, cada elemento é a 
soma dos dois anteriores. Faça um algoritmo que leia um número inteiro calcule o seu número 
de Fibonacci. F1 = 1, F2 = 1, F3 = 2, etc.
"""

def ex4():
    num = int(input("Insira um numero qualquer: "))
    contN = 2
    n1 = 0
    n2 = 1
    if num == 1 or num == 2:
        print(f"O numero de Fibonacci de {num} é 1")
    else:
        while contN <= num:
            soma = n1 + n2
            n1 = n2
            n2 = soma
            contN += 1    
    print(f"O numero de Fibonacci de {num} é: {soma}")

#ex4()


"""
Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles
usando o algoritmo de Euclides. 
"""

def ex5():
    n1 = int(input("Insira um numero inteiro: "))
    n2 = int(input("Insira outro numero inteiro: "))
    mdc = 0
    if n1 % n2 == 0:
        mdc = min(n1,n2)
        print(f"O mdc dos numeros {n1} e {n2} é: {mdc}")
    else:
        num1 = max(n1,n2)
        num2 = min(n1,n2)
        while num1 % num2 != 0:
            mdc = num1 % num2
            num1 = num2
            num2 = mdc
        print(f"O mdc dos numeros {n1} e {n2} é: {mdc}")

ex5()
