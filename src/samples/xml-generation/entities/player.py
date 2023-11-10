import xml.etree.ElementTree as ET


class Player:

    def __init__(self, name, overall, country):
        Player.counter += 1
        self._id = Player.counter
        self._name = name
        self._overall = overall
        self._country = country

    def to_xml(self):
        el = ET.Element("Player")
        el.set("id", str(self._id))
        el.set("name", self._name)
        el.set("Overall", self._overall)
        el.set("Country", str(self._country.get_id()))
        return el

    def __str__(self):
        return f"{self._name}, Overall:{self._overall}, Country:{self._country}"


Player.counter = 0
