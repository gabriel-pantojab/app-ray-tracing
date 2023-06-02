import numpy as np
from .utils import normalizar_vector
import model.constants as cnst
from .Rayo import Rayo

#Pra prueba
from .Esfera import Esfera
from .Plano import Plano



class RayTracing:
    def __init__(self, escena):
        self.escena = escena

    def ray_tracing(self, rayo, depth=0):
        if depth > cnst.depth_max:
            return np.array([.0, .0, 0.0])
        
        # Encotrar el objeto mas cercano
        t = np.inf
        for i, obj in enumerate(self.escena):
            t_obj = obj.intersectar(rayo)
            if t_obj < t:
                t, obj_idx = t_obj, i
        
        # Si no hay interseccion
        if t == np.inf:
            return np.array([.0, .0, 0.0])
    
        obj = self.escena[obj_idx]
        punto_interseccion = rayo.punto(t)
        normal_punto_interseccion = obj.calcular_normal(punto_interseccion)

        color = obj.calcular_color(punto_interseccion)
        hacia_camara = normalizar_vector(cnst.camara.posicion - punto_interseccion)

        hacia_luz = normalizar_vector(cnst.Luz - punto_interseccion)
        # Sombras
        l = [obj_sh.intersectar(
                Rayo(punto_interseccion + normal_punto_interseccion * .0001, hacia_luz)) 
                for k, obj_sh in enumerate(self.escena) if k != obj_idx]

        if l and min(l) < np.inf:
            return np.array([.0, .0, 0.0])

        # Modelo de Phong
        col_ray = cnst.ambiente
        # Lambert shading (diffuse).
        col_ray += obj.reflexion_difusa * max(np.dot(normal_punto_interseccion, hacia_luz), 0) * color
        # Blinn-Phong shading (specular).
        col_ray += (
            obj.reflexion_especular
            * max(np.dot(normal_punto_interseccion, normalizar_vector(hacia_luz + hacia_camara)), 0)
            ** cnst.especular_k
            * cnst.color_luz)

        if obj.reflexion > 0:
            # Nuevo rayo
            rayO = punto_interseccion + normal_punto_interseccion * .0001
            rayD = (
                normalizar_vector(
                    rayo.direccion - 2
                    * np.dot(rayo.direccion, normal_punto_interseccion
                )
                * normal_punto_interseccion))
            col_ray =  col_ray + obj.reflexion * self.ray_tracing(Rayo(rayO, rayD), depth + 1)

        return col_ray