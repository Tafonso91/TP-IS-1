import xml.etree.ElementTree as ET

from entities.atributo import Atributo


class Jogador:

    def __init__(self, name: str):
        Jogador.counter += 1
        self._id = Jogador.counter
        self._name = name
        self._atributos = []

    def add_atributo(self, atributos: Atributo):
        self._atributos.append(atributos)

    def to_xml(self):
        el = ET.Element("Player")
        el.set("Id", str(self._id))
        el.set("Name", self._name)

     
        atributos_el = ET.Element("Informações")
        for atributo in self._atributos:
            atributos_el.append(atributo.to_xml())   

        el.append(atributos_el)

        return el

    def __str__(self):
        return f"{self._name} ({self._id})"


Jogador.counter = 0