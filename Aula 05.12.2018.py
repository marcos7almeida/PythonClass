
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
"""

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
