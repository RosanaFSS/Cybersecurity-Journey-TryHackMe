<p align="center">October 2, 2024</p>
<p align="center">Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{149}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.</p>

<h1 align="center">
  $$\textcolor{#3bd62d}{\textnormal{Anonforce}}$$
</h1>
<p align="center">It is classified as an easy-level challenge.
<br>You can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed.
<br>Can be accessed clicking <a href="https://tryhackme.com/room/bsidesgtanonforce">here</a>.</p> 
                                                              
<p align="center"><img width="900px" src="https://github.com/user-attachments/assets/1530c396-5e63-4fa6-91d0-4a1b5a1a2491"></p>

<br>

<br>

<p><code>nmap -sV</code> Target IP</p>

<p></p>

![October-01-2024 - TryHackMe - Anonforce - CTF - Easy - Image 1 - nmap](https://github.com/user-attachments/assets/e5010f25-7987-4121-82ab-6610aaae7c3b)

<br>

<p><code>nmap -T4 -sVC</code> TargetIP</p>

![October-02-2024 - TryHackMe - Anonforce - CTF - Easy - Image 1 - Starting again from zero](https://github.com/user-attachments/assets/2f925be6-c3de-46dc-a15d-547e3b6b0125)


<br>


<p><code>ftp</code> TargetIP</p>

<br>

![October-02-2024 - TryHackMe - Anonforce - CTF - Easy - Image 2 - did nmap and now ftp](https://github.com/user-attachments/assets/39c0b88a-4df5-41c7-9dc1-1f8570ecffb8)

<br>

<p><code>get</code> user.txt</p>

![October-02-2024 - TryHackMe - Anonforce - CTF - Easy - Image 3 - ftp e acessei diretorio home, melodias](https://github.com/user-attachments/assets/a1601151-a3b0-4725-ab78-8fc6c9724276)



<br>

![October-01-2024 - TryHackMe - Anonforce - CTF - Easy - Image 3 - found root flag](https://github.com/user-attachments/assets/1b66a2bd-c7f2-4c7f-9568-92e5adc016ac)

<br>

<p><code>cat</code> user.txt</p>

![October-01-2024 - TryHackMe - Anonforce - CTF - Easy - Image 4](https://github.com/user-attachments/assets/214ff01a-672a-4a82-88fa-79efce07f21d)



<br>

<p>- <code>strings</code> backup.pgp<br>
- <code>gpg2jhon</code> private.asc<br>
- <code>gpg2jhon</code> backup.pgp<br>
- created a file with the hash</p>

<br>

![October-02-2024 - TryHackMe - Anonforce - CTF - Easy - Image 13 - selecionei um trecho importante](https://github.com/user-attachments/assets/a4561218-c820-469f-b771-65233055dc1b)


<br>

![October-02-2024 - TryHackMe - Anonforce - CTF - Easy - Image 14 - criei um nano com a parte selecionada](https://github.com/user-attachments/assets/79abbdb2-3252-4b58-8c7a-e2eeedb37601)



<br>

<p>- used <code>john</code> to crack and to show the hash</p>


![October-02-2024 - TryHackMe - Anonforce - CTF - Easy - Image 16 - encontrei a senha](https://github.com/user-attachments/assets/f5ee1db4-d249-4fa9-ae9d-5296acf9a17d)


<br>

<p>- used <code>gpg</code> to import and to decrypt backup.pgp<br><br>
<code>gpg --import private.asc<br>
...<br>
gpgp --decrypt backup.pgp</code></p>

![October-02-2024 - TryHackMe - Anonforce - CTF - Easy - Image 18](https://github.com/user-attachments/assets/fe8a2d61-5ec2-4a35-beb2-d27fa25be151)

<br>

<p>created a file root hash<br>
<br>
used <code>john</code> to crack and show root´s hash</p>

<br>

![image](https://github.com/user-attachments/assets/3cb0488c-d04c-4115-b73a-563ed63524a1)

<br>

<p>used <code>ssh</code> to get access as root and find root.txt</p>

<br>

![October-02-2024 - TryHackMe - Anonforce - CTF - Easy - Image 21](https://github.com/user-attachments/assets/2af603a9-bd29-4621-9fd6-07434583d8ea)




<br>

<br>

![October-02-2024 - TryHackMe - Anonforce - CTF - Easy - Image 22 - room complete](https://github.com/user-attachments/assets/cce16c5f-d2f5-44ab-bce8-0a2afd245a21)

<br>


![October-02-2024 - TryHackMe - Anonforce - CTF - Easy - Image 22 - room complete - full view](https://github.com/user-attachments/assets/fc5860bd-8eb9-4cfe-bb46-b16ed311c0fc)

