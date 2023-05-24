import json as js
import os
import shutil as sh

def generar_escena(name_scene):
    dir_esferas = "./escenasjson/esferas/"
    escena = {
        "esferas": []
    }

    for path in os.listdir(dir_esferas):
        with open(dir_esferas + path) as json_file:
            data = js.load(json_file)
            escena["esferas"].append(data)
    
    sh.rmtree(dir_esferas)
    

    count = 0
    dir_escenas = "./escenasjson/escenas/"
    for path in os.listdir(dir_escenas):
      if os.path.isfile(os.path.join(dir_escenas, path)):
        count += 1

    if not name_scene:
       new_archivo = open(f"./escenasjson/escenas/escena{count}.json", "w")
    else:
        new_archivo = open(f"./escenasjson/escenas/{name_scene}.json", "w")
    new_archivo.write(js.dumps(escena))
    new_archivo.close()
            