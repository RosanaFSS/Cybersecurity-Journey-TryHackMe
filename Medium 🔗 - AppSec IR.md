<h1 align="center">AppSec IR</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/0bea92e5-a71d-4ca6-a97f-8ac51f307026"><br>
2025, September 15<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>497</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>An introduction into the overlapping worlds of AppSec and IR</em>.<br>
Access it <a href="https://tryhackme.com/room/appsecir">here</a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/a42c0e98-ecbc-4fb3-978d-04de2910ecfb"></p>

<h1>Task 1 . Introduction</h1>


<p><em>Answer the question below</em></p>


<h1>Task 2 . AppSec IR Fundamentals</h1>


<p><em>Answer the questions below</em></p>



<h1>Task 3 . Preparing for Application Incidents</h1>


<p><em>Answer the questions below</em></p>


<h1>Task 4 . Responding to an Application Incident</h1>


<p><em>Answer the questions below</em></p>


<h1>Task 5 . Remediation & Recovery</h1>


<p><em>Answer the questions below</em></p>



<h1>Task 6 . Practical</h1>


<p><em>Answer the questions below</em></p>

<p>Can you investigate the incident, confirm the presence of an application vulnerability, and then answer all the questions to obtain the flag?<br>
<code></code>THM{*************************}</code></p>

<br>

<img width="832" height="695" alt="image" src="https://github.com/user-attachments/assets/c557ae00-ebb5-4297-87a9-601d30b3ecb3" />

<br>
<br>

<img width="828" height="591" alt="image" src="https://github.com/user-attachments/assets/a5b34c48-22b4-4f02-a994-e422bbf57e13" />

<br>
<br>

<h2>Preparation</h2>
<p>What should have been in place to prevent the discovered vulnerability from reaching production? Select two.</p>

[ ] Authentication middleware on all routes<br>
[x] Secure coding practices and code review<br>
[ ] Logging and alerting in production<br>
[x] A threat model identifying access control flaws<br>
[ ] Asset inventory of all public endpoints<br>
[ ] Input sanitization on all user fields<br>

<br>
<h2>Detection & Identification</h2>

<p>What vulnerability did you identifify?<br>
<code>IDOR</code></p>

<p>At what time did the attacker successfully authenticate into an account that wasn´t their? (YYYY-MM-DD HH:MM:SS)<br>
<code>2025-08-24 19:17:32</code></p>


<p>What is the user email attached to user with account ID 105?<br>
<code>john.doe@company.thm</code>
</p>


<br>
<h2>Containment</h2>

<p>Can you disable the affected endpoint using the admin user with user ID 999?<br>
<code>IDOR</code></p>


<br>
<h2>Eradication - Fix the Root Cause</h2>

<p>What should be recommended to the web develipment team to fix the IDOR vulnerability?</p>

[ ] Sanitize all user inputs<br>
[ ] Add authentication middleware to the /users/:id/profile endpoint<br>
[x] Enforce server-side validation that the session user matches the requested user ID<br>
[ ] Change the HTTP method from GET to POST<br>


<br>
<h2>Recovery</h2>
<p>What log pattern or keyword should be monitored after the patch is deployed? <em>Check the audit trail for the first unauthorized profile view - use the value in the msg fields as your monitoring keyword.</em><br>
<code>user_id mismatch</code></p>

```bash
{"event_id":"3d4e5f60-7182-93a0-b1c2-d3e4f5a61016","ts":"2025-08-24T19:17:32Z","level":"WARN","logger":"security.audit","msg":"user_id mismatch","src_ip":"203.0.113.56","method":"GET","path":"/users/103/profile","status":200,"response_ms":34,"session_id":"8a2a9e9b-5b7f-4c0a-9a3b-1d2e3f4a1010","auth":{"user_id":106,"email":"sam.jones@company.thm"},"requested_user_id":103,"accessed_profile":{"user_id":103,"email":"aaron.miller@company.thm","name":"Aaron Miller","account_tier":"Pro"},"rule":"ACCESS_CONTROL_VIOLATION","alert":"access_control_violation"}
```

<br>
<h2>IR Follow-Up</h2>
<p>What document should be updated after this incident to include IDOR response procedures?<br>
<code>IR playbook</code></p>


<br>
<h2>Post-Incident Summary Report</h2>
<p>An Insecure <strong>Direct Object Reference (IDOR)</strong> vulnerability was identified in the /users/:id/profile endpoint. This allowed authenticated users to access the profiles of other users by altering the user ID in the URL without proper authorisation enforcement.

