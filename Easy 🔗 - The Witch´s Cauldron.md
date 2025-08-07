<h1 align="center">The Witch´s Cauldron</h1>
<p align="center">2025, August 7<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>458</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>Can you share Bob's secret recipe with Alice without Eve finding out?</em>.<br>
<img width="80px" src="https://github.com/user-attachments/assets/140917bd-0b65-43d6-b19f-6431eddab707"><br>
Access this walkthrough room clicking <a href="https://tryhackme.com/room/cauldron">here </a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/03462942-e9e9-4b7c-91ad-45fdba6144ba"></p>

<br>
<h2>Task 1 .The Witch´s Cauldron</h2>
<p>Welcome to the enchanting world of witches and wizards. In this mystical laboratory, you find yourself as Witch Alice, a sorceress seeking an elusive secret potion recipe. Your trusted friend, Witch Bob, has discovered the hidden elixir of wonders and is eager to share it with you. However, an unforeseen obstacle stands in your way – Goblin Eve, determined to steal it for herself.</p>

<h3>Connection Details</h3>
<p>Start the app attached to this task by clicking "View Site". Once you have solved the challenge, submit the flag you receive below.</p>

<p>1.1. What is the flag that is returned after completing The Witch's Cauldron?<br>
<code>THM{y0u_br3w3d_7h3_53cr37}</code></p>

<br>

<img width="1346" height="865" alt="image" src="https://github.com/user-attachments/assets/fd6673b3-a244-4218-9173-5d408e3427c0" />

<img width="1346" height="867" alt="image" src="https://github.com/user-attachments/assets/4e908c5c-afc8-4d07-8715-229d78539509" />

<img width="1348" height="876" alt="image" src="https://github.com/user-attachments/assets/2f6cb2a8-f29e-43b8-954e-149dd757dce3" />

<img width="1337" height="870" alt="image" src="https://github.com/user-attachments/assets/17870994-fee7-40fc-8a25-2e581749cc0d" />

<img width="1347" height="879" alt="image" src="https://github.com/user-attachments/assets/96b119b3-dadd-4759-b2d1-be3bbd39b864" />

<img width="1350" height="775" alt="image" src="https://github.com/user-attachments/assets/f150bf12-ea30-44d1-b332-24e1c6e0fc5d" />

<br>

<h2>Task 2 .The Technical Components</h2>
<p>In the previous task, we found ourselves in a scenario where Bob needed to share his secret recipe with Eve. This effort required secure communication over a public (unsafe) medium. To achieve this, we delved into the fascinating world of cryptography and stumbled upon the Diffie-Hellman key exchange. Now, let's explore the technical theory behind this cryptographic protocol and its application in secure communication.<br>

The Diffie-Hellman key exchange, named after its inventors Whitfield Diffie and Martin Hellman, is a crucial concept in modern cryptography. It allows two parties to establish a shared secret key over an insecure communication channel without ever exchanging the key itself. This is accomplished by leveraging the properties of modular arithmetic and the computational complexity of discrete logarithm problems.</p>

<p>Below, let's walk through the steps Alice and Bob performed in The Witch's Cauldron to exchange keys and securely derive the same shared secret.</p>

<p>[ ... ]</p>

<h3>Common Base Potion</h3>
<br>

<h3>Secret Potions</h3>
<br>

<h3>Public Potions</h3>
<br>

<h3>What About Eve</h3>
<br>



<h3>Encryption and Decryption Operations</h3>
<br>


<h3>Bob's Encrypted Spell</h3>
<br>


<p><em>Answer the question below</em></p>

<p>2.1. What is the flag that is returned after decrypting <code>encrypted_spell.enc</code>?<br>
<code>THM{525403e42fbda51dfd0572025d78062f}</code></p>


<br>

```bash
:~/Rooms/cauldron# ls
alice.key  bob.public  encrypted_spell.enc
```


```bash
:~/Rooms/cauldron# openssl pkeyutl -derive -inkey alice.key -peerkey bob.public -out shared_secret.bin
```

```bash
~/Rooms/cauldron# ls
alice.key  bob.public  encrypted_spell.enc  shared_secret.bin
```

```bash
:~/Rooms/cauldron# openssl aes-256-cbc -d -in encrypted_spell.enc -pass file:shared_secret.bin
*** WARNING : deprecated key derivation used.
Using -iter or -pbkdf2 would be better.
THM{525403e42fbda51dfd0572025d78062f}
```


<p>The warning is not an error. It’s just OpenSSL telling:<br>
Hey, this method works, but it’s outdated. For future encryption, use -pbkdf2 so your files are more secure.</p>

<p>So I tried ...</p>



<br>
<br>

<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/736e166f-ea07-483f-9e7f-4e03115f1536"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/adc9c425-f2e7-4d68-b6ff-8595737a1189"></p>


<br>

<h1 align="center">My TryHackMe Journey</h1>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| 2025, August 7    |   458    |     131ˢᵗ    |      5ᵗʰ     |     664ᵗʰ   |    16ᵗʰ    | 119,526  |    902    |    73     |


</div>

<p align="center">Global All Time:   131ˢᵗ<br><img width="250px" src="https://github.com/user-attachments/assets/9f778d4c-9821-4683-bb16-11cb8c20e7b"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/e88d29a8-79b2-4573-9c53-824622397f3f"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/ecf778a7-94fe-4950-8944-71e8f256c38f"><br>
                  Global monthly:    664ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/3372c846-6493-4cce-b2a4-7e5435bf4d0b"><br>
                  Brazil monthly:     16ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/8a16764c-a1d1-43cc-9ea2-bf3a0e04322f"><br>

<br>
<h1 align="center">Thanks for Coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 
