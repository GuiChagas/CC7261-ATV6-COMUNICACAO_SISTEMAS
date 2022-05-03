import http.client
import json
import random
import time
from threading import Thread
import asyncio


def validatorProcess(initialCode, n):
    conn = http.client.HTTPSConnection("8d55dd9d.us-south.apigw.appdomain.cloud")
    headers = {'content-type': "application/json"}

    # js = {"initialCode": 16966723, "n": 13576}
    js = {"initialCode": initialCode, "n": n}

    params = str.encode(json.dumps(js))

    conn.request("POST", "/validator/key", params, headers)

    res = conn.getresponse()
    data = res.read()
    dados = json.loads(data.decode())

    return dados

def generatorKeyProcess(initialCode, n):

    if validatorProcess(initialCode, n):
        conn = http.client.HTTPSConnection("8d55dd9d.us-south.apigw.appdomain.cloud")
        headers = {'content-type': "application/json"}
        
        # js = {"initialCode": 16966723, "n": 13576}
        js = {"initialCode": initialCode, "n": n}
        params = str.encode(json.dumps(js))

        conn.request("POST", "/testp/key", params, headers)
        start = time.time()

        res = conn.getresponse()
        data = res.read()
        end = time.time()

        print(f'CODIGO INICIAL == {js["initialCode"]}')
        print(f'N == {js["n"]}')
        print(f'TIME == {(end-start)}')
        dados = json.loads(data.decode())

        print(dados["message"])
    else:
        print("invalido")

def main():
    all_time = []
    threads = []

    start = time.time()
    for i in range(20):

        code = random.randint(10000000,20000000)
        n = random.randint(5000,15000)

        t = Thread(target=generatorKeyProcess, args=(code, n))
        threads.append(t)
        t.start()

        print(".")
            
    for thread in threads:
        thread.join()

    
    end = time.time()
    print(f'TIME TOTAL == {(end-start)}')
main()    