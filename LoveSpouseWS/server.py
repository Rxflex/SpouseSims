import socket
import lovespouse as ls
import time

# Настройки сокет-сервера
HOST = '127.0.0.1'  # Локальный хост
PORT = 65432        # Порт для прослушивания

# Функция для обработки команд
def process_command(command):
    if command == "start_vibration":
        print("Вибрация началась!")
        ls.SHAKE(1, 1)
    elif command == "stop_vibration":
        print("Вибрация завершена!")
        ls.OFF()
    else:
        print(f"Неизвестная команда: {command}")

# Создание сокета и прослушивание подключений
def start_socket_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Ожидание подключения на {HOST}:{PORT}...")
        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Подключено к {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    command = data.decode('utf-8')
                    process_command(command)

# Запуск сервера
if __name__ == "__main__":
    start_socket_server()
