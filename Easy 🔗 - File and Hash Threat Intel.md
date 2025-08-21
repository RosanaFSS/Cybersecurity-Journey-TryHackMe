<h1 align="center">File and Hash Threat Intel</h1>
<p align="center">2025, August 21<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>472</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>AThis room seeks to teach on enriching file and hash artefacts using threat intelligence.</em><br>
<img width="80px" src="https://github.com/user-attachments/assets/8b0dd014-2e1b-4ce7-8d84-43e508ba3842"><br>
Access this TryHackMe´s walkthrough <a href="https://tryhackme.com/room/fileandhashthreatintel">here </a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/dae64b77-18e1-4b0e-93a7-8cccf1328d32"></p>


<br>
<h2>Task 1 . Introduction</h2>
<p>Security Operations teams live inside alert queues and triaging. Every entry follows three essential steps: verify, enrich, and decide. File and hash intelligence sits squarely in the enrich phase, transforming a lone path or hash value into contextual knowledge within your organisation about malicious artefacts that would be identified.</p>

<h3>Learning Objectives</h3>
<p>By completing this room, you will be able to:<br>

- Interpret suspicious filepaths and filenames using heuristics.<br>
- Generate and validate file hashes.<br>
- Leverage VirusTotal and MalwareBazaar to enrich newly observed binaries.<br>
- Extract behaviour from sandbox telemetry and map it to MITRE ATT&CK.</p>

<h3>Prequisites</h3>
<p>Before embarking on the journey, ensure that you have covered the following concepts and rooms:<br>

- Familiarity with basic Windows and Linux shell utilities.<br>
- Intro to Cyber Threat Intelligence.</p>

<h3>Scenario</h3>
<p>It is a Monday in April. <strong>TryDaily</strong> is preparing a significant release. The EDR tool flags multiple binaries on various workstations during a routine alert sweep. You, the L1 analyst (shadowing your L2 mentor), receive a curated triage package containing those samples. Within <strong>60 minutes</strong>, you must provide evidence to showcase whether these files are <em>bait, benign, or malicious</em>.</p>

<h3>Lab Access</h3>
<p>Before proceeding, start the lab by clicking the <strong>Start Machine</strong> button below. The VM will open in split view and take about 2 minutes to load fully. If it is not visible, click the Show Split View button at the top of the page.</p>

<br>

<p align="center"><img width="400px" src="https://github.com/user-attachments/assets/65bf2167-f533-452d-8a5c-1c6bbc5378fe"></p>

<br>

<p><em>Answer the question below</em></p>

<p>1.1. Dive into file threat intelligence<br>
<code>No answer needed</code></p>

<br>
<br>
<h2>Task 2 . Filenames and Paths</h2>
<p>You might encounter a suspicious file, such as Setup.exe, and must get as much context about it as possible. Human-readable strings, such as filepaths, are the earliest heuristics available to an analyst. When alone, they do not prove maliciousness but can reveal attacker tradecraft patterns when viewed with scepticism.</p>
<h3>Filepath Analysis</h3>
<p>File paths and names are like crime scene clues, revealing attacker behaviour. Attackers may use different disk locations to hide their actions and reduce visibility. For example:

- C:\ (System drive) can be a common target for persistence mechanisms.<br>
- C:\Users\Public profile can enable cross-user access of detonated adversary tools.<br>
- C:\Users\Public\Public Downloads provides a high-traffic directory that would often evade strict monitoring.</p>

<p>Additionally, adversaries may utilise other malware staging patterns such as:<br>

- Utilising temporary directories such as C:\Windows\Temp\ for ephemeral payloads.<br>
- Placing payloads in writable system paths, such as C:\ProgramData\ for stealth persistence.</p>

<h3>Filename Heuristic Indicators</h3>
<p>Attackers are also known to modify filenames to escape detection through implementing various types of heuristic indicators, including:<br><br>

- <code>Double extensions</code> - An example of this would be <code>invoice.pdf.exe</code>, which leverages default Windows settings that hide file extensions.<br><br>

- <code>System binary impersonation</code> - A filename such as <code>scvhost.exe</code> abuses the user's familiarity with core system processes. Defenders should include legitimate locations for system processes in an allowlist, rather than standalone filenames.<br><br>

- <code>High-entropy Strings</code> – A filename such as <code>jh8F21.exe</code> suggests automated packing or polymorphic generation, which is commonly used in a high-churn phishing operation.<br><br>

- <code>Masquerading</code> - Filenames such as <code>backup-2300.exe</code> can blend with routine files, thus leveraging on reduced suspicion. Another example is a single character substitution, which can bypass detection while looking visually legitimate to an unsuspecting employee.</p>

<br>

<p><em>Answer the question below</em></p>

<p>2.1. One file displays one of the indicators mentioned. Can you identify the file and the indicator? (Answer: file, property)<br>
<code>payroll.pdf, Double extensions</code></p>

<br>

<img width="1002" height="594" alt="image" src="https://github.com/user-attachments/assets/9ac9b125-eb86-447f-a7be-778e855b0184" />

