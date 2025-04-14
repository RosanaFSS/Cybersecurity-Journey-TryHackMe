<p align="center">April 14, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{343}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="300px" src="" alt="Your Image Badge"><br>
<img width="200px" src="https://github.com/user-attachments/assets/4fe1cc18-807a-4b4f-8db2-7dc5f7c421ba"></p>
<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Anonymous Playground}}$$</h1>
<p align="center"><em>Want to become part of Anonymous?<br> They have a challenge for you. Can you get the flags and become an operative?</em><br>
 It is classified as a hard-level CTF.<br>
You can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed.<br>
Can be accessed clicking  <a href="https://tryhackme.com/room/anonymousplayground">here</a>.</p>

<p align="center"> <img width="900px" src="> </p>

<br>
<br>

<h2>Task 1 . Prove Yourself </h2>

<p>[  Start Machine  ]</p>

<p>
<em>Also credit goes to Sq00ky for the super special idea found in the initial foothold stage (not going to give any
spoilers away!)</em><br>

Please allow 3-5 minutes for the box to fully deploy once you hit the "Deploy" button.<br>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 1.1. <em>User 1 Flag.</em>Hint : <em>You're going to want to write a Python script for this. 'zA' = 'a'</em><br><a id='1.1'></a>
>> <strong><code>9184177ecaa83073cbbf36f1414cc029</code></strong><br>
<p></p>

<br>

<br>

> 1.2. <em>User 2 Flag.</em><br><a id='1.2'></a>
>> <strong><code>69ee352fb139c9d0699f6f399b63d9d7</code></strong><br>
<p></p>

<br>

<br>

> 1.3. <em>Root Flag.</em><br><a id='1.3'></a>
>> <strong><code>____</code></strong><br>
<p></p>

<br>
<br>
<br>

<br>

<p>Used <code>nmap</code>.<br>
Discovered:<br>
-  two ports open: <code>22/ssh</code> and  <code>80/http</code>.<br>
-  <code>http-robots.txt: 1 disallowed entry </code>.<br>
-  an endpoint <code>|/zYdHuAKjP</code></br>
-  <code>|_http-title: Proving Grounds</code></p>


```bash
:~/AnonymousPlayground# nmap -sC -sV -sS -Pn -A -p- -T4 TargetIP
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
...
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
| http-robots.txt: 1 disallowed entry 
|_/zYdHuAKjP
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Proving Grounds
...
```

<br>

<p>Used <code>nmap</code> again in order to enumerate http.</p>
Discovered:<br>
-  <code>/robots.txt</code><br>
-  <code>/css/</code></br>
-  <code>/images</code><br>
-  <code>/js</code><br>
</p>

<br>

```bash
:~/AnonymousPlayground# nmap -sV --script=http-enum -A TargetIP
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
| http-enum: 
|   /robots.txt: Robots file
|   /css/: Potentially interesting directory w/ listing on 'apache/2.4.29 (ubuntu)'
|   /images/: Potentially interesting directory w/ listing on 'apache/2.4.29 (ubuntu)'
|_  /js/: Potentially interesting directory w/ listing on 'apache/2.4.29 (ubuntu)'
|_http-server-header: Apache/2.4.29 (Ubuntu)
```

<br>

<p>Added <code>TargetIP</code> and a domain name to <code>etc/hosts</code>.</p>

<br>

<p>Navigated to <code>http://TargetIP</code>.<br>
Discovered a <code>script</code>.</p>
<br>

