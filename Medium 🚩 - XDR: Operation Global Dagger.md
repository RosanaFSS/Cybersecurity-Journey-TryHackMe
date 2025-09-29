<h1 align="center">XDR: Operation Global Dagger</h1>
<p align="center"><img width="80px" src="https://github.com/user-attachments/assets/e5eea092-44e4-46bd-bc14-4ae9d24246a3"><br>
2025, September 29<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>,<br>
and I’m excited to join you on this adventure, part of my <code>511</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>
<em>Investigate and detect potential threats across your environment</em>.<br>
Access it <a href="https://tryhackme.com/room/xdroperationglobaldagger"</a>here.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/5ae55978-4d7c-4660-8a14-759921f00de4"></p>

<h2 align="center">Task 1 . Deploy the machine and Get the Flags!</h2>

<h3>Scenario</h3>
<p>Today, your organisation's threat intelligence (TI) team received classified briefings regarding an ongoing nation-state threat campaign - Operation Global Dagger. Global Dagger has targeted hundreds of global corporations using compromised software updates, remote code execution, credential theft, and cloud-based exfiltration on devices. The security team has also received alerts from Defender XDR of potential malicious activities to evade security measures. As a SOC Level 2 analyst, you have been urgently assigned to investigate these suspicious incidents that surfaced through Microsoft Defender XDR. You need to hunt, analyse, and report these malicious incidents before sensitive data is exfiltrated for containment.</p>

<h3>Room Objectives</h3>
<p>In the next task, you will be required to use different Microsoft Defender XDR products and features to detect and investigate various activities within your organisation, such as:<br>

- Privileged users' activities<br>
- Malicious executions on devices<br>
- Evasion of security tools<br>
- Lateral movement</p>

<h3>Prerequisites</h3>
<p>
  
- <a href="https://tryhackme.com/module/defender">Microsoft Defender XDR</a> module<br>
- <a href="https://tryhackme.com/room/mitre">MITRE</a> room</p>

<p><em>Answer the question below</em></p>

<p>1.1. I am ready!<br>
<code>No answer needed</code></p>

<h2 align="center">Task 2 . <code>Investigate</code> Operation Global Dagger 1</h2>
<p></p>Login to the Defender XDR portal with the credentials below, then navigate to <code>Incidents & alerts -> Incidents</code> to start your investigation.</p>

<h6 align="center"><img width="400px" src="https://github.com/user-attachments/assets/cfb7e4fd-c59b-4ee9-ada5-ade81a4bb403"><br>This image and all the theoretical content of the present article is TryHackMe´s property.<br></h6>

<p>There are a lot of unusual user and machine behaviours that need investigation before escalation to a senior analyst.<br>

Will be using incident ID 49 <strong>Hands-on keyboard attack was launched from a compromised account (attack disruption)</strong> for our investigation.</p>

<p><em>Answer the questions below</em></p>

<br>
<br>
<br>
<p>2.1. What is the <code>name of the threat</code> found on the PowerSploit post-exploitation tool alert?<br>
<code>HackTool:PowerShell/PowerSploit.F</code></p>

<p>

- click <em>Investigation & response</em><br>
- <em>Incident & alerts</em><br>
- <em>Incidents</em></p>

<img width="1908" height="770" alt="image" src="https://github.com/user-attachments/assets/9d8f0742-dee6-4ad8-884c-156f7bf8544d" />

<br>
<br>
<br>

<img width="1905" height="895" alt="image" src="https://github.com/user-attachments/assets/14efa5e4-e45d-4ac4-b871-fa485792ed9b" />

<br>
<br>
<br>

<img width="1903" height="750" alt="image" src="https://github.com/user-attachments/assets/d4e9a9f9-613f-457a-b7eb-8003ef2ae7e9" />

<br>
<br>
<br>
<p>2.2. What is the <code>remediation action result</code> for the alert from <code>question 1</code>?<br>
<code>Success</code></p>

<img width="1903" height="750" alt="image" src="https://github.com/user-attachments/assets/277e6b8b-eb29-4e0a-b1ff-18f106fc4ace" />

<br>
<br>
<br>
<p>2.3. What is the <code>name of the threat</code> you found in the alert <strong>An active 'DumpLsass' hacktool in a command line was prevented from executing</strong>?<br>
<code>HackTool:Win32/DumpLsass.R</code></p>

<img width="1902" height="896" alt="image" src="https://github.com/user-attachments/assets/d94674b2-ce95-4a87-9f8a-ee1fac99dade" />

<br>
<br>
<br>
<p>2.4. What is the <code>detection status</code> for the alert from <code>question 3</code>?<br>
<code>Blocked</code></p>

<img width="1891" height="896" alt="image" src="https://github.com/user-attachments/assets/41a9e805-b1a9-4d5c-aef9-6b50b6b312ad" />

