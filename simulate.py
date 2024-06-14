import requests
import time

# 初始值设定
i = 0

# Flask应用程序的地址
url = 'http://192.168.108.142:5000/data'

# 不停地发送POST请求
while True:
    # 模拟数据
    data = {
        'temperature': str(i),
        'humidity': str(i),
        'pm25': str(i)
    }
    
    # 发送POST请求
    response = requests.post(url, data=data)
    
    # 打印请求的结果
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")
    

    i += 1
    
    # 等待1秒再发送下一个请求
    time.sleep(1)
