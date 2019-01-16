
def test():
    import doctest
    doctest.testmod(verbose=True)

def lista_2_ex_5(media):
    """
    Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    A mensagem "Reprovado", se a média for menor do que sete;
    A mensagem "Aprovado com Distinção", se a média for igual a dez.

    >>> lista_2_ex_5(10.0)
    Aprovado com Distinção
    >>> lista_2_ex_5(6.0)
    Reprovado
    >>> lista_2_ex_5(7.0)
    Aprovado
    """


    if(media) == 10.0:
        print("Aprovado com Distinção")
    elif(media) < 7.0:
        print("Reprovado") 
    else:
        print("Aprovado")
        
n1,n2 = float(input("digite nota: n1= ")), float(input("digite nota: n2= "))

med = (n1+n2)/2
print ('A média é =%s'%med)
test()

lista_2_ex_5(med)
#print(lista_2_ex_5)
#print(help(lista_2_ex_5))











