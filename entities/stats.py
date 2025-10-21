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
        level: int = 1
        # Recorre el largo del threshold
        for i in range(len(XP_THRESHOLDS)):
            if self.total_xp >= XP_THRESHOLDS[i]:
                # Devuelve el primer nivel al que sa mayor.
                level = i + 1
            else:
                break
        return level
            
    def xp_for_next_level(self) -> int:
        next_lvl = self.get_level()
        if next_lvl >= len(XP_THRESHOLDS):
            return 0
        else:
            xp_next_lvl = XP_THRESHOLDS[next_lvl]
            xp_needed = xp_next_lvl - self.total_xp
            return xp_needed            

    def add_exp(self, exp: int) -> str:

        if exp <= 0:
            return 'No se puede añadir XP negativa o cero'
        
        else:
            current_lvl = self.get_level()
            self.total_xp += exp
            new_level = self.get_level()

            if new_level == current_lvl:
                return f'Experiencia ganada: {exp} - Experiencia total: {self.total_xp} - XP Necesaria para subir: {self.xp_for_next_level()}'
            
            else: 
                return f'Experiencia ganada: {exp} - Nuevo nivel! {current_lvl} -> {new_level}'


# TODO -
# Typing limpio en todo