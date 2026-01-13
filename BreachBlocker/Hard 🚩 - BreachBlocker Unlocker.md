<h1 align="center"><a href="https://tryhackme.com/room/sq4-aoc2025-32LoZ4zePK">BreachBlocker Unlocker</a></h1>
<h3 align="center">Advent of Cyber 2025 &nbsp;|&nbsp; Side Quest</h3>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/ffdfc164-51d8-47ab-8f97-024516a6c7da"><br>
If you find it helpful, consider coming back for research.<br><p align="center"><a href="https://github.com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=for-the-badge&logo=github&color=24292e" alt="Follow Rosana on GitHub"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://img.shields.io/badge/COMPLETED-2026%2C%20JAN%2013-444444?style=for-the-badge&logo=calendar-check" alt="Completion Date"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn"></a></p>

<h2>Task 1 . BreackBlocker Unlocker</h2>
<h3>Hopper the Detective</h3>
<p>When Sir BreachBlocker is captured, Hopper senses an opportunity: the last key to the stolen AoC charity funds is hidden somewhere on Sir BreachBlocker’s seized phone.
The device looks innocent enough: a Hopflix streaming app, a banking app, messages, photos, and settings. But nothing about this op is innocent. Hopper must somehow pivot into the linked bank account, and, outsmarting the layered authentication around it, he can wrest control of the funds before King Malhare’s cronies move them for good. If he succeeds, The Best Festival Company is saved; if he fails, the story of “Colonel Panic” ends in quiet disgrace, erased like so many secrets before.</p>


<h3>Rules</h3>
<p>

- Do not share questions or hints, including in videos, streams, or any other medium while the event is running (until Dec 31st).<br>
- Only hack machines deployed in the rooms you have legitimate, authorised access to.<br><code>*.tryhackme.com</code> and VPN servers are off-limits for probing, scanning, or exploiting.<br>Teaming up is permitted.<br>
- For a more comprehensive list, please read the <strong>Advent of Cyber 2025 Terms and Conditions</strong>.<br><strong>Initial Access</strong>.<br>

This Side Quest is unlocked by finding the Side Quest key in Advent of Cyber Day 21. Once you’ve recovered that key, visit <code>MACHINE_IP:21337</code> and enter it to unlock Hopper’s challenge. From there, your mission is simple to state and hard to execute: break into Sir BreachBlocker’s phone, bypass all authentication, and recover the final key needed to release the funds for The Best Festival Company.
</p>



<p><em>Answer the questions below</em></p>

<p>

- Navigate to <code>MACHINE_IP:21337</code><br>
- Enter the <strong>Memory Key</strong> discovered in <strong>Advent of Cyber 2025, Day 21</strong><br>
- Click <strong>UNLOCK MEMORIES</strong></p>

<br>
<h1 align="center">Port Scanning<a id='1'></a></h1>

<div align="center"><p>

| **Port**           | **Service**          | **Version**                       |
|-------------------:|:---------------------|:----------------------------------|
| `22`               |`SSH`                 |OpenSSH 9.6p1 Ubuntu 3ubuntu13.14  |
| `25`               |`SMTP`                |Postfix smtpd                      |
| `8443`             |`SSL/HTTP`            |nginx 1.29.3                       |
| `21337`            |`-`                   |-                                  |

</p></div><br>


```bash
:~/BreachblockerUnlocker# nmap -sC -sV -Pn -n -p- -T4 xx.xx.xxx.xxx
...
PORT      STATE SERVICE  VERSION
22/tcp    open  ssh      OpenSSH 9.6p1 Ubuntu 3ubuntu13.14 (Ubuntu Linux; protocol 2.0)
25/tcp    open  smtp     Postfix smtpd
| smtp-commands: hostname, PIPELINING, SIZE 10240000, VRFY, ETRN, ENHANCEDSTATUSCODES, 8BITMIME, DSN, SMTPUTF8, CHUNKING, 
|_ 2.0.0 Commands: AUTH BDAT DATA EHLO ETRN HELO HELP MAIL NOOP QUIT RCPT RSET STARTTLS VRFY XCLIENT XFORWARD 
8443/tcp  open  ssl/http nginx 1.29.3
|_http-server-header: nginx/1.29.3
|_http-title: Mobile Portal
| ssl-cert: Subject: organizationName=Internet Widgits Pty Ltd/stateOrProvinceName=Some-State/countryName=AU
| Not valid before: 2025-12-11...
|_Not valid after:  2026-12-11...
| tls-alpn: 
|   h2
|_  http/1.1
21337/tcp open  unknown
| fingerprint-strings: 
|   GetRequest: 
|     HTTP/1.1 200 OK
...
```

