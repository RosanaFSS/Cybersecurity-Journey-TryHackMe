<p align="center">November 20, 2024</p>
<p align="center">Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{197}}$$-day-streak in  <a href="https://tryhackme.com/r/hacktivities">TryHackMe</a>.</p>

<h1 align="center">
  $$\textcolor{#3bd62d}{\textnormal{XXE Injection}}$$
</h1>
<p align="center">Exploiting XML External Entities.<br>
Access this TryHackMe CTF Room clicking <a href="https://tryhackme.com/r/room/xxeinjection">XXE Injection</a>.</p><br>

<p align="center">
  <img height="150px" hspace="20" src="https://github.com/user-attachments/assets/a5324ef3-8fd6-4015-88c8-f415c54edebc"><br>
  <img width="900px" src="https://github.com/user-attachments/assets/c0dbfd51-9b09-4437-9139-06dc57863a65">
</p>

<p align="center">Summary</p>

[Introduction](#1) &nbsp;&nbsp;&nbsp;&nbsp;▪️&nbsp;&nbsp;&nbsp;&nbsp; [Exploring XML](#2) &nbsp;&nbsp;&nbsp;&nbsp;▪️&nbsp;&nbsp;&nbsp;&nbsp; [XML Parsing Mehcanisms](#3) &nbsp;&nbsp;&nbsp;&nbsp;▪️&nbsp;&nbsp;&nbsp;&nbsp; [Exploiting XXE - In-Band](#4) &nbsp;&nbsp;&nbsp;&nbsp;▪️&nbsp;&nbsp;&nbsp;&nbsp;[Exploiting XXE - Out-of-Band](#5) <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [SSRF + XXE](#6) &nbsp;&nbsp;&nbsp;&nbsp;▪️&nbsp;&nbsp;&nbsp;&nbsp; [Mitigation](#7)  &nbsp;&nbsp;&nbsp;&nbsp;▪️&nbsp;&nbsp;&nbsp;&nbsp; [Conclusion](#8) &nbsp;&nbsp;&nbsp;&nbsp;▪️&nbsp;&nbsp;&nbsp;&nbsp; [Room Complete](#9) &nbsp;&nbsp;&nbsp;&nbsp;▪️&nbsp;&nbsp;&nbsp;&nbsp; [My Journey](#10)

<br>
<h2>Task 1.  Introduction<a id='1'></a></h2>

<br>
<h2>Task 2.  Exploring XML<a id='2'></a></h2>

<br>
<h2>Task 3.  XML Parsing Mechanisms<a id='3'></a></h2>

<br>
<h2>Task 4.  Exploiting XXE - In-Band<a id='4'></a></h2>
<h3>In-Band vs Out-of-Band XXE</h3>

<p>In-band XXE refers to an XXE vulnerability where the attacker can see the response from the server. This allows for straightforward data exfiltration and exploitation. The attacker can simply send a malicious XML payload to the application, and the server will respond with the extracted data or the result of the attack.

Out-of-band XXE, on the other hand, refers to an XXE vulnerability where the attacker cannot see the response from the server. This requires using alternative channels, such as DNS or HTTP requests, to exfiltrate data. To extract the data, the attacker must craft a malicious XML payload that will trigger an out-of-band request, such as a DNS query or an HTTP request.</p>

<br>
<h3>In-Band XXE Exploitation</h3>
<p>We will be using Burp for this room. To demonstrate this vulnerability, go to http://10.10.18.162/contact.php, and fill out the form.</p>

![image](https://github.com/user-attachments/assets/0c8415df-d059-4346-956a-d07afbb133e9)

<p>Click the submit button and intercept the request.</p>

![image](https://github.com/user-attachments/assets/99f73232-bac6-4b34-a0b4-a037c3536a5d)

<p>The submitted data is processed by contact_submit.php, which contains a vulnerable PHP code designed to return the value of the name parameter when a user submits a message in the form. Below is the vulnerable code:</p>

<pre><code>libxml_disable_entity_loader(false);

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $xmlData = file_get_contents('php://input');

    $doc = new DOMDocument();
    $doc->loadXML($xmlData, LIBXML_NOENT | LIBXML_DTDLOAD); 

    $expandedContent = $doc->getElementsByTagName('name')[0]->textContent;

    echo "Thank you, " .$expandedContent . "! Your message has been received.";
}
</code></pre>

<p>Since the application returns the value of the name parameter, we can inject an entity that is pointing to /etc/passwd to disclose its values.</p>

![image](https://github.com/user-attachments/assets/0f156bea-9ebe-4a25-8926-eb6075397055)

<p>Using the payload above, replace the initial XML data submitted to contact_submit.php and resend the request.</p>

![image](https://github.com/user-attachments/assets/58e81427-a150-4b62-aff9-4fcc34890026)

<br>
<h3>XML Entity Expansion</h3>
<p>XML Entity Expansion is a technique often used in XXE attacks that involves defining entities within an XML document, which the XML parser then expands. Attackers can abuse this feature by creating recursive or excessively large entities, leading to a Denial of Service (DoS) attack or defining external entities referencing sensitive files or services. This method is central to both in-band and out-of-band XXE, as it allows attackers to inject malicious entities into the XML data. For example:</p>

![image](https://github.com/user-attachments/assets/34f34513-739c-4ffb-9727-0b37e765ff84) 

<p>In the payload above, &xxe; is expanded wherever it appears. Attackers can use entity expansion to perform a Billion Laughs attack, where a small XML document recursively expands to consume server resources, leading to a denial of service.</p>

![image](https://github.com/user-attachments/assets/5407e2fd-7b56-4115-b520-63f0c2d60d65)

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

> 4.1. <em>What XXE vulnerability occurs when the server's response is immediately disclosed to the attacker without the use of external channels?</em><br><a id='4.1'></a>
>> <strong><code>In-Band XXE</code></strong><br>
<p><br></p>


> 4.2. <em>What is the content of the file 14232d6db2b5fd937aa92e8b3c48d958.txt in the /opt directory?</em><br><a id='4.2'></a>
>> <strong><code>THM{1N_b4Nd_1$_34sYY}</code></strong><br>
<p><br></p>

![image](https://github.com/user-attachments/assets/53e2b635-6567-43c9-b046-819959d5d8b2)

![image](https://github.com/user-attachments/assets/360c7fa8-3b8e-4a67-bebf-635d22ebe578)

![image](https://github.com/user-attachments/assets/81205eb8-00d0-400c-a34a-187a4906dd1c)

![image](https://github.com/user-attachments/assets/25cb6287-639e-4953-a359-e39e3a81707b)

![image](https://github.com/user-attachments/assets/a43b9e26-ee85-4fe6-8ecc-122ba82ed00e)

<br>
<h2>Task 5.  Exploiting XXE - Out-of-Band<a id='5'></a></h2>

<br>
<h3>Out-Of-Band XXE</h3>
<p>On the other hand, to demonstrate this vulnerability, go to http://10.10.18.162/index.php. The application uses the below code when a user uploads a file:</p>

<pre><code>libxml_disable_entity_loader(false);
$xmlData = file_get_contents('php://input'); 

$doc = new DOMDocument();
$doc->loadXML($xmlData, LIBXML_NOENT | LIBXML_DTDLOAD);

$links = $doc->getElementsByTagName('file');

foreach ($links as $link) {
    $fileLink = $link->nodeValue;
    $stmt = $conn->prepare("INSERT INTO uploads (link, uploaded_date) VALUES (?, NOW())");
    $stmt->bind_param("s", $fileLink);
    $stmt->execute();
    
    if ($stmt->affected_rows > 0) {
        echo "Link saved successfully.";
    } else {
        echo "Error saving link.";
    }
    
    $stmt->close();
}
</code></pre>

<p>The code above doesn't return the values of the submitted XML data. Hence, the term Out-of-Band since the exfiltrated data has to be captured using an attacker-controlled server.<br>

For this attack, we will need a server that will receive data from other servers. You can use Python's http.server module, although there are options out there, like Apache or Nginx. Using AttackBox or your own machine, start a Python web server by using the command:</p>

![image](https://github.com/user-attachments/assets/b7d9e9ed-a71f-4c7c-a1b6-7ade0120d921)

<p>Upload a file in the application and monitor the request that is sent to submit.php using your Burp. Forward the request below to Burp Repeater.</p>

![image](https://github.com/user-attachments/assets/aa7916ce-2c43-4214-9e4f-304c21ae7da6)

<p>Using the payload below, replace the value of the XML file in the request and resend it. Note that you have to replace the ATTACKER_IP variable with your own IP.</p>

![image](https://github.com/user-attachments/assets/b221aa20-6bd1-4206-ab50-9bc732ebff0b)

<p>Send the modified HTTP request.</p>

![image](https://github.com/user-attachments/assets/b1ed89d1-ac40-4662-bfbd-60239bdab0ee)

<p>After sending the modified HTTP request, the Python web server will receive a connection from the target machine. The establishment of a connection with the server indicates that sensitive information can be extracted from the application.</p>

![image](https://github.com/user-attachments/assets/fdb2fb1e-240e-44ad-b503-7c137ffd7752)

<p>We can now create a DTD file that contains an external entity with a PHP filter to exfiltrate data from the target web application.<br>

Save the sample DTD file below and name it as sample.dtd. The payload below will exfiltrate the contents of /etc/passwd and send the response back to the attacker-controlled server:</p>

![image](https://github.com/user-attachments/assets/45fd7041-848e-47a5-b9ef-aff2a54c5070)

<h3>DTD Payload Explained</h3>
<p>The DTD begins with a declaration of an entity %cmd that points to a system resource. The %cmd entity refers to a resource within the PHP filter protocol php://filter/convert.base64-encode/resource=/etc/passwd. It retrieves the content of /etc/passwd, a standard file in Unix-based systems containing user account information. The convert.base64-encode filter encodes the content in Base64 format to avoid formatting problems. The %oobxxe entity contains another XML entity declaration, exfil, which has a system identifier pointing to the attacker-controlled server. It includes a parameter named data with %cmd, representing the Base64-encoded content of /etc/passwd. When %oobxxe; is parsed, it creates the exfil entity that connects to an attacker's server (http://ATTACKER_IP:1337/). The parameter ?data=%cmd sends the Base64-encoded content from %cmd.<br>

Go back to the repeater and change your payload to:</p>

![image](https://github.com/user-attachments/assets/be015bdf-3939-47f4-b1dc-cb935d7f92f1)

![image](https://github.com/user-attachments/assets/db35d666-7ebc-446a-ab4d-98c495262e6e)

<p>Resend the request and check your terminal. You will receive two (2) requests. The first is the request for the sample.dtd file, and the second is the request sent by the vulnerable application containing the encoded /etc/passwd.</p>

![image](https://github.com/user-attachments/assets/5c52a2e8-f6e4-424c-9703-7b52f67ba37d)


<p>Decoding the exfiltrated base64 data will show that it contains the base64 value of /etc/passwd.</p>

![image](https://github.com/user-attachments/assets/d91ff244-6083-42f4-af2f-7c3cc461a27e)


<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 5.1. <em>What kind of XXE vulnerability occurs when the response of the server is not visible to the attacker?</em><br><a id='5.1'></a>
>> <strong><code>Out-Band XXE</code></strong><br>
<p><br></p>

<br>
<h2>Task 6.  SSRF + XXE<a id='6'></a></h2>

<p>Server-Side Request Forgery (SSRF) attacks occur when an attacker abuses functionality on a server, causing the server to make requests to an unintended location. In the context of XXE, an attacker can manipulate XML input to make the server issue requests to internal services or access internal files. This technique can be used to scan internal networks, access restricted endpoints, or interact with services that are only accessible from the server’s local network.</p>

<h3>Internal Network Scanning</h3>
<p>Consider a scenario where a vulnerable server hosts another web application internally on a non-standard port. An attacker can exploit an XXE vulnerability that makes the server send a request to its own internal network resource.<br>

For example, using the captured request from the in-band XXE task, send the captured request to Burp Intruder and use the payload below:</p>

![image](https://github.com/user-attachments/assets/23ab7275-22d1-40e5-9d95-ec509e8bfb6b)


<p>The external entity is set to fetch data from http://localhost:§10§/. Intruder will then reiterate the request and search for an internal service running on the server.</p>

<h4>Steps to brute force for open ports:</h4>
<p>1. Once the captured request from the In-Band XXE is in Intruder, click the Add § button while highlighting the port.</p>

![image](https://github.com/user-attachments/assets/f3c2a4f0-5d6d-4890-a3fc-83561f128f4b)


<p>2. In the Payloads tab, set the payload type to Numbers with the Payload settings from 1 to 65535.</p>

![image](https://github.com/user-attachments/assets/1ab76d0c-5d79-419b-9423-d00c0b885b7d)




<p>3. Once done, click the Start attack button and click the Length column to sort which item has the largest size. The difference in the server's response size is worth further investigation since it might contain information that is different compared to the other intruder requests.</p>

![image](https://github.com/user-attachments/assets/f19cd60d-6755-44bc-85de-a8300001673d)

![image](https://github.com/user-attachments/assets/9ab7ed5e-78e0-4596-a8c7-e2c2f7897566)

<h4>How the Server Processes This:</h4>
<p>The entity &xxe; is referenced within the <name> tag, triggering the server to make an HTTP request to the specified URL when the XML is parsed. The response of the requested resource will then be included in the server response. If an application contains secret keys, API keys, or hardcoded passwords, this information can then be used in another form of attack, such as password reuse.</p>

<h3>Potential Security Implications</h3>
- Reconnaissance: Attackers can discover services running on internal network ports and gain insights into the server's internal architecture.<br>
- Data Leakage: If the internal service returns sensitive information, it could be exposed externally through errors or XML data output.<br>
- Elevation of Privilege: Accessing internal services could lead to further exploits, potentially escalating an attacker's capabilities within the network.<br>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<br>

> 6.1. <em>What is the flag in the application running internally?</em><br><a id='6.1'></a>
>> <strong><code>THM{0O8_xx3!!}</code></strong><br>
<p><br></p>


> 6.2. <em>What port is the internal application hosted on?</em><br><a id='6.2'></a>
>> <strong><code>81</code></strong><br>
<p><br></p>



![image](https://github.com/user-attachments/assets/03aae404-ddcb-4500-b328-18bda8fe9fba)

![image](https://github.com/user-attachments/assets/0dd3c60e-caf8-4be7-bcd3-0aacafa76592)

![image](https://github.com/user-attachments/assets/fdea94e3-0063-437b-8af5-ab3c2c9f99ea)

![image](https://github.com/user-attachments/assets/b3d5b48e-1f26-4e47-8daf-8d54ade30c29)

![image](https://github.com/user-attachments/assets/83f29c83-c8ac-467f-8543-542f1cdc0690)

![image](https://github.com/user-attachments/assets/0bc99f7c-f481-45ee-a338-3fa9b1a5e431)


<br>
<h2>Task 7. Mitigation<a id='7'></a></h2>

<h3>Avoiding Misconfigurations</h3>

<p>Misconfigurations in XML parser settings are a common cause of XXE-related vulnerabilities. Adjusting these settings can significantly reduce the risk of XXE attacks. Below are detailed guidelines and best practices for several popular programming languages and frameworks..</p>

<br>
<h3>Avoiding Misconfigurations</h3>
<p>1. Disable External Entities and DTDs: As a best practice, disable the processing of external entities and DTDs in your XML parsers. Most XXE vulnerabilities arise from malicious DTDs.<br>
2. Use Less Complex Data Formats: Where possible, consider using simpler data formats like JSON, which do not allow the specification of external entities.<br>
3. Allowlisting Input Validation: Validate all incoming data against a strict schema that defines expected data types and patterns. Exclude or escape XML-specific characters such as <, >, &, ', and ". These characters are crucial in XML syntax and can lead to injection attacks if misused.</p>

<h3>Mitigation Techniques in Popular Languages</h3>

<h4><bold><em>Java</em></bold></h4>

![image](https://github.com/user-attachments/assets/64bc62ab-e2a1-4df4-937a-a5e5b2fed07e)

<h4><bold><em>.NET</em></bold></h4>
<p>Configure XML readers to ignore DTDs and external entities:</p>

![image](https://github.com/user-attachments/assets/d93a3b44-70ab-4404-b23e-8ef0333606c5)


<h4><bold><em>PHP</em></bold></h4>
<p>Disable loading external entities by libxml:</p>

![image](https://github.com/user-attachments/assets/4d28c27c-2315-4a4e-a192-9b78e48bd92b)


<h4><bold><em>Python</em></bold></h4>
<p>Use <code>defusedxml</code> library, which is designed to mitigate XML vulnerabilities:</p>

![image](https://github.com/user-attachments/assets/e4b06c0a-a14f-48dd-a0ba-8d2f2b3b65a5)

<br>
<h3>Regularly Update and Patch</h3>
<p>- Software Updates: Keep all XML processors and libraries up-to-date. Vendors frequently patch known vulnerabilities.<br>
- Security Patches: Regularly apply security patches to web applications and their environments.</p>

<br>
<h3>Security Awareness and Code Reviews</h3>
<p>- Conduct Code Reviews: Regularly review code for security vulnerabilities, especially code that handles XML input and parsing.<br>
- Promote Security Training: Ensure developers are aware of secure coding practices, including the risks associated with XML parsing.</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 7.1. <em>Click me to proceed to the next task.</em><br><a id='7.1'></a>
>> <strong>No answer needed</strong><br>
<p><br></p>

<br>
<h2>Task 8. Conclusion<a id='8'></a></h2>
<h3>Conclusion</h3>

<p>XXE (XML External Entities) attacks arise from improper handling of user-supplied input in web applications, particularly in XML parsing. Attackers exploit vulnerable XML processors to inject malicious external entities, leading to data exfiltration, server compromise, or denial of service. XXE vulnerabilities can be prevented by disabling external entity expansion, validating user input, and using secure XML parsing libraries. Additionally, implementing security best practices such as input validation, output encoding, and secure coding practices can significantly reduce the risk of XXE attacks. Regular security audits, code reviews, and training on secure development practices are essential for identifying and mitigating XXE vulnerabilities. By understanding the risks and taking proactive measures, developers and administrators can protect their web applications from XXE attacks and ensure the security and integrity of their systems.</p>

<h3>Recap of Key Concepts Covered in the Room</h3>
<p>In this training room, we've covered a comprehensive range of topics related to XXE (XML External Entity) vulnerabilities, which are critical in understanding how these vulnerabilities can impact web security. Here's a quick recap:</p>
<p>- Understanding XML: We explored the basics of XML syntax and structure, including the use of DTDs and how they can be exploited.<br>
- XML Parsing Mechanisms: We discussed different XML parsers and their configurations, emphasizing secure practices.<br>
- Exploiting XXE: Detailed steps were provided to exploit XXE vulnerabilities, ranging from basic data exfiltration to advanced techniques like Out-of-Band XXE.<br>
- XXE+SSRF: We explored the concept of SSRF attacks via XXE for Out-of-Band data exfiltration and how to scan internal networks using this attack.<br>
- Mitigation: Strategies to prevent XXE vulnerabilities were outlined, focusing on avoiding misconfigurations and reinforcing secure coding practices.</p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<br>

> 8.1. <em>I can now exploit XXE vulnerabilities!</em><br><a id='8.1'></a>
>> <strong>No answer needed</strong><br>
<p><br></p>


<h2>Room Complete<a id='9'></a></h2>
<p>Keep learning, keep growing!<br>

![image](https://github.com/user-attachments/assets/1ff83104-d7aa-4f40-af85-cdd9b9278b38)

<br>

![image](https://github.com/user-attachments/assets/5c84bdf2-ce9e-402d-856d-3d517f8e4a9e)

<br>

<h2>My Journey<a id='10'></a></h2>
<p></p>Following I share the status of my journey in TryHackMe.</p>

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     |
| :---------------: | :------- | :----------- | :----------- | :---------- | :--------- | :------  | :-------- |
|                   |          | WorldWide    | Brazil       | WorldWide   | Brazil     |          | Completed |
| November 20, 2024 | 198      |       1,207ª |          25ª |      5,539ª |        73ª | 55,640   |       422 |

![image](https://github.com/user-attachments/assets/0272c596-24ba-4875-b56a-a8aa8ff43f91)

<br>

<p style="text-align: center;">Thank you for coming. Hope to learn together again!!</p>
