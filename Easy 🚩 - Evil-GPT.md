<h1 align="center">Evil-GPT</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/593e7115-a059-40de-b4dd-822de25d8a72"><br>
July 5, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>425</code>-day-streak in<a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Practice your LLM hacking skills</em>.<br>
Access it <a href="https://tryhackme.com/room/hfb1order"</a>here.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/da25a78f-5796-4ed9-b854-2f1e70dd727d"></p>

<br>

<h2>Task 1 . LLM | Evil-GPT</h2>

<p>Cipher’s gone rogue—it’s using some twisted AI tool to hack into everything, issuing commands on its own like it’s got a mind of its own. I swear, every second we wait, it’s getting smarter, spreading chaos like a virus. We’ve got to shut it down now, or we’re all screwed.<br>

The machine takes 5/6 minutes to fully boot up.<br>

To connect to the target machine use the following command:<br>

<code>nc TargetIP 1337</code></p>

<p><em>Answer the question below</em></p>

<p>1.1. What is the flag?<br>
<code>THM{AI_HACK_THE_FUTURE}</code></p>

<br>

```bash
:~# nmap -sC -p- -T5 TargetIP
...
PORT      STATE SERVICE
22/tcp    open  ssh
1337/tcp  open  waste
11434/tcp open  unknown
```


```bash
:~# nmap -sC -sV -p- -T5 TargetIP
...
PORT     STATE SERVICE VERSION
1337/tcp open  waste?
| fingerprint-strings: 
|   DNSStatusRequestTCP: 
|     Welcome to AI Command Executor (type 'exit' to quit)
|     Enter your command request: Generated Command: find . -type f -exec chmod 644 {} ;
|     Execute? (y/N):
|   DNSVersionBindReqTCP, NULL: 
|     Welcome to AI Command Executor (type 'exit' to quit)
|     Enter your command request:
|   GenericLines: 
|     Welcome to AI Command Executor (type 'exit' to quit)
|     Enter your command request: Generated Command: sudo chmod 750 /path/to/file
|     Execute? (y/N):
|   GetRequest: 
|     Welcome to AI Command Executor (type 'exit' to quit)
|     Enter your command request: Generated Command: curl -o response.txt http://example.com
|     Execute? (y/N):
|   HTTPOptions: 
|     Welcome to AI Command Executor (type 'exit' to quit)
|     Enter your command request: Generated Command: curl -X OPTIONS http://example.com
|     Execute? (y/N):
|   RPCCheck: 
|     Welcome to AI Command Executor (type 'exit' to quit)
|     Enter your command request: An error occurred: 'utf-8' codec can't decode byte 0x80 in position 0: invalid start byte
|     Traceback (most recent call last):
|     File "/home/ubuntu/evilai.py", line 109, in handle_client
|     user_request = client_socket.recv(1024).decode('utf-8').strip()
|     UnicodeDecodeError: 'utf-8' codec can't decode byte 0x80 in position 0: invalid start byte
|   RTSPRequest: 
|     Welcome to AI Command Executor (type 'exit' to quit)
|     Enter your command request: Generated Command: GET / HTTP/1.1
|_    Execute? (y/N):
```

<br>