<h1 align="center">File Enumeration<a id='2'></a></h1>
<p align="center">/index.html, /main.js, /main.py /nginx.conf</p>

<p>Used <strong>ffuf</strong> with the following parameters:<br>

- <code>-w</code> &nbsp; : &nbsp; Wordlist file path and (optional) keyword separated by colon. eg. '/path/to/wordlist:KEYWORD'<br>
- <code>-u</code> &nbsp; : &nbsp; Target URL<br>  
- <code>-mc</code> &nbsp; : &nbsp;  Match HTTP status codes, or "all" for everything. (default: 200-299,301,302,307,401,403,405,500)<br>
- <code>-ic</code> &nbsp; : &nbsp; Ignore wordlist comments (default: false)<br>
- <code>-c</code> &nbsp; : &nbsp; Colorize output. (default: false)<br>
- <code>-e</code> &nbsp; : &nbsp; Comma separated list of extensions. Extends FUZZ keyword.<br>
- <code>-t</code> &nbsp; : &nbsp; Number of concurrent threads. (default: 40)</p>


```bash
:~/BreachblockerUnlocker# ffuf -u https://xx.xx.xxx.xxx:8443/FUZZ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -mc 200 -ic -c -e .js,.html,.py -t 60

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.3.1
________________________________________________

 :: Method           : GET
 :: URL              : https://xx.xx.xxx.xxx:8443/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
 :: Extensions       : .js .html .py 
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 60
 :: Matcher          : Response status: 200
________________________________________________

                        [Status: 200, Size: 117357, Words: 46509, Lines: 1802]
index.html              [Status: 200, Size: 117357, Words: 46509, Lines: 1802]
main.js                 [Status: 200, Size: 24510, Words: 1075, Lines: 598]
main.py                 [Status: 200, Size: 6514, Words: 1198, Lines: 215]
:: Progress: [873060/873060] :: Job [1/1] :: 1660 req/sec :: Duration: [0:09:03] :: Errors: 0 ::
```

<img width="1778" height="501" alt="image" src="https://github.com/user-attachments/assets/7545c972-2131-48a0-9068-8adaac59892a" />

<br>
<br>
<br>

```bash
:~/BreachblockerUnlocker# ffuf -u https://xx.xx.xxx.xxx:8443/FUZZ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/quickhits.txt -e .js,.php,.json,.txt,.conf,.html -mc 200 -ic -t 60

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.3.1
________________________________________________

 :: Method           : GET
 :: URL              : https://xx.xx.xxx.xxx:8443/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/SecLists/Discovery/Web-Content/quickhits.txt
 :: Extensions       : .js .php .json .txt .conf .html 
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 60
 :: Matcher          : Response status: 200
________________________________________________

/nginx.conf             [Status: 200, Size: 890, Words: 226, Lines: 32]
:: Progress: [17073/17073] :: Job [1/1] :: 1366 req/sec :: Duration: [0:00:13] :: Errors: 0 ::
```

<img width="1775" height="451" alt="image" src="https://github.com/user-attachments/assets/7f10af9c-6da2-4618-a310-e89e3401a324" />

<br>
<br>
<h1 align="center">Web Interface Inspection</h1>
<p align="center">8443<br>/nginx.conf<br>Note <strong>location { try_files $uri @app;}</strong></p>

```bash
:~/BreachblockerUnlocker# ls
nginx.conf
```

