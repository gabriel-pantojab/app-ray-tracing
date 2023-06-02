class Objeto:
    def __init__(self, color, reflexion, reflexion_difusa=1., reflexion_especular=1.):
        self.color = color
        self.reflexion = reflexion
        self.reflexion_difusa = reflexion_difusa
        self.reflexion_especular = reflexion_especular

    def intersectar(self, rayo):
        pass
    
    def calcular_normal(self, M):
        pass
    
    def calcular_color(self, M):
        pass

