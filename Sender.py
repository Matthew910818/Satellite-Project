from flask import Flask, request
import requests
import json
import base64

app = Flask(__name__)

GITHUB_REPO = "Matthew910818/Satellite-Project"
GITHUB_TOKEN = "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"
FILE_PATH = "data.json"

@app.route('/data', methods=['POST'])
def receive_data():
    temperature = request.form['temperature']
    humidity = request.form['humidity']
    pm25 = request.form['pm25']

    data = {
        "temperature": temperature,
        "humidity": humidity,
        "pm25": pm25
    }

    # 將資料寫入 data.json 文件
    with open(FILE_PATH, 'w') as file:
        json.dump(data, file)

    # 上傳到 GitHub
    upload_to_github(data)

    return "Data received", 200

def upload_to_github(data):
    url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/{FILE_PATH}"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }

    # 讀取當前文件內容
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        sha = response.json().get('sha', '')
    else:
        sha = ""

    # 準備更新的內容
    content = base64.b64encode(json.dumps(data).encode()).decode()
    payload = {
        "message": "Update data.json",
        "content": content,
        "sha": sha
    }

    # 上傳文件到 GitHub
    response = requests.put(url, headers=headers, data=json.dumps(payload))
    if response.status_code == 200:
        print("File uploaded successfully")
    else:
        print("Failed to upload file", response.status_code, response.text)

if __name__ == '__main__':
   app.run(host='172.20.10.4', port=5000)
