import socket
import sys

host = str(input("Enter ip address: "))
port = int(input("Enter listening port: "))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(5)
conn, addr= s.accept()
print(f"Connection Established{host}")
while True:
    cmd = input()
    if cmd == "Quit":
        conn.close()
        sys.exit()
    if len(str.encode(cmd)) > 0:
        conn.send(str.encode(cmd))
        clientResp = str(conn.recv(1024),'utf-8')
        print(clientResp,end='')