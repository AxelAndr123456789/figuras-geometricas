"""Módulo que define figuras geométricas y cálculo de sus áreas."""

from abc import ABC, abstractmethod


class FiguraGeometrica(ABC):  # pylint: disable=too-few-public-methods
    """Clase abstracta que define la interfaz para calcular áreas."""

    @abstractmethod
    def calcular_area(self):
        """Método abstracto para calcular el área de una figura."""
        raise NotImplementedError("Este método debe ser implementado por una subclase.")


class Rectangulo(FiguraGeometrica):  # pylint: disable=too-few-public-methods
    """Representa un rectángulo con base y altura."""

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        """Calcula el área del rectángulo."""
        return self.base * self.altura


class Triangulo(FiguraGeometrica):  # pylint: disable=too-few-public-methods
    """Representa un triángulo con base y altura."""

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        """Calcula el área del triángulo."""
        return (self.base * self.altura) / 2


class Circulo(FiguraGeometrica):  # pylint: disable=too-few-public-methods
    """Representa un círculo con un radio dado."""

    def __init__(self, radio):
        self.pi = 3.14159
        self.radio = radio

    def calcular_area(self):
        """Calcula el área del círculo."""
        return self.pi * (self.radio ** 2)


# Constantes globales
BASE_RECTANGULO = 10
ALTURA_RECTANGULO = 5
BASE_TRIANGULO = 7
ALTURA_TRIANGULO = 4
RADIO_CIRCULO = 3


if __name__ == "__main__":
    # Crear instancias de las figuras
    rectangulo = Rectangulo(BASE_RECTANGULO, ALTURA_RECTANGULO)
    triangulo = Triangulo(BASE_TRIANGULO, ALTURA_TRIANGULO)
    circulo = Circulo(RADIO_CIRCULO)

    # Calcular y mostrar las áreas
    print(f"El área del rectángulo es: {rectangulo.calcular_area()}")
    print(f"El área del triángulo es: {triangulo.calcular_area()}")
    print(f"El área del círculo es: {circulo.calcular_area()}")
