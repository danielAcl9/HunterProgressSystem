from repositories.hunter_repository import HunterRepository
from entities.hunter import Hunter

# 1. Crear y guardar hunter
print("=== PASO 1: Crear y Guardar ===")
hunter1 = Hunter("Daniel")
hunter1.stats["Strength"].add_exp(500)
hunter1.add_gold(150)

repo = HunterRepository("data/hunter_profile.json")
repo.save(hunter1)
print("✓ Hunter guardado")

# 2. Cargar hunter
print("\n=== PASO 2: Cargar ===")
hunter2 = repo.load()
print(f"Nombre: {hunter2.name}")
print(f"Oro: {hunter2.gold}")
print(f"Fuerza XP: {hunter2.stats['Strength'].total_xp}")
print(f"Fuerza Nivel: {hunter2.stats['Strength'].get_level()}")

# 3. Verificar persistencia
assert hunter2.name == "Daniel"
assert hunter2.gold == 150
assert hunter2.stats["Strength"].total_xp == 500
print("\n✓ Todos los datos persisten correctamente")
