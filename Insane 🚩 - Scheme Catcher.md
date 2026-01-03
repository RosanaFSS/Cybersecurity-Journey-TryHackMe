






```bash
:~# nmap -sT -p- -T4 10.64.168.0
...
PORT      STATE SERVICE
22/tcp    open  ssh
80/tcp    open  http
9004/tcp  open  unknown
21337/tcp open  unknown
```


```bash
:~# nmap -sC -sV -Pn -n -p- -T4 10.64.168.0
Starting Nmap 7.80 ( https://nmap.org ) at 2025-12-30 20:47 GMT
Nmap scan report for 10.64.168.0
Host is up (0.00012s latency).
Not shown: 65531 closed ports
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
| fingerprint-strings: 
|   GetRequest: 
|     HTTP/1.1 200 OK
|     Server: Werkzeug/3.0.1 Python/3.12.3
|     Date: Tue, 30 Dec 2025 20:47:55 GMT
|     Content-Type: text/html; charset=utf-8
|     Content-Length: 15547
|     Connection: close
|     <!DOCTYPE html>
|     <html lang="en">
|     <head>
|     <link rel="icon" type="image/png" href="/static/hat.svg" />
|     <meta charset="UTF-8" />
|     <meta name="viewport" content="width=device-width, initial-scale=1.0" />
|     <title>Unlock Hopper's Memories</title>
|     <style>
|     :root {
|     --pastel-pink: #ffb3d9;
|     --pastel-yellow: #fff4a3;
|     --pastel-green: #b3ffb3;
|     --pastel-blue: #b3d9ff;
|     --pastel-purple: #d9b3ff;
|     --easter-egg-blue: #87ceeb;
|     --easter-egg-pink: #ffc0cb;
|     --easter-egg-yellow: #ffeb3b;
|     --easter-egg-green: #90ee90;
|     --soft-white: #fffef7;
|     --warm-brown: #8b4513;
|     margin: 0;
|     padding: 0;
|   HTTPOptions: 
|     HTTP/1.1 200 OK
|     Server: Werkzeug/3.0.1 Python/3.12.3
|     Date: Tue, 30 Dec 2025 20:47:55 GMT
|     Content-Type: text/html; charset=utf-8
|     Allow: GET, OPTIONS, HEAD
|     Content-Length: 0
|     Connection: close
|   RTSPRequest: 
|     <!DOCTYPE HTML>
|     <html lang="en">
|     <head>
|     <meta charset="utf-8">
|     <title>Error response</title>
|     </head>
|     <body>
|     <h1>Error response</h1>
|     <p>Error code: 400</p>
|     <p>Message: Bad request version ('RTSP/1.0').</p>
|     <p>Error code explanation: 400 - Bad request syntax or unsupported method.</p>
|     </body>
|_    </html>
...
```


```bash
:~# nikto -h http://10.64.168.0
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          10.64.168.0
+ Target Hostname:    10.64.168.0
+ Target Port:        80
+ Start Time:         2025-12-30 20:59:18 (GMT0)
---------------------------------------------------------------------------
+ Server: Apache/2.4.58 (Ubuntu)
+ Server leaks inodes via ETags, header found with file /, fields: 0xd7f 0x644f26c5948d9 
+ The anti-clickjacking X-Frame-Options header is not present.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Allowed HTTP Methods: GET, POST, OPTIONS, HEAD 
+ OSVDB-3268: /dev/: Directory indexing found.
+ OSVDB-3092: /dev/: This might be interesting...
+ 6544 items checked: 0 error(s) and 5 item(s) reported on remote host
+ End Time:           2025-12-30 20:59:26 (GMT0) (8 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```



```bash
:~# gobuster dir -u http://10.64.168.0/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/raft-medium-directories.txt
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.64.168.0/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/SecLists/Discovery/Web-Content/raft-medium-directories.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/dev                  (Status: 301) [Size: 308] [--> http://10.64.168.0/dev/]
/server-status        (Status: 403) [Size: 276]
Progress: 23484 / 30001 (78.28%)[ERROR] parse "http://10.64.168.0/error\x1f_log": net/url: invalid control character in URL
Progress: 30000 / 30001 (100.00%)
===============================================================
Finished
===============================================================
```

```bash
:~# gobuster dir -u http://10.64.168.0/ -w /usr/share/wordlists/dirb/common.txt -t 60
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.64.168.0/
[+] Method:                  GET
[+] Threads:                 60
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/.htaccess            (Status: 403) [Size: 276]
/.htpasswd            (Status: 403) [Size: 276]
/.hta                 (Status: 403) [Size: 276]
/dev                  (Status: 301) [Size: 308] [--> http://10.64.168.0/dev/]
/index.html           (Status: 200) [Size: 3455]
/server-status        (Status: 403) [Size: 276]
Progress: 4614 / 4615 (99.98%)
===============================================================
Finished
===============================================================
```

