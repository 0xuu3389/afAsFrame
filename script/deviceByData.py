
class dataDeviceBy:

    def __init__(self, data):
        # 从 data 字典中获取相应的值，并赋给类属性
        self.task_id = data.get('task_id')
        self.deviceNum = data.get('deviceNum')
        self.name = data.get('name')
        self.packageName = data.get('packageName')
        self.url = data.get('url')
        self.apk_url = data.get('apk_url')
        self.gaid = data.get('gaid')
        self.apksize = data.get('apksize')
        self.gaid_type = data.get('gaid_type')
        self.overtime_time_max = data.get('overtime_time_max')
        self.play_time = data.get('play_time')
        self.country = data.get('bundle_nation')
        self.vpn_port = data.get('vpn_port')
        self.vpn_link = data.get('vpn_link')
        self.retain_type = data.get('retain_type')
        self.task_type = data.get('task_type')
        self.offerClickDelay = data.get('offerClickDelay')
        self.clickDownloadtimedelay = data.get('clickDownloadtimedelay')
        self.apkLunchstimedelay = data.get('apkLunchstimedelay')
        self.apkDownloadSucesstimedelay = data.get('apkDownloadSucesstimedelay')
        self.task_version = data.get('task_version')
        self.advertisement_num = data.get('advertisement_num')
        self.task_record_id = data.get('task_record_id')
        self.version = data.get('version')
        self.imei = None




