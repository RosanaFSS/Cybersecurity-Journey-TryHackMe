<h1 align="center">Content Security Policy</h1>
<p align="center">2025, August 12<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my <code>464</code>-day-streak in <a href="https://tryhackme.com">TryHackMe</a>.<br>
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
<br>
<h2>Bypassing a Content Security Policy</h2>


<br>
<br>
<h2>CSP Sandbox</h2>


<br>
<br>
<h2>CSP Sandbox :: Attack challenges</h2>


<br>
<br>
<h2>CSp Sandbox :: Defend Challenges</h2>



<br>
<br>
