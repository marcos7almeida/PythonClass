
"""
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
# pypi.org (site para instação de pacotes)

Faça um programa que peça uma nota, entre zero e dez.
Mostre uma mensagem caso o valor seja inválido e
continue pedindo até que o usuário informe um valor válido.

###################################
 # python -m pip install -U jupyter
# for i in range(1,4): [1,2,3]   range(init,n-1,step)
for i in range(1,4,1):#[0,1,2]
    nota = input("Digite uma nota: ")
    print(nota)

    nota = float(nota)

    if nota >= 0 and nota <= 10:
        print(f"{i} nota: {nota}")
        break
    else:
        print(f"{i} nota errada: {nota}")
        continue

print('Fim do Script - for')

######################################


nota = -1

while not (nota >= 0 and nota <= 10):
    nota = input("Digite uma nota: ")
    nota = float(nota)
else:
    print(f" nota: {nota}")
print('Fim do Script - while')

######################################


Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
O usuário deve informar de qual numero ele deseja ver a tabuada.
A saída deve ser conforme o exemplo abaixo:



numero = input("Digite um número: ")
for i in range(1,11):
#    print(numero)
    numero = float(numero)
    prod = i*numero
#    if numero >= 0 and numero <= 10:
    print(f"{i}","X", numero ,"=", prod)
#        break

#    else:
#    print(f"{i} numero errado: {numero}")
#
#
#        continue

print('Fim do Script - for')

###########################

i = -1
numero = input("Digite um número: ")
numero = float(numero)
while (i < 10):
    i += 1
    prod = i*numero
    print(f"{i}","X", numero ,"=", prod)
#else:
#    print(f" nota: {nota}")
print('Fim do Script - while')


"""
##############
"""
14. Faça um programa que peça 10 números inteiros,
calcule e mostre a quantidade de números pares e a quantidade de números impares.
"""
"""
n_par = 0
n_impar = 0
i = 0
while (i < 10):
    i += 1
    numero = input("Digite um numero: ")
    numero = float(numero)
    if (numero %2 == 0):
        n_par += 1
    else:
        n_impar += 1

print("n par", n_par, "n impar", n_impar)
"""
##############################
"""
15. A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,...
Faça um programa capaz de gerar a série até o n−ésimo termo. Funcional: sem = 0 if i>=0  else 1
"""
"""
fib_0 = 0
fib_1 = 1
fib_2 = fib_0 + fib_1
print(fib_0)
print(fib_1)
print(fib_2)
for i in range(8):
    fib_3 = fib_2 + fib_1
    fib_1 = fib_2
    fib_2 = fib_3
    print(fib_3)
##############################

N = int(input("Digite a quantidade da serie de Fib =  "))
fib = [0,1,1]
for i in range(3,N):
        fib.append(fib[i-1] + fib[i-2]) #fib += (fib[i-1] + fib[i-2])

for seq in fib:
    print(seq)

'''
arq = open("arquivo.dat", "w")

arq.write("1\tiury\t27\n")
arq.write("2\tguilherme\t35\n")
arq.write("3\tmarcos\t63\n")
arq.write("4\tpatricia\t27\n")
arq.write("5\tfernando\t71\n")

arq.close()

##########

ler = open("arquivo.dat")


print(ler.read())

print("----")

ler.seek(0)

print(ler.read())

ler.close()

############


nome_arq = "arquivo.dat"
arq_add = open(nome_arq, "a")

id, nome, idade = (
input('id:'),
input('nome:'),
input('idade:')
)

arq_add.write(f"{id}\t{nome}\t{idade}\n")

arq_add.close()

ler = open(nome_arq)
leitura = ler.read()
print(leitura)

print(leitura)

ler.close()
######################################
arq = open("arquivo.dat", "w")

arq.write("1\tiury\t27\n")
arq.write("2\tguilherme\t35\n")
arq.write("3\tmarcos\t63\n")
arq.write("4\tpatricia\t27\n")
arq.write("5\tfernando\t71\n")

arq.close()

manipulando = open("arquivo.dat")

leitura = manipulando.readlines()

for linha in leitura:
    linha = linha.strip('\n')
    linha = linha.split('\t')
    id = int(linha[0])
    nome = linha[1]
    idade = int(linha[2])

    print(f"id: {id}; nome: {nome}; idade: {idade}")

manipulando.close()

"""

"""

1. Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo,
contendo um relatório dos endereços IP válidos e inválidos. O arquivo de entrada possui o seguinte formato:

"""
#####

"""
with open("A.txt", "w") as arq:

    arq.write("200.135.80.9\n")
    arq.write("192.168.1.1\n")
    arq.write("8.35.67.74\n")
    arq.write("257.32.4.5\n")
    arq.write("85.345.1.2\n")
    arq.write("1.2.3.4\n")
    arq.write("9.8.234.5\n")
    arq.write("192.168.0.256\n")

with open("A.txt") as arq:
#    print(arq.read())

    ler = arq.read()
    lista_ip = ler.split("\n")

    for ip in lista_ip:
        q = open("B.txt", "a")
        q.write(ip+"\n")
        q.close()

        l_ip = ip.split(".")
        if int(l_ip[0])%2 == 0:
            p = open("par.txt", "a")
            p.write(ip+"\n")
            p.close()
        else:
            p = open("impar.txt", "a")
            p.write(ip+"\n")
            p.close()
"""
#### geração de arquivos aleatórios #####

