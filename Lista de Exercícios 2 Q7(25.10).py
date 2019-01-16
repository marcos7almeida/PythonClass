
def test():
    import doctest
    doctest.testmod(verbose=True)

def lista_2_ex_7(n1,n2,n3):
    """
    Faça um Programa que leia três números e mostre o maior e o menor deles

    >>> lista_2_ex_7(1,2,3)
    O maior número é:  3 O menor número é:  1
    >>> lista_2_ex_7(9,10,8)
    O maior número é:  10 O menor número é:  8
    >>> lista_2_ex_7(4,1,2)
    O maior número é:  4 O menor número é:  1
    """

    if (n1 > n2) and (n1 > n3):
        maxi = n1
    elif (n2 > n1) and (n2 > n3):
        maxi = n2
    else:
        maxi = n3
        
    if (n1 < n2) and (n1 < n3):
        mini = n1
    elif (n2 < n1) and (n2 < n3):
        mini = n2
    else:
        mini = n3

    print("O maior número é: ", maxi, "O menor número é: ", mini)

n1,n2,n3 = float(input("digite nota: n1= ")), float(input("digite nota: n2= ")), float(input("digite nota: n3= "))

test()

lista_2_ex_7(n1,n2,n3)
#print(lista_2_ex_7)
#print(help(lista_2_ex_7))











