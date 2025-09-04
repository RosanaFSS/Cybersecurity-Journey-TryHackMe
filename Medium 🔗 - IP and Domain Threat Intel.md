<h1 align="center">IP and Domain Threat Intel</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/3c4c5c59-8c89-40f8-8562-9ee9712b751e"><br>
2025, September 4<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>486</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>A look into enriching IP and domain insights with open source threat intelligence</em>.<br>
Access it <a href="https://tryhackme.com/room/ipanddomainthreatintel">here</a><br>
<img width="1200px" src="https://github.com/user-attachments/assets/783042a7-c62a-468a-8af8-87bcae48bb5b"></p>

<h2>Task 1 . Introduction</h2>
<p>Security Operations runbooks still revolve around the process <code>verify → enrich → decide</code>, but when the alert is a lone IP address or domain, the enrichment phase looks different. Instead of hashes, we pivot on geolocation, ASNs, open-service footprints, and passive DNS to learn whether a connection is routine SaaS traffic or an adversary foothold beacon.</p>

<h3>Learning Objectives</h3>
<p>By the end of this room, you will be able to:<br>

- Understand IP and domain threat intelligence for a SOC.<br>
- Geolocate IPs and interpret their Autonomous System Numbers (ASNs).<br>
- Detect red-flag infrastructure via Shodan/Censys service banners.<br>
- Assess reputation with various tools.<br>
- Enrich domains with WHOIS age, DNS records, and certificate transparency.</p>

<h3>Learning Prerequisites</h3>
<p>

- <a href="https://tryhackme.com/room/cyberthreatintel">Intro to Cyber Threat Intel</a><br>
- <a href="https://tryhackme.com/room/fileandhashthreatintel">File and Hash Threat Intel</a></p>

<h3>Scenario</h3>
<p>It is Wednesday morning. The SOC has flagged two suspicious domains in phishing emails and three IP addresses in outbound proxy logs. You are tasked with triaging all seven artefacts, enriching them with context, and recommending actions with expiry.<br>

- advanced-ip-sccanner[.]com<br>
- 166[.]1[.]160[.]118<br>
- 64[.]31[.]63[.]194<br>
- 69[.]197[.]185[.]26<br>
- 85[.]188[.]1[.]133</p>

<h6 align="center"><img width="550px" src="https://github.com/user-attachments/assets/ca522511-4aec-4701-8508-43c240dec86c"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p><em>Answer the question below</em><br>
<ol type="1.">
    <li>All set to login&nbsp;&nbsp;&nbsp;<code>No answer needed</li></code></li>
</ol></p>

<br>
<h2>Task 2 . IP Building Blocks</h2>
<p>Network-based threat intelligence is an essential aspect of modern cyber security defence. Examining IP addresses and domains from a threat intelligence perspective involves investigating beyond network connectivity to understand the malicious intent and capability behind the digital assets in a way that supports quick, safe triage for SOC L1 analysts.</p>

<h3>Why DNS Metters in SOC</h3>
<p>Every time a user clicks a link or a system resolves a hostname, the Domain Name System (DNS) springs into action. DNS is the mechanism that converts human-friendly names like <a href="https://www.tryhackme.com/">www.tryhackme.com</a> into IP addresses that machines understand. Because of its central role in making the internet usable, DNS is also a favourite playground for attackers.<br>

For SOC analysts, DNS is one of the richest early-warning datasets. Suspicious domains will appear in alerts long before a payload hash is known. Adversaries rapidly register, configure, and abandon domains to stay ahead of defences. Our job as analysts is to turn a raw domain into a contextual artefact: who owns it, what IPs it resolves to, how often it changes, and whether it behaves more like a normal content delivery network (CDN) or a throwaway setup.</p>

<h4>Core DNS Records for Triage</h4>
<p>When you enrich a domain, these are the records that matter most:<br>

