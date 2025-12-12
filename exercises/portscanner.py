import socket

ip = input("Ingrese la dirección IP a escanear:\n")

for port in range(1, 65535):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)

    result = sock.connect_ex((ip, port))

    if result == 0:
        print(f"Puerto {port} se encuentra en estado abierto")
        sock.close()
    else:
        print(f"Puerto {port} se encuentra en estado cerrado")