import re
from datetime import datetime

def evaluar_contraseña(password):
    puntaje = 0
    mejoras = []

    # Longitud
    if len(password) >= 8:
        puntaje += 2
    else:
        mejoras.append("La contraseña debe tener al menos 8 caracteres.")

    # Mayúsculas y minúsculas
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        puntaje += 2
    else:
        mejoras.append("Usa mayúsculas y minúsculas.")

    # Números
    if re.search(r'\d', password):
        puntaje += 2
    else:
        mejoras.append("Incluye al menos un número.")

    # Caracteres especiales
    if re.search(r'[@$!%*#?&]', password):
        puntaje += 2
    else:
        mejoras.append("Agrega un carácter especial (@, $, !, %, *, #, ?, &).")

    # Fortalece más si cumple todo
    if puntaje == 8:
        mejoras.append("Tu contraseña es muy fuerte. ¡Buen trabajo!")

    return puntaje, mejoras


def guardar_log(password, puntaje):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("checks_log.txt", "a") as file:
        file.write(f"{now} | '{password}' | Puntaje: {puntaje}/8\n")


def main():
    print("🔐 Validador de Contraseñas")
    password = input("Ingresa una contraseña: ")

    puntaje, mejoras = evaluar_contraseña(password)

    print("\nResultado:")
    print(f"➡ Puntaje total: {puntaje}/8")
    print("➡ Recomendaciones:")
    for m in mejoras:
        print(f" - {m}")

    guardar_log(password, puntaje)
    print("\n📁 Registro guardado en 'checks_log.txt'")


if __name__ == "__main__":
    main()