- <strong>A / AAAA Records</strong>: Map the domain to IPv4 and IPv6 addresses. If you see several A records that hop between different networks, raise suspicion of rapid rotation. In practice, copy the A record from <a href="https://www.nslookup.io/">nslookup.io</a> or <a href="https://dnschecker.org/">dnschecker.org</a> and follow with pasting the IP into VirusTotal for a quick read.<br>
- <strong>NS Records</strong>: Identify the nameservers controlling the domain. Unusual or recently changed NS entries can mark fresh set up. As L1 analysts, we should note the provider name rather than chasing low-level details.
MX Records: Define which servers handle email. Attackers may configure MX records to deliver phishing campaigns directly. If the alert relates to web browsing, just record whether MX exists.<br>
- <strong>TXT Records</strong>: Store SPF and DKIM rules or verification tags. Poorly configured or absent SPF can increase risk in mail cases.<br>
- <strong>SOA Record</strong>: Points to the zone's primary authority and often includes contact information. It will be worth noting the primary host and serial, which will support a basic ownership picture.<br>
- <strong>TTL (Time To Live)</strong>: Tells resolvers how long to cache answers. Very low TTLs, seconds or minutes, can point to frequent changes, and should be treated as clues.</p>

<h6 align="center"><img width="200px" src="https://github.com/user-attachments/assets/65c02c03-4e9c-4424-ae49-a8a98fdd06b3"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<h3>SOC Use Cases</h3>
<p>Based on our scenario, the SIEM raises an alert pointing to the domain advanced-ip-sccanner[.]com. As L1 analysts, we need to enrich this artefact by gathering the above DNS records using tools such as <a href="https://www.nslookup.io/">nslookup.io</a> or <a href="https://dnschecker.org/">dnschecker.org</a>.</p>

<h6 align="center"><img width="550px" src="https://github.com/user-attachments/assets/dc0ffd00-9b1c-4c95-8a9c-78b57b276ba2"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<h3>Attack Techniques Using DNS</h3>
<p>
    
- <strong>Fast Flux Hosting)</strong>: Adversaries rotate many IPs quickly with short cache times to avoid simple blocks. We need to record and escalate when we identify a domain that resolves to changing IPs within a short period and across different providers.<br>
- <strong>CDN Abuse)</strong>: Legitimate CDNs like Cloudflare or Akamai change IPs too, but done within their ASN ecosystem. If the A record points to a major CDN and other values are normal, take note and carry reputation and ownership checks.<br>
- <strong>Typosquatting)</strong>: Domains like paypa1[.]com or micros0ft[.]net trick users visually. If a name looks like a brand clone, treat it as high risk and escalate it.<br>
- <strong>IDN (Internationalised Domain Names)</strong>: Attackers exploit Unicode, creating look-alike domains. Decode Punycode, for example xn--ppaypal-3ya[.]com, and compare to known brands using simple online decoder.</p>

<h3>SOC Analyst Workflow</h3>
<p>At this stage, our workflow in the SOC could look as follows. Be mindful that this would vary depending on established organisational processes and practices.<br>

- <strong>Snapshot Current DNS</strong>: Capture A, NS, MX, TXT, SOA, and TTL values for the domain in question using a single page view and simple.<br>
- <strong>Basic Ownership Check</strong>: Use WHOIS to note registrat, creation date and contact pattern, which supports a light ownership picture of the ticket.<br>
- <strong>Interpret Patterns</strong>: Assess whether the DNS behaviour aligns with benign CDN activity or indicates malicious throwaway domain, noting down the details of the changing IPs.<br>
- <strong>Log Evidence</strong>: Save screenshots or JSON extracts DNS and reputation pages to the case file for audit and escalation.<br>
- <strong>Recommend Action</strong>: Based on findings, advise blocking if high risk, monitor if suspicious but inconclusive, or close if determined benign.</p>

<p><em>Answer the questions below</em><br>
<ol type="1.">
    <li>From the downloadable report, what are the IP addresses for the A Record associated with our flagged domain, advanced-ip-sccanner[.]com? Answer: IP-1, IP-2.&nbsp;&nbsp;&nbsp;<code>172.67.189.143,104.21.9.202</li></code></li>
    <li>What nameserver addresses are associated with the IP address? Defang the addresses.&nbsp;&nbsp;&nbsp;<code>jaziel[.]ns[.]cloudflare[.]com, summer[.]ns[.]cloudflare[.]com</li></code></li>