```bash
:~/BreachblockerUnlocker# cat nginx.conf
user  nginx;
worker_processes 4;
error_log  /var/log/nginx/error.log warn;
pid        /var/run/nginx.pid;
events {
    worker_connections 2048;
}
http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;
    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';
    access_log  /var/log/nginx/access.log  main;
    sendfile        on;
    keepalive_timeout  300;
    server {
        listen 443 ssl http2;
	ssl_certificate /app/server.cert;
	ssl_certificate_key /app/server.key;
	ssl_protocols TLSv1.2;
        location / {
            try_files $uri @app;
        }
        location @app {
            include uwsgi_params;
            uwsgi_pass unix:///tmp/uwsgi.sock;
        }
    }
}
daemon off;
```

<br>
<p align="center">/main.py<br>CODE_FLAG</p>

<img width="1604" height="516" alt="image" src="https://github.com/user-attachments/assets/ed36e5c6-2a23-400d-92f0-0379dcc56936" />

```bash
...
connection = sqlite3.connect("/hopflix-874297.db")
cursor = connection.cursor()

connection2 = sqlite3.connect("/hopsecbank-12312497.db")
cursor2 = connection2.cursor()

app = Flask(__name__)
app.secret_key = os.getenv('SECRETKEY')

aes_key = bytes(os.getenv('AESKEY'), "utf-8")

# Credentials (server-side only)
HOPFLIX_FLAG = os.getenv('HOPFLIX_FLAG')
BANK_ACCOUNT_ID = "hopper"
BANK_PIN = os.getenv('BANK_PIN')
BANK_FLAG = os.getenv('BANK_FLAG')
#CODE_FLAG = THM{••••••••••••••••••••••}
...
```

