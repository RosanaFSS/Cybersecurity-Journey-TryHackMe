<p align="center">May 2, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{361}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="300px" src="" alt="Your Image Badge"><br>
<img width="200px" src="https://github.com/user-attachments/assets/1acd3213-b0f0-4ec2-a142-8e36ab0df272"><br></p>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Phishing: HiddenEye}}$$</h1>
<p align="center">A simple guide on how to use a tool known as HiddenEye developed by ANONUD4Y. This tool helps you create a phishing page for different sites such as Gmail, Snapchat, Paypal and more. Including understanding the difference between legit and fake site.<br>
It is classified an easy-level walkthrough.<br>
You can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed.<br>
Can be accessed clicking  <a href="https://tryhackme.com/room/phishinghiddeneye">here</a>.</p>

<p align="center"> <img width="900px" src=""> </p>

<br>


<h2>Task 1 . Installation & Creating your first phishing page!</h2>
<p><code>Hidden Eye</code>  is a Modern Phishing Tool with Advanced Functionality And Multiple Tunneling Services {Android-Support-Available}. Supports over 34 pages to clone and phish. Also, supports key loggers.</p>

<p>Clone the following github page:<br><br>
Previous version link: <code>https://github.com/DarkSecDevelopers/HiddenEye.git</code> <br><br>
Updated link: <code>https://gitlab.com/an0nud4y/HiddenEye</code></p>


<p>Enjoy the room and use it for educational/testing purposes ONLY.</p>

<p>Questions? Twitter: i7m4d</p>

<p>Special Thanks to MuirlandOracle for helping me polish this amazing room !<br><br>

Check out his blog at https://muirlandoracle.co.uk/ </p>


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 1.1. <em>cd to your preferred location </em><br><a id='1.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>

> 1.2. <em>git clone https://github.com/DarkSecDevelopers/HiddenEye.git </em><br><a id='1.2'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>

<p>Navigated to the <code>updated link</code> provided in the walkthrough: <code>https://gitlab.com/an0nud4y/HiddenEye</code>.</p>

<br>

![image](https://github.com/user-attachments/assets/2cd3120e-5755-4f2b-a631-90877ddb8b75)

<br>

<p>Cloned it.</p>

<br>

![image](https://github.com/user-attachments/assets/f685729c-8528-40e6-b52b-f8bf90f1bbcc)

<br>

> 1.3. <em>cd HiddenEye</em><br><a id='1.3'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/286ec6ac-c530-43e1-8aaa-96cfe27e9bd3)

<br>

> 1.4. <em>sudo chmod +x HiddenEye.py</em>Hint : <em>Run it with root permissions.</em><br><a id='1.4'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/c8698023-754b-42f0-9987-dede15d60720)


<br>

<br>

> 1.5. <em>sudo pip3 install -r requirements.txt </em>Hint : <em>If it did not work, type "sudo apt install python3-pip" Then install the requirements again.</em><br><a id='1.5'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/e5114e00-9a92-4146-aa68-fcd42171a889)

<br>




<h2>Task 2 . Deploy!</h2>

<p>Deploy the instance attached to this task by left-clicking the green "Deploy" button on the top-right of this task!<br><br>

 

You are not expected to interact with the instance just yet - you will be provided credentials later on throughout the room. But please ensure you are connected to the TryHackMe OpenVPN before proceeding.</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 2.1. <em>I've deployed my instance and ensured I am connected to the THM VPN!</em><br><a id='2.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>

<h2>Task 3 . Checksums 101</h2>
<h3>What are checksums?</h3>
<p>Checksums are a prominent attribute within the malware analysis community. But moreover, the wider Information Technology (IT) industry. Put simply, these checksums are the result of mathematical operations against an input - where the output is a sequence of characters.<br><br>

Ultimately, the markup of data on a computer system is binary, merely ones and zeros where each value is a "bit". A cryptographic checksum uses these "bits" as the input for these mathematical operations; the increased complexity of the mathematical operations applied, the more secure a checksum is considered. These checksums are also commonly referred to as "hashes".<br><br>

