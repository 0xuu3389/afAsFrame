import os
import importlib
from .game.douLuo import Game_Operate
class Task_Alloc:
    def __init__(self):
        pass

    def task_excut(self,deviceData):
        package = deviceData.packageName.replace('.', '')
        print('package===>', package)
        # 动态导入模块
        obj = Game_Operate(deviceData)
        res = obj.run_game()
        return res