```bash
from flask import Flask, request, jsonify, send_from_directory, session
import time
import random
import os
import hashlib
import time
import smtplib
import sqlite3
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

connection = sqlite3.connect("/hopflix-874297.db")
cursor = connection.cursor()

connection2 = sqlite3.connect("/hopsecbank-12312497.db")
cursor2 = connection2.cursor()

app = Flask(__name__)
app.secret_key = os.getenv('SECRETKEY')

aes_key = bytes(os.getenv('AESKEY'), "utf-8")

# Credentials (server-side only)
HOPFLIX_FLAG = os.getenv('HOPFLIX_FLAG')
BANK_ACCOUNT_ID = "hopper"
BANK_PIN = os.getenv('BANK_PIN')
BANK_FLAG = os.getenv('BANK_FLAG')
#CODE_FLAG = THM{••••••••••••••••••••••}

def encrypt(plaintext):
    cipher = AES.new(aes_key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(plaintext.encode('utf-8'))
    return base64.b64encode(cipher.nonce + tag + ciphertext).decode('utf-8')

def decrypt(encrypted_data):
    decoded_data = base64.b64decode(encrypted_data.encode('utf-8'))
    nonce_len = 16
    tag_len = 16
    nonce = decoded_data[:nonce_len]
    tag = decoded_data[nonce_len:nonce_len + tag_len]
    ciphertext = decoded_data[nonce_len + tag_len:]

    cipher = AES.new(aes_key, AES.MODE_GCM, nonce=nonce)
    plaintext_bytes = cipher.decrypt_and_verify(ciphertext, tag)
    return plaintext_bytes.decode('utf-8')

def validate_email(email):
    if '@' not in email:
        return False
    if any(ord(ch) <= 32 or ord(ch) >=126 or ch in [',', ';'] for ch in email):
        return False

    return True

def send_otp_email(otp, to_addr):
    if not validate_email(to_addr):
        return -1

    allowed_emails= session['bank_allowed_emails']
    allowed_domains= session['bank_allowed_domains']
    domain = to_addr.split('@')[-1]
    if domain not in allowed_domains and to_addr not in allowed_emails:
        return -1

    from_addr = 'no-reply@hopsecbank.thm'
    message = f"""\
    Subject: Your OTP for HopsecBank

    Dear you,
    The OTP to access your banking app is {otp}.

    Thanks for trusting Hopsec Bank!"""

    s = smtplib.SMTP('smtp')
    s.sendmail(from_addr, to_addr, message)
    s.quit()


def hopper_hash(s):
    res = s
    for i in range(5000):
        res = hashlib.sha1(res.encode()).hexdigest()
    return res

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('.', path)

@app.route('/api/check-credentials', methods=['POST'])
def check_credentials():
    data = request.json
    email = str(data.get('email', ''))
    pwd = str(data.get('password', ''))
    
    rows = cursor.execute(
        "SELECT * FROM users WHERE email = ?",
        (email,),
    ).fetchall()

    if len(rows) != 1:
        return jsonify({'valid':False, 'error': 'User does not exist'})
    
    phash = rows[0][2]
    
    if len(pwd)*40 != len(phash):
        return jsonify({'valid':False, 'error':'Incorrect Password'})

    for ch in pwd:
        ch_hash = hopper_hash(ch)
        if ch_hash != phash[:40]:
            return jsonify({'valid':False, 'error':'Incorrect Password'})
        phash = phash[40:]
    
    session['authenticated'] = True
    session['username'] = email
    return jsonify({'valid': True})

@app.route('/api/get-last-viewed', methods=['GET'])
def get_bank_account_id():
    if not session.get('authenticated', False):
        return jsonify({'error': 'Unauthorized'}), 401
    return jsonify({'last_viewed': HOPFLIX_FLAG})

@app.route('/api/bank-login', methods=['POST'])
def bank_login():
    data = request.json
    account_id = str(data.get('account_id', ''))
    pin = str(data.get('pin', ''))
    
    # Check bank credentials
    rows = cursor2.execute(
        "SELECT * FROM users WHERE email = ?",
        (account_id,),
    ).fetchall()

    if len(rows) != 1:
        return jsonify({'valid':False, 'error': 'User does not exist'})
    
    phash = rows[0][2]
    if hashlib.sha256(pin.encode()).hexdigest().lower() == phash:
        session['bank_authenticated'] = True
        session['bank_2fa_verified'] = False
        session['bank_allowed_emails'] = rows[0][5].split(',')
        session['bank_allowed_domains'] = rows[0][6].split(',')
        
        if len(session['bank_allowed_emails']) > 0:
            return jsonify({
                'success': True,
                'requires_2fa': True,
                'trusted_emails': rows[0][5].split(','),
            })
        if len(session['bank_allowed_domains']) > 0:
            return jsonify({
                'success': True,
                'requires_2fa': True,
                'trusted_domains': rows[0][6].split(','),
            })
    else:
        return jsonify({'error': 'Invalid credentials'}), 401

@app.route('/api/send-2fa', methods=['POST'])
def send_2fa():
    data = request.json
    otp_email = str(data.get('otp_email', ''))
    
    if not session.get('bank_authenticated', False):
        return jsonify({'error': 'Access denied.'}), 403
    
    # Generate 2FA code
    two_fa_code = ''.join([str(random.randint(0, 9)) for _ in range(6)])
    session['bank_2fa_code'] = encrypt(two_fa_code)

    if send_otp_email(two_fa_code, otp_email) != -1:
        return jsonify({'success': True})
    else:
        return jsonify({'success': False})

@app.route('/api/verify-2fa', methods=['POST'])
def verify_2fa():
    data = request.json
    code = str(data.get('code', ''))
    
    if not session.get('bank_authenticated', False):
        return jsonify({'error': 'Access denied.'}), 403
    
    if not session.get('bank_2fa_code', False):
        return jsonify({'error': 'No 2FA code generated'}), 404
    
    if code == decrypt(session.get('bank_2fa_code')):
        session['bank_2fa_verified'] = True
        return jsonify({'success': True})
    else:
        if 'bank_2fa_code' in session:
            del session['bank_2fa_code']
        return jsonify({'error': 'Invalid code'}), 401

@app.route('/api/release-funds', methods=['POST'])
def release_funds():
    if not session.get('bank_authenticated', False):
        return jsonify({'error': 'Access denied.'}), 403
    if not session.get('bank_2fa_verified', False):
        return jsonify({'error': 'Access denied.'}), 403
    
    return jsonify({'flag': BANK_FLAG})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True,threaded=Tru
```

<br>
<p>1.1. <em>What's the CODE_FLAG?</em><br>
<code>THM{••••••••••••••••••••••}</code></p>
<br>

<p align="center">/hopsecbank-12312497.db</p>

