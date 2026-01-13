<h1 align="center"><a href="https://tryhackme.com/room/sq2-aoc2025-JxiOKUSD9R">Scheme Catcher</a></h1>
<h3 align="center">Advent of Cyber 2025 &nbsp;|&nbsp; Side Quest</h3>
<p align="center"><img width="1200px" src="   "><br>
If you find it helpful, consider coming back for research.<br><p align="center"><a href="https://github.com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=for-the-badge&logo=github&color=24292e" alt="Follow Rosana on GitHub"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://img.shields.io/badge/COMPLETED-2026%2C%20JAN%2013-444444?style=for-the-badge&logo=calendar-check" alt="Completion Date"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn"></a></p>

<br>
<h2>Task 1 . Introduction</h2>

<h3>The Silent Control System of the Jester</h3>
<p>Once upon a time, before Hopper’s laughter echoed through HopSec Asylum, investigators discovered whispers about a strange server hidden somewhere on his personal systems. No one has actually seen it, no one has managed to access it, and every attempt to break in has failed. The few traces that exist point to a rough and unstable copy of King Malhare’s old command and control setup, rebuilt by Hopper into something twisted and unpredictable. Rumours say the place is scattered with odd folders, stray notes, and several suspicious binaries that seem to pulse with their own rhythm. Hopper is obsessed with building things, changing things, and breaking things just to rebuild them again, and he insists he never commits a single mistake. In his mind, everything he creates is perfect, even if it looks like chaos from the outside.<br>

Stranger still is how the server behaves when anyone approaches. Connections drop without reason. Tasks appear, vanish, and then reappear elsewhere. Logs rewrite themselves. Some scripts reply to commands with messages that feel a little too aware. Hopper calls the place his masterpiece. He says it’s alive. He says it only listens to him.<br>

Whether he planned sabotage, rebellion, or something far stranger remains unknown because no analyst has managed to look inside. All that is certain is that Hopper guards this secret with a wild grin and a mind that slips further away each day. The question is now: Can you prove he is wrong, or get lost in his madness</p>

<h3>Rules</h3>
<p>

- <strong>Do not</strong> share questions or hints, including in videos, streams, or any other medium while the event is running (until Dec 31st).<br>
- Only hack machines deployed in the rooms you have legitimate, authorised access to.<br>
- <code>*.tryhackme.com</code> and VPN servers are off-limits for probing, scanning, or exploiting.<br>
- Teaming up is permitted.<br>

For a more comprehensive list, please read the <a href="https://help.tryhackme.com/en/articles/8537472-advent-of-cyber-2025-terms-and-condition">Advent of Cyber 2025 Terms and Conditions</a>.<br>

This Side Quest is unlocked by finding the Side Quest key in <a href="https://tryhackme.com/room/attacks-on-ecrypted-files-aoc2025-asdfghj123">Advent of Cyber 2025 Day 9</a>. f you have been savvy enough to find it, you can unlock the machine by visiting <code>MACHINE_IP:21337</code> and entering your key. Happy Side Questing!
</p>

<p><em>Answer the questions below</em></p>

<p>

- Navigate to <code>MACHINE_IP:21337</code><br>
- Enter the <strong>Memory Key</strong> discovered in <strong>Advent of Cyber 2025, Day 9</strong><br>
- Click <strong>UNLOCK MEMORIES</strong></p>

<br>
<h1 align="center">Port Scanning<a id='1'></a></h1>

<div align="center"><p>

| **Port**           | **Service**          | **Version**                       |
|-------------------:|:---------------------|:----------------------------------|
| `22`               |`SSH`                 |OpenSSH 9.6p1 Ubuntu 3ubuntu13.11  |
| `80`               |`HTTP`                |Apache httpd 2.4.58                |
| `9004`             |`Unknown`             |-                                  |
| `21337`            |`-`                   |-                                  |

</p></div><br>


