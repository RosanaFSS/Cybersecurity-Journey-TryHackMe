<h1 align="center">Extracted</h1>
<p align="center"><img width="80px" src=""><br>
2025, April 23<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>352</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>...</em>.<br>
Access it <a href="https://medium.com/r/?url=https%3A%2F%2Ftryhackme.com%2Froom%2Fextractedroom"</a>here.<br>
<img width="1200px" src=""></p>

<h2>Task 1 . Help</h2>
<p>Working as a senior DFIR specialist brings a new surprise every day. Today, one of your junior colleagues raised an alarm that some suspicious traffic was generated from one of the workstations, but they couldn't figure out what was happening.<br>
Unfortunately, there was an issue with the SIEM ingesting the network traffic, but luckily, the network capture device was still working. They asked if you could look to find out what happened since you are known as The Magician around these parts.<br>
Note: For free users using the AttackBox, the challenge is best done using your own environment. Some browsers may detect the file as malicious. The zip file is safe to download with md5 of f9723177263da65ffdac74ffbf8d06a4. In general, as a security practice, download the zip and analyze the forensic files on a dedicated virtual machine, and not on your host OS.</p>

<p><em>Answer the question below</em></p>

<p>1.1. What's the initial part of the password?<br>
<code>THM{simsalabim_hex_hex}</code></p>

<p>

- Downloaded file-1693277727739.zip task file to my VM.<br>
- Extracted it and got traffic.pcapng.<br>
- Navigated to VirusTotal.<br>
- Uploaded traffic.pcapng and the output was an analysis report.<br>
- No security vendors flagged this file as malicious.<br>
-  There are no Communitycomments.</p>

<img width="1898" height="554" alt="image" src="https://github.com/user-attachments/assets/585178d6-9ef2-4d6c-bb7e-16304df8ea75" />

<br>
<p>

-  Launched Wireshark.<br>
-  Started clicking Statistics > File Properties.<br>
-  It is a [392 MB] file containing [53,338 packets].</p>

<img width="1509" height="712" alt="image" src="https://github.com/user-attachments/assets/f7b8a4d9-6238-4f81-b102-1e134c54606d" />

<br>
<p>

-  The capture occured in a timebox of [2 minutes 28 seconds].</p>

<img width="236" height="66" alt="image" src="https://github.com/user-attachments/assets/7bb999cf-f813-492c-8ecd-03f4aa0aafda" />

<br>
<p>
  
- Clicked Statistics > Protocol Hierarchy.<br>
-  All traffic is based on [TCP] protocol with [99%] of bytes being [data].</p>

<br>

<img width="1573" height="181" alt="image" src="https://github.com/user-attachments/assets/0819a741-5bbb-4c5a-aef6-aa90d5500927" />

<br>

<img width="1575" height="268" alt="image" src="https://github.com/user-attachments/assets/1580580a-ea11-4230-b942-2f9792526d37" />

<p>

- Clicked Statistics > Conversations.
- [10.10.45.95 :50537] sent [ 389 MB] to  [10.10.94.106 : 1337].
- [10.10.45.95 :50538] sent [ 0.0030 MB] to [10.10.94.106 : 1338].
- [10.10.45.95 :50536] sent [  0.0005 MB] to [10.10.94.106 : 1339].</p>

<img width="1721" height="160" alt="image" src="https://github.com/user-attachments/assets/80374394-a323-4f5c-9f9b-e45f2c43c72a" />

<br>
<p>

-  Right-clicked the highlighted analysis.  Clicked Apply as Filter>  Selected >  A->B.</p>

<img width="1718" height="245" alt="image" src="https://github.com/user-attachments/assets/31b25fa6-3476-4b6e-8983-dd7e439d3d06" />

<br>
<p>

-  Now we have [55,5%] of the total packets = [53,338].</p>


<img width="1854" height="385" alt="image" src="https://github.com/user-attachments/assets/7a9bddc9-9103-438c-ba20-9ca79402e89a" />

<br>
<p>

-  Right-clicked Data.  Clicked Copy> FieldName.  Got data.data.</p>

<img width="1848" height="652" alt="image" src="https://github.com/user-attachments/assets/ee711e6c-ee58-408b-ba5f-fa33e672e41a" />

<br>
<p>

-  Used Tshark filtering as in Wireshark. Got dump_database file.</p>

```bash
$ tshark -r traffic.pcapng -Y "ip.src==10.10.45.95 && tcp.srcport==50357 && ip.dst==10.10.94.106 && tcp.dstport==1337" -T fields -e data.data | tr -d '\n' | xxd -r -p > dump_database
```

<p>

- In Statistics > Conversations, right-clicked the analysis that contains 9 packets. Clicked Apply as Filter>  Selected >  A->B.</p>

<img width="1851" height="237" alt="image" src="https://github.com/user-attachments/assets/2ddd23d2-68ca-4a15-9f07-83227bcb4e42" />

<br>
<p>

- Used Tshark filtering as in Wireshark. Got dump_process file.</p>
</p>


```bash
$ tshark -r traffic.pcapng -Y "ip.src==10.10.45.95 && tcp.srcport==50358 && ip.dst==10.10.94.106 && tcp.dstport==1338" -T fields -e data.data | tr -d '\n' | xxd -r -p > dump_process
```

<h2>Walkthrough to be continued ...</h2>





<img width="1908" height="867" alt="image" src="https://github.com/user-attachments/assets/c4919db1-d050-44e6-b7e4-c5d36aaf1b4d" />

<img width="1907" height="901" alt="image" src="https://github.com/user-attachments/assets/bcc9a7c0-f356-414f-a066-b94e8e85fe94" />

<br>
<br>

<img width="329" height="88" alt="image" src="https://github.com/user-attachments/assets/b9331c5d-21e2-4fcc-b09e-f7d64cece555" />

<img width="1884" height="895" alt="image" src="https://github.com/user-attachments/assets/4e9cc4a5-f3b9-4719-99a6-42b91a328f75" />

<img width="1897" height="889" alt="image" src="https://github.com/user-attachments/assets/988af832-a0f6-469a-aa89-9fc27f274bb4" />

<img width="1897" height="894" alt="image" src="https://github.com/user-attachments/assets/4a9db4b8-18c0-410c-aaa9-a2e2cb161d83" />

<img width="1898" height="896" alt="image" src="https://github.com/user-attachments/assets/c39a625c-127a-45da-b682-eb8c5fb5e5bd" />
