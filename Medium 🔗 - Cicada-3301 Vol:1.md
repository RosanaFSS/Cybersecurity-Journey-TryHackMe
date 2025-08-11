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

<br>

<img width="436" height="259" alt="image" src="https://github.com/user-attachments/assets/be2883a4-9e97-4f37-9e48-adbb9734c3e3" />

<br>

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

```bash
$ steghide extract -sf welcome.jpg
Enter passphrase:
wrote extracted data to "invitation.txt".
```

```bash
$ cat invitation.txt
https://imgur.com/a/c0ZSZga
```

<br>
<h2>Task 5 . FInd Hidden Files</h2>
<br>


<h2>Task 6 . Book Cipher</h2>
<br>


<h2>Task 7 . The Final Song</h2>
<br>
