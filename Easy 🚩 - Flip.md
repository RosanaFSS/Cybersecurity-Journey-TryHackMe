<p align="center">April 12, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{341}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="300px" src="https://github.com/user-attachments/assets/51fb15ac-ba56-46aa-8864-66875356af39" alt="Your Image Badge"><br>
<img width="200px" src="https://github.com/user-attachments/assets/d8306acc-b031-4901-a1b9-9b3187902b21"></p>
<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Flip}}$$</h1>
<p align="center">"Hey, do a flip!"<br>
It is classified as an easy-level CTF.<br>
You can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed.<br>
Can be accessed clicking  <a href="https://tryhackme.com/room/flip">here</a>.</p>

<p align="center"> <img width="900px" src="https://github.com/user-attachments/assets/74f8a151-432f-45dd-abd1-ced2573d814b"> </p>

<br>
<br>

<h2>Task 1 . Source Code </h2>

<p>First, go ahead and review the source code before moving on to Task 2.<br>

You can review the source code by clicking on the Download Task Files button at the top of this task to download the required file.</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 1.1. <em>Download the source code.</em><br><a id='1.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br><br>

<h2>Task 2 . What is the flag?</h2>

<p>Log in as the admin and capture the flag!<br>

If you can...<br>

Whenever you are ready, click on the Start Machine button to fire up the Virtual Machine. Please allow 3-5 minutes for the VM to fully start.<br>

The server is listening on port 1337 via TCP. You can connect to it using Netcat or any other tool you prefer.</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 2.1. <em>What is the flag?</em><br><a id='2.1'></a>
>> <strong><code>THM{FliP_DaT_B1t_oR_G3t_Fl1pP3d}</code></strong><br>
<p></p>

<br><br>


<p>Discovered in the script the information below.<br><br>
<code>admin&password=sUp3rPaSs1</code></p>


<p>Ran <code>nc TargetIP</code> using usernamed as <code>admin</code> and the password just discovered.<br>
Did not work.  :-(</p>

<br>

![image](https://github.com/user-attachments/assets/1fe7fd16-c996-4594-98ef-ee3f928138a8)

<br>

<p></p>

<p>Ran <code>nc TargetIP</code> using username as <code>bdmin</code> and the same password as before.<br>
Got a <code>Leaked ciphertext</code>, the one below.<br><br>
8bb00996f6a7705fbefb7a96fcd2532f02d7a95e7e18b6c3be7c79ed855e7f24ea0a857cf91c100e299f3c81b5c80ca1</p>


<p>Based on the analysis of the <code>Task File</code> provided, I learned that the ciphertext has 3 equal size parts:<br>
<code>8b</code>b00996f6a7705fbefb7a96fcd2532f<br>
<code>02</code>d7a95e7e18b6c3be7c79ed855e7f24<br>
ea0a857cf91c100e299f3c81b5c80ca1</p>
<br>

<p>Discovered also in the script<br><br>
<code> message = 'access_username=' + username +'&password=' + password</code><br><br>
-----><br>
<code>message = 'access_username=' + username +'&password=' + password<code><br><br>
-----><br>
<code>access_username=admin&password=sUp3rPaSs1</code><br><br>
----><br>
<code>access_username=<br>
admin&password=s<br>
Up3rPaSs1$$$$$$$</code></p>

<p>From the 1st of 3 parts -----> a = <code>8b</code><br>
From the 2nd of 3 parts -----> b = <code>02</code></p>


<p>1st part<br>
XOR<br>
2nd part decrypted AES<br>
XOR<br>
3rd part.</p>

<br>

<p>We need the value of 26 XOR decrypted (7x).</p>

<br>

<p>Navigated to https://xor.pw</p>

<br>

![image](https://github.com/user-attachments/assets/794c3d6d-c7b4-415c-91f9-df0bd975fe06)

<p>8b XOR 62 = e9</p>

<br>

![image](https://github.com/user-attachments/assets/7006f78f-71b7-4762-abc6-1c40ec24b3a2)


<p>e9 XOR 61 = 88  ==><br><br>
8bb00996f6a7705fbefb7a96fcd2532f02d7a95e7e18b6c3be7c79ed855e7f24ea0a857cf91c100e299f3c81b5c80ca1 ==>
88b00996f6a7705fbefb7a96fcd2532f02d7a95e7e18b6c3be7c79ed855e7f24ea0a857cf91c100e299f3c81b5c80ca1  
</p>


![image](https://github.com/user-attachments/assets/1b437de7-1260-4adb-8dcc-48089e62fba2)




<br>
<br>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Room Completed}}$$</h1>
<br>
<p align="center">
<img width="900px" src="https://github.com/user-attachments/assets/a2321577-5e64-4a11-9c4d-0d1af82b39b4"><br>
<img width="900px" src="https://github.com/user-attachments/assets/96ef066a-dc44-457d-8337-13bd0815715f"></p>

<br>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{My TryHackMe Journey}}$$ </h1>
<br>


<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |Global        | Brazil       | Global      | Brazil     |          | Completed |           |
| April 10, 2025    | 339      |     298ᵗʰ    |        8ᵗʰ   |    250ᵗʰ    |     2ⁿᵈ    |  92,222  |       652 |   59      |

</div>

<br>

<p align="center">League<br><br><img width="300px" src="https://github.com/user-attachments/assets/29b35e41-b041-4696-985d-7b4bd6fb88ff"> </p>


<br>

<p align="center"> Global All Time: 298ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/d52c4fd8-067f-449a-aa9a-d11f9f899241"> </p>

<p align="center"> Brazil All Time: 8ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/a8f0de66-46ad-4594-8ed0-ddda17bc1981"> </p>

<p align="center"> Global monthly: 250ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/30c2bf9f-7ce8-4ca3-95d9-c901bb0e86a9"> </p>

<p align="center"> Brazil monthly: 2ⁿᵈ<br><br><img width="900px" src="https://github.com/user-attachments/assets/057a1277-d151-457c-aa6e-f4b0ae5ac00e"> </p>


<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thanks for coming!!!}}$$</h1>

<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 

<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thank you}}$$</h1>
<p align="center"><a href="https://tryhackme.com/p/tryhackme">tryhackme</a> and  <a href="https://tryhackme.com/p/hadrian3689">hadrian3689</a> for investing your time and effort to develop this walkthrough so that I could sharpen my skills!</p> 
