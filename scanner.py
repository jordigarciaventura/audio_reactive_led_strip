import requests
import socket
import re
import concurrent.futures

portal_name = "ledsname"

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 1))
ip = s.getsockname()[0]
network = re.findall(r"\d+\.\d+\.\d+", ip)[0]

devices = []
    
def ipcheck(local_ip):
  try:
    response = requests.get(f'http://{network}.{local_ip}/{portal_name}', timeout=3)
    if (response.status_code == 200):
      devices.append([f'{network}.{local_ip}', response.text])
  except Exception:
    pass

def ipchecker():
  with concurrent.futures.ThreadPoolExecutor(max_workers=255) as executor:
    executor.map(ipcheck, range(255))
    
ipchecker()
    
print(devices)