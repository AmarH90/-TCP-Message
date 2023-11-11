import socket

host = ""
port = 12345
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
print(host, port)
s.listen(1)
conn, addr = s.accept()
print("\n\rConnect by ", addr)
while True:
    try:
        data = conn.recv(1024)
        if not data: break
        print ("\n\rClient Says:\n\r\n\r ", data)
        message_s = input("\n\rServer enter  your message:\n\r\n\r ")
        to_send_s = str(message_s)
        conn.sendall(message_s.encode())

    except socket.error: 
        print ("Error Occured.")
        break
conn.close()
