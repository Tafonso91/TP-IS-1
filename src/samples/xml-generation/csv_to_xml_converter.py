import csv
import xml.dom.minidom as md
import xml.etree.ElementTree as ET

from csv_reader import CSVReader
from entities.country import Country
from entities.team import Team
from entities.player import Player
from entities.jogador import Jogador
from entities.atributo import Atributo


class CSVtoXMLConverter:

    def __init__(self, path):
        self._reader = CSVReader(path)

    def to_xml(self):
        # read countries
        countries = self._reader.read_entities(
            attr="Country",
            builder=lambda row: Country(row["Country"])
        )

        # read teams
        teams = self._reader.read_entities(
            attr="Club",
            builder=lambda row: Team(row["Club"])
        )

        # read players

        def after_creating_player(player, row):
            # add the player to the appropriate team
            teams[row["Club"]].add_player(player)

        self._reader.read_entities(
            attr="Name",
            builder=lambda row: Player(
                name=row["Name"],
                overall=row["Overall"],
                country=countries[row["Country"]]
            ),
            after_create=after_creating_player
        )

        # read Jogador
        jogadores = self._reader.read_entities(
            attr="Name",
            builder=lambda row: Jogador(row["Name"])
        )

         # read atributos

        def after_creating_atributo(atributo, row):
            # add the player to the appropriate team
            jogadores[row["Name"]].add_atributo(atributo)

        self._reader.read_entities(
            attr="Name",
            builder=lambda row: Atributo(
                price=row["Price"],
                height=row["Height"],
                salary=row["Salary"]
                
            ),
            after_create=after_creating_atributo
        )
        

        # generate the final xml
        root_el = ET.Element("Football")

        teams_el = ET.Element("Club")
        for team in teams.values():
            teams_el.append(team.to_xml())

        countries_el = ET.Element("Country")
        for country in countries.values():
            countries_el.append(country.to_xml())

        jogadores_el = ET.Element("Players")
        for jogador in jogadores.values():
            jogadores_el.append(jogador.to_xml())

        root_el.append(teams_el)
        root_el.append(countries_el)
        root_el.append(jogadores_el)

        return root_el

    def to_xml_str(self):
        xml_str = ET.tostring(self.to_xml(), encoding='utf8', method='xml').decode()
        dom = md.parseString(xml_str)
        return dom.toprettyxml()

