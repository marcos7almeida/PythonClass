# Lista de Exercícios

# Questão 3 - soma
'''
x, y = float(input("x:")), float(input("y:"))

x, y = float(x), float(y)

result = (x + y)

print('A soma é: %s' %result)
'''
# Questão 4
'''
x, y, z, t = float(input("x=")), float(input("y=")), float(input("z=")), float(input("t=")),

media = (x+y+z+t)/4

print ('A média é =%s'%media)
'''
# Questão 5
'''
xm = float(input("x="))

xcm = xm*100
       
print ('O valor em cm é =%s'%xcm)
'''

# Questão 6
'''
raio = float(input("raio="))
import math
pi = math.pi

Area = pi*raio**2

print('Area:%s'%Area)
'''

# Questão 7
'''
l,h = float(input("l=")), float(input("h="))

area = l*h

area2 = 2*area

print('Area duplicada:%s'%area2)
'''
# Questão 8
'''
custohora, horatra = float(input("custohora R$ = ")), float(input("horatra = "))

salario = custohora*horatra

print('salário R$:%s'%salario)
'''

# Questão 9
'''
F = float(input("F:"))

C = 5*(F-32)/9

print ('A temperatura em Celsius é: %s' %C)
'''
# Questão 10
'''
C = float(input("C = "))

F = ((9*C)/5) + 32

print('temp em F =%s'%F)
'''

# Questão 11
'''
I1, I2, R1 = int(input("Inteiro 1 = ")), int(input("Inteiro 2 = ")), float(input("Real = "))

a = 2*I1 + R1/2

b = 3*I1 + R1

c = R1**3

print('a =%s'%a, 'b =%s'%b, 'c =%s'%c )

'''

# Questão 12
'''
altura = float(input("altura = "))

peso = (72.7*altura) - 58

print(' o peso é = %s'%peso)
'''

# Questão 13
'''
alth= float(input("altura do homem = "))
altm= float(input("altura da mulher = "))
pesoh = (72.7*alth) - 58
pesom = (62.1*altm) - 44.7
print(' o peso do homem é = %s'%pesoh, ' o peso da mulher é = %s'%pesom)
'''

# Questão 14
'''
peso= float(input("peso do peixe = "))
pes = abs(1-(peso/50))
import math
pes1 = math.trunc(pes)

print('pes = %s' %pes1)
excesso = pes1*50
multa = excesso*4

print('peso = %s' %peso, 'excesso = %s' %excesso, 'multa = %s' %multa)
'''
# Questão 15
'''
custohora, horatra = float(input("custohora R$ = ")), float(input("horatra = "))

salario = custohora*horatra

IR = 0.11*salario

INSS = 0.08*salario

SIND = 0.05*salario 

SalLiq = salario - INSS - SIND

print('salário R$:%s'%salario, 'IRPF = %s'%IR, 'INSS = %s'%INSS, 'Sindicato = %s'%SIND, 'Salário Líquido = %s'%SalLiq)
'''

# Questão 16

'''
Tam = float(input("Tamanho em m2 = "))

Tinta = Tam/3

Latas = Tinta/18

Preco = Latas*80.00

print('Área (m2):%s'%Tam, 'Quant de Tinta (l)= %s'%Tinta, 'Quant de latas (unidades)= %s'%Latas, 'Preço (R$) = %s'%Preco)



# Questão 17

Tam = float(input("Tamanho em m2 = "))

Tinta = Tam/3

Latas1 = Tinta/18

import math
Latas = math.ceil(Latas1)

Preco = Latas*80.00

print('Área (m2):%s'%Tam, 'Quant de Tinta (l)= %s'%Tinta, 'Quant de latas (unidades)= %s'%Latas, 'Preço (R$) = %0.2f' %Preco)




# Questão 18

import math

quantidade_lata = 18
quantidade_galao = 3.6
rendimento_tinta = 6
galoes = 0
latas = 0

area = int(input("Informe a área a ser pintada: "))
litros_necessarios = (area / rendimento_tinta)

print (litros_necessarios, 'litros são necessários para cobrir a área')

latas = math.floor(litros_necessarios/quantidade_lata)
litros_restantes = litros_necessarios - (latas)
print ("quantidade_lata",latas)
print (litros_restantes, " de tinta restante a comprar")

galoes = math.ceil(litros_restantes/quantidade_galao)

print ("quantidade_galao",galoes)


# Questão 19


Tam = float(input("Entre com o Tamanho do arquivo em Mb = "))

Vel = float(input("Entre com a velocidade do Link em Mbps = "))

tempo = Tam/Vel

tempoM1 = tempo/60

import decimal
import math

tempoM = math.trunc(tempoM1)

index = str(tempoM1).index('.')
tempoS_int = int(str(tempoM1)[0:index])
tempoS_dec = int(str(tempoM1)[index+1:])*60


print ("Tempo em Minutos", tempoS_int)
print ('Tempo em Segundos', tempoS_dec)

print ("Tempo em segundos",tempo, "Tempo em minutos", tempoM)



tamanho = float(input('Tamanho do arquivo (MB): '))
velocidade = float(input('Velocidade de Internet (MBps): '))
print('Tempo aproximado de download: %.0f Minutos ' %((tamanho / velocidade) * 60))

'''

