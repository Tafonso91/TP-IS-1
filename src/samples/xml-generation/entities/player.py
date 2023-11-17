import xml.etree.ElementTree as ET
from entities.country import Country



class Player:
    def __init__(self, id, name, height, price, salary, country_id, strong_foot, ofensive_performance, defensive_performance):
        self._id = id
        self._name = name
        self._height = height
        self._price = price
        self._salary = salary
        self._country_id = country_id
        self._strong_foot = strong_foot
        self._ofensive_performance = ofensive_performance
        self._defensive_performance = defensive_performance

    def to_xml(self):
        player_el = ET.Element("Player")
        player_el.set("Id", str(self._id))
        player_el.set("countryRef", str(self._country_id))

        info_el = ET.Element("Information")
        info_el.set("name", self._name)
        info_el.set("height", str(self._height))
        info_el.set("price", self._price)
        info_el.set("salary", self._salary)
        player_el.append(info_el)

        stats_el = ET.Element("Statistics")
        stats_el.set("strong_foot", self._strong_foot.lower())
        stats_el.set("ofensive_performance", self._ofensive_performance.capitalize())
        stats_el.set("defensive_performance", self._defensive_performance.capitalize())
        player_el.append(stats_el)

        return player_el

    def __str__(self):
        return f"{self._name} ({self._id})"

Player.counter = 0
