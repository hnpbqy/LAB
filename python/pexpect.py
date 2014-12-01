#ssh_cmd.py
#coding:utf-8

import pexpect

def ssh_cmd(ip, user, passwd, cmd):
    ssh = pexpect.spawn('ssh %s@%s "%s"' % (user, ip, cmd))
    r = ''
    try:
        i = ssh.expect(['password: ', 'continue connecting (yes/no)?'])
        if i == 0 :
            ssh.sendline(passwd)
        elif i == 1:
            ssh.sendline('yes')
    except pexpect.EOF:
        ssh.close()
    else:
        r = ssh.read()
        ssh.expect(pexpect.EOF)
        ssh.close()
    return r

hosts = '''
192.168.0.12:smallfish:1234:df -h,uptime
192.168.0.13:smallfish:1234:df -h,uptime
'''

for host in hosts.split("/n"):
    if host:
        ip, user, passwd, cmds = host.split(":")
        for cmd in cmds.split(","):
            print "-- %s run:%s --" % (ip, cmd)
            print ssh_cmd(ip, user, passwd, cmd)