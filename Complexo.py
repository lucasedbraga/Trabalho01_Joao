#########################################
# Lucas Eduardo Silva Braga - 201570023 #
#########################################

import cmath, math

class Polar:
    def __init__(self, z, ang):
        if z is str:
            z = float(z.replace(',','.'))
        if ang is str:
            ang = float(ang.replace(',', '.'))
        Polar._rect(self, z, ang)
        Polar._pol(self)

    def _rect(self,z ,ang):
        self.rect = cmath.rect(z, math.radians(ang))

    def _pol(self):
        self._pol = cmath.polar(self.rect)
        self.mod = self._pol[0]
        self.ang = math.degrees(self._pol[1])
        self.polar = (self.mod, self.ang)


class Rect:

    def __init__(self, re, img):
        if re is str:
            re = float(re.replace(',', '.'))
        if img is str:
            img = float(img.replace(',', '.'))
        self.rect = complex(re,img)
        Rect._pol(self)

    def _pol(self):
        self._pol = cmath.polar(self.rect)
        self.mod = self._pol[0]
        self.ang = math.degrees(self._pol[1])
        self.polar = (self.mod,self.ang)


def SomaComplexa(a, b):
    soma = a.rect + b.rect
    soma = Rect(soma.real, soma.imag)
    return soma

def SubtracaoComplexa(a, b):
    sub = a.rect - b.rect
    sub = Rect(sub.real, sub.imag)
    return sub

def ProdutoComplexa(a, b):
    prod = [a.mod * b.mod, a.ang + b.ang]
    prod = Polar(prod[0], prod[1])
    return prod

def DivisaoComplexa(a, b):
    divisao = [a.mod / b.mod, a.ang - b.ang]
    divisao = Polar(divisao[0], divisao[1])
    return divisao

def ConjugadoComplexo(a):
    conjugado = Rect(a.rect.real, -a.rect.imag)
    return conjugado


x = cmath.rect(83.5019,6.7318)
print(x)