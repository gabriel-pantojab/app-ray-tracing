import customtkinter as ctk
import tkinter as tk
from PIL import Image
import numpy as np

from model.Esfera import Esfera
from model.Plano import Plano
from controller import Controller

import jsonutils.utils as jsU
import json as js
import os

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

class AppWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.objetos = []

        self.title("Ray Tracing")
        self.geometry("900x400+0+0")
        self.update_idletasks()
        width = 900
        height = 400
        x = (self.winfo_screenwidth() - width) // 2
        y = (self.winfo_screenheight() - height) // 2
        self.geometry(f"{width}x{height}+{x+150}+{y}")

        self.escena = [
            Plano(np.array([0., -.5, 0.]), np.array([0., 1., 0.]), reflection=.5, refraction=1., diffuse_c=.75, specular_c=.5)
        ]
        
        self.main_frame = ctk.CTkFrame(self, width=900, height=400)
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=1)
        self.main_frame.rowconfigure(1, weight=3)

        self.options_frame = ctk.CTkFrame(self.main_frame, width=200, height=200)
        self.options_frame.grid(row=0, column=0, sticky=tk.NSEW, ipadx=10, ipady=10, padx=(0, 10), pady=(0, 10))
        self.options_frame.columnconfigure(0, weight=1)


        self.img_frame = ctk.CTkFrame(self.main_frame, width=700, height=400)
        self.img_frame.grid(row=0, column=1, sticky=tk.NSEW, rowspan=2)

        self.objetos_frame = ctk.CTkFrame(self.main_frame, width=200, height=200)
        self.objetos_frame.grid(row=1, column=0, sticky=tk.NSEW, ipadx=10, ipady=10, padx=(0, 10))


        self.label_objetos = ctk.CTkLabel(self.objetos_frame, text="Objetos", font=ctk.CTkFont(size=15, weight="bold"))
        self.label_objetos.pack()
        scrollbar = tk.Scrollbar(self.objetos_frame, orient=tk.VERTICAL)
        self.obj_list = tk.Listbox(self.objetos_frame, yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.obj_list.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.obj_list.pack(expand=True, fill=tk.BOTH, pady=5, padx=5)

        self.loading_label = ctk.CTkLabel(self.img_frame, text="ARMA TU ESCENA", font=ctk.CTkFont(size=20, weight="bold"))
        self.loading_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.label = ctk.CTkLabel(self.options_frame, text="Ray Tracing", font=ctk.CTkFont(size=15, weight="bold"))
        self.label.grid(row=0, column=0, sticky=tk.NSEW)

        self.run_button = ctk.CTkButton(self.options_frame, text="Run Ray Tracing")
        self.run_button.grid(row=1, column=0, sticky=tk.NSEW, pady=5, padx=5)
        self.run_button.configure(state=tk.DISABLED)

        self.clear_button = ctk.CTkButton(self.options_frame, text="Clear")
        self.clear_button.grid(row=2, column=0, sticky=tk.NSEW, pady=5, padx=5)

        self.add_sefera_button = ctk.CTkButton(self.options_frame, text="Agregar Esfera")
        self.add_sefera_button.grid(row=3, column=0, sticky=tk.NSEW, pady=5, padx=5)

        self.generar_escena_button = ctk.CTkButton(self.options_frame, text="Generar Escena", command=self.handle_generar_escena)
        self.generar_escena_button.grid(row=4, column=0, sticky=tk.NSEW, pady=5, padx=5)
        self.generar_escena_button.configure(state=tk.DISABLED)

        self.cargar_escena_button = ctk.CTkButton(self.options_frame, text="Cargar Escena", command=lambda: self.cargar_escena())
        self.cargar_escena_button.grid(row=5, column=0, sticky=tk.NSEW, pady=5, padx=5)

        self.escena_label = ctk.CTkLabel(self.options_frame, text="Escena:\n EMPTY", font=ctk.CTkFont(size=13, weight="bold"))
        self.escena_label.grid(row=6, column=0, sticky=tk.NSEW)

        self.main_frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

    def update_img(self):
        self.img = ctk.CTkImage(Image.open("./resultado/app.png"), size=(700, 400))
        self.loading_label.configure(text="")
        self.loading_label.configure(image=self.img)
    
    def clear(self):
        self.loading_label.configure(image="")
        self.loading_label.configure(text="ARMA TU ESCENA")
        self.escena_label.configure(text="Escena:\n EMPTY")
        self.run_button.configure(state=tk.DISABLED)
        self.add_sefera_button.configure(state=tk.NORMAL)
        self.objetos = []
        while len(self.escena) > 1:
            self.escena.pop()
        self.update_lista_objetos()
        self.generar_escena_button.configure(state=tk.DISABLED)


    def handle_generar_escena(self):
        self.obj_list.delete(0, tk.END)
        self.objetos = []
        file_dialog = tk.filedialog.asksaveasfilename(initialdir="./escenasjson/escenas/",
                                                    title="Select file",
                                                    filetypes=(("json files", "*.json"), ("all files", "*.*")))
        if file_dialog:
            jsU.generar_escena(os.path.basename(file_dialog))
            self.generar_escena_button.configure(state=tk.DISABLED)

    def cargar_escena(self):
        file_dialog = tk.filedialog.askopenfilename(initialdir="./escenasjson/escenas/",
                                                    title="Select file", 
                                                    filetypes=(("json files", "*.json"), ("all files", "*.*")))
        dir_escena = file_dialog
        if not dir_escena:
            print("No se selecciono ninguna escena")
            return
        self.add_sefera_button.configure(state=tk.DISABLED)
        # limpiar escena
        while len(self.escena) > 1:
            self.escena.pop()
        self.escena_label.configure(text=f"Escena:\n {os.path.basename(dir_escena)}")
        with open(dir_escena) as json_file:
            data = js.load(json_file)
            for esfera in data["esferas"]:
                centro = np.array([esfera["centro"][0], esfera["centro"][1], esfera["centro"][2]])
                radio = esfera["radio"]
                color = np.array([esfera["color"][0], esfera["color"][1], esfera["color"][2]])
                reflection = esfera["reflection"]
                refraction = esfera["refraction"]
                self.escena.append(Esfera(centro, radio, color, reflection, refraction))
        self.run_button.configure(state=tk.NORMAL)
        self.update_lista_objetos()
        self.generar_escena_button.configure(state=tk.DISABLED)
        print(f"Escena cargada {len(self.escena)}")

    def update_lista_objetos(self):
        self.obj_list.delete(0, tk.END)
        self.generar_escena_button.configure(state=tk.NORMAL)
        for i, objeto in enumerate(self.escena):
            self.obj_list.insert(tk.END, f"{objeto.__class__.__name__} {i}")


app = AppWindow()
ctr = Controller(app)