<img width="1603" height="205" alt="image" src="https://github.com/user-attachments/assets/caaf2107-34be-42d2-92d3-4f0f8a8a32cc" />

<br>
<br>
<br>
<p align="center">/hopflix-874297</p>

<img width="1606" height="226" alt="image" src="https://github.com/user-attachments/assets/a4f45f21-43ab-4ca3-b5cc-715bdd35bb4f" />

<br>
<br>
<br>

```bash
:~/BreachblockerUnlocker# ls
hopflix-874297.db  nginx.conf
```

<BR>
<p align="center">/hopflix-874297  > password_hash</p>

```bash
:~/BreachblockerUnlocker# sqlite3 hopflix-874297.db .dump
```

<img width="1771" height="208" alt="image" src="https://github.com/user-attachments/assets/79d18d39-b754-4d85-a5bf-117f1a0349c3" />

<br>
<br>
<br>
<p>Remember from <code>main.py</code>:<br>

- <strong>Hash-per-Character Expansion</strong>: &nbsp; The system expects the stored hash (<code>phash</code>) to be exactly 40 times longer than the input password (<code>pwd</code>), confirming that each individual character is represented by a 40-character SHA-1 hash.<br>
- <strong>Iterative Comparison</strong>: &nbsp; The <code>for</code> loop iterates through every character (<code>ch</code>) in the provided password.<br>
- <strong>Block Validation</strong>: &nbsp; For each character, it calculates a <code>hopper_hash</code> and compares it against the next 40-character block of the stored hash (<code>phash[:40]</code>).<br>
- <strong>Pointer Shifting</strong>: &nbsp; After a successful match, it "slices" the string (<code>phash[:40]</code>) to move to the next 40-character segment for the subsequent password character.</p>

```bash
if len(pwd)*40 != len(phash):
    return jsonify({'valid':False, 'error':'Incorrect Password'})

for ch in pwd:
    ch_hash = hopper_hash(ch)
    if ch_hash != phash[:40]:
        return jsonify({'valid':False, 'error':'Incorrect Password'})
    phash = phash[40:]
```

<br>
<p>
  
- Split the <code>password_hash</code> in blocks of <code>40</code> characters</p>

```bash
03c96ceff1a9758a1ea7c3cb8d43264616949d88
b5914c97bdedb1ab511a85c480d49b77c4977520
ebc1b24149a1fd25c37aeb2d9042d0d05492ba5c
19b23990d991560019487301ef9926d9d99a2962
b5914c97bdedb1ab511a85c480d49b77c4977520
7dc2d45214515ff55726de5fc73d5bd5500b3e86
fa6c34156f954d4435e838f6852c647621710420
7dc2d45214515ff55726de5fc73d5bd5500b3e86
504fa1cfe6a6f5d5c407f673dd67d71a34cbb077
2c21afa8b8f0b5e1c1a377b7168e542ea41f67a6
96e4c3dda73fa679990918ab333b6fab8c8e5f22
96e56d15f089c659a1bbc1d2b6f70b6c80720f1a
```


<p>

- Decode <strong>sbreachblocker@easterbunnies.thm</strong>´s password using a very simple script that I crafted.</p>

```bash
:~/BreachBlockerUnlocker$ python3 1.py
________________________________________________________________________________

TryHackMe BreachBlocker Unlock by Rosana
sbreachblocker@easterbunnies.thm contains  : 'm'
________________________________________________________________________________
```

```bash
:~/BreachBlockerUnlocker$ python3 2.py
________________________________________________________________________________

TryHackMe BreachBlocker Unlock by Rosana
sbreachblocker@easterbunnies.thm contains  : 'a'
________________________________________________________________________________
```

<img width="1346" height="249" alt="image" src="https://github.com/user-attachments/assets/4ab05d83-092e-443f-9a86-ee2c493c926a" />

<br>
<p>

- Execute it for each 40-character block<br>
- Navigate to the <strong>Hopflix</strong> application<br>
- Enter the credentials :<br>Username : <strong>sbreachblocker@easterbunnies.thm</strong><br>Password : <strong>ma..........</strong><br>
- Click <strong>Sign in...</strong><br>
- Discover the HOPFLIX_FLAG</p>

