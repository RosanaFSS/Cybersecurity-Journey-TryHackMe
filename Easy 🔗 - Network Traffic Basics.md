<h1 align="center">Network Traffic Basics</h1>
<p align="center">2025, October 16  &nbsp; .  &nbsp; Hey! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure on my <code>528</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>This room teaches the basics of Network Traffic Analysis. &nbsp;&nbsp;Access it <a href="https://tryhackme.com/room/networktrafficbasics">here</a>.<br><br><img width="1200px" src="https://github.com/user-attachments/assets/1264299b-241b-4311-8719-00b49821ba11"></p>


<h2>Task 1 . Introduction</h2>
<p>Network Traffic Analysis (NTA) is a process that encompasses capturing, inspecting, and analyzing data as it flows in a network. Its goal is to have complete visibility and understand what is communicated inside and outside the network. It is important to stress that NTA is not a synonym for the tool Wireshark. It is more than that: It is a combination of correlating several logs, deep packet inspection, and network flow statistics with specific outlined goals (which we will discuss later on).<br>

Knowing how to analyze network traffic is an essential skill, not only for an aspiring SOC L1 analyst but also for many other blue and red team roles. As an L1 analyst, you need to be able to navigate through the sea of network information and understand what is normal and what deviates from the baseline.<br>

In this room, we will focus on defining network traffic analysis, why you need it, what and how you can observe network traffic, and some of the sources and flows of network traffic you need to be aware of.</p>

<h3>Learning Objectives</h3>
<p>

- Know what network traffic analysis is<br>
- Know what can be observed<br>
- Know how to observe network traffic<br>
- Know typical network traffic sources and flows</p>

<h3>Prerequisites</h3>
<p>

- <a href="https://tryhackme.com/path/outline/presecurity">Pre Security</a><br>
- <a href="https://tryhackme.com/room/networkingessentials">Networking Essentials</a></p>

<p><em>Answer the question below</em></p>

<p>1.1. Continue to discover the purpose of network traffic analysis<br>
<code>No answer needed</code></p>

<br>
<h2>Task 2 . What is the Purpose of Network Traffic Analysis?</h2>
<p>Why should we analyze network traffic? Before we answer this question, let's look at the following scenario.</p>

<h4>DNS Tunneling and Beaconing</h4>
<p>You are an SOC analyst, and you receive an alert stating that an unusual number of DNS queries are coming from a host named WIN-016 with IP 192.168.1.16. The DNS logs on the firewall show multiple DNS queries going to the same TLD, each time using a different subdomain.</p>

```bash
2025-10-03 09:15:23    SRC=192.168.1.16      QUERY=aj39skdm.malicious-tld.com    QTYPE=A      
2025-10-03 09:15:31    SRC=192.168.1.16      QUERY=msd91azx.malicious-tld.com    QTYPE=A     
2025-10-03 09:15:45    SRC=192.168.1.16      QUERY=cmd01.malicious-tld.com       QTYPE=TXT     
2025-10-03 09:15:45    SRC=192.168.1.16      QUERY=cmd01.malicious-tld.com       QTYPE=TXT     
```

<p>Based on DNS logs, we can retrieve the following information:<br>

- Query and querytype<br>
- Subdomain and top-level domain: We can check tools like abuseDB or VirusTotal to check if the domain is malicious<br>
- Host IP: We can identify the system sending out the DNS queries<br>
- Destination IP: We can use tools like <a href="https://www.abuseipdb.com/">AbuseIPDB</a> or <a href="https://virustotal.com/">VirusTotal</a> to verify if the IP is flagged as malicious<br>
- Timestamp: We can build a timeline mapping out the different suspicious queries<br>

The DNS logs don't contain more information than that, so it is hard to draw a conclusion based on that information alone. We will need to inspect the DNS traffic more thoroughly and check the content of the DNS queries and replies. This will allow us to determine the nature of these queries and replies.<br>

This scenario is a prime example of why we need network traffic analysis. Firewalls and other devices register DNS queries and their responses but not their content. Threat actors could, for example, use TXT records to send Command and Control instructions to a compromised system. We can discover this by inspecting the content of the DNS queries. The packet capture fragnment below shows the content of a DNS reply that contains C2 commands.</p>