</ol></p>

<h6 align="center"><img width="500px" src="https://github.com/user-attachments/assets/501ebbc0-b1da-461c-b1bc-c1f3e2df93d6"><br>Task File<br><br>
                   <img width="500px" src="https://github.com/user-attachments/assets/5e516942-5db5-4458-be8b-30309164474a"><br>Task File</h6>


<br>
<h2>Task 3 . IP Enrichment: Geolocation and ASN</h2>
<h3>IP Enrichment Within the SOC</h3>
<p></p>Most SIEM or EDR alerts contain at least one IP address. An IP address is ambiguous by itself: it could belong to a compromised router in a home office, a shared CDN edge, or a cloud service used by thousands of tenants. Without enrichment, we risk overreacting (blocking legitimate infrastructure) or underreacting (ignoring a real command-and-control server).<br>

<strong>Enrichment</strong> is adding ownership, ASN (Autonomous System Number), geolocation, and service context to an IP so that our decision is evidence-driven. SOC Level 1 analysts must perform this consistently, since IPs are the most common indicators in alert queues.</p>

<h3>The Role of RDAP</h3>
<p></p>The <strong>Registration Data Access Protocol (RDAP)</strong> is the authoritative source for IP ownership. Unlike commercial GeoIP services or provider marketing pages, RDAP data is maintained by Regional Internet Registries (RIRs) such as RIPE NCC, ARIN, and APNIC. It tells us precisely who has been provided with the netblock.<br><br>

From RDAP, we obtain:<br>

- NetRange: The range of addresses delegated.<br>
- Organisation: The registered holder (e.g., Amazon, Vodafone, TryHackMe).<br>
- Remarks: Often include whether the block is used for hosting, broadband, or mobile.<br>
- Abuse Contact: The official mailbox for incident reporting.<br>

In our scenario, we can retrieve RDAP details on the IP address 64[.]31[.]63[.]194.</p>

<h6 align="center"><img width="550px" src="https://github.com/user-attachments/assets/82ec356b-de43-46ab-be4f-b0756a83414a"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>If our alert points to suspicious traffic, we should pivot to the domain or certificate to narrow the scope.<br>

We should also preserve audit evidence of this data in reliable formats such as raw RDAP JSON, preventing reliance on potentially outdated secondary sources.</p>

<h3>Autonomous Systems and Heuristics</h3>
<p>An Autonomous System (AS) is a collection of IP prefixes under a single organisation’s control. Each AS is assigned a unique 16 or 32-bit number (ASN), only required for external communications. Looking at the ASN helps analysts assess the likely role of an IP.<br>

- <strong>Hosting ASNs</strong>: Many small netblocks, often with diverse tenants. Suspicious domains are frequently hosted here.<br>
- <strong>Residential ISPs</strong>: These have huge ranges covering millions of users. Alerts on these may indicate compromised home routers or consumer devices.<br>
- <strong>Cloud/CDN ASNs</strong>: Global anycast, dozens of prefixes, shared edges. Blocking whole ranges here causes collateral damage.<br><br>

Some heuristic examples of ASN classification include:<br>

- <strong>AS32934 - Facebook/Meta</strong>: Traffic from here is based on the social media infrastructure. Malicious use may likely indicate an account issue, and not malicious hosting.<br>
- <strong>AS16509 - Amazon AWS</strong>: This would cover a massive cloud space, and attackers would often abuse it for short-lived servers. Blocking the entire ASN would be catastrophic, so we scope to the FQDN or narrow the CIDR.<br>
- <strong>AS124888 - Vodafone</strong>: This covers an ISP. Malicious activity would likely be from a compromised customer device.</p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/fb97c2ba-3a5d-46a9-894e-e3cf18335aac"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<h3>Geolocation: Value and Limitations</h3>
<p>GeoIP is widely used but often misunderstood. Tools like <a href="https://ipinfo.io/">ipinfo.io</a> and <a href="https://iplocation.net/">iplocation.net</a> provide approximate country and city. However, it is worth observing that:<br>

