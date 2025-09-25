<h1 align="center">Network Secuity Essentials</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/0dbfdc88-3523-46d7-b37d-20a60db8b9b"><br>
2025, September 25<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>507</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>Learn about key aspects of network security essentials and how to monitor and protect against adversaries</em>.<br>
Access it <a href="https://tryhackme.com/room/networksecurityessentials">here</a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/6eb54ea1-8481-4b05-99e2-a7d7453f78b3"></p>


<h2 align="center">Task 1 . Introduction</h2>
<br>

<p><em>Answer the question below</em></p>

<p>1.1. Complete the task.<br>
<code>No answer needed</code></p>

<h2 align="center">Task 2 . Lab Connectionn</h2>
<br>

<p><em>Answer the question below</em></p>

<p>2.1. Connect to the lab.<br>
<code>No answer needed</code></p>

<h2 align="center">Task 3 . A Network - Overview</h2>
<br>

<p><em>Answer the question below</em></p>

<p>3.1. Continue to the next task.<br>
<code>No answer needed</code></p>

<h2 align="center">Task 4 . Network Visibility</h2>
<br>

<p><em>Answer the question below</em></p>

<p>4.1. Continue to the next task.<br>
<code>No answer needed</code></p>


<h2 align="center">Task 5 . Network Perimeter</h2>
<br>

<p><em>Answer the question below</em></p>

<p>5.1. Continue to the next task.<br>
<code>No answer needed</code></p>

<h2 align="center">Task 6 . Network Perimeters: Monitoring and Protecting</h2>
<br>

<p><em>Answer the question below</em></p>

<p>6.1. Examine the firewall logs.  Which IP address is performing the port scan?<br>
<code>203.0.113.10</code></p>

<img width="911" height="78" alt="image" src="https://github.com/user-attachments/assets/b7fa8cd9-9d97-4737-b4e5-5479c991abe7" />

<br>
<br>

<img width="1066" height="383" alt="image" src="https://github.com/user-attachments/assets/30de1bd9-1ee4-493b-b43f-9385c9a70e32" />

<br>
<br>
<p>6.2.  In the WAF Logs, which single source IP is responsible for all the blocked web attacks??<br>
<code>198.51.100.12</code></p>

```bash
ubuntu@tryhackme:~/Desktop/Perimeter_logs/task6$ grep -E 'BLOCK' waf_logs.txt
```

<img width="1175" height="147" alt="image" src="https://github.com/user-attachments/assets/3c15969e-c790-445b-9af0-9777916e0c48" />

<br>
<br>
<p>6.3 .In the VPN logs, how many brute-force attempts failed?<br>
<code>90</code></p>

```bash
$ grep 'FAILED_AUTH' vpn_logs.txt | awk -F' ' '{split($5,a,":"); print a[1]}' | sort | uniq -c
```

<img width="1174" height="72" alt="image" src="https://github.com/user-attachments/assets/8412eade-cb62-428f-89b0-e49922165ce1" />

<br>
<br>
<p>6.4. Which suspicious IP address was found attempting the brute-force attack against the VPN gateway?<br>
<code>45.137.22.13</code></p>

```bash
$ grep 'AUTH' vpn_logs.txt | awk '{split($5,a,":"); ip=a[1]; match($0, /\(user '\''[^'\'']+'\''\)/, u); user=substr($0, RSTART+7, RLENGTH-8); print ip, user}' | sort | uniq -c
```

<img width="1173" height="532" alt="image" src="https://github.com/user-attachments/assets/c1be1886-8308-4286-b7cc-466e57316312" />

<br>
<br>
<h2 align="center">Task 7 . Network Perimeters: Monitoring and Protecting</h2>
<br>

<p><em>Answer the question below</em></p>

<p>7.1. Examine the firewall logs. What external IP performed the most reconnaissance?<br>
<code>203.0.113.45</code></p>

```bash
index="network_logs"  alert="ET SCAN Possible Portscan" | sort +_time
```

<img width="1197" height="641" alt="image" src="https://github.com/user-attachments/assets/ea17d68a-e75e-4231-8df3-81ad0eb45ef8" />

<br>
<br>

<img width="1192" height="754" alt="image" src="https://github.com/user-attachments/assets/c8c4daee-5dad-4c86-9cbf-d586f5bf2eeb" />

<br>
<br>
<p>7.2. In the firewall log, Which internal host was targeted by scans?<br>
<code>10.0.0.20</code></p>

```bash
index="network_logs"  alert="ET SCAN Possible Portscan" | sort +_time
```

<img width="1194" height="753" alt="image" src="https://github.com/user-attachments/assets/3110a2fa-b833-4454-91c7-e89e1dc12501" />

<br>
<br>

```bash
index="network_logs"  src_ip=203.0.113.45 source="ids_alerts.json" alert="ET SCAN Possible Portscan"
| stats count by dst_ip, dst_port
```

<img width="1048" height="533" alt="image" src="https://github.com/user-attachments/assets/97986c82-8b81-4891-93fc-3f523dd44c94" />

<br>
<br>
<p>7.3. Which username was targeted in VPN logs?<br>
<code>svc_backup</code></p>

```bash
index="network_logs" source="vpn_auth.json"  assigned_ip=null  src_ip="203.0.113.45" | sort +_time
```

