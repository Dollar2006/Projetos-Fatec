"""
  ex1
  Faça um programa que peça dois números inteiros 
  e imprima a soma desses dois números
"""
def ex1():
  num1 = int(input("Insira um numero: "))
  num2 = int(input("Insira o segundo numero: "))
  print(num1 + num2)

#ex1()

"""
 Escreva um programa que leia um valor em metros 
 e o exiba convertido em milímetros 
"""
  
def ex2():
  metros = float(input("Insira um valor em metros:"))
  print(metros * 100)

#ex2()

"""
Escreva um programa que leia a quantidade de dias,
horas, minutos e segundos do usuário. Calcule 
o total em segundos. 
"""

def ex3():
  dias = int(input("Insira a quantidade de dias: "))
  horas = int(input("Insira a quantidade de horas: "))
  minutos = int(input("Insira a quantidade de minutos: "))
  segundos = int(input("Insira a quantidade de segundos: "))
  print(segundos + (minutos * 60) + (horas * 3600) + (dias * 86400))

#ex3()

"""
Faça um programa que calcule o aumento de um salário. 
Ele deve solicitar o valor do salário e a 
porcentagem do aumento. Exiba o valor do aumento e do novo salário. 
"""

def ex4():
  salario = float(input("Insira o salario:"))
  aumento = float(input("Insira a porcentagem de aumento"))
  print(salario * aumento / 100)
  print(salario + (salario * aumento / 100))

ex4()

"""
Solicite o preço de uma mercadoria e o percentual de desconto. 
Exiba o valor do desconto e o preço a pagar.
"""

def ex5():
  mercadoria = float(input("Insira o preço de uma mercadoria: "))
  percDes = int(input("Insira o percentual de desconto: "))
  valorDes = mercadoria * (percDes / 100)
  precoPag = mercadoria - valorDes 
  print(f"O valor a ser descontado é: {valorDes}")
  print(f"O valor com o desconto é: {precoPag}")

ex5()