- <strong>Country mismatches</strong> are common. CDN and cloud providers may register ranges in one country but host edges globally.<br>
- <strong>City-level accuracy</strong> is unreliable. SOC analysts should never justify a block based on a city.<br>
- <strong>Jurisdiction</strong> matters in legal escalations: legal teams may pursue takedown requests via the abuse contact if a host is located in a cooperative country.<br><br>

<strong>Best practice</strong>: Record the country reported by at least two sources and note discrepancies. Treat this as a hint, not a fact.</p>

<h3>SOC Analyst Workflow</h3
<p>At this stage, our workflow in the SOC could resemble the following, though it may vary depending on established organisational processes and practices.<br>

- <strong>Start with RDAP</strong>: Confirm netrange, org, ASN, and abuse contacts.<br>
- <strong>Add ASN Context</strong>: Check bgpview.io or ipinfo.io for ASN details and role.<br>
- <strong>Check Geolocation</strong>: Capture country from at least two sources. Record mismatches.<br>
- <strong>Look for rDNS Patterns</strong>: Reverse DNS can hint at hosting type (e.g., *[.]btcentralplus[.]com = UK broadband). Do not base decisions solely on rDNS.<br>
- <strong>Consult Internal Logs</strong>: Has this IP appeared in the last 30 days? If yes, in what context?<br>
- <strong>Classify Role</strong>: Hosting, residential, CDN, or cloud. Record reasoning.<br>
- <strong>Plan Outreach</strong>: If confirmed malicious and in a cooperative ASN, prepare a report for the abuse contact.</p>

<p><em>Answer the questions below</em><br>
<ol type="1.">
    <li>Open <a href="https://client.rdap.org/">client.rdap.org</a> and identify when the 64[.]31[.]63[.]194 IP was logged for registration. (Answer in UTC: MM/DD/YY, H:MM:SS AM/PM)&nbsp;&nbsp;&nbsp;<code>12/27/2010, 3:51:03 PM</code></li>
    <li>What roles are assigned to the entity Entity NOC2791-ARIN associated with the IP address 64[.]31[.]63[.]194?&nbsp;&nbsp;&nbsp;<code>administrative,technical</code></li>
    <li>What is the country's name for the IP 64[.]31[.]63[.]194? &nbsp;&nbsp;&nbsp;<code>France</code></li>
    <li>Can you identify the Autonomous System linked with the IP 64[.]31[.]63[.]194?&nbsp;&nbsp;&nbsp;<code>AS136258</code></li>
</ol></p>

<h6 align="center"><img width="700px" src="https://github.com/user-attachments/assets/7d98e445-46d9-4828-8545-afde505eddaa"><br><a href="https://client.rdap.org/">client.rdap.org</a><br><br>
                   <img width="700px" src="https://github.com/user-attachments/assets/d5615375-b6af-45ec-9aaf-126d04c59cb5"><br><a href="https://client.rdap.org/">client.rdap.org</a><br><br>
                   <img width="700px" src="https://github.com/user-attachments/assets/a42618cf-2faa-41be-9a7e-f2e0c447f070"><br> <a href="https://iplocation.net/">iplocation.net</a><br><br>
                   <img width="700px" src="https://github.com/user-attachments/assets/2984a4ee-ed1a-44c8-a168-3d909cb43a56"><br><a href="https://ipinfo.io/">ipinfo.io</a></h6>

<br>
<h2>Task 4 . Service Exposure</h2>
<h3>Services and Certificates</h3>
<p>Looking at an IP or domain's location data also helps us understand its function. Exposed services provide information on the system's intent and potential blast radius if abused. For example, an IP with RDP exposed on port 3389 may be a target for a brute-force attack.</p>

<h3>Shodan Reconnaissance</h3>
<p>Shodan is a powerful reconnaissance tool for IP address analysis. By indexing internet-connected devices and services, Shodan provides detailed information about open ports, running services, and system configurations. Queries like org:example[.]com reveal all systems associated with specific organisations, while searches for specific software versions help identify vulnerable systems.<br>

Let us look at a sample IP search associated with the IP address from our flagged list, 69[.]197[.]185[.]26.</p>

