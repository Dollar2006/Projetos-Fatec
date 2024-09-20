import calendar
import math


"""
Faça um Programa que peça os três lados de um triângulo.
O programa deverá informar se os valores podem ser 
um triângulo. Indique, caso os lados formem um triângulo,
se o mesmo é: equilátero, isósceles ou escaleno
"""


def ex1():
    l1 = float(input("Informe um dos lados do triangulo: "))
    l2 = float(input("Informe o segundo lado do triangulo: "))
    l3 = float(input("Informe o terceiro lado do triangulo: "))
    if l1 > 0 and l2 > 0 and l3 > 0:
        if l1 == l2 and l1 == l3:
            print("O triangulo é equilátero")
        elif l1 == l2 and l1 != l3 or l2 == l3 and l2 != l1 or l1 == l3 and l3 != l2:
            print("O triangulo é isosceles")
        else:
            print("O triangulo é escaleno")

ex1()


"""
Determine se um ano é bissexto. Verifique no Google como fazer isso...
"""

def ex2():
    ano = int(input("Insira um ano qualquer: "))
    print(calendar.isleap(ano))

ex2()


"""
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de 
seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do 
estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você 
faça um programa que leia a variável peso (peso de peixes) e verifique se há excesso. Se houver, gravar na 
variável excesso e na variável multa o valor da multa que João deverá pagar. Caso contrário mostrar tais 
variáveis com o conteúdo ZERO.
"""

def ex3():
    peso = float(input("Insira o peso dos peixes pescados: "))
    if peso > 50:
        excedente = peso - 50
        multa = float(excedente * 4)
        print(f"O peso excedente é: {excedente} kg")
        print(f"O valor da multa é de R${multa}")
    else:
        print("Não há excedente!")

ex3()


"""
Faça um Programa que leia três números e mostre o maior deles
"""

def ex4():
    n1 = float(input("Insira o primeiro numero: "))
    n2 = float(input("Insira o segundo numero: "))
    n3 = float(input("Insira o terceiro numero: "))

    if n1 > n2 and n1 > n3:
        print(f"O numero {n1} é o maior!")
    elif n2 > n1 and n2 > n3:
        print(f"O numero {n2} é o maior!")
    else:
        print(f"O numero {n3} é o maior!")

ex4()

"""
Faça um Programa que leia três números e mostre o maior e o menor deles. 
"""

def ex5():
    n1 = float(input("Insira o primeiro numero: "))
    n2 = float(input("Insira o segundo numero: "))
    n3 = float(input("Insira o terceiro numero: "))

    if n1 == n2 and n1 == n3:
        print("Todos os três numeros, são iguais!")
    else:
        maior = max(n1,n2,n3)
        menor = min(n1,n2,n3)
        print(f"O maior numero é {maior} e o menor numero é {menor}")
ex5()

"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas
no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são
descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato,
faça um programa que nos dê o salário bruto, quanto pagou ao INSS, quanto pagou ao
sindicato e o salário líquido. Observe que Salário Bruto - Descontos = Salário Líquido.
Calcule os descontos e o salário líquido, conforme a tabela abaixo: 
a. + Salário Bruto : R$ 
b. - IR (11%) : R$ 
c. - INSS (8%) : R$ 
d. - Sindicato ( 5%) : R$ 
e. = Salário Liquido : R$
"""
    
def ex6():
    horasTrab = int(input("Quantas horas foram trabalhadas? "))
    GanhoHora = float(input("Quanto é ganho por hora?"))
    salarioB = horasTrab * GanhoHora
    ImpostoR = salarioB * 0.11
    INSS = salarioB * 0.08
    sindicato = salarioB * 0.05
    salarioL = salarioB - (ImpostoR + INSS + sindicato)

    print(f"O salario bruto do empregado é: R${salarioB}")
    print(f"O valor pago ao Imposto de renda é: R${ImpostoR}")
    print(f"O valor pago ao INSS é: R${INSS}")
    print(f"O valor pago ao sindicato é: R${sindicato}")
    print(f"E o salário liquido com os descontos é: R${salarioL}")

ex6()

"""
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a 
ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida 
em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem 
compradas e o preço total. Obs. : somente são vendidos um número inteiro de latas.
"""

def ex7():
    metrosQ = float(input("Insira um valor em metros quadrados a serem pintados:"))
    #Valor total que 1 lata consegue pintar
    totalLata = 18 * 3
    latasCompradas = metrosQ / totalLata
    preco = math.ceil(latasCompradas * 80)
    print(f"Serão necessária(s) {math.ceil(latasCompradas)} lata(s) para a pintura da área.")
    print(f"O preço total fica em: R${round(float(preco),2)}")

ex7()
    