```bash
Domain Name System (response)
    Transaction ID: 0x4a2b
    Flags: 0x8180 Standard query response, No error
        1... .... .... .... = Response: Message is a response
        .... .... .... 0000 = RCODE: No error (0)
    Questions: 1
    Answer RRs: 1
    Authority RRs: 0
    Additional RRs: 0
    Queries
        cmd1.evilc2.com: type TXT, class IN
    Answers
        cmd1.evilc2.com: type TXT, class IN, TTL 60, TXT length: 20 
```

<h3>Why should we analyse network traffic?</h3>
<p>Generally, we will use network traffic analysis to:<br>

- Monitor network performance<br>
- Check for abnormalities in the network. E.g., sudden performance peaks, slow network, etc<br>
- Inspect the content of suspicious communication internally and externally. E.g., exfiltration via DNS, download of a malicious ZIP file over HTTP, lateral movement, etc<br>

From a SOC perspective, network traffic analysis helps:<br>

- Detecting suspicious or malicious activity<br>
- Reconstructing attacks during incident response<br>
- Verifying and validating alerts<br>

Below are two more scenarios that illustrate the importance of network traffic analysis:<br>

- Based on the logs for an end-user system, the system began to deviate from its normal behavior around 4 PM UTC. Analyzing the network traffic going to and from this system, we found a suspicious HTTP request and were able to extract a suspicious ZIP-file<br>
- We received an alert that an end-user system is sending many DNS requests in comparison to baseline of the network. After inspecting the DNS requests, we discovered that data was being exfiltrated using a technique called DNS tunneling<br>

Now that we know why we need network traffic analysis, let's continue with the next task to discover what exactly we can monitor.</p>

<p><em>Answer the question below</em></p>

<p>2.1.What is the name of the technique used to smuggle C2 commands via DNS?<br>
<code>DNS tunneling</code></p>

<br>
<h2>Task 3 . What Network Traffic Can We Observer?</h2>
<p>The best way to showcase the traffic we can observe in the network is by using the architecture implemented in nearly every device with a network interface: the TCP/IP stack. The image below shows the different layers of the TCP/IP model. Each layer describes the required information (headers) to pass the data to the next layer. The information included in each header, together with the application data, is precisely what we want to observe. Logs often include bits and pieces of these headers, but never the full packet details. This is why we need to do network traffic analysis.</p>

<h6 align="center"><img width="700px" src="https://github.com/user-attachments/assets/f04f7050-e735-4ddd-8c30-d543f47979a0"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<h4>Application</h4>

<p>On the application layer, we can find two important information structures: the application header information and the application data itself (payload). This information will change depending on which application layer protocol is used. Let's look at an example of HTTP.<br>

The code snippets below show the application headers of a client sending a GET request and the server's response. Most web proxies and firewalls log this header data. What they don't log is the application data or payload. From the GET request, you can determine that the client is requesting a file named <code>suspicious_package.zip</code>. The server's response includes a 200 code, which means the request was accepted. However, what you can't see in the logs is the content of the ZIP file (highlighted in yellow).</p>

<h6><em>Request</em></h6>

```bash
GET /downloads/suspicious_package.zip HTTP/1.1
Host: www.tryhackrne.thn
User-Agent: curl/7.85.0
Accept: */*
Connection: close
```

<h6><em>Response</em></h6>

```bash
HTTP/1.1 200 OK
Date: Mon, 29 Sep 2025 10:15:30 GMT
Server: nginx/1.18.0
Content-Type: application/zip
Content-Length: 10485760
Content-Disposition: attachment; filename="suspicious_package.zip"
Last-Modified: Mon, 29 Sep 2025 09:54:00 GMT
ETag: "5d8c72-9f8a1c-3a2b4c"
Accept-Ranges: bytes
Connection: close

[binary ZIP file bytes follow — 10,485,760 bytes]
```

<h4>Transport</h4>
<p>The application data and header are segmented and encapsulated at the transport layer into smaller pieces. Each piece includes a transport header, in most cases TCP or UDP. Let's have a look at the firewall log entries below:</p>

```bash
2025-10-13 09:15:32 ACCEPT TCP src=192.168.1.45 dst=172.217.22.14 sport=51432 dport=443 flags=SYN len=60
2025-10-13 09:15:32 ACCEPT TCP src=172.217.22.14 dst=192.168.1.45 sport=443 dport=51432 flags=SYN,ACK len=60
```

