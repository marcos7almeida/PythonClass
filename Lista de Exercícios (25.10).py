def test():
    import doctest
    doctest.testmod(verbose=True)
def lista_2_ex_4(letra):
    """
    Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
    >>> lista_2_ex_4('V')
    Vogal
    >>> lista_2_ex_4('C')
    Consoante
    """
    
    lista = ["a","e","i","o","u","A","E","I","O","U"]
    if(letra) in lista:
        print("Vogal")
    else:
        print("Consoante")
    
letra = input("Digite uma letra= ")

test()

lista_2_ex_4(letra)
#print(lista_2_ex_4)
#print(help(lista_2_ex_4))











