import socket
import json
import random
import time
import matplotlib.pyplot as plt
import numpy as np


total_time = 0

unique_executions_times = []
total_executions_times = []
num_max_fexecution = []
number_exec = int(input('Quantas execuções deseja fazer: '))

for x in range(number_exec):
  total_time_mark = 0
  time_mark = False
  for i in range(15):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      start = time.time()
      s.connect(("192.168.0.27", 50002))
      unique_start = time.time()

      code = random.randint(10000000,20000000)
      n = random.randint(5000,15000)
      
      js = {"codigo": code, "n": n}
      jserialize = json.dumps(js)
      
      s.send(str.encode(jserialize))
      dados = s.recv(1024)
      unique_end = time.time()
      keytime = unique_end - unique_start
      unique_executions_times.append(keytime)
      
      print("================================================================================")
      print(f'Codigo Inicial: {js["codigo"]}')
      print(f'N: {js["n"]}')
      print(f"Resposta do servidor chave única {i+1}: {dados.decode()}")
      print(f"Tempo de resposta {i+1}: {keytime}")

      end = time.time()
      total_time_mark = total_time_mark + keytime
      total_time = total_time + (end-start)

      if(total_time_mark >= 5 and not time_mark):

          print("===========================")
          print("5 seconds Limit.")
          print(f"Max. de execuções {i}")
          print(f"Tempo de execução {total_time_mark}")
          num_max_fexecution.append(i)
          time_mark = True
  total_executions_times.append(total_time_mark)
  print(f'')
  print(f'Desvio padrão baseado no tempo de execução de cada key: {np.std(unique_executions_times)}')
  print(f'Média baseada no tempo de execução de cada key: {np.mean(unique_executions_times)}')

# print(f'TotalTime: {total_time}')
# print(f'TotalExecution: {number_exec}')
# print(f'NumberTotal: {num_max_fexecution}')
# print(f'ExecutionUniqueTime: {unique_executions_times}')
# print(f'TotalExecutionall: {total_executions_times}')
# print(np.arange(0, number_exec), total_time)
# plt.plot(total_executions_times, num_max_fexecution)
# plt.show()