<p>Firewall logs often include the source and destination ports and the flags, but all the other fields are often not included. However, they are valuable for detecting certain types of attacks, such as session hijacking. <ins>Session hijacking</ins> can be detected by analyzing the <ins>sequence numbers</ins> included in the header. If the sequence numbers are suddenly far apart, further investigation is warranted. The output below shows a series of packets captured with Wireshark. </p>

```bash
No.     Time        Source          Destination     Protocol Length  Info
1       0.000000    192.168.1.45    172.217.22.14   TCP      74      51432 → 80 [SYN] Seq=0 Win=64240 Len=0 MSS=1460
2       0.000120    172.217.22.14   192.168.1.45    TCP      74      80 → 51432 [SYN, ACK] Seq=0 Ack=1 Win=65535 Len=0 MSS=1460
3       0.000220    192.168.1.45    172.217.22.14   TCP      66      51432 → 80 [ACK] Seq=1 Ack=1 Win=64240 Len=0
4       0.010500    192.168.1.45    172.217.22.14   TCP      1514    51432 → 80 [PSH, ACK] Seq=1 Ack=1 Win=64240 Len=1460
5       0.010620    172.217.22.14   192.168.1.45    TCP      66      80 → 51432 [ACK] Seq=1 Ack=1461 Win=65535 Len=0
6       0.020100    192.168.99.200  172.217.22.14   TCP      74      51432 → 80 [PSH, ACK] Seq=34567232 Ack=1 Win=64240 Len=20  
```

<p>

- The first 3 lines show a normal TCP 3-way handshake<br>
- Lines 4 and 5 show legitimate data transfer<br>
- Line 6 shows a packet from another source trying to inject itself into the session. Note the massive jump in the sequence number</p>

<h4>Internet</h4>
<p>When the transport layer sends down a segment, the internet layer also adds its header. If the segment is larger than the Maximum Transmission Unit (MTU), it will be divided into fragments, and a header will be added to each of them. The fields that are most often logged are the source and destination IP and TTL. This is sufficient for most use cases. But, if we want to, for example, detect fragmentation attacks, we will need to inspect the fragment offset and total length fields as well. There are different variations of a fragmentation attack. For example, an attacker can create tiny fragments to evade the IDS or mess up the reassembly of fragments by using overlapping byte ranges. The example below shows overlapping byte ranges. The offset in line 3 (highlighted in yellow) overlaps with the one in line 2. This means that the complete packet can be reassembled one way or another. Attackers can use this technique to bypass an IDS, for example.</p>

```bash
No.   Time       Source        Destination   Protocol Length Info
1     0.000000   203.0.113.45  192.168.1.10  UDP      1514    Fragmented IP protocol (UDP) (id=0x1a2b) [MF] Offset=0, Len=1480
2     0.000015   203.0.113.45  192.168.1.10  UDP      1514    Fragmented IP protocol (UDP) (id=0x1a2b) [MF] Offset=1480, Len=1480
3     0.000030   203.0.113.45  192.168.1.10  UDP       600    Fragmented IP protocol (UDP) (id=0x1a2b) Offset=1480, Len=64   <-- Overlap
4     0.000045   192.168.1.10  203.0.113.45  ICMP      98     Destination unreachable (Fragment reassembly time exceeded)
```

<h4>Link</h4>
<p>Once the internet layer finishes encapsulation, the IP packet is sent to the link layer. The link layer adds its header as well, containing more addressing information. Most logs will display the source and destination MAC addresses. For certain types of attacks, for example, ARP poisoning or spoofing, the information in the logs won't be sufficient. For these types of attacks, we need the full packet and context. What you, for example, can't see in a log is when the MAC address appears from multiple interfaces or when many gratuitous ARP packets are sent out with conflicting MAC addresses. The example below shows a packet capture detailing an ARP poisoning attack. The host with IP 192.168.1.200 is replying to each ARP request with the same MAC.</p>

```bash
No.   Time       Source           Destination      Protocol Length Info
1     0.000000   192.168.1.1      Broadcast        ARP      60     Who has 192.168.1.10? Tell 192.168.1.1
2     0.000025   192.168.1.10     192.168.1.1      ARP      60     192.168.1.10 is at 00:11:22:33:44:55
3     1.002010   192.168.1.200    192.168.1.1      ARP      60     192.168.1.10 is at aa:bb:cc:dd:ee:ff  <-- Attacker spoof
4     1.002015   192.168.1.200    192.168.1.10     ARP      60     192.168.1.1 is at aa:bb:cc:dd:ee:ff  <-- Attacker spoof
5     1.100000   192.168.1.10     172.217.22.14    TCP      74     54433 → 80 [SYN] Seq=0 Win=64240 Len=0
6     1.100120   192.168.1.200    172.217.22.14    TCP      74     54433 → 80 [SYN] Seq=0 Win=64240 Len=0  <-- Relayed via attacker
```

