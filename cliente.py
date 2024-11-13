from websockets.sync.client import connect


def main():
    is_connected = False
    try:
        with connect('ws://localhost:5000/ws') as ws:
            is_connected = True
            while is_connected:
                message = input("Enter a message: ")
                ws.send(message)
                word_key = 'Desconexion'
                if message == word_key or message == word_key.upper() or message == word_key.lower():
                    is_connected = False
                    print(ws.recv())
                else:
                    response = ws.recv()
                    print(f"Received: {response}")
    except :
        is_connected = False        


if __name__ == "__main__":
    main()