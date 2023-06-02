import numpy as np
from .Camara import Camara

w = 700
h = 400

camara = Camara(np.array([0., 0.3, -1.]), np.array([0., 0., 0.]))

# Posición de la luz y color.
Luz = np.array([5., 5., -5.])
color_luz = np.ones(3)


ambiente = .05
reflexion_difusa = 1.
reflexion_especular = 1.
especular_k = 50

depth_max = 5 # Profundidad maxima de recursion

col = np.zeros(3) # color actual

r = float(w) / h
# Coordenadas de la pantalla
pantalla = (-1.,
            -1. / r + .25,
            1.,
            1. / r + .25)

img = np.zeros((h, w, 3))

color_plane0 = 1. * np.ones(3)
#color_plane0 = np.array([1., 0., .0])
#color_plane1 = 0. * np.zeros(3)
color_plane1 = np.array([0., 1., .0])