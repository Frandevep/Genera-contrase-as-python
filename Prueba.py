import random
import string

# Función para generar una contraseña
def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

# Pedimos la longitud de la contraseña al usuario
longitud = int(input("Ingresa la longitud de la contraseña: "))

# Generamos y mostramos la contraseña
contrasena_generada = generar_contrasena(longitud)
print("Tu contraseña aleatoria es:", contrasena_generada)