Because of how cryptographic algorithms work, regardless of the size of the input - such as a file - the length of the output will remain the same. For example, take an algorithm and apply these mathematical operations against two files listed below:</p>

![image](https://github.com/user-attachments/assets/e968c0a8-0789-4868-8d32-c80709fe2a95)

<p>Although the file size is vastly different, the length of the output calculated will be the same, albeit its contents different. For example, in this algorithm I have as an example, the output length is 12 characters:</p>

![image](https://github.com/user-attachments/assets/1e4b7b64-c151-4c4b-a688-f726a7406580)

<p>Whilst the values calculated from the algorithm are different from each file, they remain the same length - irrespective of the file size. Because the two files have different contents, in this case, each output is unique for the file.<br><br>

The increased complexity of the mathematical operations vastly reduces the chances of two files with different contents from having the same output. If this was to occur, it is known as a "hash collision". Explaining the math behind how this happens is out of scope, however, it is extremely rare. To put into perspective, the hashing algorithm MD5 which is a famous recent example will need 6 billion files to be hashed per second - for 100 years on average. (Kornel., 2008) </p>


<h6>Whilst it's pretty safe to say that the probability of a hash collision occurring is pretty low, it is mathematically possible. For example, researchers (Stevens et al., 2017) report on Shattered.io, where they were able to demonstrate a SHA1 hash collision in practice. I greatly encourage taking the time to read through the report to understand how these collisions can be made into proof of concepts but to also appreciate why discoveries like this are important in the world of information security.</h6>

<p>It's safe to say it's pretty rare for this error to happen, although it is mathematically possible. We'll visualise this below.</p>

<h3>Checksums Continued:</h3>
<p>Let's contextualise checksums a bit more. In IT, checksums are used for verifying the integrity of data. Have you ever copied a file onto a USB drive where Windows complains that the file is now corrupt? That is data corruption; binary data was lost somewhere during the transfer process, either due to software or hardware error.<br><br>

Due to how these cryptographic algorithms work, namely, they produce a result after processing a piece of data at every single bit, checksums are fantastic for verifying if data has completely copied to a new location. Humans can't compare the binary data (which could be millions of values to compare) of two files to ensure they are correct. They can, however, compare two-fixed length values - such as the 12 character length output of the algorithm specified above. In the real-world, some popular algorithms are SHA1, SHA-256 and in some cases, SHA-512, where the output length of each algorithm is varied based on its security.<br><br>

We'll visualise how hashing algorithms work below:</p>

![image](https://github.com/user-attachments/assets/6ca47048-e57b-4344-a2ef-65b7d1942de8)

<p>See here how the contents of the first two files are the same with "TryHackMe". When using the same algorithm, the generated checksum is the same. This is because the binary data of these two files are identical, so the same algorithm will output the same result. This is not a hash collision.<br><br>

Notice the third file with the same contents of "TryHackMe" resulting in the same binary data has a different checksum. This is because the algorithm, in this case, SHA256 instead of the previous MD5, uses different mathematical operations. The mathematics behind this algorithm is complex in comparison to MD5, so the length of the output string is longer.<br><br>

Finally, notice in the screenshot below (the last file in the screenshot above, just cropped below for clarity) that the contents of the file are now "TryHackeM" and not "TryHackMe":

</p>


![image](https://github.com/user-attachments/assets/58944d77-d3d1-4fd7-9ff3-1e0a4ac0eab8)


<p>Whilst the same algorithm used on the first two files are also used on this file (MD5) because the contents are now different - albeit very similar - the output is now different in comparison.</p>

<h3>Visualizsing a Hash Collision</h3>
<p>Okay, bear with me here. It's been pretty theory-heavy I understand...We're almost there I promise! The example screenshots below outline how the various outputs will differ based upon either the algorithm used or the contents of the file. Here we will go through an example of a hash collision:</p>

![image](https://github.com/user-attachments/assets/58bbfec2-28b0-46bb-bcd8-0fdca3ad289f)

<p>The contents of the two files above are very different. In the real world, the differences could be simply adding or removing a character, but I have made dramatised this example to visualise things better.<br><br>

A hash collision is when two files with different content (such as the two above) have the same output. From a mathematics perspective, these files are identical. However, we know by the contents that they are not at all.</p>


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 3.1. <em>Name the term for an individual piece of binary</em><br><a id='3.1'></a>
>> <strong><code>Bit</code></strong><br>
<p></p>

<br>

> 3.2. <em>What are checksums also known as?</em><br><a id='3.2'></a>
>> <strong><code>Hashes</code></strong><br>
<p></p>

<br>

> 3.3. <em>Name the algorithm that is next in the series after SHA-256</em><br><a id='3.3'></a>
>> <strong><code>SHA-512</code></strong><br>
<p></p>

<br>

> 3.4. <em>According to this task, how long will you need to hash 6 million files before a MD5 hash collision occurs?</em><br><a id='3.4'></a>
>> <strong><code>100 Years</code></strong><br>
<p></p>

<br>

> 3.5. <em>Who developed the MD5 algorithm?</em><br><a id='3.5'></a>
>> <strong><code>Ronald Rivest</code></strong><br>
<p></p>

<br>
<br>


<h2>Task 4 . Online Sandboxingy</h2>
<h3>What is Online Sandboxing</h3>
<p>Sometimes things are left best to the experts. That's especially true in the case of malware analysis. However, online sandboxing hosts use to a wider audience than just hobbyists.<br><br>

In the context of information security, sandboxing is the technique used to isolate processes to prevent direct interaction with one another. There are many examples of this. For example, using Virtualbox as a Hypervisor to run the Kali Linux operating system virtually, in parallel on your main computer. The processes within Kali Linux interact only through the means of Virtualbox and has no interference with processes on your main operating system, such as Windows.<br><br>

In a malware analysis context, analysts employ virtual environments - such as those on TryHackMe, to facilitate analysis of potentially malicious code more securely.<br><br>

Now, with this being said, malware has been known and can very well escape this virtual environment onto the analyst's host system. Whilst this risk is somewhat limited to sophisticated malware, it's very achievable. For example, CVE-2018-2689 is a CVE for Virtualbox where malware was capable of escaping this restricted virtual environment. CVE's such as these are extremely valuable and seldom disclosed due to the actors who discover them and their intentions, namely malicious malware authors.<br><br>

I've written more about how malware detects it is in a virtual environment and the possible routes it can take to escape on my blog. What should be taken away from this task is that a virtual environment alone does not protect you from malware. Simply, virtual environments merely provide a convenient platform to analyse code.<br><br>

Simply, an online sandbox is this virtual environment - but placed online by services such as:</p>

<p>- any.run<br>
- hybrid-analysis</p>

<p>These services are fantastic, as it allows hobbyists to begin understanding how malware behaves with no detriment or risk to themselves. Moreover, online sandboxing platforms are highly sophisticated and are likely to report behaviours that an analyst may have missed.<br><br>

 

With this said, automated analysis cannot replace the skill and depth that an analyst can exhibit and traverse too. For example, reverse engineering. These platforms are only capable of executing malware and generating reports based upon interactions made with the operating system, any communication attempts and any signatures left behind. For example:</p>

<p>- Contacting a domain name (DNS Lookups, etc)<br>
- Creating registry keys<br>
- Read/Writing files<br>
- Creating system processes<br>
- Maintaining persistent through system startup entries</p>

<p>All of which are all discoverable by an analyst after some time. Therefore, online sandboxes are useful for a precursory inspection of a file.</p>

<h3>Interacting with an online sandboxing Service:</h3>
<p>In the example screenshots below, this sample was run through the hybrid-analysis service. The sample took a total of 10 minutes and was free of charge. The report detailed an extensive number of behaviours such as networking traffic and the execution chain, this would have taken an analyst a considerable amount of time to of detailed themselves.</p>

![image](https://github.com/user-attachments/assets/bc31707a-8403-4416-bfa5-9896bbd83eec)


<p>Note how the file is still identified only by its "Checksums":</p>

![image](https://github.com/user-attachments/assets/32f439cd-b4a8-4a18-8328-946112166c3a)

<p>If an analyst was to now search google with any of these checksums, the report generated by this sandboxing engine will now be provided as a listing for future analysts.<br><br>

Proceeding to read through the report, interesting behaviours are summarised such as those below:</p>

![image](https://github.com/user-attachments/assets/ee838f2a-e978-439d-a2da-3c20ea1e2358)

<br>

![image](https://github.com/user-attachments/assets/4153462f-13d6-4c75-9672-b9148b5ba35f)

<p>To answer the following questions, read through this analysed sample to solve the following questions:</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 4.1. <em>Name the key term for the type of malware that Emotet is classified as</em>Hint : <em>Look at the room's thumbnail for a hint!</em><br><a id='4.1'></a>
>> <strong><code>Trojan</code></strong><br>
<p></p>

<br>

<p>Accessed https://assets.tryhackme.com/additional/cmn-malware/int-mal-sample.pdf (provided in the walkthrough).</p>

![image](https://github.com/user-attachments/assets/d44ae270-31d8-4cd2-8300-ef265a2e1e4e)



> 4.2. <em>Research time! What type of emails does Emotet use as its payload?</em><br><a id='4.2'></a>
>> <strong><code>spam emails</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/3cf180f9-5963-4ee2-a14f-462f97aaf8af)

<br>


> 4.3. <em>Begin analysing the report, what is the timestamp of when the analysis was made?</em>Hint : <em>Copy and paste exactly how it is listed on the report</em><br><a id='4.3'></a>
>> <strong><code>9/16/2019, 13:54:48</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/2ef26bd0-3cb1-4eb7-9693-da741ddd24ed)

<br>


> 4.4. <em>Name the file that is detected as a "Network Trojan"</em><br><a id='4.4'></a>
>> <strong><code>easywindow.exe </code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/4ac31303-da3d-4aeb-9d02-7ebed1a305a1)

<br>


> 4.5. <em>What is the PID of the first HTTP GET request?</em><br><a id='4.5'></a>
>> <strong><code>2748</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/3053ed82-3d4f-4dfa-aa86-2da9cc0bd79a)

<br>


> 4.6. <em>What is the only DNS request that is made after the sample is executed?</em><br><a id='4.6'></a>
>> <strong><code>blockchainjoblist.com </code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/4a035670-a4f9-43ac-b9ea-c8031e3e4dac)

<br>
<br>


<h2>Task 5 . Practical: Calculating & Reporting Checksums</h2>
<h3>Calculating the MD5 Checkesums of provided of provided material</h3>
<p>You will be able to interact with your instance using the in-browser functionality, however, you may connect via RDP using the details below - ensuring you are connected to the TryHackMe VPN beforehand. </p>
<p>IP Address: XX.XX.XXX.XXX<br>

Username: XXXXXXXXXXXXX<br>

Password: XXXXXXXXXXXXX</p>

<p>I have provided the tools and materials on this Instance for you to complete the questions. I will go through obtaining the MD5 Checksum of a file using two methods - you will apply these techniques to answer the questions for this task.<br><br>

The required material is located on the "Administrator" user's Desktop.</p>

<h3>Using the 3rd-party application "HashTab"</h3>
<p>1. 1. Right-click the file you wish to retrieve the checksum of. I will be using "ComplexCalculatorv2" in this example.<br>

2. Left-click the "Properties" title in the drop-down.<br>

![image](https://github.com/user-attachments/assets/8e3f1b4a-b7c5-454e-8997-dbcb40589a51)


3. In the popup, navigate to the "File Hashes" tab, where you will see a screenshot akin to the one below. Note that this tab is not present on a default Windows installation:<br>


![image](https://github.com/user-attachments/assets/eef9e347-f125-495a-8387-7d0f7a9e1f55)

You can now answer question 1.</p>

<h3>Uzing Windows' PowerShell"</h3>

<p>1. Firstly we will need to open up "Powershell". You can do this by opening the Windows Search bar.<br>

![image](https://github.com/user-attachments/assets/4bfe092c-46db-46f0-a589-dc2069c1e2b0)

2. Next, change the directory of the users Desktop by using cd Desktop <br>

3. Verify you are in the right directory by using dir to list the files in the directory. You should see the three below:<br>

![image](https://github.com/user-attachments/assets/9ca073ae-d2a0-4892-be35-20b25f18a414)

<p>Powershell has both CertUtil and File-Hash commands that allow us to retrieve various checksums of files, including MD5, SHA1, SHA2, and SHA-256. I will detail the syntax for both below, calculating the MD5 checksum of a file.</p>

<h3>Using CertUtil</h3>
<p><code>CertUtil -hashfile ComplexCalculatorv2.exe MD5|SHA256|SHA512</code> or "CertUtil -hashfile <filename> <algorithm>" such as in the example below:</p>

![image](https://github.com/user-attachments/assets/ba37cd14-c07a-4387-92e2-3b8483c0eac4)

<h3>Using FileHash</h3>
<p><code>Get-FileHash file_name -Algorithm MD5|SHA256|SHA512</code></p>

![image](https://github.com/user-attachments/assets/89da5c39-534b-4132-88c8-82c335946357)

<p>Now you can proceed to answer the remaining questions!</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 5.1. <em>Using the HashTab tool, what is the MD5 checksum for "LoginForm.exe"?</em>Hint : <em>You can copy and paste over RDP!</em><br><a id='5.1'></a>
>> <strong><code>FF395A6D528DC5724BCDE9C844A0EE89</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/8442e159-1ac8-47bf-9b69-44c3af15db27)


<br>


![image](https://github.com/user-attachments/assets/4def5583-c4c4-4ab7-9946-7eb134d9d4ae)


<br>


> 5.2. <em>Using Get-FileHash in Powershell, retrieve the SHA256 of "TryHackMe.exe"</em><br><a id='5.2'></a>
>> <strong><code>6F870C80361062E8631282D31A16872835F7962222457730BC55676A61AD1EE0</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/a9276e3a-085f-4bec-95a7-a1509ba09974)

<br>

![image](https://github.com/user-attachments/assets/d4e0a57d-93ec-462e-98ed-becc02400c4e)

<br>

> 5.3. <em>What would be the syntax to retrieve the SHA256 checksum of "TryHackMe.exe" using CertUtil in Powershell?</em><br><a id='5.3'></a>
>> <strong><code>CertUtil -hashfile TryHackMe.exe SHA256</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/54d8e67a-445a-4d88-86af-0b0bac1c63d3)

<br>
<br>

<h2>Task 6 . VirusTotal</h2>
<p>Another online service that utilises these checksums is Virustotal. Virustotal acts as an indexer and aggregator for various Anti Virus (AV) engines. When a checksum is submitted to Virsutotal, fellow malware analysts can view the AV reports attributed to that file. 

![image](https://github.com/user-attachments/assets/317754d1-e857-4d00-8a98-accd57868c5c)

<p>Much like a search engine, you can search for reports by a few characteristics, for example:<br>

- The IP Addresses that samples communicate with<br>
- Checksums<br>
- The file itself<br><br>
 

In the screenshot below, I have uploaded the "TryHackMe.exe" executable to Virustotal. If you were to browse to VirusTotal, you would be able to discover this report by entering the files' checksum. I have provided the report for you here.</p>

![image](https://github.com/user-attachments/assets/2f1928db-64b5-4e6c-b386-3194c32dbb6e)

<p>
A THM Contributor, Darkstar7471 has a fantastic room on using both Volatility, a memory analysis framework and Virustotal. I highly recommend checking it out as you extract files and interact with VirusTotal to determine their maliciousness from the aggregated AV ratings.<br><br>

Read the report provided (here) to answer the questions provided.</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 6.1. <em>Navigate to the "Details" tab, what is the other filename and extension reported as present?</em><br><a id='6.1'></a>
>> <strong><code>HxD.exe</code></strong><br>
<p></p>

<br>

<p>Navigated to <code>VirusTotal</code> using the link provided in the walkthrough: https://www.virustotal.com/gui/file/6f870c80361062e8631282d31a16872835f7962222457730bc55676a61ad1ee0/details.</p>

<br>

![image](https://github.com/user-attachments/assets/9eae83eb-df4c-4957-9e19-a7b5b83328d8)

<br>

![image](https://github.com/user-attachments/assets/207520c4-8731-4e94-bfbf-baa4bac0dfd3)


<br>


> 6.2. <em>In the same "Details" tab, what is the reported compilation timestamp?</em><br><a id='6.2'></a>
>> <strong><code>2020-02-28 11:16:36 UTC</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/5962cc3f-3136-4153-89e9-3fd1d6ac89fb)


<br>

> 6.3. <em>What is the THM{} formatted flag on the report?</em>Hint : <em>Look through the tabs!</em><br><a id='6.3'></a>
>> <strong><code>HM{TryHackMe_Malware_Series_Research_Flag}</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/f8cb210b-1641-446c-9720-d2450d4000cb)


<br>
<br>

<h2>Task 7 . Future Reading (References)</h2>

<h3>Cryptography and Cheskcums</h3>
<p align="left">- <a href="https://scholarworks.sjsu.edu/cgi/viewcontent.cgi?referer=https://www.google.com/&httpsredir=1&article=1020&context=etd_projects">A Meaningful MD5 Hash Collision Attack</a> - (Narayana D. Kashyap., 2008)</p>
<p align="left">- <a href="https://dl.acm.org/doi/book/10.5555/1209579">Cryptography & Network Security</a> - Cryptography & Network Security</p>
<p align="left">- <a href="https://shattered.io/static/shattered.pdf">The first collision for full SHA-1</a> - - (Stevens et al., 2017) / (Shattered.io)</p>

<h3>Blog (Selfless Promo)</h3>
<p align="left">- <a href="https://blog.cmnatic.co.uk/posts/so-you-want-to-analyse-malware/">So you want to analyse malware?</a></p>


<h3>Sandboxes Engine</h3>
<p align="left">- <a href="https://any.run/">any.run</a></p>
<p align="left">- <a href="https://hybrid-analysis.com/">hubrid.analysis</a></p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 7.1. <em>Thanks! I'll stay tuned for more.</em><br><a id='7.1'></a>
>> <code><strong>NO answer needed</strong></code>


<br>
<br>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Room Completed}}$$</h1>
<br>
<p align="center">
<img width="1000px" src="https://github.com/user-attachments/assets/83784394-9ede-440b-a383-7b407b843dcd"><br>
<img width="1000px" src="https://github.com/user-attachments/assets/e2895dc1-33bb-4718-a263-de2aa88dc9ed"></p>

<br>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{My TryHackMe Journey}}$$ </h1>
<br>


<div align="center">

|       Date        |   Streak |   All Time   |   All Time   |   Monthly   |   Monthly  |  Points  |   Rooms   |   Badges  |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
|    May 2, 2025    |    361   |     241ˢᵗ    |      6ᵗʰ     |     603ʳᵈ   |     7ᵗʰ    |  99,151  |    701    |     60    |

</div>

<br>

<p align="center"> Global All Time: 241ˢᵗ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/8c9ab271-5562-4a82-9725-625be132d71f"> </p>

<p align="center"> Brazil All Time:   6ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/835516a0-6720-4ee8-a236-628db691bfdf"> </p>

<p align="center"> Global monthly:  603ʳᵈ<br><br><img width="900px" src="https://github.com/user-attachments/assets/bcc7f5ca-b428-4a92-a2ac-23cdb4244248"> </p>

<p align="center"> Brazil monthly:    7ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/fa66de90-f182-4a49-b4c1-8929c2efb22d"> </p>


<br>
<br>

<p align="center"> Weekly League:    12ⁿᵈ Platinum<br><br><img width="1000px" src="https://github.com/user-attachments/assets/98e9c8eb-cf59-4292-bb23-2dfed2e6535c"> </p>

<br>
<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thanks for coming!!!}}$$</h1>

<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 

<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thank you}}$$</h1>
<p align="center"><a href="https://tryhackme.com/p/cmnatic">cmnatic</a> for investing your time and effort to develop this walkthrough so that I could sharpen my skills!</p>
