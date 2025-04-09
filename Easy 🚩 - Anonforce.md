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

<p>user.txt</p>

![October-01-2024 - TryHackMe - Anonforce - CTF - Easy - Image 4](https://github.com/user-attachments/assets/214ff01a-672a-4a82-88fa-79efce07f21d)


<br>

<p><code>gpg</code></p>

![October-01-2024 - TryHackMe - Anonforce - CTF - Easy - Image 7](https://github.com/user-attachments/assets/93125179-5f97-4106-a8fb-b893f3053460)

<br>

<p><code>strings</code> <code>backup.gpg</code></p>

<br>

![October-02-2024 - TryHackMe - Anonforce - CTF - Easy - Image 10 - usei o comando strings no arquivo](https://github.com/user-attachments/assets/094a2464-0485-4ab6-bc4d-ecc7fe1e06ca)


<br>

<p><code>gpg2jhon</code> <code>backup.gpg</code></p>

![October-02-2024 - TryHackMe - Anonforce - CTF - Easy - Image 11 - usei o comando gpg2john no arquivo backup-pgp](https://github.com/user-attachments/assets/8cb31f01-683c-47d8-9ef7-4bba067e640d)

<br>

<p><code>gpg2jhon</code> <code>private.asc</code></p>

![October-02-2024 - TryHackMe - Anonforce - CTF - Easy - Image 12 - usei o comando gpg2john no arquivo private-asc](https://github.com/user-attachments/assets/6ab9e38f-f1a7-46d2-bc85-48dc1a38b030)

<br>

![October-02-2024 - TryHackMe - Anonforce - CTF - Easy - Image 13 - selecionei um trecho importante](https://github.com/user-attachments/assets/a4561218-c820-469f-b771-65233055dc1b)


<br>

<p>Create a file.</p>

![October-02-2024 - TryHackMe - Anonforce - CTF - Easy - Image 14 - criei um nano com a parte selecionada](https://github.com/user-attachments/assets/79abbdb2-3252-4b58-8c7a-e2eeedb37601)



<br>

<p><code>john</code> with the hash file just created.</p>

![October-02-2024 - TryHackMe - Anonforce - CTF - Easy - Image 15 - usei o comando john com wordlist](https://github.com/user-attachments/assets/c24ac1e2-dd8e-4ce8-b8ec-5e2ea0b8479d)


<br>

![October-02-2024 - TryHackMe - Anonforce - CTF - Easy - Image 16 - encontrei a senha](https://github.com/user-attachments/assets/f5ee1db4-d249-4fa9-ae9d-5296acf9a17d)


<br>

![October-02-2024 - TryHackMe - Anonforce - CTF - Easy - Image 22 - room complete - full view](https://github.com/user-attachments/assets/fc5860bd-8eb9-4cfe-bb46-b16ed311c0fc)

