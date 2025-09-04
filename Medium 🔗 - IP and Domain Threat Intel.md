<h1 align="center">IP and Domain Threat Intel</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/3c4c5c59-8c89-40f8-8562-9ee9712b751e"><br>
2025, September 4<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>486</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>A look into enriching IP and domain insights with open source threat intelligence</em>.<br>
Access it <a href="https://tryhackme.com/room/ipanddomainthreatintel">here</a><br>
<img width="1200px" src="h></p>

<br>
<h2>Task 1 . Introduction</h2>
<p>Security Operations runbooks still revolve around the process <code></code>erify → enrich → decide</code>, but when the alert is a lone IP address or domain, the enrichment phase looks different. Instead of hashes, we pivot on geolocation, ASNs, open-service footprints, and passive DNS to learn whether a connection is routine SaaS traffic or an adversary foothold beacon.</p>

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


<h6 align="center"><img width="700px" src="https://github.com/user-attachments/assets/ca522511-4aec-4701-8508-43c240dec86c"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p><em>Answer the question below</em><br>
<ol type="1.">
    <li>All set to login&nbsp;&nbsp;&nbsp;<code>No answer needed</li></code></li>
</ol></p>

<br>
<h2>Task 2 . IP Building Blocks</h2>

<p><em>Answer the question below</em><br>
<ol type="1.">
    <li>All set to login&nbsp;&nbsp;&nbsp;<code>No answer needed</li></code></li>
</ol></p>

<h2>Task 3 . IP Enrichment: Geolocation and ASN</h2>

<p><em>Answer the questions below</em><br>
<ol type="1.">
    <li>Open client.rdap.org and identify when the 64[.]31[.]63[.]194 IP was logged for registration. (Answer in UTC: MM/DD/YY, H:MM:SS AM/PM)&nbsp;&nbsp;&nbsp;<code>12/27/2010, 3:51:03 PM</code></li>
    <li>OWhat roles are assigned to the entity Entity NOC2791-ARIN associated with the IP address 64[.]31[.]63[.]194?&nbsp;&nbsp;&nbsp;<code>administrative,technical</code></li>
    <li>What is the country's name for the IP 64[.]31[.]63[.]194? &nbsp;&nbsp;&nbsp;<code>France</code></li>
    <li>Can you identify the Autonomous System linked with the IP 64[.]31[.]63[.]194?&nbsp;&nbsp;&nbsp;<code>AS136258</code></li>
</ol></p>


<h6 align="center"><img width="700px" src="https://github.com/user-attachments/assets/7d98e445-46d9-4828-8545-afde505eddaa"><br>RDAP.org</h6>

<h6 align="center"><img width="700px" src="https://github.com/user-attachments/assets/d5615375-b6af-45ec-9aaf-126d04c59cb5"><br>RDAP.org</h6>

<h6 align="center"><img width="700px" src="https://github.com/user-attachments/assets/a42618cf-2faa-41be-9a7e-f2e0c447f070"><br>iplocation.net</h6>

<h6 align="center"><img width="700px" src="https://github.com/user-attachments/assets/2984a4ee-ed1a-44c8-a168-3d909cb43a56"><br>ipinfo.io</h6>


<br>
<h2>Task 4 . Service Exposure</h2>
<h3>Services and Certificates</h3>


<h3>Shodan Reconnaissance</h3>


<h3>TLS Certificates as Infrastructure Clues</h3>



<h3>SOC Analyst Workflow</h3>


<p><em>Answer the questions below</em><br>
<ol type="1.">
    <li>Using <a href="https://www.shodan.io/">shodan.io</a>, find which service is primarily associated with the IP address 85[.]188[.]1[.]133.&nbsp;&nbsp;&nbsp;<code>12/27/2010, 3:51:03 PM</code></li>
    <li>Using <a href="https://www.shodan.io/">shodan.io</a>, find which service is primarily associated with the IP address 85[.]188[.]1[.]133.&nbsp;&nbsp;&nbsp;<code>a6</code></li>
    <li>Using <a href="https://search.censys.io/">search.censys.io</a>, identify the TLS certificate fingerprint for the IP address.&nbsp;&nbsp;&nbsp;<code>    48d6057099841bd18809fd61aa990b17779176de7799f301dac24879da553456</code></li>
    <li>According to  <a href="https://crt.sh/">crt.sh</a>, are there Certificate Transparency log entries captured associated with the TLS certificate identified above? (Answer: Yay or Nay)&nbsp;&nbsp;&nbsp;<code>yAY</code></li>
</ol></p>


<h6 align="center"><img width="700px" src="https://github.com/user-attachments/assets/d7cf2ddb-8603-4805-a622-2118ebef95d7"><br>shodan.io</h6>

<h6 align="center"><img width="700px" src="https://github.com/user-attachments/assets/920736b9-6fa3-41da-954e-4aafe76e0415"><br>search.censys.io</h6>