<h6 align="center"><img width=550px" src="https://github.com/user-attachments/assets/b7473b95-b329-475c-84f6-a885a4a4975e"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>From our search, we can extract information on:<br>

- <strong>Open Ports</strong>: This is the first fingerprint of exposure.<br>
- <strong>Service Banners</strong>: These provide hints on server types and frameworks used. Additionally, software versions and cookies in RDP/HTTP banners can inform us about operator markers.</p>

<h3>TLS Certificates as Infrastructure Clues</h3>
<p>We can look at TLS certificate information using tools such as  <a href=https://crt.sh/">crt.sh</a> as a gold mine for enrichment. Certificate Transparency logs every publicly trusted certificate. The key fields to look out for include:<br>

- <strong>Issuer</strong>: This field provides details on who signed the certificate. For example, Let's Encrypt is a common but neutral vendor. A self-signed certificate may be a sign of a hastily deployed system.<br>
- <strong>Validity Period</strong>: Short-lived certificates of up to 90 days are normal for usage. Analysts must look for bursts of reissued certificates and investigate suspected phishing infrastructure.<br>
- <strong>Subject Alternative Names</strong>: This provides details on the domains covered by the certificate.</p>

<h4>Pivoting and Mapping</h4>
<p>Tools like  <a href=https://search.censys.io/">Censys.io</a> allow analysts to pivot by finding siblings with the same certificate or using a subject fragment to find look-alike clusters. However, some of these features may require an account on the platform.<br>
As analysts, we are to identify suspicious patterns. For example, a burst of issuance within a short period that maps to many domains and mixed hosting ASNs suggests automated kit use.</p>

<h6 align="center"><img width="500px" src="https://github.com/user-attachments/assets/587bba8a-8361-43f0-97cd-c381ef96507d"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<h3>SOC Analyst Workflow</h3>
<p></p>At this stage, our workflow in the SOC could resemble the following, though it may vary depending on established organisational processes and practices.<br>

- <strong>Check Shodan/Censys banners</strong>: Identify exposed services and possible misconfigurations.
- <strong>Review TLS certificates</strong>: Ensure to record issuer, SANs, and validity period.
- <strong>Look for anomalies</strong>: Instances of multiple SANs, brand look-alikes or sudden bursts of issuance.
- <strong>Pivot</strong>: Utilise the certificate or banner artefacts to uncover related infrastructure.
- <strong>Assess blast radius</strong>:<br> - RDP/SSH on residential ASN → shows a likelihood of a compromised endpoint.<br> - TLS with many unrelated SANs on CDN ASN → shared infrastructure, avoid IP block.</p>

<p><em>Answer the questions below</em><br>
<ol type="1.">
    <li>Using <a href="https://www.shodan.io/">shodan.io</a>, find which service is primarily associated with the IP address 85[.]188[.]1[.]133.&nbsp;&nbsp;&nbsp;<code>FTP</code></li>
    <li>Using <a href="https://www.shodan.io/">shodan.io</a>, find which service is primarily associated with the IP address 85[.]188[.]1[.]133.&nbsp;&nbsp;&nbsp;<code>6</code></li>
    <li>Using <a href="https://search.censys.io/">search.censys.io</a>, identify the TLS certificate fingerprint for the IP address.&nbsp;&nbsp;&nbsp;<code>48d6057099841bd18809fd61aa990b17779176de7799f301dac24879da553456</code></li>
    <li>According to  <a href="https://crt.sh/">crt.sh</a>, are there Certificate Transparency log entries captured associated with the TLS certificate identified above? (Answer: Yay or Nay)&nbsp;&nbsp;&nbsp;<code>Yay</code></li>
</ol></p>

<h6 align="center"><img width="700px" src="https://github.com/user-attachments/assets/d7cf2ddb-8603-4805-a622-2118ebef95d7"><br><a href="https://www.shodan.io/">shodan.io</a><br><br>
                   <img width="700px" src="https://github.com/user-attachments/assets/920736b9-6fa3-41da-954e-4aafe76e0415"><br><a href="https://search.censys.io/">search.censys.io</a><br><br>
                   <img width="700px" src="https://github.com/user-attachments/assets/7ba0151e-9e96-4f25-a196-4e018535236e"><br><a href="https://search.censys.io/">search.censys.io</a></h6>

