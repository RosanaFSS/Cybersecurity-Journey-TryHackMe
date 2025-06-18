<p align="center"><img width="80px" src=""><br>
June 17, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure,<br>
part of my <code>407</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
My first CTF ! <br>Click <a href="https://tryhackme.com/room/olympusroom">here</a>to access the "room".<br>
<img width="1200px" src="e"></p>

<h2> Task 1 . Connection</h2>

<h3 align="left"> Answer the question below</h3>

> 1.1. <em>Start the VM</em><br><a id='1.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>

<h2>Task 2 . Flag submission</h2>

<h3 align="left"> Answer the questions below</h3>

> 2.1. <em>What is Flag 1?</em><br><a id='2.1'></a>
>> <strong><code>flag{Sm4rt!_k33P_d1gGIng}</code></strong><br>
<p></p>

<br>

> 2.2. <em>What is Flag 2??</em><br><a id='2.2'></a>
>> <strong><code>flag{Y0u_G0t_TH3_l1ghtN1nG_P0w3R}</code></strong><br>
<p></p>

<br>

> 2.3. <em>What is Flag 3?</em><br><a id='2.3'></a>
>> <strong><code>____</code></strong><br>
<p></p>

<br>

> 2.4. <em>What is Flag 4?</em><br><a id='2.4'></a>
>> <strong><code>____</code></strong><br>
<p></p>

<br>

<h3>nmap</h3>

```bash
:~# nmap -sS TargetIP
...
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http
...
```

```bash
:~# nmap -sC -sV -Pn -p- -T4 TargetIP
...
PORT   STATE SERVICE VERSION
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Did not follow redirect to http://olympus.thm
...
```

```bash
TargetIP olympus.thm
```

<h3>dirsearch</h3>

```bash
:~# dirsearch -u http://olympus.thm/ -i200,301,302,401 -w /usr/share/dirb/wordlists/common.txt
...
Target: http://olympus.thm/

Starting: 
301 -  315B  - /~webmaster  ->  http://olympus.thm/~webmaster/
301 -  315B  - /javascript  ->  http://olympus.thm/javascript/
301 -  311B  - /static  ->  http://olympus.thm/static/

Task Completed
```

```bash
:~# dirsearch -u http://olympus.thm/~webmaster/ -i200,301,302,401 -w /usr/share/dirb/wordlists/common.txt
...
Starting: ~webmaster/
301 -  321B  - /~webmaster/admin  ->  http://olympus.thm/~webmaster/admin/
301 -  319B  - /~webmaster/css  ->  http://olympus.thm/~webmaster/css/
301 -  321B  - /~webmaster/fonts  ->  http://olympus.thm/~webmaster/fonts/
301 -  319B  - /~webmaster/img  ->  http://olympus.thm/~webmaster/img/
301 -  324B  - /~webmaster/includes  ->  http://olympus.thm/~webmaster/includes/
301 -  318B  - /~webmaster/js  ->  http://olympus.thm/~webmaster/js/
200 -    1KB - /~webmaster/LICENSE

Task Completed
```

```bash
:~# dirsearch -u http://olympus.thm/~webmaster/admin/ -i200,301,302,401 -w /usr/share/dirb/wordlists/common.txt
...
Starting: ~webmaster/admin/
301 -  325B  - /~webmaster/admin/css  ->  http://olympus.thm/~webmaster/admin/css/
301 -  327B  - /~webmaster/admin/fonts  ->  http://olympus.thm/~webmaster/admin/fonts/
301 -  330B  - /~webmaster/admin/includes  ->  http://olympus.thm/~webmaster/admin/includes/
301 -  325B  - /~webmaster/admin/img  ->  http://olympus.thm/~webmaster/admin/img/
301 -  324B  - /~webmaster/admin/js  ->  http://olympus.thm/~webmaster/admin/js/

Task Completed
:~# 
```

<h3>http://olympus.thm</h3>
<p>- Olympus v2<br>
- under developpment<br>
- root@the-it-department</p>

![image](https://github.com/user-attachments/assets/6c601d90-db9c-45d3-b864-05949c980b7a)

<h3>http://olympus.thm/~webmaster/admin/ --> http://olympus.thm/~webmaster/index.php</h3>
<p>- Gods and Godess<br>
- 900 * 300<br>
- wordlist<br>
- Victor Alagwu
</p>

![image](https://github.com/user-attachments/assets/6f783828-a123-4b54-8c76-8b31f47449cc)

![image](https://github.com/user-attachments/assets/cd6ba025-f71a-448b-9e41-58a803329f94)

<h3>Burp Suite</h3>

![image](https://github.com/user-attachments/assets/7d40c041-4db0-4458-a81d-c053b3468fa6)

<p>saved <code>re</code></p>


<h3>sqlmap</h3>
<p>- <code>user_id</code> : <code>3</code><br>
- <code>user_name</code> : <code>prometheus</code><br>
- <code>user_firstname</code> : <code>prometheus</code><br>
- <code>user_lastname</code> : <code> </code><br>
- <code>user_email</code> : <code>prometheus@olympus.thm</code><br>
- <code>user_role</code> : <code>User</code><br>
- <code>user_password</code> : <code>$2y$10$YC6uoMwK9VpB5QL513vfLu1RV2sgBf01c0lzPHcz1qK2EArDvnj3C</code><br><br>

- <code>user_name</code> : <code>root</code><br> </p>
