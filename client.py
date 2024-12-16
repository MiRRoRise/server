import socket
import sys
def run_client(host="127.0.0.1", port=65433):
    # Создаем клиентский сокет
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.settimeout(10)
        try:
            client_socket.connect((host, port))
        except TimeoutError:
            print("\nСервер не отвечает. Клиент завершает работу.")
            return
        except ConnectionResetError:
            print("\nСервер не отвечает. Клиент завершает работу.")
            return
        print(f"Соединение с сервером {host}:{port} установлено.")
        
        try:
            while True:
                # Отправляем сообщение "ping"
                message = input("Введите сообщение (или 'exit' для выхода): ").strip()
                if message.lower() == "exit":
                    print("Завершаем работу клиента.")
                    break
                client_socket.sendall(message.encode())  # Отправляем сообщение
                print(f"Отправлено сообщение: {message}")

                # Получаем ответ от сервера
                data = client_socket.recv(1024)
                if(data.decode()==""):
                    print("Сервер завершает свою работу. Завершаем работу клиента.")
                    break
                print(f"Ответ сервера: {data.decode()}")
        except KeyboardInterrupt:
            print("\nКлиент завершает работу.")


if __name__ == "__main__":
    run_client(sys.argv[1],int(sys.argv[2]))

