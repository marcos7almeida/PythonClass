
def test():
    import doctest
    doctest.testmod(verbose=True)

def lista_2_ex_8(p1,p2,p3):
    """
    Faça um programa que pergunte o preço de três produtos e informe
    qual produto você deve comprar, sabendo que a decisão é sempre pelo
    mais barato.

    >>> lista_2_ex_8(1.00,2.00,3.00)
    O menor preço é: 1.00
    >>> lista_2_ex_8(9.00,8.00,10.00)
    O menor preço é: 8.00
    >>> lista_2_ex_8(4.00,3.00,2.00)
    O menor preço é: 2.00
    """

    if (p1 < p2) and (p1 < p3):
        print(f"O menor preço é: {p1:0.2f}")
    elif (p2 < p1) and (p2 < p3):
        print(f"O menor preço é: {p2:0.2f}")
    elif (p3 < p1) and (p3 < p2):
        print(f"O menor preço é: {p3:0.2f}")
        
p1,p2,p3 = float(input("digite preço 1: p1= ")), float(input("digite preço 2: p2= ")), float(input("digite preço 3: p3= "))

test()

lista_2_ex_8(p1,p2,p3)
#print(lista_2_ex_8)
#print(help(lista_2_ex_8))


    