<br>
<br>
<br>
<h2>Task 3 . File Hash Lookup</h2>
<br>

<p><em>Answer the questions below</em></p>

<p>3.1. What is the SHA256 hash of the file bl0gger?<br>
<code>2672b6688d7b32a90f9153d2ff607d6801e6cbde61f509ed36d0450745998d58</code></p>
<br>

<img width="1299" height="480" alt="image" src="https://github.com/user-attachments/assets/32f2ed54-a545-45cc-b24c-7395f580eca9" />

<br>
<br>
<br>
<p>3.2. On VirusTotal, what is the threat label used to identify the malicious file?<br>
<code>trojan.graftor/flystudio</code></p>
<br>

<img width="1878" height="893" alt="image" src="https://github.com/user-attachments/assets/0d180f18-c3b8-48bd-81f4-cf4bd98d5aff" />

<br>
<br>
<br>
<p>3.3. When was the file first submitted for analysis? (Answer format: YYYY-MM-DD HH:MM:SS)<br>
<code>2025-05-15 12:03:49</code></p>
<br>

<img width="1898" height="208" alt="image" src="https://github.com/user-attachments/assets/14d0f27e-3f7b-4074-a798-9b1e91661ef6" />

<br>
<br>
<br>
<p>3.4. According to MalwareBazaar, which vendor classified the Morse-Code-Analyzer file as non-malicious?<br>
<code>CyberFortress</code></p>
<br>

<p>

- https://bazaar.abuse.ch/<br>
- sha256:1F8806869616C18CBAE9FFCF581C0428915D32FB70119DF16D08078D92D1A5E3</p>
<br>


<img width="1307" height="128" alt="image" src="https://github.com/user-attachments/assets/98fe8dcf-c9ec-4509-8da5-7a65aa890b97" />

<br>
<br>

<img width="1257" height="583" alt="image" src="https://github.com/user-attachments/assets/c176f9d7-1bc0-4f03-9a75-501b8bc78de1" />

<br>
<br>

<img width="1307" height="405" alt="image" src="https://github.com/user-attachments/assets/99bc1484-2e5c-4a76-b69a-407e5a8a1e8a" />

<br>
<br>
<br>
<p>3.5. On VirusTotal, what MITRE technique has been flagged for persistence and privilege escalation for the Morse-Code-Analyzer file?<br>
<code>DLL Side-Loading</code></p>
<br>

<img width="1896" height="731" alt="image" src="https://github.com/user-attachments/assets/2f29707f-92d0-4122-9c47-0bfdd228eda2" />

<br>
<br>

<img width="1902" height="290" alt="image" src="https://github.com/user-attachments/assets/df3a29a9-6b7e-4803-aebc-e4ee1a6f5b76" />

<br>
<br>

<h2>Task 4 . Sandbox Analysis</h2>
<br>

<p><em>Answer the questions below</em></p>

<p>4.1. What tags are used to identify the bl0gger.exe malicious file on Hybrid Analysis? (Answer: Tag1, Tag2, Tag3)<br>
<code>BlackMoon, Discovery, windows-server-utility</code></p>
<br>

<img width="1316" height="455" alt="image" src="https://github.com/user-attachments/assets/b59a869f-979b-45ff-bcad-51859bd684fb" />

<br>
<br>
<br>
<p>4.2. What was the stealth command line executed from the file?<br>
<code>regsvr32 %WINDIR%\Media\ActiveX.ocx /s</code></p>
<br>

<img width="1308" height="303" alt="image" src="https://github.com/user-attachments/assets/c54a0365-83c2-4000-9f79-1d45af675524" />

<br>
<br>

<img width="1310" height="409" alt="image" src="https://github.com/user-attachments/assets/600b7a86-f116-408f-8f88-ff3e652d06b9" />

<br>
<br>
<br>
<p>4.3. Which other process was spawned according to the process tree?<br>
<code>werfault.exe</code></p>
<br>

<img width="1306" height="346" alt="image" src="https://github.com/user-attachments/assets/09948fe1-d5cb-4a66-a223-9b3f716bc0de" />

<br>
<br>
<br>
<p>4.4. The payroll.pdf application seems to be masquerading as which known Windows file?<br>
<code>svchost.exe</code></p>
<br>

<p><img width="1077" height="501" alt="image" src="https://github.com/user-attachments/assets/4de2b29d-f59d-4363-86da-9bdc9ffb0481" /></p>

<br>
<br>

<p>
  
- D202ED020ED8E36BD8A0F5B571A19D386C12ABECB2A28C989D50BBF92C78F54E</p>
<br>

<p><img width="1311" height="682" alt="image" src="https://github.com/user-attachments/assets/a9e6e6c6-01ba-4d99-bf39-22c5f80b1470" /></p>

<br>
<br>

<p><img width="1226" height="757" alt="image" src="https://github.com/user-attachments/assets/e299db91-ebf2-4cae-8bd7-9785ca43a027" /></p>


<br>
<br>
<br>
<p>4.5. What associated URL is linked to the file?<br>
<code>hxxp://121.182.174.27:3000/server.exe</code></p>
<br>

