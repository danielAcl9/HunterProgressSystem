import json
import os
from typing import Optional
from entities.hunter import Hunter
from entities.stats import Stat

class HunterRepository:

    def __init__(self, root: str) -> None:
        # Recibe la ruta del archivo JSON donde guardará datos
        self.root = root
    
    def _data_exists(self) -> None:
        # Método privado: Asegurar que existe la carpeta data
        pass

    def _hunter_to_dict(self, hunter: Hunter) -> None:
        self.hunter = Hunter
        dict_hunter = dict([
            ('Name', self.hunter.name),
            ('Gold', self.hunter.gold)
            # Ahora, como guardo las clases? 
        ])
        # Convertir un objeto Hunter en un diccionario para guardar en JSON
        pass