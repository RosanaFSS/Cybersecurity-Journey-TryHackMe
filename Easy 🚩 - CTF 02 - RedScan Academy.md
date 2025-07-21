<h1 align="center">CTF 02 - Redscan Academy</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/91a4c48a-17fd-4eb6-9e1e-d43e74e6f83d"><br>
July 18, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, 
and I’m excited to join you on this adventure, part of my <code>437</code>-day-streak in<a href="https://tryhackme.com">TryHackMe</a>.<br>
<em </em>.<br>
Access it <a href="https://tryhackme.com/room/ctf2redscanacademy">here</a>.<br><br>
<img width="1200px" src=""></p>


<br>

<h2>Task 1 . Enumerationg</h2>
<p>Why is it important? Enumeration reveals the attack surface and helps uncover potential weaknesses that can be exploited later.<br><br>
Welcome to the CTF 02 - RedScan Academy!!!<br><br>
https://www.redscanacademy.com.br/<br><br>
Let´s Play the Game!!!</p>

<h3 align="left"> Answer the questions below</h3>

> 1.1. <em>How many open TCP ports are present opened on the host?</em><br><a id='1.1'></a>
>> <strong><code>5</code></strong><br>
<p></p>

```bash
:~/CTF02RedScanAcademy# nmap -sT -p- TargetIP
...
PORT      STATE SERVICE
21/tcp    open  ftp
80/tcp    open  http
3389/tcp  open  ms-wbt-server
20000/tcp open  dnp
20443/tcp open  unknown
```

<br>

> 1.2. <em>What technology and version are identified on the highest-numbered port?</em><br><a id='1.2'></a>
>> <strong><code>Apache 2.4.34</code></strong><br>
<p></p>

<p>

- <code>  21</code> : ftp<br>
- <code>  80</code> : http<br>
- <code>3389</code> : RDP<br>
- <code>7680</code> : <br>
- <code>20000</code> : DNP<br>
- <code>20443</code> : HTTPS<br>
</p>

```bash
:~/CTF02RedScanAcademy# nmap -sC -sV -Pn -p- -T4 TargetIP
...
PORT      STATE SERVICE       VERSION
21/tcp    open  ftp           Microsoft ftpd
| ftp-syst: 
|_  SYST: Windows_NT
80/tcp    open  http          Microsoft IIS httpd 10.0
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/10.0
|_http-title: DarkPan - Bootstrap 5 Admin Template
3389/tcp  open  ms-wbt-server Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: CTF2-REDSCAN
|   NetBIOS_Domain_Name: CTF2-REDSCAN
|   NetBIOS_Computer_Name: CTF2-REDSCAN
|   DNS_Domain_Name: CTF2-RedScan
|   DNS_Computer_Name: CTF2-RedScan
|   Product_Version: 10.0.19041
|_  System_Time: 2025-07-18Txx:xx:xx+00:00
| ssl-cert: Subject: commonName=CTF2-RedScan
| Not valid before: 2025-07-15Txx:xx:xx
|_Not valid after:  2026-01-14Txx:xx:xx
|_ssl-date: 2025-07-18Txx:xx:xx+00:00; 0s from scanner time.
7680/tcp  open  pando-pub?
20000/tcp open  http          Apache httpd 2.4.34 ((Win32) OpenSSL/1.1.0i PHP/7.2.9)
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Apache/2.4.34 (Win32) OpenSSL/1.1.0i PHP/7.2.9
|_http-title: Drivin - Driving School Website Template
20443/tcp open  http          Apache httpd 2.4.34 ((Win32) OpenSSL/1.1.0i PHP/7.2.9)
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Apache/2.4.34 (Win32) OpenSSL/1.1.0i PHP/7.2.9
|_http-title: Bad request!
```

<br>

> 1.3. <em>What version of PHP is running?</em><br><a id='1.3'></a>
>> <strong><code>PHP/7.2.9</code></strong><br>
<p></p>

<p>Discovered the answer in 1.2.</p>

<br>

> 1.4. <em>What is the name of the admin user logged into the web application on the lowest-numbered port?</em><br><a id='1.4'></a>
>> <strong><code>Jhon Doe</code></strong><br>
<p></p>

<img width="1156" height="419" alt="image" src="https://github.com/user-attachments/assets/36bcd38a-31ba-4d08-b142-cd53d1684141" />

<br>

> 1.5. <em>What sensitive directory was found on website?</em><br><a id='1.5'></a>
>> <strong><code>_______</code></strong><br>
<p></p>

```bash
:~/CTF02RedScanAcademy# nmap -sT -p- TargetIP
...
PORT      STATE SERVICE
21/tcp    open  ftp
80/tcp    open  http
3389/tcp  open  ms-wbt-server
20000/tcp open  dnp
20443/tcp open  unknown
```

<br>

> 1.6. <em>What is the name of the web application that is running?</em><br><a id='1.6'></a>
>> <strong><code>_______</code></strong><br>
<p></p>


```bash
pip3 install html2text


<br>

> 1.7. <em>What information do you receive when trying to log into the lowest port service?</em><br><a id='1.7'></a>
>> <strong><code>_______</code></strong><br>
<p></p>

<br>

<h3>nmap</h3>



