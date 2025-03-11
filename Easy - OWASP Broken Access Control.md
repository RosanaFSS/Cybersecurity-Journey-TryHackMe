March 10, 2025, Day 308<br>

<h2>Broken Access Control</h2>
<p>Exploit Broken Access Control: Number 1 of the Top 10 web security risks.</p>

<br>

![image](https://github.com/user-attachments/assets/9bc9dfea-7267-42b9-9338-70b0c4fcf00c)

<br>

<h2>Task 3 . Deploy the Machine</h2>

<p>Added Target_IP and a domain name into <code>/etc/hosts</code>.<br>
Visited <code>http://Target_IP</code>.</p>

![image](https://github.com/user-attachments/assets/fd773358-d96b-403f-9813-f3f53bb3f06f)

<h4 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h4>
<br>

> 3.1. <em>I have deployed the machine attached to the task.</em><br><a id='1.1'></a>
>> <code><strong>No answer needed</strong></code>

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



<br>

<h4 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h4>
<br>

> 4.1. <em>What is the name of the parameter in the JSON response from the login request that contains a redirect link?</em><br><a id='4.1'></a>
>> <code><strong>redirect_link</strong></code>


<p>Inspected the interception of my login.</p>

![image](https://github.com/user-attachments/assets/f1b24ad3-fee4-44b9-a760-51feaa5d4e18)

<br>

> 4.2. <em>What Burp Suite module allows us to capture requests and responses between ourselves and our target?</em><br><a id='4.2'></a>
>> <code><strong>Proxy</strong></code>



![image](https://github.com/user-attachments/assets/aeeca082-fd92-443b-8cde-5d1b9d88b0e4)

<br>

> 4.3. <em>What is the admin’s email that can be found in the online users’ table?</em><br><a id='4.3'></a>
>> <code><strong>admin@admin.com</strong></code>


![image](https://github.com/user-attachments/assets/c72f4144-4769-4942-a92f-aace2f44985b)

<br>

<h2>Task 5 . Exploiting the Web Application</h2>

<p>Copied the <code>is_admin</code> parameter, and used it in the <code>url</code>. But instead of simply copying, I changed from <code>false</code> to <code>true</code>.</p>

![image](https://github.com/user-attachments/assets/d6bcba96-f6b5-4035-a9c9-bdfbe62a45f5)

<br>

![image](https://github.com/user-attachments/assets/26e6a20f-887c-4998-b566-a8b6fb9b19d8)

<br>



![image](https://github.com/user-attachments/assets/7c0a6b2c-1328-4793-8219-442173130d56)

<br>

![image](https://github.com/user-attachments/assets/32ba754e-b977-426a-b583-2607aed7c215)

<br>



<p>What kind of privilege escalation happened after accessing admin.php?<br>
<code>vertical</code></p>p>

<br>


<p>What parameter allows the attacker to access the admin page?<br>
<code>isadmin</code></p>

<p>What is the flag in the admin page?<br>
<code>THM{I_C4n_3xpl01t_B4c}</code></p>


<h2>Task 6 . Mitigation</h2>


<p>Click me to proceed onto the next task.<br>
<code>No answer needed</code></p>

<br>

<h2>Task 7 . Conclusion</h2>
<p>Broken access control is a security vulnerability that occurs when a system fails to properly enforce access controls, which can result in unauthorized users gaining access to sensitive information or performing actions they are not authorized to do.<br>

Horizontal privilege escalation occurs when a user is able to access data or perform actions that they are not authorized to do within their own privilege level. This can be dangerous because it can allow an attacker who has already gained access to the system to move laterally through the network and access additional resources or sensitive data.<br>

Vertical privilege escalation occurs when a user is able to gain access to data or perform actions that are reserved for users with higher privilege levels, such as system administrators. This can be even more dangerous because it can allow an attacker to gain full control of the system and potentially take over the entire network.<br>

The impact of these types of privilege escalation can vary depending on the specific system and the level of access that is gained. However, in general, the consequences can include unauthorized access to sensitive information, data loss or theft, disruption of critical systems or services, and even complete network compromise. Therefore, it is important to implement strong access controls and regularly monitor for any signs of unauthorized access or activity.<br>

Here are some references that you can give to PHP developers to help them implement these mitigation strategies:<br>
. OWASP PHP Configuration Cheat Sheet<br>
. PHP The Right Way: Security<br>
. Secure Coding in PHP</p>

<br>

<p>Click me to finish this room.<br>
<code>No answer needed</code></p>

<br>

<h2>Room Completed</h2>

![image](https://github.com/user-attachments/assets/8b0771dc-077e-4ad0-83bf-113735a691e3)

<br>

![image](https://github.com/user-attachments/assets/69da413b-865c-4f87-80ab-e2fed3696968)

<br>



<h2>My journey on TryHackMe</h2>

```
308 days streak 🎉 ▪ 86,309 points ▪ 613 rooms completed ▪ 59 badges🎖️
Global ranking:    358ᵗʰ all time    ▪    323ʳᵈ monthly
Brazil ranking:      8ᵗʰ all time    ▪      7ᵗʰ monthly
```

<br>

<p>Global all time ranking: 323ʳᵈ</p>

![image](https://github.com/user-attachments/assets/dad38196-d441-4413-82c2-3d3d2ed381a1)



<br>

<p>Brazil all time ranking: 8ᵗʰ</p>

![image](https://github.com/user-attachments/assets/404cff32-3164-4c5b-a2ec-3ffb81a382a8)


<br>

<p>Global monthly ranking: 381st</p>

![image](https://github.com/user-attachments/assets/439ff06c-6edc-4f18-b472-b7e9d370f928)


<br>

<p>Brazil monthly ranking: 7ᵗʰ</p>

![image](https://github.com/user-attachments/assets/81b85838-1706-499f-aad7-805349923b88)
