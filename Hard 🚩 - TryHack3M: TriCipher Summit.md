<h1 align="center">TryHack3M: TriCipher Summit</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/c343b580-87d4-41ba-8608-536321007e44"><br>
2025, September 13<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>495</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>Reach the apex of this triple-crypto challenge</em>!<br>
Access it <a href="https://tryhackme.com/room/tryhack3mencryptionchallenge">here</a>.<br>
<img width="1200px" src=""></p>


<h1>Task 1 .Find the TryHack3M Flags</h1>
<p>Step into the realm of TryHackM3 as we approach 3 million users, where '3 is the magic number'! Embark on the TryHackM3 challenge, intercepting credentials, cracking custom crypto, hacking servers, and breaking into smart contracts to steal the 3 million. Are you ready for the cryptography ultimate challenge?<br>

In this challenge, you will be expected to:<br>

- Perform supply chain attacks<br>
- Reverse engineer cryptography<br>
- Hack a crypto smart contract<br>

Press the Start Machine button and wait at least 5 minutes for the VM to boot up properly.</p>

<p><em>Answer the questions below</em></p>

<p>1.1. What is Flag 1?<br>
<code></code></p>

<p>1.2. What is Flag 2?<br>
<code></code></p>



<p>1.3. What is Flag 3?<br>
<code></code></p>


<h2>nmap</h2>
<p>

- &nbsp;&nbsp;22 &nbsp; ・ &nbsp; ssh<br>
- &nbsp;&nbsp;80 &nbsp; ・ &nbsp; http &nbsp; ・ &nbsp; WebSockify Python/3.8.10<br>
- &nbsp;443 &nbsp; ・ &nbsp; ssl/http &nbsp; ・ &nbsp; nginx 1.25.4<br>
- 5000 &nbsp; ・ &nbsp; ssl/upnp? &nbsp; ・ &nbsp; Werkzeug/3.0.2 Python/3.8.10 &nbsp; ・ &nbsp; ECorp Super Secret Super Secure Login<br>
- 8000 &nbsp; ・ &nbsp; http &nbsp; ・ &nbsp; nginx 1.25.4<br>
- 9444 &nbsp; ・ &nbsp; http &nbsp; ・ &nbsp; wso2esb-console?</p>


