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

threading.current_thread().setName("Cliente")
HOST = '192.168.0.6'
PORT = 21
bufferSize = 1024
password='admin'
user='user'
main=protocoloFTP()
TCPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
main.cConect(TCPClientSocket,HOST,PORT)
time.sleep(1)
main.cLogin(TCPClientSocket,user,password)
time.sleep(1)
main.cDIR(TCPClientSocket)
time.sleep(1)
main.cSET(TCPClientSocket)
time.sleep(1)
main.cCLOSE(TCPClientSocket)