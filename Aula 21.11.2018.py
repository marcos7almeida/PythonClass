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
"""
N = int(input("Digite a quantidade da serie de Fib =  "))
fib = [0,1,1]
for i in range(3,N):
        fib.append(fib[i-1] + fib[i-2]) #fib += (fib[i-1] + fib[i-2])

for seq in fib:
    print(seq)