<h4>Confirmed Vulnerability:</h4>
<p>

- <strong>Type</strong>: IDOR (Insecure Direct Object Reference)<br>
- <strong>Affected Endpoint</strong>: /users/:id/profile<br>
- <strong>Attacker Activity</strong>: Confirmed unauthorised access to another user's account<br>
- <strong>Affected User</strong>: Account ID 103 - Email: aaron.miller@company.thm</p>

<h4>Containment Action:</h4>
<p>The vulnerable profile endpoint was <strong>successfully disabled</strong>, halting further unauthorised access during the investigation.</p>

<h4>Eradication Recommendation:</h4>
<p>Implement <strong>server-side validation</strong> to ensure the session user matches the user ID requested in the URL.

<h4>Recovery Considerations</h4>
<p>
  
- <strong>Monitoring Guidance</strong>: Add detection logic to monitor for the keyword: user_id mismatch in application logs post-deployment to identify future access control violations.<br>
- <strong>Playbook Update</strong>: Update the Incident Response Playbook to include detection, triage, and containment guidance for IDOR-style access control issues.</p>


<p>What document should be updated after this incident to include IDOR response procedures?<br>
<code>IR playbook</code></p>

<h2 align="center">nmap</h2>

<p>

- <strong>Port 80</strong> : Runs Nginx 1.24.0, likely hosting the main web service and primary attack vector.
Ports 88, 389, 445, 464, 3268: Indicate this is a domain controller for the domain university.htb, with Kerberos, LDAP, SMB, and password services active.
</p>

```bash
:~/AppsecIR# nmap -sC -sV -Pn -n -p- -T4 partpickerparadise.thm
...
PORT    STATE  SERVICE VERSION
22/tcp  open   ssh     OpenSSH 9.6p1 Ubuntu 3ubuntu13.11 (Ubuntu Linux; protocol 2.0)
80/tcp  open   http    nginx 1.24.0 (Ubuntu)
|_http-server-header: nginx/1.24.0 (Ubuntu)
|_http-title: PartPickerParadise
443/tcp closed https
```

<h2 align="center">/etc/hosts</h2>

```bash
xx.xxx.xx.xxx  partpickerparadise.thm
```

<h2 align="center">Web 80</h2>

<img width="1059" height="437" alt="image" src="https://github.com/user-attachments/assets/ae714f03-9891-4b8f-b1d6-9fb57a92bec6" />

<br>
<br>

<p>
  
- Identified Broken Access Control</p>

<h2 align="center">http://partpickerparadise.thm/assets/index-1rIfu-CQ.js</h2>

```bash
Incident Responder",username:"Incident_Responder",password:"incident123",email:"incident_responder@company.thm",phone:"(555) 123-4567",address:"123 Security Lane, Cyber City, CC 12345",ssn:"***-**-4567",creditCard:"****-****-****-4567",role:"Security Analyst",department:"Information Security",joinDate:"2023-01-15",isAdmin:!1},


101:{id:101,name:"Jessica Warner",username:"jessica",password:"jessica123",email:"jessica@company.thm",phone:"(555) 234-5678",address:"456 Employee St, Business City, BC 67890",ssn:"123-45-6789",creditCard:"4532-1234-5678-9012",role:"Software Developer",department:"Engineering",joinDate:"2022-03-22",isAdmin:!1},
102:{id:102,name:"Bob Williams",username:"bob",password:"bob123",email:"bob.williams@company.thm",phone:"(555) 345-6789",address:"789 Worker Ave, Corporate Town, CT 13579",ssn:"987-65-4321",creditCard:"5555-4444-3333-2222",role:"Marketing Manager",department:"Marketing",joinDate:"2021-07-10",isAdmin:!1},
103:{id:103,name:"Aaron Miller",username:"aaron",password:"aaron123",email:"aaron.miller@company.thm",phone:"(555) 456-7890",address:"321 Office Rd, Enterprise City, EC 24680",ssn:"555-44-3333",creditCard:"4111-1111-1111-1111",role:"HR Specialist",department:"Human Resources",joinDate:"2020-11-05",isAdmin:!1},
104:{id:104,name:"David Brown",username:"david",password:"david123",email:"david.brown@company.thm",phone:"(555) 567-8901",address:"654 Business Blvd, Company City, CC 97531",ssn:"777-88-9999",creditCard:"3782-822463-10005",role:"Finance Analyst",department:"Finance",joinDate:"2019-09-18",isAdmin:!1},
105:{id:105,name:"John Doe",username:"john",password:"john1234",email:"john.doe@company.thm",phone:"(555) 567-8901",address:"654 Business Blvd, Company City, CC 97531",ssn:"123-45-6789",creditCard:"4532-1234-5678-9012",role:"Software Developer",department:"Engineering",joinDate:"2019-09-18",isAdmin:!1},
106:{id:106,name:"Sam Jones",username:"sam",password:"sam1234",email:"sam.jones@company.thm",phone:"(555) 567-8901",address:"654 Business Blvd, Company City, CC 97531",ssn:"123-45-6789",creditCard:"4532-1234-5678-9012",role:"Software Developer",department:"Engineering",joinDate:"2019-09-18",isAdmin:!1},
999:{id:999,name:"System Administrator",username:"admin",password:"admin123",email:"admin@company.thm",phone:"(555) 999-0000",address:"1 Admin Plaza, Control Center, CC 00001",ssn:"000-00-0001",creditCard:"0000-0000-0000-0001",role:"System Administrator",department:"IT Operations",joinDate:"2018-01-01",isAdmin:!0}},nn={HOME:"/",LOGIN:"/login",PROFILE:"/users/:id/profile",FLAG_SUBMISSION:"/flag-submission"},$2=[{name:"Ryzen 5 5600X",description:"6-Core, 12-Thread Unlocked Desktop Processor",price:299.99,image:"gpu.png",category:"Minuteman's Armoury"},{name:"Intel Core i7-12700K",description:"12th Gen Intel Core i7 Processor",price:419.99,image:"cpu.png",category:"Minuteman's Armoury"},{name:"Ryzen 9 5900X",description:"12-
```

