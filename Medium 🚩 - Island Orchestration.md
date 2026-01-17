<h1 align="center">Island Orchestration</h1>
<h3 align="center">Attempting to practice with this lab unsuccessfully. It seems to be broken.</h3>
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
<h1 align="center">Port Scanning</h1>
<p align="center"><strong>3</strong> open ports</p>

<div align="center"><p>

| **Port**           | **Service**          | **Version**                     |
|-------------------:|:---------------------|:--------------------------------|
| `22`               |`SSH`                 |OpenSSH 7.6p1 Ubuntu 4ubuntu0.3  |
| `80`               |`HTTP`                |Closed / Filtered (Not starting) |
| `8443`             |`HTTPS/ALT`           |Closed / Filtered (Not starting) |

</p></div><br>

```bash
:~/IslandOrchestration# nmap 10.201.84.25
...
PORT     STATE    SERVICE
22/tcp   open     ssh
80/tcp   filtered http
8443/tcp filtered https-alt
```



```bash
:~/IslandOrchestration$ nmap -sT -Pn -T4 10.66.155.123
...
PORT   STATE SERVICE
22/tcp open  ssh

Nmap done: 1 IP address (1 host up) scanned in 8.97 seconds
```

```bash
:~/Spring/IslandOrchestration$ sudo nmap -v10 -sC -sV -p22,80 -oA nse xx.xx.xxx.xxx
...
PORT   STATE  SERVICE REASON         VERSION
22/tcp open   ssh     syn-ack ttl 62 OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   3072 9f:ae:04:9e:f0:75:ed:b7:39:80:a0:d8:7f:bd:61:06 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADA...
|   256 cf:cb:89:62:99:11:d7:ca:cd:5b:57:78:10:d0:6c:82 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBDJH2hRXWCeM4AC7WvCY/PpWUXdSiNB+E05tW7LGCL0R6WTJLTCKpmKMWdaf3PbDMgPJlR9GzaPhOvUBFZ0uI8U=
|   256 5f:11:10:0d:7c:80:a3:fc:d1:d5:43:4e:49:f9:c8:d2 (ED25519)
|_ssh-...
80/tcp closed http    reset ttl 61
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```





<br>
<br>
<br>

<p>2025, Oct 6 -->I opened a ticket because this challenge is "broken".<br>Enumerated many times and just port 22 is open<br>
2025, Oct 18 --> Restarted the challenge and could not proceed due to the same reason.<br>
2026, Jan 16 -->  Restarted the challenge multiple times and could not proceed due to the same reason. The Kubernetes cluster inside the VM seems to fail during boot.</p>
