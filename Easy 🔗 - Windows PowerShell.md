<h3> Welcome to the <em>TryHackMe ...</em></h3>
<h1>Cyber Security 101 learning path > Command Line ></h1>
<h2>Windows PowerShell</h2>
<p>Discover the "Power" in PowerShell and learn the basics.</p>
<p>October 24, 2024<br></p>

<img src="https://github.com/user-attachments/assets/bea96084-67d8-454f-8378-0817d5a7e37b" height="200" width="200">

![image](https://github.com/user-attachments/assets/94f6424d-1119-4ff8-a570-6c03fc45b01e)



<p>Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure. It´s key part of my 171-day-streak. Let´s get started!!<br><br>
Access this TryHackMe Room clicking <a href="https://tryhackme.com/r/room/windowspowershell">Windows PowerShell</a></p>

<h2>Task 1 - Introduction</h2>

> 1.1 - <em>Raise the anchor, hoist the sails—it's time to set sail!</em><br>
>> <strong>No answer needed</strong><br>
<p><br></p>

<h2>Task 2 - What is PowerShell</h2>

> 2.1 - <em>What do we call the advanced approach used to develop PowerShell?</em><br>
>> <strong>object-oriented</strong><br>
<p><br></p>

<h2>Task 3 - PowerShell Basics</h2>

![image](https://github.com/user-attachments/assets/7b55a162-5305-404d-9361-ffbc3fa416f2)

![image](https://github.com/user-attachments/assets/bce37bdd-8171-4820-91c3-badc23bd709d)

![image](https://github.com/user-attachments/assets/0b7988f1-3a33-4a62-8c88-b6c015bdb416)

> 3.1 - <em>How would you retrieve a list of commands that start with the verb Remove? [for the sake of this question, avoid the use of quotes (" or ') in your answer]</em><br>
>> <strong>Get-Command -Name Remove*</strong><br>
<p><br></p>

> 3.2 - <em>What cmdlet has its traditional counterpart echo as an alias?</em><br>
>> <strong>Write-Output</strong><br>
<p><br></p>

> 3.3 - <em>What is the command to retrieve some example usage for the cmdlet New-LocalUser?</em><br>
>> <strong>Get-Help New-LocalUser -examples</strong><br>
<p><br></p>

<h2>Task 4 - Navigating the File System and Working with Files</h2>

> 4.1 - <em>What cmdlet can you use instead of the traditional Windows command type?</em><br>
>> <strong>Get-Content</strong><br>
<p><br></p>

> 4.2 - <em>What PowerShell command would you use to display the content of the "C:\Users" directory? [for the sake of this question, avoid the use of quotes (" or ') in your answer]</em><br>
>> <strong> Get-ChildItem -Path C:\Users</strong><br>
<p><br></p>

> 4.3 - <em>How many items are displayed by the command described in the previous question?</em><br>
>> <strong>4</strong><br>
<p><br></p>

![image](https://github.com/user-attachments/assets/1a575685-1563-46a3-9000-72294ffc10cc)

<h2>Task 5 - Piping, Filtering, and Sorting Data</h2>

> 5.1 - <em>How would you retrieve the items in the current directory with size greater than 100? [for the sake of this question, avoid the use of quotes (" or ') in your answer]</em><br>
>> <strong>Get-ChildItem | Where-Object -Property Length -gt 100</strong><br>
<p><br></p>


<h2>Task 6 - System and Network Information</h2>

> 6.1 - <em>Other than your current user and the default "Administrator" account, what other user is enabled on the target machine?</em><br>
>> <strong>p1r4t3</strong><br>
<p><br></p>

![image](https://github.com/user-attachments/assets/2f63e825-7688-4729-bc4f-7b00955aef63)

> 6.2 - <em>This lad has hidden his account among the others with no regard for our beloved captain! What is the motto he has so bluntly put as his account's description?</em><br>
>> <strong>A merry life and a short one.</strong><br>
<p><br></p>

> 6.3 - <em>Now a small challenge to put it all together. This shady lad that we just found hidden among the local users has his own home folder in the "C:\Users" directory.
Can you navigate the filesystem and find the hidden treasure inside this pirate's home??</em><br>
>> <strong>THM{p34rlInAsh3ll}</strong><br>
<p><br></p>

![image](https://github.com/user-attachments/assets/a0f5c439-6cb0-47fc-9a82-5baa6617ecff)

<h2>Task 7 - Real-Time System Analysis</h2>

> 7.1 - <em>In the previous task, you found a marvellous treasure carefully hidden in the target machine. What is the hash of the file that contains it?</em><br>
>> <strong>71FC5EC11C2497A32F8F08E61399687D90ABE6E204D2964DF589543A613F3E08 </strong><br>
<p><br></p>

![image](https://github.com/user-attachments/assets/a1d684f0-2b8c-4a1b-8460-fadbc23f2669)

> 7.2 - <em>What property retrieved by default by Get-NetTCPConnection contains information about the process that has started the connection?</em><br>
>> <strong>OwningProcess</strong><br>
<p><br></p>

![image](https://github.com/user-attachments/assets/b819866c-9d22-4740-b4f7-be04960ebd54)

> 7.3 - <em>It's time for another small challenge. Some vital service has been installed on this pirate ship to guarantee that the captain can always navigate safely. But something isn't working as expected, and the captain wonders why. Investigating, they find out the truth, at last: the service has been tampered with! The shady lad from before has modified the service DisplayName to reflect his very own motto, the same that he put in his user description.<br><br>

With this information and the PowerShell knowledge you have built so far, can you find the service name?</em><br>
>> <strong>p1r4t3-s-compass</strong><br>
<p><br></p>

<h2>Task 8 - Scripting</h2>

> 8.1 - <em>What is the syntax to execute the command Get-Service on a remote computer named "RoyalFortune"? Assume you don't need to provide credentials to establish the connection. [for the sake of this question, avoid the use of quotes (" or ') in your answer]</em><br>
>> <strong>Invoke-Command -ComputerName RoyalFortune -ScriptBlock { Get-Service }</strong><br>
<p><br></p>

<h2>Task 9 - COnclusion</h2>

> 8.1 - <em>I'm ready to go on to the next adventure!</em><br>
>> <strong>No answer needed</strong><br>
<p><br></p>


<h2>Room completed</h2>

![image](https://github.com/user-attachments/assets/bc4697dc-8a46-4517-8421-de6ef980d0e8)
