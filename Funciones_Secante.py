# Funciones Secante 

# %% Librerías
import math

# %% Funciones a evaluar
def f(p):
    f = p - (0.5*math.tan(p))
    return f

# %% Errores
def Errores(tipErr,p,z):
    if tipErr == 1:
        E = abs(p-z)
    elif tipErr == 2:
        E = abs((p-z)/(p))
    elif tipErr == 3:
        E = abs((p-z)/(p))*100.0
    return E