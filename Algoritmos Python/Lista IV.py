import random

"""
Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra
o maior e o menor valor, sem usar
as funções max e min
"""

def ex01():
    contN = 0
    numMaior = 0
    numMenor = 101
    nums = []
    while contN <= 10:
        nums.append(random.randrange(1,100,1))
        contN += 1
    contN = 0
    while contN <= 9:
        if nums[contN] >= numMaior:
            numMaior = nums[contN]
        if nums[contN] <= numMenor:
            numMenor = nums[contN]
        contN += 1
    print(f"O menor numero é: {numMenor} \n E o maior numero é: {numMaior}")

#ex01()


"""
Sorteie 20 inteiros entre 1 e 100 numa lista. Armazene os números pares
na lista PAR e os
números ímpares na lista IMPAR. Imprima as três
listas
"""
def ex2():
    Par = []
    Impar = []
    nums = []
    contN = 0
    while contN <= 20:
        nums.append(random.randrange(1,100,1))
        contN += 1
    contN = 0
    contP = 0
    contI = 0
    while contN <= 19:
        if nums[contN] % 2 == 0:
            Par.append(nums[contN])
            contP += 1
        else:
            Impar.append(nums[contN])
            contI += 1
        contN += 1
    print("-------LISTA DOS NUMEROS---------")
    for i in range(19):    
        print(nums[i])
    print("-------LISTA DOS PARES---------")
    for i in range(contP):
        print(Par[i])
    print("-------LISTA DOS IMPARES---------")
    for i in range(contI):
        print(Impar[i])
#ex2()



"""
Faça um programa que crie
dois vetores com 10 elementos
aleatórios entre 1 e 100
. Gere um
terceiro
vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos
intercalados dos dois outros vetores.
Imprima os três vetores
"""


def ex3():
    vetor1 = []
    vetor2 = []
    for i in range(10):
        vetor1.append(random.randrange(1,100,1))
    for i in range(10):
        vetor2.append(random.randrange(1,100,1))
    vetor12 = []
    contN = 0
    pos1 = 0
    pos2 = 0
    while contN < 20:
        if contN % 2 == 0:
            vetor12.append(vetor1[pos1])
            pos1 += 1
        else:
            vetor12.append(vetor2[pos2])
            pos2 += 1
        contN += 1
    print("Numeros do vetor 1: ")
    for i in range(0,9):
        print(vetor1[i])
    print("Numeros do vetor 2: ")
    for i in range(0,9):
        print(vetor2[i])
    print("Numeros dos vetores 1 e 2 : ")
    for i in range(0,19):
        print(vetor12[i])

#ex3()

"""
Seja o statement sobre diversidade: “The Python Software Foundation and the global Python 
community welcome and encourage participation by everyone. Our community is based on 
mutual respect, tolerance, and encouragement, and we are working to help each other live up 
to these principles. We want our community to be more diverse: whoever you are, and 
whatever your background, we welcome you.”. Gere uma lista de palavras deste texto com 
split(), a seguir crie uma lista com as palavras que começam ou terminam com uma das
letras “python”. Imprima a lista resultante. Não se esqueça de remover antes os caracteres especiais 
e cuidado com maiúsculas e minúsculas. 
"""

def ex4():
    letras = ["p","y","t","h","o","n"]
    texto = """The Python Software Foundation and the global Python 
community welcome and encourage participation by everyone. Our community is based on 
mutual respect, tolerance, and encouragement, and we are working to help each other live up 
to these principles. We want our community to be more diverse: whoever you are, and 
whatever your background, we welcome you."""
    txtSplit = texto.split()
    palavrasConvert = []
    for palavra in txtSplit:
        nova_palavra = ""
        for caractere in palavra:
            if caractere == "." or caractere == "," or caractere == ":":
                pass
            else:
                nova_palavra += caractere.lower()
        palavrasConvert.append(nova_palavra)
    palavrasVerificadas = []
    for palavra in palavrasConvert:
        if palavra[0] in letras: 
            palavrasVerificadas.append(palavra)     
    print(palavrasVerificadas)
#ex4()

"""
Seja o mesmo texto acima “splitado”. Calcule quantas palavras possuem uma das letras 
“python” e que tenham mais de 4 caracteres. Não se esqueça de transformar maiúsculas para 
minúsculas e de remover antes os caracteres especiais.
"""
def ex5():
    letras = ["p","y","t","h","o","n"]
    texto = """The Python Software Foundation and the global Python 
community welcome and encourage participation by everyone. Our community is based on 
mutual respect, tolerance, and encouragement, and we are working to help each other live up 
to these principles. We want our community to be more diverse: whoever you are, and 
whatever your background, we welcome you."""
    txtSplit = texto.split()
    palavrasConvert = []
    for palavra in txtSplit:
        nova_palavra = ""
        for caractere in palavra:
            if caractere == "." or caractere == "," or caractere == ":":
                pass
            else:
                nova_palavra += caractere.lower()
        palavrasConvert.append(nova_palavra)
    palavrasVerificadas = []
    for palavra in palavrasConvert:
        if palavra[0] in letras and len(palavra) > 4: 
            palavrasVerificadas.append(palavra)     
    print(palavrasVerificadas)
#ex5()

