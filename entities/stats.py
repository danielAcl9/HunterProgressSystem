XP_THRESHOLDS :list[int] = [
    0,      # Nivel 1
    100, 250, 450, 700,    # Hasta nivel 5
    1000, 1350, 1750, 2200, 2700, 3250    # Hasta nivel 10
]

class Stats():
    def __init__(self, name: str, total_xp: int) -> None:
        self.name = name
        self.total_xp = total_xp

    def get_level(self) -> int:
        level = 1
        # Recorre el largo del threshold
        for i in range(len(XP_THRESHOLDS)):
            if self.total_xp >= XP_THRESHOLDS[i]:
                # Devuelve el primer nivel al que sa mayor.
                level = i + 1
            else:
                break
        return level
            
    def xp_for_next_level(self) -> str:
        next_lvl = self.get_level()
        if next_lvl > len(XP_THRESHOLDS):
            return 0
        else:
            xp_next_lvl = XP_THRESHOLDS[next_lvl]
            xp_needed = xp_next_lvl - self.total_xp
            return f'XP necesaria para el siguiente nivel: {xp_needed} XP'

# TODO: Resolver de acá para abajo
            

    # def add_exp(self, exp: int) -> str:
    #     self.total_xp += exp
        
    #     return f'Se añadió {exp} puntos de experiencia. Experiencia actual de la clase {self.name}: {self.total_xp} XP'


stat = Stats("Fuerza", 250)
# print(f'Nivel actual: {stat.get_level(50)}')
print(stat.xp_for_next_level())