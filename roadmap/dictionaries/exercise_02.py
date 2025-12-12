# Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.

info_user = {}

info_user['name'] = input('>>> NOMBRE COMPLETO: ')
info_user['age'] = input('>>> EDAD: ')
info_user['address'] = input('>>> DOMICILIO: ')
info_user['num_phone'] = input('>>> NÚMERO TELEFÓNICO: ')

print(f">>> {info_user['name']} TIENE {info_user['age']} AÑOS, VIVE EN {info_user['address']} Y SU NÚMERO DE TELÉFONO ES {info_user['num_phone']}.")