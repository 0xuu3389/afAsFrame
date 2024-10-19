import time

import requests

class BaseReq:
    def __init__(self):
        self.shellUrl = 'http://127.0.0.1:8766/do?type=Shell'
        pass

    def set_changeMachine(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            # 打印响应内容
            presjson = response.json()
            print('presjson==>',presjson)
            return  presjson
        except requests.exceptions.RequestException as e:
            print('网络异常:', e)

    def check_ip(self):
        print('wait.....')
        try:
            response = requests.get('https://ipinfo.ipidea.io', timeout=5)
            resjson = response.json()
            print('ip检测结果==>',resjson)
            return resjson['ip']
        except requests.exceptions.RequestException as e:
            print('ip异常需要切换', str(e))
            return None

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
    def shell_user_post(self,url,data):
        try:
            # 设置请求头
            headers = {
                'Content-Type': 'application/json'
            }
            # 发送POST请求
            response = requests.post(url=url, headers=headers, json=data)
            # 打印响应内容
            presjson = response.json()
            return presjson
        except requests.exceptions.RequestException as e:
            # 捕获并处理网络请求中的异常
            print('网络异常:', e)

    def changeIpFunc(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            response.encoding = response.apparent_encoding  # Set correct encoding
            print(response.text)
            return response.text
        except requests.exceptions.RequestException as e:
            print('网络异常:', e)
            return False


    def shell_user_rotation(self, flag):
        try:
            # 根据flag的值设置rotation_value
            rotation_value = '1' if flag else '0'
            # 设置请求头
            headers = {
                'Content-Type': 'application/json'
            }
            # 构建要发送的JSON payload
            data = {
                'shell': f'settings put system user_rotation {rotation_value}',
                'is_root': False
            }
            # 发送POST请求
            response = requests.post(url=self.shellUrl, headers=headers, json=data)
            # 打印响应内容
            print(response.text)
        except requests.exceptions.RequestException as e:
            # 捕获并处理网络请求中的异常
            print('网络异常:', e)
