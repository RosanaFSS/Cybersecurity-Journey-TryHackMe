<p align="center">April 12, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{341}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="300px" src="https://github.com/user-attachments/assets/670400e3-4ebe-4f41-a592-24eb5bab0810" alt="Your Image Badge"><br>
<img width="200px" src="https://github.com/user-attachments/assets/d8306acc-b031-4901-a1b9-9b3187902b21"></p>
<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Flip}}$$</h1>
<p align="center"><em>Hey, do a flip!</em> It is classified as an easy-level CTF.<br>
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
<code>message = 'access_username=' + username +'&password=' + password</code><br><br>
-----><br>
<code>message = 'access_username=' + username +'&password=' + password</code><br><br>
-----><br>
<code>access_username=admin&password=sUp3rPaSs1</code><br><br>
----><br>
<code>access_username=<br>
admin&password=s<br>
Up3rPaSs1$$$$$$$</code></p>

<p>
From the 1ˢᵗ of 3 parts -----> a = <code>8b</code>.<br>
From the 2ⁿᵈ of 3 parts -----> b = <code>02</code>.</p>


<p>[ 1ˢᵗ part ] XOR [ 2ⁿᵈ part decrypted ] XOR [ 3ʳᵈ part].</p>

<br>

<p>We need the value of  <code>8b</code> XOR decrypted <code>02</code>.</p>

<br>

<p>Navigated to https://xor.pw</p>

<br>

![image](https://github.com/user-attachments/assets/794c3d6d-c7b4-415c-91f9-df0bd975fe06)


<p><code>8b</code> XOR decrypted <code>62</code> = <code>e9</code><br>
<code>62</code> is the value of <code>b</code></p>

<br>

![image](https://github.com/user-attachments/assets/7006f78f-71b7-4762-abc6-1c40ec24b3a2)


<p><code>e9</code> XOR <code>61</code> = <code>88</code><br>
<code>61</code> is the value of <code>a</code><br><br>

The leaked cyphertext:<br>
<code>8b</code>b00996f6a7705fbefb7a96fcd2532f02d7a95e7e18b6c3be7c79ed855e7f24ea0a857cf91c100e299f3c81b5c80ca1
<br><br> transforms into<br><br>
<code>88</code>b00996f6a7705fbefb7a96fcd2532f02d7a95e7e18b6c3be7c79ed855e7f24ea0a857cf91c100e299f3c81b5c80ca1</p>

<br>


![image](https://github.com/user-attachments/assets/1b437de7-1260-4adb-8dcc-48089e62fba2)




<br>
<br>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Room Completed}}$$</h1>
<br>
<p align="center">
<img width="900px" src="https://github.com/user-attachments/assets/a2321577-5e64-4a11-9c4d-0d1af82b39b4"><br>
<img width="900px" src="https://github.com/user-attachments/assets/d3f18e8e-5a06-4711-95d8-6ea841289358"></p>


<br>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{My TryHackMe Journey}}$$ </h1>
<br>


<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |Global        | Brazil       | Global      | Brazil     |          | Completed |           |
| April 12, 2025    | 441      |     290ᵗʰ    |        8ᵗʰ   |    182ⁿᵈ    |     2ⁿᵈ    |  92,920  |       654 |   59      |

</div>

<br>

<p align="center"> Global All Time: 290ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/df5f5daf-bfbf-4707-bd1c-4e268704dde7"> </p>

<p align="center"> Brazil All Time: 8ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/4359417b-dc62-4e49-8105-4a52272d7cec"> </p>

<p align="center"> Global monthly: 182ⁿᵈ<br><br><img width="900px" src="https://github.com/user-attachments/assets/eefe4839-d008-454f-95a9-f143944542a6"> </p>

<p align="center"> Brazil monthly: 2ⁿᵈ<br><br><img width="900px" src="https://github.com/user-attachments/assets/b8148be9-3b29-4df1-a557-bb7060f943b3"> </p>


<br>

<p align="center">Weekly League: 4ᵗʰ Bronze<br><br><img width="900px" src="https://github.com/user-attachments/assets/24d07cc5-a176-46df-83b7-a6a65bdb104b"> </p>

<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thanks for coming!!!}}$$</h1>

<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 

<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thank you}}$$</h1>
<p align="center"><a href="https://tryhackme.com/p/tryhackme">tryhackme</a> and  <a href="https://tryhackme.com/p/hadrian3689">hadrian3689</a> for investing your time and effort to develop this walkthrough so that I could sharpen my skills!</p> 