<p><em>Answer the questions below</em></p>
    
<p>3.1. Look at the HTTP example in the task and answer the following question: What is the size of the ZIP attachment included in the HTTP response? Note down the answer in bytes.<br>
<code>10485760</code></p>

<br>
<p>3.2. Which attack do attackers use to try to evade an IDS?<br>
<code>fragmentation</code></p>

<br>
<p>3.3. What field in the TCP header can we use to detect session hijacking?<br>
<code>sequence number</code></p>




<br>
<h2>Task 4 . Network Traffic Sources and Flows</h2>
<p>In the previous task, we discussed what we can observe theoretically based on the TCP/IP stack. Practically, it is more helpful to focus on specific sources and flows. A corporate network typically has some predetermined network flows and sources.<br>
  
We can group the <code>sources</code> into <code>two categories</code>:<br>

- <code>Intermediary</code><br>
- <code>Endpoint</code><br>

The <code>flows</code> we can also group into <code>two categories</code>:<br>

- <code>North-South</code>: Traffic that exits or enters the LAN and passes the firewall<br>
- <code>East-West</code>: Traffic that stays within the LAN (including LAN that extends to the cloud)<br>

Let's explore each of them below.</p>

<h3>Sources</h3>
<p></p>As mentioned, two network traffic sources exist: endpoint and intermediary devices. These devices can be found within the LAN and WAN.</p>

> <strong>Intermediary Sources</strong><br>
>> These are devices through which traffic mostly passes. While they generate some traffic, it is significantly lower than what endpoint devices generate. Under this category, we can find firewalls, switches, web proxies, IDS, IPS, routers, access points, wireless LAN controllers, and many more. Maybe less relevant for us, but all the infrastructure of Internet Service Providers is also considered part of this category.<br><br>
>> The traffic that originates from these devices comes from services like routing protocols (EIGRP, OSPF, BGP), management protocols (SNMP, PING), logging protocols (SYSLOG), and other supporting protocols (ARP, STP, DHCP).<br>

> <strong>Endpoint Sources</strong><br>
>> These are devices where traffic originates and ends. Endpoint devices take the bulk of the network bandwidth. Devices that fall under this category are servers, hosts, IoT devices, printers, virtual machines, cloud resources, mobile phones, tablets, and many more.

<h3>Flows</h3>
<p>A network traffic flow is typically determined by the services available in the network, such as Active Directory, SMB, HTTPS, and so on. In a typical corporate network, we can group these flows into North-South and East-West traffic.</p>

<h4>North-South Traffic</h4>
NS traffic is often monitored closely as it flows from the LAN to the WAN and vice versa. The most well-known services in this category are client-server protocols like HTTPS, DNS, SSH, VPN, SMTP, RDP, and many more. Each of these protocols has two streams: ingress (inbound) and egress (outbound). All of this traffic passes the firewall in one way or another. Configuring firewall rules and logging properly are key to visibility.

<h4>East-West Traffic</h4>
<p>EW traffic stays within the corporate LAN, so it is often monitored less. However, it is important to keep track of these flows. When the network is compromised, an attacker will often exploit different services internally to move laterally within the network. As we see below, there are many services within this category. Click on each category to see which services it contains.<br><br>

- Directory, Authentication & Identity Services<br>- Kerberos / LDAP: Authentication/queries to Active Directory<br>- RADIUS / TACACS+: Network access control<br>- Certificate Authority issuing internal certifications<br><br>
- File shares & print services<br>- SMB/CIFS: Accessing network drives<br>- IPP/LPD: Printing over the network<br><br>
- Router, switching, and infrastructure services<br>- DHCP traffic between hosts and the DHCP server<br>- ARP broadcast messages<br>- Internal DNS<br>- Routing protocol messages<br><br>
- Application Communication<br>- Database Connections: SQL over TCP<br>- Microservices APIs: REST or gRPC calls between services<br><br>
- Backup & Replication<br>- File Replication: Between data centers or to backup servers<br>- Database Replication: MySQL binlog replication, PostgreSQL streaming, and more<br><br>
- Monitoring & Management<br>- SNMP: Device health metrics<br>- Syslog: Centralized logging<br>- NetFlow/IPFIX: Traffic flow telemetry<br>- Other endpoint logs sent to a central logging server</p>

