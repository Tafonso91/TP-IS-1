import xml.etree.ElementTree as ET

class Atributo:

    def __init__(self, price, height, salary):
        Atributo.counter += 1
        self._id = Atributo.counter
        self._price = price
        self._height= height
        self._salary = salary

    def to_xml(self):
        el = ET.Element("Player")
        el.set("Price", self._price)
        el.set("Height", self._height)
        el.set("Salary", self._salary)
        return el

    def __str__(self):
        return f"Preço:{self._price}, Altura:{self._height}, Salário:{self._salary}"


Atributo.counter = 0