```bash
:~/TriCipherSummit# nmap -sC -sV -Pn -n -p- -T4 10.201.48.84
Starting Nmap 7.80 ( https://nmap.org ) at 2025-09-14 00:39 BST
NSOCK ERROR [102.4220s] mksock_bind_addr(): Bind to 0.0.0.0:81 failed (IOD #119): Address already in use (98)
Nmap scan report for 10.201.48.84
Host is up (0.0069s latency).
Not shown: 65529 closed ports
PORT     STATE SERVICE          VERSION
22/tcp   open  ssh              OpenSSH 8.2p1 Ubuntu 4ubuntu0.11 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http             WebSockify Python/3.8.10
| fingerprint-strings: 
|   GetRequest: 
|     HTTP/1.1 405 Method Not Allowed
|     Server: WebSockify Python/3.8.10
|     Date: Sat, 13 Sep 2025 23:39:59 GMT
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
|     Date: Sat, 13 Sep 2025 23:39:59 GMT
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
|     Date: Sat, 13 Sep 2025 23:40:13 GMT
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
|     Date: Sat, 13 Sep 2025 23:40:13 GMT
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
| Not valid before: 2025-09-13T23:35:12
|_Not valid after:  2026-09-13T23:35:12
8000/tcp open  http             nginx 1.25.4
|_http-server-header: nginx/1.25.4
|_http-title: Site doesn't have a title (application/xml).
9444/tcp open  wso2esb-console?
| fingerprint-strings: 
|   GetRequest: 
|     HTTP/1.1 200 OK
|     Content-Type: application/xml
|     cache-control: no-cache, max-age=0
|     last-modified: Sat, 13 Sep 2025 23:40:08 GMT
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
|     last-modified: Sat, 13 Sep 2025 23:40:09 GMT
|     cache-control: no-cache, max-age=0
|     set-cookie: NINJA_SESSION=5c98e1c580fd3567991fd6bdea13b9d8d5b475d3d6b3b9c31df74ec380d03f2e6e2b9fa579cd43d04dd6ea839bba284db20748f9b2ada779072aeccb35813c01:?previousCSRFToken=&CSRFToken=b1105c3e-e58f-4220-89e4-81d6b2ba8ed4&lastCSRFRecompute=1757806809026; Max-Age=7776000; Expires=Fri, 12 Dec 2025 23:40:09 GMT; Path=/; HTTPOnly; SameSite=Lax
     server: 7cbb9dd73e39
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

<h2>Web port 80</h2>
<p>

- <code>Advanced ...</code><br>
- <code>Accept the Risk and Continue</code><br>
- visit the admin UI</p>

<img width="1056" height="373" alt="image" src="https://github.com/user-attachments/assets/9d5cc57f-f617-498e-afff-4a532445daec" />

<br>
<br>
<p>

- View Certificate<br>
- identify <code>cdn.tryhackm3.loc</code></p>

<img width="1053" height="644" alt="image" src="https://github.com/user-attachments/assets/4b5bde9b-746a-4bdd-a879-e5262318d2d1" />

<br>
<br>

<img width="990" height="625" alt="image" src="https://github.com/user-attachments/assets/fc7ae654-8eee-440f-89a9-b0569cb2716b" />


<br>
<br>
<h2>/ui</h2>
<p>

- S3 ninja<br>
- Version: 8.3.3., Build: 433 (2024-02-14 10:40), Revision: 75e012cb6689de1921bd07a07c5c886d0a683866<br>
- Storage Path: /home/sirius/data (Free: 31.49 GB)<br>
- Access Key: AKIAIOSFODNN7EXAMPLE<br>
- Secret Key: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY</p>


<img width="1056" height="514" alt="image" src="https://github.com/user-attachments/assets/3f36f360-fdf5-4413-9af6-b767af87daf5" />

<br>
<br>
<h2>/ui/libraries</h2>

<p>

- <code>Make private</code><br>
- <code>Upload file</code><br>
- auth.js<br>
- form-submit.js<br>
- Actios: Properties, Delete<br>
- Fork me on GitHub: https://github.com/scireum/s3ninja<<br>
- Supported API: Supported Object Methods, Supported Multipart Methods<br>
- Access Logs: identified many occurences of form-submit.js.</p>

<img width="1052" height="638" alt="image" src="https://github.com/user-attachments/assets/920a3921-8207-4ab3-9765-44d1f7254b1b" />

<br>
<br>

<img width="1056" height="721" alt="image" src="https://github.com/user-attachments/assets/f4e87b09-609b-4e00-8ac2-734a86b253ca" />

<br>
<br>

<img width="1060" height="725" alt="image" src="https://github.com/user-attachments/assets/63e74ce1-53b4-42be-9aed-49616ed54090" />

<br>
<br>

<h2>/ui/libraries/form-submit.js</h2>

```bash
const form = document.querySelector('#login-form');
const privkey = `MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCuL9Yb8xsvKimy
lR/MJB2Z2oBXuIvIidHIVxf7+Sl3Y35sU53Vd+D1QOuJByvpLmpczYsQkUMJmKha
36ibC2gjBMlTlZJ0OwnjG+Na0libW9fnWZVKq0JuAhyJd9OUyO0Up1hk2W6/1abU
OuEcYn1CTdYrTq7pdRhKLp2kYfVo64oV+NPDgQWvaIyR9vdEA+tGa4bgm5BQENaw
0Uh6qrtBh8pFKDX9EMEizauhRAsOUVlZ6ZYWCiT+A+IGZHpzFIXWh0gRbIANDZAd
g+CATLT/jee9wi0Vvg7L4o/Xn293SIAXYK7NYEHwMZP/SSmtcasYSFfgFvZ3BX+j
OLNynG5lAgMBAAECggEABXwFGlEvwG7r7C8M1sEmW3NJSjnJ0PEh9VRksW7ZcuRj
lSaW2CNTpnU6VVCv/cIT4EMqh0WDnlg7qMzVAri7uSqL6kFR4K4BNDDrGi94Ub/1
Dtg/vp+g0lTnsB5hP5SJ/nX8bwR3m7uu6ozGDL4/ImjP/wIVuM0SjDdmiEf7UafX
iWE12Lq5RbsHnvcXte2wl09keRszatRk/ODrqMPxzjS1NSt6KBfxtiRPNB+GZt1y
DhYKaHEO0riDsUiXurMwt7bAlupiiIS0pDAfNDEnvc2gWaiir8pIFGezowd+sIOd
XSW3aJU2Y5ByroelgkovRNIpF2QPXfFSsHyzx5uQawKBgQDsnwAuzp07CaHrXyaJ
HBno149LOaGYzRucxdKFFndizY/Le7ONl4PujRV+dwATAnuo8WIz7Upitd1uuh+H
0n37G4gaKIPK0o/pNYgIpMAoWSRI9zkPyId8yBEcpMJiUYXhXziQHhYhJ3shzn/2
Rh5RDS31tCxykpe5AHATw+R60wKBgQC8c9bPRNakEftP4IkC5wriHXpwEXYWRmCf
rRmeJmfApUgGfnAWzWBu1D5eHZU5z+6iojSSyxZSGJfKedON6loySWww/ZF/1QqQ
xkS+E3S86jp1PeJVYu2DuYhfcb8AXjt4ed48DNEMR5XZeWIKCYLsACHmag1IR9cW
XmCgovO+5wKBgQDJaVp1fUfW3g8m07pwkSv4x6vgg3DrKQPtAXJ9+K6sun9A3M3s
o2EY6Jy4JkE47S8nkjheLQjZVybiPqniKik0Wq4SXhQ4y9zVzMw7V0l9zssVFONM
bQvvCjmOoSwZFn2YZj42ZnW9yOaF00mW7v6VTVumvrPq3p8pSZcdK+zLIwKBgQCm
qiwIEvFhGSYRdpq1nm/Zmgh2pHqzKHq7vPMzEvQfRA128Mtg3zGx0rN1uOQIxQRf
gOTODh4nbOiRgTy//crXPmgYy6iqTVeSwkZ5c+uCSAR7O8e3jE5SePtKreYmBTDD
U8Rfh1Y6bfTw6JD0H4VSAqv4g0JL8n0eo0kByBuZcQKBgGdaG1XJZbK4a1fQ3scR
sv8Z+HgkaKS1FY0nXShNwFaE4Tfk6f/gsTgNqbyhk+HsFelmxKoFgf0Sa7313TPR
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

```bash
:~/TriCipherSummit# wget https://xx.xxxx.xx.xx/ui/libraries/form-submit.js -o form-submit.js
```

<p>

- downloaded form-submit.js<br>
- added <code>//</code><br>
- uploaded updated form-submit.js in https://xx.xxx.xx.xx/ui/</p>

<img width="1019" height="167" alt="image" src="https://github.com/user-attachments/assets/ac5d3251-321d-4dab-a191-3b1ac8bcfeef" />


<h2>/etc/hosts</h2>

```bash
xx.xxx.xx.xx cdn.tryhackm3.loc
```

<h2>cdn.tryhackm3.loc:5000</h2>
<p></p>


```bash


```


```bash


```


```bash


```


```bash


```


```bash


```


```bash


```








