import requests
import time

i = 0

# Flask地址
url = 'http://172.20.10.4:5000/data'

# 發出POST請求
while True:
    data = {
        'temperature': str(i),
        'humidity': str(i),
        'pm25': str(i)
    }
    
    response = requests.post(url, data=data)
    
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")
    

    i += 1
    
    time.sleep(1)
