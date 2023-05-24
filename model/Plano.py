from .Objeto import *
import numpy as np
from .constants import *

class Plano(Objeto):
    def __init__(self, punto, normal,
             reflection, refraction, diffuse_c, specular_c, color = None,):
        if not color:
            color = (lambda M: (color_plane0 if (int(M[0] * 2) % 2) == (int(M[1] * 2) % 2) else color_plane1))
        super().__init__(color, reflection, refraction, diffuse_c, specular_c)
        self.punto = punto
        self.normal = normal
    
    def intersectar(self, rayo):
        Origen = rayo.origen
        Direccion = rayo.direccion
        denom = np.dot(Direccion, self.normal)
        if np.abs(denom) < 1e-6:
            return np.inf
        d = np.dot(self.punto - Origen, self.normal) / denom
        if d < 0:
            return np.inf
        return d
    
    def calcular_normal(self, M):
        return self.normal

    def calcular_color(self, M):
        return self.color(M)


if __name__ == "__main__":
    print("Plano.py")