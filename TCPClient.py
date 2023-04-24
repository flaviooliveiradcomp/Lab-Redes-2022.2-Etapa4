import webbrowser
from socket import *

HOST = '127.0.0.1'
PORT = 12000
client = socket(AF_INET, SOCK_STREAM)
client.connect((HOST, PORT))

req = 'GET / HTTP/1.1\nHost: ' + HOST + '\n\n'
client.send(req.encode())
res = client.recv(4096).decode()

header, body = res.split('\n\n', 1)
if header.split()[1] == '200':
  with open('index.html', 'wb') as file:
    file.write(body.encode())
  webbrowser.open_new_tab('http://' + HOST + ':' + str(PORT))
else:
  print('ERROR')

client.close()