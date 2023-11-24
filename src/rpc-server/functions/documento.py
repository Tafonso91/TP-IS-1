from database.database import Database

class Documento:
    def importar_documento(ficheiro_xml,xml_content):
        
            database = Database()

            
            insert_query = "INSERT INTO public.imported_documents (file_name, xml) VALUES (%s, %s)"
            data = (ficheiro_xml, xml_content)
            database.insert(insert_query, data)
            

            return "Mandou pa BD!"

    def listar_documentos():
        
            database = Database()
            dados = database.selectTudo(
                "SELECT id, file_name, xml, created_on, updated_on FROM imported_documents ")
            database.disconnect()
            return dados

    

    def delete_documentos(ficheiro):
    
            database = Database()

            database.softdelete(ficheiro)

            return "Soft Delete aplicado com sucesso."

    

    
   




