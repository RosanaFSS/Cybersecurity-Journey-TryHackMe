<h1 align="center">Island Orchestration</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/a11551ff-026d-4458-b5e4-3b15243ffccd"><br>
2025, October 6<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>517</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>Looking for the next holiday destination? Look no further than the Islands of Orchestration</em><br>
Access it <a href="https://tryhackme.com/room/islandorchestration"</a>here.<br>
<img width="1200px" src=""></p>


<h2>Task 1 . Challenge</h2>
<p>Check out the best tropical islands to visit on your next vacation!<br>

Please allow 4 to 5 minutes for the VM to boot.</p>


<p><em>Answer the question below</em></p>

<p>1.1. What is the flag:<br>
<code>*******************************</code></p>


<br>
<br>
<h1 align="center">Port Scanning → Service Discovery</h1>
<p align="center"><strong>3</strong> open ports</p>

<div align="center"><p>

| **Port**           | **Service**          | **Version**                     |
|-------------------:|:---------------------|:--------------------------------|
| `22`               |`SSH`                 |OpenSSH 7.6p1 Ubuntu 4ubuntu0.3  |
| `80`               |`HTTP`                |                                 |
| `8443`             |`SSL/HTTP`            |                                 |

</p></div><br>

```bash
:~/IslandOrchestration# nmap 10.201.84.25
...
PORT     STATE    SERVICE
22/tcp   open     ssh
80/tcp   filtered http
8443/tcp filtered https-alt
```

<img width="1275" height="274" alt="image" src="https://github.com/user-attachments/assets/16c93518-6033-49f5-94be-1b570f4179b6" />

<br>
<br>
<br>

<p>I opened a ticket because this challenge is "broken".<br>Enumerated many times and just port 22 is open</p>
