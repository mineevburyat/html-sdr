import socket
import numpy as np

fft_size = 1024
udp_data = None
UDP_IP = "127.0.0.1"
UDP_PORT = 2000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((UDP_IP, UDP_PORT))
sock.settimeout(0.5)

try:
    data, addr = sock.recvfrom(fft_size * 4)
    print(data)
    if len(data) == 4096:
        udp_data = np.frombuffer(data, dtype=np.float32)
        print(udp_data)
except socket.timeout:
    print('timeout')
    pass