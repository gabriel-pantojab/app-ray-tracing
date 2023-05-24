class Objeto:
    def __init__(self, color, reflection, refraction, diffuse_c=1., specular_c=1.):
        self.color = color
        self.reflection = reflection
        self.refraction = refraction
        self.diffuse_c = diffuse_c
        self.specular_c = specular_c

    def intersectar(self, rayo):
        pass
    
    def calcular_normal(self, M):
        pass
    
    def calcular_color(self, M):
        pass