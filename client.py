# client.py
import socket

s = socket.socket()
host="192.168.20.25"
port = 8080

s.connect((host, port))
f=open("test1.bin", "w")
while True:
  read_len=0
  buf={}
  buf2=bytes()
  print("2222222222 ")
  for i in range (1, 9):
    buf[i]=s.recv(512)
    read_len += len(buf[i])
    if len(buf[i]) == 0:
        break
    print("read_len1 ", read_len)
    s.send(buf[i])
    print("read_len2 ", read_len)

  for j in range (1, i+1):
    buf2 += buf[j]

  f.write(buf2)

  if read_len < 4096:
     print("111111111 ")
     break

f.close()
s.close()
