import sims4.commands
from sims4.commands import CheatOutput
import socket

# Настройки сокета для подключения к серверу
HOST = '127.0.0.1'  # Локальный хост
PORT = 65432        # Порт для сокет-соединения

# Функция для проверки наличия мода WickedWhims
def is_wickedwhims_installed():
    try:
        import wickedwhims
        return dir(wickedwhims)
    except ImportError:
        return False

# Функция для активации вибрации
def start_vibration():
    try:
        # Отправка команды через сокет
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))  # Подключаемся к серверу
            s.sendall(b"start_vibration")  # Отправляем команду на сервер
            s.close()
        print("Вибрация активирована.")
    except Exception as e:
        print(f"Ошибка при подключении к сокет-серверу: {e}")

# Функция для завершения вибрации
def stop_vibration():
    try:
        # Отправка команды через сокет
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))  # Подключаемся к серверу
            s.sendall(b"stop_vibration")  # Отправляем команду на сервер
            s.close()
        print("Вибрация завершена.")
    except Exception as e:
        print(f"Ошибка при подключении к сокет-серверу: {e}")

# Обработчик для начала вуху
def on_woohoo_started():
    if is_wickedwhims_installed():
        start_vibration()

# Обработчик для завершения вуху
def on_woohoo_ended():
    stop_vibration()

# Основная команда для игры
@sims4.commands.Command('vibrationmod', command_type=sims4.commands.CommandType.Live)
def vibrationmod(_connection=None):
    output = CheatOutput(_connection)
    output("Запуск мода вибрации для вуху.")

    # Тестовая отправка команды на сокет
    start_vibration()  # Отправляем команду на начало вибрации
    output("Команда для вибрации отправлена на сервер.")

    # Завершаем вибрацию для теста
    stop_vibration()  # Отправляем команду на завершение вибрации
    output("Команда для завершения вибрации отправлена на сервер.")

# Обработчик для отслеживания вуху
def handle_woohoo_event(event):
    if event == "start":
        on_woohoo_started()
    elif event == "end":
        on_woohoo_ended()

# Регистрация события для вуху (использование события)
def register_woohoo_event():
    start_vibration()
    pass

# Команда для проверки наличия мода WickedWhims
@sims4.commands.Command('checkwickedwhims', command_type=sims4.commands.CommandType.Live)
def checkwickedwhims(_connection=None):
    output = CheatOutput(_connection)
    iswwi = is_wickedwhims_installed()
    if iswwi is not False:
        output("Мод WickedWhims установлен.")
        output(" ".join(iswwi))
    else:
        output("Мод WickedWhims не установлен.")
