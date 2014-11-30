#!/usr/bash
# -*- coding: utf-8 -*-
intellij IDEA
IDEA theme   saltstack  ansible  capistrano chef
http://blog.chinaunix.net/uid-24250828-id-3882898.html
chef-server192.168.10.250    
chef-workstation192.168.10.250 
chef-client192.168.10.10   
2.3.1  
http://mirrors.sohu.com/fedora-epel/5Server/ 
 
--------------------------------------------------------
#puppet服务端
yum install ntp vixie-cron wget vim-enhanced telnet  -y
chkconfig --level 35 ntpd on
crontab -e  
10 5 * * * root /usr/sbin/ntpdate time.nist.gov && /sbin/hwclock -w
 
service crond restart
echo "192.168.1.167 client1.viong.com" >>/etc/hosts
hostname server.viong.com
 vi /etc/sysconfig/network 改hostname
 /etc/resolv
 #search localdomain        #注释掉这行，不然造成后面无法认证
 yum install ruby ruby-libs ruby-rdoc  -y
 
 安装puppet之前必须先安装facter
[root@puppet soft]# wget http://downloads.puppetlabs.com/facter/facter-1.6.8.tar.gz
[root@puppet soft]# tar -zxvf facter-1.6.8.tar.gz
[root@puppet soft]# cd facter-1.6.8 
[root@puppet facter-1.6.8]# ruby install.rb

  wget http://downloads.puppetlabs.com/puppet/puppet-2.7.14.tar.gz

[root@puppet soft]# tar -zxvf puppet-2.7.14.tar.gz

[root@puppet soft]# cd puppet-2.7.14

[root@puppet puppet-2.7.14]# ruby install.rb

 cp conf/redhat/fileserver.conf /etc/puppet/          
 cp conf/redhat/puppet.conf /etc/puppet/
 cp conf/redhat/server.init /etc/init.d/puppetmaster
 chmod +x /etc/init.d/puppetmaster
 ll /etc/init.d/puppetmaster
  chkconfig --add puppetmaster
  chkconfig --level 35 puppetmaster on
  
puppetmasterd --mkusers 

ls -l /etc/puppet/
id puppet  确认系统生成puppet用户
保证/var/lib/puppet/rrd目录存在且属主是puppet
ls -l /var/lib/puppet/
netstat -Tanlp | grep 8140
#puppet客户端
 echo "192.168.1.168 server.viong.com" >>/etc/hosts
 hostname client1.viong.com
 vi /etc/sysconfig/network
ifconfig eth0 192.168.1.167 netmask 255.255.255.0 up
DEVICE=eth0
BOOTPROTO=static
ONBOOT=yes
HWADDR=00:0c:29:91:ea:aa
IPADDR=192.168.1.167
NETMASK=255.255.255.0
GATEWAY=192.168.1.1

rm -rf /etc/init.d/puppetmaster
  chkconfig --del puppetmaster
  chkconfig --level 35 puppetmaster on
  
cp conf/redhat/client.init /etc/init.d/puppet
  chkconfig --add puppet
chkconfig --level 35 puppet on
#测试连通性
telnet server.viong.com 8140
puppetd --test --server server.viong.com 命令是指puppetd 从 server.viong.com去读取puppet配置文件. 第一次连接,双方会进行ssl证书的验证,这是一个新的客户端,在服务器端那里还没有被认证,因此需要在服务器端进行证书认证
#建立认证关系，客户端请求服务端认证
#①在客户端执行，申请证书 
申请签名认证 puppet agent  --server=server.viong.com --no-daemonize –verbose  
#②在服务端执行，接受申请 
查看当然待批准证书列表  #puppet cert  –list    [root@server ~]# puppetca –l   
批准当前证书  [root@server ~]# puppetca -s client1.viong.com

查看验证签名,注意前面的+号，说明已经签名  puppetca -a --list
[
如果要批准全部证书
puppetca -s -a
也可以在puppetmaster端的puppet.conf加入这行：
autosign = true
服务端就自动签证书
]

#③客户端执行，取回通过审批的证书  puppetd --test --server server.viong.com
[-客户端和服务器端时间不同步
-签名完毕后不能再随意修改主机名,否则认证失效

#若出现修改主机名问题引起无法认证，需要重新申请证书，操作以下两个步骤：
删除掉服务器端的客户机证书 rm -f    /var/lib/puppet/ssl/ca/signed/主机名.pem
客户端删除掉ssl目录 /var/lib/puppet/ssl

服务端 puppet cert clean client1.viong.com

客户端rm -f /var/lib/puppet/ssl/certs/client1.viong.com.pem
puppet agent -t
 ]

