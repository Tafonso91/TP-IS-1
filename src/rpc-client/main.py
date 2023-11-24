
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
                print(f"- {promessa}")
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





def main():
    while True:
        print("\n***** Queries *****")
        print("1 -Listagem dos clubes")
        print("2 -Listagem dos países")
        print("3 -Listagem dos jogadores")
        print("4 -Listagem dos pés preferidos")
        print("5 -10 jogadores com maior overall")
        print("6 -Pesquisar jogadores por equipa")
        print("7 -Promessas portuguesas")
        print("8 -Pesquisar estatística jogador")
        

        print("0 - Sair")

        option = input("Escolha uma opção: ")

        if option == '1':
            listar_clubes()
            continue

        if option == '2':
            listar_paises()
            continue

        if option == '3':
            listar_jogadores()
            continue

        if option == '4':
            listar_pe()
            continue

        if option == '5':
            listar_top_jogadores()
            continue

        if option == '6':
            pesquisar_jogador()
            continue

        if option == '7':
            promessas_tugas()
            continue

        if option == '8':
            pesquisar_stat()
            continue

        

        elif option == '0':
            print("\nA sair!")
            break
        else:
            print("\nOpção errada ,insira outro número.")

if __name__ == "__main__":
    main()
