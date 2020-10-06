#########################################
# Lucas Eduardo Silva Braga - 201570023 #
#########################################

import Complexo, math, cmath

#Exercício 2

r = 0.107
L = 1.355 * 10**(-3)
C = 0.008 * 10**(-6)
f = 60
l = 100
w = 2*math.pi*f

# Circuito Pi Nominal
Z = complex(r,w*L)*l
Z = Complexo.Rect(Z.real, Z.imag)

Y = complex(0,w*C)*l
Yhalf = Y*(1/2)
Yquart = Y*(1/4)
Y = Complexo.Rect(Y.real,Y.imag)
Yhalf = Complexo.Rect(Yhalf.real,Yhalf.imag)
Yquart = Complexo.Rect(Yquart.real,Yquart.imag)


print(f'Para o circuito Pi Nominal, temos que:\n'
      f'   - Z = {Z.polar}\n'
      f'   - Y/2 = {Yhalf.polar} ',end='\n \n')
###############################################################

# Constantes Generalizadas
A = Complexo.ProdutoComplexa(Z,Yhalf)
A = Complexo.SomaComplexa(A,Complexo.Rect(1,0))

B = Z

C = Complexo.ProdutoComplexa(Z,Yquart)

C = Complexo.SomaComplexa(C,Complexo.Rect(1,0))
C = Complexo.ProdutoComplexa(Y, C)

D = A

print('As Constantes Generalizadas foram calculadas:\n'
      f'    - A = {A.polar}\n'
      f'    - B = {B.polar}\n'
      f'    - C = {C.polar}\n'
      f'    - D = {D.polar}',end='\n \n')
##############################################################

# Tensão no Barramento dado uma Carga e a Tensão
Vr = (135*10 **3)/math.sqrt(3)
Vr = Complexo.Polar(Vr, 0)
print(f' Vr = {Vr.polar}')

S = (50*10**6)
S_mono = S/3
angS = math.degrees(math.acos(0.95))
S_mono = Complexo.Polar(S_mono, angS)

ir_conj = Complexo.DivisaoComplexa(S_mono, Vr)
ir = Complexo.ConjugadoComplexo(ir_conj)
print(f' Ir = {ir.polar}')

Vs = Complexo.SomaComplexa(Complexo.ProdutoComplexa(A, Vr), Complexo.ProdutoComplexa(B,ir))
p1 = Complexo.ProdutoComplexa(A, Vr)
p2 = Complexo.ProdutoComplexa(B,ir)
Vs = Complexo.SomaComplexa(p1,p2)
print(f' VS = {Vs.polar}')


Vs_linha = Complexo.ProdutoComplexa(Complexo.Rect(math.sqrt(3),0),Vs)


print('Foram calculados: \n'
      f'    - |Vs| = {Vs_linha.mod/10**3} kV\n'
      f'    - Abertura Angular = {Vs_linha.ang} graus', end='\n \n')

####################################################

# Fluxo de Potência e Rendimento
i_s = Complexo.SomaComplexa(Complexo.ProdutoComplexa(C, Vr), Complexo.ProdutoComplexa(D,ir))
i_s_conj = Complexo.ConjugadoComplexo(i_s)
Ss = Complexo.ProdutoComplexa(Vs, i_s_conj)
Pmono_emi = Ss.rect.real
Qmono_emi = Ss.rect.imag
Ptri_emi = 3*Pmono_emi
Qtri_emi = 3*Qmono_emi


Ptri_recept = 1
#Qtri_recept

rend = ((Ptri_recept)/(Ptri_emi))*100

Consumo = Ptri_emi - Ptri_recept

print('Calculando o Fluxo de Potência, temos: \n'
      f'    - P_trifasica_emissor = {Ptri_emi/10**6} MW\n'
      f'    - Q_trifasica_emissor = {Qtri_emi/10**6} Mvar\n'
      f'    - P_trifasica_receptor = {Ptri_emi/10**6} MW\n'
      f'    - Q_trifasica_receptor = {Qtri_emi/10**6} Mvar'
      f'    - Rendimento = {rend} %\n'
      f'    - Consumo da Linha = {Qtri_emi / 10 ** 6} Mvar'
      , end='\n \n')


#######################################################

# Regulação e Efeito Ferranti

Reg = Complexo.DivisaoComplexa(Vs, A)
Reg = Complexo.SubtracaoComplexa(Reg, Vr)
Reg = Complexo.DivisaoComplexa(Reg,Vr)
Reg = Reg.mod * 100

Ferranti = Vs.mod/Vr.mod

print('Condições de Operação: \n'
      f'    - Regulação de Tensão = {Reg} % \n'
      f'    - Efeito Ferranti = {Ferranti} ', end='\n \n')