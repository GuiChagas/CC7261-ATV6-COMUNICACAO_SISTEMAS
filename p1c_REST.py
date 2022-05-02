import http.client
import json
import random
import time

code = random.randint(10000000,20000000)
n = random.randint(5000,15000)

js = {"initialCode": code, "n": n}
jserialize = json.dumps(js)

conn = http.client.HTTPSConnection("8d55dd9d.us-south.apigw.appdomain.cloud")

params = str.encode(jserialize)

headers = {
    'content-type': "application/json",
    'accept': "application/json"
    }

conn.request("POST", "/testp/key", params, headers)
start = time.time()

res = conn.getresponse()
data = res.read()
end = time.time()

print(f'CODIGO INICIAL == {js["initialCode"]}')
print(f'N == {js["n"]}')
print(f'TIME == {(end-start)}')
print(data.decode("utf-8"))