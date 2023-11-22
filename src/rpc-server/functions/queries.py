
from database.database import Database
import psycopg2

class QueryFunctions:
    def __init__(self):
        self.database = Database()

    def _execute_query(self, query, data):
        database = Database()
        try:
            result = database.selectUm(query, data)
            return result
        finally:
            database.disconnect()
    
    def buscar_clubes(self):
        database = Database()
        list_clubes = []

        dados = database.selectTudo("SELECT unnest(xpath('//Teams/Club/@Name', xml)) as result FROM imported_documents")
        database.disconnect()

        for club in dados:
            if not club in list_clubes:
                list_clubes.append(club)

        return list_clubes
    

    def buscar_paises(self):
        database = Database()
        list_paises = []

        dados = database.selectTudo("SELECT unnest(xpath('//Countries/Country/@Name', xml)) as result FROM imported_documents")
        database.disconnect()

        for pais in dados:
            if not pais in list_paises:
                list_paises.append(pais)

        return list_paises

    def buscar_pe(self):
        database = Database()
        list_pe = []

        dados = database.selectTudo("SELECT unnest(xpath('//Strong_Foot/Foot/@Name', xml)) as result FROM imported_documents")
        database.disconnect()

        for pes in dados:
            if not pes in list_pe:
                list_pe.append(pes)

        return list_pe
    
    def buscar_top_jogadores(self):
        database = Database()
        list_jogadores = []

        dados = database.selectTudo("SELECT (xpath('//Player/Main_Stats/@Over', xml))::text::integer[] as result, (xpath('//Player/Information/@Name', xml))::text[] as name FROM imported_documents")
        database.disconnect()

        for result, name in dados:
            for jogador_over, jogador_name in zip(result, name):
                list_jogadores.append((jogador_over, jogador_name))

        # Ordenar a lista de jogadores por overall e pegar os 10 primeiros
        list_jogadores.sort(reverse=True)
        list_jogadores = list_jogadores[:10]

        return list_jogadores
    
    def buscar_estatisticas_jogador(self, nome_jogador):
        database = Database()
        # Escape single quotes in the player's name
        nome_jogador = nome_jogador.replace("'", "''")
        query =  '''
                SELECT unnest(xpath(format('//Players/Player[Information/@Name=''%s'']/Main_Stats/@*', %s), xml)) as result 
                FROM imported_documents
                '''
        dados = database.selectTudo(query, (nome_jogador, nome_jogador))
        database.disconnect()

        estatisticas = {}
        for dado in dados:
            estatisticas[dado[0]] = dado[1]

        return estatisticas


    
   