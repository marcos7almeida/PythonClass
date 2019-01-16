# x = input("x:")
# print('O número informado foi: %s' %x)

#####

# print(f"O número informado foi {input('Qual é o número:')}")

# x, y, z, t = float(input("x:")), float(input("y:")), float(input("z:")), float(input("t:")) 

# x, y, z, t = float(x), float(y),  float(z),  float(t)

# result = (x + y + z + t)/4

# print('A média é: %s' %result)

####

# F = float(input("F:"))

# C = 5*(F-32)/9

# print ('A temperatura em Celsius é: %s' %C)

#%%%%%%%%%%%%%%%%%%%%%%%

# str_list = ['U','F','P','E']

# print(str_list[0:4:2])
# print(str_list[1:4:1])
# print(str_list[2::])
# print(str_list[3::])

# [start: end: step]

# %%%%%%%%%%%%%%%%%

# linguagem = "python"

# caracter = list(linguagem)

# print(caracter)

# palavra = ".".join(caracter)
# print(palavra)

# %%%%%%%%%%%%%%%%%
'''
matrix = [0]
matrix = matrix*3
print(matrix)
matrix[1] = 2
print(matrix)
'''
'''
M = [[0,0,0]]*3
print(M)
print(M[0])
print(M[0][1])

M[0][1]=1
print(M)

# abertura de arquivo -> dictionary

# Arrays = List (order, changeable)/ Tupla / Set / Dictionary

'''

this_list = ["apple", "banana", "cherry"]
this_list[1] = ["blackcurrant"]
print(this_list)
print(len(this_list))
this_list.append("orange")
print(this_list)
this_list.append("orange")
this_list[4] = ["tee", "coffee"]
print(this_list)
this_list.append(["tee", "coffee"])
print(this_list)
this_list.insert(1,"orange")
print(this_list)
this_list.remove("orange")
print(this_list)
this_list.pop()
print(this_list.pop())
print(this_list)

del this_list[0]
print(this_list)

# Tela -> Monokai  // VScode

del this_list [0:2]
print(this_list)

this_list = ["apple", "banana", "cherry"]
print(this_list)
this_list.clear()
print(this_list)

# The list() Constructor
this_list = list(("apple", "banana", "cherry"))
print(this_list)

# List Methods --> dir()

list_all_methods = dir(list)
print(list_all_methods)


help([].append)

help([])


# Look up

# list.append(self, value)
# list.clear(self)
# list.insert(self, index, value)
# list.pop(self, index=-1)
# list.remove(self, value)

# list.copy(self)
# list.count(self, value)
# list.extend(self, iterable)
# list.index(self, value, start=0, stop=len(self))
# list.reverse(self)
# list.sort(self, key=None, reverse=False)

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

a_fruits = fruits
b_fruits = fruits.copy()

id_a = id(a_fruits)
id_b = id(b_fruits)
id_c = id(fruits)

print(id_a ==id_c)
print(id_b ==id_c)


fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

print(fruits.count('apple'))
print(fruits.count('tangerine'))

print(fruits.index('banana'))
print(fruits.index('banana', 4))

'''
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

fruits.reverse()
print(fruits)

fruits.sort()
print(fruits)

fruits.sort(reverse = True)
print(fruits)

'''


'''
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

fruits.sort(key=lambda f: f[-1])
print(fruits)

fruits.sort(key=lambda f: f[2])
print(fruits)




fruits = ['orange', 'apple', 'pear']

add_fruits = ['banana', 'kiwi', 'apple', 'banana']

fruits.append(add_fruits)
print(fruits)

fruits.pop()
print(fruits)

fruits.extend(add_fruits)
print(fruits)

'''
# Max and Min


points = [5.3, 6,7,8,10]

max_point = max(points)
min_point = min(points)
print(max_point)
print(min_point)

'''


'''
this_list = ['apple', 'banana', 'cherry']
for x in this_list:
    print(x)



X = [1,2,3,4]
sum = 0
for n in x:
    sum+=n
    mean=sum/4


    # sqrt = Num**(0.5)

'''
'''
X = [5,2,3,10]
n = len(X)
sum=0
for _X in X:
    sum = sum+_X    #(sum+=_X)
mean = sum/n
print(sum)
print(mean)

sum1=0
for k in X:
    erro1=(k-mean)
    erro=erro1**2
    sum1=sum1+erro
mean_erro = sum1/n
sigma = mean_erro**0.5

print(sigma)

standard_mean = sum1/n-1

standard = standard_mean**0.5
    
print(standard)
'''

#range[start, end-1, step]
'''
l=[4,3,2,1]
X = [5,2,3,10]
n = len(X)
sum=0
for x in range(n):
    sum+=l[x]
print(sum)

'''

'''
'''
% phyton



R=[]
r = [0,0]
R.append(r)
R = []
R.append(r)
R


Microsoft Windows [versão 10.0.17134.285]
(c) 2018 Microsoft Corporation. Todos os direitos reservados.

C:\Users\Marcos Almeida>python
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>  R = [i for i in range(2)]
  File "<stdin>", line 1
    R = [i for i in range(2)]
    ^
IndentationError: unexpected indent
>>> R = [i for i in range(2)]
>>> R
[0, 1]
>>> R = []
>>> for i in range(2)
  File "<stdin>", line 1
    for i in range(2)
                    ^
SyntaxError: invalid syntax
>>> for i in range(2)
  File "<stdin>", line 1
    for i in range(2)
                    ^
SyntaxError: invalid syntax
>>> for i in range(2):
...     R.append(i)
... R
  File "<stdin>", line 3
    R
    ^
SyntaxError: invalid syntax
>>>     R.append(i)
  File "<stdin>", line 1
    R.append(i)
    ^
IndentationError: unexpected indent
>>> for i in range(2):
...     R.append(i)
...
>>> R
[0, 1]
>>>

'''





# >>> R = [i for i in range(2)]


R = [[i+j for i in range(2)] for j in range(2)]











    






