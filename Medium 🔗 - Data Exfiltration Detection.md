<h1 align="center">Data Exfiltration Detection</h1>
<p align="center">2025, October 2<br>Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>514</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Learn how to detect data exfiltration attempts in various network channels.</em><br>
<img width="80px" src="https://github.com/user-attachments/assets/ed94084a-a1da-47fa-ab6c-56c9b8fcfd07"><br>
Access it <a href="https://tryhackme.com/room/dataexfildetection">here</a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/73d7e9c2-1af2-4841-bd32-e9c6d788bf46"></p>

<h2>Task 1 . Introduction</h2>
<p>Data exfiltration is the unauthorized transfer of sensitive data from a computer or other device. It's a primary objective for attackers who have breached a network. As a SOC analyst, our job is to detect and stop this before sensitive information walks out the door. This room will cover the common techniques attackers use to steal data and, more importantly, how we can catch them in the act.</p>

<h3>Learning Objectives</h3>
<p>In this room, we will cover the following learning objectives:<br>

- Understand the common methods used for data exfiltration.<br>
- Learn how to detect exfiltration attempts using network traffic analysis.<br>
- Identify signs of exfiltration on endpoint devices.<br>
- Correlate logs in a SIEM to uncover hidden exfiltration channels.</p>

<h3>Prerequisites</h3>
<p>This room expects the users to have covered or explored the following rooms:<br>

- <a href="https://tryhackme.com/room/wiresharkthebasics">Wireshark: The Basics</a><br>
- <a href="https://tryhackme.com/room/networksecurityessentials">Network Security Essentials</a><br>
- <a href="https://tryhackme.com/room/splunk101">Splunk Basics</a><br>
- <a href="https://tryhackme.com/room/splunkexploringspl">Splunk Exploring SPL</a><br>

Let's begin our learning journey.</p>

<p><em>Answer the question below</em></p>

<p>1.1. Continue to the next task.<br>
<code>No answer needed</code></p>

<br>
<h2>Task 2 . Lab Connection</h2>
<p>Before moving forward, start the lab by clicking the <code>Start Machine</code> button. It will take 3 minutes to load properly. The VM will be accessible on the right side of the split screen. If the VM is not visible, use the blue Show Split View button at the top of the page.
  
<p>All files required to complete the room are placed in the <code>data_exfil</code> folder on the Desktop. The log files for the investigation's coming tasks are pre-ingested into the Splunk Instance, which can be accessed from within the Machine at <code>MACHINE_IP:8000</code>.</p>

<p>For the practical lab, there are three ways to approach the practical:<br>

- Explore the network traffic in the respective folder in the <code>data_exfil</code> directory on the Desktop.<br>
- Perform Log Analysis on the log file in the same folder.<br>
- Examine the logs already ingested into the Splunk instance. Make sure to select All times and use the <code>dindex=ata_exfil</code>, as shown below:</p>

<p><em>Answer the question below</em></p>

<p>2.1 Connect with the lab.<br>
<code>No answer needed</code></p>

<img width="1320" height="550" alt="image" src="https://github.com/user-attachments/assets/88496489-5456-4b73-9ce9-78946b9ad71d" />

<br>
<br>
<br>
<h2>Task 3 . Data Exfil: Overview, techniques, and indicators</h2>
<br>

<p><em>Answer the question below</em></p>

<p>3.1. Exfiltrating the data through HTTP comes under which technique?<br>
<code>Network-based</code></p>

<br>
<br>
<br>
<h2>Task 4 . Detection: Data Exfil through DNS Tunneling</h2>
<br>

<p><em>Answer the questions below</em></p>

<p>4.1. What is the suspicious domain receiving the DNS traffic?<br>
<code>tunnelcorp.net</code></p>

```bash
index="data_exfil" sourcetype="dns_logs"
|  stats count by query
|  sort -count
```

<img width="853" height="545" alt="image" src="https://github.com/user-attachments/assets/fed83099-c316-4c51-b8b2-16eaba5185ec" />

<br>
<br>
<br>

