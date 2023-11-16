import xml.etree.ElementTree as ET
from entities.country import Country

class Player:

    def __init__(self,id, name, height,price,salary, country_id):
        
        self._id = id
        self._name = name
        self._height = height
        self._price = price
        self._salary = salary
        self._country_id = country_id
        
        


    def to_xml(self):
        el = ET.Element("Player")
        el.set("Id", str(self._id))

        name_el = ET.Element("Name")
        name_el.text = self._name
        el.append(name_el)

        height_el = ET.Element("Height")
        height_el.text = str(self._height)
        el.append(height_el)

        price_el = ET.Element("Price")
        price_el.text = self._price
        el.append(price_el)

        salary_el = ET.Element("Salary")
        salary_el.text = self._salary
        el.append(salary_el)

        country_el = ET.Element("CountryId")  # Modificado para incluir o ID do país
        country_el.text = str(self._country_id)
        el.append(country_el)

        return el

    def __str__(self):
        return f"{self._name} ({self._id})"


Player.counter = 0
