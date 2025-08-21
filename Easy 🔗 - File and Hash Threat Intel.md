<h1 align="center">File and Hash Threat Intel</h1>
<p align="center">2025, August 19<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>471</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>AThis room seeks to teach on enriching file and hash artefacts using threat intelligence.</em><br>
<img width="80px" src="https://github.com/user-attachments/assets/8b0dd014-2e1b-4ce7-8d84-43e508ba3842"><br>
Access this TryHackMe´s walkthrough <a href="https://tryhackme.com/room/fileandhashthreatintel">here </a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/7023575a-62f2-48d1-8e29-8e5895daf862"></p>



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
<p> ... </p>

<br>

<p><em>Answer the question below</em></p>

<p>1.1. Dive into file threat intelligence<br>
<code>No answer needed</code></p>

<br>
<br>
<h2>Task 2 . Filenames and Paths</h2>
<p>You might encounter a suspicious file, such as Setup.exe, and must get as much context about it as possible. Human-readable strings, such as filepaths, are the earliest heuristics available to an analyst. When alone, they do not prove maliciousness but can reveal attacker tradecraft patterns when viewed with scepticism.</p>
<p> ... </p>

<br>

<p><em>Answer the question below</em></p>

<p>2.1. One file displays one of the indicators mentioned. Can you identify the file and the indicator? (Answer: file, property)<br>
<code>___________________________</code></p>

<br>
<br>
<br>
<br>

<p>A</p>

<img width="871" height="86" alt="image" src="https://github.com/user-attachments/assets/f6f6af05-8915-422a-94b2-8a34d32ce51e" />


<p>B</p>

<img width="1345" height="485" alt="image" src="https://github.com/user-attachments/assets/bda52203-b0dc-46b4-bf32-86daa201be9f" />

<p>C</p>

<img width="1141" height="93" alt="image" src="https://github.com/user-attachments/assets/19918b7c-fa1e-47da-9c0a-7007f866109f" />

<p>D</p>
<p>1f8806869616c18cbae9ffcf581c0428915d32fb70119df16d08078d92d1a5e3</p>

<img width="1886" height="885" alt="image" src="https://github.com/user-attachments/assets/3266a111-509a-4a7f-9521-8b88c3af767e" />

<br>
<br>
<h2>Task 3 . File Hash Lookup</h2>
<br>

<p><em>Answer the questions below</em></p>

<p>3.1. What is the SHA256 hash of the file bl0gger?<br>
<code>2672b6688d7b32a90f9153d2ff607d6801e6cbde61f509ed36d0450745998d58</code></p>
<br>


<br>
<p>3.2. On VirusTotal, what is the threat label used to identify the malicious file?<br>
<code>trojan.graftor/flystudio</code></p>
<br>

<img width="1878" height="893" alt="image" src="https://github.com/user-attachments/assets/0d180f18-c3b8-48bd-81f4-cf4bd98d5aff" />

<br>
<p>3.3. When was the file first submitted for analysis? (Answer format: YYYY-MM-DD HH:MM:SS)<br>
<code>2025-05-15 12:03:49</code></p>
<br>

<img width="1898" height="208" alt="image" src="https://github.com/user-attachments/assets/14d0f27e-3f7b-4074-a798-9b1e91661ef6" />

<br>
<p>3.4. According to MalwareBazaar, which vendor classified the Morse-Code-Analyzer file as non-malicious?<br>
<code>CyberFortress</code></p>
<br>


<br>
<p>3.5. On VirusTotal, what MITRE technique has been flagged for persistence and privilege escalation for the Morse-Code-Analyzer file?<br>
<code>DLL Side-Loading</code></p>
<br>


<br>
<br>
<h2>Task 4 . Sandbox Analysis/h2>

<p>4.1. What tags are used to identify the bl0gger.exe malicious file on Hybrid Analysis? (Answer: Tag1, Tag2, Tag3)<br>
<code>BlackMoon, Discovery, windows-server-utility</code></p>
<br>


<br>
<p>4.2. What was the stealth command line executed from the file?<br>
<code>regsvr32 %WINDIR%\Media\ActiveX.ocx /s</code></p>
<br>


<br>
<p>4.3. Which other process was spawned according to the process tree?<br>
<code>werfault.exe</code></p>
<br>


<br>
<p>4.4. The payroll.pdf application seems to be masquerading as which known Windows file?<br>
<code>svchost.exe</code>
<br>

<img width="1101" height="696" alt="image" src="https://github.com/user-attachments/assets/ac89220d-8c5e-493c-ad2f-a8441095cc7a" />

<br>
<p>4.5. What associated URL is linked to the file?<br>
<code>_________</code>
<br>


<br>
<p>4.6. How many extracted strings were identified from the sandbox analysis of the file?<br>
<code>_________</code>
<br>


<br>
<br>
<h2>Task 5 . Threat Intelligence Challenge</h2>
<br>

<p><em>Answer the questions below</em></p>

<p>5.1. What is the SHA256 hash of the file?<br>
<code>43b0ac119ff957bb209d86ec206ea1ec3c51dd87bebf7b4a649c7e6c7f3756e7</code></p>

<br>
<br>
<p>5.2. What family labels are assigned to the file on VirusTotal?<br>
<code>akira, filecryptor</code></p>
<br>

<img width="1336" height="457" alt="image" src="https://github.com/user-attachments/assets/f186d540-be43-4495-9919-46608c1b240e" />

<br>
<br>
<p>5.3. How many security vendors have flagged the file as malicious?.<br>
<code>61</code></p>
<br>

<img width="1335" height="467" alt="image" src="https://github.com/user-attachments/assets/9cc7f9bd-c9a2-4221-ab5b-ba92fafeb0ea" />

<br>
<br>
<p>5.4. Name the text file dropped during the execution of the malicious file.<br>
<code>akira_readme.txt</code></p>

<img width="1344" height="207" alt="image" src="https://github.com/user-attachments/assets/36118ca9-4807-4467-86bb-30b82d5d8570" />

<br>
<br>
<p>5.5. What PowerShell script is observed to be executed?<br>
<code>Get-WmiObject Win32_Shadowcopy | Remove-WmiObject</code></p>

<img width="917" height="554" alt="image" src="https://github.com/user-attachments/assets/5e198ca2-3a01-47df-b421-2c782b081674" />

<br>
<br>
<p>5.6. What is the MITRE ATT&CK ID associated with this execution? <br>
<code>T1490</code></p>
<br>

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
