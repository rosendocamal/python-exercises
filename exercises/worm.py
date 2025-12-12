import shutil
import sys

if len(sys.argv) == 2:
    for num in range(0, int(sys.argv[1])):
        shutil.copy(sys.argv[0], sys.argv[0] + f'{num}')


"""
Usar así en la terminal: 

$ python3 file.py num

Donde file.py es el archivo donde se guarda el script y num la cantidad de archivos a crear

"""