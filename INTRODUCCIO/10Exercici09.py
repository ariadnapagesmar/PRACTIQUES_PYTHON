# 9. Operacions amb conjunts (Sets)

# Concepte: Conjunts, unió (|) i intersecció (&).

# Enunciat:
# Teniu dos conjunts de videojocs que agraden a dues persones diferents:
# grup_a = {"FIFA", "Minecraft", "Zelda"}
# grup_b = {"Zelda", "Fortnite", "Minecraft"}
# Troba quins videojocs agraden a tots dos (intersecció).
# Troba la llista total de jocs únics que els agraden combinats (unió).

grup_a = {"FIFA", "Minecraft", "Zelda"}
grup_b = {"Zelda", "Fortnite", "Minecraft"}

interseccio = grup_a & grup_b
print(interseccio)

unio = grup_a | grup_b
print(unio)