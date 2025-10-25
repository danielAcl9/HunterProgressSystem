from repositories.hunter_repository import HunterRepository
from entities.hunter import Hunter

# Crear hunter original
hunter1 = Hunter("Daniel")
hunter1.stats["Fuerza"].add_exp(500)
hunter1.add_gold(150)

print(f"Original - Fuerza XP: {hunter1.stats['Fuerza'].total_xp}")
print(f"Original - Gold: {hunter1.gold}")

# Convertir a dict
repo = HunterRepository("data/hunter.json")
data = repo._hunter_to_dict(hunter1)

# Convertir de vuelta a hunter
hunter2 = repo._dict_to_hunter(data)

print(f"Reconstruido - Fuerza XP: {hunter2.stats['Fuerza'].total_xp}")
print(f"Reconstruido - Gold: {hunter2.gold}")

# Deben ser iguales
assert hunter2.stats["Fuerza"].total_xp == 500
assert hunter2.gold == 150