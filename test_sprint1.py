# 1. Crear Hunter llamado "Daniel"
# 2. Imprimir su nivel global y oro inicial
# 3. Crear Quest "El Núcleo" (Fuerza, Diaria, 50 XP, 20 oro)
# 4. Manualmente añadir 150 XP a la stat de Fuerza del Hunter
# 5. Imprimir si Fuerza subió de nivel
# 6. Imprimir el nuevo nivel de Fuerza
# 7. Recalcular nivel global del Hunter
# 8. Imprimir nivel global actualizado

from entities.stats import Stat
from entities.hunter import Hunter
from entities.quest_dificulty import QuestDifficulty

# print("=== Test 1: Creación Básica ===")
# stat = Stats("Fuerza", 0)
# print(f'Nivel: {stat.get_level()}, XP Faltante: {stat.xp_for_next_level()}')

# print("\n === Test 2: Añadir XP SIN Level-up ===")
# print(stat.add_exp(50))

# print("\n === Test 3: Añadir XP Level-up Simple ===")
# print(stat.add_exp(100))

# print("\n === Test 4: Level-up Múltiple ===")
# stat2 = Stats("Agilidad", 100)
# print(stat.add_exp(1000))

# print("\n === Test 5: Nivel Máximo ===")
# stat3 = Stats("Inteligencia", 3250)
# print(f'Nivel: {stat3.get_level()}, XP Faltante: {stat3.xp_for_next_level()}')


hunter = Hunter("Daniel")

print(hunter.get_global_exp())
print(hunter.get_global_level())

hunter.stats["Fuerza"].add_exp(1000)
print(hunter.get_global_exp())
print(hunter.get_global_level())

print(hunter.add_gold(15))