"""
import random

L = list(range(0,10))
str_p = "file_"
for _ in L:
    num = random.choice(L)
    r = open(f"{str_p}{num}.txt","a")
    r.write(f'{random.random()}\n')
    r.close()


#### geração de arquivos aleatórios #####

import random

L = list(range(0,10))
str_p = "file_"
for _ in L:
    num = random.choice(L)
    r = open(f"{str_p}{num}.txt","a")
    r.write(f'{random.random()}\n')
    r.close()

import glob
str_p = "file_"
print(glob.glob("*"))
print(glob.glob(f'{str_p}*'))
L_arq = glob.glob(f'{str_p}*')

num_min = 2
file_min =''
num_max = 0
file_max =''

for arq in L_arq:
    print(arq)
    q = open(arq)
#    print(q.read())

    ler = q.read()
    #print(ler)
    lista = ler.split('\n')
#    lista = lista.split(',')
    print(lista)

    for L in lista:
        L = L.strip('\n')
        if L:
            num = float(L)
            print(num)
            if num < num_min:
                    num_min = num
                    file_min = arq
            if num > num_max:
                    num_max = num
                    file_max = arq
    q.close()
min = open('min.txt', 'w')
max = open('max.txt', 'w')
min.write(f'{file_min}\t{num_min}')
max.write(f'{file_max}\t{num_max}')
min.close()



uf = {
"PE": "Pernambuco",
"RN": "Rio Grande do Norte"
}

print(uf['PE'])
print(uf['RN'])

siglas = uf.keys()
estados = uf.values()

print(siglas)
print(estados)
############

# 1. Classe Bola:
# - Crie uma classe que modele uma bola:
#  - Atributos:
#       - core
#       - circunferencia
#       - material
#  - Métodos
#       - troca cor
#       - mostra cor

# Atributos
import pprint

bola = {
'cor' : 'verde',
'circunferencia' : 12,
'material' : 'fibra de vidro',
}

# Métodos

bola['cor'] = 'azul'
print(bola['cor'])

pprint.pprint(bola)

##################################################################
#Pandas === equivalente ao R (precisa instalar)

#pythom -m pip install -U Pandas

import pandas as pd

pessoa_1 = {
'CPF': 12587117453,
'NOME': 'Marcos',
'CIDADE': 'Recife',
'IDADE': 63
}
pessoa_2 = {
'CPF': 11111111111,
'NOME': 'João',
'CIDADE': 'Jaboatão',
'IDADE': 33
}


print(pd.DataFrame([pessoa_1,pessoa_2]))

######################################


import pandas as pd

# import csv

pessoas = []

for _ in range(2):
    pessoa = {
    'CPF': input('digite o cpf: '),
    'NOME': input('digite o nome: '),
    'CIDADE': input('digite a cidade: '),
    'IDADE': int(input('digite a idade: '))
    }
    pessoas.append(pessoa)

data = pd.DataFrame(pessoas)

print(data['IDADE'].mean())
data['IDADE'].plot.line()

print(dir(data))

print(data)


# dir(pd) ---- métodos
# help(pd) ----como usa os métodos     site pandas
######################################

"""

class Bola:
    def __init__(self, cor, raio):
        self.cor = cor
        self.raio = raio

    def mostrar_cor(self):
        print(self.cor)

    def mostrar_raio(self):
        print(self.raio)


bola = Bola('verde', '10')
print(bola.cor)
print(bola.raio)

tenis = Bola('azul', '3')
print(tenis.cor)
print(tenis.raio)

bola.mostrar_cor()
tenis.mostrar_cor()
bola.mostrar_raio()
tenis.mostrar_raio()

tenis.material = 'polimero'
bola.material = 'plastico'
print(tenis.material)
print(bola.material)

class BolaGolf(Bola):
    material = 'palha'


golf = BolaGolf('branco',1)
print(golf.material)
golf.mostrar_cor()
golf.mostrar_raio()

class BolaSquash(Bola):
    def __init__(self, cor, raio, material):
        Bola.__init__(self,cor, raio)
        self.material = material

    def exibir_material(self):
        print(self.material)


squash = BolaSquash('verde','17','lona')
squash.exibir_material()
squash.mostrar_cor()
squash.mostrar_raio()

#####################################
'''
1. Classe Bola: Crie uma classe que modele uma bola:
Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor
'''

class Bola:
    def __init__(self, cor):
        self.cor = cor

    def trocar_cor(self, outra_cor):
        self.cor = outra_cor


bol = Bola('verde')
print(bol.cor)
bol.trocar_cor('vermelho')
print(bol.cor)
'''

2. Classe Quadrado: Crie uma classe que modele um quadrado:
Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
'''
class Quadrado:
    def __init__(self, tamanho):
        self.tamanho = tamanho

    def mudar_lado(self, tamanho_novo):
        self.tamanho = tamanho_novo

    def retornar_lado(self):
        print(self.tamanho)

    def calcular_area(self):
        print(self.tamanho**2)

quadrado = Quadrado(12)

quadrado.retornar_lado()
quadrado.calcular_area()

quadrado.mudar_lado(20)
quadrado.calcular_area()

'''
3. Classe Retangulo: Crie uma classe que modele um retangulo:

Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local.
Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.
'''
class Retangulo:
    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b

    def mudar_lado(self, novo_a, novo_b):
        self.Lado_a = novo_a
        self.lado_b = novo_b

    def exibir_lados(self):
        return (self.lado_a, self.lado_b)

    def calcular_area(self):
        return (self.lado_a*self.lado_b)

    def calcular_perimetro(self):
        return (2*self.lado_a*self.lado_b)


retangulo = Retangulo(3,5)
retangulo.lado_a
retangulo.lado_b
retangulo.exibir_lados()
print (retangulo.calcular_area())
print(retangulo.calcular_perimetro())

retangulo.mudar_lado(4,6)
print (retangulo.calcular_area())
print(retangulo.calcular_perimetro())


'''
3. Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer.
Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos,
ela deve crescer 0,5 cm

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
'''
