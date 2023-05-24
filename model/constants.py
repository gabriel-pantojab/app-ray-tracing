import numpy as np
from .Camara import Camara

w = 700
h = 400

camara = Camara(np.array([0., 0.3, -1.]), np.array([0., 0., 0.]))

color_plane0 = 1. * np.ones(3)
#color_plane0 = np.array([1., 0., .0])
#color_plane1 = 0. * np.zeros(3)
color_plane1 = np.array([0., 1., .0])

# Light position and color.
Luz = np.array([5., 5., -5.])
color_light = np.ones(3)

# Default light and material parameters.
ambient = .05
diffuse_c = 1.
specular_c = 1.
specular_k = 50
refraction = 1

depth_max = 5  # Maximum number of light reflections.

col = np.zeros(3)  # Current color.

r = float(w) / h
# Screen coordinates: x0, y0, x1, y1.
pantalla = (-1.,
            -1. / r + .25,
            1.,
            1. / r + .25)

img = np.zeros((h, w, 3))

'''scene = [
        Esfera(np.array([-1., .5, 1.]), .6, np.array([0., 0., 1.]), reflection=0, refraction=1.),
        Esfera(np.array([.5, .5, 1.5]), .6, np.array([.5, .223, .5]), reflection=.5, refraction=1.),
        Esfera(np.array([1., .5, 2.]), .6, np.array([1., .572, .184]), reflection=.5, refraction=1.),
        Plano(np.array([0., -.5, 0.]), np.array([0., 1., 0.]), reflection=.5, refraction=1., diffuse_c=.75, specular_c=.5),
    ]'''