import xml.etree.ElementTree as ET
from entities.country import Country



class Player:
    def __init__(self, id, name, height, price, salary,overall, potential, country_id,  strong_foot, ofensive_performance, defensive_performance, crossing, finishing, heading_accuracy, short_passing, volleys, dribbling, curve, fk_accuracy, long_pass, ball_control, accelaration, sprint, agility, reactions, balance, shot_power, jump, stamina, strenght, long_shot, agression, interception, positioning, vision, penalty, composure, defense_awareness, slide_tackle, diving,kicking, gk_positioning, reflexes):
        self._id = id
        self._name = name
        self._height = height
        self._price = price
        self._salary = salary
        self._overall= overall
        self._potential= potential
        self._country_id = country_id
        self._strong_foot = strong_foot
        self._ofensive_performance = ofensive_performance
        self._defensive_performance = defensive_performance
        self._crossing = crossing
        self._finishing = finishing
        self._heading_accuracy = heading_accuracy
        self._short_passing = short_passing
        self._volleys= volleys
        self._dribbling = dribbling
        self._curve = curve
        self._fk_accuracy = fk_accuracy
        self._long_pass = long_pass
        self._ball_control = ball_control
        self._acelaration = accelaration
        self._sprint = sprint
        self._agility = agility
        self._reactions = reactions
        self._balance = balance
        self._shot_power = shot_power
        self._jump = jump
        self._stamina = stamina
        self._strenght = strenght
        self._long_shot = long_shot
        self._agression = agression
        self._interception = interception
        self._positioning = positioning
        self._vision = vision
        self._penalty = penalty
        self._composure = composure
        self._defense_awareness = defense_awareness
        self._slide_tackle= slide_tackle
        self._diving = diving
        self._kicking = kicking
        self._gk_positioning = gk_positioning
        self._reflexes= reflexes




        
        
        


    def to_xml(self):
        player_el = ET.Element("Player")
        player_el.set("Id", str(self._id))
        player_el.set("countryRef", str(self._country_id))

        info_el = ET.Element("Information")
        info_el.set("Name", self._name)
        info_el.set("Height", str(self._height))
        info_el.set("Price", self._price)
        info_el.set("Salary", self._salary)
        
        player_el.append(info_el)

        stats_el = ET.Element("Main_Stats")
        stats_el.set("Over", self._overall)
        stats_el.set("Potential", self._potential)
        stats_el.set("Foot", self._strong_foot.lower())
        stats_el.set("Offense", self._ofensive_performance.capitalize())
        stats_el.set("Defense", self._defensive_performance.capitalize())
        player_el.append(stats_el)

        atack_el = ET.Element("Atack_Stats")
        atack_el.set("Crossing", self._crossing)
        atack_el.set("Finishing", self._finishing)
        atack_el.set("Heading", self._heading_accuracy)
        atack_el.set("Short_Pass", self._short_passing)
        atack_el.set("Volleys", self._volleys)
        player_el.append(atack_el)

        skill_el = ET.Element("Skill_Stats")
        skill_el.set("Crossing", self._crossing)
        skill_el.set("Finishing", self._finishing)
        skill_el.set("Heading", self._heading_accuracy)
        skill_el.set("Short_Pass", self._short_passing)
        skill_el.set("Volleys", self._volleys)
        player_el.append(skill_el)

        movement_el = ET.Element("Movement_Stats")
        movement_el.set("Acceleration", self._acelaration)
        movement_el.set("Sprint", self._sprint)
        movement_el.set("Agility", self._agility)
        movement_el.set("Reactions", self._short_passing)
        movement_el.set("Balance", self._balance)
        player_el.append(movement_el)

        power_el = ET.Element("Power_Stats")
        power_el.set("Shot_power", self._shot_power)
        power_el.set("Jump", self._jump)
        power_el.set("Stamina", self._stamina)
        power_el.set("Strenght", self._strenght)
        power_el.set("Long_shot", self._long_shot)
        player_el.append(power_el)

        

        return player_el

    def __str__(self):
        return f"{self._name} ({self._id})"

Player.counter = 0
