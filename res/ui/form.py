from airscript.system import R
from airscript.ui import Window
import json
def tunnel(k,v):
    if k =="close":
        print(v) # 用户点X关闭了窗口
    elif k =="res":
        print(v) # 用户点击确定并回传了数据
        resobj = json.loads(v)
        print(resobj)
        print('用户名',resobj['user'])
        print('分组选择框',resobj['select1'])
        print('单行选择框',resobj['select2'])
        print('开关',resobj['check'])
        print('单选',resobj['radio'])
        print('复选全部结果',resobj['mcheck'])
        print('复选第一个结果',resobj['mcheck'][0])

formw =  Window(R(__file__).ui("form.html"),tunnel)
formw.height("70vh")
formw.show()