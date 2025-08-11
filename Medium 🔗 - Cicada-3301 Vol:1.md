<h1 align="center">Cicada-3301 Vol:1</h1>
<p align="center">2025, August 11<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>462</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>A basic steganography and cryptography challenge room based on the Cicada 3301 challenges</em>.<br>
<img width="80px" src=https://github.com/user-attachments/assets/4fadd8a0-4df0-4906-8d4d-f5d80db1f61f"><br>
Access this TryHackMe´s walkthrough <a href="https://tryhackme.com/room/cicada3301vol1">here </a>.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/b5cdc3f5-c330-4f5c-a1f6-e9eeb8d9b451"></p>


<br>


<h1>Cicada-3301 Vol:1</h1>
<p>A basic steganography and cryptography challenge room based on the Cicada 3301 challenges
<p>2025, August 11 - Day 462</p>


<h2>Task 1 . Download</h2>
<p>Hello, We are looking for highly intelligentindividuals. To find them, we have devised a test.<br>
There is a message hidden in this image.<br>
Download and unzip the folder given to begin.<br>
Good Luck.<br>
-3301</p>

<p><em>Answer the question below</em></p>

<p>1.1. Download and unzip the given folder<br>
<code>No answer needed</code></p>

<br>
<h2>Task 2 . Analyze the Audio</h2>
<p>Web Browsers are useless here<br>

Welcome.<br>

Good Luck<br>

-3301<br>

Use Sonic Visualizer to analyze the audio.</p>

<p><em>Answer the question below</em></p>

<p>2.1. What is the link inside of the audio?<br>
<code>https://pastebin.com/wphPq0Aa</code></p>

<br>

<p>

- launched <code>Sonic Visualiser</code><br>
- opened <code>3301.wav</code><br>
- clicked <code>Pane</code> > <code>Add Spectrogram</code><br>
- saved the QR code<br>
- uploaded the file in <code>CyberChef</code><br>
- used the recipe <code>Parse QR code</code></p>

<br>

<br>

```bash
$ sudo apt-get install sonic-visualiser
```


<img width="1916" height="1028" alt="image" src="https://github.com/user-attachments/assets/cf94ad73-b965-4964-8807-ebad25eb3ac8" />

<br><br>

<img width="261" height="202" alt="image" src="https://github.com/user-attachments/assets/b7d13869-c29a-45e3-9088-7da24514bbae" />

<br><br>

<img width="1358" height="237" alt="image" src="https://github.com/user-attachments/assets/26bb5516-d7d5-4373-8c5b-8a692b1c9416" />

<br>
<br>
<h2>Task 3 . Decode the Passphrase</h2>
<p>Welcome.<br>

Good Luck.<br>

-3301<br>

Use various encryption methods and ciphers to decode the passphrase and<br>

access the metadata of Welcome.jpg<br>

<p><em>Answer the questions below</em></p>

<p>3.1. Find and Decrypt the passphrase and key<br>
<code>No answer needed</code></p>

<br>

<p>3.2. What is the decrypted passphrase? Hint : Base64<br>
<code>Hm5R_4_P455mhp453!</code></p>

<br>

<p>3.3. What is the decrypted key? Hint : Base64<br>
<code>Cicada</code></p>

<br>

<p>3.4. Still looks funny? Find and use a cipher along with the key to decipher the passphrase. Hint : French Diplomat Cipher<br>
<code>No answer needed</code></p>

<br>

<p>3.5. What is the final passphrase. Hint : Encode using Vigenere Cipher<br>
<code>Ju5T_4_P455phr453!</code></p>

<br>

<p>
  
- navigated to the link discovered in the previous task<br>
- discovered Passphrase: SG01Ul80X1A0NTVtaHA0NTMh<br>
- discovered Key: Q2ljYWRh<br>
- decoded it<br>
- got <code>Hm5R_4_P455mhp453!</code> : <code>Cicada</code><br>
- used <code>Vigenere Cipher</code> = https://www.dcode.fr/vigenere-cipher</p>

<br>

<img width="1282" height="286" alt="image" src="https://github.com/user-attachments/assets/050354ff-ef69-4ddb-bf02-b8fb4ffb8fc4" />

<br><br>

```bash
$ echo "SG01Ul80X1A0NTVtaHA0NTMh" | base64 -d
Hm5R_4_P455mhp453!
```

<br>

```bash
$ echo "Q2ljYWRh" | base64 -d
Cicada
```

