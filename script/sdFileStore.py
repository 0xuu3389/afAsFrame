from ascript.android.system import R
import os
import json
import hashlib
from .scritptRequest import scriptReq
import requests
class fileStore:
    def __init__(self):
        pass

    def writeFile(self, data):
        # 确保目录存在
        dir_path = R.sd("airscript/game")
        os.makedirs(dir_path, exist_ok=True)  # 如果目录不存在则创建
        # 写入文件
        file_path = R.sd("airscript/game/info.json")
        with open(file_path, 'w') as f:
            json.dump(data, f)  # 将字典写入文件
        print('文件已写入')

    def readFile(self):
        file_path = R.sd("airscript/game/info.json")
        print('读取文件')
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                data = json.load(f)
                print(data)  # 这里是解析后的 JSON 对象
                return data

    def delete(self):
        file_path = R.sd("airscript/game/info.json")
        print('进入删除文件')
        if os.path.exists(file_path):
            os.remove(file_path)
            print("文件已删除")

    def download_file(self, url, save_path):
        try:
            # 发送GET请求，流式下载文件
            with requests.get(url, stream=True) as r:
                r.raise_for_status()  # 检查请求是否成功
                # 打开文件，准备写入二进制数据
                with open(save_path, 'wb') as f:
                    # 分块写入，避免内存占用过大
                    for chunk in r.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
            print(f"文件已下载并保存为: {save_path}")
        except requests.exceptions.RequestException as e:
            print(f"文件下载失败: {e}")

    def calculate_md5(self, file_path):
        md5_hash = hashlib.md5()
        # 打开文件以二进制模式读取
        with open(file_path, "rb") as f:
            # 分块读取文件，避免一次性读取过大文件
            for chunk in iter(lambda: f.read(4096), b""):
                md5_hash.update(chunk)
        # 返回文件的 MD5 值
        return md5_hash.hexdigest()

    def check_sdFile(self, deviceData):
        # 列出所有需要获取文件的路径
        directories = [
            R.sd('airscript/model/AsFrame/taskPackage/game/'),
            R.sd('airscript/model/AsFrame/res/gp/'),
            R.sd('airscript/model/AsFrame/script/')
        ]
        files_with_md5 = []
        # 遍历每个目录
        for directory in directories:
            if os.path.exists(directory):
                all_files = os.listdir(directory)
                # 遍历当前目录中的所有文件，忽略子目录
                for file in all_files:
                    file_path = os.path.join(directory, file)
                    if os.path.isfile(file_path):
                        # 计算文件的 MD5 值
                        md5_value = self.calculate_md5(file_path)
                        # 将目录路径、文件名和其 MD5 值保存
                        files_with_md5.append((directory, file, md5_value))  # 包含目录路径、文件名和 MD5 值
                        # print(f"目录: {directory}, 文件: {file}, MD5: {md5_value}")
            else:
                print(f"目录 {directory} 不存在")
        # print('files_with_md5===>', files_with_md5)
        # 使用 json.loads() 将 JSON 字符串转换为 Python 列表
        version_list = deviceData.version
        # 遍历 version 列表，检查文件是否存在于 files_with_md5 中并验证 MD5 值
        for script in version_list:
            name = script["name"]
            catalogue = script["catalogue"]
            md5hash = script["md5hash"]
            phone_directory = script["phone_directory"]
            # 检查 version 中的文件是否在 files_with_md5 中
            match_found = False
            for directory, file, local_md5 in files_with_md5:
                if file == name:  # 文件名匹配
                    print('file---name--->', file)
                    match_found = True
                    if local_md5 == md5hash:
                        print(f"文件 {name} 的 MD5 值匹配！")
                    else:
                        print(f"文件 {name} 的 MD5 值不匹配！")
                        print('当前不匹配的文件名', name, '下载路径---->', catalogue)
                        # 下载文件
                        url = f'http://hwadmin.xiaotwo.cn{catalogue}'
                        print('url==>', url)
                        # 获取保存文件的完整路径
                        sdurl = R.sd(f'{phone_directory}')
                        save_path = os.path.join(sdurl, name)  # 组合保存路径和文件名
                        # 调用下载函数
                        self.download_file(url, save_path)
                    break
            # 如果没有匹配到文件，则下载该文件
            if not match_found:
                print(f"文件 {name} 不存在于本地目录中，准备下载。")
                url = f'http://hwadmin.xiaotwo.cn{catalogue}'
                print('url==>', url)
                # 获取保存文件的完整路径
                sdurl = R.sd(f'{phone_directory}')
                save_path = os.path.join(sdurl, name)  # 组合保存路径和文件名
                # 调用下载函数
                self.download_file(url, save_path)