import pickle
import socket
import numpy as np

model = pickle.load(open('rf_classifier.pickle', 'rb'))
TCP_IP = '169.254.74.41'  # this IP of my pc. When I want raspberry pi 2`s as a server, I replace it with its IP '169.254.54.195'
TCP_PORT = 5005
BUFFER_SIZE = 1024 # Normally 1024, but I want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print ('Connection address:', addr)
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    Input = np.fromstring(data, dtype=float, count = -1, sep=' ')
    res = model.predict(np.array([Input]))
    print ("received data:", Input)
    print ("prediction:", res)
    conn.send(data)  # echo
conn.close()



