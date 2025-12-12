HIGHER_PRICE = 10
LOWER_PRICE = 5
FREE_PRICE = 0
ADULT_MIN_AGE = 18
CHILDREN_MIN_AGE = 4 

try:
    MIN_AGE_HUMAN = 0
    MAX_AGE_HUMAN = 130
    age_client = int(input('INGRESE SU EDAD:\n'))
    if MIN_AGE_HUMAN < age_client < MAX_AGE_HUMAN:
        if age_client < CHILDREN_MIN_AGE:
            ticket_price = FREE_PRICE
        elif age_client >= CHILDREN_MIN_AGE and age_client <= ADULT_MIN_AGE:
            ticket_price = LOWER_PRICE
        elif age_client > ADULT_MIN_AGE:
            ticket_price = HIGHER_PRICE

        print(f'EL PRECIO DE LA ENTRADA ES ${ticket_price}')
        
    else:
        print(f'INGRESE VALORES ENTEROS ENTRE {MIN_AGE_HUMAN} Y {MAX_AGE_HUMAN}')
except ValueError:
    print('REINTENTE DE NUEVO. INGRESE VALORES NÚMERICOS')