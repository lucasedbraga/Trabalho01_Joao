import cmath, math


class ComplexoPolar:
    def __init__(self, z, ang):
        z = float(z.replace(',','.'))
        ang = float(ang.replace(',', '.'))
        ComplexoPolar._rect(self, z, ang)
        ComplexoPolar._pol(self)

    def _rect(self,z ,ang):
        self.rect = cmath.rect(z, math.radians(ang))

    def _pol(self):
        self._pol = cmath.polar(self.rect)
        self.mod = self._pol[0]
        self.ang = math.degrees(self._pol[1])
        self.polar = (self.mod, self.ang)


class ComplexoRect:
    def __init__(self, re, img):
        re = float(re.replace(',', '.'))
        img = float(img.replace(',', '.'))
        self.rect = complex(re,img)
        ComplexoRect._pol(self)

    def _pol(self):
        self._pol = cmath.polar(self.rect)
        self.mod = self._pol[0]
        self.ang = math.degrees(self._pol[1])
        self.polar = (self.mod,self.ang)


def SomaComplexa(a, b):
    soma = a.rect + b.rect
    return soma

def SubtracaoComplexa(a, b):
    sub = a.rect - b.rect
    return sub

def ProdutoComplexa(a, b):
    prod = ((a.mod * b.mod),(a.ang + b.ang))
    return prod

def DivisaoComplexa(a, b):
    divisao = ((a.mod / b.mod), (a.ang - b.ang))
    return divisao