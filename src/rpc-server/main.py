import signal, sys
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
from functions.csv_to_xml_converter import CSVtoXMLConverter
from lxml import etree as ETREE

from functions.string_length import string_length
from functions.string_reverse import string_reverse
from database.database import Database

from functions.queries import QueryFunctions




class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


with SimpleXMLRPCServer(('0.0.0.0', 9000), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()
    query_functions = QueryFunctions()
    database=Database()
    
    
    
    def signal_handler(signum, frame):
        print("received signal")
        server.server_close()

        # perform clean up, etc. here...

        print("exiting, gracefully")
        sys.exit(0)
    
        
    csv_file = "/data/fifa23.csv"
    xml_file = "/data/fifa23.xml"
    xsd_file = "/data/schema.xsd"
    converter = CSVtoXMLConverter("/data/fifa_23.csv")
    xml_str = converter.to_xml_str()  # Obtém a representação XML como string

   
   
    # Carrega o schema XSD
    with open(xsd_file, 'r') as schema_file:
        schema_doc = ETREE.parse(schema_file)
        schema = ETREE.XMLSchema(schema_doc)

    # Carrega o XML como um objeto lxml
    xml_doc = ETREE.fromstring(xml_str)

    # Valida o XML contra o schema

    try:
        schema.assertValid(xml_doc)
        # Escreve a string XML em um arquivo
        with open("/data/fifa_23.xml", "w") as xml_file:
            xml_file.write(xml_str)
        print("Validação concluída com sucesso!") 
        print("Arquivo XML 'fifa_23.xml' criado com sucesso!") 
        with open("/data/fifa_23.xml", "r") as xml_file:  
            xml_content = xml_file.read()
        
        insert_query = "INSERT INTO public.imported_documents (file_name, xml) VALUES (%s, %s)"
        data = ("/data/fifa23.xml", xml_content)
        database.insert(insert_query, data)

        
    except ETREE.DocumentInvalid as e:
        # Se o XML não é válido, imprime o(s) erro(s)
        print("Erro de validação XML:")
        print(e)

   
    # signals
    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGHUP, signal_handler)
    signal.signal(signal.SIGINT, signal_handler)

    # register both functions
    server.register_function(query_functions.lista_clubes)
    server.register_function(query_functions.lista_paises)
    server.register_function(query_functions.lista_pe)
    server.register_function(query_functions.lista_top_jogadores)
    server.register_function(query_functions.lista_jogadores)
    server.register_function(query_functions.lista_promessas_portugal)
    server.register_function(query_functions.lista_estatisticas_jogador)
    server.register_function(string_reverse)
    server.register_function(string_length)

    # start the server
    print("Starting the RPC Server...")
    server.serve_forever()
