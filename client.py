import socket

def edit_records(record_id):
    server_host = '127.0.0.1'  # IP-адреса сервера
    server_port = 12345  # Порт сервера

    # Створення сокету
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Підключення до сервера
        client_socket.connect((server_host, server_port))

        # Відправка ID запису на сервер
        client_socket.send(record_id.encode())

        # Отримання даних від сервера
        data = client_socket.recv(1024).decode()
        print("Отримані записи:")
        print(data)
    except ConnectionRefusedError:
        print("Помилка підключення до сервера.")

    # Закриття з'єднання з сервером
    client_socket.close()

record_id = input("Введіть ID запису для редагування: ")
edit_records(record_id)