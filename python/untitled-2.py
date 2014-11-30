#!/usr/bin/env python
#coding:utf-8
 
import paramiko
import threading
import os,sys,time
 
def ssh2(ip,pt,pw,us,comm):
        try:
 
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(ip,port=pt,username=us,password=pw)
                f.write(('='*20 +'%s status' +'='*20 + '\n')% ip)
                for COMM in comm:
                        stdin,stdout,stderr = ssh.exec_command(COMM)
                        read = stdout.read()
                        f.write(read)
                ssh.close()
 
#        except SyntaxError:
#               print "please checking"
#               sys.exit()
        except:
                print "Connection refused"
                sys.exit()
 
if __name__ == '__main__':
        print "\033[1;31m  请等待.....\033[0m"
        open_ip = open('/home/test/iplist.txt')
        f = open('/home/test/Allsystem.log','w')
        paramiko.util.log_to_file('/home/test/paramiko.log')
        up='uptime'
        df = "df -Ph |awk 'NR == 1 || NR == 6{print $0}'"
        net="ifconfig |awk 'NR==8'|sed 's/^\s*//g'"
        command = [up,df,net]
        for ip in open_ip.readlines():
                split = ip.split()
                name = split[1]
                ipaddr = split[2]
                password = split[3]
                aa = threading.Thread(target=ssh2,args=(ipaddr,22,password,name,command))
                aa.start()
                aa.join()
        open_ip.close()
        f.write('='*20 +'All done' +'='*20 + '\n')
        f.flush()
        f.close()
