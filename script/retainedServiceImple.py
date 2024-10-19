import json
import time
from ascript.android.node import Selector
from ascript.android import action
from .scritptRequest import scriptReq
from ascript.android import system
class retainServiceImple:
    def __init__(self):
        self.key = '7z85z5a89mrq'
        self.scriptReqBase = scriptReq()
        self.gaijiPack = 'com.gaiji.kiggaiji10'
        pass

    # 获取设备启动配置
    def service_remaincallback(self,retain_data):
        url = f'http://hwadmin.xiaotwo.cn/task/remaincallback?retain_record_id={retain_data.retain_record_id}&gaid={retain_data.gaid}&android_id={retain_data.deviceNum}&task_id={retain_data.task_id}'
        print('留存任务上报===>',url)
        resp = self.scriptReqBase.check_task_req(url)
        code = resp.get('code')
        if code == 1:
            print('留存上传成功')
            return True
        return False

    #kig获取备份列表
    def service_getBackupList(self,retain_data):
        self.open_gaiji()
        url = f'http://127.0.0.1:8766/do?type=GetAppBackList&packagename={retain_data.packageName}'
        resp = self.scriptReqBase.shell_user_get(url)
        print('resp=>',resp)
        return resp

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

    def services_killApp(self,retain_data):
        self.open_gaiji()
        while True:
            killStatus = self.scriptReqBase.shell_user_kill(retain_data.packageName)
            if killStatus:
                print('app已杀死')
                return
            else:
                self.clean_backend()
                self.open_gaiji()
            time.sleep(2)

    #还原备份
    def service_restoreBackup(self,retain_data):
        url = f'http://127.0.0.1:8766/do?type=Up&backname={retain_data.retain_imei}&packagename={retain_data.packageName}'
        print('backUrl===>',url)
        resp = self.scriptReqBase.shell_user_get(url)
        print('resp=>',resp)
        if '还原完成' in resp.get('Msg'):
            print('还原成功')
            system.open(retain_data.packageName)
            time.sleep(1)
            return True
        return False
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

    #留存备份状态
    #http://hwadmin.xiaotwo.cn/task/retainbackupsstatus?retain_record_id=16044&gaid=8966a0d7-d426-4e6c-aaa4-1f3967405aab&android_id=50051&task_id=16018&backups_status=1
    def services_backupsstatus(self,retain_data,status):
        url = f'http://hwadmin.xiaotwo.cn/task/retainbackupsstatus?retain_record_id={retain_data.retain_record_id}&gaid={retain_data.gaid}&android_id={retain_data.deviceNum}&task_id={retain_data.task_id}&backups_status={status}'
        print('留存备份状态url===>',url)
        resp = self.scriptReqBase.check_task_req(url)
        code = resp.get('code')
        return code

    #kig删除备份
    def service_delBackup(self,retain_data):
        url = f'http://127.0.0.16:8766/do?type=DelBack'
        retain_del = retain_data.retain_del
        print('retain_del==>',type(retain_del))
        print('retain_del==>',retain_del)
        if retain_del:
            print('备份不为空')
            for back_del in retain_del:
                if back_del:
                    print('back_del备份删除',back_del)
                    data = {
                        "packagename": retain_data.packageName,
                        "backname": back_del
                    }
                    print('data==>',data)
                    resp = self.scriptReqBase.shell_user_post(url, data)
                    print('Response=>', resp)
                    time.sleep(2)
            # 上报删除备份
            report_url = f"http://hwadmin.xiaotwo.cn/task/remainimeidel?task_id={retain_data.task_id}&android_id={retain_data.deviceNum}&retain_del={json.dumps(retain_del)}"
            print('Report URL===>', report_url)
            resp = self.scriptReqBase.check_task_req(report_url)
            code = resp.get('code')
            print('IMEI DelBackup Code-->', code)
            return code

    def imie_delBackup(self,retain_data):
        retain_del = []
        retain_del.append(retain_data.retain_imei)
        print('retain_del====>',retain_del)
        # 转换为 JSON 字符串
        retain_del_str = json.dumps(retain_del)
        url = f'http://hwadmin.xiaotwo.cn/task/remainimeidel?task_id={retain_data.task_id}&android_id={retain_data.deviceNum}&retain_del={retain_del_str}'
        print('url====>',url)
        resp = self.scriptReqBase.check_task_req(url)
        code = resp.get('code')
        print('imie_delBackup--code-->',code)
        return code