```bash
:~# nmap -sC -sV -Pn -n -p- -T4 10.64.168.0
...
PORT      STATE SERVICE VERSION
22/tcp    open  ssh     OpenSSH 9.6p1 Ubuntu 3ubuntu13.11 (Ubuntu Linux; protocol 2.0)
80/tcp    open  http    Apache httpd 2.4.58 ((Ubuntu))
|_http-server-header: Apache/2.4.58 (Ubuntu)
|_http-title: Under Construction
9004/tcp  open  unknown
| fingerprint-strings: 
|   DNSStatusRequestTCP, DNSVersionBindReqTCP, GetRequest, HTTPOptions, Help, JavaRMI, Kerberos, RPCCheck, RTSPRequest, SSLSessionReq, TLSSessionReq, TerminalServerCookie: 
|     Payload Storage Malhare's
|     Version 4.2.0
|     >>Invalid option
|   GenericLines, NULL: 
|     Payload Storage Malhare's
|_    Version 4.2.0
21337/tcp open  unknown
...
```


<br>
<h1 align="center">Directory & File Enumeration<a id='2'></a></h1>


```bash
:~# ffuf -u http://xx.xx.xxx.xx/FUZZ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -mc 200,301 -e .html,.zip,.txt -ic -c -t 60

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.3.1
________________________________________________

 :: Method           : GET
 :: URL              : http://xx.xx.xxx.xx/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
 :: Extensions       : .html .zip .txt 
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 60
 :: Matcher          : Response status: 200,301
________________________________________________

                        [Status: 200, Size: 3455, Words: 1317, Lines: 129]
index.html              [Status: 200, Size: 3455, Words: 1317, Lines: 129]
dev                     [Status: 301, Size: 310, Words: 20, Lines: 10]
:: Progress: [873060/873060] :: Job [1/1] :: 11488 req/sec :: Duration: [0:01:17] :: Errors: 0 ::
```

<img width="1258" height="428" alt="image" src="https://github.com/user-attachments/assets/616f8540-c232-4975-b27e-2c5ebba044f7" />


<br>
<br>
<br>
<h1 align="center">Web Interface Inspection<a id='3'></a></h1>

<img width="1200" height="474" alt="image" src="https://github.com/user-attachments/assets/2c94c5f9-75b1-4437-a396-d8d7e10ea53a" />

<br>
<br>
<br>

<img width="1196" height="267" alt="image" src="https://github.com/user-attachments/assets/e1cff400-1d22-4713-b043-c42d3e0cb597" />

<br>
<br>
<br>

```bash
:~/SchemeCatcher# ls
4.2.0.zip
```

```bash
:~/SchemeCatcher# file 4.2.0.zip
4.2.0.zip: Zip archive data, at least v1.0 to extract
```

```bash
:~/SchemeCatcher# unzip 4.2.0.zip
Archive:  4.2.0.zip
   creating: latest/
  inflating: latest/beacon.bin       
```

<img width="1262" height="156" alt="image" src="https://github.com/user-attachments/assets/c713419a-e734-4693-bd3f-72a18b454431" />

<br>
<br>
<br>

```bash
:~/SchemeCatcher# ls
4.2.0.zip  latest
```

```bash
:~/SchemeCatcher# cd latest
```

```bash
:~/SchemeCatcher/latest# file beacon.bin
beacon.bin: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=6130a2932421dfd5fb7f8034bd8ca749bac01434, for GNU/Linux 3.2.0, not stripped
```

```bash
:~/SchemeCatcher/latest# strings beacon.bin > strings.txt
```


```bash
:~/SchemeCatcher/latest# grep -E THM strings.txt
THM{••••••••••••••••••••••••••••••}
```

<img width="1259" height="86" alt="image" src="https://github.com/user-attachments/assets/827894f4-c327-401d-b184-314969ffdca8" />

<br>
<br>
<br>
<p>1.1. <em>What is the flag hidden in the file?</em><br>
<code>THM{••••••••••••••••••••••••••••••}</code></p>
<br>


<img width="1024" height="315" alt="image" src="https://github.com/user-attachments/assets/0ad26848-c63e-46b7-9a1c-37082812ae36" />

<br>
<br>
<br>