<br>
<br>
<br>
<p>2.5. What was the <code>initiating process</code> for the alert from <code>question 3</code>?<br>
<code>powershell.exe</code></p>

<img width="1880" height="872" alt="image" src="https://github.com/user-attachments/assets/f3b070a2-501a-4354-b356-a1b01b8c0d0e" />

<br>
<br>
<br>
<p>2.6. What is the <code>name of the privilege escalation alert</code>code> found by Defender XDR?<br>
<code>UAC bypass was detected</code></p>

<img width="1843" height="854" alt="image" src="https://github.com/user-attachments/assets/81f7b09b-46ca-4fe5-924a-7b5cf8266a6c" />

<br>
<br>
<br>
<p>2.7. What is the <code>location of the set value data</code> for the alert from <code>question 6</code>?<br>
<code>c:\windows\System32\#{payload}</code></p>

<img width="1913" height="895" alt="image" src="https://github.com/user-attachments/assets/924ede51-17ba-4295-a98a-b64879338268" />

<br>
<br>
<br>
<p>2.8. What is the <code>file path of the image</code> of the alert from <code>question 6</code>?<br>
<code>C:\Windows\System32\reg.exe</code></p>

<img width="1903" height="899" alt="image" src="https://github.com/user-attachments/assets/7ca5e35a-5466-4072-afff-b3a8d1187999" />

<br>
<br>
<br>
<p>2.9. Which <code>lateral movement alert</code> is associated with a  <code>high severity</code>?<br>
<code>Compromised account conducting hands-on-keyboard attack</code></p>

<img width="1905" height="863" alt="image" src="https://github.com/user-attachments/assets/89fb757c-3617-431a-8c29-51344543b1bf" />


<br>
<br>
<br>
<p>2.9. What is the  <code>command-line query</code> used to execute the attack for the alert from <code>question 9</code>?<br>
<code>"ie4uinit.exe" -UserConfig</code></p>


<img width="1904" height="887" alt="image" src="https://github.com/user-attachments/assets/0b79829e-0445-4ea4-8954-48a7ec848899" />

<br>
<br>
<br>

<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/2455a85b-89b1-4d4c-b198-dd0b534f2105"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/4ed59a77-97e1-492c-b402-1e02502fc9d2"></p>

<h1 align="center">My TryHackMe Journey ・ 2025, September</h1>

<div align="center"><h6>

