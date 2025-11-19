import re
from colorama import Fore, Style, init
init(autoreset=True)

def evaluar_contraseña(password):
    score = 0
    recomendaciones = []

    if len(password) >= 8:
        score += 2
    else:
        recomendaciones.append("- Usa al menos 8 caracteres.")

    if re.search(r"[A-Z]", password):
        score += 2
    else:
        recomendaciones.append("- Agrega mayúsculas.")

    if re.search(r"[a-z]", password):
        score += 2
    else:
        recomendaciones.append("- Incluye minúsculas.")

    if re.search(r"[0-9]", password):
        score += 2
    else:
        recomendaciones.append("- Incluye números.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 2
    else:
        recomendaciones.append("- Añade símbolos como ! @ # $ %.")

    if " " in password:
        recomendaciones.append("- No uses espacios en la contraseña.")

    comunes = ["password", "123456", "qwerty", "admin", "iloveyou"]
    if password.lower() in comunes:
        score = max(score - 3, 0)
        recomendaciones.append("- Evita contraseñas comunes como '123456' o 'password'.")

    return score, recomendaciones

def mostrar_resultado(score):
    if score >= 9:
        return Fore.GREEN + "MUY FUERTE 💪"
    elif score >= 7:
        return Fore.LIGHTGREEN_EX + "Fuerte ✔"
    elif score >= 5:
        return Fore.YELLOW + "Media ⚠"
    else:
        return Fore.RED + "DÉBIL ❗"

print(Fore.CYAN + "=== VALIDADOR DE CONTRASEÑAS — Paula A. Gálvez ===")

while True:
    password = input("Ingresa la contraseña a evaluar: ")

    if password == "":
        print(Fore.MAGENTA + "Saliendo del programa... 🐰✨")
        break

    score, recomendaciones = evaluar_contraseña(password)

    print("\nResultado:")
    print("→ Seguridad:", mostrar_resultado(score))
    print(f"→ Puntuación: {score}/10\n")

    if recomendaciones:
        print(Fore.LIGHTYELLOW_EX + "Recomendaciones:")
        for r in recomendaciones:
            print(Fore.YELLOW + r)
    else:
        print(Fore.GREEN + "¡Excelente! Tu contraseña es muy segura 🛡")

    print(Fore.LIGHTBLACK_EX + "\n-----------------------------------------------\n")
