

<h2>Task 5 - Webserver | Enumeration</h2>
<p>As with any attack, we first begin with the enumeration phase. Completing the Nmap room (if you haven't already) will help with this section.<br>

Thomas gave us an IP to work with (shown on the Network Panel at the top of the page). Let's start by performing a port scan on the first 15000 ports of this IP.<br>

Note: Here (and in general), it's a good idea to save your scan results to a file so you don't have to re-run the same scan twice.</p>

<p><em>Answer the questions below</em></p>

<p>5.1. <em>How many of the first 15000 ports are open on the target?</em> Hint: nmap -p-15000 -vv TARGET_IP -oG initial-scan<br>
<code>4</code>/p>

<p>5.2. <em>Perform a service scan on these open ports. What OS does Nmap think is running?</em> Hint: This will be given by the webserver. Note that Nmap is unlikely to get a valid result with -O, so use the headers from the webserver to ascertain the OS.<br>
<code>CentOS</code>

<p>5.3. <em>Okay, we know what we're dealing with. Open the IP in your browser -- what site does the server try to redirect you to?</em><br>
<code>https://thomaswreath.thm</code>

<p>You will have noticed that the site failed to resolve. Looks like Thomas forgot to set up the DNS!</p>

<p>Add it to your hosts file manually. This can be accomplished by editing the /etc/hosts file on Linux/MacOS, or C:\Windows\System32\drivers\etc\hosts on Windows, to include the IP address, followed by a tab, then the domain name. Note: this must be done as root/Administrator.</p>


<p>5.4. <em>It should look something like this when done, although the IP address and domain name will be different:</em> <code>10.10.10.10 example.thm</code> Hint: Make sure you don't include the https://. It should just be domainname.thm<br>
<code>No answer needed</code>

```bash
:~# nmap -sC -sV -T4 -p- 15000 10.200.100.0/24


```



```bash
:~# nmap -p-15000 -vv 10.200.180.209 -oG initial-scan

```



```bash
:~# nmap -p-15000 -vv 10.200.180.209 -oG initial-scan

```