| Date   | Room                                  |Streak   |All Time<br>Global|All Time<br>Brazil|Monthly<br>Global|Monthly<br>Brazil|Points|Rooms<br>Completed|Badges|
|:------:|:--------------------------------------|--------:|------------:|------------:|------------:|------------:|------------:|------------:|------------:|
|29      |Medium 🚩 - <strong>XDR: Operation Global Dagger</strong> | 511| 109ᵗʰ | 4ᵗʰ  |     217ᵗʰ    |     5ᵗʰ    | 127,784  |    980    |    76     |
|28      |Hard 🚩 - Sea Surfer, in progress      | 510    |     -        |      4ᵗʰ     |     -        |     -      | -        |    979    |    76     |
|28      |Medium 🔗 - Windows PrivEsc Arena, in progress|510 | -         |      4ᵗʰ     |     -        |     -      | -        |    979    |    76     |
|27      |Medium 🚩 - Backtrack                  | 509    |     109ᵗʰ    |      4ᵗʰ     |     318ᵗʰ    |     5ᵗʰ    | 127,334  |    979    |    76     |
|26      |Medium 🚩 - ContainMe                  | 508    |     109ᵗʰ    |      4ᵗʰ     |     301ˢᵗ    |     5ᵗʰ    | 127,304  |    978    |    76     |
|26      |Medium 🚩 - Sequence                   | 508    |     110ᵗʰ    |      4ᵗʰ     |     301ˢᵗ    |     5ᵗʰ    | 127,274  |    977    |    76     |
|25      |Medium 🔗 - Introduction to Honeypots  | 507    |     109ᵗʰ    |      4ᵗʰ     |     305ᵗʰ    |     5ᵗʰ    | 127,214  |    976    |    76     |
|25      |Medium 🔗 - Windows x64 Assembly       | 507    |     109ᵗʰ    |      4ᵗʰ     |     303ʳᵈ    |     5ᵗʰ    | 127,110  |    975    |    76     | 
|25      |Easy 🔗 - Network Secuity Essentials   | 507    |     112ⁿᵈ    |      4ᵗʰ     |     302ⁿᵈ    |     5ᵗʰ    | 126,990  |    974    |    76     | 
|24      |Medium 🔗 - Linux Threat Detection 1   | 506    |     110ᵗʰ    |      4ᵗʰ     |     330ᵗʰ    |     5ᵗʰ    | 126,894  |    973    |    76     | 
|24      |Hard 🚩 - Iron Corp                    | 506    |     111ˢᵗ    |      4ᵗʰ     |     363ʳᵈ    |     5ᵗʰ    | 126,768  |    972    |    76     |    
|23      |Medium 🔗 - Intro to Credential Harvesting|505  |     109ᵗʰ    |      4ᵗʰ     |     346ᵗʰ    |     5ᵗʰ    | 126,768  |    971    |    76     |    
|22      |                                        | 504   |              |      4ᵗʰ     |              |             |         |            |    76     |    
|21      |                                        | 503   |              |      4ᵗʰ     |              |             |         |            |    76     |    
|20      |                                        | 502   |              |      4ᵗʰ     |              |             |         |            |    76     |    
|19      |                                        | 501   |              |      4ᵗʰ     |              |             |         |            |    76     |        
|18      |Easy 🔗 - Detecting Web DDos           | 500    |     106ᵗʰ    |      4ᵗʰ     |     312ⁿᵈ    |     4ᵗʰ    | 126,674  |    970    |    76     |
|17      |Medium 🔗 - DLL Hijacking              | 499    |     106ᵗʰ    |      4ᵗʰ     |     348ᵗʰ    |     7ᵗʰ    | 126,554  |    969    |    75     |
|17      |Medium 🔗 - The Docker Rodeo           | 499    |     106ᵗʰ    |      4ᵗʰ     |     346ᵗʰ    |     7ᵗʰ    | 126,546  |    968    |    75     |
|17      |Easy 🔗 - Linux Logging for SOC        | 499    |     106ᵗʰ    |      4ᵗʰ     |     345ᵗʰ    |     7ᵗʰ    | 126,538  |    967    |    74     |
|16      |Hard 🚩 - TryHack3M: TriCipher Summit  | 498    |     107ᵗʰ    |      4ᵗʰ     |     364ᵗʰ    |     7ᵗʰ    | 126,420  |    966    |    74     |
|16      |Easy 🔗 - Chaining Vulnerabilities     | 498    |     108ᵗʰ    |      5ᵗʰ     |     365ᵗʰ    |     7ᵗʰ    | 126,420  |    965    |    74     |
|15      |Medium 🔗 - AppSec IR                  | 497    |     108ᵗʰ    |      5ᵗʰ     |     352ⁿᵈ    |     7ᵗʰ    | 126,404  |    964    |    74     |
|14      |Hard 🚩 - Misguided Ghosts, in progress| 496    |     108ᵗʰ    |      5ᵗʰ     |     389ᵗʰ    |     6ᵗʰ    | 126,300  |    963    |    74     |
|14      |Hard 🚩 - VulnNet: Endgame             | 496    |     108ᵗʰ    |      5ᵗʰ     |     394ᵗʰ    |     6ᵗʰ    | 126,270  |    963    |    74     |
|13      |Hard 🚩 - Royal Router                 | 495    |     107ᵗʰ    |      5ᵗʰ     |     388ᵗʰ    |     6ᵗʰ    | 126,160  |    962    |    74     |
|13      |Medium 🚩 - Void Execution             | 495    |     107ᵗʰ    |      5ᵗʰ     |     383ʳᵈ    |     6ᵗʰ    | 126,120  |    961    |    73     |
|12      |Easy 🚩 - Invite Only                  | 494    |     110ᵗʰ    |      5ᵗʰ     |     352ⁿᵈ    |     6ᵗʰ    | 126,056  |    960    |    73     |
|12      |Medium 🚩 - Devie                      | 494    |     110ᵗʰ    |      5ᵗʰ     |     607ᵗʰ    |     9ᵗʰ    | 125,606  |    959    |    73     |
|11      |Medium 🚩 - Backtrack, in progress     | 493    |     110ᵗʰ    |      5ᵗʰ     |     629ᵗʰ    |     9ᵗʰ    | 125,516  |    958    |    73     |
|11      |Easy 🔗 - Detecting Web Attacks        | 493    |     110ᵗʰ    |      5ᵗʰ     |     629ᵗʰ    |     9ᵗʰ    | 125,516  |    958    |    73     |
|10      |Easy 🔗 - Attacking ICS Plant #1       | 492    |     110ᵗʰ    |      5ᵗʰ     |     675ᵗʰ    |     9ᵗʰ    | 125,428  |    957    |    73     |
|10      |Easy 🔗 - SOC Role in Blue Team        | 492    |     110ᵗʰ    |      5ᵗʰ     |     664ᵗʰ    |     9ᵗʰ    | 125,292  |    956    |    73     |
|9       |Hard 🚩 - Python Playground            | 491    |     111ˢᵗ    |      5ᵗʰ     |     693ʳᵈ    |     9ᵗʰ    | 125,236  |    955    |    73     |
|9       |Hard 🚩 - Borderlands                  | 491    |     111ˢᵗ    |      5ᵗʰ     |     713ʳᵈ    |    10ᵗʰ    | 125,146  |    954    |    73     |
|9       |Medium 🚩 - Forgotten Implant          | 491    |     112ⁿᵈ    |      5ᵗʰ     |     660ᵗʰ    |    10ᵗʰ    | 125,016  |    953    |    73     |
|8       |Easy 🔗 - Web Enumeration              | 490    |     112ⁿᵈ    |      5ᵗʰ     |     663ʳᵈ    |    10ᵗʰ    | 124,986  |    952    |    73     |
|8       |Easy 🔗 - iOS: Forensics               | 490    |     113ʳᵈ    |      5ᵗʰ     |     548ᵗʰ    |     9ᵗʰ    | 124,850  |    951    |    73     |
|7       |Medium 🚩 - VulnNet: Active            | 489    |     114ᵗʰ    |      5ᵗʰ     |     542ⁿᵈ    |     9ᵗʰ    | 124,746  |    950    |    73     |
|7       |Medium 🚩 - pyLon                      | 489    |     114ᵗʰ    |      5ᵗʰ     |     535ᵗʰ    |     9ᵗʰ    | 124,716  |    949    |    73     |
|7       |Medium 🚩 - Pressed                    | 489    |     113ʳᵈ    |      5ᵗʰ     |     508ᵗʰ    |     9ᵗʰ    | 124,886  |    948    |    73     |
|6       |Easy 🚩 - Classic Passwd               | 488    |     114ᵗʰ    |      5ᵗʰ     |     683ʳᵈ    |    12ⁿᵈ    | 124,476  |    947    |    73     |
|6       |Medium 🚩 - toc2                       | 488    |     114ᵗʰ    |      5ᵗʰ     |     695ᵗʰ    |    12ⁿᵈ    | 124,446  |    946    |    73     |
|6       |Hard 🚩 - Extract                      | 488    |     114ᵗʰ    |      5ᵗʰ     |     716ᵗʰ    |    13ʳᵈ    | 124,386  |    945    |    73     |
|6       |Medium 🚩 - Plotted-EMR                | 488    |     114ᵗʰ    |      5ᵗʰ     |     844ᵗʰ    |    12ⁿᵈ    | 124,326  |    944    |    73     |
|5       |Medium 🚩 - Inferno                    | 487    |     114ᵗʰ    |      5ᵗʰ     |     758ᵗʰ    |    12ⁿᵈ    | 124,236  |    943    |    73     |
|5       |Easy 🔗 - Psycho Break                 | 487    |     115ᵗʰ    |      5ᵗʰ     |     724ᵗʰ    |    10ᵗʰ    | 124,152  |    942    |    73     |
|4       |Medium 🚩 - Cold VVars                 | 486    |     113ʳᵈ    |      5ᵗʰ     |     579ᵗʰ    |    10ᵗʰ    | 124,048  |    941    |    73     |
|4       |Medium 🔗 - IP and Domain Threat Intel | 486    |     113ʳᵈ    |	     5ᵗʰ    |     579ᵗʰ     |    10ᵗʰ    | 124,018  |   940     |    73     |
|3       |Easy 🔗 - Malware Classification       | 485    |     112ⁿᵈ    |      5ᵗʰ     |     714ᵗʰ    |    13ʳᵈ    | 123,882  |    939    |    73     |
|2       |Medium 🔗 - Session Forensics          | 484    |     111ˢᵗ    |      5ᵗʰ     |     706ᵗʰ    |    14ᵗʰ    | 123,786  |    938    |    73     |
|1       |Medium 🚩 - Voyage                     | 483    |     111ˢᵗ    |      5ᵗʰ     |     849ᵗʰ    |    15ᵗʰ    | 123,636  |    937    |    73     |

</h6></div><br>

<br>

<p align="center">Global All Time:   109ᵗʰ<br><img width="250px"  src="https://github.com/user-attachments/assets/185c7b5c-fb04-4114-b7a0-c96bc09ec01f"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/0852934a-3e45-4e05-82f2-a77bc7ee8dc5"><br><br>
                  Brazil All Time:     4ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/9d6b9c76-6497-491a-ba80-7b6d0991d652"><br>
                  Global monthly:    217ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/6381cf23-436c-4748-88ba-ddb9a9fbc74e"><br>
                  Brazil monthly:      5ᵗʰ<br><img width="1200px" src="image" src="https://github.com/user-attachments/assets/8e277129-34a7-4d99-b5d7-ef5174f0ecf9"><br>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
