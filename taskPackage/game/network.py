import time
import requests
from ascript.android import system

class Network:
    def __init__(self):
        self.shellUrl = 'http://127.0.0.1:8766/do?type=Shell'
        self.pack = 'com.gaiji.kiggaiji10'
        pass


    def check_task_req(self, url):
        while True:
            try:
                response = requests.get(url, timeout=10)
                response.raise_for_status()  # 检查请求是否成功
                resjson = response.json()  # 解析 JSON 数据
                print('任务检测结果==>', resjson)
                return resjson
            except requests.exceptions.RequestException as e:
                print(f'请求异常: {e}')
                print('等待 5 秒后重试...')
                time.sleep(5)  # 等待 5 秒后重试


    def shell_user_rotation(self,packageName):
        try:
            # 设置请求头
            headers = {
                'Content-Type': 'application/json'
            }
            # 构建要发送的JSON payload
            data = {
                'shell': f'am force-stop {packageName}',
                'is_root': False
            }
            # 发送POST请求
            response = requests.post(url=self.shellUrl, headers=headers, json=data)
            # 打印响应内容
            print(response.text)
        except requests.exceptions.RequestException as e:
            # 捕获并处理网络请求中的异常
            print('网络异常:', e)
            system.open(self.pack)
            time.sleep(3)



