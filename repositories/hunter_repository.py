from entities.hunter import Hunter
import os

# TO-DO
# Asegurar que existe la carpeta data/.
# Convertir diccionario → objeto Hunter (el inverso de lo que hiciste).
# Guardar Hunter en JSON (usa _hunter_to_dict()).
# Cargar Hunter desde JSON (usa _dict_to_hunter() + lógica de Hunter por defecto).

class HunterRepository:

    def __init__(self, filepath: str) -> None:
        # Recibe la ruta del archivo JSON donde guardará datos
        self.filepath = filepath
        self._ensure_data_directory()

    def _ensure_data_directory(self) -> None:
        # Crea la carpeta data si no existe
        dir_path = os.path.dirname(self.filepath)

        if dir_path and not os.path.exists(dir_path):
            os.makedirs(dir_path)
            
    
    def _create_data_folder(self) -> None:
        # Método privado: Asegurar que existe la carpeta data
        pass

    def _hunter_to_dict(self, hunter: Hunter) -> dict:

        # 1. Crear diccionaro base con datos simples
        data = {
            "name": hunter.name,
            "gold": hunter.gold
        }

        # 2. Convertir las stats (diccionario de objetos Stat)
        stats_data = {}

        for stat_name, stat_object in hunter.stats.items():
            stats_data[stat_name] = {
                "name": stat_object.name,
                "total_xp": stat_object.total_xp
            }

        # 3. Agregar stats al diccionario principal
        data["stats"] = stats_data

        return data
    
    def _dict_to_hunter(self, data: dict) -> Hunter:
        name = data["name"]
        gold = data["gold"]

        hunter = Hunter(name)
        hunter.gold = gold

        for stat_name, stat_data in data["stats"].items():
            hunter.stats[stat_name].total_xp = stat_data["total_xp"]
        
        return hunter