![image](https://github.com/user-attachments/assets/b777a1cf-20f3-4835-8c68-a2d984221c35)

<br>

<p>Viewed page source.<br>
Discovered an <code>access</code> cookie with a <code>Value</code> field as <code>denied</code>.</p>

<br>

![image](https://github.com/user-attachments/assets/833214d3-dfae-4a01-8cb5-b500aa304e7a)


<br>

<p>Navigated to<code>http://TargetIP/robots.txt</code>.<br>
Confirmed the endpoint discovered in the first nmap.</p>

<br>

![image](https://github.com/user-attachments/assets/0176a7ce-b3b1-4a98-bdd8-540ef0192761)

<br>


<p>Navigated to <code>http://TargetIP/zYdHuAKjP</code>.<br>
Saved <code>granted</code> instead of <code>denied</code> and refreshed the webpage.<br><br>
Discovered something that might have the format <code>user</code>::<code>password</code>.<br><br>
Which user? Which password?<br><br>
Read the hint: <code>You're going to want to write a Python script for this. 'zA' = 'a'</code>.</p>

<br>

![image](https://github.com/user-attachments/assets/4e6dc7dd-1d48-41ce-8a63-79be69dba928)

<br>

```bash
hEzAdCfHzA::hEzAdCfHzAhAiJzAeIaDjBcBhHgAzAfHfN
```

<br>

<p>Wrote a script named <code>discovery.py</code>.</p>

```bash
cipher = "zA"
print("Cipher:", cipher)

firstchar  = cipher[0]
secondchar = cipher[1]
needed     = (ord(firstchar)+(ord(secondchar)%65)+1)
print("Needed :", needed) 
a =chr(needed) 
print("Final :",a)

```

<br>

<p>Ran the script.</p>

<br>

![image](https://github.com/user-attachments/assets/1c0e04f0-f149-4b06-8f31-985c2406d0dc)

<br>

<p>Since my Python skills are basic, I changed the previous script to analyze a pair of characters per round.<br>
Ran it.</p>

<br>

```bash
cipher =  input("Hey!  Please entre 2 characters: ")
print("Cipher:", cipher)

firstchar  = cipher[0]
secondchar = cipher[1]
needed     = (ord(firstchar)+(ord(secondchar)%65)+1)
print("Needed :", needed) 
a =chr(needed)
print("Final :",a)
```

<br>


![image](https://github.com/user-attachments/assets/a194b3de-f214-4ba0-9db2-13e542b597b1)


<br>

<p>Identified previously <code>hEzAdCfHzA::hEzAdCfHzAhAiJzAeIaDjBcBhHgAzAfHfN</code>code>.<br><br>
Discovered <code>hE zA dC fH zA</code>  -----  <code>m { g n {<br></code>.<br><br>
Discovered <code>hE zA dC fH zA   hA iJ   zA eI    aD jB cB hH gA zA fH fN</code> ----- <code>m { g n {   i s   { n    e l e p h { n t</code>.<br><br>
I am guessing <code>{</code> is <code>a</code>. <br><br>
Let´s keep analysing!</p>

<br>

<p>Navigated to <code>http://TargetIP/operatives.php</code>.<br>
It looks like name of team members.</p>

<br>

![image](https://github.com/user-attachments/assets/91f5726c-6998-4ea3-9947-a58853750c36)


<p>8:-)<br><br>
There is <code>magna</code> among the list!<br><br>
So ...<code>magna::magnaisanelephant</code>.<br><br>
Credentials!</p>

<br>


![image](https://github.com/user-attachments/assets/91f5726c-6998-4ea3-9947-a58853750c36)

<br>

<p>Saved it.</p>

```bash
themayor
spooky
darkstar
akaelite
ninja
w0rmer
nameless0ne
0day
szymex
ma1ware
paradox
bee
iamwill
jammy
magna
cryillic
skidy
naughty
thealchemist
itsunda
```

<br>





<br>






![image](https://github.com/user-attachments/assets/547696de-3cf5-4791-afa4-ff5182e6aeb1)

![image](https://github.com/user-attachments/assets/956199b1-7288-4058-b9c6-633733241a78)


---


![image](https://github.com/user-attachments/assets/eef4c330-b464-4668-b0ef-494fdbf67a0c)

![image](https://github.com/user-attachments/assets/6ed2d642-0ca5-467d-9045-09f241b93c6d)

![image](https://github.com/user-attachments/assets/4b010762-1831-4d90-b059-48646ac784dd)


