<h6 align="center"><img width="700px" src="https://github.com/user-attachments/assets/7ba0151e-9e96-4f25-a196-4e018535236e"><br>search.censys.io</h6>

<br>
<h2>Task 5 . Repuration Checks and Passive DNS</h2>
<h3>Why Reputation and History Matter</h3>
<p>By this stage of enrichment, we have uncovered two major intelligence avenues: “Who owns this IP/domain?” and “What services does it expose?” However, we still need to identify more, especially regarding what the infrastructure has been doing over time.<br>

As we know, file hashes are static, while IPs and domains are dynamic assets. Given that a domain may be registered for a phishing campaign today and parked within the week, the IP addresses used may be reassigned to different tenants or pass from malicious to benign use in days.<br>

This makes time context critical when investigating incidents and using threat intelligence to enrich our findings. Reputation services and passive DNS analysis provide us with a way of adding that value.</p>


<h3>Reputation Services</h3>
<p>VirusTotal is a primary reputation source that provides information such as detection ratio and indicator relations.<br>

Another resource is Cisco Talos Intelligence, which provides frequently updated web and email reputation scores and category labels.</p>

<h4>Talos Dashboard</h4>
<p>By default, the dashboard presents an overview of email traffic across numerous countries, with indicators of whether the emails are legitimate, spam, or malware. Any of these markers will produce more information associated with IP and hostname addresses, daily volume, and type.</p>

<img width="1916" height="982" alt="image" src="https://github.com/user-attachments/assets/9ab883fc-4473-45ac-94fe-8c989716dcef" />

<p>Additionally, there are other features useful for enrichment:<br>

- Vulnerability Information: Disclosure and zero-day vulnerability reports marked with CVE numbers and CVSS scores. Details of the reported vulnerabilities are provided when you select a specific report, including the timeline to publish the report. Microsoft vulnerability advisories are also provided, with the applicable Snort rules that can be used.<br>
- Reputation Centre: Provides access to searchable threat data related to IPs and files using their SHA256 hashes. Analysts would rely on these options to conduct their investigations. Additional email and spam data are under the Email & Spam Data tab.</p>

<h4>IP2Proxy</h4>
<p>IP2Proxy is another vital resource for labelling VPN, proxy, and Tor exit nodes. These are legitimate shared egress points, which can weaken attribution.</p>

<img width="1800" height="1996" alt="image" src="https://github.com/user-attachments/assets/35f43bbb-6730-4d42-897e-ffb94e5d75fb" />

<h3>Passive DNS</h3>
<p>Passive DNS adds time context in domain enrichment, providing a historical record of how domains resolved over time. The key signals to look at include:<br>

 First Seen/Last Seen: These tell us if a domain is new or long-lived.<br>
 Number of IPs in Time Window: A high churn over days would suggest flux or agile hosting.<br>
- ASN Spread: If IPs belong to many unrelated ASNs, this should be marked as suspicious, while those limited to one ASN should be marked as stable or belonging to a CDN mapping.<br><br>

Beyond using passive DNS to gather domain history, other valuable sources include:<br>

- Certificate Transparency (CT) Logs: These logs show certificate issuance history. They are useful for detecting sudden bursts of domains registered under phishing themes.<br>
- Wayback Machine: Reveals historical website content. A domain that hosted a blog for years but switched to a phishing kit last week is high-risk.</p>


<h3>SOC Analyst Workflow</h3>
<p>In summary, our workflow in the SOC would look as follows. Be mindful that this would vary depending on established organisational processes and practices.<br>

- Check VirusTotal: Record detection ratio, First Seen, Last Seen, and any community notes.<br>
- Check Cisco Talos: Record reputation score and category, noting any changes in the last 30 days.<br>
- Check IP2Proxy: Flag if VPN/proxy/Tor; adjust severity accordingly.<br>
- Check Passive DNS: Record First Seen, Last Seen, number of IPs in the last 7 days, and ASN spread.<br>
- Check CT Logs: Note certificate bursts, suspicious SANs.<br>
- Cross-Reference with Wayback: Identify content shifts (benign → phishing).<br>
- Decision: Block, monitor, or close, with expiry tied to observed activity.</p>

<p><em>Answer the questions below</em><br>
<ol type="1.">
    <li>What file has been linked to the IP 166[.]1.160[.]118?&nbsp;&nbsp;&nbsp;<code></code>ff4c287c60ede1990442115bddd68201d25a735458f76786a938a0aa881d14ef.exe</code></li>
    <li>What organisation is identified on historical WHOIS lookups?&nbsp;&nbsp;&nbsp;<code>Ace Data Centers, Inc.</code></li>
</ol></p>

virustotal.com, Detection

<img width="1904" height="594" alt="image" src="https://github.com/user-attachments/assets/d5396318-7544-4fa7-b221-072d30b50242" />

virustotal.com, Relations

<img width="1889" height="886" alt="image" src="https://github.com/user-attachments/assets/74746a65-ba33-4a2b-b7a8-3429294de361" />

