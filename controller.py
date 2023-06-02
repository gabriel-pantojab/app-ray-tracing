from model.RayTracing import RayTracing
import numpy as np
import model.constants as cnst
from model.utils import normalizar_vector
from model.Rayo import Rayo
from matplotlib import pyplot as plt
import threading as th
import tkinter as tk
from PopupEsfera import PopupEsfera
import os

class Controller:
    def __init__(self, app):
        self.app = app
        self.app.run_button.configure(command=lambda: self.run_algorithm())
        self.app.clear_button.configure(command=lambda: self.clear())
        self.app.add_sefera_button.configure(command=lambda: self.popup_esfera())

        self.escena = self.app.escena
        self.model = RayTracing(self.escena)
        self.camara = cnst.camara

        self.app.mainloop()

    def disable_buttons(self):
        self.app.run_button.configure(state=tk.DISABLED)
        self.app.clear_button.configure(state=tk.DISABLED)
        self.app.add_sefera_button.configure(state=tk.DISABLED)
        self.app.generar_escena_button.configure(state=tk.DISABLED)
        self.app.cargar_escena_button.configure(state=tk.DISABLED)

    def enable_buttons(self):
        self.app.clear_button.configure(state=tk.NORMAL)
        self.app.cargar_escena_button.configure(state=tk.NORMAL)

    def popup_esfera(self):
        PopupEsfera(self.app)

    def clear(self):
        self.app.clear()

    def run_algorithm(self):
        self.disable_buttons()
        self.app.loading_label.configure(image="")
        self.hilo = th.Thread(target=self.run_ray_tracing)
        self.hilo.start()

    def run_ray_tracing(self):
        col = np.zeros(3)  # Current color.
        for i, x in enumerate(np.linspace(cnst.pantalla[0], cnst.pantalla[2], cnst.w)):
            if i % 10 == 0:
                t = str(int(i / float(cnst.w) * 100))
                self.app.loading_label.configure(text="Procesando... " + t + "%")
            for j, y in enumerate(np.linspace(cnst.pantalla[1], cnst.pantalla[3], cnst.h)):
                col[:] = 0
                #cambia la direccion de la camara
                self.camara.direccion = np.array([x, y, 0])
                
                D = normalizar_vector(self.camara.direccion - self.camara.posicion)
                rayO = self.camara.posicion
                rayD = D
                col = self.model.ray_tracing(Rayo(rayO, rayD))
                cnst.img[cnst.h - j - 1, i, :] = np.clip(col, 0, 1)

        plt.imsave('./resultado/app.png', cnst.img)
        self.app.update_img()
        self.enable_buttons()