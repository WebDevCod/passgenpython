import random

print("Generador de contraseñas")
print("========================")

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@€$%^&*().,?0123456789"

number = input("Cantidad de contraseñas que necesitas: ")
number = int(number)

length = input("Cantidad de caracteres: ")
length = int(length)

print("\nContraseñas generadas:")

for pwd in range(number):
    passwords = ""
    for c in range(length):
        passwords += random.choice(chars) 
    print(passwords)