<h2 align="center">http://partpickerparadise.thm/login</h2>

<img width="1050" height="432" alt="image" src="https://github.com/user-attachments/assets/1bedf954-af9e-45a2-a363-650787940540" />


<br>
<br>

<img width="1051" height="111" alt="image" src="https://github.com/user-attachments/assets/c0b92de6-3dc5-4d11-ba36-92b57723444c" />

<br>
<br>

<img width="1053" height="446" alt="image" src="https://github.com/user-attachments/assets/18623867-8884-4cb1-b73c-8050f43d797a" />

<br>
<br>

<img width="1053" height="428" alt="image" src="https://github.com/user-attachments/assets/f64346a4-bad3-4be0-8b5a-89cd7d94492a" />

<br>
<br>

<img width="1052" height="433" alt="image" src="https://github.com/user-attachments/assets/3f57cb33-8a93-4e4f-b360-ae01c3dcd440" />


<br>
<br>

<img width="1053" height="360" alt="image" src="https://github.com/user-attachments/assets/963cffc5-7a89-40bd-81ce-57a83e8db8ca" />





<h2 align="center">dirsearch</h2>
<p>

- /assets/<br>
- /images</p>

```bash
:~/AppSecIR# dirsearch -u http://partpickerparadise.thm/ -i200,301,02,401 -w /usr/share/wordlists/dirb/common.txt
...
[xx:xx:xx/ 201  -  178B  -  /assets  ->  http://partpickerparadise.thm/assets/
[xx:xx:xx/ 201  -  178B  -  /images  ->  http://partpickerparadise.thm/images/

Task Completed
```

<h2 align="center">appsecir</h2>


```bash
:~/AppSecIR# ssh appsecir@partpickerparadise.thm
...
appsecir@tryhackme-2404:~$ id
uid=1001(appsecir) gid=1001(appsecir) groups=1001(appsecir),100(users)
appsecir@tryhackme-2404:~$ pwd
/home/appsecir
```

<h2>linpeas</h2>