<br>

<img width="461" height="118" alt="image" src="https://github.com/user-attachments/assets/4a1bb106-9ae4-4dac-ae3a-985e4547f000" />

<br><br>

<img width="436" height="259" alt="image" src="https://github.com/user-attachments/assets/be2883a4-9e97-4f37-9e48-adbb9734c3e3" />

<br><br>

<img width="358" height="311" alt="image" src="https://github.com/user-attachments/assets/65015a08-87c1-4fa9-b583-336a0c073e82" />

<br>

<h2>Task 4 . Gather Metadata</h2>
<p>Good Luck<br>

-3301<br>

Use Steganography tools to gather metadata from Welcome.jpg as well as<br>

find the hidden message inside of the image file.</p>

<p><em>Answer the questions below</em></p>

<p>4.1. Using the found passphrase along with Stego tools find the secret message. Hint : Steghide<br>
<code>No answer needed</code></p>

<br>

<p>4.2. What link is given? Hint : Base64<br>
<code>https://imgur.com/a/c0ZSZga</code></p>

<br>

```bash
$ steghide extract -sf welcome.jpg
Enter passphrase:
wrote extracted data to "invitation.txt".
```

<br>

```bash
$ cat invitation.txt
https://imgur.com/a/c0ZSZga
```

<br>
<h2>Task 5 . FInd Hidden Files</h2>
<p>I am surprised you have made it this far...<br>

I doubt you will make it any further.<br>

-3301<br>

Use Stego tools to find the hidden files inside of the image</p>

<p><em>Answer the questions below</em></p>

<p>5.1. Using stego tools find the hidden file inside of the image Hint : Use the same tool used to extract data in the original Cicada challenges<br>
<code>No answer needed</code></p>

<br>

<p>5.2. What tool did you use to find the hidden file.<br>
<code>outguess</code></p>

<br>

<p>

- navigated to the linked discovered in the previous task<br>
- downloaded the image<br>
- used outguess</p>

<br>
<br>

<img width="1126" height="666" alt="image" src="https://github.com/user-attachments/assets/28fb2975-0aee-474c-a364-86cdd8567ac9" />

<br>
<br>

```bash
$ sudo apt-get install outguess
```

<br>

```bash
$ outguess -r Imgur.jpg outputmessage
Reading Imgur.jpg....
Extracting usable bits:   29035 bits
Steg retrieve: seed: 38, len: 1351
```

<br>

```bash
$ cat outputmessage
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA1

Welcome again.

Here is a book code.  To find the book, break this hash:

b6a233fb9b2d8772b636ab581169b58c98bd4b8df25e452911ef75561df649edc8852846e81837136840f3aa453e83d86323082d5b6002a16bc20c1560828348

Use positive integers to go forward in the text use negative integers to go backwards in the text.

I:1:6
I:2:15
I:3:26
I:5:4
I:6:15
I:10:26
/
/
I:13:5
I:13:1
I:14:7
I:3:29
I:19:8
I:22:25
/
I:23:-1
I:19:-1
I:2:21
I:5:9
I:24:-2
I:22:1
I:38:1


Good luck.

3301

-----BEGIN PGP SIGNATURE-----
Version: GnuPG v1.4.11 (GNU/Linux)

...
URKvgl0/nZumrPQYbB1roxAaCMtlMoIOvwcyldO0iOQ/2iD4Y0L4sTL7ojq2UYwX
bCotrhYv1srzBIOh+8vuBhV9ROnf/gab4tJII063EmztkBJ+HLfst0qZFAPHQG22
41kaNgYIYeikTrweFqSK
=Ybd6
-----END PGP SIGNATURE-----
```

<br>

<h2>Task 6 . Book Cipher</h2>
<p></p>We have one last challenge to find our individuals<br>

Find the last clue, crack the hash, decipher the message<br>

Good Luck<br>

-3301<BR>

Use Hash cracking tools to reveal the text to the text<br>

Use methods like Cicada to decipher the message</p>
<br>

<p><em>Answer the questions below</em></p>

<p>6.1. Crack the Hash<br>
<code>No answer needed</code></p>

<br>

<p>6.2. What is the Hash type? Hint : SHA... Figure out the rest<br>
<code>SHA512</code></p>

<br>

```bash
$ sudo apt-get install hashid
```

<br>

