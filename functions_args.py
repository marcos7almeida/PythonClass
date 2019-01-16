################## Módulos  ############

# variáveis locais estão dentro da função
# variáveis globais estão dentro do programa
"""
documentação da soma
"""

#print(__doc__)
#print(__file__)

#import builtins

# print(dir(builtins))

#import math

def soma(x, y):

    '''
    soma (x, y) ----> result
    '''
    res = x + y
#    args_locals = locals()
#    print(args_locals)
    return res

args_globals = globals()

if __name__ == '__main__':
    resulta = soma(2, 3)
    print(resulta)

#print(args_globals)
#print(args_globals['__name__'])
#print(__name__)
