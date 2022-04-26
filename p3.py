import socket
import json
from unicodedata import decimal
import sympy

    
def tCalculaPrimoPre(data, n):
    primos = 0
  
    while (primos != n):
        data = data - 1
        if sympy.isprime(data):
            primos = primos + 1

        if primos == n:
            return data


def tCalculaPrimoPos(data, n):
    primos = 0
  
    while (primos != n):
        data = data + 1
        if sympy.isprime(data):
            primos = primos + 1

        if primos == n:
            return data


def criaChave(data, n):
    return tCalculaPrimoPre(data, n) * tCalculaPrimoPos(data, n) 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind((socket.gethostname(), 50003))
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

                chave = str(criaChave(data["codigo"], data["n"]))

                conexao.send(str.encode(chave))
    except KeyboardInterrupt:
        s.close()
        break



