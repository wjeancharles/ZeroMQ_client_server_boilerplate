import zmq
import time

port = "5556"
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind("tcp://*:%s" % port)

while True:
    socket.send_string("A message from CS361")
    msg = socket.recv()
    print(msg)
    time.sleep(1)
