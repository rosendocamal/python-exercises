"""
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
"""

class Polygon:
    def __init__(self, name, sides, side1, side2):
        self.name = name
        self.sides = sides
        self.side1 = side1
        self.side2 = side2

    def area(self):
        sub_area = self.side1 * self.side2
        if self.sides == 3:
            return sub_area / 2
        return sub_area

    def name_area(self):
        print(f"El área de \"{self.name.lower()}\" es {self.area()} u².")


def main():
    triangle = Polygon("triangle", 3, 2, 3)
    square = Polygon("square", 4, 2, 2)
    rectangle = Polygon("rectangle", 4, 2, 4)

    triangle.name_area()
    square.name_area()
    rectangle.name_area()

if __name__ == "__main__":
    main()
