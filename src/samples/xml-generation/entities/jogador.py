import xml.etree.ElementTree as ET




class Jogador:

    def __init__(self, name: str,height, salary, price):
        Jogador.counter += 1
        self._id = Jogador.counter
        self._name = name
        self._height = height
        self._salary = salary
        self._price = price

        

    def to_xml(self):
        el = ET.Element("Player")
        el.set("Id", str(self._id))
        el.set("Height", self._height)
        el.set("Salary", self._salary)
        el.set("Price", self._price)
        

        return el

    def get_id(self):
        return self._id
    
    def __str__(self):
        return f"id:{self._name} id:({self._id})"


Jogador.counter = 0