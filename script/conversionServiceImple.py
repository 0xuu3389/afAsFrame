import json
import math
import random
import time
from ascript.android import system
from ascript.android.node import Selector
from ascript.android.ui import Dialog
import numpy as np
from .scritptRequest import scriptReq
from .base_req import BaseReq
from ascript.android import action
class converServiceImple:
    def __init__(self):
        self.scriptReqBase = scriptReq()
        self.reques = BaseReq()
        self.gaijiPack = 'com.gaiji.kiggaiji10'
        self.changeAPI = "http://127.0.0.1:8766"
        pass

    #请求web
    #http://58.56.44.30:9083/api//api/job/requestOfferUrl?clickReportId=15928107
    def service_requestOfferUrl(self,deviceData):
        shell_url = f'http://127.0.0.16:8766/do?type=Web'
        data = {"url": deviceData.url}
        response = self.scriptReqBase.shell_user_web(shell_url, data)
        if '正常' in response.get('Msg'):
            print('请求正常')
            wv_btn_close = Selector().id("com.gaiji.kiggaiji10:id/wv_btn_close").find()
            if wv_btn_close is not None:
                wv_btn_close.click()
            return True
        else:
            Dialog.toast('网络异常')
            return False
    #计算时间
    def wait_ctiTime(self,citiTime,packageName):
        start_time = time.time()
        duration = citiTime
        toast_interval = random.randint(5,10)
        last_toast_time = 0  # 上一次显示toast的时间
        while True:
            current_time = time.time()
            elapsed_time = current_time - start_time
            remaining_time = int(duration - elapsed_time)
            if elapsed_time >= duration:
                print("启动时间到")
                system.open(packageName)
                Dialog.toast("正在启动app")
                self.start_time = time.time()
                break
            # 每次都会随机生成一个新的toast间隔
            if current_time - last_toast_time >= toast_interval:
                Dialog.toast(f"还剩余ctit {remaining_time} 秒",2000)
                last_toast_time = current_time
                toast_interval = random.randint(5, 10)  # 重新生成新的随机间隔

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

    def open_gaiji(self):
        system.open(self.gaijiPack)
        while True:
            ViewGroupFlag = Selector().packageName("com.gaiji.kiggaiji10").type("ViewGroup").find()
            button1 = Selector().id("android:id/button1").text("知道了").find()
            loginBtn = Selector().id("com.gaiji.kiggaiji10:id/login").find()
            print('ViewGroupFlag===>', ViewGroupFlag)
            Pkage = Selector().packageName("com.gaiji.kiggaiji10").find()
            if Pkage is None:
                system.open(self.gaijiPack)
                time.sleep(2)
            if ViewGroupFlag != None:
                break
            else:
                time.sleep(2)
            if button1 is not None:
                button1.click()
            if loginBtn is not None:
                loginBtn.click()
    def services_back(self):
        while True:
            back_Url = 'http://127.0.0.1:8766/do?type=Back'
            respon = self.scriptReqBase.shell_user_get(back_Url)
            print('respon--->',respon)
            if '备份成功' in respon.get('Msg'):
                return 1
            else:
                self.clean_backend()
                self.open_gaiji()
            time.sleep(2)

    def services_killApp(self,package):
        self.open_gaiji()
        while True:
            killStatus = self.scriptReqBase.shell_user_kill(package)
            if killStatus:
                print('app已杀死')
                return
            else:
                self.clean_backend()
                self.open_gaiji()
            time.sleep(2)

    def secode_gaid(self,deviceData):
        url = self.changeAPI + "/do?type=Set_Gaid"
        data = {
                  "gaid": deviceData.gaid
                }
        gaidData = self.reques.shell_user_post(url,data)
        print('gaid===>',gaidData)
        Gaid = gaidData.get('Data').get('gaid')
        if Gaid:
            print('Gaid=设置成功=>',Gaid)
            deviceData.imei = gaidData.get('Data').get('imei')
            return True
        return False

    def services_backupsstatus(self,deviceData,status):
        url = f'http://hwadmin.xiaotwo.cn/task/backupsstatus?task_id={deviceData.task_id}&android_id={deviceData.deviceNum}&task_record_id={deviceData.task_record_id}&retain_imei={deviceData.imei}&backups_status={status}'
        resp = self.scriptReqBase.check_task_req(url)
        code = resp.get('code')
        return code

    def cal_ctit(self, offerClickDelay, clickDownloadtimedelay, apkLunchstimedelay, apkDownloadSucesstimedelay):
        print('--------cal_ctit---------')
        # 将每个字符串参数拆分并转换为整数，然后计算高斯分布的随机数
        params_list = [offerClickDelay, clickDownloadtimedelay, apkLunchstimedelay, apkDownloadSucesstimedelay]
        # 使用高斯分布函数计算每个参数，并求和
        results = [self.getRandomNum(*map(int, params.split(','))) for params in params_list]
        # 将每个计算的正态分布时间单独保存，并转换为毫秒
        offerClickDelay_time = results[0] * 1000  # Convert seconds to milliseconds
        clickDownloadtimedelay_time = results[1] * 1000
        apkLunchstimedelay_time = results[2] * 1000
        apkDownloadSucesstimedelay_time = results[3] * 1000

        url = 'http://127.0.0.1:8766/do?type=Set_ctit'
        data = {
            'offerClickDelay': offerClickDelay_time,
            'apkLunchstimedelay': clickDownloadtimedelay_time,
            'clickDownloadtimedelay': apkLunchstimedelay_time,
            'apkDownloadSucesstimedelay': apkDownloadSucesstimedelay_time
        }

        jsonData = self.scriptReqBase.shell_user_post(url, data)
        print('--jsonData----')
        # 设置改机时间(设置ctit成功)
        msg = jsonData.get('Msg')
        print('msg', msg)
        if '设置ctit成功' in msg:
            print('时间设置成功')
            # 返回它们的总和
            total_sum = sum(results)
            return total_sum
        return None

    # 检测随机数生成函数
    def getRandomNum(self, min_val, max_val):
        mu = (min_val + max_val) / 2
        sigma = (max_val - mu) / 3
        s = np.random.normal(mu, sigma, 1)[0]  # 直接获取数组中的第一个元素
        return round(s)  # 使用 round() 四舍五入并返回整数

















