import requests
from threading import *
import subprocess

import socket
import time

def extract_ip():
    st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        st.connect(('10.255.255.255', 1))
        IP = st.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        st.close()
    return IP

PORT = 80
list_ip = []

socket.setdefaulttimeout(0.01)

# def get_ip_addres_windows():
#     loc_ip = func_get_local_ip.extract_ip()
#     output = str(subprocess.check_output('arp -a'), 'CP866')
#     ip_loc_x_x_a_a = str(loc_ip.split('.')[0]) + '.' + str(loc_ip.split('.')[1])
#     output = output.split(loc_ip)[1]
#     Out = output.split(ip_loc_x_x_a_a)[1:]
#     oUt = []
#     for i in Out:
#         oUt.append(i.split(' ')[0])
#     Out.clear()
#     for i in oUt:
#         Out.append(ip_loc_x_x_a_a + i)
#     return Out

start_time = time.time()

def get_ip_addres_all_plat():
    loc_ip = extract_ip()
    ip_loc_x_x_x_a = str(loc_ip.split('.')[0]) + '.' + str(loc_ip.split('.')[1]) + '.' + str(loc_ip.split('.')[2])
    Out = []
    for ii in range(256):
        Out.append(ip_loc_x_x_x_a + '.' + str(ii))
    return Out

def connect(hostname, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        result = sock.connect_ex((hostname, port))
        if result == 0:
            # stderr.write(f"[{perf_counter() - start:.5f}] Found {hostname}\n")
            list_ip.append(hostname)

def find_dev(sort_p):
    list_ip_res=[]
    list_ip.clear()
    for i in get_ip_addres_all_plat():
        # print(i)
        connect(i, PORT)



    for i in list_ip:
        response = requests.get('http://'+i+'/test')
        if sort_p == str(response.content, 'utf8'):
            list_ip_res.append(i)

    return list_ip_res


if __name__ == '__main__':
    print( find_dev('its_ok'))

    print(time.time() - start_time)