<img width="1584" height="818" alt="image" src="https://github.com/user-attachments/assets/05bbfb9e-85e4-40c5-9315-e30a73b1d8a0" />


<br>
<br>
<br>

<img width="1589" height="516" alt="image" src="https://github.com/user-attachments/assets/9debc99e-78de-4017-bcd5-172033c96d83" />

<br>
<br>
<br>

<img width="1582" height="825" alt="image" src="https://github.com/user-attachments/assets/98e3d72a-4919-4340-a0b8-cdd5ea45a8dd" />

<br>
<br>
<br>
<p>1.2. <em>What's the HOPFLIX_FLAG?</em><br>
<code>THM{•••••••••••••••••••••••}</code></p>
<br>

<p>
  
- Click <strong>Back</strong></p>


<img width="1582" height="321" alt="image" src="https://github.com/user-attachments/assets/f3ea8a77-1f39-4958-a192-692b8528d267" />

<br>
<br>
<br>
<p>

- Navigate to <strong>Settings</strong> > <strong>Security</strong> > <strong>Two-Factor Authentication</strong><br>
- Disable <strong>Two-Factor Authentication</strong></p>

<img width="1586" height="388" alt="image" src="https://github.com/user-attachments/assets/988dc8f2-4076-49c3-8ae3-f3aac8b32b5b" />


- Navigate to the <strong>Hopsec Bank</strong> application</p>

<img width="1590" height="336" alt="image" src="https://github.com/user-attachments/assets/e465b0b9-85e2-4fee-ab23-ff205e7dac60" />

<br>
<br>
<br>
<p>

- Enter the same credentials as before:<br>Account ID : <strong>sbreachblocker@easterbunnies.thm</strong><br>Pin / Password : <strong>ma..........</strong><br>
- Click <strong>Access Account</strong></p>

<img width="1593" height="622" alt="image" src="https://github.com/user-attachments/assets/1a5a5eff-6b3f-4559-a21c-c274fd58b2af" />

<br>
<br>
<br>
<p>

