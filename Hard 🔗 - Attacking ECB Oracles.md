<p align="center">April 19, 2025<br> 
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{348}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
<img width="300px" src="https://github.com/user-attachments/assets/d166a4ea-990f-4986-a6df-d3c181f805ea" alt="Your Image Badge"><br>
<img width="200px" src="https://github.com/user-attachments/assets/82705b74-d6b3-4b79-bae6-2dfa4440b08b"></p>
<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Attacking ECB Oracles}}$$</h1>
<p align="center"><em>Learn about the electronic codebook (ECB) cipher mode and how to exploit its weaknesses.</em>.<br>
It is classified as a hard-level CTF.<br>It is premium: only for subscribers.<br>
Can be accessed clicking  <a href="https://tryhackme.com/room/attackingecboracles">here</a>.</p>

<p align="center"> <img width="900px" src="https://github.com/user-attachments/assets/33a7f45c-a756-4266-9dee-f3bef3522509"> </p>

<br>
<br>

<h2>Task 1 . Introduction </h2>

<p>...</p>

<p>[  Start Machine  ]</p>


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 1.1. <em>I am ready to learn about ECB and how to exploit it!</em><br><a id='1.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>


<br>
<br>

<h2>Task 2 . Symmetric Encryption </h2>

<p>...</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 2.1. <em>In what year did NIST hold a competition to find a new encryption algorithm that correctly implemented the three fundamental rules of cryptography?</em><br><a id='2.1'></a>
>> <strong><code>1997</code></strong><br>
<p></p>

<br>

> 2.2. <em>What is the AES cipher otherwise known as?</em><br><a id='2.2'></a>
>> <strong><code>Rijndael cipher</code></strong><br>
<p></p>

<br>

> 2.3. <em>What type of encryption is AES? (Symmetric/Asymmetric)</em><br><a id='2.3'></a>
>> <strong><code>Symmetric</code></strong><br>
<p></p>

<br>
<br>

<h2>Task 3 . Code Books and Cipher Modes </h2>

<p>...</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 3.1. <em>AES is a cipher block which means that the text will be broken down into fixed-sized blocks to be converted into ciphertext. What is used when the last AES block of the original message isn't completely filled?</em><br><a id='3.1'></a>
>> <strong><code>padding</code></strong><br>
<p></p>

<br>

> 3.2. <em>What is the ciphertext when encrypting the message CryptographyAndADreamToSecurity using the secret NotAGreatSecret!?</em><br><a id='3.2'></a>
>> <strong><code>c35a97106295a3101b6be8a9af954d198462b30f0af7f669d46766cbeea7eabf</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/5f23ccd8-4633-46fb-8ba6-4628a1dc0992)


<br>
<br>

<h2>Task 4 . ECB Insecurities </h2>

<p>...</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questiosn below}}$$ </h3>

<br>

> 4.1. <em>What cipher principle does ECB not perform sufficiently, leading to it being vulnerable?</em><br><a id='4.1'></a>
>> <strong><code>diffusion</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/9e8b92ba-0be4-4bce-a588-e6d87847f027)


<br>

![image](https://github.com/user-attachments/assets/bbe924d5-01ff-44e5-9b59-80e4a21bfbdb)


<br>

![image](https://github.com/user-attachments/assets/30bb3640-90f4-4bef-b32e-920d1125750f)


<br>

> 4.2. <em>What types of files are notoriously difficult for ECB to encrypt?</em><br><a id='4.1'></a>
>> <strong>images<code>diffusion</code></strong><br>
<p></p>

<br>
<br>

<h2>Task 5 . Chosen-Plaintext Attacks </h2>

<p>...</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questiosn below}}$$ </h3>

<br>

> 5.1. <em>What do we need to determine in the first step to attack an ECB oracle?</em><br><a id='5.1'></a>
>> <strong><code>diffusion</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/8fb5d0b2-0d58-4c21-8d04-6c56576a9519)

<br>

> 5.2. <em>What is the second element that we need to determine to attack an ECB oracle?</em><br><a id='5.2'></a>
>> <strong><code>offset</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/09c1ac95-8309-48d4-9d21-852016f14c14)


<br>

> 5.3. <em>Using the script, what is the first character that is leaked from the oracle?</em><br><a id='5.2'></a>
>> <strong><code>O</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/74390644-9e4f-407c-b7ef-b84cfb062d14)

