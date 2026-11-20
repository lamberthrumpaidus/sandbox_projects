import socket


def check_open_port(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((host, port))
    return result == 0


# Mengecek port 80 (HTTP) pada host 'example.com'
host = 'example.com'
port = 80
if check_open_port(host, port):
    print(f'Port {port} terbuka di {host}')
else:
    print(f'Port {port} tertutup di {host}')