<br>
<h2>Task 5 . Reputation Checks and Passive DNS</h2>
<h3>Why Reputation and History Matter</h3>
<p>By this stage of enrichment, we have uncovered two major intelligence avenues: “Who owns this IP/domain?” and “What services does it expose?” However, we still need to identify more, especially regarding what the infrastructure has been doing over time.<br>

As we know, file hashes are static, while IPs and domains are dynamic assets. Given that a domain may be registered for a phishing campaign today and parked within the week, the IP addresses used may be reassigned to different tenants or pass from malicious to benign use in days.<br>

This makes time context critical when investigating incidents and using threat intelligence to enrich our findings. Reputation services and passive DNS analysis provide us with a way of adding that value.</p>


<h3>Reputation Services</h3>
<p>VirusTotal is a primary reputation source that provides information such as detection ratio and indicator relations.<br>

Another resource is Cisco Talos Intelligence, which provides frequently updated web and email reputation scores and category labels.</p>

<h4>Talos Dashboard</h4>
<p>By default, the dashboard presents an overview of email traffic across numerous countries, with indicators of whether the emails are legitimate, spam, or malware. Any of these markers will produce more information associated with IP and hostname addresses, daily volume, and type.</p>

<h6 align="center"><img width="550px" src="https://github.com/user-attachments/assets/9ab883fc-4473-45ac-94fe-8c989716dcef"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>Additionally, there are other features useful for enrichment:<br>

- Vulnerability Information: Disclosure and zero-day vulnerability reports marked with CVE numbers and CVSS scores. Details of the reported vulnerabilities are provided when you select a specific report, including the timeline to publish the report. Microsoft vulnerability advisories are also provided, with the applicable Snort rules that can be used.<br>
- Reputation Centre: Provides access to searchable threat data related to IPs and files using their SHA256 hashes. Analysts would rely on these options to conduct their investigations. Additional email and spam data are under the Email & Spam Data tab.</p>

<h4>IP2Proxy</h4>
<p>IP2Proxy is another vital resource for labelling VPN, proxy, and Tor exit nodes. These are legitimate shared egress points, which can weaken attribution.</p>

<h6 align="center"><img width="550px" src="https://github.com/user-attachments/assets/35f43bbb-6730-4d42-897e-ffb94e5d75fb"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<h3>Passive DNS</h3>
<p>Passive DNS adds time context in domain enrichment, providing a historical record of how domains resolved over time. The key signals to look at include:<br>

- <strong>First Seen/Last Seen</strong>: These tell us if a domain is new or long-lived.<br>
- <strong>Number of IPs in Time Window</strong>: A high churn over days would suggest flux or agile hosting.<br>
- <strong>ASN Spread</strong>: If IPs belong to many unrelated ASNs, this should be marked as suspicious, while those limited to one ASN should be marked as stable or belonging to a CDN mapping.<br><br>

Beyond using passive DNS to gather domain history, other valuable sources include:<br>

- <strong>Certificate Transparency (CT) Logs</strong>: These logs show certificate issuance history. They are useful for detecting sudden bursts of domains registered under phishing themes.<br>
- <strong>Wayback Machine</strong>: Reveals historical website content. A domain that hosted a blog for years but switched to a phishing kit last week is high-risk.</p>

<h3>SOC Analyst Workflow</h3>
<p>In summary, our workflow in the SOC would look as follows. Be mindful that this would vary depending on established organisational processes and practices.<br>

- <strong>Check VirusTotal</strong>: Record detection ratio, First Seen, Last Seen, and any community notes.<br>
- <strong>Check Cisco Talos</strong>: Record reputation score and category, noting any changes in the last 30 days.<br>
- <strong>Check IP2Proxy</strong>: Flag if VPN/proxy/Tor; adjust severity accordingly.<br>
- <strong>Check Passive DNS</strong>: Record First Seen, Last Seen, number of IPs in the last 7 days, and ASN spread.<br>
- <strong>Check CT Logs</strong>: Note certificate bursts, suspicious SANs.<br>
- <strong>Cross-Reference with Wayback</strong>: Identify content shifts (benign → phishing).<br>
- <strong>Decision</strong>: Block, monitor, or close, with expiry tied to observed activity.</p>

