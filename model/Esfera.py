import numpy as np
from .Objeto import Objeto
from .utils import normalizar_vector

class Esfera(Objeto):
    def __init__(self, centro, radio, color, reflection, refraction=0):
        super().__init__(color, reflection, refraction)
        self.centro = centro
        self.radio = radio
    
    def intersectar(self, rayo):
      Origen = rayo.origen
      Direccion = rayo.direccion
      a = np.dot(Direccion, Direccion)
      OS = Origen - self.centro
      b = 2 * np.dot(Direccion, OS)
      c = np.dot(OS, OS) - self.radio * self.radio
      disc = b * b - 4 * a * c
      if disc > 0:
        distSqrt = np.sqrt(disc)
        q = (-b - distSqrt) / 2.0 if b < 0 else (-b + distSqrt) / 2.0
        t0 = q / a
        t1 = c / q
        t0, t1 = min(t0, t1), max(t0, t1)
        if t1 >= 0:
            return t1 if t0 < 0 else t0
      return np.inf
    
    def calcular_normal(self, M):
        return normalizar_vector(M - self.centro)

    def calcular_color(self, M):
        return self.color
    

if __name__ == '__main__':
    print(__package__)