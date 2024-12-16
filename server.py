import socket
from threading import Thread
import sys

def serve(conn, addr):
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



def start_server(host="127.0.0.1", port=65433):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        try:
            server_socket.bind((host, port))
            server_socket.listen()
            print(f"Сервер запущен на {host}:{port} и ожидает соединений...")
            while True:
                try:
                    conn, addr = server_socket.accept()
                    t = Thread(target=serve, args=(conn,addr), daemon=True)
                    t.start()
                except KeyboardInterrupt:
                    print("\nСервер завершает свою работу")
                    break
        except OSError:
            print("Сервер не может быть запущен порт занят")

if __name__ == "__main__":
    start_server(sys.argv[1],int(sys.argv[2]))

