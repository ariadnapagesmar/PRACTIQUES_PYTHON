# 1. Verificació de temperatura (if-else)

# Concepte: if, else, operadors de comparació.

# Enunciat: Escriu un estructura condicional que imprimeixi "Fa calor" 
# si la temperatura és superior o igual a 25, i "Fa fresca o fred" en cas contrari.

temperatura = float(input("Quina és la temperatura actual?"))

if temperatura >= 25:
    print("Fa calor")
else:
    print("Fa fresca o fred")