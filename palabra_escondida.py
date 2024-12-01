print("Bienvenido al juego palabra_escondida")
print("menu principal")
print("selecionas tu opcion del menu")
print("1. Function-1 Name. princio del juego")
print("2. Function-2 Name. continua el juego")
print("3. Function-3 Name  comience el juego desde el cero")
print("4. function-4 Exit")
print("tienes 3 intento de adivinar")

nombres = ["alexander", "jose", "pedro","andres", "maria"]

palabra_secreta = "jose"

adivina_la_primera_letra = input("adivina la primera letra del nombre: ")

adivina_la_primera_letra = input("adivina la primera letra del nombre: ")
adivina_la_segunda_letra = input("adivina la primera letra del nombre:")
adivina_la_tercera_letra = input("adivina la primera letra del nombre:")
adivina_la_cuatro_letra = input("adivina la primera letra del nombre:")

intento = 3

if intento > 0:
    print("es tu primera intento")
elif intento > 1:
    print("agotaste tu primer intentalo de nuevo")
elif intento > 2:
    print("agotaste tu segundo intento te queda un intento mas")
elif intento > 3:
    print("es tu ultimo intento")
else:
    print("se te acabaron tu ultimo intento")

print("terminaro el juegos")

