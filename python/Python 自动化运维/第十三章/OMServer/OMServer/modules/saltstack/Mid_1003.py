# -*- coding: utf-8 -*-
from Public_lib import *

#查看系统版本模块#

class Modulehandle():
    def __init__(self,moduleid,hosts,sys_param_row):
        self.hosts = ""
        self.Runresult = ""
        self.moduleid = moduleid
        self.sys_param_array= sys_param_row
        self.hosts=target_host(hosts,"HN").split(";")

    def run(self):
        try:
            client = salt.client.LocalClient()
            self.Runresult  = client.cmd(self.hosts,'cmd.run',["/usr/bin/head -n 1 /etc/issue"],expr_form='list')
            if len(self.Runresult) == 0:
                return "No hosts found,请确认主机已经添加saltstack环境！"
        except Exception,e:
            return str(e)
        return self.Runresult
