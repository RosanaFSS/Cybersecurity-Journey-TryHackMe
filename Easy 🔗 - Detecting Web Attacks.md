


:~/DetectingWebAttacks# nmap 10.201.26.201
Starting Nmap 7.80 ( https://nmap.org ) at 2025-09-11 21:36 BST
mass_dns: warning: Unable to open /etc/resolv.conf. Try using --system-dns or specify valid servers with --dns-servers
mass_dns: warning: Unable to determine any DNS servers. Reverse DNS is disabled. Try using --system-dns or specify valid servers with --dns-servers
Nmap scan report for 10.201.26.201
Host is up (0.00013s latency).
Not shown: 997 closed ports
PORT     STATE SERVICE
22/tcp   open  ssh
80/tcp   open  http
5901/tcp open  vnc-1
MAC Address: 16:FF:D5:A1:BB:BB (Unknown)




:~/DetectingWebAttacks# nmap -sC -sV -Pn -p- -T4 10.201.26.201
Starting Nmap 7.80 ( https://nmap.org ) at 2025-09-11 21:37 BST
mass_dns: warning: Unable to open /etc/resolv.conf. Try using --system-dns or specify valid servers with --dns-servers
mass_dns: warning: Unable to determine any DNS servers. Reverse DNS is disabled. Try using --system-dns or specify valid servers with --dns-servers
Nmap scan report for 10.201.26.201
Host is up (0.00012s latency).
Not shown: 65532 closed ports
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 9.6p1 Ubuntu 3ubuntu13.5 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http    WebSockify Python/3.12.3
| fingerprint-strings: 
|   GetRequest: 
|     HTTP/1.1 405 Method Not Allowed
|     Server: WebSockify Python/3.12.3
|     Date: Thu, 11 Sep 2025 20:37:52 GMT
|     Connection: close
|     Content-Type: text/html;charset=utf-8
|     Content-Length: 355
|     <!DOCTYPE HTML>
|     <html lang="en">
|     <head>
|     <meta charset="utf-8">
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
|     Server: WebSockify Python/3.12.3
|     Date: Thu, 11 Sep 2025 20:37:52 GMT
|     Connection: close
|     Content-Type: text/html;charset=utf-8
|     Content-Length: 360
|     <!DOCTYPE HTML>
|     <html lang="en">
|     <head>
|     <meta charset="utf-8">
|     <title>Error response</title>
|     </head>
|     <body>
|     <h1>Error response</h1>
|     <p>Error code: 501</p>
|     <p>Message: Unsupported method ('OPTIONS').</p>
|     <p>Error code explanation: 501 - Server does not support this operation.</p>
|     </body>
|     </html>
|   RTSPRequest: 
|     <!DOCTYPE HTML>
|     <html lang="en">
|     <head>
|     <meta charset="utf-8">
|     <title>Error response</title>
|     </head>
|     <body>
|     <h1>Error response</h1>
|     <p>Error code: 400</p>
|     <p>Message: Bad request version ('RTSP/1.0').</p>
|     <p>Error code explanation: 400 - Bad request syntax or unsupported method.</p>
|     </body>
|_    </html>
|_http-server-header: WebSockify Python/3.12.3
|_http-title: Error response
5901/tcp open  vnc     VNC (protocol 3.8)
|_ssl-cert: ERROR: Script execution failed (use -d to debug)
|_ssl-date: ERROR: Script execution failed (use -d to debug)
|_sslv2: ERROR: Script execution failed (use -d to debug)
|_vnc-info: ERROR: Script execution failed (use -d to debug)






<h2>Task 4 . Log-Based Detection</h2>




<p><em>Answuer the questions below</em></p>

<p>4.1. What is the attacker´s User-Agent performing the directory fuzz?<br>
<code>FFUF v2.1.0</code></p>

<img width="1074" height="229" alt="image" src="https://github.com/user-attachments/assets/c9adddeb-f166-40a4-b1d4-7bb30866bd78" />

<br>
<p>4.2. What is the name of the page on which the attacker performs a brute-force attack?<br>
</p>

<img width="1075" height="379" alt="image" src="https://github.com/user-attachments/assets/d816791c-c679-41fc-b31d-84d45e90d96f" />

<br>
<p>What is the complete, decoded SQLi payload the attacker uses on the <code>/changeusername.php</code>code> form?<br>
<code>%' OR '1'='1</code></p>

<img width="1073" height="631" alt="image" src="https://github.com/user-attachments/assets/a64e947f-d5d1-4dd6-afda-43cab005807d" />

<br>
<br>

<img width="1360" height="185" alt="image" src="https://github.com/user-attachments/assets/de3fab31-181f-4183-ad0e-28930f54c543" />

<br>
<br>
<h2>Task . 5 Network-Based Detection</h2>


<p><em>Answuer the questions below</em></p>

<p>5.1. What is the attacker´s User-Agent performing the directory fuzz?<br>
<code>astrongpassword123</code></p>

<img width="1389" height="443" alt="image" src="https://github.com/user-attachments/assets/063d3dee-4b96-40cb-8a4f-53ba4699316a" />


<br>
<br>
<p>5.2.What is the flag the attacker found in the database using SQLi?<br>
<code>THM{dumped_the_db}</code></p>

<img width="1379" height="572" alt="image" src="https://github.com/user-attachments/assets/446ad857-7e02-43ab-8430-367e5bff24de" />


<br>
<br>


<h2>Task 6 . Web Application Firewall</h2>




<h3>Rules</h3>



<h3>Integrating Known Indicators and Threat Intelligence</h3>



<p><em>Answuer the questions below</em></p>

<p>6.1. What do WAFs inspect and filter?<br>
<code>Web requests</code></p>


<p>6.2. Create a custom firewall rule to block any <code>User-Agent</code> that matches "<code>BotTHM</code>". Hint: <em> Syntax: IF field-name CONTAINS value THEN action</em><br>
<code>IF User-Agent CONTAINS "BotTHM" THEN block</code></p>

192.168.1.9


<img width="1367" height="292" alt="image" src="https://github.com/user-attachments/assets/471f201c-2e23-4d9c-b855-b84df9ca039b" />

<br>
<br>

<img width="1364" height="318" alt="image" src="https://github.com/user-attachments/assets/7be1b71c-9e7b-4a8e-a485-d952c31f33b5" />

<br>
<br>

<img width="1362" height="287" alt="image" src="https://github.com/user-attachments/assets/7180b38e-7b88-41a9-bd31-b2656109707f" />








