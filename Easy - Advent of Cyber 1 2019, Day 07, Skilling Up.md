<p align="center">November 28, 2024</p>
<p align="center">Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{206}}$$-day-streak in  <a href="https://tryhackme.com/r/hacktivities">TryHackMe</a>.</p>

<h1 align="center">
  $$\textcolor{#3bd62d}{\textnormal{Advent of Cyber 1 [2019], [Day 7] Skilling Up}}$$

</h1>
<p align="center">Get started with Cyber Security in 25 Days - Learn the basics by doing a new, beginner friendly security challenge every day leading up to Christmas.</p>
<p align="center">Access this 🆓 TryHackMe CTF Room clicking <a href="https://tryhackme.com/r/room/25daysofchristmas">Advent of Cyber 1 [2019]</a>.</p><br>
<p align="center">
  <img height="150px" hspace="20" src="https://github.com/user-attachments/assets/f59c6a13-447f-4f2a-ade0-a28bc0f05118">
  <img height="150px" src="https://github.com/user-attachments/assets/7a3dd02f-39d7-4e1e-b64d-e0ec60bdb2f2">

</p>

<h2>[Day 7] Skilling Up<a id='1'></a></h2>
<p>Previously, we saw mcsysadmin learning the basics of Linux. With the on-going crisis, McElferson has been very impressed and is looking to push mcsysadmin to the security team. One of the first things they have to do is look at some strange machines that they found on their network.<br>

Check out the supporting material here.</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

> 1.1. <em>How many TCP ports under 1000 are open?</em><br><a id='1.1'></a>
>> <code><strong>3</strong></code>

<br>

<pre><code>root@ip-[THM AttackBox]:~/AdventOfCyber# nmap -p1-1000 -A day7.thm
Starting Nmap 7.80 ( https://nmap.org ) at 2024-11-28 04:14 GMT
Nmap scan report for day7.thm ([Target])
Host is up (0.00042s latency).
Not shown: 997 closed ports
PORT    STATE SERVICE VERSION
22/tcp  open  ssh     OpenSSH 7.4 (protocol 2.0)
| ssh-hostkey: 
...
111/tcp open  rpcbind 2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100024  1          38797/udp6  status
|   100024  1          39741/tcp6  status
|   100024  1          45433/udp   status
|_  100024  1          52553/tcp   status
999/tcp open  http    SimpleHTTPServer 0.6 (Python 3.6.12)
|_http-server-header: SimpleHTTP/0.6 Python/3.6.12
|_http-title: Directory listing for /
MAC Address: 02:65:71:20:B5:E1 (Unknown)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
...

Network Distance: 1 hop

TRACEROUTE
HOP RTT     ADDRESS
1   0.42 ms day7.thm ([Target])

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 27.68 seconds
</code></pre><br>

<br>

> 1.2. <em>What is the name of the OS of the host?</em><br><a id='1.2'></a>
>> <code><strong>linux</strong></code>

<br>

<p>No exact OS matches, but nmap indicates.</p>

<pre><code>root@ip-[THM AttackBox]:~/AdventOfCyber# nmap -sV day7.thm -A
Starting Nmap 7.80 ( https://nmap.org ) at 2024-11-28 04:10 GMT
Nmap scan report for day7.thm ([Target])
Host is up (0.00040s latency).
Not shown: 997 closed ports
PORT    STATE SERVICE VERSION
22/tcp  open  ssh     OpenSSH 7.4 (protocol 2.0)
| ssh-hostkey: 
...
111/tcp open  rpcbind 2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100024  1          38797/udp6  status
|   100024  1          39741/tcp6  status
|   100024  1          45433/udp   status
|_  100024  1          52553/tcp   status
999/tcp open  http    SimpleHTTPServer 0.6 (Python 3.6.12)
|_http-server-header: SimpleHTTP/0.6 Python/3.6.12
|_http-title: Directory listing for /
MAC Address: 02:65:71:20:B5:E1 (Unknown)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.80%E=4%D=11/28%OT=22%CT=1%CU=42930%PV=Y%DS=1%DC=D%G=Y%M=026571%
OS:TM=6747ED36%P=x86_64-pc-linux-gnu)SEQ(SP=106%GCD=1%ISR=10B%TI=Z%CI=Z%II=
OS:I%TS=A)OPS(O1=M2301ST11NW7%O2=M2301ST11NW7%O3=M2301NNT11NW7%O4=M2301ST11
OS:NW7%O5=M2301ST11NW7%O6=M2301ST11)WIN(W1=68DF%W2=68DF%W3=68DF%W4=68DF%W5=
OS:68DF%W6=68DF)ECN(R=Y%DF=Y%T=FF%W=6903%O=M2301NNSNW7%CC=Y%Q=)T1(R=Y%DF=Y%
OS:T=FF%S=O%A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=FF%W=0%S=A%A=Z%F=
OS:R%O=%RD=0%Q=)T5(R=Y%DF=Y%T=FF%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T
OS:=FF%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=FF%W=0%S=Z%A=S+%F=AR%O=%RD=
OS:0%Q=)U1(R=Y%DF=N%T=FF%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(
OS:R=Y%DFI=N%T=FF%CD=S)

Network Distance: 1 hop

TRACEROUTE
HOP RTT     ADDRESS
1   0.40 ms day7.thm ([Target])

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 27.76 seconds


</code></pre><br>


<br>

> 1.3. <em>What version of SSH is running?</em><br><a id='1.3'></a>
>> <code><strong>7.4</strong></code>

<br>

![image](https://github.com/user-attachments/assets/9f323a16-603f-47ea-b9f9-e817332a4971)

<br>

> 1.4. <em>What is the name of the file that is accessible on the server you found running?</em><br><a id='1.4'></a>
>> <code><strong>interesting.file</strong></code>

<br>

<pre><code>root@ip-[THM AttackBox]:~/AdventOfCyber# nmap -p1-1000 -A day7.thm
...
999/tcp open  http    SimpleHTTPServer 0.6 (Python 3.6.12)
|_http-server-header: SimpleHTTP/0.6 Python/3.6.12
|_http-title: Directory listing for /
...
</code></pre><br>

<br>

![image](https://github.com/user-attachments/assets/e0b72ff6-da86-4d27-8198-b82a8aa3310e)

<br>

![image](https://github.com/user-attachments/assets/8a7d3f22-8bf6-4931-aeaf-a8d4107504d2)

<br>

![image](https://github.com/user-attachments/assets/17d688ad-e8ea-41b7-9cf8-cf150897e894)

<br>




<h2>Task Complete<a id='2'></a></h2>
<p>Keep learning, keep growing!<br>

<h3 align="center"> <img width="900px" src="https://github.com/user-attachments/assets/83085928-3c6e-473d-bedc-3362cc9ef6d2"> </h3>


<h2>My Journey<a id='3'></a></h2>
<p></p>Following I share the status of my journey in TryHackMe.</p>

<h3 align="center"> <img width="900px" src="https://github.com/user-attachments/assets/6647d0de-9dbe-4fa0-aecf-869c7f9444e7"> </h3>


<p style="text-align: center;">Thank you for coming. Hope to learn together again!!</p>
