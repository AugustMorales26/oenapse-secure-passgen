#OENAPSE: Open-source Efficient Numeric Alphanumeric Password Secure Encryption
import json
import random
import string
import emoji
import os

# Función para imprimir el título estilo "hacker"
def print_hacker_title(title):
    print("\n".join([
        " ██████╗ ███████╗███╗   ██╗ █████╗ ██████╗ ███████╗███████╗",
        "██╔═══██╗██╔════╝████╗  ██║██╔══██╗██╔══██╗██╔════╝██╔════╝",
        "██║   ██║█████╗  ██╔██╗ ██║███████║██████╔╝███████╗█████╗  ",
        "██║   ██║██╔══╝  ██║╚██╗██║██╔══██║██╔═══╝ ╚════██║██╔══╝  ",
        "╚██████╔╝███████╗██║ ╚████║██║  ██║██║     ███████║███████╗",
        " ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚══════╝╚══════╝",
        "                                                         ",
        "             " + title + "            "
    ]))


# Función para generar una contraseña segura
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Función para guardar la contraseña en un archivo JSON
def save_password(service, password):
    data = {}
    if os.path.exists('passwords.json'):
        with open('passwords.json', 'r') as f:
            data = json.load(f)
    data[service] = password
    with open('passwords.json', 'w') as f:
        json.dump(data, f, indent=4)

# Función para mostrar las contraseñas generadas
def show_passwords():
    if os.path.exists('passwords.json'):
        with open('passwords.json', 'r') as f:
            data = json.load(f)
        for service, password in data.items():
            print(f"✅ Servicio: {service}, Contraseña: {password}")
    else:
        print("No passwords generated yet.")

# Menú principal
while True:
    os.system('clear' if os.name == 'posix' else 'cls')  # Limpia la pantalla    print("Password Generator")
    print_hacker_title("")
    print("1. Generar una nueva contraseña")
    print("2. Ver contraseñas generadas")
    print("3. Salir del programa")
    print("_______________________________")
    choice = input("🍺 - Elije una opción: ")

    if choice == "1":
        os.system('clear' if os.name == 'posix' else 'cls')  # Limpia la pantalla
        service = input("🍺 - Ingrese el servicio (e.g. Facebook): ")
        password = generate_password()
        save_password(service, password)
        print(f"✅ Contraseña generada para {service}: {password}")
        input("Presione <Enter> para continuar...")  # Pausa para que el usuario vea el resultado
    elif choice == "2":
        os.system('clear' if os.name == 'posix' else 'cls')  # Limpia la pantalla
        print_hacker_title("")
        print("🍺 - Contraseñas generadas:")
        show_passwords()
        input("Presione <Enter> para continuar...")  # Pausa para que el usuario vea el resultado
    elif choice == "3":
        os.system('clear' if os.name == 'posix' else 'cls')  # Limpia la pantalla
        print("🍺 - Vuelve pronto! 👋")
        break
    else:
        print("🍺 - Opción inválida. ¡Intentar otra vez!")
        input("Presione <Enter> para continuar...")  # Pausa para que el usuario vea el error
