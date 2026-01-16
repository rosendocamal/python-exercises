# Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.

def main():
    persona = {}
    continuar = True

    print("--- Registro de Usuario Pro ---")

    while continuar:
        clave = input("\n¿Qué dato quieres guardar? (o escribe 'salir'): ").strip().capitalize()
        
        if clave.lower() == 'salir':
            break

        valor = input(f"Introduce el valor para '{clave}': ").strip()

        persona[clave] = valor

        print("\nEstado actual del registro:")
        print("-" * 30)
        for k, v in persona.items():
            print(f"{k}: {v}")
        print("-" * 30)

if __name__ == "__main__":
   main()