<img width="1041" height="585" alt="image" src="https://github.com/user-attachments/assets/77b09a2b-c72c-4447-8010-169e18f4aa86" />

<br>
<br>
<p>7.4. What internal IP was assigned after successful VPN login?<br>
<code>svc_backup</code></p>

```bash
index="network_logs" source="vpn_auth.json"  src_ip="203.0.113.45"  username=svc_backup   result=SUCCESS | sort +_time
```

<img width="1043" height="632" alt="image" src="https://github.com/user-attachments/assets/e7821347-5d43-47ef-9f0e-603f8a3564d2" />

<br>
<br>
<p>7.5. Which port was used for lateral SMB attempts?<br>
<code>445</code></p>

```bash
index="network_logs"  alert="ET EXPLOIT Possible MS-SMB Lateral Movement"  dst_ip="10.0.0.20" | sort +_time
```


<img width="1038" height="651" alt="image" src="https://github.com/user-attachments/assets/085e21fd-ff8a-46b0-839f-e27168f427a3" />

<img width="1193" height="573" alt="image" src="https://github.com/user-attachments/assets/2386a177-0e01-4f2c-b5fe-0a3970ce57a9" />

<br>
<br>
<p>7.6. In the IDS logs, which host beaconed to the C2?<br>
<code>10.0.0.60</code></p>

```bash
index="network_logs"  source="ids_alerts.json"  alert="ET TROJAN Possible C2 Beaconing" | sort +_time
```

<img width="1191" height="617" alt="image" src="https://github.com/user-attachments/assets/2b3994b5-a7e1-4807-861c-e588e7685124" />

<br>
<br>
<p>7.7. During the investigation, which IP was observed to be associated with C2?<br>
<code>445</code></p>

```bash
index="network_logs"  source="ids_alerts.json"  alert="ET TROJAN Possible C2 Beaconing" | sort +_time
```

<img width="1191" height="617" alt="image" src="https://github.com/user-attachments/assets/2b3994b5-a7e1-4807-861c-e588e7685124" />


<br>
<br>
<p>7.8. Which host showed the exfiltration attempts?<br>
<code>10.0.0.51</code></p>

```bash
index="network_logs"  source="ids_alerts.json"  classification="Potential Data Exfiltration" | sort +_time
```

<img width="1192" height="706" alt="image" src="https://github.com/user-attachments/assets/1cbc8514-51b7-45b9-9e9a-ad7cb627d588" />

<br>
<br>
<h2 align="center">Task 8 . Conclusion</h2>
<p>In this room, you learned that an enterprise network is not just a collection of computers and servers. It’s an ecosystem with critical components like firewalls, Active Directory, application servers, file/database servers, endpoints, and wireless access points.<br>

- The network perimeter acts as the boundary between trusted and untrusted networks.<br>
- Attackers test this boundary constantly with port scans, brute-force attempts, and exploits against exposed services.<br>
- Monitoring the perimeter allows SOC analysts to detect these early signs before attackers can move deeper into the network.<br><br>

As a security analyst, our role is to:<br>

 Recognize normal vs suspicious network traffic.<br>
- Escalate unusual activity to higher SOC tiers.<br>
- Understand how each network component fits into the bigger picture of enterprise defense.</p>

<p><em>Answer the question below</em></p>

<p>8.1.Complete the room.<br>
<code>No answer needed</code></p>

<br>
<br>


<img width="1910" height="884" alt="image" src="https://github.com/user-attachments/assets/2fe2e60d-a892-4214-896b-b76f6ce95a0a" />

<img width="1904" height="893" alt="image" src="https://github.com/user-attachments/assets/f5b00d90-ca45-4562-95d4-1dc0bf24902e" />






<p><em>Practited ...</em></p>

<img width="1324" height="467" alt="image" src="https://github.com/user-attachments/assets/b2c0b654-f8ee-4e60-877f-3fbeefa68f11" />

<br>
<br>

<img width="1329" height="316" alt="image" src="https://github.com/user-attachments/assets/72e3023e-f87c-461f-a57d-c3e8d5d056c2" />

<br>
<br>

<img width="1330" height="105" alt="image" src="https://github.com/user-attachments/assets/7f6d1187-b69d-4742-b151-aabcfb6fe2f1" />

```bash
grep '203.0.113.10' firewall.log | grep 'ALLOW' | head -n 20
```

<img width="1334" height="372" alt="image" src="https://github.com/user-attachments/assets/4008ddbe-e9ba-429f-9075-bdf179bd2845" />

<br>
<br>



```bash
index="network_logs"  sourcetype=firewall_logs
| stats count by src_ip
| table src_ip, count
| sort by -count
```

<img width="778" height="681" alt="image" src="https://github.com/user-attachments/assets/1937edb8-b870-4e36-bdcd-88e9c7c1b4c7" />



index="network_logs"  sourcetype="firewall_logs" src_ip=203.0.113.45
| stats count by dst_ip, dst_port
| sort +dst_ip

<img width="792" height="799" alt="image" src="https://github.com/user-attachments/assets/8d596a52-ddc3-4311-9cf1-825721c9db9a" />


<br>
<br>

<p>7.2. In the firewall log, Which internal host was targeted by scans?<br>
<code>203.0.113.45</code></p>

index="network_logs"  sourcetype=firewall_logs
| stats count by dst_port
| table dst_ip, dst_port, count
| sort by -count