<h3>Flow Examples</h3>
<p>Let's have a visual look at some of the network flows mentioned above.</p>

<h4><strong>HTTPS</strong></h4>
<p>There are different variations of HTTPS network traffic flows. Let's examine a flow where the web proxy does TLS inspection:<br>
A host requests a website; this request is sent to the NGFW, which includes a web proxy. The web proxy will act as the web server and simultaneously establish a new TCP session with the actual web server and forward the clients' requests. When the web proxy receives the answer from the web server, it inspects its contents and then forwards it to the host if deemed safe. To summarize, we have two sessions, one between the client and the proxy and the other between the proxy and the web server. From the client's point of view, it has established a session with the web server.</p>

<h6 align="center"><img width="800px" src="https://github.com/user-attachments/assets/1e46b970-79ab-4e78-b039-5f103f8ce586"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<br>
<h4><strong>External DNS</strong></h4>
<p>DNS traffic within a corporate network starts when a host sends a DNS query. The host sends the query to the internal DNS server on port 53, which will then act on behalf of the host. First, it will check if it has an answer to the query in its cache; if not, it will send the query via the router, through the firewall, to the configured DNS servers. The answer will then follow the same path to the internal DNS server, which will then forward it to the host. The network diagram below shows a simplified flow.</p>

<h6 align="center"><img width="800px" src="https://github.com/user-attachments/assets/5b4d9e30-389c-4e1c-acb5-5e3ef3a134f3"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6

<br>                                                                                                                                                                                                                           
<h4><strong>SMB with Kerberos</strong></h4>
<p>When a host opens a share to, for example, \\FILESERVER\MARKETING, an SMB session is set up. First, authentication is done via Kerberos. When a user logged in on the host, it <strong>authenticated</strong> with the Key Distribution Center on the Domain Controller and received a Ticket Granting Ticket to request "<strong>service authentication tickets</strong>strong>". Now, the host requests a service ticket using the Ticket Granting Ticket it received earlier. The host then uses this ticket to establish the SMB connection. Once the SMB session is set up, the host can access the share. Below we see a simplified network diagram of the flow.</p>

<h6 align="center"><img width="800px" src="https://github.com/user-attachments/assets/925d2798-dd0e-4e9f-8180-fd513e97ece9"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6
    
<p><em>Answer the questions below</em></p>
    
<p>4.1. Which category of devices generates the most traffic in a network?<br>
<code>endpoint devices</code></p>

<p>4.2. Before an SMB session can be established, which service needs to be contacted first for authentication?<br>
<code>Kerberos</code></p>

<p>4.3. What does TLS stand for?br>
<code>Transport Layer Security</code></p>

<br>
<h2>Task 5 . How Can We Observe Network Traffic?</h2>
<p>Now that we have covered what we can and should observe in a network, let's examine how. As mentioned in the introduction, network traffic analysis focuses on combining multiple sources of information, analyzing them, finding patterns, and using the results to inform actions.<br>

We can obtain these sources of information in multiple ways:<br>

- Logs<br>
- Full Packet Capture<br>
- Network Statistics</p>

<h3>Logs</h3>
<p>Logs are our first entry into acquiring information about what is going on in the network. Each system and protocol in the network includes a way of logging information. It is essential to know that there is no universal standard for implementing logging on each system and protocol. Each vendor chooses how to implement logging for themselves. For example, Microsoft implements Windows Event Logs. Also, the data that is logged is up to the vendor. Most vendors will not log a full packet as it enters or exits the system. They will log some fields that they deem useful, such as a source IP address and a destination IP address. On the terminal below, we see some example logs of authentication on a Linux host using the Syslog format and an Apache web server access log that uses the CLF standard.</p>

```bash
# Auth log
Oct  8 11:20:15 web01 sshd[2145]: Accepted password for gensane from 192.168.1.50 port 52234 ssh2

# Apache web server access log
192.168.1.50 - - [08/Oct/2025:11:20:18 +0200] "GET /index.html HTTP/1.1" 200 2326 "-" "Mozilla/5.0"
```