- Note that you will get the following message:<br>Select Authorized Email<br>Your account is shared. Any person in your authorized group or domain can receive an OTP for you. Who should receive this OTP?<br>
- Note that below the message you are able to select who should receive it through a pull down menu between <strong>carrotbane@easterbunnies.thm</strong> or <strong>malhare@easterbunnies.thm</strong><br>
- Select <strong>carrotbane@easterbunnies.thm</strong><br>
- <code>Inspect</code><br>
- Change <strong>carrotbane@easterbunnies.thm</strong> to <code>anyname</code>[<code>IP of Your Attack VM</code>](@easterbunnies.thm<br>
- Click <strong>ENTER</strong><br>
- Make sure you select <code>anyname</code>@easterbunnies.thm<br>
- Set up an <code>aiosmtpd</code> listerner<br>
- Click <strong>Send OTP</strong><br>
- Provide the 6-digit <strong>Two-Factor Authentication</strong> uncovered through <code>aiosmtpd</code><br>
- Click <code>Release Charity Funds</code></p>


<img width="1584" height="565" alt="image" src="https://github.com/user-attachments/assets/d3369c19-cd83-415b-9fc1-ead418770f9e" />

<br>
<br>
<br>

<img width="1591" height="629" alt="image" src="https://github.com/user-attachments/assets/d89205ae-1556-4f86-ab24-1f9c4a938f0e" />

<br>
<br>
<br>

```bash
:~/BreachblockerUnlocker# python3 -m aiosmtpd -n -l xx.xx.xxx.xxx:25
```

<img width="1182" height="345" alt="image" src="https://github.com/user-attachments/assets/aba69175-1e1f-48eb-b0c7-77fcc5b597ff" />

<br>
<br>
<br>

<img width="1155" height="314" alt="image" src="https://github.com/user-attachments/assets/4d518275-e4b4-4492-9046-a2e4aa633b8a" />

<br>
<br>
<br>

<img width="1183" height="764" alt="image" src="https://github.com/user-attachments/assets/e9c76908-aa53-4bfe-9b34-26e8027d77a8" />

<br>
<br>
<br>

<img width="1184" height="804" alt="image" src="https://github.com/user-attachments/assets/ea1bfaf0-2c43-4da0-b477-129ba8b2a78e" />

<br>
<br>
<p>1.3. <em>What's the BANK_FLAG?</em><br>
<code>THM{•••••••••••••••••}</code></p>
<br>
<br>
<br>
<h1 align="center">Challenge Completed</h1>


<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/70fa17ca-98ab-476d-a59f-072e9d4b00f6"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/a9fe9dcd-5e84-41b3-b07d-cc81c56901ee"></p>

<h1 align="center">My TryHackMe Journey ・ 2026, January</h1>

<div align="center"><h6>

| Date<br><br>   | Room <br><br> |Streak<br><br>   |Global<br>All Time|Brazil<br>All Time|Global<br>Monthly|Brazil<br>Monthly|Points<br><br>|Rooms<br>Completed|Badges<br><br>|
|:------:|:--------------------------------------|:--------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|
|13     |Hard 🚩 - Breachblocker Unlocker      |12 |     86ᵗʰ  |     3ʳᵈ    |      526ᵗʰ   |        5ᵗʰ     |    138,732  |    1,064    |    87     |
|11     |Medium 🚩 - Azure: Eyes Wide Shut     |10 |     86ᵗʰ  |     3ʳᵈ    |      558ᵗʰ   |        5ᵗʰ     |    138,450  |    1,063    |    86     |
|8      |Medium ⚙️ - Phishing Unfolding        | 7 |     86ᵗʰ  |     3ʳᵈ    |      508ᵗʰ   |        4ᵗʰ     |    138,372  |    1,062    |    84     |
|8      |Easy ⚙️ - Introduction to Phishing    | 7 |     96ᵗʰ  |     3ʳᵈ    |    2,479ᵗʰ   |       32ⁿᵈ     |    137,117  |    1,062    |    84     |
|8      |Medium 🔗 - KaffeeSec - SoMeSINT      | 7 |     98ᵗʰ  |     3ʳᵈ    |    2,847ᵗʰ   |       38ᵗʰ     |    137,052  |    1,062    |    84     |
|7      |Hard 🚩 - Hack Back                   | 6 |     98ᵗʰ  |     3ʳᵈ    |    2,798ᵗʰ   |       37ᵗʰ     |    136,908  |    1,061    |    84     |
|7      |Hard 🚩 - Dead End?                   | 6 |     99ᵗʰ  |     3ʳᵈ    |    2,924ᵗʰ   |       37ᵗʰ     |    136,788  |    1,060    |    84     |
|6      |Easy 🔗 - Linux Strength Training     | 5 |     98ᵗʰ  |     3ʳᵈ    |    3,172ⁿᵈ   |       47ᵗʰ     |    136,608  |    1,059    |    84     |
|4      |Medium 🚩 - JVM Reverse Engineering   | 3 |     96ᵗʰ  |     3ʳᵈ    |    3,031ˢᵗ   |       46ᵗʰ     |    136,450  |    1,058    |    84     |
|3      |Medium 🚩 - Carrotbane of My Existence| 2 |     96ᵗʰ  |     3ʳᵈ    |    3,468ᵗʰ   |       49ᵗʰ     |    136,150  |    1,057    |    84     |
|2      |Easy 🔗 - Learn Rust                  | 1 |     96ᵗʰ  |     3ʳᵈ    |    5,152ⁿᵈ   |       67ᵗʰ     |    136,030  |    1,056    |    84     |


</h6></div><br>


<p align="center">Global All Time:    86ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/3a1b1784-75e5-43a8-abc4-55bd039f0c00"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/8f0fd4f8-6508-4fb1-845b-ed3043d5a389"><br><br>
                  Brazil All Time:      3ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/b4586b14-c44a-4f9c-8228-3e60cf7bca06"><br><br>
                  Global monthly:     526ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/82f7e6af-54e6-4d18-9d31-1564bbbb56da"><br><br>
                  Brazil monthly:       5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/6cbc3c62-643b-41c9-9a5a-45cd64a03ee5"></p>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
