#########################################
# Lucas Eduardo Silva Braga - 201570023 #
#########################################

import Complexo, math, cmath
import numpy as np

def Correceao(z,y):
    Zc = math.sqrt((z / y))
    cte_prop = math.sqrt(z * y)
    return Zc, cte_prop

def Zlinha(z,y,l):
    Zc, cte_prop = Correceao(z,y)
    zlinha = Zc*np.sinh(cte_prop*l)
    return zlinha

def Ylinha(z,y,l):
    Zc, cte_prop = Correceao(z, y)
    ylinha = (1/Zc)*((np.cosh(cte_prop*l)-1)/np.sinh(cte_prop*l))
    return ylinha