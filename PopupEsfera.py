import customtkinter as tk
import os
from model.Esfera import Esfera
import json as js
import model.utils as utils

class PopupEsfera(tk.CTkToplevel):
    def __init__(self, padre):
        super().__init__()
        self.title("Esfera")
        self.geometry("330x220+10+10")
        self.resizable(False, False)

        self.padre = padre

        self.frame = tk.CTkFrame(self)
        self.frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=1)
        self.frame.rowconfigure(2, weight=1)

        self.frame_position = tk.CTkFrame(self.frame)
        self.frame_position.grid(row=0, column=0, sticky=tk.NSEW)
        self.frame_position.columnconfigure(0, weight=1)
        self.frame_position.columnconfigure(1, weight=1)

        self.label = tk.CTkLabel(self.frame_position, text="Centro")
        self.label.grid(row=0, column=0, sticky=tk.NSEW, columnspan=2)

        self.label_x = tk.CTkLabel(self.frame_position, text="X: [-2.1, 2.1]")
        self.entry_x = tk.CTkEntry(self.frame_position, width=50)
        self.label_x.grid(row=1, column=0, sticky=tk.NSEW)
        self.entry_x.grid(row=1, column=1, sticky=tk.NSEW, padx=5)

        self.label_y = tk.CTkLabel(self.frame_position, text="Y: [-0.5, 1.3]")
        self.entry_y = tk.CTkEntry(self.frame_position, width=40)
        self.label_y.grid(row=2, column=0, sticky=tk.NSEW)
        self.entry_y.grid(row=2, column=1, sticky=tk.NSEW, padx=5)

        self.label_z = tk.CTkLabel(self.frame_position, text="Z: [ 1.5, 5.0]")
        self.entry_z = tk.CTkEntry(self.frame_position, width=40)
        self.label_z.grid(row=3, column=0, sticky=tk.NSEW)
        self.entry_z.grid(row=3, column=1, sticky=tk.NSEW, padx=5)

        self.frame_radio = tk.CTkFrame(self.frame)
        self.frame_radio.grid(row=1, column=0, sticky=tk.NSEW)
        self.frame_radio.columnconfigure(0, weight=1)

        self.label_radio = tk.CTkLabel(self.frame_radio, text="Radio: [0.1, 1]")
        self.entry_radio = tk.CTkEntry(self.frame_radio, width=40)
        self.label_radio.grid(row=0, column=0, sticky=tk.NSEW)
        self.entry_radio.grid(row=0, column=1, sticky=tk.NSEW, padx=5)

        self.frame_color = tk.CTkFrame(self.frame)
        self.frame_color.grid(row=0, column=1, sticky=tk.NSEW)
        self.frame_color.columnconfigure(0, weight=1)
        self.frame_color.columnconfigure(1, weight=1)

        self.label = tk.CTkLabel(self.frame_color, text="Color")
        self.label.grid(row=0, column=0, sticky=tk.NSEW, columnspan=2)

        self.label_r = tk.CTkLabel(self.frame_color, text="R: [0, 255]")
        self.entry_r = tk.CTkEntry(self.frame_color, width=40)
        self.label_r.grid(row=1, column=0, sticky=tk.NSEW)
        self.entry_r.grid(row=1, column=1, sticky=tk.NSEW, padx=5)

        self.label_g = tk.CTkLabel(self.frame_color, text="G: [0, 255]")
        self.entry_g = tk.CTkEntry(self.frame_color, width=40)
        self.label_g.grid(row=2, column=0, sticky=tk.NSEW)
        self.entry_g.grid(row=2, column=1, sticky=tk.NSEW, padx=5)

        self.label_b = tk.CTkLabel(self.frame_color, text="B: [0, 255]")
        self.entry_b = tk.CTkEntry(self.frame_color, width=40)
        self.label_b.grid(row=3, column=0, sticky=tk.NSEW)
        self.entry_b.grid(row=3, column=1, sticky=tk.NSEW, padx=5)

        self.frame_reflection = tk.CTkFrame(self.frame)
        self.frame_reflection.grid(row=1, column=1, sticky=tk.NSEW)
        self.frame_reflection.columnconfigure(0, weight=1)

        self.label_reflection = tk.CTkLabel(self.frame_reflection, text="Reflection: [0, 1]")
        self.entry_reflection = tk.CTkEntry(self.frame_reflection, width=40)
        self.label_reflection.grid(row=0, column=0, sticky=tk.NSEW)
        self.entry_reflection.grid(row=0, column=1, sticky=tk.NSEW, padx=5)

        '''self.frame_refraction = tk.CTkFrame(self.frame)
        self.frame_refraction.pack(fill=tk.BOTH, expand=True, ipadx=10, ipady=10)

        self.label_refraction = tk.CTkLabel(self.frame_refraction, text="Refraction: [0, 1]")
        self.entry_refraction = tk.CTkEntry(self.frame_refraction, width=40)
        self.label_refraction.grid(row=0, column=0, sticky=tk.NSEW)
        self.entry_refraction.grid(row=0, column=1, sticky=tk.NSEW)'''

        self.frame_buttons = tk.CTkFrame(self.frame)
        self.frame_buttons.grid(row=2, column=0, columnspan=2, sticky=tk.NSEW, ipadx=10)
        self.frame_buttons.columnconfigure(0, weight=1)
        self.frame_buttons.columnconfigure(1, weight=1)
        self.frame_buttons.rowconfigure(0, weight=1)

        self.button_agregar = tk.CTkButton(self.frame_buttons, text="Agregar", command=lambda: self.get_esfera())
        self.button_agregar.grid(row=0, column=0, sticky=tk.NSEW, padx=10)

        self.button_cancelar = tk.CTkButton(self.frame_buttons, text="Cancelar", command=lambda: self.destroy())
        self.button_cancelar.grid(row=0, column=1, sticky=tk.NSEW, padx=10)

    
    def get_esfera(self):
        centro = ([float(self.entry_x.get()), float(self.entry_y.get()), float(self.entry_z.get())])
        radio = float(self.entry_radio.get())
        color = utils.normalizar_color([float(self.entry_r.get()), float(self.entry_g.get()), float(self.entry_b.get())])
        reflection = float(self.entry_reflection.get())
        #refraction = float(self.entry_refraction.get())
        esfera =  Esfera(centro, radio, color, reflection)
        esfera_json = js.dumps(esfera.__dict__)

        count = 0
        dir = "./escenasjson/esferas/"
        if not os.path.exists(dir):
            os.makedirs(dir)
        for path in os.listdir(dir):
            if os.path.isfile(os.path.join(dir, path)):
                count += 1

        new_archivo = open(f"./escenasjson/esferas/esfera{count}.json", "w")
        new_archivo.write(esfera_json)
        new_archivo.close()
        self.padre.update_lista_objetos()
        self.destroy()




