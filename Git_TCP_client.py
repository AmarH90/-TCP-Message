import socket


host = socket.gethostname()
port = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
while True:
    try:
        message_1 = input("\n\rClient Your message:\n\r\n\r ")
        to_str = str(message_1)
        s.sendall(message_1.encode())
        data = s.recv(1024)
        print("\n\rMessage receved:\n\r\n ",data)
    except socket.error:
        print("Error Occured at client")
        break
s.close()

