
import xmlrpc.client
from xml.etree import ElementTree as ET

print("connecting to server...")
server = xmlrpc.client.ServerProxy('http://is-rpc-server:9000')


# Function to list all clubs
def listar_clubes():
    try:
        clubes = server.lista_clubes()
        if clubes:
            print("\nLista dos clubes:")
            for clube in clubes:
                print(f"- {clube}")
        else:
            print("Nada foi encontrado.")
    except Exception as e:
        print(f"Erro: {e}")
# Function to list all players
def listar_jogadores():
    try:
        jogadores = server.lista_todos_jogadores()
        if jogadores:
            print("\nLista dos jogadores:")
            for jogador in jogadores:
                print(f"- {jogador}")
        else:
            print("Nada foi encontrado.")
    except Exception as e:
        print(f"Erro: {e}")


# Function to list all countries
def listar_paises():
    try:
        paises = server.lista_paises()
        if paises:
            print("\nLista dos países:")
            for pais in paises:
                print(f"- {pais}")
        else:
            print("Nada foi encontrado.")
    except Exception as e:
        print(f"Erro: {e}")


# Function to list all preferred feet
def listar_pe():
    try:
        pes = server.lista_pe()
        if pes:
            print("\nLista dos pés preferidos:")
            for pe in pes:
                print(f"- {pe}")
        else:
            print("Nada foi encontrado.")
    except Exception as e:
        print(f"Erro: {e}")


# Function to list top 10 players
def listar_top_jogadores():
    try:
        jogadores = server.lista_top_jogadores()
        if jogadores:
            print("\n10 jogadores com maior overall:")
            for jogador in jogadores:
                print(f"- {jogador}")
        else:
            print("Nada foi encontrado.")
    except Exception as e:
        print(f"Erro: {e}")


# Function to search for players by team
def pesquisar_jogador():
    try:
        nome_equipa = input("Insira o nome da equipa: ")
        jogadores = server.lista_jogadores(nome_equipa)
        if jogadores:
            print("\nLista dos jogadores:")
            for jogador in jogadores:
                print(f"- {jogador}")
        else:
            print("Nada foi encontrado.")
    except Exception as e:
        print(f"Erro: {e}")


# Function to list Portuguese promising players
def promessas_tugas():
    try:
        promessas = server.lista_promessas_portugal()
        if promessas:
            print("\nPromessas portuguesas:")
            for promessa in promessas:
                print(f"Nome: {promessa[1]}")
                print(f"Overall: {promessa[2]}")
                print(f"Potencial: {promessa[0]}")
                print(f"Altura: {promessa[3]}cm")
                print(f"Preço: {promessa[4]}")
                print(f"Salário: {promessa[5]}\n")
        else:
            print("Nada foi encontrado.")
    except Exception as e:
        print(f"Erro: {e}")







# Function to search for a player's statistics
def pesquisar_stat():
    try:
        nome_jogador = input("Insira o nome do jogador: ")
        tipo_estatistica = input(f"""Insira o tipo de estatística que deseja ver do {nome_jogador}:
| 'ataque'     | 'guarda-redes' | 'informação' | 'principal' |
| 'skill'      | 'movimento'    | 'força'      | 'mental'    |
| 'defesa'     |
Escolha uma opção: """)

        estatisticas = server.lista_estatisticas_jogador(nome_jogador, tipo_estatistica)
        if estatisticas:
            print(f"\nEstatísticas de {tipo_estatistica} do {nome_jogador}:")
            for estatistica in estatisticas:
                element = ET.fromstring(estatistica)
                for attr, value in element.attrib.items():
                    print(f"{attr} = {value}")
        else:
            print("Nada foi encontrado.")
    except Exception as e:
        print(f"Erro: {e}")

def importa_documento():
    
        caminho = input("\nIntroduz o caminho do xml: ")

        if not caminho:
            print("Tenta outra vez")
            return 0

        with open(caminho, 'r', encoding='utf-8') as xml_file:
            xml_content = xml_file.read()

        dados = server.importar_doc(xml_content, caminho)
        print(dados)

def listar_jogadores_benfica():
    try:
        jogadores_benfica = server.lista_jogadores_benfica()
        if jogadores_benfica:
            print("\nLista dos jogadores do Benfica:")
            for jogador in jogadores_benfica:
                print(f"- {jogador}")
        else:
            print("Nada foi encontrado.")
    except Exception as e:
        print(f"Erro: {e}")


def main():

       while True:
        print("\n***** Menu Principal *****")
        print("1 - Queries")
        print("2 - XML")
        print("0 - Sair")

        main_option = input("Escolhe uma opção: ")

        if main_option == '1':
            queries_menu()
        elif main_option == '2':
            xml_menu()
        elif main_option == '0':
            print("\nA sair!")
            break
        else:
            print("\nOpção errada, escolhe outro número.")

def queries_menu():
    while True:
        print("\n***** Queries *****")
        print("1 - Listagem dos clubes")
        print("2 - Listagem dos países")
        print("3 - Listagem dos jogadores")
        print("4 - Listagem dos pés preferidos")
        print("5 - 10 jogadores com maior overall")
        print("6 - Pesquisar jogadores por equipa")
        print("7 - Promessas portuguesas")
        print("8 - Pesquisar estatística jogador")
        print("0 - Voltar ao Menu Principal")

        query_option = input("Escolhe uma opção: ")

        if query_option == '1':
            listar_clubes()
        elif query_option == '2':
            listar_paises()
        elif query_option == '3':
            listar_jogadores()
        elif query_option == '4':
            listar_pe()
        elif query_option == '5':
            listar_top_jogadores()
        elif query_option == '6':
            pesquisar_jogador()
        elif query_option == '7':
            promessas_tugas()
        elif query_option == '8':
            pesquisar_stat()
        elif query_option == '0':
            print("\nEstou a voltar ao Menu Principal.")
            break
        else:
            print("\nOpção errada, escolhe outro número.")

def xml_menu():
    while True:
        print("***** XML *****")
        print("1 - Importar para a BD")
        print("2 - Listar Documentos")
        print("3 - Soft Delete")
        print("0 - Voltar ao Menu Principal")

        xml_option = input("Escolhe uma opção: ")

        if xml_option == '1':
            importa_documento()
        elif xml_option == '2':
            importa_documento()
        elif xml_option == '3':
            importa_documento()
        elif xml_option == '0':
            print("\nEstou a voltar ao Menu Principal.")
            break
        else:
            print("\nOpção errada, escolhe outro número.")
    
if __name__ == "__main__":
    main()
