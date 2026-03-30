import re

def check_password(password):
    score = 0
    feedback = []

    # Longitud mínima
    if len(password) >= 8:
        score += 20
    else:
        feedback.append("❌ Mínimo 8 caracteres")

    # Longitud ideal
    if len(password) >= 16:
        score += 20
        feedback.append("✅ Longitud excelente")

    # Mayúsculas
    if re.search(r'[A-Z]', password):
        score += 20
    else:
        feedback.append("❌ Agregá al menos una mayúscula")

    # Números
    if re.search(r'[0-9]', password):
        score += 20
    else:
        feedback.append("❌ Agregá al menos un número")

    # Caracteres especiales
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 20
    else:
        feedback.append("❌ Agregá un carácter especial (!@#$...)")

    return score, feedback


def main():
    print("=" * 40)
    print("   🔐 Password Strength Checker")
    print("=" * 40)

    password = input("\nIngresá una contraseña: ")
    score, feedback = check_password(password)

    print(f"\nScore: {score}/100")

    if score <= 40:
        print("Nivel: ❌ MUY DÉBIL")
    elif score <= 60:
        print("Nivel: ⚠️  DÉBIL")
    elif score <= 80:
        print("Nivel: 🟡 MODERADA")
    else:
        print("Nivel: ✅ FUERTE")

    if feedback:
        print("\nSugerencias:")
        for tip in feedback:
            print(f"  {tip}")

    print("=" * 40)


if __name__ == "__main__":
    main()