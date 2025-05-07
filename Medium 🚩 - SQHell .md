<p align="center">May 7, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{366}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="300px" src="" alt="Your Image Badge"><br></p>
<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{SQHell}}$$</h1>
<p align="center"><em>Try and find all the flags in the SQL Injections</em>.<br>
It is classified as a medium-level walkthrough.<br>
You can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed.<br>
Can be accessed clicking  <a href="https://tryhackme.com/room/sqhell</a>.</p>

<p align="center"> <img width="1000px" src="https://github.com/user-attachments/assets/8815edcb-552d-4ad4-807a-bd9c1b9a8dc3"> </p>


<br>
<br>

<h2>Task 1 . Find all the Fçags!</h2>
<p>Give the machine a minute to boot and then connect to http://MACHINE_IP<br><br>

There are 5 flags to find but you have to defeat the different SQL injection types.<br><br>

Hint: Unless displayed on the page the flags are stored in the flag table in the flag column.</p>


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

> 1.1. <em>Flag 1</em><a id='1.1'></a>
>> <code><strong>__________</strong></code><br>

<br>

> 1.2. <em>Flag 2</em>Hint : <em>Make sure to read the terms and conditions ;)</em><a id='1.2'></a>
>> <code><strong>T__________</strong></code><br>

<br>

> 1.3. <em>Flag 3</em><a id='1.3'></a>
>> <code><strong>___________</strong></code><br>

<br>

> 1.4. <em>Flag 4</em>Hint : <em>Well, dreams, they feel real while we're in them right?</em><a id='1.4'></a>
>> <code><strong>T__________</strong></code><br>

<br>

> 1.5. <em>Flag 5</em><a id='1.5'></a>
>> <code><strong>___________</strong></code><br>

<br>
<br>


<br>


<h3>---------- nmap -----------</h3>
<p>There is <code>nginx</code> in <code>80/tcp</code>.<br><br>
<code>nginx</code> works as a proxy server for as IMAP, POP3, and SMTP.</p>

<br>

```bash
~/SQHell# nmap -A TargetIP
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.1 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    nginx 1.18.0 (Ubuntu)
|_http-server-header: nginx/1.18.0 (Ubuntu)
|_http-title: Home
...
```

<br>

```bash
:~/SQHell# nmap -sC -sV -Pn -p- -T4 TargetIP
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.1 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    nginx 1.18.0 (Ubuntu)
|_http-server-header: nginx/1.18.0 (Ubuntu)
|_http-title: Home
...
```

<br>

```bash
:~/SQHell# nmap -A -Pn -p- TargetIP
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.1 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    nginx 1.18.0 (Ubuntu)
|_http-server-header: nginx/1.18.0 (Ubuntu)
|_http-title: Home
...
```

<h3>-------- gobuster ---------</h3>

<br>

```bash
:~/SQHell# gobuster dir -u http://TargetIP/ -w /usr/share/wordlists/dirb/common.txt -t 100
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://TargetIP/
[+] Method:                  GET
[+] Threads:                 100
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/login                (Status: 200) [Size: 1763]
/post                 (Status: 200) [Size: 21]
/register             (Status: 200) [Size: 2593]
/user                 (Status: 200) [Size: 21]
Progress: 4614 / 4615 (99.98%)
===============================================================
Finished
===============================================================
:~/SQHell# 
```

<h3>-------- <code>http://TargetIP</code> ---------</h3>
<p>Confirmed:<br>
- <code>/login</code><br>
- <code>/register</code></p>
<p>Discovered:<br>
- code>/user?id=1</code>:<code>admin</code><br>
- <code>/post?id=2"</code>.</p>

```bash
:~/SQHell# curl http://TargetI`P
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Home</title>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
</head>
<body>
<div class="pull-right" style="padding:15px">
    <a href="/login" class="btn btn-success">Login</a>
    <a href="/register" class="btn btn-info">Register</a>
</div>
<div class="container" style="padding-top:60px">
    <h1 class="text-center">My Blog</h1>
    <div class="row">
        <div class="col-md-8 col-md-offset-2">
                        <div class="panel panel-default">
                <div class="panel-heading">Second Post : by <a href="/user?id=1">admin</a></div>
                <div class="panel-body">
                    Etiam sit amet est in lacus ullamcorper luctus. Aliquam erat volutpat. Aliquam diam enim, consequat eget dui nec, congue porta enim. Integer venenatis dignissim erat, non elementum ante tincidunt a. Proin congue faucibus odio, at condimentum nibh hen [<a href="/post?id=2">Read More</a>]
                </div>
            </div>
                        <div class="panel panel-default">
                <div class="panel-heading">First Post : by <a href="/user?id=1">admin</a></div>
                <div class="panel-body">
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. In id mollis quam. Quisque quis enim eu velit dapibus dignissim quis id dolor. Sed volutpat, magna ut venenatis egestas, diam velit hendrerit nisl, ac suscipit lacus tortor ut nisi. Vestibulum  [<a href="/post?id=1">Read More</a>]
                </div>
            </div>
                    </div>
    </div>
    <div class="text-center"><a href="/terms-and-conditions">Terms &amp; Conditions</a></div>
</div>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
</body>
:~/SQHell# 

```

<br>


<h3>-------- <code>http://TargetIP/login</code> ---------</h3>

<br>

```bash
:~/SQHell# curl http:/TargetIP/login
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Login</title>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
</head>
<body>
<div class="pull-right" style="padding:15px">
    <a href="/login" class="btn btn-success">Login</a>
    <a href="/register" class="btn btn-info">Register</a>
</div>
<div class="container" style="margin-top:20px">
    <h1 class="text-center">Login</h1>
    <div class="row">
        <div class="col-md-6 col-md-offset-3">
            <ol class="breadcrumb">
                <li><a href="/">Home</a></li>
                <li class="active">Login</li>
            </ol>
                        <form method="post">
                <div class="panel panel-default" style="margin-top:50px">
                    <div class="panel-heading">Login</div>
                    <div class="panel-body">
                        <div><label>Username:</label></div>
                        <div><input class="form-control" name="username"></div>
                        <div style="margin-top:7px"><label>Password:</label></div>
                        <div><input type="password" class="form-control" name="password"></div>
                        <div style="margin-top:11px">
                            <input type="submit" class="btn btn-success pull-right" value="Login">
                        </div>
                    </div>
                </div>
            </form>
        </div>
    </div>
</div>
</body>
</html>root@ip-10-10-107-242:~/SQHell# 
```

<br>

<h3>-------- <code>http://TargetIP/login</code> ---------</h3>


<h3>-------- curl ---------</h3>


![image](https://github.com/user-attachments/assets/e77b5e17-671e-4036-a7ff-e8c2772b3b26)

