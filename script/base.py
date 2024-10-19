import random
import time
from ascript.android.ui import Dialog
from ascript.android.node import Selector
from ascript.android.action import slide
from ascript.android import action
from ascript.android import screen
from ascript.android import system
from ascript.android.screen import FindColors
from ascript.android.ui import WebWindow
from ascript.android.system import R
from ascript.android.screen import CodeScanner
from ascript.android.screen import Ocr
import concurrent.futures
import threading
import time
import json
import re
from ascript.android.screen import FindImages
from .base_req import BaseReq
from .vpn import VpnBaseObj


class Base:
    def __init__(self):
        self.packageName = None
        self.changeAPI = "http://127.0.0.1:8766"
        self.reques = BaseReq()
        self.vpnBase = VpnBaseObj()
        pass

    def vpn_ip(self, deviceData):
        # 生成 5 到 8 位随机数字
        length = random.randint(5, 8)
        random_number = ''.join([str(random.randint(0, 9)) for _ in range(length)])
        # 拼接最终字符串
        username = f"kong005-res-{deviceData.country}-lsid-{random_number}"
        return username

    def chang_vpn_func_ip(self, deviceData):
        Dialog.toast("正在切换IP")
        # 无限循环，直到成功获取新IP
        while True:
            # 切换IP
            try:
                username = self.vpn_ip(deviceData)
                password = "Us2l8X40RWjtq1V"
                proxy = f"http://{username}:{password}@gw-zhuandian.ntnt.io:5959"
                vpnStatus = self.vpnBase.changeVpn_1(deviceData, username)
                print('vpnStatus====路过===>', vpnStatus)
                if vpnStatus:
                    new_ip = self.vpnBase.check_ip(proxy)
                    print('new_ip====路过===>', new_ip)
                    if new_ip != None:
                        if deviceData.task_type == 0 or deviceData.task_type == 9:
                            url = f'http://hwadmin.xiaotwo.cn/task/taskip?task_id={deviceData.task_id}&android_id={deviceData.deviceNum}&task_record_id={deviceData.task_record_id}&ip={new_ip}'
                            print('ip---url--->', url)
                            ipJson = self.reques.check_task_req(url)
                            ipCode = ipJson.get('code')
                            if ipCode == 1:
                                Dialog.toast("转化IP切换成功")
                                return new_ip  # IP切换成功，退出函数
                            else:
                                Dialog.toast("IP重复,重新切换IP")
                        else:
                            Dialog.toast("留存IP切换成功")
                            return new_ip  # IP切换成功，退出函数
                else:
                    Dialog.toast("IP切换失败,再次切换ip")
            except Exception as e:
                print(f'切换IP时发生异常: {str(e)}')
                continue
            time.sleep(5)

    # 清理所有后台
    def clean_backend(self):
        action.Key.recents()
        time.sleep(1)
        listViews = Selector().type("ListView").child().type("FrameLayout").find_all()
        print((listViews))
        if listViews != None:
            for view in listViews:
                print(view.desc)
                slide(500, 870, 500, 400)
                time.sleep(0.5)
        action.Key.home()
        time.sleep(3)

    # 改机
    def changeMachine(self, deviceData):
        time.sleep(1)
        system.open('com.gaiji.kiggaiji10')
        while True:
            ViewGroupFlag = Selector().packageName("com.gaiji.kiggaiji10").type("ViewGroup").find()
            button1 = Selector().id("android:id/button1").text("知道了").find()
            loginBtn = Selector().id("com.gaiji.kiggaiji10:id/login").find()
            print('ViewGroupFlag===>', ViewGroupFlag)
            if ViewGroupFlag != None:
                break
            else:
                time.sleep(2)
            if button1 is not None:
                button1.click()
            time.sleep(1)
            if loginBtn is not None:
                loginBtn.click()
        time.sleep(0.5)
        # 设置国家
        Dialog.toast('设置国家')
        url = self.changeAPI + "/do?type=Set_languag_zone&countries=" + deviceData.country
        self.reques.set_changeMachine(url)
        time.sleep(1)
        Dialog.toast('勾选APK')
        url = self.changeAPI + "/do?type=SetDestAppName&packagename=" + deviceData.packageName
        self.reques.set_changeMachine(url)
        time.sleep(1)
        Dialog.toast('刷新设备')
        url = self.changeAPI + "/do?type=Gaiji_go"
        deviceJson = self.reques.set_changeMachine(url)
        time.sleep(1)
        if '获取参数失败' in deviceJson.get('Msg'):
            print('改机失败')
            return None

        url = self.changeAPI + "/do?type=Set_Gaid"
        print('提前gaid-->', deviceData.gaid)
        data = {
            "gaid": deviceData.gaid
        }
        gaidData = self.reques.shell_user_post(url, data)
        print('gaid===>', gaidData)
        Gaid = gaidData.get('Data').get('gaid')
        if Gaid:
            print('Gaid=设置成功=>', Gaid)
            print('gaidDataJson--->', gaidData)
        return gaidData

    def check_package(self, deviceData):
        self.clean_backend()
        time.sleep(1)
        system.open('com.gaiji.kiggaiji10')
        while True:
            ViewGroupFlag = Selector().packageName("com.gaiji.kiggaiji10").type("ViewGroup").find()
            button1 = Selector().id("android:id/button1").text("知道了").find()
            loginBtn = Selector().id("com.gaiji.kiggaiji10:id/login").find()
            print('ViewGroupFlag===>', ViewGroupFlag)
            if ViewGroupFlag != None:
                break
            else:
                time.sleep(2)
            if button1 is not None:
                button1.click()
            time.sleep(1)
            if loginBtn is not None:
                loginBtn.click()
        time.sleep(0.5)
        url = self.changeAPI + "/do?type=SetDestAppName&packagename=" + deviceData.packageName
        json = self.reques.set_changeMachine(url)
        data = json.get('Data')
        print('data====>', data)

        '''注释判断应用存在的逻辑'''
        # if data:
        #     print(f'{deviceData.packageName}包名存在')
        #     Dialog.toast(f'{deviceData.packageName}包名存在')
        #     return True
        # else:
        #     print(f'{deviceData.packageName}包名不存在')
        #     Dialog.toast(f'{deviceData.packageName}包名不存在', 5000)
        #     return False

    def changeIp(self, deviceData):
        new_ip = self.chang_vpn_func_ip(deviceData)
        pass


    def run_base(self, deviceData):
        print("=========================run_base=========================")
        while True:
            self.clean_backend()
            self.packageName = deviceData.packageName
            '''改机'''
            gaidData = self.changeMachine(deviceData)
            print('返回---Gaid->', gaidData)
            if gaidData:
                break
        '''切换 ip'''
        new_ip = self.chang_vpn_func_ip(deviceData)

        phone_sdk = gaidData.get('Data').get('phone_sdk')
        deviceData.imei = gaidData.get('Data').get('imei')
        phone_brand = gaidData.get('Data').get('phone_brand')
        phone_id = gaidData.get('Data').get('phone_id')
        phone_model = gaidData.get('Data').get('phone_model')
        ''' 提交至后台看转化'''
        url = f'http://hwadmin.xiaotwo.cn/task/upphonedata?task_id={deviceData.task_id}&android_id={deviceData.deviceNum}&task_record_id={deviceData.task_record_id}&task_ip={new_ip}&phone_id={phone_id}&phone_brand={phone_brand}&phone_model={phone_model}&phone_sdk={phone_sdk}&retain_imei={deviceData.imei}'
        print('url===========>', url)
        remainJson = self.reques.check_task_req(url)
        remain_upload_status = remainJson.get('code')
        if remain_upload_status == 1:
            return True
        else:
            return False
        time.sleep(3)