<p><em>Answer the questions below</em><br>
<ol type="1.">
    <li>What file has been linked to the IP 166[.]1.160[.]118?&nbsp;&nbsp;&nbsp;<code>ff4c287c60ede1990442115bddd68201d25a735458f76786a938a0aa881d14ef.exe</code></li>
    <li>What organisation is identified on historical WHOIS lookups?&nbsp;&nbsp;&nbsp;<code>Ace Data Centers, Inc.</code></li>
</ol></p>

<h6 align="center"><img width="700px" src="https://github.com/user-attachments/assets/d5396318-7544-4fa7-b221-072d30b50242"><br><a href="https://www.virustotal.com/">VirusTotal . Detection</a><br><br>
                   <img width="700px" src="https://github.com/user-attachments/assets/74746a65-ba33-4a2b-b7a8-3429294de361"><br><a href="https://www.virustotal.com/">VirusTotal . Relations</a></h6>

<br>
<h2>Task 6 . Operation Integrtion</h2>
<p>Analysts need to understand how to turn intelligence into safe action. The risk here is missing an attack and breaking legitimate business applications through overbroad controls. We avoid that outcome by being precise and planning for expiry and review.</p>

<h3>Safe Integration Patterns</h3>
<p>

- Prefer hostnames when domains are stable: IPs change frequently on CDNs or anycast platforms. Use DNS response policy zones, proxy categories, or SNI filtering.<br>
- Use narrow IPs for single-purpose VPS: When an address is clearly dedicated to staging or command and control, a /32 block is effective with minimal blast radius.<br>
- Set expiry on blocks: Infrastructure is reused and recycled. A seven-day or fourteen-day expiry, with auto-renew on re-observation, prevents permanent collateral damage.<br>Document evidence in SOAR: Include screenshots, RDAP events, certificate excerpts, and reasoning.</p>

<h3>Geofencing Cautions</h3>
<p>Country blocks feel attractive; however, they often break real workflows. Colleagues travel, third-party services use overseas PoPs, and some vendors terminate TLS in unexpected regions. We treat geolocation as enrichment to raise priority, not as a primary control, unless the risk decision has been reviewed with the business and tested.</p>

<h3>Cloud and Large Provider Pitfalls</h3>
<p>Do not add entire CDN IP ranges like Amazon or Microsoft to a deny list. These providers reuse IPs across many customers and services. Blocking a large cloud block will eventually impact business systems. If a malicious hostname is served from a cloud edge network, take action at the domain or path level and consider vendor abuse processes.</p>

<h3>Legal and Provider Considerations</h3>
<p>Knowing the provider and country informs whether evidence preservation or rapid takedown is achievable. Some providers have strong abuse desks and comply quickly with requests. Others are slower or operate under legal frameworks that make urgent actions difficult. Record the RIR ownership and the abuse contacts gathered from RDAP for escalation paths.</p>

<h3>From Data to Decision</h3>
<p>We can now follow a simple playbook to make informed decisions when investigating an indicator.<br>

- Verify: Confirm that the indicator appears in our telemetry and is relevant to our environment.<br>
- Enrich: Collect geolocation, ASN, banners, certificates, reputation, and history.<br>
- Score: Apply the confidence matrix and record the rationale.<br>
- Decide: Block, monitor, or allow. Prefer precise controls, add expiry, and document.<br>
- Hunt and notify: Search for related indicators, inform stakeholders, and create follow-up tasks.</p>

<h6 align="center"><img width="250px" src="https://github.com/user-attachments/assets/567a2104-fdf9-48a2-b758-dc42e7ea4fea"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p><em>Answer the question below</em><br>
<ol type="1.">
    <li>I´m ready to move to the final challenge&nbsp;&nbsp;&nbsp;<code>No answer needed</code></li>
</ol></p>

