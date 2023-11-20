import signal, sys
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
from functions.csv_to_xml_converter import CSVtoXMLConverter

from functions.string_length import string_length
from functions.string_reverse import string_reverse



class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


with SimpleXMLRPCServer(('0.0.0.0', 9000), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    
    def signal_handler(signum, frame):
        print("received signal")
        server.server_close()

        # perform clean up, etc. here...

        print("exiting, gracefully")
        sys.exit(0)
    converter = CSVtoXMLConverter("/data/fifa_23.csv")
    xml_str = converter.to_xml_str()  # Obtém a representação XML como string

    # Escreve a string XML em um arquivo
    with open("/data/fifa_23.xml", "w") as xml_file:
        xml_file.write(xml_str)

    print("Arquivo XML 'fifa_23.xml' criado com sucesso!")
    


    # signals
    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGHUP, signal_handler)
    signal.signal(signal.SIGINT, signal_handler)

    # register both functions
    server.register_function(string_reverse)
    server.register_function(string_length)

    # start the server
    print("Starting the RPC Server...")
    server.serve_forever()
