# server.py
import socket

s = socket.socket()
host="192.168.20.25"
port = 8080
s.bind((host,port))

s.listen(5)
while True:
    c, addr = s.accept()
    f=open("esp8266-20191220-v1.12.bin", "r")
    print("got connection from",addr)
    while True:
        buf={}
        read_len=0
        for i in range (1, 9):
            buf[i]=f.read(512)
            read_len += len(buf[i])
            print("read_len1 ", read_len)
            c.send(buf[i])
            #if len(buf[i]) == 0:
            #    break
            print("read_len2 ", read_len)
            buf1=c.recv(512)

        if read_len < 4096:
            print("111111111 ")
            break

    f.close()
    c.close()
