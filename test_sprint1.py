# 1. Crear Hunter llamado "Daniel"
# 2. Imprimir su nivel global y oro inicial
# 3. Crear Quest "El Núcleo" (Fuerza, Diaria, 50 XP, 20 oro)
# 4. Manualmente añadir 150 XP a la stat de Fuerza del Hunter
# 5. Imprimir si Fuerza subió de nivel
# 6. Imprimir el nuevo nivel de Fuerza
# 7. Recalcular nivel global del Hunter
# 8. Imprimir nivel global actualizado

from entities.stats import Stats
# from entities.hunter import Hunter

stat = Stats("Fuerza", 250)
# print(f'Nivel actual: {stat.get_level(50)}')
# print(f'Nivel {stat.get_level()}, XP Faltante: {stat.xp_for_next_level()}')

print(stat.add_exp(100))