"""
 * Crea un programa que cuente cuantas veces se repite cada palabra
 * y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que
 *   lo resuelvan automáticamente.
"""

def get_phrase():
    while True:
        phrase = input('Escriba una frase:\n').strip()

        if phrase != '':
            return phrase.lower()

        print('Por favor, introduzca una frase a continuación...')

def get_substrings(string):
    substrings = list()
    substring = str()

    for i in range(len(string)):
        if string[i].isalpha():
            substring += string[i]
        else:
            if i == len(string):
                substrings.append(substring)
                substring = str()
            else:
                substrings.append(substring)
                substring = str()

    substrings.sort()
    return substrings

def counter_words_in_list(list_words):
    words = list_words
    words_unique = set(list_words)

    count_words = {word:0 for word in words_unique}

    for key_word in count_words.keys():
        for word in words:
            if key_word == word:
                count_words[key_word] += 1

    return count_words

def main():
    phrase = get_phrase()
    words = get_substrings(phrase)
    counter_words = counter_words_in_list(words)

    for i in counter_words.keys():
        print(f'La palabra "{i}" se repite {counter_words[i]} veces.')

if __name__ == '__main__':
    main()
