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
        toL = normalizar_vector(cnst.Luz - punto_interseccion)
        toO = normalizar_vector(cnst.camara.posicion - punto_interseccion)

        # Sombras
        l = [obj_sh.intersectar(Rayo(punto_interseccion + normal_punto_interseccion * .0001, toL)) 
                for k, obj_sh in enumerate(self.escena) if k != obj_idx]

        if l and min(l) < np.inf:
            return np.array([.0, .0, 0.0])

        # Modelo de Phong
        col_ray = cnst.ambient
        # Lambert shading (diffuse).
        col_ray += obj.diffuse_c * max(np.dot(normal_punto_interseccion, toL), 0) * color
        # Blinn-Phong shading (specular).
        col_ray += obj.specular_c * max(np.dot(normal_punto_interseccion, normalizar_vector(toL + toO)), 0) ** cnst.specular_k * cnst.color_light

        if obj.reflection > 0:
            # Nuevo rayo
            rayO = punto_interseccion + normal_punto_interseccion * .0001
            rayD = normalizar_vector(rayo.direccion - 2 * np.dot(rayo.direccion, normal_punto_interseccion) * normal_punto_interseccion)
            col_ray =  col_ray + obj.reflection * self.ray_tracing(Rayo(rayO, rayD), depth + 1)

        return col_ray
    
if __name__ == "__main__":
    scene = [
        Esfera(np.array([-1., .5, 1.]), .6, np.array([0., 0., 1.]), reflection=0, refraction=1.),
        Esfera(np.array([.5, .5, 1.5]), .6, np.array([.5, .223, .5]), reflection=.5, refraction=1.),
        Esfera(np.array([1., .5, 2.]), .6, np.array([1., .572, .184]), reflection=.5, refraction=1.),
        Plano(np.array([0., -.5, 0.]), np.array([0., 1., 0.]), reflection=.5, refraction=1., diffuse_c=.75, specular_c=.5),
    ]
    rayTracing = RayTracing()
    #rayTracing.run_ray_tracing(scene)
    print("Hola mundo desde RayTracing.py")