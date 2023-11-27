from database.database import Database

class Documento:
    def importar_doc(self,ficheiro_xml,xml_content):
        
            database = Database()

            
            insert_query = "INSERT INTO public.imported_documents (file_name, xml) VALUES (%s, %s)"
            data = (ficheiro_xml, xml_content)
            database.insert(insert_query, data)
            

            return "Mandou para a BD!"
        
        

    def listar_doc():
        
            database = Database()
            dados = database.selectTudo(
                "SELECT id, file_name, xml, created_on, updated_on FROM imported_documents ")
            database.disconnect()
            return dados

    

    def soft_delete_by_filename(file_name):
        database = Database()
        database.soft_delete(file_name)
        return "Soft Delete aplicado com sucesso."

    

    
   




