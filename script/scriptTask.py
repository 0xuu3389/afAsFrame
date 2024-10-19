import random
import threading
import time
from .scriptModuleClass import moduleClass


class TaskClass:
    def __init__(self):
        self.done_event = threading.Event()  # 用于停止线程的事件
        self.moduleClassBase = moduleClass()
        pass

    def check_background_task(self):
        while not self.done_event.is_set():
            try:
                # print("Running check_background_task")
                # self.moduleClassBase.service_check_background()
                print('ok')
            except Exception as e:
                print(f"check_background_task 出现异常: {e}")

    def script_Maintask(self):
        print('程序结束')
        try:
            self.moduleClassBase.init_page()
            # self.moduleClassBase.configTask_modele()
            # self.moduleClassBase.Retained_modele()
        except Exception as e:
            print(f"script_Maintask 出现异常: {e}")
        pass

    def test_task(self):
        self.script_Maintask()


    def runTask(self):
        # while True:
            print('执行中')
            """
            启动子线程和主线程
            """
            thread_targets = [
                (self.check_background_task, ()),
            ]
            # 启动子线程
            threads = []
            for task, args in thread_targets:
                t = threading.Thread(target=task, args=args)
                t.daemon = True  # 确保主线程结束时子线程也会退出
                t.start()
                threads.append(t)

            # 主线程执行
            self.script_Maintask()
            # 通知所有线程停止
            # self.done_event.clear()
            # 通知所有线程停止 ( self.done_event.set发出指令结束任务)

            # time.sleep(random.randint(60, 100))

    # 访问安卓系统 API
    # def get_free_space(self):
    #     # 获取系统存储路径
    #     storage_path = "/sdcard"
    #     stat = android.os.StatFs(storage_path)
    #
    #     # 获取块大小和可用块数
    #     block_size = stat.getBlockSizeLong()
    #     available_blocks = stat.getAvailableBlocksLong()
    #
    #     # 计算剩余空间
    #     free_space = available_blocks * block_size
    #     return free_space
    #
    # # 将字节转换为GB
    # free_space_gb = get_free_space() / (1024 * 1024 * 1024)
    # print(f"剩余存储空间: {free_space_gb:.2f} GB")




taskObj = TaskClass()
taskObj.test_task()