```bash
$ hashid b6a233fb9b2d8772b636ab581169b58c98bd4b8df25e452911ef75561df649edc8852846e81837136840f3aa453e83d86323082d5b6002a16bc20c1560828348
Analyzing 'b6a233fb9b2d8772b636ab581169b58c98bd4b8df25e452911ef75561df649edc8852846e81837136840f3aa453e83d86323082d5b6002a16bc20c1560828348'
[+] SHA-512
[+] Whirlpool
[+] Salsa10
[+] Salsa20
[+] SHA3-512
[+] Skein-512
[+] Skein-1024(512)
```


<br>

<p>6.3. What is the Link from the hash? Hint : Answer is not in conventional wordlists, try an online service<br>
<code>https://pastebin.com/6FNiVLh5</code></p>

<br>

```bash
$ sudo apt-get install hashid
```

<p>

- navigated to <code>https://md5hashing.net/hash/sha512</code><br>
- pasted the hash in <code>Reverse sha512 decoder</code><br>
- clicked <code>Decode!</code></p>

<br>

<img width="1605" height="477" alt="image" src="https://github.com/user-attachments/assets/e25b63be-ea7b-4a4c-9364-09da1e28c6e2" />

<br>

<p>6.4. Decipher the message. Hint : Use the same techniques the Cicada participants used<br>
<code>No need to answer</code></p>

<br>

<p>

- navigated to the link discovered in the previous step</p>

<br>

<img width="1214" height="876" alt="image" src="https://github.com/user-attachments/assets/1fb6f362-d385-47cc-81ec-048aa6ddec11" />


<br>

<p>6.5. What is the link?<br>
<code>https://bit.ly/39pw2NH</code></p>

<br>


<p>

- <code>I:1:6</code> = <code>1.</code>, <code>6</code>th character = <code>h</code><br>
- <code>I:2:15</code> = <code>2.</code>, <code>15</code>th character = <code>t</code><br>
- <code>I:3:26</code> = <code>3.</code>, <code>26</code>th character = <code>t</code><br>
- ...
</p>

<br>

<p>
  
Chapter I<br>

1. Had! T<code>h</code>e manifestation of Nuit.<br>
 
2. The unveiling of <code>t</code>he company of heaven.<br>
 
3. Every man and every woman is a s<code>t</code>ar.<br>
 
4. Every number is infinite; there is no difference.<br>
 
5. Hel<code>p</code> me, o warrior lord of Thebes, in my unveiling before the Children of men!<br>
 
6. Be thou Hadit, my <code>s</code>ecret centre, my heart & my tongue!<br>
 
7. Behold! it is revealed by Aiwass the minister of Hoor-paar-kraat.<br>
 
8. The Khabs is in the Khu, not the Khu in the Khabs.<br>
 
9. Worship then the Khabs, and behold my light shed over you!<br>
 
10. Let my servants be few & secret<code>:</code> they shall rule the many & the known.</p>

<br>

<h2>Task 7 . The Final Song</h2>
<p>We have found the individuals we sought<br>

-3301</p>

<p><em>Answer the questions below</em></p>

<p>7.1. What is the song linked?<br>
<code>The Instar Emergence</code></p>

<br>

<img width="429" height="33" alt="image" src="https://github.com/user-attachments/assets/87b10c16-3749-4497-9104-3d5c0a8cb018" />

<br>

<img width="1162" height="339" alt="image" src="https://github.com/user-attachments/assets/b47b0020-2242-4300-832b-0b070f6ee57d" />

<br>
<br>

<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/c64adecd-0d6c-4853-81a6-c3ae7c33f90e"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/eba0bfc3-4156-419a-9111-1b18df444dea"></p>

<br>

<h1 align="center">My TryHackMe Journey</h1>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| 2025, August 11   |   462    |     128ᵗʰ    |      5ᵗʰ     |     364ᵗʰ   |     7ᵗʰ    | 120,476  |    909    |    73     |


</div>

<p align="center">Global All Time:   126ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/ce6ab721-f601-4f8a-a55b-9de40602bd82"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/1a83a5b6-66d7-4c3f-874e-7231ddc42f81"><br><br>
                  Brazil All Time:     5ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/faca4f31-5550-4156-939c-b23cd9b788c8"><br>
                  Global monthly:    364ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/686d15e3-8a56-4bb6-800d-6c19939ba097"><br>
                  Brazil monthly:      7ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/f638c626-c74c-48cd-b0b3-297e155572bd"><br>

<br>
<h1 align="center">Thanks for Coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 