```bash

[+] Analyzing .service files
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#services
/run/user/1001/systemd/generator.late/app-snap\x2duserd\x2dautostart@autostart.service
/run/user/1001/systemd/generator.late/app-xdg\x2duser\x2ddirs@autostart.service
/run/user/1001/systemd/generator.late/xdg-desktop-autostart.target.wants/app-snap\x2duserd\x2dautostart@autostart.service
/run/user/1001/systemd/generator.late/xdg-desktop-autostart.target.wants/app-xdg\x2duser\x2ddirs@autostart.service
You can't write on systemd PATH so I'm not going to list relative paths executed by services

...
[+] Users with console
appsecir:x:1001:1001:,,,:/home/appsecir:/bin/bash
root:x:0:0:root:/root:/bin/bash
ubuntu:x:1000:1000:Ubuntu:/home/ubuntu:/bin/bash

...
[+] All users & groups
uid=0(root) gid=0(root) groups=0(root)
uid=1(daemon) gid=1(daemon) groups=1(daemon)
uid=10(uucp) gid=10(uucp) groups=10(uucp)
uid=100(systemd-network) gid=102(systemd-network) groups=102(systemd-network)
uid=1000(ubuntu) gid=1000(ubuntu) groups=1000(ubuntu),4(adm),20(dialout),24(cdrom),25(floppy),27(sudo),29(audio),30(dip),44(video),46(plugdev),117(netdev),118(lxd)
uid=1001(appsecir) gid=1001(appsecir) groups=1001(appsecir),100(users)
uid=101(systemd-resolve) gid=103(systemd-resolve) groups=103(systemd-resolve)
uid=102(systemd-timesync) gid=104(systemd-timesync) groups=104(systemd-timesync)
uid=103(messagebus) gid=106(messagebus) groups=106(messagebus)
uid=104(syslog) gid=110(syslog) groups=110(syslog),4(adm),5(tty)
uid=105(_apt) gid=65534(nogroup) groups=65534(nogroup)
uid=106(tss) gid=111(tss) groups=111(tss)
uid=107(uuidd) gid=112(uuidd) groups=112(uuidd)
uid=108(tcpdump) gid=113(tcpdump) groups=113(tcpdump)
uid=109(sshd) gid=65534(nogroup) groups=65534(nogroup)
uid=110(landscape) gid=115(landscape) groups=115(landscape)
uid=111(pollinate) gid=1(daemon) groups=1(daemon)
uid=112(ec2-instance-connect) gid=65534(nogroup) groups=65534(nogroup)
uid=113(fwupd-refresh) gid=119(fwupd-refresh) groups=119(fwupd-refresh)
uid=114(dhcpcd) gid=65534(nogroup) groups=65534(nogroup)
uid=13(proxy) gid=13(proxy) groups=13(proxy)
uid=2(bin) gid=2(bin) groups=2(bin)
uid=3(sys) gid=3(sys) groups=3(sys)
uid=33(www-data) gid=33(www-data) groups=33(www-data)
uid=34(backup) gid=34(backup) groups=34(backup)
uid=38(list) gid=38(list) groups=38(list)
uid=39(irc) gid=39(irc) groups=39(irc)
uid=4(sync) gid=65534(nogroup) groups=65534(nogroup)
uid=41(gnats) gid=41(gnats) groups=41(gnats)
uid=5(games) gid=60(games) groups=60(games)
uid=6(man) gid=12(man) groups=12(man)
uid=65534(nobody) gid=65534(nogroup) groups=65534(nogroup)
uid=7(lp) gid=7(lp) groups=7(lp)
uid=8(mail) gid=8(mail) groups=8(mail)
uid=9(news) gid=9(news) groups=9(news)
uid=997(polkitd) gid=997(polkitd) groups=997(polkitd)
uid=998(lxd) gid=100(users) groups=100(users)
uid=999(systemd-coredump) gid=999(systemd-coredump) groups=999(systemd-coredump)

...
[+] Searching Cloud-Init conf file
Found readable /etc/cloud/cloud.cfg
    lock_passwd: True
    groups: [adm, cdrom, dip, lxd, sudo]
    sudo: ["ALL=(ALL) NOPASSWD:ALL"]
```

<br>
<h1>Task 7 . Conclusion</h1>
<h2>Turning Incidentes Into Win-Cidents!</h2>
<p>This room has covered the overlap between AppSec and incident response, showing how the two practices can be leveraged to increase the efficiency of the other. With applications being targeted more and more, it has never been more important to be prepared for incidents and respond to them in a timely and effective manner. Here is a summary of what has been covered in this room:<br>

- Why <strong>AppSec IR</strong> matters and what tools can be used to achieve it<br>
- The importance of being <strong>prepared</strong> for application incidents, and the steps that can be taken to ensure that you are<br>
- How to effectively <strong>detect</strong> and <strong>contain</strong> an application threat/attack<br>
- Considerations to be taken when <strong>recovering</strong> from an application incident <br>
- How crucial drawing <strong>lessons learned</strong> from an incident is in ensuring future application incidents are better handled, or even better prevented</p>

<p><em>Answer the question below</em></p>

<p>7.1. All done!<br>
<code>No answer needed</code></p>

<br>
<br>


<img width="1903" height="893" alt="image" src="https://github.com/user-attachments/assets/f04ad4a5-cc76-4671-bc90-82b4fd42ba2d" />

<img width="1902" height="890" alt="image" src="https://github.com/user-attachments/assets/73c56414-dd87-4ad3-886a-b7ae5985a36b" />


