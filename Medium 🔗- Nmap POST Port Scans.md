<h3> Welcome to the <em>TryHackMe ...</em></h3>

<h1>Jr Penetration Tester learning path> Network Security</h1>
<h2>Nmap Post Port Scans</h2>
<p>Learn how to leverage Nmap for service and OS detection, use Nmap Scripting Engine (NSE), and save the results.</p>
<p>2025, May 31</p>

<div style="display: flex; justify-content: center; align-items: center;">
    <img src="https://github.com/user-attachments/assets/6b9fe713-660d-4b02-a8c1-223ebbeb5e3b" width="150px" height="150px"/>
</div>
<br>

![image](https://github.com/user-attachments/assets/8d219eef-44b2-41a3-b045-4c2f4f5240f3)



<p>Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure. It´s key part of my 25-day-streak in <a href="https://www.wicys.org/benefits/security-training-scholarship/">WiCyS SANS Security Training</a> Stage 2 Program. Let´s get started!!<br><br>
Access this TryHackMe Room clicking <a href="https://tryhackme.com/r/room/nmap04">Nmap Post Port Scans</a></p>

<h2>Task 1 - Introduction</h2>

<p>This room is the last in the Nmap series (part of the Introduction to Network Security module). In this room, we focus on the steps that follow port-scanning: in particular, service detection, OS detection, Nmap scripting engine, and saving the scan results.<br>
<ol type="1. ">
    <li><a href="https://tryhackme.com/r/room/nmap01">Nmap Live Host Discover</a></li>
    <li><a href="https://tryhackme.com/r/room/nmap02">Nmap Basic Port Scans</a></li>
    <li><a href="https://tryhackme.com/r/room/nmap03">Nmap Advanced Port Scans</a></li>
    <li><a href="https://tryhackme.com/r/room/nmap04">Nmap Post Port Scans</a></li>
</ol></p>
<p>In the first room of this series, we have learned how Nmap can enumerate targets, discover live hosts, and use reverse-DNS to find interesting names. The second and third rooms of the series focused on the basic and advanced types of scans for network ports.<br><br>
In the last room, as shown in the figure below, we focus on how Nmap can be used to:</p>
<ol type="1. ">
  <li>Detect versions of the running services (on all open ports)</li>
  <li>Detect versions of the running services (on all open ports)</li>
  <li>Run Nmap’s traceroute</li>
  <li>Run select Nmap scripts</li>
  <li>Save the scan results in various formats</li>
</ol></p>

![image](https://github.com/user-attachments/assets/402c010d-a03f-4d84-a0d5-1c384077ff95)


<p>This room will focus on these steps and how to execute them after the port scan.</p>

> 1.1 - <em>Ensure you have a solid understanding of how the Nmap scan progresses and the steps and stages it follows. Launch the AttackBox by using the Start AttackBox button, as you will need it to answer the questions in later tasks.</em><br>
>> <strong>No answer needed</strong><br>
<p><br></p>

<h2>Task 2 - Service Detection</h2>

<pre><code>$ nmap -sV --version-light 10.10.9.70

Starting Nmap 7.60 ( https://nmap.org ) at 2024-10-24 02:20 BST
Nmap scan report for ip-10-10-9-70.eu-west-1.compute.internal (10.10.9.70)
Host is up (0.0064s latency).
Not shown: 992 closed ports
PORT    STATE SERVICE  VERSION
22/tcp  open  ssh      OpenSSH 9.2p1 Debian 2+deb12u3 (protocol 2.0)
25/tcp  open  smtp     Postfix smtpd
80/tcp  open  http     nginx 1.22.1
110/tcp open  pop3     Dovecot pop3d
111/tcp open  rpcbind
143/tcp open  imap     Dovecot imapd
993/tcp open  ssl/imap Dovecot imapd
995/tcp open  ssl/pop3 Dovecot pop3d
MAC Address: 02:B2:32:44:5A:57 (Unknown)
Service Info: Host:  debra2.thm.local; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 14.88 seconds
</code></pre>

> 2.1 - <em>Start the target machine for this task and launch the AttackBox. Run nmap -sV --version-light 10.10.9.70via the AttackBox. What is the detected version for port 143?</em><br>
>> <strong>Docevot impad</strong><br>
<p><br></p>

> 2.2 - <em>Which service did not have a version detected with --version-light? </em><br>
>> <strong>rpcbind</strong><br>
<p><br></p>

<h2>Task 3 - OS Detection and Traceroute</h2>

> 3.1 - <em>Run nmap with -O option against 10.10.9.70. What OS did Nmap detect?</em><br>
>> <strong>Docevot impad</strong><br>
<p><br></p>

<pre><code>$ nmap -O 10.10.9.70

Starting Nmap 7.60 ( https://nmap.org ) at 2024-10-24 02:29 BST
Nmap scan report for ip-10-10-9-70.eu-west-1.compute.internal (10.10.9.70)
Host is up (0.0011s latency).
Not shown: 992 closed ports
PORT    STATE SERVICE
22/tcp  open  ssh
25/tcp  open  smtp
80/tcp  open  http
110/tcp open  pop3
111/tcp open  rpcbind
143/tcp open  imap
993/tcp open  imaps
995/tcp open  pop3s
MAC Address: 02:B2:32:44:5A:57 (Unknown)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.60%E=4%D=10/24%OT=22%CT=1%CU=41787%PV=Y%DS=1%DC=D%G=Y%M=02B232%
OS:TM=6719A2F7%P=x86_64-pc-linux-gnu)SEQ(SP=101%GCD=1%ISR=10C%TI=Z%CI=Z%TS=
OS:A)SEQ(SP=100%GCD=1%ISR=10C%TI=Z%CI=Z%II=I%TS=A)OPS(O1=M2301ST11NW7%O2=M2
OS:301ST11NW7%O3=M2301NNT11NW7%O4=M2301ST11NW7%O5=M2301ST11NW7%O6=M2301ST11
OS:)WIN(W1=F4B3%W2=F4B3%W3=F4B3%W4=F4B3%W5=F4B3%W6=F4B3)ECN(R=Y%DF=Y%T=40%W
OS:=F507%O=M2301NNSNW7%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS%RD=0%Q=)T2(R=
OS:N)T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5(R=Y%DF=Y%T=40%W=
OS:0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T
OS:7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=N%T=40%IPL=164%UN
OS:=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%CD=S)

Network Distance: 1 hop

OS detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 15.71 seconds
</code></pre>

![image](https://github.com/user-attachments/assets/510e88fa-5ef7-4a09-a763-d5f398bea21f)


<h2>Task 4 - Nmap Scripting Engine (NSE)</h2>

> 4.1 - <em>Knowing that Nmap scripts are saved in /usr/share/nmap/scripts on the AttackBox. What does the script http-robots.txt check for?</em><br>
>> <strong>disallowed entries</strong><br>
<p><br></p>

<pre><code>$ cat http-robots.txt.nse
    local http = require "http"
local nmap = require "nmap"
local shortport = require "shortport"
local strbuf = require "strbuf"
local table = require "table"

description = [[
Checks for disallowed entries in <code>/robots.txt</code> on a web server.

The higher the verbosity or debug level, the more disallowed entries are shown.
]]

---
--@output
-- 80/tcp  open   http    syn-ack
-- |  http-robots.txt: 156 disallowed entries (40 shown)
-- |  /news?output=xhtml& /search /groups /images /catalogs
-- |  /catalogues /news /nwshp /news?btcid=*& /news?btaid=*&
-- |  /setnewsprefs? /index.html? /? /addurl/image? /pagead/ /relpage/
-- |  /relcontent /sorry/ /imgres /keyword/ /u/ /univ/ /cobrand /custom
-- |  /advanced_group_search /googlesite /preferences /setprefs /swr /url /default
-- |  /m? /m/? /m/lcb /m/news?
...
</code></pre>

> 4.2 - <em>Can you figure out the name for the script that checks for the remote code execution vulnerability MS15-034 (CVE2015-1635)?</em><br>
>> <strong>http-vuln-cve2015-1635</strong><br>
<p><br></p>

![image](https://github.com/user-attachments/assets/0b459a92-6f31-4c6c-ba03-aa5606ea1fbf)


> 4.3 - <em>Launch the AttackBox if you haven't already. After you ensure you have terminated the VM from Task 2, start the target machine for this task. On the AttackBox, run Nmap with the default scripts -sC against 10.10.83.27. You will notice that there is a service listening on port 53. What is its full value?<br>
</strong><br> 9.18.28-1~deb12u2-Debian</strong><br>
<p><br></p>

<pre><code>$nmap -sC 10.10.83.27

Starting Nmap 7.60 ( https://nmap.org ) at 2024-10-24 02:53 BST
Nmap scan report for ip-10-10-83-27.eu-west-1.compute.internal (10.10.83.27)
Host is up (0.0039s latency).
Not shown: 991 closed ports
PORT    STATE SERVICE
22/tcp  open  ssh
25/tcp  open  smtp
|_smtp-commands: debra2.thm.local, PIPELINING, SIZE 10240000, VRFY, ETRN, STARTTLS, ENHANCEDSTATUSCODES, 8BITMIME, DSN, CHUNKING, 
| ssl-cert: Subject: commonName=debra2.thm.local
| Not valid before: 2021-08-10T12:10:58
|_Not valid after:  2031-08-08T12:10:58
|_ssl-date: TLS randomness does not represent time
53/tcp  open  domain
| dns-nsid: 
|_  bind.version: 9.18.28-1~deb12u2-Debian
80/tcp  open  http
|_http-title: Welcome to nginx on Debian!
110/tcp open  pop3
|_pop3-capabilities: PIPELINING SASL AUTH-RESP-CODE STLS CAPA RESP-CODES TOP UIDL
| ssl-cert: Subject: commonName=debra2.thm.local
| Not valid before: 2021-08-10T12:10:58
|_Not valid after:  2031-08-08T12:10:58
111/tcp open  rpcbind
| rpcinfo: 
|   program version   port/proto  service
|   100000  2,3,4        111/tcp  rpcbind
|_  100000  2,3,4        111/udp  rpcbind
143/tcp open  imap
...
</code></pre>

> 4.4 - <em>Based on its description, the script ssh2-enum-algos “reports the number of algorithms (for encryption, compression, etc.) that the target SSH2 server offers.” What is the name of the server host key algorithm that relies on SHA2-512 and is supported by 10.10.83.27?<br>
</strong><br>rsa-sha2-512</strong><br>
<p><br></p>


<pre><code>$nmap --script ssh2-enum-algos 10.10.83.27
    
Starting Nmap 7.60 ( https://nmap.org ) at 2024-10-24 02:58 BST
Nmap scan report for ip-10-10-83-27.eu-west-1.compute.internal (10.10.83.27)
Host is up (0.0063s latency).
Not shown: 991 closed ports
PORT    STATE SERVICE
22/tcp  open  ssh
| ssh2-enum-algos: 
|   kex_algorithms: (11)
|       sntrup761x25519-sha512@openssh.com
|       curve25519-sha256
|       curve25519-sha256@libssh.org
|       ecdh-sha2-nistp256
|       ecdh-sha2-nistp384
|       ecdh-sha2-nistp521
|       diffie-hellman-group-exchange-sha256
|       diffie-hellman-group16-sha512
|       diffie-hellman-group18-sha512
|       diffie-hellman-group14-sha256
|       kex-strict-s-v00@openssh.com
|   server_host_key_algorithms: (4)
|       rsa-sha2-512
|       rsa-sha2-256
|       ecdsa-sha2-nistp256
|       ssh-ed25519
|   encryption_algorithms: (6)
|       chacha20-poly1305@openssh.com
|       aes128-ctr
|       aes192-ctr
|       aes256-ctr
|       aes128-gcm@openssh.com
|       aes256-gcm@openssh.com
...
</code></pre>


<h2>Task 5 - Saving th Output</h2>

<p>Terminate the target machine of the previous task and start the target machine for this task. On the AttackBox terminal, issue the command scp pentester@10.10.83.27:/home/pentester/* . to download the Nmap reports in normal and grepable formats from the target virtual machine.<br><br>

Note that the username pentester has the password THM17577</p>

> 5.1- <em>Check the attached Nmap logs. How many systems are listening on the HTTPS port?<br>
</strong><br>3</strong><br>
<p><br></p>

<pre><code>$ ssh pentester@10.10.129.43
The authenticity of host '10.10.129.43 (10.10.129.43)' can't be established.
ECDSA key fingerprint is SHA256:kcGwJEX39K8gePz3uvXXJ53uiW+0hg9f8TF+WuIN/v0.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '10.10.129.43' (ECDSA) to the list of known hosts.
pentester@10.10.129.43's password: 
Linux ip-10-10-129-43 6.1.0-23-amd64 #1 SMP PREEMPT_DYNAMIC Debian 6.1.99-1 (2024-07-15) x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Tue Sep 14 09:52:04 2021 from 10.20.30.1
pentester@ip-10-10-129-43:~$ 
</code></pre>

<p></p>

<code><pre> pentester@ip-10-10-129-43:~$ ls -la
total 56
drwxr-xr-x 2 pentester pentester  4096 Sep 14  2021 .
drwxr-xr-x 5 root      root       4096 Oct 24 03:07 ..
-rw-r--r-- 1 pentester pentester   220 Sep 14  2021 .bash_logout
-rw-r--r-- 1 pentester pentester  3515 Sep 14  2021 .bashrc
-rw-r--r-- 1 pentester pentester   675 Sep 14  2021 .profile
-rw-r--r-- 1 pentester pentester 13198 Sep 14  2021 scan_172_17_network.gnmap
-rw-r--r-- 1 pentester pentester 16916 Sep 14  2021 scan_172_17_network.nmap
pentester@ip-10-10-129-43:~$ grep https scan_172_17_network.gnmap
Host: 172.17.0.215 ()	Ports: 22/closed/tcp//ssh///, 80/open/tcp//http///, 443/open/tcp//https///	Ignored State: filtered (997)
Host: 172.17.19.249 ()	Ports: 22/open/tcp//ssh///, 53/open/tcp//domain///, 80/open/tcp//http///, 443/open/tcp//https///	Ignored State: closed (996)
Host: 172.17.23.240 ()	Ports: 22/closed/tcp//ssh///, 80/open/tcp//http///, 443/open/tcp//https///	Ignored State: filtered (997)
</code></pre>

> 5.2- <em>What is the IP address of the system listening on port 8089?<br>
</strong><br>172.17.20.147</strong><br>
<p><br></p>

</code></pre>
pentester@ip-10-10-129-43:~$ grep 8089 scan_172_17_network.gnmap
Host: 172.17.20.147 ()	Ports: 22/open/tcp//ssh///, 8000/open/tcp//http-alt///, 8089/open/tcp//unknown///	Ignored State: closed (997)
</code></pre>

<h2>Task 6 - Summary</h2>

> 6.1 - <em>This room concludes the Nmap series of 4 rooms. Ensure you have taken note of all the Nmap options explained in this room and previous ones.<br>
</strong><br>No answer needed</strong><br>
<p><br></p>

<h2>Room Complete</h2>

![image](https://github.com/user-attachments/assets/2e0db498-f2fe-4c41-9125-11b2620dfcce)
