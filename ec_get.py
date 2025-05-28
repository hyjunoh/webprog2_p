import socket

HOST = '220.149.232.226'
PORT = 10017

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    request = (
        f"GET /greet?username=HJ HTTP/1.1\r\n"
        f"Host: {HOST}:{PORT}\r\n"
        f"Connection: close\r\n"
        f"\r\n"
    )
    s.sendall(request.encode('utf-8'))

    response = b''
    while True:
        chunk = s.recv(4096)
        if not chunk:
            break
        response += chunk

    print(response.decode('utf-8'))