[验证证书是否正确
服务端：
[root@server ~]# md5sum /var/lib/puppet/ssl/ca/signed/client1.viong.com.pem
8529a6f2d42c1b492c016fe870b744b6 /var/lib/puppet/ssl/ca/signed/client1.viong.com.pem
客户端：
[root@client1 puppet-2.7.14]# md5sum /var/lib/puppet/ssl/certs/client1.viong.com.pem
8529a6f2d42c1b492c016fe870b744b6 /var/lib/puppet/ssl/certs/client1.viong.com.pem  
]
------------------------------------------------------------------------------------------
#功能测试
#服务端
vi /etc/puppet/manifests/site.pp
node default {

file {"/tmp/viong.txt":

content=>"good,test pass!\n";}
}
service puppetmaster restart 
   
#客户端：
puppetd --test --server server.viong.com   
附 设置客户端的守护进程

[root@client1 puppet-2.7.14]# puppetd --test --server server.viong.com --verbose --waitforcert 100

info: Caching catalog for client1.viong.com

info: Applying configuration version '1338897814'

notice: Finished catalog run in 0.03 seconds

--server 服务端FQDN –-verbose 输出冗余信息 –-waitforcert 超时100

1本人觉得使用cron或者手动运行puppet比较符合需求，或者以脚本方式，当master有改变再执行编写的脚本 第一次启动建议采用puppet master --verbose --no-daemonize方式启动，有助于测试和调试错误，如果采用后面这种方式，你可以看到启动的整个过程，启动过程会做一些初始化的工作，为master创建本地证书认证中心，证书和key。并打开socket等待client的连接。你可以在/etc/puppet/ssl目录看到相关的文件和目录。
Puppet工作流程：
1.客户端puppetd调用facter，facter会探测出这台主机的一些变量如主机名、内存大小、IP地址等。然后puppetd把这些信息发送到服务器端。 
2.服务器端的puppetmaster检测到客户端的主机名，然后会找到manifest里面对应的node配置，然后对这段内容进行解析；facter送过来的信息可以作为变量进行处理，node牵涉到的代码才解析，其它的代码不解析；解析分几个过程：语法检查、然后会生成一个中间的伪代码，然后再把伪代码发给客户机。 
3.客户端接收到伪代码之后就会执行，客户端再把执行结果发送给服务器。 
4.服务器再把客户端的执行结果写入日志。

说明：Puppet后台运行的时间默认是半小时执行一次，不是很方便。可以考虑不让它在后台跑而是使用crontab来调用。这样可以精确控制每台客户端的执行时间，分散执行时间也可以减轻服务器负载。

2.生成配置文件，3.1.1源码包的conf里面没有puppet的配置文件，可以用下面的方式生成配置文件。
puppet master--genconfig > /etc/puppet/puppet.conf 生成master配置文件
puppet agent--genconfig > /etc/puppet/puppet.conf 生成agent配置文件
puppet2.6后支持windows  3好像支持图形化
hosts 例子172.16.228.30   puppet.sina.com.cn puppet
启动Server端：
service puppetmaster start
启动客户端：
/etc/init.d/puppet once -v
#每个客户端默认每半个小时和服务器进行一次通信，确认配置信息的更新情况。如果有新的配置信息或者配置信息已经改变，配置将会被重新编译并发布到各客户端执行。也可以在服务器上主动触发一个配置信息的更新，强制各客户端进行配置。？如果客户端的配置信息被改变了，它可以从服务器获得原始配置进行校正
puppetrun 用于连接客户端，强制运行本地配置文件
# puppet kick -p 10 -t remotefile -t webserver host1 host2
puppet kick -p 10   -t remotefile -t webserver client1.viong.com
？filebucket 客户端用于发送文件到puppet file bucket的工具
# filebucket -b /tmp/filebucket /my/file
path /run
auth any
method save
allow puppet.xxx.com

------------------------------------------------------------------------
#应用实例 包括软件的安装，文件的配置，系统服务，文件的管理，用户的添加/删除，定时计划配置等。在puppet中，将上述列出的管理任务称为资源
1 文件分发
/etc/puppet/manifests/site.pp
 /etc/puppet/fileserver.conf
