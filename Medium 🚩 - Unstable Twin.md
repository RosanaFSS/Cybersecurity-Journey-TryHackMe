<p>June 26, 2025</p>
<h1>Unstable Twin</h1>
<p>A Services based room, extracting information from HTTP Services and finding the hidden messages.</p>

<br>

<h2>Task 1 . Unstable Twin</h2>
<p>Based on the Twins film, find the hidden keys.

Julius and Vincent have gone into the SERVICES market to try and get the family back together.<br>
They have just deployed a new version of their code, but Vincent has messed up the deployment!<br>

Can you help their mother find and recover the hidden keys and bring the family and girlfriends back together?</p>

<p>1.1. What is the build number of Vincent's server?<br>
<code></code></p>

<br>

<p>1.2. What is the build number of Vincent's server?<br>
<code></code></p>

<br>

<p>1.2. What is the build number of Vincent's server?<br>
<code></code></p>


<br>

<p>1.3. How many users are there?<br>
<code></code></p>


<br>

<p>1.4. <p>What colour is Vincent?<br>
<code></code></p>

<br>

<p>1.5. <p>What is Mary Ann's SSH password<br>
<code></code></p>

<br>

<p>1.6. <p>User Flag<br>
<code></code></p>

<br>

<p>1.7. <p>Final Flag<br>
<code></code></p>

<br>
<br>

<h3>nmap</h3>

```bash
:~# nmap -sC -sV -O -A -p- -T4 TargetIP
...
PORT      STATE SERVICE   VERSION
22/tcp    open  ssh       OpenSSH 7.6p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
...
80/tcp    open  http      Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Did not follow redirect to http://cybercrafted.thm/
25565/tcp open  minecraft Minecraft 1.7.2 (Protocol: 127, Message: ck00r lcCyberCraftedr ck00rrck00r e-TryHackMe-r  ck00r, Users: 0/1)
...
```

```bash
:~# nmap -sC -sV -O -A -p- -T4 TargetIP
...
PORT      STATE SERVICE   VERSION
22/tcp    open  ssh       OpenSSH 7.6p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
...
80/tcp    open  http      Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Did not follow redirect to http://cybercrafted.thm/
25565/tcp open  minecraft Minecraft 1.7.2 (Protocol: 127, Message: ck00r lcCyberCraftedr ck00rrck00r e-TryHackMe-r  ck00r, Users: 0/1)
...
```