# ATOM
# VSCODE
# SUBLIME(pg)
# VIM
'''
name_1 = "Marcus"
name_2 = "Joe"
string_1 = "olá Marcus"
string_2 = "olá Joe"
if "Marcus" == name_2:
    print(string_1)
else:
    print(" Descule, não entendo")

if "Marcus" == name_2:
    print(string_1)

elif "Joe" == name_2:
    print(string_2)

else:
    print(" Descule, não entendo")
'''
#   == ---> =
#   != ---> diferente
#    < ---> =  <
#    > ---> =  >
#   <= ---> = menor ou igual a 
#   >= ---> = maior ou igual a 

'''
name_1 = "Marcus"
name_2 = "Joe"
string_1 = "olá Marcus"
string_2 = "olá Joe"


number_1 = 3
number_2 = 4.5
number_3 = 3

result_1 = number_1 == number_2
print(result_1)

result_2 = number_1 != number_2
print(result_2)



number_1 = 3
number_2 = 4.5
number_3 = 3

result_7 = not (number_1 ==number_2)
print(result_7)

result_8 = not (number_1 == number_3) or (number_1 == number_2)
print(result_8)

result_9 = not (number_1 == number_3) or (number_1 != number_2)
print(result_9)



number_1 = 5
number_2 = 4.5
number_3 = 6

if number_1 < number_2:
    print(number_1)
else:
    print(number_2)
if number_1 > number_2:
    print(number_1)
else:
    print(number_2)



def ordene(a,b):
   if a<b:
        print(a,b)
   else:
       print(b,a)
x=2
y=3
ordene(x,y)





number_1 = 1
number_2 = 2
number_3 = 3

if (number_1 < number_2) and (number_1 < number_3):
    print(number_1)
    if (number_2 < number_3):
        print(number_2)
        print(number_3)
    else:
        print(number_3)
        print(number_2)
elif (number_2 < number_1) and (number_2 < number_3):
    print(number_2)
    if (number_1 < number_3):
        print(number_1)
        print(number_3)
    else:
        print(number_3)
        print(number_1)  

elif (number_3 < number_1) and (number_3 < number_2):
    print(number_3)
    if (number_1 < number_2):
        print(number_1)
        print(number_2)
    else:
        print(number_2)
        print(number_1)



a=3
b=2

def ordene(a,b):
   if a < b:
        print(a,b)
   else:
       print(b,a)

ordene(a,b)



a=2
b=3

def sorted_numbers(a,b):
    if a < b:
        print(a,b)
    else:
        print(b,a)
        
'''


def sorted_numbers(a,b,c):
    """
>>> sorted_numbers(9,6,7)
    6 7 9
>>> sorted_numbers(8,5,1)
    1 5 8

    
    """
    if a < b and b < c:
        print(a,b,c)
    elif a < c and c < b:
        print(a,c, b)
    elif a < c and c < b:
        print(a,c,b)
    elif b < a and a < c:
        print(b,a,c)
    elif b < c and c < a:
        print(b,c,a)
    elif c < a and a < b:
        print(c,a,b)
    else:
        print(c,b,a)


import doctest
doctest.testmod(verbose=True)

