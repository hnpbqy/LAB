
node default {

file {"/tmp/viong.txt":
content=>"good,test pass!\n";}

file
{ "/opt/openvpn-2.2.2.tar.gz":
source =>"puppet://$puppetserver/files/openvpn-2.2.2.tar.gz",
}

file
{ "/tmp/puppet.sh":
owner => "puppet",
group => "puppet",
mode => 666,
}

exec {"exec-mkdir":
cwd => "/opt",
command => "sh /opt/puppet.sh",
user => "root",
path =>"/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin",
}

service
{ crond:
ensure => "running",
}

}