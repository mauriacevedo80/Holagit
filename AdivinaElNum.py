import random 


print("Hola, dime tu nombre: ")
Nombre = input()

print("Estoy pensando en un numero del 1 al 100, puedes adivinarlo? " + (Nombre))
print("Tienes 8 intentos, suerte.")

print("~" * 25)

numero_a_adivinar = random.randint(1, 100)

intentos_restantes = 8

while intentos_restantes > 0:

    numero_str = input("Ingrese un numero: ")

    if not numero_str.isdigit():
        print("Eso no es un numero entero. Intenta otra vez.")
        continue

    numero_user = int(numero_str)

    if numero_user == numero_a_adivinar:
        print(" " * 80)
        print(f"Felicidades, {Nombre}. Adivinaste el numero. {9 - intentos_restantes}.")
        print(" " * 80)
        break
    elif numero_user < numero_a_adivinar:
        print("El numero adivinado es MAYOR.")
        print("+" * 80)
    else:
        print("El numero a adivinado es menor.")
        print("-" * 80)

    intentos_restantes -= 1

    print(f"Te quedan {intentos_restantes} intentos.")

    print("*" * 80)

    if intentos_restantes == 0:
        print(f"Lo siento, {Nombre}, se te acabaron los intentos. El numero a adivinar era {numero_a_adivinar}.")