<br>

![image](https://github.com/user-attachments/assets/ee36c091-1244-40eb-8087-9629bd234885)

<br>

<br>

> 5.4. <em>Now for the challenge, upgrade the script to recover the entire secret from the oracle. What is this secret?</em>Hint : <em>Once you have extracted the first character, you want to calculate a new reference chunk with one less injected character. Then, since you know the character, you can add it back again and then stage an attack against the oracle to find the second character. The reference chunk for calculating the second byte (using all As) is 13a23afdd6652229dafd95506a4677ba, if you get a different reference chunk, it is most likely because you are "adding too much data" when generating your chunk.</em><br><a id='5.2'></a>
>> <strong><code>OracleKnows</code></strong><br>
<p></p>

<br>

<p>O</p>

![image](https://github.com/user-attachments/assets/9d0fcd21-7dac-49cb-b666-6edde192acd7)

<p>Or</p>

![image](https://github.com/user-attachments/assets/039c645b-7039-483c-9921-a988e656438a)

<p>Ora</p>

![image](https://github.com/user-attachments/assets/3b8bb1ff-913d-467d-9b27-96be4fb93c56)


<p>Orac</p>

![image](https://github.com/user-attachments/assets/fbdec159-e1ae-445c-882c-50dae22b7aba)

<br>

![image](https://github.com/user-attachments/assets/69cad735-a557-4d17-ab76-60cccb11b263)


<p>Oracl</p>

<br>

![image](https://github.com/user-attachments/assets/822a7380-f962-489f-a7e4-a7fe61d9ff57)

<br>

<p>Oracle<br>
OracleK</p>

<br>

![image](https://github.com/user-attachments/assets/5ea6e280-5a11-476b-8d1b-b9d1f9a9c521)


![image](https://github.com/user-attachments/assets/56be5fcd-ce14-4098-9648-2cc93f13beae)


<br>


<p>OraclKn</p>

<br>

![image](https://github.com/user-attachments/assets/8144c8ca-a7dc-44cf-b859-5df3abfef165)

<br>

<p>...</p>

<br>

<br>
<br>

<h2>Task 6 . Cipher Mode Best Practices</h2>

<p>...</p>

<br>

> 6.1. <em>I understand how to attack ECB oracles!</em><br><a id='6.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>





<br>
<br>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Room Completed}}$$</h1>
<br>
<p align="center">
<img width="900px" src="https://github.com/user-attachments/assets/cb432459-1401-404e-b374-de0a39de666f"><br>
<img width="900px" src="https://github.com/user-attachments/assets/7ad80a01-7a28-48e3-ba56-3139900d13547"></p>



<br>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{My TryHackMe Journey}}$$ </h1>
<br>


<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |   Brazil     |    Global   |   Brazil   |          | Completed |           |
| April 19, 2025    |   348    |     269ᵗʰ    |     6ᵗʰ      |      43rd   |     2ⁿᵈ    |  95,737  |    673    |    59     |

</div>


<br>


<p align="center"> Global All Time:  269ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/28a89c97-c7b8-4388-8e1a-45b0e374f3f9"> </p>

<p align="center"> Brazil All Time:    6ᵗʰ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/2a271a3c-c75f-4e18-964d-087ab9086d8f4"> </p>

<p align="center"> Global monthly:     43rd<br><br><img width="1000px" src="https://github.com/user-attachments/assets/1d044499-33e2-47c9-b8c7-0dce8a8f6a15"> </p>

<p align="center"> Brazil monthly:      2ⁿᵈ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/27939e38-54aa-4acd-b9da-a5ef6a89ae3a"> </p>


<br>

<p align="center">Weekly League: Silver 3ʳᵈ<br><br><img width="1000px" src="https://github.com/user-attachments/assets/7d852664-93b9-4295-82d8-ae74d3eb942b"> </p>

<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thanks for coming!!!}}$$</h1>

<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 

<br>

<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Thank you}}$$</h1>
<p align="center"><a href="https://tryhackme.com/p/tryhackme">tryhackme</a> and <a href="https://tryhackme.com/p/am03bam4nd">am03bam4nd</a>  for investing your time and effort to develop this walkthrough so that I could sharpen my skills!</p> 


