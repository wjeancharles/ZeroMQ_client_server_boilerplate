import zmq
import time

port = "5556"
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.connect("tcp://localhost:%s" % port)

while True:
    msg = socket.recv()
    print(msg)
    socket.send_string("A message from CS361")
    time.sleep(1)
