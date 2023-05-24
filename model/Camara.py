import numpy as np
class Camara:
    def __init__(self, posicion, direccion = np.array([0, 0, 0])):
        self.posicion = posicion
        self.direccion = direccion