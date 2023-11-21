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


def main():
    while True:
        print("\n-----> Menu <------")
        print("1 -Listagem dos clubes")
        print("0 - Sair")

        option = input("Choose an option: ")

        if option == '1':
            listar_clubes()
            continue  
        
        elif option == '0':
            print("\nA sair!")
            break
        else:
            print("\nOpção errada ,insere outro número.")

if __name__ == "__main__":
    main()