[files]
path /opt/
allow 192.168.133.0/24

第二步：vi/etc/puppet/manifests/site.pp
file
{ "/opt/openvpn-2.2.2.tar.gz":
source =>"puppet://$puppetserver/files/openvpn-2.2.2.tar.gz",
}
 此处“$puppetserver”是puppet Server端的名称，即hostname，网上教程都是在hosts里指定，生产环境下用内部的DNS上作解析，像我公司一个www平台就有70台linux服务器，一个个添加hosts，不搞死人去。
 
2 修改文件属性：
vi /etc/puppet/manifests/site.pp
---内容如下
file
{ "/tmp/puppet.sh":
owner => "puppet",
group => "puppet",
mode => 666,
}
3 执行SHELL命令或shell脚本：   
实例：通过puppet分发执行shell脚本，在客户端的opt目录下新建一目录shelldir。
exec {"exec-mkdir":
cwd => "/opt",
command => "sh /opt/puppet.sh",
user => "root",
path =>"/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin",
} 
把服务端改文件属性的文件删除 报这个
notice: Run of Puppet configuration client already in progress; skipping

4服务检查及修改： service命令操作的。所以，只能针对在/etc/init.d/目录下的服务
service
{ crond:
ensure => "running",
}	
5 cron计划任务：
接上面的shell程序实例，在17：30执行/opt/lgh.sh。
cron { "cron-shell": #title部分，可用来作为注释。
command => "sh /opt/lgh.sh" #要执行的命令
user => "root", #添加到root用户下的crontab中
minute => "30", #即第一个星号
hour => "17" #即第二个星号
}
登录客户端查看效果 crontab -l
6 *要求系统启动后，sshd服务自动启动 
*要求通过系统进程方式查看sshd服务运行状态 
*要求服务关闭后能够自动重启 
*要求配置文件被更改后服务能够执行restart动作
class ssh::service{ 
        service { $ssh::params::ssh_service_name: 
		                ensure => running,                 
						hasstatus => false,                 
						hasrestart => true,                 
						enable => true, 
						subscribe => Class["ssh::config"],       
						} 
						} 
 或 
class ssh::service{ 
        service { $ssh::params::ssh_service_name:                 
					ensure => stopped,                 
					hasstatus => false,                 
					hasrestart => true,                
					enable => true, 
                 subscribe => Class["ssh::config"],         
				 } 
			}   
客户端测试  puppet agent     --test
nfo: Applying configuration version '1414674033' 不一样
测试结果：ensure => running, hasstatus => false,的情况下服务如果被关闭是起不来的，ensure => stopped, hasstatus => false,的情况下服务如果是运行的可以被关闭 建议：写SysV脚本放到/etc/init.d目录下来实现 
7 *要求服务配置文件被改动后，服务能够自动reload而不是自动restart（也可以通过exec资源实现2.2 配置说明 
class ssh::service{ 
        service { $ssh::params::ssh_service_name:                 ensure => running,                 hasstatus => true,                 hasrestart => true,                 enable => true, 
                subscribe => Class["ssh::config"], #               provider => base|daemontools|init,                 provider => init,   
                path => "/etc/rc.d/init.d", 
                restart => "/etc/rc.d/init.d/sshd reload",                 start => "/etc/rc.d/init.d/sshd start",                 stop => "/etc/rc.d/init.d/sshd stop",         } }  
class ssh::config{ 
        file { $ssh::params::ssh_service_config:                 ensure => present,                 owner => 'root',                 group => 'root',                 mode => 0640, 
                source => "puppet:///modules/ssh/etc/ssh/sshd_config", #               backup => ".$backup_date.bak",                 backup => 'main', 
                require => Class["ssh::install"], 
                notify => Class["ssh::service"],  #等同于class ssh::service中的subscribe
				}
				}
2.2 配置说明 
class ssh::service{ 
        service { $ssh::params::ssh_service_name:                 ensure => running,                 hasstatus => true,                 hasrestart => true,                 enable => true, 
                subscribe => Class["ssh::config"], #               provider => base|daemontools|init,                 provider => init,   
                path => "/etc/rc.d/init.d", 
                restart => "/etc/rc.d/init.d/sshd reload",                 start => "/etc/rc.d/init.d/sshd start",                 stop => "/etc/rc.d/init.d/sshd stop",         } }  
