
def test():
    import doctest
    doctest.testmod(verbose=True)

def lista_2_ex_6(n1,n2,n3):
    """
    Faça um Programa que leia três números e mostre o maior deles.

    >>> lista_2_ex_6(1,2,3)
    3
    >>> lista_2_ex_6(9,10,8)
    10
    >>> lista_2_ex_6(4,1,2)
    
    """

    if (n1 > n2) and (n1 > n3):
        print(n1)
    elif (n2 > n1) and (n2 > n3):
        print(n2)
    elif (n3 > n1) and (n3 > n2):
        print(n3)
        
n1,n2,n3 = float(input("digite nota: n1= ")), float(input("digite nota: n2= ")), float(input("digite nota: n3= "))

test()

lista_2_ex_6(n1,n2,n3)
#print(lista_2_ex_6)
#print(help(lista_2_ex_6))











