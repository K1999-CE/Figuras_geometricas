class Color:
    def __init__(self, nombre):
        self._nombre = nombre

    def __str__(self):
        return f'Color: {self._nombre}'

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

if __name__ == '__main__':
    c1 = Color('Rojo')
    print(c1)