class ssh::config{ 
        file { $ssh::params::ssh_service_config:                 ensure => present,                 owner => 'root',                 group => 'root',                 mode => 0640, 
                source => "puppet:///modules/ssh/etc/ssh/sshd_config", #               backup => ".$backup_date.bak",                 backup => 'main', 
                require => Class["ssh::install"], 
                notify => Class["ssh::service"],  #等同于class ssh::service中的subscribe				
				
-----------------------------------------------------------------------
#epel源安装 ,centos6选6，5就选5

　　32位系统选择：
　　rpm -ivh http://dl.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm
　rpm -ivh http://dl.fedoraproject.org/pub/epel/5/i386/epel-release-5-4.noarch.rpm

　　64位系统选择：
　　rpm -ivh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
　　rpm -ivh http://dl.fedoraproject.org/pub/epel/5/x86_64/epel-release-5-4.noarch.rpm

比如 rpm -ivh http://download.fedoraproject.org/pub/epel/4/i386/epel-release-4-10.noarch.rpm
 其实上面安装的那个包就是在你系统/etc/yum.repos.d/下释放了2个yum源的repo文件而已：
导入key：
rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-6
rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-5
/etc/yum.repos.d/epel.repo          正式版，所有的软件都是稳定可以信赖的 

/etc/yum.repos.d/epel-testing.repo  测试版

但是默认情况下，只有正式版是有效状态的，如果你想试试测试版的话，需要修改/etc/yum.repos.d/epel-testing.repo，把enabled=0改成enabled=1即可。

另外，如果你要使用yumdownloader来下载src.rpm包的话，需要把epel.repo里[epel-source]域下的enabled=0也改成enabled=1即可。

当然了，如果你暂时不想使用EPEL的yum源的话，把对应文件里的enabled=1改成enabled=0就行了，如果你完全不需要了，那就直接卸载掉：

[root@test ~]# rpm -e epel-release   或者把/etc/yum.repos.d/的文件变成默认的
rpm -e foreman-release
 yum repolist  查看。 
  
##加源头 2步   安装源头包（远程或本地）   安装好后 会有2个100%然后 yum repolist 
 [root@puppet src]# yum -y install http://yum.theforeman.org/releases/1.6/el6/x86_64/foreman-release.rpm
Loaded plugins: fastestmirror
Setting up Install Process
Cannot open: http://yum.theforeman.org/releases/1.6/el6/x86_64/foreman-release.rpm. Skipping.
Error: Nothing to do
[root@puppet src]# rpm -ivh foreman-release.rpm 
warning: foreman-release.rpm: Header V4 RSA/SHA1 Signature, key ID 1aa043b8: NOKEY
Preparing...                ########################################### [100%]
	package foreman-release-1.5.3-1.el6.noarch is already installed
[root@puppet src]# rpm -ivh foreman-release.rpm 
warning: foreman-release.rpm: Header V4 RSA/SHA1 Signature, key ID 1aa043b8: NOKEY
Preparing...                ########################################### [100%]
   1:foreman-release        ########################################### [100%]
 rpm 包安装后又软件版本名称 卸载的时候用。
加3种源  系统centos5.1 64位 与centos6.6 64位
①foreman源  安装foreman
yum -y install http://yum.theforeman.org/releases/1.6/el6/x86_64/foreman-release.rpm
yum -y install foreman-installer

②puppetlabs源 安装puppet
rpm -ivh http://yum.puppetlabs.com/puppetlabs-release-el-6.noarch.rpm

③epel源   软件包很多
rpm -ivh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
bad： rpm -ivh http://download.fedora.redhat.com/pub/epel/6/x86_64/epel-release-6-5.noarch.rpm

其实还可以结合本地源
-----------------------------------------------------------------------
#rpmforge源安装
•Use cat /etc/redhat-release to find which release of EL you are using
•Use uname -a to find your processor architecture
•Use rpm -ivh package-filename to install the rpmforge-release package (also works with URLs)
•You can use wget or curl to download the package using one of the above links if needed (for example on a server with no X Window)
•Then you can use yum to install the available packages from the RepoForge repo, e.g. yum install --enablerepo=rpmforge-extras
•Afterward, you can disable accidental updates from the repo by setting enabled = 0 in the repo definition file in /etc/yum.repos.d/

-----------------------------------------------------------------------
#升级 rbuy1.86到2.1 后gem rake 也有了 yum -y install zlib-devel curl-devel openssl-devel httpd-devel apr-devel apr-util-devel mysql-devel
yum install -y gcc zlib zlib-devel   
  
wget ftp://ftp.ruby-lang.org/pub/ruby/2.1/ruby-2.1.4.tar.gz
tar xvf ruby-1.8.7-p334.tar.gz   
cd ruby-1.8.7-p334   
./configure --enable-pthread   
make   
make install  
：http://www.linuxidc.com/Linux/2011-04/34623.htm 
通过yum –y install ruby*安装即可，还有另外一种情况，ruby和rubygems都已经安装，但没达到dbshards运行的版本(我在使用dbshards软件，它需要ruby更高的版本)，http://blog.sina.com.cn/s/blog_62739908010168wh.html
bash -s stable < <(curl -s https://raw.github.com/wayneeseguin/rvm/master/binscripts/rvm-installer)   
 rvm list known 
安装一个ruby版本  rvm install 1.9.3  #这里安装了最新的1.9.3, rvm list known列表里面的都可以拿来安装。
使用一个ruby版本  rvm use 1.9.3 
如果想设置为默认版本，可以这样 rvm use 1.9.3 --default 
查询已经安装的ruby rvm list
卸载一个已安装版本  rvm remove 1.9.2
列出当前ruby的gemset  rvm gemset list
-----------------------------------------------------------------------
#Puppet Dashboard
yum install  ruby-mysql mysql-server puppet-dashboard

[root@puppetserver rpms]# /etc/rc.d/init.d/mysqld restart
[root@puppetserver ~]# chkconfig mysqld on
[root@puppetserver rpms]# mysqladmin -uroot password odotboss
重置密码mysqladmin -u root -podotboss password ""   删用户Delete FROM user Where User="puppet"; 
[root@puppetserver rpms]# mysql -podotboss
mysql> create database dashboard character set utf8;
mysql> grant all on dashboard.* to 'dashboard'@'localhost' identified by "odotboss";
mysql> flush privileges;    
[root@puppetserver rpms]# mysql -udashboard -p  #测试账号是否创建成功
…
Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
mysql>
rake gems:refresh_specs
RAILS_ENV=production db:migrate 
#环境变量RAILS_ENV=production告诉Ruby on Rails我们工作在生产环境。每次你运行一个rake命令都需要使用合适的环境值来设置RAILS_ENV环境变量
 {

 create database foreman character set utf8;
  grant all privileges on foreman.* to 'foreman'@'localhost' identified by 'odotboss';
   create database foremandevel character set utf8;
  grant all privileges on foremandevel.* to 'foreman'@'localhost' identified by 'odotboss';
foreman、foremandevel、foremantest}
https://downloads.puppetlabs.com/dashboard/puppet-dashboard-1.2.23.tar.gz
 Ruby 1.8.7
* RubyGems
* Rake >= 0.8.3
* MySQL server 5.x
* Ruby-MySQL bindings 2.7.x or 2.8.x  
bringing up interface eth0 device eth0 does not seem to be present delaying 
00:0C:29:0D:F1:39  00:0C:29:0B:EA:7B   00:0C:29:36:DD:8D
gems install  *.gem
-----------------------------------------------------------------------
 <VirtualHost *:80>
      ServerName www.yourhost.com
      # !!! Be sure to point DocumentRoot to 'public'!
      DocumentRoot /somewhere/public    
      <Directory /somewhere/public>
         # This relaxes Apache security settings.
         AllowOverride all
         # MultiViews must be turned off.
         Options -MultiViews
         # Uncomment this if you're on Apache >= 2.4:
         #Require all granted
      </Directory>
   </VirtualHost>
-----------------------------------------------------------------------			
yum clean all
yum -y groupinstall "Development tools"
rpm -ivh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
rpm -vih http://yum.puppetlabs.com/el/6/products/x86_64/\
puppetlabs-release-6-7.noarch.rpm
yum -y install http://yum.theforeman.org/releases/1.2/el6/x86_64/\
foreman-release.rpm
yum -y install dhcp
yum -y install foreman-installer
ruby /usr/share/foreman-installer/generate_answers.rb	