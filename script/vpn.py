import random
import time
import requests
from ascript.android.screen import Ocr
from ascript.android.node import Selector
from ascript.android import action
import threading
from ascript.android import system
from ascript.android.screen import FindColors
from ascript.android.system import R
from ascript.android.screen import FindImages
from ascript.android.action import slide
# 获取当前设备运行的APP信息
from ascript.android.system import Device
# 包
from ascript.android import media
# 隐藏悬浮窗
from ascript.android.ui import FloatWindow
from ascript.android.ui import Dialog

class VpnBaseObj:
    def __init__(self):
        self.gaijiPack = 'com.gaiji.kiggaiji10'
        pass

    def changeVpn_1(self,deviceData,username):
        print('打开vpn')
        system.open('moe.nb4a')
        time.sleep(2)

        # add
        YesBtn = Selector().id("android:id/button1").find()
        if YesBtn is not None:
            YesBtn.click()
            time.sleep(0.5)
        action_add = Selector().id("moe.nb4a:id/action_add").find()
        if action_add is not None:
            action_add.click()
            time.sleep(0.5)
        ManualSetting = Selector(2).packageName("moe.nb4a").type("ListView").child(4).find()
        if ManualSetting is not None:
            ManualSetting.click()
            time.sleep(0.5)
        SOCKSBtn = Selector().id("moe.nb4a:id/title").text("SOCKS").parent(1).find()
        if SOCKSBtn is not None:
            SOCKSBtn.click()
            time.sleep(0.5)
        ServerBtn = Selector(2).id("moe.nb4a:id/recycler_view").type("RecyclerView").child(4).find()
        if ServerBtn is not None:
            ServerBtn.click()
            time.sleep(0.5)

        editServer = Selector().id("android:id/edit").click().input("gw-zhuandian.ntnt.io").find()
        time.sleep(1)
        OKBtn = Selector(2).id("moe.nb4a:id/buttonPanel").type("ScrollView").child(2).find()
        if OKBtn is not None:
            OKBtn.click()
            time.sleep(0.5)

        PortBtn = Selector(2).id("moe.nb4a:id/recycler_view").type("RecyclerView").child(5).find()
        if PortBtn is not None:
            PortBtn.click()
            time.sleep(0.5)

        Selector().id("android:id/edit").click().input("9595").find()
        time.sleep(1)
        OKBtn = Selector(2).id("moe.nb4a:id/buttonPanel").type("ScrollView").child(2).find()
        if OKBtn is not None:
            OKBtn.click()
            time.sleep(0.5)

        userNameSet = Selector(2).id("moe.nb4a:id/recycler_view").type("RecyclerView").child(6).find()
        if userNameSet is not None:
            userNameSet.click()
            time.sleep(0.5)
        # 拼接最终字符串
        Selector().id("android:id/edit").click().input(username).find()
        time.sleep(1)
        OKBtn = Selector(2).id("moe.nb4a:id/buttonPanel").type("ScrollView").child(2).find()
        if OKBtn is not None:
            OKBtn.click()
            time.sleep(0.5)
        time.sleep(1)

        Password = Selector(2).id("moe.nb4a:id/recycler_view").type("RecyclerView").child(7).find()
        if Password is not None:
            Password.click()
            time.sleep(0.5)

        Selector().id("android:id/edit").click().input('Us2l8X40RWjtq1V').find()
        time.sleep(1)
        OKBtn = Selector(2).id("moe.nb4a:id/buttonPanel").type("ScrollView").child(2).find()
        if OKBtn is not None:
            OKBtn.click()
            time.sleep(0.5)

        time.sleep(2)
        ApplyBtn = Selector(2).type("FrameLayout").child(4).find()
        if ApplyBtn is not None:
            ApplyBtn.click()
            time.sleep(0.5)

        time.sleep(1)
        content = Selector().id("moe.nb4a:id/content").find()
        if content is not None:
            content.click()
            time.sleep(0.5)
        time.sleep(1)

        ImageButton = Selector().packageName("moe.nb4a").type("ImageButton").find()
        if ImageButton is not None:
            ImageButton.click()
            time.sleep(0.5)
        time.sleep(1)

        Route = Selector(2).id("moe.nb4a:id/nav_route").find()
        if Route is not None:
            Route.click()
            time.sleep(0.5)

        CreateRotue = Selector(2).id("moe.nb4a:id/action_new_route").find()
        if CreateRotue is not None:
            CreateRotue.click()
            time.sleep(0.5)
        domainBtn = Selector().id("android:id/title").text("domain").parent(1).find()
        if domainBtn is not None:
            domainBtn.click()
            time.sleep(0.5)
        Selector().id("android:id/edit").input(
            "domain:159.138.24.234\ndomain:hwadmin.xiaotwo.cn\ndomain:hwadmin.xiaotwo.cn").find()
        time.sleep(1)

        OKBtn = Selector(2).id("moe.nb4a:id/buttonPanel").type("ScrollView").child(2).find()
        if OKBtn is not None:
            OKBtn.click()
            time.sleep(0.5)
        action.slide(560, 1200, 560, 1070)
        time.sleep(2)
        outbound = Selector().id("android:id/title").text("outbound").parent(1).find()
        if outbound is not None:
            outbound.click()
            time.sleep(0.5)

        time.sleep(1)
        BypassBtn = Selector(2).packageName("moe.nb4a").type("ListView").child(2).find()
        if BypassBtn is not None:
            BypassBtn.click()
            time.sleep(0.5)
        time.sleep(2)

        ApplyBtn = Selector(2).id("moe.nb4a:id/action_apply").find()
        if ApplyBtn is not None:
            ApplyBtn.click()
            time.sleep(0.5)
        time.sleep(1)

        ImageButton = Selector().packageName("moe.nb4a").type("ImageButton").find()
        if ImageButton is not None:
            ImageButton.click()
            time.sleep(0.5)
        time.sleep(1)

        time.sleep(1)
        action.Key.back()
        time.sleep(1)
        fabBtn = Selector().id("moe.nb4a:id/fab").find()
        if fabBtn is not None:
            fabBtn.click()
            time.sleep(0.5)
        time.sleep(1)
        OKBtn = Selector().id("android:id/button1").text("OK").find()
        if OKBtn is not None:
            OKBtn.click()
            time.sleep(0.5)
        time.sleep(2)
        action.click(530, 2080)
        time.sleep(10)
        node = Selector().id("moe.nb4a:id/status").find()
        print('node===>', node)
        content = node.text
        print('content===>', content)
        if 'Success' in content or '成功' in content:
            print('ip切换成功')
            action.Key.home()
            return True

        content = Selector().id("moe.nb4a:id/content").find()
        if content is None:
            YesBtn = Selector().id("android:id/button1").find()
            if YesBtn is not None:
                YesBtn.click()
                time.sleep(0.5)
            action_add = Selector().id("moe.nb4a:id/action_add").find()
            if action_add is not None:
                action_add.click()
                time.sleep(0.5)
            ManualSetting = Selector(2).packageName("moe.nb4a").type("ListView").child(4).find()
            if ManualSetting is not None:
                ManualSetting.click()
                time.sleep(0.5)
            SOCKSBtn = Selector().id("moe.nb4a:id/title").text("SOCKS").parent(1).find()
            if SOCKSBtn is not None:
                SOCKSBtn.click()
                time.sleep(0.5)
            ServerBtn = Selector(2).id("moe.nb4a:id/recycler_view").type("RecyclerView").child(4).find()
            if ServerBtn is not None:
                ServerBtn.click()
                time.sleep(0.5)

            editServer = Selector().id("android:id/edit").click().input("gw-zhuandian.ntnt.io").find()
            time.sleep(1)
            OKBtn = Selector(2).id("moe.nb4a:id/buttonPanel").type("ScrollView").child(2).find()
            if OKBtn is not None:
                OKBtn.click()
                time.sleep(0.5)

            PortBtn = Selector(2).id("moe.nb4a:id/recycler_view").type("RecyclerView").child(5).find()
            if PortBtn is not None:
                PortBtn.click()
                time.sleep(0.5)

            Selector().id("android:id/edit").click().input("9595").find()
            time.sleep(1)
            OKBtn = Selector(2).id("moe.nb4a:id/buttonPanel").type("ScrollView").child(2).find()
            if OKBtn is not None:
                OKBtn.click()
                time.sleep(0.5)

            userNameSet = Selector(2).id("moe.nb4a:id/recycler_view").type("RecyclerView").child(6).find()
            if userNameSet is not None:
                userNameSet.click()
                time.sleep(0.5)
            # 拼接最终字符串
            Selector().id("android:id/edit").click().input(username).find()
            time.sleep(1)
            OKBtn = Selector(2).id("moe.nb4a:id/buttonPanel").type("ScrollView").child(2).find()
            if OKBtn is not None:
                OKBtn.click()
                time.sleep(0.5)
            time.sleep(1)

            Password = Selector(2).id("moe.nb4a:id/recycler_view").type("RecyclerView").child(7).find()
            if Password is not None:
                Password.click()
                time.sleep(0.5)

            Selector().id("android:id/edit").click().input('Us2l8X40RWjtq1V').find()
            time.sleep(1)
            OKBtn = Selector(2).id("moe.nb4a:id/buttonPanel").type("ScrollView").child(2).find()
            if OKBtn is not None:
                OKBtn.click()
                time.sleep(0.5)

            time.sleep(2)
            ApplyBtn = Selector(2).type("FrameLayout").child(4).find()
            if ApplyBtn is not None:
                ApplyBtn.click()
                time.sleep(0.5)

            time.sleep(1)
            content = Selector().id("moe.nb4a:id/content").find()
            if content is not None:
                content.click()
                time.sleep(0.5)
            time.sleep(1)

            ImageButton = Selector().packageName("moe.nb4a").type("ImageButton").find()
            if ImageButton is not None:
                ImageButton.click()
                time.sleep(0.5)
            time.sleep(1)

            Route = Selector(2).id("moe.nb4a:id/nav_route").find()
            if Route is not None:
                Route.click()
                time.sleep(0.5)

            CreateRotue = Selector(2).id("moe.nb4a:id/action_new_route").find()
            if CreateRotue is not None:
                CreateRotue.click()
                time.sleep(0.5)
            domainBtn = Selector().id("android:id/title").text("domain").parent(1).find()
            if domainBtn is not None:
                domainBtn.click()
                time.sleep(0.5)
            Selector().id("android:id/edit").input("domain:159.138.24.234\ndomain:hwadmin.xiaotwo.cn\ndomain:hwadmin.xiaotwo.cn").find()
            time.sleep(1)

            OKBtn = Selector(2).id("moe.nb4a:id/buttonPanel").type("ScrollView").child(2).find()
            if OKBtn is not None:
                OKBtn.click()
                time.sleep(0.5)
            action.slide(560, 1200, 560, 1070)
            time.sleep(2)
            outbound = Selector().id("android:id/title").text("outbound").parent(1).find()
            if outbound is not None:
                outbound.click()
                time.sleep(0.5)

            time.sleep(1)
            BypassBtn = Selector(2).packageName("moe.nb4a").type("ListView").child(2).find()
            if BypassBtn is not None:
                BypassBtn.click()
                time.sleep(0.5)
            time.sleep(2)

            ApplyBtn = Selector(2).id("moe.nb4a:id/action_apply").find()
            if ApplyBtn is not None:
                ApplyBtn.click()
                time.sleep(0.5)
            time.sleep(1)

            ImageButton = Selector().packageName("moe.nb4a").type("ImageButton").find()
            if ImageButton is not None:
                ImageButton.click()
                time.sleep(0.5)
            time.sleep(1)

            '''注释设置代理模式的代码'''
            # SettingsBtn = Selector(2).id("moe.nb4a:id/nav_settings").find()
            # if SettingsBtn is not None:
            #     SettingsBtn.click()
            #     time.sleep(0.5)
            # time.sleep(1)
            # # 滑动操作
            # node = Selector().type("RecyclerView").find()
            # if node:
            #     node.slide(-1)
            #
            # time.sleep(2)
            # VpnMode = Selector(2).id("moe.nb4a:id/recycler_view").child(8).find()
            # if VpnMode is not None:
            #     VpnMode.click()
            #     time.sleep(0.5)
            # time.sleep(1)
            # ProxyBtn = Selector(2).id("moe.nb4a:id/appProxyModeOn").find()
            # if ProxyBtn is not None:
            #     ProxyBtn.click()
            #     time.sleep(0.5)
            # time.sleep(1)
            # SystemApps = Selector(2).id("moe.nb4a:id/show_system_apps").find()
            # if SystemApps is not None:
            #     SystemApps.click()
            #     time.sleep(0.5)
            # time.sleep(1)
            # self.find_package_proxy(self.gaijiPack)
            # self.find_package_proxy(deviceData.packageName)
            # time.sleep(1)
            # action.Key.back()


            # time.sleep(1)
            # action.Key.back()
            # time.sleep(1)
            # fabBtn = Selector().id("moe.nb4a:id/fab").find()
            # if fabBtn is not None:
            #     fabBtn.click()
            #     time.sleep(0.5)
            # time.sleep(1)
            # OKBtn = Selector().id("android:id/button1").text("OK").find()
            # if OKBtn is not None:
            #     OKBtn.click()
            #     time.sleep(0.5)
            # time.sleep(2)
            # action.click(530,2080)
            # time.sleep(10)
            # node = Selector().id("moe.nb4a:id/status").find()
            # print('node===>', node)
            # content = node.text
            # print('content===>', content)
            # if 'Success' in content or '成功'in content:
            #     print('ip切换成功')
            #     action.Key.home()
            #     return True
        # else:
        #     print('已有代理服务器')
        #     VpnOn = Selector().desc("VPN on.").find()
        #     if VpnOn is not None:
        #         fabBtn = Selector().id("moe.nb4a:id/fab").find()
        #         if fabBtn is not None:
        #             fabBtn.click()
        #             time.sleep(0.5)
        #         time.sleep(1)
        #     EditBtn = Selector(2).id("moe.nb4a:id/edit").find()
        #     if EditBtn is not None:
        #         EditBtn.click()
        #         time.sleep(0.5)
        #     time.sleep(1)
        #     userNameSet = Selector(2).id("moe.nb4a:id/recycler_view").type("RecyclerView").child(6).find()
        #     if userNameSet is not None:
        #         userNameSet.click()
        #         time.sleep(0.5)
        #     Selector().id("android:id/edit").click().input(username).find()
        #     time.sleep(1)
        #     OKBtn = Selector(2).id("moe.nb4a:id/buttonPanel").type("ScrollView").child(2).find()
        #     if OKBtn is not None:
        #         OKBtn.click()
        #         time.sleep(0.5)
        #     time.sleep(1)
        #     time.sleep(2)
        #     ApplyBtn = Selector().id("moe.nb4a:id/action_apply").find()
        #     if ApplyBtn is not None:
        #         ApplyBtn.click()
        #         time.sleep(0.5)
        #     time.sleep(1)
        #
        #     ImageButton = Selector().packageName("moe.nb4a").type("ImageButton").find()
        #     if ImageButton is not None:
        #         ImageButton.click()
        #         time.sleep(0.5)
        #     time.sleep(1)

            # SettingsBtn = Selector(2).id("moe.nb4a:id/nav_settings").find()
            # if SettingsBtn is not None:
            #     SettingsBtn.click()
            #     time.sleep(0.5)
            # time.sleep(1)
            # node = Selector().type("RecyclerView").find()
            # if node:
            #     node.slide(-1)
            # time.sleep(2)
            # VpnMode = Selector(2).id("moe.nb4a:id/recycler_view").child(8).find()
            # if VpnMode is not None:
            #     VpnMode.click()
            #     time.sleep(0.5)
            # time.sleep(1)
            # SystemApps = Selector().id("moe.nb4a:id/show_system_apps").find()
            # if SystemApps is not None:
            #     SystemApps.click()
            #     time.sleep(0.5)
            # time.sleep(1)
            # self.find_package_proxy(self.gaijiPack)
            # self.find_package_proxy(deviceData.packageName)
            # time.sleep(1)
            # action.Key.back()
            # time.sleep(1)
            # action.Key.back()
            # time.sleep(1)
            # fabBtn = Selector().id("moe.nb4a:id/fab").find()
            # if fabBtn is not None:
            #     fabBtn.click()
            #     time.sleep(0.5)
            # time.sleep(1)
            # OKBtn = Selector().id("android:id/button1").text("OK").find()
            # if OKBtn is not None:
            #     OKBtn.click()
            #     time.sleep(0.5)
            # time.sleep(2)
            # action.click(530,2080)
            # time.sleep(10)
            # node = Selector().id("moe.nb4a:id/status").find()
            # print('node===>', node)
            # content = node.text
            # print('content===>', content)
            # if 'Success' in content or '成功'in content:
            #     print('ip切换成功')
            #     action.Key.home()
            #     return True
        # return False

    def check_ip(self, proxy):
        print('wait.....')
        # 使用 HTTP/HTTPS 代理
        proxies = {"http": proxy, "https": proxy}
        print('proxies===>', proxies)
        try:
            response = requests.get('https://ipinfo.ipidea.io', proxies=proxies, verify=False, timeout=5)
            resjson = response.json()
            print('ip检测结果==>', resjson)
            return resjson['ip']
        except Exception as e:
            print('ip异常需要切换', str(e))
            return None

    def find_package_proxy(self, package):
        lastAppack = None
        same_count = 0
        max_same_count = 3  # 最大允许相同内容次数
        while True:
            applist = Selector().id("moe.nb4a:id/list").child().find_all()
            print('applist===>', applist)
            if applist:
                for app in applist:
                    content = app.child(2).text
                    if package in content:
                        print('存在')
                        print('包名--->',content)
                        checkStatus = app.child(3).checked
                        if not checkStatus:
                            print('未点击')
                            app.click()
                            time.sleep(2)
                        return
                current_app = applist[-1].child(2).text
                print(f'当前应用内容: {current_app}')
                # 如果 current_app 和 lastAppack 一样，增加 same_count，否则重置 same_count 并更新 lastAppack
                same_count = same_count + 1 if lastAppack == current_app else 0
                lastAppack = current_app
                # 如果连续出现了 max_same_count 次相同内容，则返回 True
                if same_count >= max_same_count:
                    print(f'{current_app} 已连续出现 {same_count} 次，返回')
                    return
            # 滑动操作
            node = Selector().type("RecyclerView").find()
            if node:
                node.slide(-1)
            else:
                print("没有找到可滑动的节点")
                return   # 如果找不到可滑动节点则退出
            time.sleep(2)
