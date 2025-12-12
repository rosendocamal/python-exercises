base_ingredients = ["mozzarella", "tomate"]
vegetarian_ingredients = ["pimiento", "tofu"]
non_vegetarian_ingredients = ["peperoni", "jamón", "salami"]

while True:
    try:
        type_pizza = int(
            input("ELIGE EL TIPO DE PIZZA:\n[1] VEGETARIANA\n[2] NO VEGETARIANO\n")
        )
        if type_pizza == 1:
            print("ELIGE UN INGREDIENTE:")
            for i in range(0, len(vegetarian_ingredients)):
                print(f"[{i + 1}] {vegetarian_ingredients[i].upper()}")
            while True:
                try:
                    option_ingredient = int(input(""))
                    if option_ingredient == 1 or option_ingredient == 2:
                        print(
                            f"HAZ ELEGIDO {vegetarian_ingredients[option_ingredient - 1].upper()}"
                        )
                        break
                    else:
                        print("POR FAVOR, INGRESE UNA OPCIÓN VÁLIDA")
                except ValueError:
                    print("REINTENTE DE NUEVO. INGRESE VALORES ENTEROS")
            print(
                "\nHAZ ELEGIDO UNA PIZZA VEGETARIANA Y TIENE LOS SIGUIENTES INGREDIENTES:"
            )
            base_ingredients.append(vegetarian_ingredients[option_ingredient - 1])
            for i in base_ingredients:
                print(i.upper())
        elif type_pizza == 2:
            print("ELIGE UN INGREDIENTE:")
            for i in range(0, len(non_vegetarian_ingredients)):
                print(f"[{i + 1}] {non_vegetarian_ingredients[i].upper()}")
            while True:
                try:
                    option_ingredient = int(input(""))
                    if (
                        option_ingredient == 1
                        or option_ingredient == 2
                        or option_ingredient == 3
                    ):
                        print(
                            f"\nHAZ ELEGIDO {non_vegetarian_ingredients[option_ingredient - 1].upper()}"
                        )
                        break
                    else:
                        print("POR FAVOR, INGRESE UNA OPCIÓN VÁLIDA")
                except ValueError:
                    print("REINTENTE DE NUEVO. INGRESE VALORES ENTEROS")
            print(
                "\nHAZ ELEGIDO UNA PIZZA NO VEGETARIANA Y TIENE LOS SIGUIENTES INGREDIENTES:"
            )
            base_ingredients.append(non_vegetarian_ingredients[option_ingredient - 1])
            for i in base_ingredients:
                print(i.upper())
            
        else:
            print("REINTENTE DE NUEVO. ELIGE UNA OPCIÓN ENTRE EL 1 Y  EL 2")
        break
    except ValueError:
        print("REINTENTE DE NUEVO. INGRESE UN OPCIÓN VÁLIDA")
