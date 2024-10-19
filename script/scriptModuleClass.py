import json
import random
import time
from ..taskPackage.transferTask import Task_Alloc
from .conversionServiceImple import converServiceImple
from .retainedServiceImple import retainServiceImple
from .configTask import configTask
from .base import Base
from ascript.android.ui import Dialog
from .deviceByData import dataDeviceBy
from .retainedClass import reTainedClazz
from ascript.android.ui import WebWindow
from ascript.android.system import R
from .sdFileStore import fileStore
# 隐藏悬浮窗
from ascript.android.ui import FloatWindow


class moduleClass:
    def __init__(self):
        self.converServiceImpleBase = converServiceImple()
        self.configTask = configTask()
        self.retainBase = retainServiceImple()
        self.base = Base()
        self.task_base = Task_Alloc()
        self.fileBase = fileStore()
        self.last_request_time = time.time()  # 初始化为当前时间
        self.last_toast_time = self.last_request_time
        self.toast_interval = random.randint(5, 15)  # 随机生成初始toast间隔
        self.wait_time = 0  # 初始等待时间为0秒
        self.max_wait_time = 180  # 最大等待时间为3分钟（180秒）

    def tunnel(self, k, v):
        if k == "close":
            print(v)  # 用户点X关闭了窗口
        elif k == "res":
            print(v)  # 用户点击确定并回传了数据
            resobj = json.loads(v)
            print(resobj)
            deviceNum = resobj['userIp']
            print('deviceNum=========>', deviceNum)
            self.configTask_modele(deviceNum)

    def init_page(self):
        print("初始化界面")
        formw = WebWindow(R.ui('form.html'), self.tunnel)
        formw.gravity(1 | 1)
        formw.show()

    # 配置任务信息
    def configTask_modele(self, deviceNum):
        print('执行任务')
        # while True:
        try:
            response = self.fileBase.readFile()
            if response is not None:
                print('获取Sd文件信息')
                task_type = response.get('taskList').get('task_type')
                print('task_type=====>', task_type)
                if task_type == 0:
                    deviceData = dataDeviceBy(response.get('taskList'))
                    print('正常任务')
                    self.second_conversion_modele(deviceData)
                elif task_type == 1:
                    retain_data = reTainedClazz(response.get('taskList'))
                    print('留存任务')
                    self.Retained_modele(retain_data)
                elif task_type == 5:
                    print('重启手机')
                elif task_type == 9:
                    print('点击任务')
                    deviceData = dataDeviceBy(response.get('taskList'))
                    self.Click_task(deviceData)
            else:
                current_time = time.time()
                # 计算距离下次请求的剩余时间
                elapsed_time = current_time - self.last_request_time
                remaining_time = int(max(0, self.wait_time - elapsed_time))  # 强制转换为整数
                # 请求逻辑
                if elapsed_time >= self.wait_time:
                    print('获取服务器文件信息')
                    response = self.configTask.service_getConfig(deviceNum)
                    resCode = response.get('code')
                    if resCode == 1:
                        task_type = response.get('taskList').get('task_type')
                        if response is not None:
                            print('task_type=====>', task_type)
                            if task_type == 0:
                                deviceData = dataDeviceBy(response.get('taskList'))
                                print('正常任务')
                                self.conversion_modele(deviceData, response)
                            elif task_type == 1:
                                print('留存任务')
                                self.fileBase.writeFile(response)
                                retain_data = reTainedClazz(response.get('taskList'))
                                self.Retained_modele(retain_data)
                            elif task_type == 5:
                                print('重启手机')
                            elif task_type == 9:
                                # print('点击任务')
                                self.fileBase.writeFile(response)
                                deviceData = dataDeviceBy(response.get('taskList'))
                                self.Click_task(deviceData)

                    else:
                        Dialog.toast("获取任务失败", 2000)
                        self.wait_time = min(self.wait_time + 60, self.max_wait_time)  # 增加等待时间，但不超过最大值
                    self.last_request_time = current_time  # 更新上次请求时间
                # 每次都会随机生成一个新的toast间隔
                if current_time - self.last_toast_time >= self.toast_interval:
                    Dialog.toast(f"还剩余 {remaining_time} 秒开始请求任务", 2000)
                    self.last_toast_time = current_time
                    self.toast_interval = random.randint(5, 15)  # 重新生成新的随机间隔
            FloatWindow.show()
            # time.sleep(random.randint(5, 10))
            time.sleep(30)
        except Exception as e:
            print(f"configTask_modele 出现异常: {e}")

    # 转化模块
    def conversion_modele(self, deviceData, response):
        self.fileBase.check_sdFile(deviceData)
        Dialog.toast("更新脚本完成")
        # packStatus = self.base.check_package(deviceData)
        self.base.check_package(deviceData)
        # if not packStatus:
        #     return
        # isSuccess = self.base.run_base(deviceData)
        self.base.run_base(deviceData)
        '''注释后面请求点击连接相关的代码'''
        # if isSuccess:
        #     print('----计算时间--')
        #     # 计算正态分布
        #     # 总体时间
        #     total_ctit_sumTime = self.converServiceImpleBase.cal_ctit(deviceData.offerClickDelay,deviceData.clickDownloadtimedelay,deviceData.apkLunchstimedelay,deviceData.apkDownloadSucesstimedelay)
        #     print('total_ctit_sumTime===>',total_ctit_sumTime)
        ''' 请求 offer（点击连接）'''
        #     # 请求web
        #     webExecppt = self.converServiceImpleBase.service_requestOfferUrl(deviceData)
        #     if webExecppt:
        #         self.fileBase.writeFile(response)
        #         if total_ctit_sumTime is not None:
        #             print('----total_ctit_sumTime--------')
        '''
        等待一段时间后自动打开APP
        '''
        #             self.converServiceImpleBase.wait_ctiTime(total_ctit_sumTime,deviceData.packageName)
        #             #加载脚本 返回是否转化
        '''
        task_excut: 对目标APP操作的具体流程
        '''
        #             respStatus = self.task_base.task_excut(deviceData)
        #             self.converServiceImpleBase.services_killApp(deviceData.packageName)
        #             if respStatus:
        #                 # 备份
        #                 if deviceData.retain_type == 1:
        #                     backStatus = self.converServiceImpleBase.services_back()
        #                     #上传备份状态
        #                     #http://hwadmin.xiaotwo.cn/task/backupsstatus?task_id=16015&android_id=a2&task_record_id=649&retain_imei=4444&backups_status=1
        #                     self.converServiceImpleBase.services_backupsstatus(deviceData,backStatus)
        #                     time.sleep(1)
        #                     self.fileBase.delete()
        #             else:
        #                 self.fileBase.delete()
        #     else:
        #         self.fileBase.delete()
        #         self.base.clean_backend()
        time.sleep(2)

    def second_conversion_modele(self, deviceData):
        self.fileBase.check_sdFile(deviceData)
        Dialog.toast("更新脚本完成")
        # 加载脚本
        respStatus = self.task_base.task_excut(deviceData)
        self.converServiceImpleBase.services_killApp(deviceData.packageName)
        if respStatus:
            # 备份
            if deviceData.retain_type == 1:
                backStatus = self.converServiceImpleBase.services_back()
                gaidStatus = self.converServiceImpleBase.secode_gaid(deviceData)
                if gaidStatus:
                    print('gaid设置状态正常')
                    # 上传备份状态
                    # http://hwadmin.xiaotwo.cn/task/backupsstatus?task_id=16015&android_id=a2&task_record_id=649&retain_imei=4444&backups_status=1
                    self.converServiceImpleBase.services_backupsstatus(deviceData, backStatus)
                    time.sleep(1)
                    self.fileBase.delete()
        else:
            self.fileBase.delete()

    # 留存模块
    def Retained_modele(self, retain_data):
        print('留存模块')
        self.fileBase.check_sdFile(retain_data)
        Dialog.toast("更新脚本完成")
        self.base.changeIp(retain_data)
        # 删除留存
        data_list = self.retainBase.service_getBackupList(retain_data)
        data = data_list.get('Data')
        if data is not None:
            # 提取所有字典中的 m_imei
            imei_list = [item['m_imei'] for item in data]
            print('imei_list===>', imei_list)
            print('retain_imei======>', retain_data.retain_imei)
            if retain_data.retain_imei in imei_list:
                print('存在')
                # 还原备份
                code = self.retainBase.service_restoreBackup(retain_data)
                if code:
                    runStatus = self.task_base.task_excut(retain_data)
                    if runStatus:
                        self.retainBase.services_killApp(retain_data)
                        uploadStatus = self.retainBase.service_remaincallback(retain_data)
                        print('uploadStatus===>上报成功')
                        time.sleep(1)
                        backStatus = self.retainBase.services_back()
                        # 上报备份状态
                        upstatus = self.retainBase.services_backupsstatus(retain_data, backStatus)
                        print('上报备份状态==>', upstatus)
                        time.sleep(1)
                        self.fileBase.delete()
                        self.retainBase.service_delBackup(retain_data)
            else:
                print('不存在')
                self.fileBase.delete()
                self.retainBase.service_delBackup(retain_data)
                self.retainBase.imie_delBackup(retain_data)
        time.sleep(2)

    def Click_task(self, deviceData):
        self.fileBase.check_sdFile(deviceData)
        Dialog.toast("更新脚本完成")
        packStatus = self.base.check_package(deviceData)
        # if not packStatus:
        #     return
        self.base.check_package(deviceData)
        isSuccess = self.base.run_base(deviceData)
        # if isSuccess:
        #     print('----计算时间--')
        #     # 计算正态分布
        #     # 请求web
        #     webStatus = self.converServiceImpleBase.service_requestOfferUrl(deviceData)
        #     if webStatus:
        #         print('webStatus==>', '点击正常')
        #         time.sleep(1)
        #         self.fileBase.delete()
