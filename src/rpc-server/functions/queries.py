
from database.database import Database

class QueryFunctions:
    def __init__(self):
        self.database = Database()

    def _execute_query(self, query, data):
        database = Database()
        try:
            result = database.selectOne(query, data)
            return result
        finally:
            database.disconnect()
    
    def buscar_clubes(self):
        database = Database()
        list_clubes = []

        results = database.selectAll("SELECT unnest(xpath('//Teams/Club/@Name', xml)) as result FROM imported_documents")
        database.disconnect()

        for club in results:
            if not club in list_clubes:
                list_clubes.append(club)

        return list_clubes