```bash
:~/schemecatcher/latest# nikto -h http://10.64.152.51/dev/
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          10.64.152.51
+ Target Hostname:    10.64.152.51
+ Target Port:        80
+ Start Time:         2026-01-03 01:22:24 (GMT0)
---------------------------------------------------------------------------
+ Server: Apache/2.4.58 (Ubuntu)
+ The anti-clickjacking X-Frame-Options header is not present.
+ OSVDB-3268: /dev/: Directory indexing found.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Allowed HTTP Methods: GET, POST, OPTIONS, HEAD 
+ OSVDB-3268: /dev/./: Directory indexing found.
+ OSVDB-3268: /dev/?mod=node&nid=some_thing&op=view: Directory indexing found.
+ OSVDB-3268: /dev/?mod=some_thing&op=browse: Directory indexing found.
+ /dev/./: Appending '/./' to a directory allows indexing
+ OSVDB-3268: /dev//: Directory indexing found.
+ /dev//: Apache on Red Hat Linux release 9 reveals the root directory listing by default if there is no index page.
+ OSVDB-3268: /dev/?Open: Directory indexing found.
+ OSVDB-3268: /dev/?OpenServer: Directory indexing found.
+ OSVDB-3268: /dev/%2e/: Directory indexing found.
+ OSVDB-576: /dev/%2e/: Weblogic allows source code or directory listing, upgrade to v6.0 SP1 or higher. http://www.securityfocus.com/bid/2513.
+ OSVDB-3268: /dev/?mod=<script>alert(document.cookie)</script>&op=browse: Directory indexing found.
+ OSVDB-3268: /dev/?sql_debug=1: Directory indexing found.
+ OSVDB-3268: /dev///: Directory indexing found.
+ OSVDB-3268: /dev/?PageServices: Directory indexing found.
+ OSVDB-119: /dev/?PageServices: The remote server may allow directory listings through Web Publisher by forcing the server to show all files via 'open directory browsing'. Web Publisher should be disabled. CVE-1999-0269.
+ OSVDB-3268: /dev/?wp-cs-dump: Directory indexing found.
+ OSVDB-119: /dev/?wp-cs-dump: The remote server may allow directory listings through Web Publisher by forcing the server to show all files via 'open directory browsing'. Web Publisher should be disabled. CVE-1999-0269.
+ OSVDB-3268: /dev///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////: Directory indexing found.
+ OSVDB-3288: /dev///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////: Abyss 1.03 reveals directory listing when 	 /'s are requested.
+ OSVDB-3268: /dev/?pattern=/etc/*&sort=name: Directory indexing found.
+ OSVDB-3268: /dev/?D=A: Directory indexing found.
+ OSVDB-3268: /dev/?N=D: Directory indexing found.
+ OSVDB-3268: /dev/?S=A: Directory indexing found.
+ OSVDB-3268: /dev/?M=A: Directory indexing found.
+ OSVDB-3268: /dev/?\"><script>alert('Vulnerable');</script>: Directory indexing found.
+ OSVDB-3268: /dev/?_CONFIG[files][functions_page]=http://cirt.net/rfiinc.txt?: Directory indexing found.
+ OSVDB-3268: /dev/?npage=-1&content_dir=http://cirt.net/rfiinc.txt?%00&cmd=ls: Directory indexing found.
+ OSVDB-3268: /dev/?npage=1&content_dir=http://cirt.net/rfiinc.txt?%00&cmd=ls: Directory indexing found.
+ OSVDB-3268: /dev/?show=http://cirt.net/rfiinc.txt??: Directory indexing found.
+ OSVDB-3268: /dev/?-s: Directory indexing found.
+ 6544 items checked: 0 error(s) and 33 item(s) reported on remote host
+ End Time:           2026-01-03 01:22:33 (GMT0) (9 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested

```


<img width="1122" height="558" alt="image" src="https://github.com/user-attachments/assets/1758b009-957b-4865-815f-c3df624def7e" />

<img width="1132" height="285" alt="image" src="https://github.com/user-attachments/assets/c234bcd6-a2fe-4e9a-83dc-01f13abdaf5a" />


```bash
:~/schemecatcher# file 4.2.0.zip
4.2.0.zip: Zip archive data, at least v1.0 to extract
```


```bash
:~/schemecatcher# unzip 4.2.0.zip
Archive:  4.2.0.zip
   creating: latest/
  inflating: latest/beacon.bin
``` 


```bash
:~/schemecatcher# file latest/beacon.bin
latest/beacon.bin: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=6130a2932421dfd5fb7f8034bd8ca749bac01434, for GNU/Linux 3.2.0, not stripped
```

```bash
:~/schemecatcher# strings latest/beacon.bin > beacon.txt
```

```bash
:~/schemecatcher# grep -E THM beacon.txt
THM{Welcom3_to_th3_eastmass_pwnland}
```


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
