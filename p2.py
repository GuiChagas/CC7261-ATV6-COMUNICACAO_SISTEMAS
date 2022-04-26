import socket
import json

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind((socket.gethostname(), 50002))
  print(s)
  s.listen()
  while True:
    try:
      conexao, addr = s.accept()
      with conexao:
        print(f"Cliente conectado: {addr}")
        while True:
          dados = conexao.recv(1024)
          if not dados:
            break
          data = json.loads(dados.decode())

          if (int(data["codigo"]) > 10000000 and ((int(data["n"]) > 5000 and int(data["n"]) < 150000))):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sk:

              sk.connect(("192.168.0.27", 50003))
              sk.sendall(dados)
              dadosrv3 = sk.recv(1024)
              
            conexao.sendall(dadosrv3)
            
          else: 
            conexao.send(str.encode('O código inicial ou o n esta fora do range'))
    except KeyboardInterrupt:  
      s.close()  
      break
