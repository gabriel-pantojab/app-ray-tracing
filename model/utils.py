import numpy as np

def normalizar_vector(x):
    x /= np.linalg.norm(x)
    return x

def normalizar_color(color):
    r = color[0] * 1 / 255
    g = color[1] * 1 / 255
    b = color[2] * 1 / 255
    return [r, g, b]

if __name__ == '__main__':
    print(__package__)