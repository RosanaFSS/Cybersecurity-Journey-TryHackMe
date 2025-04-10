<p align="center">April 9, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{338}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br></p>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Breaking Crypto the Simple Way}}$$</h1>


<p align="center">Exploiting common cryptographic mistakes. It is classified as an easy-level challenge, and you can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed. Click <a href="https://tryhackme.com/room/breakingcryptothesimpleway">here</a>.</p>

<p align="center"> <img width="900px" src="https://github.com/user-attachments/assets/37769b50-72b8-4de9-9c5c-362dcfcda5e9"> </p>

<br>
<br>


<h2>Task 1 . Introduction</h2>
<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

> 1.1. <em>I have started the target machine and I'm ready to break crypto!</em>.<a id='1.1'></a>
>> <code><strong>No answer needed</strong></code><br>

<br>

<p>Navigated to <code>http://TargetIP</code> after adding it to <code>/etc/hosts</code>.</p>

![image](https://github.com/user-attachments/assets/ecf0d6ce-fa8c-4b5e-a8ef-776effb72306)

<br>


<h2>Task 2 . Brute-forcing Keys</h2>
<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

> 2.1. <em>What is the flag?</em>.<a id='2.1'></a>
>> <code><strong>THM{Psssss_4nd_Qsssssss}</strong></code><br>

<br>

<p>Navigated to <code>https://factordb.com/</code>.</p>

![image](https://github.com/user-attachments/assets/c69fe52c-d256-45b4-9deb-31e58156f1ad)

<br>

<p>Discovered <code>p</code> and <code>q</code>.</p>

<br>

<p>Ran the script <a href="https://github.com/RosanaFSS/Cybersecurity-Journey-TryHackMe/blob/CTFs-%26-Infos/Easy%20%F0%9F%94%97%20-%20Breaking%20Crypto%20the%20Simple%20Way%20-%20Task%202-1.py">Task2-1.py</a>.</p>

<br>


![image](https://github.com/user-attachments/assets/d7c04856-662f-456e-bb3d-f845d15cb715)

<br>

<p>Ran the script <a href="https://github.com/RosanaFSS/Cybersecurity-Journey-TryHackMe/blob/CTFs-%26-Infos/Easy%20%F0%9F%94%97%20-%20Breaking%20Crypto%20the%20Simple%20Way%20-%20Task%202-2.py">Task2-2.py</a>.</p>

<br>

![image](https://github.com/user-attachments/assets/3e2d1919-7e3c-4690-a3aa-4ffc00d63190)

<br>

<h2>Task 3 . Breaking Hashes</h2>
<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

> 3.1. <em>What is the flag?</em><a id='3.1'></a>
>> <code><strong>sunshine</strong></code><br>


<br>

<p>Ran the script <a href="https://github.com/RosanaFSS/Cybersecurity-Journey-TryHackMe/blob/CTFs-%26-Infos/Easy%20%F0%9F%94%97%20-%20Breaking%20Crypto%20the%20Simple%20Way%20-%20Task%203.py">Task3.py</a>.</p>

<br>

![image](https://github.com/user-attachments/assets/3d301f4d-dd00-4332-a503-93fac5ed0990)

<br>

![image](https://github.com/user-attachments/assets/c64b0d0c-dc89-42fe-8552-c0177ff292c5)

<br>

<h2>Task 4 . Exposed Keys</h2>
<br>


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

> 4.1. <em>What is the flag?</em>.<a id='4.1'></a>
>> <code><strong>THM{3nD_2_3nd_is_n0t_c0mpl1c4ted}</strong></code><br>

<br>

![image](https://github.com/user-attachments/assets/3a4066c5-2cb2-4b04-b2df-0a285be59e75)

<br>

![image](https://github.com/user-attachments/assets/1779da3d-143a-489f-9835-b06cf6f36f98)

<br>

<p>Ran the script <a href="https://github.com/RosanaFSS/Cybersecurity-Journey-TryHackMe/blob/CTFs-%26-Infos/Easy%20%F0%9F%94%97%20-%20Breaking%20Crypto%20the%20Simple%20Way%20-%20Task%205.py">Task5.py</a>.<br>
<br>  
It just worked using <code>python3.9</code>.</p>

<br>

![image](https://github.com/user-attachments/assets/7b092508-f232-445d-ba3f-4c3974e807e8)


<br>

<h2>Task 5 . Bit Flipping Attacks</h2>
<br>


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

> 5.1. <em>What is the flag?</em>.<a id='5.1'></a>
>> <code><strong>THM{flip_n_flip}</strong></code><br>

<br>

<p>Navigated to lab4.</p>

![image](https://github.com/user-attachments/assets/e632a3d6-96f3-4dce-b27e-c93056ee2c11)

<p>Typed <code>user</code> and <code>password</code>.<br>
Clicked <code>Login</code>.</p>

![image](https://github.com/user-attachments/assets/b4b159f0-8804-4252-b14b-613f6a12f56e)

<p>The credentials were accepted.</p>

![image](https://github.com/user-attachments/assets/9311c49f-fc55-45af-8ca0-a5b89360f8c2)

<p>Checked the <code>cookies</code>.</p>

![image](https://github.com/user-attachments/assets/87905ba3-3463-4d34-9fe9-199c267a5e42)

<br>

<p>Ran the script provided with the specific <code>role token</code>.</p>

![image](https://github.com/user-attachments/assets/7a71549e-32e5-4d05-81db-f9ce9de6bc1b)

<br>

<p>Copied the <code>Modified Token</code> content and pasted in the <code>Value</code> field of the <code>role</code> cookie.<br>
Refreshed the webpage.</p>


![image](https://github.com/user-attachments/assets/e9489568-a885-4f07-b1b0-6345f161419a)

<br>

<h2>Task 6 .Conclusion</h2>
<br>


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

> 6.1. <em>Click me to proceed to the next task.?</em>.<a id='6.1'></a>
>> <code><strong>No answer needed</strong></code><br>

<br>
<br>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Room Completed}}$$</h1>
<br>
<p align="center"><img width="900px" src="https://github.com/user-attachments/assets/f75badee-e26d-4d1a-87d2-fc4c1aee3b99">
<br><img width="900px" src="https://github.com/user-attachments/assets/8506dc32-b0f9-4ab6-959e-de9004c8d848"></p>

<br>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{My TryHackMe Journey}}$$ </h1>
<br>


<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |Global        | Brazil       | Global      | Brazil     |          | Completed |           |
| April 7, 2025     | 336      |     299ᵗʰ    |        8ᵗʰ   |    354ᵗʰ    |     3ʳᵈ    |  92,038  |       650 |   59      |

</div>

<br>

<p align="center">League<br><br><img width="300px" src="https://github.com/user-attachments/assets/35c02f68-2fbc-4da9-a282-357432eaf2da"> </p>


<br>

<p align="center"> Global All Time: 299ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/3f8e44e6-6775-4fd5-b5c3-46e01bfd6190"> </p>

<p align="center"> Brazil All Time: 8ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/5ec0e0dd-31e1-4cbe-9c74-e25bfab3975b"> </p>

<p align="center"> Global monthly: 354ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/bf1107f3-05cf-40f6-88b6-203e87a5b315"> </p>

<p align="center"> Brazil monthly: 3ʳᵈ<br><br><img width="900px" src="https://github.com/user-attachments/assets/a413e51a-c2a3-48fa-809a-26498fe717eb"> </p>


<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thanks for coming!!!}}$$</h1>

<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 

<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thank you}}$$</h1>
<p align="center"><a href="https://tryhackme.com/p/tryhackme">tryhackme</a> and  <a href="https://tryhackme.com/p/l000g1c">l000g1c</a> for investing your time and effort to develop this walkthrough so that I could sharpen my skills!</p> 
