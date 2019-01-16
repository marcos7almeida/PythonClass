
def test():
    import doctest
    doctest.testmod(verbose=True)

def sorted_numbers(a,b,c):
    
    """
    >>> sorted_numbers(9,6,7)
    6,7,9
    >>> sorted_numbers(8,5,1)
    1,5,8
    >>> sorted_numbers(2,6,7)
    2,6,7
    """

    if a < b and b < c:
        print(a,b,c)
    elif a < c and c < b:
        print(a,c,b)
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
        
a,b,c = float(input("digite o número 1: a= ")), float(input("digite o número 2: b= ")), float(input("digite o número 3: c= "))

test()

sorted_numbers(a,b,c)
#lista_2_ex_9(a,b,c)
#print(lista_2_ex_9)
#print(help(lista_2_ex_9))


    














