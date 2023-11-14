import xml.etree.ElementTree as ET


class Atributo:

    def __init__(self, height,salary,price):
        Atributo.counter += 1
        self._id = Atributo.counter
        self._height = height
        self._salary = salary
        self._price = price
       

    def to_xml(self):
        el = ET.Element("Atributos")
        el.set("Id", str(self._id))
        el.set("Height", self._height)
        el.set("Salary", self._salary)
        el.set("Price", self._price)
        
        return el

    def __str__(self):
        return f"{self._height}, {self._salary}, {self._price}"


Atributo.counter = 0

