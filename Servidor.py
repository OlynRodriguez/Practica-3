import socket
import threading
import logging
import time
from main import *
from os import listdir
from os.path import isfile, join
bufferSize = 512
logging.basicConfig(level=logging.DEBUG,format='(%(threadName)-2s) %(message)s',)

def ls(ruta = 'archivos'):
    return [arch for arch in listdir(ruta) if isfile(join(ruta, arch))]


def ServidorPS(TCPServerSocket,main):
    print("servidor listo")
    try:
        while True:
            Client_conn=main.sConect(TCPServerSocket)
            thread_read = threading.Thread(name='Server', target=Atender, args=[Client_conn])
            thread_read.start()
    except Exception as e:
        print(e)

def Atender(conn):
     time.sleep(1)
     main.sLogin(conn)
     time.sleep(1)
     main.sDIR(conn)
     time.sleep(1)
     main.sSET(conn)
     time.sleep(1)
     main.sCLOSE(conn)

HOST ='192.168.0.6'
PORT =21
threading.current_thread().setName("Server")
main=protocoloFTP('admin','user')
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPServerSocket:
    TCPServerSocket.bind((HOST, PORT))
    TCPServerSocket.listen()
    print("El servidor está disponible y en espera de solicitudes")
    ServidorPS(TCPServerSocket,main)