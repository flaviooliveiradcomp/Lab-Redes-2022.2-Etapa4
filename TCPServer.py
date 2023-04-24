from socket import *
import os

PORT = 12000
server = socket(AF_INET, SOCK_STREAM)
server.bind(('', PORT))
server.listen(1)
print("READY")

while True:
  conn, addr = server.accept()
  req = conn.recv(1024).decode()
    
  if req.startswith('GET'):
    file_name = req.split()[1]
    if file_name == '/':
      file_name = '/index.html'
            
    if os.path.isfile('.' + file_name):
      file = open('.' + file_name, 'rb')
      res = file.read()
      file.close()
      header = 'HTTP/1.1 200 OK\nContent-Type: text/html\n\n'
    else:
      res = 'Arquivo não encontrado'.encode()
      header = 'HTTP/1.1 404 Not Found\nContent-Type: text/plain\n\n'
  else:
      res = 'Método não suportado'.encode()
      header = 'HTTP/1.1 405 Method Not Allowed\nContent-Type: text/plain\n\n'

  conn.send(header.encode() + res)
  conn.close()
