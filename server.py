import socket

def run_server(host="127.0.0.1", port=65432):
    # Создаем серверный сокет
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Сервер запущен на {host}:{port} и ожидает соединений...")
        try:
            while True:
                conn, addr = server_socket.accept()  # Ожидание соединения
                with conn:
                    print(f"Соединение установлено с {addr}")
                    while True:
                        data = conn.recv(1024)  # Получение данных
                        if not data:
                            break
                        print(f"Получено сообщение: {data.decode()}")

                        # Проверяем, если это "ping"
                        if data.decode().lower() == "ping":
                            conn.sendall(b"pong")  # Отправка ответа "pong"
                            print("Ответ отправлен: pong")
                        else:
                            conn.sendall(b"unknown command")  # Ответ на неизвестный запрос
                            print("Ответ отправлен: unknown command")
        except KeyboardInterrupt:
            print("\nСервер завершает работу.")

if __name__ == "__main__":
    run_server()
