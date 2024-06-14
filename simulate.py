import requests
import time

# 模擬數據
data_template = {
    'temperature': '10',
    'humidity': '60',
    'pm25': '35'
}

# Flask應用程序的地址
url = 'http://192.168.105.226:5000/data'

# 不停地發送POST請求
while True:
    # 發送POST請求
    response = requests.post(url, data=data_template)
    
    # 打印請求的結果
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")
    
    # 等待1秒再發送下一個請求
    time.sleep(1)