<img width="1022" height="153" alt="image" src="https://github.com/user-attachments/assets/0b88359f-c05c-40af-8888-4fbd845eb256" />

<br>
<br>
<br>
<p>1.2. <em>What is the content of foothold.txt?</em><br>
<code>THM{••••••••••••••••••••••••••••••}</code></p>


<img width="1022" height="139" alt="image" src="https://github.com/user-attachments/assets/78f5c3c3-004f-4f16-8631-48e0f3fc89dd" />

<br>
<br>
<br>


```bash
:~/SchemeCatcher# file 4.2.0-R1-1337-server.zip
4.2.0-R1-1337-server.zip: Zip archive data, at least v2.0 to extract
```

```bash
:~/SchemeCatcher# unzip 4.2.0-R1-1337-server.zip
Archive:  4.2.0-R1-1337-server.zip
  inflating: ld-linux-x86-64.so.2    
  inflating: libc.so.6               
  inflating: server                  
```

<img width="1192" height="145" alt="image" src="https://github.com/user-attachments/assets/cfb55127-ae05-497f-9a94-13bbaad096e1" />

<br>
<br>
<br>

:~/SchemeCatcher# ls
4.2.0-R1-1337-server.zip  4.2.0.zip  latest  ld-linux-x86-64.so.2  libc.so.6  server


```bash
Command executed
/tmp/b68vC103RH
Failed to execute the command
Command exited with status: %d
Command terminated abnormally
Payload loaded
Socket creation failed
localhost
Connection failed
GET %s HTTP/1.1
Host: localhost
Connection: close
Failed to send HTTP request
Command deleted
Successfully deleted /tmp/b68vC103RH
Failed to delete /tmp/b68vC103RH
=== Menu ===
1. Execute command
2. Load payload
3. Delete command
4. Exit
Choose an option: 
Enter key: 
Hello %s!
socket failed
setsockopt
bind failed
listen
Socket server listening on port 4444...
accept
Received command: %s
Exit command received
Invalid command: %s
EastMass
Access denied.
Access granted! Starting socket server...
9*3$"
GCC: (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0
```

```bash

```


<img width="1122" height="558" alt="image" src="https://github.com/user-attachments/assets/1758b009-957b-4865-815f-c3df624def7e" />

<img width="1132" height="285" alt="image" src="https://github.com/user-attachments/assets/c234bcd6-a2fe-4e9a-83dc-01f13abdaf5a" />




<p>


- EastMass<br>
- Hello %s!<br>
- system@GLIBC_2.2.5<br>
- Enter key:<br>Access granted! Starting socket server...</p>