<p><img width="1222" height="308" alt="image" src="https://github.com/user-attachments/assets/cff088b4-1f8d-4ff1-9b39-f9895a36e200" /></p>

<br>
<br>
<br>
<p>4.6. How many extracted strings were identified from the sandbox analysis of the file?<br>
<code>454</code></p>
<br>

<p><img width="1222" height="301" alt="image" src="https://github.com/user-attachments/assets/6bbfef03-3421-4643-9d56-0834e4033faa" /></p>

<br>
<br>
<br>
<h2>Task 5 . Threat Intelligence Challenge</h2>
<br>

<p><em>Answer the questions below</em></p>

<p>5.1. What is the SHA256 hash of the file?<br>
<code>43b0ac119ff957bb209d86ec206ea1ec3c51dd87bebf7b4a649c7e6c7f3756e7</code></p>

<img width="871" height="86" alt="image" src="https://github.com/user-attachments/assets/f6f6af05-8915-422a-94b2-8a34d32ce51e" />

<br>
<br>
<br>
<p>5.2. What family labels are assigned to the file on VirusTotal?<br>
<code>akira, filecryptor</code></p>

<img width="1336" height="457" alt="image" src="https://github.com/user-attachments/assets/f186d540-be43-4495-9919-46608c1b240e" />

<br>
<br>
<br>
<p>5.3. How many security vendors have flagged the file as malicious?.<br>
<code>61</code></p>

<img width="1335" height="467" alt="image" src="https://github.com/user-attachments/assets/9cc7f9bd-c9a2-4221-ab5b-ba92fafeb0ea" />

<br>
<br>
<br>
<p>5.4. Name the text file dropped during the execution of the malicious file.<br>
<code>akira_readme.txt</code></p>
<br>

<img width="1141" height="93" alt="image" src="https://github.com/user-attachments/assets/19918b7c-fa1e-47da-9c0a-7007f866109f" />

<br>
<br>

<img width="1344" height="207" alt="image" src="https://github.com/user-attachments/assets/36118ca9-4807-4467-86bb-30b82d5d8570" />

<br>
<br>
<br>
<p>5.5. What PowerShell script is observed to be executed?<br>
<code>Get-WmiObject Win32_Shadowcopy | Remove-WmiObject</code></p>

<img width="917" height="554" alt="image" src="https://github.com/user-attachments/assets/5e198ca2-3a01-47df-b421-2c782b081674" />

<br>
<br>
<br>
<p>5.6. What is the MITRE ATT&CK ID associated with this execution? <br>
<code>T1490</code></p>
<p>
  
- https://attack.mitre.org/versions/v14/techniques/T1490/</p>

<br>

<img width="1901" height="649" alt="image" src="https://github.com/user-attachments/assets/bb3599c1-7477-4cf2-8afb-df6883d7d2a6" />

<br>
<br>
<h2>Task 6 . Conclusion</h2>
<p>Congratulations on completing the room! Threat intelligence is integral to an SOC workflow that enriches unknown binaries encountered by threat alerts.</p>
<h3>Key Takeaways</h3>
<p>

- Validate evidence before analysis: confirm you have the exact binaries and hashes.<br>
- Analyse filepaths and filenames for quick context: Unusual storage locations, trusted software directories, and naming tricks highlight items that warrant deeper review.<br>
- Generate hashes early to pivot into external or internal knowledge bases.<br>
- Observe runtime behaviour in a controlled environment to confirm intent, extract network and persistence indicators, and map activity to recognised attack techniques.<br>
- Translate findings into a brief that lists indicators by type, summarises behaviour and provides proportionate recommendations supported by evidence.</p>

<p><em>Answer the questions below</em></p>

<p>6.1. I am ready to continue with more threat intelligence!<br>
<code>No answer needed</code></p>

<br>
<br>


<br>
<br>

<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/835bd5fa-43e1-453d-bb8f-aa2abc4392f1"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/0198cbf1-79d3-4d7a-91a9-b94fcc18ff8d"></p>


<br>

<img width="1892" height="889" alt="image" src="https://github.com/user-attachments/assets/34711c50-a11f-44bb-b8d7-768fe50e793d" />


<h1 align="center">My TryHackMe Journey</h1>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| 2025, August 21   | 472      |     118ᵗʰ    |      5ᵗʰ     |     326ᵗʰ   |     9ᵗʰ    | 122,182  |    922    |    73     |

</div>

<p align="center">Global All Time:   118ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/1fe63294-45db-49ca-ae7a-e1aa600bdc80"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/34711c50-a11f-44bb-b8d7-768fe50e793d"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/fe556708-5e07-44ea-950b-d685c9c2e90f"><br>
                  Global monthly:    382ⁿᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/898eec3e-e12a-4af8-884d-b73a2d3dbbb6"><br>
                  Brazil monthly:      8ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/090b3f6a-787b-4aa5-9f92-90f05a5e203b"><br>

<br>
<h1 align="center">Thanks for Coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 
