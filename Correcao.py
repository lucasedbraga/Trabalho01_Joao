#########################################
# Lucas Eduardo Silva Braga - 201570023 #
#########################################

import Complexo, math, cmath
import numpy as np

class Hiperbolica:
    def __init__(self,z,y,l):
        Zc = Complexo.DivisaoComplexa(z,y)
        self.Zc = Complexo.RaizFasor(Zc)
        cte_prop = Complexo.ProdutoComplexa(z,y)
        cte_prop = Complexo.RaizFasor(cte_prop)
        cte_prop = cte_prop.rect*l
        self.cte_prop = Complexo.Rect(cte_prop.real,cte_prop.imag)


    def Zlinha(self):
        print(f' Zc = {self.Zc.polar} \n')
        print(f' Lambda*l = {self.cte_prop.polar} \n')
        zlinha = self.Zc.rect*np.sinh(self.cte_prop.rect)
        zlinha = Complexo.Rect(zlinha.real,zlinha.imag)
        return zlinha

    def Ylinha(self):
        ylinha = 2*(1/self.Zc.rect)*((np.cosh(self.cte_prop.rect)-1)/np.sinh(self.cte_prop.rect))
        ylinha = Complexo.Rect(ylinha.real, ylinha.imag)
        return ylinha