import re
import json
import time
import os
from collections import Counter
from pydriller import Repository


def extraer_palabras_de_funcion(nombre_funcion):
    paso1 = re.sub(r'([a-z])([A-Z])', r'\1 \2', nombre_funcion)
    # Separa snake_case: de 'make_response' a 'make response'
    paso2 = paso1.replace('_', ' ')
    # devuelve lista en minúsculas 
    return paso2.lower().split()

# lista de repos
repos_a_minar = [
    "https://github.com/pallets/flask"
]

# Regex para Python y Java
regex_nombres = r'(?:def\s+|[\w\<\>\[\]]+\s+)(\w+)\s*\('

ranking_acumulado = Counter()


for i, url in enumerate(repos_a_minar):
    nombre_repo = url.split('/')[-1]
    print(f"\n[{i+1}/{len(repos_a_minar)}] {nombre_repo}...")
    
    conteo_del_repo = Counter()
    
    try:
        # HEAD (el último commit) de cada repositorio
        # only_in_branch=None permite que PyDriller encuentre la rama principal solo
        for commit in Repository(url, only_modifications_with_file_types=['.py', '.java']).traverse_commits():
            
            for file in commit.modified_files:
                if file.source_code:
                    # Extraer nombres de funciones
                    nombres = re.findall(regex_nombres, file.source_code)
                    
                    for nombre in nombres:
                        palabras = extraer_palabras_de_funcion(nombre)
                        # Actualizamos ambos contadores
                        conteo_del_repo.update(palabras)
                        ranking_acumulado.update(palabras)
            
            # IMPORTANTE: Solo procesamos el estado actual, no la historia completa
            break 

        # ACTUALIZAR JSON 
        estado = {
            "repo_actual": nombre_repo,
            "progreso": f"{i+1}/{len(repos_a_minar)}",
            "top_del_repo": dict(conteo_del_repo.most_common(10)),
            "ranking_general": dict(ranking_acumulado.most_common(15))
        }
        
        with open('progreso_miner.json', 'w', encoding='utf-8') as f:
            json.dump(estado, f, indent=4)
        
        print(f" {nombre_repo} cargado 👍👍👍👍")
        
        time.sleep(3)

    except Exception as e:
        print(f"Error en {nombre_repo}: {e}")

print("👍👍")