```bash
:~/schemecatcher# cat beacon_strings.txt
/lib64/ld-linux-x86-64.so.2
GLIBC_2.14
GLIBC_2.2.5
GLIBC_2.34
GLIBC_2.4
GLIBC_2.7
__gmon_start__
__isoc99_scanf
__libc_start_main
__stack_chk_fail
_exit
accept
atoi
bind
close
connect
gethostbyname
htons
libc.so.6
listen
memcpy
perror
puts
read
remove
send
setsockopt
setvbuf
snprintf
socket
stderr
stdin
stdout
strcmp
strcspn
strlen
system
]YH<
":ac;W<UE
iE&	(%
iE&	(%
THM{Welcom3_to_th3_eastmass_pwnland}
Command executed
/tmp/b68vC103RH
Failed to execute the command
Command exited with status: %d
Command terminated abnormally
Payload loaded
Socket creation failed
localhost
Connection failed
GET %s HTTP/1.1
Host: localhost
Connection: close
Failed to send HTTP request
Command deleted
Successfully deleted /tmp/b68vC103RH
Failed to delete /tmp/b68vC103RH
=== Menu ===
1. Execute command
2. Load payload
3. Delete command
4. Exit
Choose an option: 
Enter key: 
Hello %s!
socket failed
setsockopt
bind failed
listen
Socket server listening on port 4444...
accept
Received command: %s
Exit command received
Invalid command: %s
EastMass
Access denied.
Access granted! Starting socket server...
9*3$"
GCC: (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0
_DYNAMIC
_GLOBAL_OFFSET_TABLE_
_IO_stdin_used
__FRAME_END__
__GNU_EH_FRAME_HDR
__TMC_END__
__abi_tag
__bss_start
__data_start
__do_global_dtors_aux
__do_global_dtors_aux_fini_array_entry
__dso_handle
__frame_dummy_init_array_entry
__gmon_start__
__isoc99_scanf@GLIBC_2.7
__libc_start_main@GLIBC_2.34
__stack_chk_fail@GLIBC_2.4
_dl_relocate_static_pie
_edata
_end
_exit@GLIBC_2.2.5
_fini
_init
accept@GLIBC_2.2.5
action
atoi@GLIBC_2.2.5
bind@GLIBC_2.2.5
close@GLIBC_2.2.5
completed.0
connect@GLIBC_2.2.5
crt1.o
crtstuff.c
delete_cmd
deregister_tm_clones
flag
frame_dummy
gethostbyname@GLIBC_2.2.5
htons@GLIBC_2.2.5
listen@GLIBC_2.2.5
main
memcpy@GLIBC_2.14
menu
payload_load
perror@GLIBC_2.2.5
puts@GLIBC_2.2.5
read@GLIBC_2.2.5
read_opt
remove@GLIBC_2.2.5
send@GLIBC_2.2.5
setsockopt@GLIBC_2.2.5
setup
setvbuf@GLIBC_2.2.5
snprintf@GLIBC_2.2.5
socket@GLIBC_2.2.5
source.c
start_socket_server
stderr@GLIBC_2.2.5
stdin@GLIBC_2.2.5
stdout@GLIBC_2.2.5
strcmp@GLIBC_2.2.5
strcspn@GLIBC_2.2.5
strlen@GLIBC_2.2.5
system@GLIBC_2.2.5
username.0
.bss
.comment
.data
.dynamic
.dynstr
.dynsym
.easter
.eh_frame
.eh_frame_hdr
.fini
.fini_array
.gnu.hash
.gnu.version
.gnu.version_r
.got
.got.plt
.init
.init_array
.interp
.note.ABI-tag
.note.gnu.build-id
.note.gnu.property
.plt.sec
.rela.dyn
.rela.plt
.rodata
.shstrtab
.strtab
.symtab
.text
```

<br>
<br>

<img width="1336" height="553" alt="image" src="https://github.com/user-attachments/assets/8dc5199f-7a2d-411a-b934-4f22af1324b9" />

<br>
<br>

<img width="1333" height="568" alt="image" src="https://github.com/user-attachments/assets/f39507c3-a0a6-4204-a6e7-6909e9137ff6" />



