from .scritptRequest import scriptReq

class configTask:
    def __init__(self):
        self.scriptReqBase = scriptReq()
        self.key = 'wwhkp6jgwhok' #工作室key
        pass
    def service_getConfig(self,deviceNum):
        print('--------service_getConfig----------')
        #http://58.56.44.30:9083/api/api/device/getDeviceByDeviceNum?deviceNum=50037&username=lv
        url = f'http://hwadmin.xiaotwo.cn/task/hwlist?android_id={deviceNum}&is_test=1&key={self.key}&model=&edition='
        print('url-->',url)
        response = self.scriptReqBase.check_task_req(url)
        print('response--->',response)
        return response



# http://hwadmin.xiaotwo.cn/task/hwlist?android_id=10001&is_test=1&key=wwhkp6jgwhok&model=&edition=





