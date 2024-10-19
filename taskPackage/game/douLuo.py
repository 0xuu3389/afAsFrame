import random
import time
from ascript.android.screen import Ocr
from ascript.android import action
import threading
from ascript.android.screen import FindColors
from ascript.android.system import R
from ascript.android.screen import FindImages
# 获取当前设备运行的APP信息
from ascript.android.system import Device
from ascript.android.ui import Dialog
# 隐藏悬浮窗
from ascript.android.ui import FloatWindow
from .network import Network

class Game_Operate:
    def __init__(self,deviceData):
        # 定义一个事件对象
        self.packagename = deviceData.packageName
        self.start_time = time.time()
        self.done_event = threading.Event()  # 用于停止线程的事件
        self.deviceData = deviceData
        self.playtime = deviceData.play_time
        self.taskStatus = True
        self.networkBase =Network()

    def check_normal_status(self):
        min_value, max_value = map(int, self.playtime.split(','))
        duration = random.randint(min_value,max_value)
        start_time = time.time()
        toast_interval = random.randint(5,15)
        req_interval = 250
        last_toast_time = 0  # 上一次显示toast的时间
        req_toast_time = 0
        maxTime = 0
        codeStatus = 0
        while not self.done_event.is_set():
            try:
                current_time = time.time()
                elapsed_time = current_time - start_time
                remaining_time = int(duration - elapsed_time)
                if elapsed_time >= duration:
                    print("游戏时间到，结束游戏。")
                    self.done_event.set()
                    break
                # 每次都会随机生成一个新的toast间隔
                if current_time - last_toast_time >= toast_interval:
                    Dialog.toast(f"还剩余 {remaining_time} 秒", 2000)
                    last_toast_time = current_time
                    toast_interval = random.randint(5,15)  # 重新生成新的随机间隔

                if current_time - req_toast_time >= req_interval:
                    print('达到所需时间')
                    req_toast_time = current_time
                    if maxTime < 3 and self.deviceData.task_type == 0:
                        url = f'http://hwadmin.xiaotwo.cn/task/getcallbackstatus?task_record_id={self.deviceData.task_record_id}&task_id={self.deviceData.task_id}&gaid={self.deviceData.gaid}&android_id={self.deviceData.deviceNum}'
                        resp = self.networkBase.check_task_req(url)
                        code = resp.get('code')
                        print('code===>',code)
                        if code == 0:
                            print('code============0',codeStatus)
                            if codeStatus == 2:
                                self.done_event.set()
                                self.taskStatus = False
                            codeStatus += 1
                        maxTime += 1
            except Exception as e:
                print(f"check_normal_status 出现异常: {e}")

    def game_task(self):
        while not self.done_event.is_set():
            try:
                print("Running game_task")

            except Exception as e:
                print(f"game_task 出现异常: {e}")

    def game_main(self):
        print('负责游戏任务')
        self.game_task()
        print('主线程任务结束')

    def run_game(self):
        FloatWindow.hide()
        time.sleep(0.5)
        """
        启动子线程和主线程
        """
        thread_targets = [
            (self.check_normal_status, ())
        ]
        # 启动子线程
        threads = []
        for task, args in thread_targets:
            t = threading.Thread(target=task, args=args)
            t.daemon = True  # 确保主线程结束时子线程也会退出
            t.start()
            threads.append(t)
        # 主线程执行
        self.game_main()  # 通知所有线程停止 ( self.done_event.set发出指令结束任务)
        time.sleep(random.randint(15,20))
        self.done_event.clear()
        print('游戏所有任务结束')
        return  self.taskStatus