<p>Even though there is no standard logging way, there are some protocols that offer a standardized way of sending log messages from devices to collectors, for example, Syslog and SNMP.<br>

When the logs don't provide enough information, we must dig deeper. To do so, we need to correlate logs, inspect full packet captures, and check network statistics.</p>

<h3>Full Packet Capture</h3>
<p>In task three, we discussed what a full packet looks like. Now, we want to know how to capture and inspect those packets. To do this, we have two options:<br>

- Install a physical network tap<br>
- Configure port mirroring</p>

<h4><strong>Network Tap</strong></h4>
<p>A network tap is a physical device you place inline in your network. These devices create a copy of all the network traffic that passes without affecting performance. That copied data is then forwarded to a packet capture box, IDS, or other system using the dedicated monitoring port. It is interesting to know that a TAP operates only on the link layer of the TCP-IP model; it does not need a MAC or IP address, because it copies the electrical/light signals and sends them to its monitoring port. This way, there is no added delay to the network. The image below shows an example of a network TAP.</p>

<h6 align="center"><img width="500px" src="https://github.com/user-attachments/assets/7d217978-5d55-4832-a4bb-62494581d358"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6

<br>
<h4><strong>Port Mirroring</strong></h4>
<p>Port mirroring is a software approach to copying packets from one port on an intermediary device to another that is attached to, for example, an IDS, packet capture box, or other systems. Each vendor has its own name. Cisco, for example, calls it SPAN. On the terminal below, we can see how to configure SPAN on a Cisco device. In this example, the packets going through <code>fastEthernet0/1</code> are duplicated and sent to <code>fastEthernet0/2</code>.</p>

```bash
Switch(config)# monitor session 1 source interface fastEthernet0/1
Switch(config)# monitor session 1 destination interface fastEthernet0/2
```

<p>The image below shows what this would look like. The WIN-001 sends packets through the switch to communicate with the server. When the packet arrives at the switch, it gets duplicated and is also sent to the monitoring device.</p>

<h6 align="center"><img width="500px" src="https://github.com/user-attachments/assets/016d3947-9c73-43c6-9f9b-4d3ee0e73b9c"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6
    
<p>Note that the intermediary devices do not necessarily need to be physical, port mirroring can also be configured on a virtual devices such as a VMware vSwitch. Cloud environments also have specific services that offer mirroring. AWS, for example, offers VPC Traffic Mirroring.</p>

<h4>Best Practices</h4>
<p>When doing full packet capture, we need to take some things into account:<br>

- Placement: Depending on which traffic we want to capture, we need to place the TAP or configure the mirror in the right place<br>
- Duration: Full packet capture will require a proportionate amount of storage. If you capture traffic on a 1 Gbps line for a whole day, we would need an average of 10.8 TB of storage space. Imagine the amount of storage we need on 10Gb or 40Gb lines<br>
- Mirror vs TAP: Physical taps offer close to zero performance reduction. Mirroring can impact performance when a huge amount of traffic passes through the mirrored port<br><br>

<code>Exercise</code>:<br>
- Open the static site and complete the two exercises by placing the tap in the correct position and uncovering the flag in the traffic.<br>
- Fill in the flags at the end of this task.<br>
- You can open the static site by clicking on the "View Site" button and the top of this task.<br>
- The static site will open in split-screen.<br>
- To open the static site in full screen, click the "Full Screen" button on the static siteM.</p>

<h4>Tools</h4>
<p>Now that we know how to do full packet captures lets have a look at the tools available to analyze these packets:<br>

- Wireshark<br>
- TCPdump<br>
- IPS/IDS like Snort, Suricata and zeek<br>

These are some of the many tools that are available to analyze full packet captures. In the following rooms in this module we will focus on using Wireshark.</p>

<h3>Network Statistics</h3>
<p>Another great way to find anomalies in your network is to gather metadata about the data flowing through the network, such as counting the number of DNS requests that a host sends out. A few protocols facilitate this. We will briefly discuss two of them: NetFlow and IPFIX.<br>

<strong>NetFlow</strong> is a protocol developed by Cisco that collects metadata about traffic flowing in a network. It is a great way to detect things like C2 traffic, data exfiltration, and lateral movement. The image below shows a sample of NetFlow output. As we can see, the sample does not contain individual packets but metadata about the flow of packets going from the source IP 12.1.1.1 to the destination IP 13.1.1.2.</p>

