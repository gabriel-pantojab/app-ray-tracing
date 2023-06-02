from .Objeto import *
import numpy as np
from .constants import *

class Plano(Objeto):
    def __init__(self, punto, normal,
             reflexion, reflexion_difusa, reflexion_especular, color):
        super().__init__(color, reflexion, reflexion_difusa, reflexion_especular)
        self.punto = punto
        self.normal = normal
    
    def intersectar(self, rayo):
        Origen = rayo.origen
        Direccion = rayo.direccion
        denominador = np.dot(Direccion, self.normal)
        if np.abs(denominador) < 1e-6:
            return np.inf
        d = np.dot(self.punto - Origen, self.normal) / denominador
        if d < 0:
            return np.inf
        return d
    
    def calcular_normal(self, M):
        return self.normal

    def calcular_color(self, M):
        if not hasattr(self.color, '__len__') : return self.color(M)
        else : return self.color


if __name__ == "__main__":
    print("Plano.py")