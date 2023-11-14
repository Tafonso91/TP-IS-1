import xml.etree.ElementTree as ET


class Player:

    def __init__(self, name):
        Player.counter += 1
        self._id = Player.counter
        self._name = name
       

    def to_xml(self):
        el = ET.Element("Player")
        el.set("Id", str(self._id))
        el.set("Name", self._name)
        
        return el

    def __str__(self):
        return f"{self._name}"


Player.counter = 0
