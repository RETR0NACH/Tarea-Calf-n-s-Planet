"""
Integrantes: Ignacio Chacón - David Nahuelcar 
"""

# Importación del módulo random para generar números aleatorios
import random

# Generación de un número aleatorio que representa la cantidad de hojitas en la ramita
ramita = random.randint(6, 20)

# Mensaje de bienvenida al juego
print(
    f"\n---- ¡Bienvenido al juego de Me quieres mucho, poquito, nada de Calfún's Planet! ----"
)

# Breve explicación del juego para iniciar el juego.
print(
    "\nEn este juego, deshojarás una ramita y dirás 'Me quiere mucho', 'Me quiere poquito', o 'No me quiere'."
)
print("La cantidad de hojitas que deshojarás en cada turno será aleatoria.")
print("¡Comencemos!\n")
print("Iniciando juego.....\n")

# Mientras aún queden hojitas en la ramita, se juega
while ramita > 0:
    # Se determina cuántas hojitas deshojar en esta ronda
    hojas = random.randint(1, 3)

    # Se definen las opciones posibles para el mensaje
    opciones = ["mucho", "poquito", "nada"]

    # Se selecciona aleatoriamente una opción para el mensaje
    resultado = opciones[hojas - 1]

    # Se imprime el mensaje correspondiente
    print(f"Me quieres {resultado}")

    # Se deshojan las hojitas seleccionadas
    for i in range(hojas):
        ramita -= 1

# Después de deshojar todas las hojitas, se determina el resultado final
if resultado == "mucho":
    # Se imprime un mensaje especial si el resultado es "mucho"
    print("")
    print("Felicidades, ¡¡Te Quieren Mucho!!!")
    print("Mucho!!!")
    print("Mucho! !!")
    print("Mucho!!!")

elif resultado == "poquito":
    # Se imprime un mensaje especial si el resultado es "poquito"
    print("PERO NO TANTO:( ")
else:
    # Se imprime un mensaje especial si el resultado es "nada"
    print("\nMe Cuernean 3:(")
