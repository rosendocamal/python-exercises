# Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica.

def get_nums():
    nums = input('>>> INTRODUZCA UNA LISTA DE NÚMEROS SEPARADOS POR UNA COMA:\n>>> ').strip().split(',')

    nums_temp = list()

    for i in nums:
        try:
            nums_temp.append(float(i))
        except ValueError:
            pass
    
    return nums_temp

def calculate_average(nums):
    average = 0

    for i in nums:
        average += i / len(nums)

    return average


def calculate_standard_deviation(nums, average):
    desviations = 0

    for i in nums:
        desviations += (i - average) ** 2

    return (desviations / len(nums)) ** (1/2)


def main():
    nums = get_nums()
    if not nums:
        print('>>> NO SE INTRODUJERON NÚMEROS VÁLIDOS')
        return
    
    average = calculate_average(nums)
    s_desviation = calculate_standard_deviation(nums, average)

    print(f'>>>\n>>> CALCULANDO EL PROMEDIO...\n>>> CALCULANDO LA DESVIACIÓN TÍPICA (TODOS LOS NÚMEROS)...\n>>>')
    print(f'>>> EL PROMEDIO ES: {average}\n>>> LA DESVIACIÓN TÍPICA ES: {s_desviation:.2f}')

if __name__ == '__main__':
    main()