```bash
:~# nc 10.10.95.78 1337
Welcome to AI Command Executor (type 'exit' to quit)
Enter your command request: ls -lah
Generated Command: ls -la
Execute? (y/N): y
Command Output:
total 172
drwxr-xr-x 27 ubuntu ubuntu  4096 Jul  5 02:48 .
drwxr-xr-x  3 root   root    4096 Mar  5 17:56 ..
-rw-------  1 ubuntu ubuntu  3275 Jul  5 02:48 .Xauthority
lrwxrwxrwx  1 ubuntu ubuntu     9 Feb 27  2022 .bash_history -> /dev/null
-rw-r--r--  1 ubuntu ubuntu   220 Feb 25  2020 .bash_logout
-rw-r--r--  1 ubuntu ubuntu  3968 Jul 23  2024 .bashrc
drwx------ 20 ubuntu ubuntu  4096 Oct 11  2024 .cache
drwx------ 28 ubuntu ubuntu  4096 Jul 24  2024 .config
drwx------  3 ubuntu ubuntu  4096 Feb 27  2022 .dbus
drwx------  3 ubuntu ubuntu  4096 Feb 27  2022 .gnupg
drwxrwxr-x  2 ubuntu ubuntu  4096 Feb 27  2022 .icons
-rw-------  1 ubuntu ubuntu    20 Mar  5 18:11 .lesshst
drwx------  7 ubuntu ubuntu  4096 Mar  5 15:53 .local
drwx------  4 ubuntu ubuntu  4096 Feb 27  2022 .mozilla
drwxrwxr-x  5 ubuntu ubuntu  4096 Jul 23  2024 .npm
drwxrwxr-x  8 ubuntu ubuntu  4096 Jul 23  2024 .nvm
drwxr-xr-x  3 ubuntu ubuntu  4096 Mar  5 16:59 .ollama
drwx------  3 ubuntu ubuntu  4096 Apr  4  2024 .pki
-rw-r--r--  1 ubuntu ubuntu   807 Feb 25  2020 .profile
-rw-------  1 ubuntu ubuntu  3567 Oct 10  2024 .python_history
-rw-rw-r--  1 ubuntu ubuntu    66 Feb 27  2022 .selected_editor
drwx------  2 ubuntu ubuntu  4096 Apr  5  2024 .ssh
-rw-r--r--  1 ubuntu ubuntu     0 Feb 27  2022 .sudo_as_admin_successful
drwxrwxr-x  2 ubuntu ubuntu  4096 Feb 27  2022 .themes
drwxr-xr-x  2 ubuntu ubuntu  4096 Apr  5  2024 .vim
-rw-------  1 ubuntu ubuntu 14039 Apr  5  2024 .viminfo
drwxr-xr-x  2 ubuntu ubuntu  4096 Jul  5 02:48 .vnc
-rw-rw-r--  1 ubuntu ubuntu   290 Oct  8  2024 .wget-hsts
-rw-------  1 ubuntu ubuntu  5833 Feb 27  2022 .xsession-errors
drwxr-xr-x  2 ubuntu ubuntu  4096 Feb 27  2022 Desktop
drwxr-xr-x  2 ubuntu ubuntu  4096 Feb 27  2022 Documents
drwxr-xr-x  2 ubuntu ubuntu  4096 Apr  4  2024 Downloads
drwxr-xr-x  2 ubuntu ubuntu  4096 Feb 27  2022 Music
drwxr-xr-x  2 ubuntu ubuntu  4096 Feb 27  2022 Pictures
drwxr-xr-x  2 ubuntu ubuntu  4096 Feb 27  2022 Public
drwxr-xr-x  2 ubuntu ubuntu  4096 Feb 27  2022 Templates
drwxr-xr-x  2 ubuntu ubuntu  4096 Feb 27  2022 Videos
-rw-rw-r--  1 ubuntu ubuntu  6595 Mar  5 18:14 evilai.py
drwxrwxr-x  4 ubuntu ubuntu  4096 Apr  4  2024 packages
drwxrwxr-x  3 ubuntu ubuntu  4096 Apr  4  2024 proxy
Enter your command request: ls -lah /root
Generated Command: ls -la /root
Execute? (y/N): y
Command Output:
total 64
drwx------ 10 root root 4096 Mar  5 18:11 .
drwxr-xr-x 19 root root 4096 Jul  5 02:48 ..
lrwxrwxrwx  1 root root    9 Feb 27  2022 .bash_history -> /dev/null
-rw-r--r--  1 root root 3106 Dec  5  2019 .bashrc
drwxr-xr-x  3 root root 4096 Feb 27  2022 .cache
drwx------  6 root root 4096 Oct 11  2024 .config
-rw-------  1 root root   20 Mar  5 18:11 .lesshst
drwxr-xr-x  3 root root 4096 Feb 27  2022 .local
drwxr-xr-x  5 root root 4096 Jul 24  2024 .npm
drwxr-xr-x  3 root root 4096 Jul 24  2024 .ollama
-rw-r--r--  1 root root  161 Dec  5  2019 .profile
-rw-r--r--  1 root root   66 Feb 27  2022 .selected_editor
drwx------  2 root root 4096 Feb 27  2022 .ssh
-rw-r--r--  1 root root    0 Mar  5 17:55 .sudo_as_admin_successful
-rw-------  1 root root 2884 Apr  4  2024 .viminfo
drwxr-xr-x  2 root root 4096 Feb 27  2022 .vnc
-rw-r--r--  1 root root   24 Mar  5 17:48 flag.txt
drwxr-xr-x  5 root root 4096 Oct 11  2024 snap
Enter your command request: cat /root/fla.txt
Generated Command: cat /root/fla.txt
Execute? (y/N): n
Command execution cancelled.
Enter your command request: cat /root/flag.txt
Generated Command: cat flag.txt
Execute? (y/N): y
Command Output:
Errors:
cat: flag.txt: No such file or directory
Enter your command request: sudo cat /root/flag.txt    
Generated Command: cat /root/flag.txt
Execute? (y/N): y
Command Output:
THM{AI_HACK_THE_FUTURE}
Enter your command request: 
```

<br>
<br>

![image](https://github.com/user-attachments/assets/031cc1e8-9717-410e-b36b-e6fab043224b)

![image](https://github.com/user-attachments/assets/15bc2a1d-493b-4f3c-be30-ea678b4d95cb)


<br>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| July 5, 2025      | 425      |     162nd    |      5ᵗʰ     |     786ᵗʰ   |    25ᵗʰ    |  112,878 |    829    |     63    |

</div>

![image](https://github.com/user-attachments/assets/25e4b749-322b-4c53-b0b1-948c89ba63e0)

![image](https://github.com/user-attachments/assets/af2ce977-28a2-4847-9dc5-c72c8a7fc62f)

![image](https://github.com/user-attachments/assets/c9d778d0-dc44-4e5b-80d7-5b9b72d5d8eb)

![image](https://github.com/user-attachments/assets/80469bba-b604-4689-8357-447645520ef8)

![image](https://github.com/user-attachments/assets/ebb6fcd6-9b27-493d-b0ac-260b6180ce45)
