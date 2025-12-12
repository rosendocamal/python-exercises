"""
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
  las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""
import time

def are_anagrams(first_word, second_word):
    first_word = first_word.lower()
    second_word = second_word.lower()

    if first_word.isalpha() and second_word.isalpha():
        if len(first_word) == len(second_word):
            if first_word != second_word:

                temp_first_word = list()
                for i in first_word:
                    temp_first_word.append(i)
                temp_second_word = list()
                for i in second_word:
                    temp_second_word.append(i)

                temp_first_word.sort()
                temp_second_word.sort()

                if ''.join(temp_first_word) == ''.join(temp_second_word):
                    return True
    
    return False

def main():
    continue_program = True

    while continue_program:
        initial_time = time.time()

        first_word = input('>>> ESCRIBA LA PRIMERA PALABRA:\n>>> ').strip()
        second_word = input('>>> ESCRIBA LA SEGUNDA PALABRA:\n>>> ').strip()

        if are_anagrams(first_word, second_word):
            print('>>>\n>>> SON ANAGRAMAS')
        else:
            print('>>> NO SON ANAGRAMAS')

        final_time = time.time()

        print(final_time - initial_time)
        
        if (final_time - initial_time) < 60:
            answer = input('>>>\n>>> ¿DESEA CONTINUAR CON EL PROGRAMA (s\\n)? ').strip()
            if len(answer):
                if answer[0].lower() == 'y' or answer[0].lower() == 's':
                    pass
                elif answer[0].lower() == 'n':
                    continue_program = False
        else:
            continue_program = False
            print('>>> EL PROGRAMA SE VA A CERRAR POR INACTIVIDAD...')
        
    print('>>> EL PROGRAMA HA FINALIZADO CON ÉXITO...')


if __name__ == '__main__':
    main()