<h6 align="center"><img width="400px" src="https://github.com/user-attachments/assets/55e8af01-bef4-4e34-b188-53d42a7df6c5"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6

<p>The <strong>Internet Protocol Flow Information Export protocol (IPFIX)</strong> can be considered as the successor to NetFlow. NetFlow was initially a proprietary protocol from Cisco. This means that the protocol was designed for Cisco systems only. Only from NetFlow v9 on did Cisco include templating, so other vendors could adapt it to their devices. In collaboration with Cisco and other vendors, the IETF created IPFIX and released it as a vendor-neutral standard. It offers features similar to NetFlow, but includes more flexibility in configuring which fields to capture.<br>

To <strong>implement NetFlow</strong> or <strong>IPFIX</strong>, we don't need a whole new set of infrastructure or dedicated servers. Most vendors implement these protocols standard in their devices. We just have to enable and configure the protocol and have a place to send the metadata. You don't need a dedicated server for collecting this data; many NGFWs, IPS, and IDS have an implementation to collect and analyze flow data.</p>

<p><em>Answer the question below</em></p>
    
<p>5.1. What is the flag found in the HTTP traffic in scenario 1? Hint: <em>All HTTPS traffic needs to pass through the configured Web Proxy server</em><br>
<code>THM{***************}</code></p>

<p>5.2. What is the flag found in the DNS traffic in scenario 2?Hint: <em>C2 commands are often infiltrated via TXT records</em><br>
<code>THM{**************}</code></p>

<br>
<h2>Task 6 . Conclusion</h2>
<p>Now that we know what NTA is, why we need it, how to capture network traffic and analyze it; we are ready to get hands on with effectively analyzing network traffic using a tool called Wireshark. Proceed to the next room to get started with the basics of Wireshark.</p>

<p><em>Answer the question below</em></p>
    
<p>6.1. I am ready to do some traffic analysis!<br>
<code>No answer needed</code></p>

<br>
<br>
<br>
<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/e2f30f3a-2312-4ad5-96d9-fe5e5fe84d7a"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/7f571574-7b21-4ede-b50f-9606aca14540"></p>

<h1 align="center">My TryHackMe Journey ・ 2025, October</h1>


<div align="center"><h6>

