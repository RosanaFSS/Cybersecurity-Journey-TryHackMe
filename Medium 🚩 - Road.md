<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Road}}$$</h1>
<p align="center">May 25, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my $$\textcolor{#FF69B4}{\textbf{384}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a><br>
Inspired by a real-world pentesting engagement Access it clicking <a href="https://tryhackme.com/room/road"</a>here.<br><br>
<img width="1000px" src="https://github.com/user-attachments/assets/c49275ea-0bed-4101-9267-2e8a35458681"></p>

<br>
<br>


<h2>Task 1 . Submit Flags!</h2>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>


> 1.1. <em>What is the user.txt flag?</em><br><a id='1.1'></a>
>> <strong><code>63191e4ece37523c9fe6bb62a5364d45</code></strong><br>
<p></p>

<br>

> 1.2. <em>What is the root.txt flag?</em><br><a id='1.2'></a>
>> <strong><code>3a62d897c40a815ecbe267df2f533ac6</code></strong><br>
<p></p>

<br>
<br>

<h3>nmap</h3>

```bash
:~/Road# nmap -sV -sC -sS -A -O -p- -T4 TargetIP
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.2 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Sky Couriers

...
```

<br>

<h3>gobuster</h3>


```bash
gobuster dir -u http://TargetIP/ -w /usr/share/dirb/wordlists/common.txt
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://TargetIP/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/dirb/wordlists/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/.hta                 (Status: 403) [Size: 277]
/.htaccess            (Status: 403) [Size: 277]
/.htpasswd            (Status: 403) [Size: 277]
/assets               (Status: 301) [Size: 313] [--> http://10.10.181.12/assets/]
/index.html           (Status: 200) [Size: 19607]
/phpMyAdmin           (Status: 301) [Size: 317] [--> http://10.10.181.12/phpMyAdmin/]
/server-status        (Status: 403) [Size: 277]
/v2                   (Status: 301) [Size: 309] [--> http://10.10.181.12/v2/]
Progress: 4614 / 4615 (99.98%)
===============================================================
Finished
===============================================================
root@ip-10-10-212-118:~/Road# 


```

<br>

```bash
~/Road# gobuster dir -u http://targetIP/v2/ -w /usr/share/dirb/wordlists/common.txt
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://Target_IP/v2/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/dirb/wordlists/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/.hta                 (Status: 403) [Size: 277]
/.htaccess            (Status: 403) [Size: 277]
/.htpasswd            (Status: 403) [Size: 277]
/admin                (Status: 301) [Size: 315] [--> http://10.10.181.12/v2/admin/]
/index.php            (Status: 302) [Size: 20178] [--> /v2/admin/login.html]
Progress: 4614 / 4615 (99.98%)
===============================================================
Finished

```

<br>

<h3>http://TargetIP/v2/admin/login.html</h3>

![image](https://github.com/user-attachments/assets/6da3e664-2d16-4a08-91c9-e0f4ba409c95)


<br>

![image](https://github.com/user-attachments/assets/a33a7182-59cb-4ff4-9a91-0708fcd76415)

<p><code>Your account has been created</code>.</p>

![image](https://github.com/user-attachments/assets/aecf6a3c-8288-4fd5-8baf-a7cea5e290de)

<br>

![image](https://github.com/user-attachments/assets/48ecaac8-314f-4f83-9207-b190efcda632)

<br>

![image](https://github.com/user-attachments/assets/26387bab-50b6-432b-9464-858356847d5e)

<br>

<p>Added TargetIP ands skycouriers.thm to /etc/hosts</p>

<br>

<h3>gobuster</h3>

```bash
:~/Road# gobuster dir -u http://skycouriers.thm/ -w /usr/share/dirb/wordlists/common.txt -t 100 -x txt,php,html,bak
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://skycouriers.thm/
[+] Method:                  GET
[+] Threads:                 100
[+] Wordlist:                /usr/share/dirb/wordlists/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Extensions:              php,html,bak,txt
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/.php                 (Status: 403) [Size: 280]
/.hta.html            (Status: 403) [Size: 280]
/.hta                 (Status: 403) [Size: 280]
/.hta.php             (Status: 403) [Size: 280]
/.hta.txt             (Status: 403) [Size: 280]
/.html                (Status: 403) [Size: 280]
/.htpasswd.txt        (Status: 403) [Size: 280]
/.htpasswd.bak        (Status: 403) [Size: 280]
/assets               (Status: 301) [Size: 319] [--> http://skycouriers.thm/assets/]
/.htpasswd.html       (Status: 403) [Size: 280]
/.htpasswd.php        (Status: 403) [Size: 280]
/.htaccess.bak        (Status: 403) [Size: 280]
/.htaccess.html       (Status: 403) [Size: 280]
/.htpasswd            (Status: 403) [Size: 280]
/.htaccess            (Status: 403) [Size: 280]
/.htaccess.txt        (Status: 403) [Size: 280]
/.htaccess.php        (Status: 403) [Size: 280]
/.hta.bak             (Status: 403) [Size: 280]
/career.html          (Status: 200) [Size: 9289]
/index.html           (Status: 200) [Size: 19607]
/index.html           (Status: 200) [Size: 19607]
/phpMyAdmin           (Status: 301) [Size: 323] [--> http://skycouriers.thm/phpMyAdmin/]
/server-status        (Status: 403) [Size: 280]
/v2                   (Status: 301) [Size: 315] [--> http://skycouriers.thm/v2/]
Progress: 23070 / 23075 (99.98%)
===============================================================
Finished
===============================================================

```


<br>

<h3>Job opnening</h3>


![image](https://github.com/user-attachments/assets/4207a85b-5adc-4722-8f2d-e55c987836af)



<br>

![image](https://github.com/user-attachments/assets/447c11f8-4278-46a0-8783-733abb370b1b)

<br>

![image](https://github.com/user-attachments/assets/882dea37-c07c-452d-8eba-5dad558a8c7d)


<br>

![image](https://github.com/user-attachments/assets/9cbb7ed4-ef53-40a5-a7d4-d9f4f35c0ff5)

<br>

![image](https://github.com/user-attachments/assets/dce26fb1-cb20-4314-8af4-75a4137999fd)

<br>

![image](https://github.com/user-attachments/assets/c6157bac-51ee-4da9-a58c-51c42ccbd1d6)


<br>


<br>

![image](https://github.com/user-attachments/assets/bd837196-a623-46e3-ae9a-a9ed1f6a759a)




<br>

![image](https://github.com/user-attachments/assets/67d66d1d-404c-40b9-9fc8-5f5de9b8c821)

<br>


![image](https://github.com/user-attachments/assets/f72daadb-41eb-4227-9a65-3b72625d1b0e)


<br>

![image](https://github.com/user-attachments/assets/59780970-bd10-4aeb-aa18-bebc2bcea42d)

<br>

![image](https://github.com/user-attachments/assets/993cf885-ba06-4d55-9606-961cab96e503)

 "_id" : ObjectId("60ae2661203d21857b184a76"), "Month" : "Feb", "Profit" : "25000" }
{ "_id" : ObjectId("60ae2677203d21857b184a77"), "Month" : "March", "Profit" : "5000" }
{ "_id" : ObjectId("60ae2690203d21857b184a78"), "Name" : "webdeveloper", "Pass" : "BahamasChapp123!@#" }
{ "_id" : ObjectId("60ae26bf203d21857b184a79"), "Name" : "Rohit", "EndDate" : "December" }
{ "_id" : ObjectId("60ae26d2203d21857b184a7a"), "Name" : "Rohit", "Salary" : "30000" }

<br>

![image](https://github.com/user-attachments/assets/542a666a-544a-4349-bf37-d3d719ba81ea)

<br>

![image](https://github.com/user-attachments/assets/9dcaedb5-604f-4056-aa44-2210b47f6fa5)


<br>

![image](https://github.com/user-attachments/assets/e9129504-4220-4f31-befe-fccb2623b137)

<br>

![image](https://github.com/user-attachments/assets/c66feba5-d411-430b-84e1-77eb68a4ca24)

<br>

![image](https://github.com/user-attachments/assets/7129f2ad-345b-448b-ac2f-e03ac3c07b6b)

<br>

![image](https://github.com/user-attachments/assets/064e1b58-f328-4816-9f1c-b1cab9c012cf)



<p>I was able to complete this CTF with the guidance of a walkthrough:  thank you!<br>
https://github.com/siunam321/CTF-Writeups/tree/main/TryHackMe/Road</p>

<br>
<br>

![image](https://github.com/user-attachments/assets/14ccaebb-80be-4bba-b47f-4be57e66e4e7)

<br>

![image](https://github.com/user-attachments/assets/4daed7fd-3fd6-4457-9b74-d884ba40cdb5)


<br>
<br>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{My TryHackMe Journey}}$$</h1>


<div align="center">

| Date<br>          |  Streak<br>|   All Time<br>Global   |   All Time<br>Brazil |  Monthly<br>Global   |  Monthly<br>Brazil   |  SHOGUN<br>points  |   Rooms<br>completed  |  Badges<br> |
| :---------------: | :--------: | :--------------------: | :------------------: | :------------------: | :------------------: | :----------------: | :-------------------: | :---------: |
| May 25, 2025      |     384    |          212nd         |            4ᵗʰ       |        159ᵗʰ         |           3ʳᵈ        |       104,721      |             748      |    62       |

</div>

<p align="center"> Global All Time: 212nd <br><img width="300px" src="https://github.com/user-attachments/assets/139e5a09-f4d0-4ec5-b438-0a3f5ecc0c64" alt="Your Image Badge"><br>
                                              <img width="1000px" src="https://github.com/user-attachments/assets/0a042acf-bf40-4ec1-bb42-9966982e81c1"><br><br>
                   Brazil All Time:   4ᵗʰ<br><img width="1000px" src="https://github.com/user-attachments/assets/3b251328-3675-4fdb-893c-46e42e054401"><br><br>
                   Global monthly:    159ᵗʰ<br><img width="1000px" src="https://github.com/user-attachments/assets/89a74605-d9d0-4307-945c-39e405b4abb7"><br><br>
                   Brazil monthly:   3ʳᵈ<br><img width="1000px" src="https://github.com/user-attachments/assets/88eb4868-40dc-45a2-891b-09ddb9ea0d4d"><br><br>
Weekly League, Dimaond:   15ᵗʰ<br><img width="300px" src="https://github.com/user-attachments/assets/e41fa027-eba9-4e19-b0ab-aaad783db5ff"><br>
	                          <img width="1000px" src="https://github.com/user-attachments/assets/bb32913a-938f-4e38-b95d-e4a1fff8b0f0"><br><br><br></p>


<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Thanks for coming!}}$$</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 
