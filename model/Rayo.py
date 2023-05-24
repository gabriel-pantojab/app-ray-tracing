class Rayo:
    def __init__(self, origen, direccion):
        self.origen = origen
        self.direccion = direccion
    
    def punto(self, t):
        return self.origen + self.direccion * t
    
    def __str__(self):
        return "Origen: " + str(self.origen) + " Direccion: " + str(self.direccion)
