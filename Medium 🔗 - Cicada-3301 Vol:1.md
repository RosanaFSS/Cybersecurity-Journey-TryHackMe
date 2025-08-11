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

<img width="1126" height="666" alt="image" src="https://github.com/user-attachments/assets/28fb2975-0aee-474c-a364-86cdd8567ac9" />

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

iQIcBAEBAgAGBQJQ5QoZAAoJEBgfAeV6NQkPf2IQAKWgwI5EC33Hzje+YfeaLf6m
sLKjpc2Go98BWGReikDLS4PpkjX962L4Q3TZyzGenjJSUAEcyoHVINbqvK1sMvE5
9lBPmsdBMDPreA8oAZ3cbwtI3QuOFi3tY2qI5sJ7GSfUgiuI6FVVYTU/iXhXbHtL
boY4Sql5y7GaZ65cmH0eA6/418d9KL3Qq3qkTcM/tRAHhOZFMZfT42nsbcvZ2sWi
YyrAT5C+gs53YhODxEY0T9M2fam5AgUIWrMQa3oTRHSoNAefrDuOE7YtPy40j7kk
5/5RztmAzeEdRd8QS1ktHMezXEhdDP/DEdIJCLT5eA27VnTY4+x1Ag9tsDFuitY4
2kEaVtCrf/36JAAwEcwOg2B/stdjXe10RHFStY0N9wQdReW3yAOBohvtOubicbYY
mSCS1Bx91z7uYOo2QwtRaxNs69beSSy+oWBef4uTir8Q6WmgJpmzgmeG7ttEHquj
69CLSOWOm6Yc6qixsZy7ZkYDrSVrPwpAZdEXip7OHST5QE/Rd1M8RWCOODba16Lu
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

<p>6.2.What is the Hash type? Hint : SHA... Figure out the rest<br>
<code>SHA512</code></p>

<br>

```bash
$ sudo apt-get install hashid
```

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



<h2>Task 7 . The Final Song</h2>
<br>
