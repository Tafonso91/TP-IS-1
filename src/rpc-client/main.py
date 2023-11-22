import xmlrpc.client

print("connecting to server...")
server = xmlrpc.client.ServerProxy('http://is-rpc-server:9000')


    

   



def listar_clubes():
    try:
        clubes = server.buscar_clubes()
        if clubes:
            print("\nLista dos clubes:")
            for clube in clubes:
                print(f"- {clube}")
        else:
            print("Nada foi encontrado.")
    except Exception as e:
        print(f"Erro: {e}")

def listar_paises():
    try:
        paises = server.buscar_paises()
        if paises:
            print("\nLista dos países:")
            for pais in paises:
                print(f"- {pais}")
        else:
            print("Nada foi encontrado.")
    except Exception as e:
        print(f"Erro: {e}")

def listar_pe():
    try:
        pes = server.buscar_pe()
        if pes:
            print("\nLista dos pés preferidos:")
            for pe in pes:
                print(f"- {pe}")
        else:
            print("Nada foi encontrado.")
    except Exception as e:
        print(f"Erro: {e}")

def listar_jogadores():
    try:
        jogadores = server.buscar_top_jogadores()
        if jogadores:
            print("\n10 jogadores com maior overall:")
            for jogador in jogadores:
                print(f"- {jogador}")
        else:
            print("Nada foi encontrado.")
    except Exception as e:
        print(f"Erro: {e}")

def buscar_estatisticas_jogador():
    try:
        nome_jogador = input("Insira o nome do jogador: ")
        estatisticas = server.buscar_estatisticas_jogador(nome_jogador)
        if estatisticas:
            print(f"\nEstatísticas para {nome_jogador}:")
            for stat, valor in estatisticas.items():
                print(f"- {stat}: {valor}")
        else:
            print("Jogador não encontrado.")
    except Exception as e:
        print(f"Erro: {e}")


def main():
    while True:
        print("\n***** Queries *****")
        print("1 -Listagem dos clubes")
        print("2 -Listagem dos países")
        print("3 -Listagem dos pés preferidos")
        print("4 -10 jogadores com maior overall")
        print("5 -Pesquisar stats dum jogador")
        print("0 - Sair")

        option = input("Escolha uma opção: ")

        if option == '1':
            listar_clubes()
            continue

        if option == '2':
            listar_paises()
            continue

        if option == '3':
            listar_pe()
            continue

        if option == '4':
            listar_jogadores()
            continue
        if option == '5':
            buscar_estatisticas_jogador()
            continue   
        
        elif option == '0':
            print("\nA sair!")
            break
        else:
            print("\nOpção errada ,insira outro número.")

if __name__ == "__main__":
    main()