<br>
<h2>Task 6 . Operation Integrtion</h2>
<p>Analysts need to understand how to turn intelligence into safe action. The risk here is missing an attack and breaking legitimate business applications through overbroad controls. We avoid that outcome by being precise and planning for expiry and review.</p>p>

<h3>Safe Integration Patterns</h3>
- Prefer hostnames when domains are stable: IPs change frequently on CDNs or anycast platforms. Use DNS response policy zones, proxy categories, or SNI filtering.<br>
- Use narrow IPs for single-purpose VPS: When an address is clearly dedicated to staging or command and control, a /32 block is effective with minimal blast radius.<br>
- Set expiry on blocks: Infrastructure is reused and recycled. A seven-day or fourteen-day expiry, with auto-renew on re-observation, prevents permanent collateral damage.<br>Document evidence in SOAR: Include screenshots, RDAP events, certificate excerpts, and reasoning.<br><br>

<h3>Geofencing Cautions</h3>h3>
Country blocks feel attractive; however, they often break real workflows. Colleagues travel, third-party services use overseas PoPs, and some vendors terminate TLS in unexpected regions. We treat geolocation as enrichment to raise priority, not as a primary control, unless the risk decision has been reviewed with the business and tested.

<h3>Cloud and Large Provider Pitfalls</h3>
<p></p>Do not add entire CDN IP ranges like Amazon or Microsoft to a deny list. These providers reuse IPs across many customers and services. Blocking a large cloud block will eventually impact business systems. If a malicious hostname is served from a cloud edge network, take action at the domain or path level and consider vendor abuse processes.</p>

<h3>Legal and Provider Considerations</h3>h3>
<p></p>Knowing the provider and country informs whether evidence preservation or rapid takedown is achievable. Some providers have strong abuse desks and comply quickly with requests. Others are slower or operate under legal frameworks that make urgent actions difficult. Record the RIR ownership and the abuse contacts gathered from RDAP for escalation paths.</p>

<h3>From Data to Decision</h3>
<p>We can now follow a simple playbook to make informed decisions when investigating an indicator.<br>

- Verify: Confirm that the indicator appears in our telemetry and is relevant to our environment.<br>
- Enrich: Collect geolocation, ASN, banners, certificates, reputation, and history.<br>
- Score: Apply the confidence matrix and record the rationale.<br>
- Decide: Block, monitor, or allow. Prefer precise controls, add expiry, and document.<br>
- Hunt and notify: Search for related indicators, inform stakeholders, and create follow-up tasks.</p>

<img width="1401" height="1080" alt="image" src="https://github.com/user-attachments/assets/567a2104-fdf9-48a2-b758-dc42e7ea4fea" />

<p><em>Answer the question below</em><br>
<ol type="1.">
    <li>I´m ready to move to the final challenge&nbsp;&nbsp;&nbsp;<code></code>No answer needed</code></li>
</ol></p>

<h2>Task 7 . Challenge</h2>
<p>It’s 09:10 on a Monday. Over the weekend, Finance reported a burst of “account verification” emails that looked unusually polished. Your secure email gateway caught a subset; one clicked sample was redirected to <code>santagift[.]shop</code>.<br><br>
At the same time, your EDR shows workstations briefly beaconing to 170[.]130[.]202[.]134.<br><br>

Use the skills and tools covered in the room to enrich the three indicators and answer the questions below.</p>

<p><em>Answer the questions below</em><br>
<ol type="1.">
    <li>What is the RIR associated with 170[.]130[.]202[.]134?&nbsp;&nbsp;&nbsp;<code>ARIN</code></li>
    <li>What ASN is the IP connected with?&nbsp;&nbsp;&nbsp;<code>__________________________________</code></li>
    <li>Identify the number of NS records for the domain santagift[.]shop.&nbsp;&nbsp;&nbsp;<code>4</code></li>
    <li>Which NS is identified as the Start of Authority (SOA) for the domain?&nbsp;&nbsp;&nbsp;<code>ns-298.awsdns-37.com</code></li>
    <li>When was the domain registered? (Answer:DD/MM/YYYY)&nbsp;&nbsp;&nbsp;<code>30/10/2022</code></li>
</ol></p>

ipinfo.io

<img width="1868" height="474" alt="image" src="https://github.com/user-attachments/assets/3bc1f3d4-44ce-4bc6-b224-fc2a0fe26287" />



nslookup santagift.shop

whois 52.92.1.132

<img width="1172" height="732" alt="image" src="https://github.com/user-attachments/assets/f16a20c0-49bf-46ab-8410-70a2e6963b30" />




Whois DNS Records

<img width="1884" height="814" alt="image" src="https://github.com/user-attachments/assets/fae69d78-412b-4f58-8246-64cbd5a1d705" />


Whois

<img width="1887" height="822" alt="image" src="https://github.com/user-attachments/assets/b92f9d0a-e17a-476f-a01e-d214711e75b9" />



<h2>Task 8 .Conclusion</h2>




<br>
<br>