<h2>Task 7 . Challenge</h2>
<p>It’s 09:10 on a Monday. Over the weekend, Finance reported a burst of “account verification” emails that looked unusually polished. Your secure email gateway caught a subset; one clicked sample was redirected to <code>santagift[.]shop</code>.<br>
At the same time, your EDR shows workstations briefly beaconing to 170[.]130[.]202[.]134.<br><br>
Use the skills and tools covered in the room to enrich the three indicators and answer the questions below.</p>

<p><em>Answer the questions below</em><br>
<ol type="1.">
    <li>What is the RIR associated with 170[.]130[.]202[.]134?&nbsp;&nbsp;&nbsp;<code>ARIN</code></li>
    <li>What ASN is the IP connected with?&nbsp;&nbsp;&nbsp;<code>AS62904</code></li>
    <li>Identify the number of NS records for the domain santagift[.]shop.&nbsp;&nbsp;&nbsp;<code>4</code></li>
    <li>Which NS is identified as the Start of Authority (SOA) for the domain?&nbsp;&nbsp;&nbsp;<code>ns-298.awsdns-37.com</code></li>
    <li>When was the domain registered? (Answer:DD/MM/YYYY)&nbsp;&nbsp;&nbsp;<code>30/10/2022</code></li>
</ol></p>


<h6 align="center"><img width="700px" src="https://github.com/user-attachments/assets/3bc1f3d4-44ce-4bc6-b224-fc2a0fe26287"><br>ipinfo.io<br><br>
                   <img width="700px" src="https://github.com/user-attachments/assets/74746a65-ba33-4a2b-b7a8-3429294de361"><br><code>nslookup satantagift.shop</code><br><br>
                   <img width="700px" src="https://github.com/user-attachments/assets/f16a20c0-49bf-46ab-8410-70a2e6963b30"><br><code>whois 52.92.1.132</code><br><br>
                   <img width="700px" src="https://github.com/user-attachments/assets/fae69d78-412b-4f58-8246-64cbd5a1d705"><br>Whois . DNS Records<br><br>
                   <img width="700px" src="https://github.com/user-attachments/assets/b92f9d0a-e17a-476f-a01e-d214711e75b9"><br>Whois</h6>

<br>
<h2>Task 8 .Conclusion</h2>
<p>Congratulations on gaining more skills in threat intelligence.<br>

We have learned how to enrich and transform raw IPs and domains into decisions leadership can trust. We looked at RDAP for source-of-truth ownership, ASN role to judge risk, DNS patterns to tell flux from CDN, banners, and certificates to infer purpose and discover siblings, reputation, and history to add time context. Furthermore, we also looked at safe-block practices to avoid collateral damage. This workflow scales when automated, and remains effective even as adversaries churn infrastructure.</p>

<p><em>Answer the question below</em><br>
<ol type="1.">
    <li>Complete the room.&nbsp;&nbsp;&nbsp;<code>No answer needed</code></li>
</ol></p>

<br>
<br>
<h2 align="center">Completed</h2>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/192387f1-ca47-4eb1-a158-32f3a90bf464"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/885b6a4b-26cc-48d6-af27-e876c68d5b5f"></p>



<h2 align="center">My TryHackMe Journey</h2>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| 2025, September 3 | 485      |     112ⁿᵈ    |      5ᵗʰ     |     714ᵗʰ   |    13ʳᵈ    | 123,882  |    939    |    73     |

</div>

<p align="center">Global All Time:   112ⁿᵈ<br><img width="250px" src="https://github.com/user-attachments/assets/b5c0eb3f-eec8-4b9e-9b3f-9d49b4187caf"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/ab79edb0-c7a3-4ce8-aa39-9837d5da56c1"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/c0464bcc-2fec-4349-a73b-e7ccb7fc4750"><br>
                  Global monthly:    714ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/4ddb0c0f-36a1-4cb4-94ba-d18ce835e0b7"><br>
                  Brazil monthly:     13ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/8e7cac62-423d-4ff7-963e-8d0e8645d9d9"><br>

<h2 align="center">Thanks for coming!</h2>
<p align="left">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>







