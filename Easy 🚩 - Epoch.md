<p align="center">April 13, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{342}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="300px" src="https://github.com/user-attachments/assets/7853bb5f-3f01-459c-8ff6-e37e175bd632" alt="Your Image Badge"><br>
<img width="200px" src="https://github.com/user-attachments/assets/962ae40d-abca-4ea0-9255-663cad56a1a5"></p>
<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Epoch}}$$</h1>
<p align="center"><em>Be honest, you have always wanted an online tool that could help you convert UNIX dates and timestamps!</em>.<br>
It is classified as an easy-level CTF.<br>It is premium: only for subscribers.<br>
Can be accessed clicking  <a href="https://tryhackme.com/room/epoch">here</a>.</p>

<p align="center"> <img width="900px" src="https://github.com/user-attachments/assets/0058d539-b29b-4000-af22-a21fa745fce9"> </p>


<br>
<br>

<h2>Task 1 . Epoch </h2>

<p>[  Start Machine  ]</p>


<p>Be honest, you have always wanted an online tool that could help you convert UNIX dates and timestamps! Wait... it doesn't need to be online, you say? Are you telling me there is a command-line Linux program that can already do the same thing? Well, of course, we already knew that! Our website actually just passes your input right along to that command-line program!<br><br>
Access this challenge by deploying both the vulnerable machine by pressing the green "Start Machine" button located within this task, and the TryHackMe AttackBox by pressing the  "Start AttackBox" button located at the top-right of the page.<br><br>

Navigate to the following URL using the AttackBox: http://TargetIP<br><br><br>

Check out similar content on TryHackMe:<br>

. Command Injection</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 1.1. <em>Find the flag in this vulnerable web application!</em> Hint : <em>The developer likes to store data in environment variables, can you find anything of interest there?</em><br><a id='1.1'></a>
>> <strong><code>flag{7da6c7debd40bd611560c13d8149b647}</code></strong><br>
<p></p>

<br>

<p>Used <code>nmap</code>.  Discovered:<br>
.  Ports <code>22</code> and <code>80</code> are open.<br>
.  <code>Supported Methods: GET HEAD</code>.<br></p>

<br>

![image](https://github.com/user-attachments/assets/53e60f01-24ac-4a88-8bc7-811061b0b402)

<br>



```bash
:~/Epoch# nmap -sC -sV -sS -Pn -A -p- -T4 10.10.121.208
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.4 (Ubuntu Linux; protocol 2.0)
80/tcp open  http
| fingerprint-strings: 
|   GetRequest: 
|     HTTP/1.1 200 OK
|     Date: Sun, 13 Apr 2025 ...
|     Content-Type: text/html; charset=utf-8
|     Content-Length: 1184
|     Connection: close
|     <!DOCTYPE html>
|     <head>
|     <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"
|     integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
|     <style>
|     body,
|     html {
|     height: 100%;
|     </style>
|     </head>
|     <body>
|     <div class="container h-100">
|     <div class="row mt-5">
|     <div class="col-12 mb-4">
|     class="text-center">Epoch to UTC convertor 
|     </h3>
|     </div>
|     <form class="col-6 mx-auto" action="/">
|     <div class=" input-group">
|     <input name="epoch" value="" type="text" class="form-control" placeholder="Epoch"
|   HTTPOptions, RTSPRequest: 
|     HTTP/1.1 405 Method Not Allowed
|     Date: Sun, 13 Apr 2025 ...
|     Content-Type: text/plain; charset=utf-8
|     Content-Length: 18
|     Allow: GET, HEAD
|     Connection: close
|_    Method Not Allowed
|_http-title: Site doesn't have a title (text/html; charset=utf-8).
```

<br>

<p>Navigated to <code>http://TargetIP</code></p>

<br>

![image](https://github.com/user-attachments/assets/f7269da5-ecc3-44ea-96e2-174c510abaff)

<br>

<p>Googled to know what is and <code>Epoch Converter</code>.</p>

<br>

![image](https://github.com/user-attachments/assets/4f36e95e-0c74-485b-8b34-2ba76450db62)

<br>

<p>For exampled here is an online <code>Epoch Converter</code> app -----> https://www.epochconverter.com/</p>

<br>

<p>Entered <code>1743543172</code> that means <code>Sun, 1 Apr 2025 21:32:52 GMT</code>.<br>
Worked smoothly .... but<br>
Discovered <code>/?epoch=</code>, and in this room introduction there is a suggestion: <code>Check out similar content on TryHackMe: Command Injection</code></p></code>.</p>


![image](https://github.com/user-attachments/assets/01875d7d-3f37-4127-b15c-7ee30306d874)


<br>

<p>Tried <code>1743543172;ls</code>.</p>

<br>

![image](https://github.com/user-attachments/assets/ed4105a5-21c8-41bc-8f1d-31ad9f472833)

<br>

<p>Tried <code>1743543172;ls -la /home</code>.</p>

<br>

![image](https://github.com/user-attachments/assets/5ab3ff85-b1b8-495c-a097-9746aa3eca73)

<br>

<p>Set up a listener.</p>

<p>Tried <code>1743543172;ls -la /home/challenge</code>.<br><br>
Got the shell.</p>

<br>

![image](https://github.com/user-attachments/assets/f2d33fbd-fb11-433b-baa0-3ecec8898c44)

<br>

![image](https://github.com/user-attachments/assets/274b1f88-d74f-46b6-b00d-6cb2d32d9b1f)

<br>

<p>Used command <code>printenv</code> because in the hint there is: <code>The developer likes to store data in environment variables, can you find anything of interest there?</code></p>

<br>

![image](https://github.com/user-attachments/assets/3249ad4c-0573-4b44-825f-5a812f311407)




<br>
<br>


<br>
<br>


<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Room Completed}}$$</h1>
<br>
<p align="center">
<img width="900px" src="https://github.com/user-attachments/assets/4493b313-6ee2-4a37-85d8-64779999ce98"><br>
<img width="900px" src="https://github.com/user-attachments/assets/b9ce85b2-cd94-476b-aa67-da8e5a73306c"></p>


<br>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{My TryHackMe Journey}}$$ </h1>
<br>


<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |Global        | Brazil       | Global      | Brazil     |          | Completed |           |
| April 13, 2025    | 342      |     286ᵗʰ    |        8ᵗʰ   |    217ᵗʰ    |     2ⁿᵈ    |  93,198  |       656 |   59      |

</div>

<br>



<p align="center"> Global All Time: 290ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/72d1031c-d96b-4bdc-b5cd-1a913b198b75"> </p>

<p align="center"> Brazil All Time: 8ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/9fb390af-8d36-419b-966f-385c4e473fb8"> </p>

<p align="center"> Global monthly: 217ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/0739ecfe-df6d-46d9-b8a3-31db605b53326"> </p>

<p align="center"> Brazil monthly: 2ⁿᵈ<br><br><img width="900px" src="https://github.com/user-attachments/assets/a6c2f602-87bf-47e7-a4eb-bc16eaa9d4fd"> </p>


<br>

![image](https://github.com/user-attachments/assets/f65c56a0-5fdd-43e5-bc08-cd03cf2458a2)



<p align="center">Weekly League: 3ʳᵈ Bronze<br><br><img width="900px" src="https://github.com/user-attachments/assets/f65c56a0-5fdd-43e5-bc08-cd03cf2458a2"> </p>

<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thanks for coming!!!}}$$</h1>

<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 

<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thank you}}$$</h1>
<p align="center"><a href="https://tryhackme.com/p/cmnatic">cmnatic</a>  for investing your time and effort to develop this walkthrough so that I could sharpen my skills!</p> 