```bash
index="data_exfil" sourcetype="dns_logs" 
| eval query_length=len(query)
| where query_length > 30
| table timestamp, src_ip, dst_ip, query,query_length
| sort +timestamp
```

<img width="857" height="563" alt="image" src="https://github.com/user-attachments/assets/c4ed3570-1d49-47c9-9298-d72b06076fd7" />

<br>
<br>
<br>
<p>4.2. How many suspicious traffic/logs related to dns tunneling were observed?<br>
<code>315</code></p>

```bash
index="data_exfil" sourcetype="DNS_logs" label="suspicious"
|  table timestamp, label, src_ip, dst_ip, label, query
|  stats count by src_ip
|  sort by -count
```

<img width="852" height="339" alt="image" src="https://github.com/user-attachments/assets/fd8db5d3-5429-4af3-ace4-78c5140b78bb" />

<br>
<br>
<br>

```bash
dns.qry.name contans "tunnel"
```

<img width="1131" height="451" alt="image" src="https://github.com/user-attachments/assets/b4a63645-05be-4e3c-bdfe-53d59f811512" />

<br>
<br>
<br>
<p>4.3. Which local IP sent the maximum number of suspicious requests?<br>
<code>192.168.1.103</code></p>

```bash
index="data_exfil" sourcetype="DNS_logs" label="suspicious"
|  table timestamp, label, src_ip, dst_ip, label, query
|  sort by +timestamp
```

<img width="850" height="469" alt="image" src="https://github.com/user-attachments/assets/c140dc44-96c7-4261-a61f-0ac3fe8f9590" />

<br>
<br>
<br>

```bash
index="data_exfil" sourcetype="DNS_logs" label="suspicious"
|  table timestamp, label, src_ip, dst_ip, label, query
|  stats count by src_ip
|  sort by -count
```

<img width="856" height="458" alt="image" src="https://github.com/user-attachments/assets/1daa4f5c-dc6a-4b06-964f-d086eff852ae" />

<br>
<br>
<br>
<h2>Task 5 . Detection: Data Exfil through FTP</h2>
<br>

<p><em>Answer the questions below</em></p>

<p>5.1. How many connections were observed from the guest account?<br>
<code>5</code></p>

```bash
index="data_exfil" method=POST
```

<img width="1170" height="527" alt="image" src="https://github.com/user-attachments/assets/8f46581a-fa90-4733-820f-6b94fe7506c1" />

<br>
<br>
<br>

```bash
ftp.request.arg == "guest"
```

<img width="1127" height="197" alt="image" src="https://github.com/user-attachments/assets/f7665c57-dbe0-4796-b070-9942dcd21e5a" />

<br>
<br>
<br>
<p>5.2. Apply the filter; what is the name of the customer-related file exfiltrated from the root account?<br>
<code>*************.****</code></p>

```bash
ip.src == xxx.xxx.x.xxx && tcp.analysis.bytes_in_flight > 46
```

<img width="1128" height="453" alt="image" src="https://github.com/user-attachments/assets/755a28f4-3000-4668-bc1b-28c57de120f9" />

<br>
<br>
<br>
<p>5.3. Which internal IP was found to be sending the largest payload to an external IP?<br>
<code>xxx.xxx.x.xxx</code></p>

<img width="1126" height="217" alt="image" src="https://github.com/user-attachments/assets/6cd53987-53d7-440d-a8aa-df98374d1003" />

<br>
<br>
<br>
<p>5.4. What is the flag hidden inside the ftp stream transferring the CSV file to the suspicious IP?<br>
<code>THM{*********************}</code></p>

<img width="880" height="285" alt="image" src="https://github.com/user-attachments/assets/db16b532-f76f-4c8c-9390-1526dfa9fea5" />

<br>
<br>
<br>
<h2>Task 6 . Detection: Data Exfil via HTTP</h2>
<br>

<p><em>Answer the questions below</em></p>

<p>6.1. Which internal compromised host was used to exfiltrate this sensitive data?<br>
<code>192.168.1.103</code></p>