```bash
:~/schemecatcher/latest# r2 -A beacon.bin
[Cannot find function at 0x00804000 sym. and entry0 (aa)
[x] Analyze all flags starting with sym. and entry0 (aa)
[x] Analyze function calls (aac)
[x] Analyze len bytes of instructions for references (aar)
[x] Check for objc references
[x] Check for vtables
[x] Type matching analysis for all functions (aaft)
[x] Propagate noreturn information
[x] Use -AA or aaaa to perform additional experimental analysis.
[0x00804000]> afl
0x00804008    3 37           fcn.00804008
0x004013b0    1 32           sym.deregister_tm_clones
0x004013e0    1 17           sym.register_tm_clones
0x00401420    1 23           entry.fini0
0x00401450    4 94   -> 106  entry.init0
0x00401884    1 8            sym.start_socket_server
0x004017b5    1 8            sym.read_opt
0x0040174b    1 12           sym.menu
0x00401bc4    1 2            sym._fini
0x0040153c    1 8            sym.payload_load
0x004016fe    1 12           sym.delete_cmd
0x004014bb    1 8            sym.cmd
0x004013a0    1 4            sym._dl_relocate_static_pie
0x00401370    1 13           sym._start
0x00401b4a    1 8            main
0x00401804    1 75           sym.action
0x00804007    1 1            fcn.00804007
0x0040253d    1 127          fcn.0040253d
df @sym.action
\u250c 75: sym.action (int64_t arg1, int64_t arg2, int64_t arg3, int64_t arg4, int64_t arg5);
\u2502           ; arg int64_t arg1 @ rdi
\u2502           ; arg int64_t arg2 @ rsi
\u2502           ; arg int64_t arg3 @ rdx
\u2502           ; arg int64_t arg4 @ rcx
\u2502           ; arg int64_t arg5 @ r8
\u2502           0x00401804      fe02           inc byte [rdx]              ; arg3
\u2502           0x00401806      13f7           adc esi, edi                ; arg2
\u2502           0x00401808      58             pop rax
\u2502           0x00401809      4584e8         test r8b, r13b
\u2502           0x0040180c      458008e2       or byte [r8], 0xe2          ; [0xe2:1]=255 ; 226 ; arg5
\u2502           0x00401810      040d           add al, 0xd                 ; 13
\u2502           0x00401812      0d4584cab5     or eax, 0xb5ca8445
\u2502           0x00401817      0d0d0d0de5     or eax, 0xe50d0d0d
\u2502           0x0040181c      4df7f2         div r10
\u2502           0x0040181f      f2b72d         mov bh, 0x2d                ; '-' ; 45
\u2502           0x00401822      0d0d0d4580     or eax, 0x80450d0d
\u2502           0x00401827      0819           or byte [rcx], bl           ; arg4
\u2502           0x00401829      240d           and al, 0xd                 ; 13
\u2502           0x0040182b      0d4584cbb2     or eax, 0xb2cb8445
\u2502           0x00401830      0d0d0d0de5     or eax, 0xe50d0d0d
\u2502           0x00401835      6af7           push -9
\u2502           0x00401837      f2f2458008c3   or byte [r8], 0xc3          ; [0xc3:1]=255 ; 195 ; arg5
\u2502           0x0040183d      040d           add al, 0xd                 ; 13
\u2502           0x0040183f      0d4584cb45     or eax, 0x45cb8445
\u2502           0x00401844      8008fb         or byte [rax], 0xfb         ; [0xfb:1]=255 ; 251
\u2502           0x00401847      250d0d4584     and eax, 0x84450d0d
\u2514           0x0040184c      cae533         retf 0x33e5
[0x00804000]> 
```







```bash
:~/latest# nc 10.64.168.0 9004
Payload Storage Malhare's
Version 4.2.0
[1] C:
[2] U:
[3] D:
[4] E:
>>1
size: 
100
[1] C:
[2] U:
[3] D:
[4] E:
>>2
idx:
0
offset:
0
data:
EastMass
[1] C:
[2] U:
[3] D:
[4] E:
>>4
Bye
```



```bash
:~/schemecatcher/latest# docker run --rm -v $(pwd):/data -it ubuntu:22.04 bash
...
...:/# cd /data
```

```bash
...:/data# ls
beacon.bin
```

```bash
...:/data# ./beacon.bin
Enter key: EastMass
Hello EastMass!
Access granted! Starting socket server...
Socket server listening on port 4444...
```


<img width="1336" height="198" alt="image" src="https://github.com/user-attachments/assets/3096d98a-bc6f-4290-86c8-2aef5e1888b8" />




root@57516d8d398d:/data# pkill beacon.bin
root@57516d8d398d:/data# ./beacon.bin
Enter key: EastMass
Hello EastMass!
Access granted! Starting socket server...
Socket server listening on port 4444...
docker ps
flag




<img width="1170" height="127" alt="image" src="https://github.com/user-attachments/assets/27e54923-e46c-4197-876c-c0b093714d49" />

<img width="776" height="273" alt="image" src="https://github.com/user-attachments/assets/88e9c882-1bd9-483f-b6a4-b353b8122452" />


<img width="738" height="741" alt="image" src="https://github.com/user-attachments/assets/fcfd5df3-dfa0-443a-963d-f1c25cc27498" />
