<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Kubernetes for Everyone}}$$</h1>
<p align="center"><img width="200px" src="https://github.com/user-attachments/assets/dea7aa5d-00b4-4a3a-a417-28d7040d7c9c"><br>
May 27, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my $$\textcolor{#FF69B4}{\textbf{386}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a><br>
A Kubernetes hacking challenge for DevOps/SRE enthusiasts. Access it clicking <a href="https://tryhackme.com/room/kubernetesforyouly"</a>here.<br><br>
<img width="1000px" src=""></p>

<br>
<br>




<h2>Task 1 . Access the Cluster</h2>

<p>To access a cluster, you need to know the location of the K8s cluster and have credentials to access it. Compromise the cluster and best of luck.<br><br>

Use Nmap to find open ports and gain a foothold by exploiting a vulnerable service. If you are new at Nmap, take a look at the <code>Nmap room</code>.</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>


> 1.1. <em>Find the username?</em><br><a id='1.1'></a>
>> <strong><code>______</code></strong><br>
<p></p>


<br>

> 1.2. <em>Find the username?</em><br><a id='1.2'></a>
>> <strong><code>______</code></strong><br>
<p></p>


<br>

<h3>nmap</h3>


```bash
:~/Kubernetes-for-Everyone# nmap -sS -sV -Pn -p- -T4 TargetIP
...
PORT     STATE SERVICE           VERSION
22/tcp   open  ssh               OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
111/tcp  open  rpcbind           2-4 (RPC #100000)
3000/tcp open  ppp?
5000/tcp open  http              Werkzeug httpd 2.0.2 (Python 3.8.12)
6443/tcp open  ssl/sun-sr-https?
2 services unrecognized despite returning data. If you know the service/version, please submit the following fingerprints at https://nmap.org/cgi-bin/submit.cgi?new-service :
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
```


<br>
<br>



<h2>Task 2 . Mobile Devices Within Digital Forensics</h2>
