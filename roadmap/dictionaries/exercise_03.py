# Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
"""
Fruta 	    Precio
Plátano 	1.35
Manzana 	0.80
Pera 	    0.85
Naranja 	0.70
"""

fruits_prices = {"PLATANO": 1.35, "MANZANA": 0.80, "PERA": 0.85, "NARANJA": 0.70}

def get_fruit_name():
    fruit_name = input('>>> FRUTA:\n>>> ').strip().upper()
    
    if fruit_name.isalpha():
        if fruit_name not in fruits_prices:
            print('>>> ALERTA: NO ESTÁ REGISTRADA LA FRUTA INGRESADA')
        else:
            return fruit_name
    else:
        print('>>> ERROR: INGRESE EL NOMBRE DE UNA FRUTA')


def get_fruit_kg():
    try:
        fruit_kg = float(input('>>> CANTIDAD (KG):\n>>> '))
        if fruit_kg >= 0:
            return fruit_kg
        else:
            print('>>> ALERTA: NO SE PUEDEN INGRESAR CANTIDADES (KG) MENORES A CERO')
    except ValueError:
        print('>>> ERROR: INGRESE UNA CANTIDAD VÁLIDA EN KG')

def show_total_price_fruit(db_fruits, fruit, amount):
    total_price = db_fruits[fruit] * amount
    msg = f'>>> EL TOTAL DEL PRECIO DE {fruit} POR {amount:5.2f} KG ES ${total_price:5.2f}'
    return msg

def main():
    while True:
        fruit_name = get_fruit_name()
        if isinstance(fruit_name, str):
            break

    while True:
        amount_fruit = get_fruit_kg()
        if isinstance(amount_fruit, float):
            break

    resume = show_total_price_fruit(fruits_prices, fruit_name, amount_fruit)
    print(resume)

if __name__ == "__main__":
    main()