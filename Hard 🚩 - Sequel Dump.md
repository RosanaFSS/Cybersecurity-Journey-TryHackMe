<p>July 12, 2025 - Day 432</p>
<h1>Sequel Dump</h1>
<p>Can you decipher the captured traffic of an SQL Injection attack?</p>
<p>https://tryhackme.com/room/hfb1sequeldump</p>

<br>

<img width="1900" height="376" alt="image" src="https://github.com/user-attachments/assets/51d92da3-990c-443e-990e-efa83ad24a7d" />

<br>

<img width="937" height="126" alt="image" src="https://github.com/user-attachments/assets/e1532ba6-9d98-412c-bfef-23a546b2c7e2" />


<h3>Connection from another VM</h3>
<p>TargetIP:8000</p>

<img width="1165" height="137" alt="image" src="https://github.com/user-attachments/assets/aade754e-9bc5-4e5e-a320-3d6cb98e9d2b" />

<h3>challenge.pcapng</h3>

<img width="399" height="43" alt="image" src="https://github.com/user-attachments/assets/d876c8a7-8f32-4653-85fb-7b85c79d6274" />

<h3>Wireshark</h3>

<img width="1330" height="750" alt="image" src="https://github.com/user-attachments/assets/59e0af2d-95b5-412d-a8fb-cd10c4e9c5b7" />

<img width="1361" height="513" alt="image" src="https://github.com/user-attachments/assets/83952e88-c057-401a-be0d-390108b54a86" />

<img width="1367" height="520" alt="image" src="https://github.com/user-attachments/assets/8c528efd-1c2e-4fa0-9df5-eed59493bc44" />

<img width="581" height="133" alt="image" src="https://github.com/user-attachments/assets/74225fd5-4525-47d8-a0c8-db32c8adc2ef" />

<img width="1368" height="519" alt="image" src="https://github.com/user-attachments/assets/eefe0fb3-6eff-4f08-9b87-5235f70c6fb5" />

<img width="1367" height="522" alt="image" src="https://github.com/user-attachments/assets/19892bb6-acb1-43a6-bd5b-97e12324d607" />


<p>

 - ?query=1 AND 2238=2238<br>
 - ?query=1 AND (SELECT QUARTER(NULL XOR NULL)) IS NULL<br>
 - ?query=1 AND ORD(MID((SELECT IFNULL(CAST(CHAR_LENGTH(column_name) AS NCHAR),0x20) FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name=0x70726f66696c6573 AND table_schema=0x70726f66696c655f6462 LIMIT 2,1),2,1))>51<br>
</p>

<h3>blind_sqli_table_reconstruction.py by Carson Shaffer</h3>
<p>https://raw.githubusercontent.com/CarsonShaffer/THM-Sequel-Dump/refs/heads/main/blind_sqli_table_reconstruction.py</p>

<h3>scapy</h3>

```bash
:~/SequelDump# python3 -m venv roseenv
:~/SequelDump# source roseenv/bin/activate
(roseenv) :~/SequelDump# 
(roseenv) :~/SequelDump#  pip3 install scapy
Collecting scapy
  Downloading scapy-2.6.1-py3-none-any.whl (2.4 MB)
     |\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588| 2.4 MB 14.4 MB/s 
Installing collected packages: scapy
Successfully installed scapy-2.6.1
(roseenv) :~/SequelDump#  pip list
Package       Version
------------- -------
pip           20.0.2 
pkg-resources 0.0.0  
scapy         2.6.1  
setuptools    44.0.0 
(roseenv) :~/SequelDump# pip install requirements.txt
```

<h3>reassemble.py</h3>

```bash
(roseenv) :~/SequelDump# python3 reassembly.py
Reconstructed Table:

Row 0:
  id          : 1
  name        : Void
  description : The cryptography expert who deciphers the toughest encryptions, searching for vulnerabilities in Voids encoded fortress.

Row 1:
  id          : 2
  name        : Zero-Day
  description : The exploit hunter who detects and patches vulnerabilities before they can be weaponized, skilled in penetration testing and reverse engineering.

Row 2:
  id          : 3
  name        : Phantom
  description : The OSINT (Open-Source Intelligence) specialist who tracks Voids movements through the dark web and gathers intelligence from hidden networks.

Row 3:
  id          : 4
  name        : Root
  description : The network infiltrator who can breach even the most fortified systems, bypassing firewalls and uncovering hidden data.

Row 4:
  id          : 5
  name        : Specter
  description : The forensic analyst who reconstructs digital crime scenes, piecing together evidence from fragmented files and corrupted logs.

Row 5:
  id          : 6
  name        : Sentinel
  description : The AI security specialist who builds countermeasures against Voids evolving attack algorithms and neutralizes rogue AI threats.

Row 6:
  id          : 7
  name        : supersecrethiddenuser
  description : Here's the flag: THM{r3tr13v1ng_th3_dump}
```

<br>

<img width="1201" height="571" alt="image" src="https://github.com/user-attachments/assets/31623fdb-d145-42be-a382-e69b102c4bfd" />

<br>
<br>

<img width="1908" height="887" alt="image" src="https://github.com/user-attachments/assets/36896039-7eff-4906-9355-9ef7fc9a843f" />

<img width="1908" height="895" alt="image" src="https://github.com/user-attachments/assets/3241f283-83f1-4ec5-b708-6c835b80dbb7" />


<br>
<br>


<img width="427" height="283" alt="image" src="https://github.com/user-attachments/assets/ef0b8646-d1e5-44d3-9f43-5b3857bb1a47" />

<img width="1900" height="892" alt="image" src="https://github.com/user-attachments/assets/c1a19ee8-c8c7-48e3-a199-5ac178259b42" />

<img width="1891" height="881" alt="image" src="https://github.com/user-attachments/assets/201de0e6-391e-4e9f-8be1-113af87dcccc" />

<img width="1886" height="891" alt="image" src="https://github.com/user-attachments/assets/3edce61e-b5b0-4199-a963-5471e21da61b" />

<img width="1889" height="891" alt="image" src="https://github.com/user-attachments/assets/3469aa8b-33ee-438f-9b78-5952ed5aede8" />