<p>6.2. What's the flag hidden inside the exfiltrated data?<br>
<code>THM{*****************************}</code></p>
  
<p>
  
- lenght<br>
- stream</p>
<img width="1215" height="604" alt="image" src="https://github.com/user-attachments/assets/9fba46c7-56f6-46ee-bc27-1d73ef0e0e91" />

<br>
<br>
<br>
<h2>Task 7 . Detection: Data Exfiltration via ICMP</h2>
<br>

<p><em>Answer the question below</em></p>

<p>7.1. What is the flag found in the exfiltrated data through ICMP?<br>
<code>THM{*****************************}</code></p>

<p>

- Base64</p>

<img width="1189" height="553" alt="image" src="https://github.com/user-attachments/assets/6c65b56e-d7e6-412c-a665-4e6663c2f1f7" />

<br>
<br>
<br>

<img width="1216" height="796" alt="image" src="https://github.com/user-attachments/assets/2e19974f-0d77-446d-8076-120eb20b9039" />

<br>
<br>
<br>

<img width="1902" height="232" alt="image" src="https://github.com/user-attachments/assets/4693144b-7205-4a3a-a96c-ad765e79114b" />

<br>
<br>
<br>

<h2>Task 8 . Conclusion</h2>
<p>That's it from this room. This room only touched a few channels used for data exfiltration, and we looked at the network-centric log sources to find the footprints of the data being sent out of the organization. <br>

We've explored data exfiltration from a defender's perspective in this room. We covered:<br>

- The Fundamentals: What data exfiltration is and why it's a critical threat to organizations.<br>
- Attacker Frameworks: How data exfiltration fits into established models like the Cyber Kill Chain (Actions on Objectives).<br>
- Common Techniques: The various methods attackers use to steal data, including FTP, HTTP, DNS & ICMP tunneling.<br>

Adversaries use more channels to exfiltrate the data, and we can look at other log sources to find indicators of the attack. Future rooms will cover more.</p>

<p><em>Answer the question below</em></p>

<p>8.1. Continue to complete the room<br>
<code>No answer needed</code></p>

<br>
<br>
<br>
<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/b6153b7f-7f7e-41c7-8a76-4a84b6b17da8"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/db41ef70-411d-4a3c-939a-129927d970b8"></p>

<h1 align="center">My TryHackMe Journey ・ 2025, October</h1>

<div align="center"><h6>

| Date   | Room                                  |Streak   |All Time<br>Global|All Time<br>Brazil|Monthly<br>Global|Monthly<br>Brazil|Points|Rooms<br>Completed|Badges|
|:------:|:--------------------------------------|--------:|------------:|------------:|------------:|------------:|------------:|------------:|------------:|
|2       |Medium 🔗 - Data Exfiltration Detection| 514    |     108ᵗʰ    |      4ᵗʰ     |     521ˢᵗ    |     8ᵗʰ    | 128,503  |    985    |    76     |
|1       |Medium 🔗 - Network Discovery Detection| 513    |     108ᵗʰ    |      4ᵗʰ     |     875ᵗʰ    |     7ᵗʰ    | 128,407  |    984    |    76     |
|1       |Medium 🚩 - Intranet                   | 513    |     108ᵗʰ    |      4ᵗʰ     |    3,357ᵗʰ   |    57ᵗʰ    | 128,335  |    983    |    76     |

</h6></div>
<br>

<p align="center">Global All Time:   108ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/e481ff1c-0bb2-42ba-854f-472d9ebdf2fb"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/7f8af7f7-f70c-4cbb-b189-04bd3d5db0b3"><br><br>
                  Brazil All Time:     4ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/3fab1674-247d-42ef-bfce-5b334c4fa3ba"><br>
                  Global monthly:    521ˢᵗ<br><img width="1200px" src="https://github.com/user-attachments/assets/11dc0452-310e-496c-8980-09a2c5570e34"><br>
                  Brazil monthly:      8ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/e3cc7097-307e-4869-9e17-0254be33140e"><br>

<br>
<h1 align="center">Thanks for Coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 
