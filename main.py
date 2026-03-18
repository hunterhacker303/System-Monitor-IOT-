import psutil
import requests
import time

ESP32_IP = "http://10.202.196.31/data"  

while True:
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent





    # making dis for sending data to esp 32 in  Json formate 
    data = {
        "cpu": cpu,
        "ram": ram,
        "disk": disk
    }
    

    # exception handling for avoiding code breaking 

    
    try:
        response = requests.post(ESP32_IP, json=data)
        print("Sent:", data)
    except Exception as e:
        print("Error:", e)

    time.sleep(2)