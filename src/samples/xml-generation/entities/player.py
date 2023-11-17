import xml.etree.ElementTree as ET
from entities.country import Country



class Player:
    def __init__(self, id, name, height, price, salary,overall, potential, performance, country_id,  strong_foot, ofensive_performance, defensive_performance, crossing, finishing, heading_accuracy, short_passing, volleys ):
        self._id = id
        self._name = name
        self._height = height
        self._price = price
        self._salary = salary
        self._overall= overall
        self._potential= potential
        self._performance= performance
        self._country_id = country_id
        self._strong_foot = strong_foot
        self._ofensive_performance = ofensive_performance
        self._defensive_performance = defensive_performance
        self._crossing = crossing
        self._finishing = finishing
        self._heading_accuracy = heading_accuracy
        self._short_passing = short_passing
        self._volleys= volleys
        
        


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

        stats_el = ET.Element("General_Stats")
        stats_el.set("Overall", self._overall)
        stats_el.set("Potential", self._potential)
        stats_el.set("Performance", self._performance)
        stats_el.set("strong_foot", self._strong_foot.lower())
        stats_el.set("ofensive_performance", self._ofensive_performance.capitalize())
        stats_el.set("defensive_performance", self._defensive_performance.capitalize())
        player_el.append(stats_el)

        atack_el = ET.Element("Attacking_Stats")
        atack_el.set("Crossing", self._crossing)
        atack_el.set("Finishing", self._finishing)
        atack_el.set("Heading_accuracy", self._heading_accuracy)
        atack_el.set("Short_Passing", self._short_passing)
        atack_el.set("Volleys", self._volleys)
        player_el.append(atack_el)

        return player_el

    def __str__(self):
        return f"{self._name} ({self._id})"

Player.counter = 0
