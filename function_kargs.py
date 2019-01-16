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

def soma(*args,**kwargs):

    '''
    soma (x,y,z,....) ----> result
    '''
    #import pdb; pdb.set_trace() # forma tradicional
    breakpoint()#novo em python 3.7
    return sum(args) + sum(kwargs.values())

#    res = x + y
#    args_locals = locals()
#    print(args_locals)
    print(type(args))
    return x + x1 + sum(args)

#args_globals = globals()

if __name__ == '__main__':
    l=[1,1]
    d={'x':2, 'x1':2, 'x2':2}



#    resulta = soma(2)
#    print(resulta)
#    l = [1,2,3,4]
#    print(soma(*l))
    print(soma(**d))
#print(args_globals)
#print(args_globals['__name__'])
#print(__name__)
