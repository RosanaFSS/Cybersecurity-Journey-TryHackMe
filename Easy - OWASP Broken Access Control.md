March 10, 2025, Day 308<br>

<h2>Broken Access Control</h2>
<p>Exploit Broken Access Control: Number 1 of the Top 10 web security risks.</p>

<br>


<h2>Task 3 . Deploy the Machine</h2>

<p>Added Target_IP and a domain name into <code>/etc/hosts</code>.<br>
Visited <code>http://Target_IP</code>.</p>

![image](https://github.com/user-attachments/assets/fd773358-d96b-403f-9813-f3f53bb3f06f)

<br>

<h2>Task 4 . Acessing the Web Application</h2>

<p>Used <code>nmap</code></p>

```bash
:~/BrokenAccessControl# nmap -sC -sV -sS -Pn -p- -T4 bac.thm
Starting Nmap 7.80 ( https://nmap.org ) at 2025-03-11 02:20 GMT
Nmap scan report for bac.thm (10.10.235.10)
Host is up (0.0066s latency).
Not shown: 65531 closed ports
PORT     STATE SERVICE   VERSION
22/tcp   open  ssh       OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http      Apache httpd 2.4.38 ((Debian))
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-server-header: Apache/2.4.38 (Debian)
|_http-title: Welcome to VulnerableApp
443/tcp  open  ssl/https Apache/2.4.38 (Debian)
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|       secure flag not set and HTTPS in use
|_      httponly flag not set
|_http-server-header: Apache/2.4.38 (Debian)
|_http-title: Welcome to VulnerableApp
3306/tcp open  mysql?
| fingerprint-strings: 
|   DNSStatusRequestTCP: 
|     8.0.32
|     l2IF%AQC
|     ;N!tM
|     mysql_native_password
|     #08S01Got packets out of order
|   DNSVersionBindReqTCP: 
|     8.0.32
|     lP^Y.f0(
|     mysql_native_password
|     #08S01Got packets out of order
|   GenericLines: 
|     8.0.32
|     ./}xt
|     mysql_native_password
|     #08S01Got packets out of order
|   GetRequest: 
|     8.0.32
|     >>#C.>(
|     u?iR@H Ip
|     mysql_native_password
|     #08S01Got packets out of order
|   HTTPOptions: 
|     8.0.32
|     ;UEW
|     ai/@
|     mysql_native_password
|     #08S01Got packets out of order
|   Help: 
|     8.0.32
|     ">I`W
|     /e=K,{
|     mysql_native_password
|     #08S01Got packets out of order
|   NULL: 
|     8.0.32
|     ./}xt
|     mysql_native_password
|   RPCCheck: 
|     8.0.32
|     L&<'V
|     u0A/&9
|     mysql_native_password
|     #08S01Got packets out of order
|   RTSPRequest: 
|     8.0.32
|     FMP4R!>
|     ,dD'
|     mysql_native_password
|     #08S01Got packets out of order
|   SSLSessionReq: 
|     8.0.32
|     `=#%?0p
|     Zaf<
|     mysql_native_password
|_    #08S01Got packets out of order
| mysql-info: 
|   Protocol: 10
|   Version: 8.0.32
|   Thread ID: 46
|   Capabilities flags: 65535
|   Some Capabilities: LongPassword, SupportsCompression, InteractiveClient, LongColumnFlag, ConnectWithDatabase, IgnoreSigpipes, FoundRows, Support41Auth, SupportsLoadDataLocal, SupportsTransactions, DontAllowDatabaseTableColumn, SwitchToSSLAfterHandshake, Speaks41ProtocolNew, IgnoreSpaceBeforeParenthesis, ODBCClient, Speaks41ProtocolOld, SupportsMultipleResults, SupportsAuthPlugins, SupportsMultipleStatments
|   Status: Autocommit
|   Salt: '\4MmnP\x13J3sHWWz\qTny
|_  Auth Plugin Name: mysql_native_password
...
```

<p>What is the type of server that is hosting the web application? This can be found in the response of the request in Burp Suite.</p>
<code>Apache</code><br>

<p>Created an account.<br>
Notice that I was redirected to <code>http://Target_IP/login.php?result=Registration successful</code></p>

![image](https://github.com/user-attachments/assets/0d6fadc3-1c62-4d3a-9c1a-b7cf0b71931c)

<br>


![image](https://github.com/user-attachments/assets/66849ede-642a-43c1-a621-677fa491fbb6)

<br>

<p>Logged in.</p>

![image](https://github.com/user-attachments/assets/4d8e726d-7fab-4398-84d9-ea654acead6c)

<p>Obtained access to a dashboard.</p>


![image](https://github.com/user-attachments/assets/e5014748-64c5-4005-af1e-d2a0356e8b87)

<br>

<p>Logged out.</p>

<p>Launched <code>Burp Suite</code>.</p>
<p>Enabled <code>FoxProxy</code>.</p>
<p>Logged in.</p>
<p>Inspected the <code>Response</code> of <code>Burp Suite</code>´s interception, and discovered the <code>server</code> type.<br>
In the output of <code>nmap</code> scan we can also visualize it.</p>

![image](https://github.com/user-attachments/assets/4b560bd3-db7b-403d-ae35-dbe3015c501d)


<p>Used <code>nmap</code></p>

```bash

...
```


''''
''''