| Date   | Room                                  |Streak   |All Time<br>Global|All Time<br>Brazil|Monthly<br>Global|Monthly<br>Brazil|Points|Rooms<br>Completed|Badges|
|:------:|:--------------------------------------|--------:|------------:|------------:|------------:|------------:|------------:|------------:|------------:|
|16      |Easy 🔗 - Network Traffic Basics       | 528    |      90ᵗʰ    |      4ᵗʰ     |      89ᵗʰ    |     2ⁿᵈ    | 131,138  |  1,004    |    79     |
|16      |Medium 🔗 - Linux Threat Detection 3   | 528    |      90ᵗʰ    |      4ᵗʰ     |      89ᵗʰ    |     2ⁿᵈ    | 131,066  |  1,003    |    79     |
|15      |Medium 🔗 - Windows PrivEsc, in progress| 527   |      91ˢᵗ    |      4ᵗʰ     |      83ʳᵈ    |     2ⁿᵈ    | 131,050  |  1,002    |    79     |
|13      |Hard 🚩 - M4tr1x: Exit Denied          | 525    |      92ⁿᵈ    |      4ᵗʰ     |      76ᵗʰ    |     2ⁿᵈ    | 130,938  |  1,002    |    79     |
|12      |Easy 🔗 - Atlas                        | 524    |     101ˢᵗ    |      4ᵗʰ     |     251ˢᵗ    |     3ʳᵈ    | 129,902  |  1,001    |    76     |
|11      |Easy 🔗 - Brute Force Heroes           | 523    |     101ˢᵗ    |      4ᵗʰ     |     217ᵗʰ    |     3ʳᵈ    | 129,878  |  1,000    |    76     |
|11      |Hard 🚩 - Rocket                       | 523    |     102ⁿᵈ    |      4ᵗʰ     |     211ˢᵗ    |     3ʳᵈ    | 129,870  |    999    |    76     |
|10      |Easy 🚩 - Shadow Trace                 | 522    |     101ˢᵗ    |      4ᵗʰ     |     159ᵗʰ    |     3ʳᵈ    | 129,810  |    998    |    76     |
|10      |Easy 🔗 - Defensive Security Intro     | 522    |     103ʳᵈ    |      4ᵗʰ     |     357ᵗʰ    |     3ʳᵈ    | 129,405  |    997    |    76     |
|10      |Easy 🔗 - 25 Days of Cyber Security, Day 2| 522|      103ʳᵈ    |      4ᵗʰ     |     355ᵗʰ    |     3ʳᵈ    | 129,405  |    996    |    76     |
|9       |Medium 🔗 - Linux Threat Detection 2   | 521    |     103ʳᵈ    |      4ᵗʰ     |     326ᵗʰ    |     3ʳᵈ    | 129,373  |    996    |    76     |
|9       |Medium 🚩 - WWBuddy                    | 521    |     103ʳᵈ    |      4ᵗʰ     |     390ᵗʰ    |     4ᵗʰ    | 129,293  |    995    |    76     |
|8       |Hard 🚩 - Motunui                      | 520    |     103ʳᵈ    |      4ᵗʰ     |     383ʳᵈ    |     4ᵗʰ    | 129,201  |    994    |    76     |
|8       |Easy 🔗 - Man-in-the-Middle            | 520    |     103ʳᵈ    |      4ᵗʰ     |     390ᵗʰ    |     4ᵗʰ    | 129,141  |    993    |    76     |
|7       |Medium 🚩 - Profiles, in progress      | 519    |              |              |              |            | 129,021  |    992    |    76     |
|6       |Medium 🚩 - VulnNet                    | 518    |     105ᵗʰ    |      4ᵗʰ     |     348ᵗʰ    |     5ᵗʰ    | 129,021  |    992    |    76     |
|6       |Easy 🚩 - DearQA                       | 518    |     105ᵗʰ    |      4ᵗʰ     |     333ʳᵈ    |     6ᵗʰ    | 128,991  |    991    |    76     |
|5       |Medium 🚩 - Frank & Herby try again.....| 517   |     106ᵗʰ    |      4ᵗʰ     |     300ᵗʰ    |     5ᵗʰ    | 128,931  |    990    |    76     |
|4       |Medium 🚩 - Frank & Herby make an app  | 516    |     105ᵗʰ    |      4ᵗʰ     |     233ʳᵈ    |     3ʳᵈ    | 128,871  |    989    |    76     |
|4       |Info ℹ️ - OverlayFS - CVE-2021-3493    | 516    |     105ᵗʰ    |      4ᵗʰ     |     235ᵗʰ    |     3ʳᵈ    | 128,841  |    988    |    76     |
|3       |Medium 🚩 - XDR: Operation Global Dagger2| 515  |     104ᵗʰ    |      4ᵗʰ     |     149ᵗʰ    |     3ʳᵈ    | 128,833  |    987    |    76     |
|3       |Medium 🚩 - VulnNet: dotpy             | 515    |     108ᵗʰ    |      4ᵗʰ     |     741ˢᵗ    |    11ˢᵗ    | 128,563  |    986    |    76     |
|2       |Medium 🔗 - Data Exfiltration Detection| 514    |     108ᵗʰ    |      4ᵗʰ     |     521ˢᵗ    |     8ᵗʰ    | 128,503  |    985    |    76     |
|1       |Medium 🔗 - Network Discovery Detection| 513    |     108ᵗʰ    |      4ᵗʰ     |     875ᵗʰ    |     7ᵗʰ    | 128,407  |    984    |    76     |
|1       |Medium 🚩 - Intranet                   | 513    |     108ᵗʰ    |      4ᵗʰ     |    3,357ᵗʰ   |    57ᵗʰ    | 128,335  |    983    |    76     |

</h6></div>

<br>

<p align="center">Global All Time:   90ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/3af950f2-7de7-4e62-b9ab-6a7e52dde0f0"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/4ab07bcf-9460-4eba-85db-d974e1473c3b"><br><br>
                  Brazil All Time:     4ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/1316ce80-e144-4e9f-9f68-b30f7a20156e"><br>
                  Global monthly:     83ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/9cc5157f-74dc-40fc-916f-4b26c9d67f6e"><br>
                  Brazil monthly:      2ⁿᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/4e6ecb02-20c4-450c-bd12-222e56c45461"></p>


<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
