XP_THRESHOLDS :list[int] = [
    0,      # Nivel 1
    100, 250, 450, 700,    # Hasta nivel 5
    1000, 1350, 1750, 2200, 2700, 3250    # Hasta nivel 10
]

class Stats():
    def __init__(self, name: str, total_xp: int) -> None:
        self.name = name
        self.total_xp = total_xp
        # Revisar
        # level = Stats.get_level(self.total_xp)

    def get_level(self, total_xp: int) -> int:
        level = 1
        # Recorre el largo del threshold
        for i in range(len(XP_THRESHOLDS)):
            if total_xp >= XP_THRESHOLDS[i]:
                # Devuelve el primer nivel al que sa mayor.
                level = i + 1
            else:
                break
        return level
            

# TODO: Resolver de acá para abajo
            
    # def xp_for_next_level(self):
    #     current_lvl = Stats.get_level(self.total_xp)

    # def add_exp(self, exp: int) -> str:
    #     self.total_xp += exp
        
    #     return f'Se añadió {exp} puntos de experiencia. Experiencia actual de la clase {self.name}: {self.total_xp} XP'


stat = Stats("Fuerza", 0)
print(f'Nivel actual: {stat.get_level(50)}')
print(f'Nivel actual: {stat.get_level(100)}')
print(f'Nivel actual: {stat.get_level(300)}')
print(f'Nivel actual: {stat.get_level(1000)}')