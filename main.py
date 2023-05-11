import socket
import threading

# Функція для перевірки доступності запису для редагування
def check_record_access(record_id):
    if record_id == "1":
        return True
    else:
        return False


# Функція для передачі записів клієнту
def send_records(client_socket):
    # Передача даних:
    records = ["Запис 1", "Запис 2", "Запис 3"]
    data = "\n".join(records)
    client_socket.send(data.encode())


# Функція для обробки підключення клієнта
def handle_client(client_socket):
    # Отримання ID запису від клієнта
    record_id = client_socket.recv(1024).decode()

    # Перевірка доступності запису
    if check_record_access(record_id):
        # Якщо запис доступний, відправляємо записи клієнту
        send_records(client_socket)
    else:
        # Якщо запис недоступний, відправляємо повідомлення про відмову в доступі
        message = "Запис недоступний для редагування"
        client_socket.send(message.encode())

    # Закриття з'єднання з клієнтом
    client_socket.close()


# Головна функція сервера
def run_server():
    host = '127.0.0.1'  # IP-адреса сервера
    port = 12345  # Порт сервера

    # Створення сокету
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))

    # Незавершені з'єднання очікуються на черзі до 5 клієнтів
    server_socket.listen(5)
    print("Сервер запущений.")

    while True:
        # Прийом нового з'є
        client_socket, addr = server_socket.accept()
        print(f"З'єднання з клієнтом {addr} встановлено.")
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

# Запуск сервера в окремому потоці
server_thread = threading.Thread(target=run_server)
server_thread.start()
