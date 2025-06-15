<h1 align="center">Custom Tooling using Burp</h1>
<p align="center"><img width="180px" src="https://github.com/user-attachments/assets/a74da0a4-04dc-432a-add8-95a9454fd5ef"><br>
Jun 1, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my 391-day-streak in  <a href="https://tryhackme.com">TryHackMe</a><br>
Creating custom tooling for application testing using Burp Plugins. Access it clicking <a href="https://tryhackme.com/room/customtoolingviaburp"</a>here.<br><br>
<img width="1000px" src="https://github.com/user-attachments/assets/d09f4ae6-96e4-4dbe-8ec3-3d4b25de796d"></p>

https://github.com/user-attachments/assets/d09f4ae6-96e4-4dbe-8ec3-3d4b25de796d

https://github.com/user-attachments/assets/971a1553-af84-4268-8d87-52bdecbd7504


<br>
<br>

<h2>Task 1 . Introduction</h2>

<p>The ability to create your own custom tooling is critically important for web application red teaming. Rarely will you be able to find a tool or plugin that will do exactly what you need. This then calls for you to develop custom tooling! This custom tooling module will showcase different ways you can approach this problem. Each option is unique and has its benefits and drawbacks.

<br>
<br>
In this room, we will focus on using <code>Burp</code> plugins to create tools and exploit them. Burp acts as an intercepting proxy, allowing you to view and modify requests and responses as the web application interfaces with it. Burp has several features, such as repeating requests or performing automated brute forcing of specific requests and payloads. This makes plugins a unique option when you need additional versatility in your tooling to be used in an automated and manual fashion. While we will showcase using Burp plugins in this room, the principles can be applied to any intercepting proxy you choose. Let's dive in and use Burp plugins to create our very own custom tools and exploits!</p>

<br>

<h3 align="left">Answer the question below</h3>


> 1.1. <em>I am ready to learn about creating custom Burp plugins!</em><br><a id='1.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<p></p>

<br>
<br>

<h2>Task 2 . Using a Proxy for Custom Tooling</h2>
<h3>Why Create Your Own Tools?</h3>

<p>[ ... ]</p>

<h3>Custom Crypto Cryptonite</h3>

<p>[ ... ]</p>

<h3>Interesting Intercepting Proxies and Where to Find Them</h3>

<p>[ ... ]</p>

<h3>Beautiful Burp</h3>

<p>[ ... ]</p>

<br>

<h3 align="left">Answer the questions below</h3>


> 2.1. <em>Which intercepting proxy currently only has support for Windows?</em><br><a id='2.1'></a>
>> <strong><code>Fiddler</code></strong><br>
<p></p>

<br>

> 2.2. <em>Which intercepting proxy allows us to write plugins using TypeScript?</em><br><a id='2.2'></a>
>> <strong><code>Caido</code></strong><br>
<p></p>

<br>

> 2.3. <em>Which intercepting proxy allows plugins to be written in the most amount of different coding languages?</em><br><a id='2.3'></a>
>> <strong><code>Burp</code></strong><br>
<p></p>


<br>
<br>

<h2>Task 3 . Using Extensions in Burp</h2>
<p>In this task, we will explore Burp extensions and how they ease a pentester’s job by automating routine tasks. Burp offers built-in extensions that enhance basic security testing capabilities, such as logging, request/response modification, and simple automation. Some of the extensions are available for free, while a few require Burp Professional.</p>

<h3>Playing with Extensions</h3>
<p>In the attached VM, click on the <code>Burp</code> icon on the left pane to open the Burp Sutie Community Edition. Once Burp is open, click on the <code>Extension</code> tab and then click on the <code>BApp Store</code> to view multiple extensions offered by Burp and uploaded by community users worldwide. </p>

<br>

![image](https://github.com/user-attachments/assets/65094468-a106-4d2c-8f1c-e0e6e152f6d4)

<br>

<p>In this task, we will install the famous extension <code>Decoder Improved</code>, which allows for the encoding and decoding of URLs and HTML, and hashing of input. This extension comes in handy when you are dealing with a complex web application that has incorporated multiple encoding mechanisms; therefore, instead of using any other application or custom script, you can simply use this extension to perform decoding. 

<br>
<br>

In the list of available extensions, find <code>Decoder Improved</code> and you will find the <code>Install</code> button on the right side to install it (Do not click the button yet), as shown below:</p>

<br>

![image](https://github.com/user-attachments/assets/1d721d88-ce2c-4183-ba5e-d22320a123a6)

<br>

<p>Note: Since the attached VM is not connected to the internet, we will install the extension in offline mode. However, on an internet-connected machine, you can simply click the Install button to install the extension directly.<br><br>

On the same screen, click the Manual Install button as shown below, and select the Decoder-Improved.bapp file from /home/ubuntu/lib, as shown below:</p>

<br>

![image](https://github.com/user-attachments/assets/813c5ee0-3015-4176-9760-5bdfd16e3766)

<br>

<p>Once the installation is complete, a new tab will appear, allowing you to access the extension's features.<br><br>

Now, let's explore the Decoder Improved extension and use it to Base64 encode a simple string. First, navigate to the Decoder Improved tab to access the extension's GUI. On the right side, select the Text (1) radio button, then choose Encode as (1) from the dropdown menu and select Base64 (1) as the encoding option. In the upper window, on the left side, enter TryHackMe (2), and the extension will automatically generate the Base64-encoded output in the bottom window, as shown below:</p>

<br>

![image](https://github.com/user-attachments/assets/87f43311-46b6-4754-9043-15f7f2b705c1)

<br>

<p>This is a simple demonstration of how extensions help a pentester ease routine tasks. Burp offers a variety of other extensions, such as Hackvertor, Logger++, XSS Validator, Turbo Intruder and many more, to enable automation and custom tooling.</p>

<br>

<h3 align="left">Answer the questions below</h3>


> 3.1. <em>What is the decoded value for the string VEhNezEwMUJ1cnB9?</em><br><a id='3.1'></a>
>> <strong><code>THM{101Burp}</code></strong><br>
<p></p>

<br>


> 3.2. <em>Does Burp only offer paid extensions developed by users worldwide? (yea/nay) </em><br><a id='3.2'></a>
>> <strong><code>nay</code></strong><br>
<p></p>

<br>

![image](https://github.com/user-attachments/assets/64919d82-4cc3-4a65-a66b-dd19a3409d2b)

<br>

![image](https://github.com/user-attachments/assets/5ccbec4b-70de-426f-bca3-ed8a4e253f62)

<br>

![image](https://github.com/user-attachments/assets/5bfbecbd-e4be-416c-82d9-58bfaa44e03b)

<br>
<br>

<h2>Task 4 . Creating a Basic Burp Extension</h2>
<p>Now that we understand how Burp extensions work, we will create a simple Burp extension to enable automation while pentesting a website. In this task, we will bypass authentication against a website hosted on https://SECOND_VM_IP:8443, as shown below:</p>

<br>

![image](https://github.com/user-attachments/assets/dcfe5017-4fe5-47ba-aa6b-e8c077c281bf)

<br>

<p>During the reconnaissance phase, we found that ecorp_user is the username for the website, and the password contains 4 digits, which means the correct password lies in the range of 0000 and 9999. However, during source code analysis, we noticed that username and password are not being sent directly to the /login endpoint; rather, they are being encrypted/encoded before submission. By analysing the client-side script at https://SECOND_VM_IP:8443/static/form-submit.js, we see that the code generates an AES key, encrypts the username and password, and then encodes the data before sending the request.
<br>
<br>

The following JS snippet shows how the web application encrypts credentials before sending them:</o>

<p>[ ... ]</p>

<br>

<h3 align="left">Answer the questions below</h3>


> 4.1. <em>What is the password for the user ecorp_user?</em><br><a id='4.1'></a>
>> <strong><code>0007</code></strong><br>
<p></p>

<br>

> 4.2. <em>What is the name of the function that performs brute forcing in the Burp extension?</em><br><a id='4.2'></a>
>> <strong><code>startBruteForce</code></strong><br>
<p></p>

<br>

<p>SecondTargetIP:8443</p>

<br>

![image](https://github.com/user-attachments/assets/e9bfe57d-d8f5-4ca8-a944-9598d9938595)


<br>

![image](https://github.com/user-attachments/assets/feaa369c-ffec-4e2d-9ebe-ebd9cb6105ff)

<br>


![image](https://github.com/user-attachments/assets/1a2b1166-8239-4f13-887d-7283e122742d)

<br>

<p>Viewed Page Source.<br><br>
static/form-submit.js</p>

<br>

![image](https://github.com/user-attachments/assets/66cd24f5-4c1e-4e95-a2b5-bdb5537d112c)


<br>

<p>Navigated to <code>https://SecondTargetIP:8443/static/form-submit.js</code></p>

<br>


```bash
const form = document.querySelector('#login-form');
const enc = new TextEncoder()

function str2ab(str) {
    const buf = new ArrayBuffer(str.length);
    const bufView = new Uint8Array(buf);
    for (let i = 0, strLen = str.length; i < strLen; i++) {
      bufView[i] = str.charCodeAt(i);
    }
    return buf;
}

async function getSecretKey(key) {
    return await window.crypto.subtle.importKey("raw", key, "AES-CBC", true,
        ["encrypt", "decrypt"]
    );
}

async function encryptMessage(key, message) {
	console.log(key);
	console.log(message);
    iv = enc.encode("0000000000000000").buffer;
    return await window.crypto.subtle.encrypt(
      {
        name: "AES-CBC",
        iv
      },
      key,
      message
    );
}

async function decryptMessage(key, message) {
    iv = enc.encode("0000000000000000").buffer;
    return await window.crypto.subtle.decrypt(
      {
        name: "AES-CBC",
        iv
      },
      key,
      message
    );
}

form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const formData = (new FormData(form));
    const formDataObj = {};
    formData.forEach((value, key) => (formDataObj[key] = value));
    console.log(formDataObj)

    const rawAesKey = window.crypto.getRandomValues(new Uint8Array(16));
    const aesKey = await getSecretKey(rawAesKey)
    console.log(aesKey)
    let rawdata = "username=" + formDataObj["username"] + "&password=" + formDataObj["password"]
    let data = window.btoa(String.fromCharCode(...new Uint8Array(await encryptMessage(aesKey, enc.encode(rawdata).buffer))))

    const response = await fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
        },
        body: "mac=" + encodeURIComponent(window.btoa(String.fromCharCode(...rawAesKey))) + "&data=" + encodeURIComponent(data)
    });
    if (response.ok && response.status == 200 && (await response.text()).startsWith("result=")) {
        window.location.href = '/authenticate';
    } else {
        alert('Login failed');
    }
});
```

<br>

![image](https://github.com/user-attachments/assets/3ab3b5c2-0306-4f32-842d-5094287f2508)

<br>

```bash
const rawAesKey = window.crypto.getRandomValues(new Uint8Array(16));
    const aesKey = await getSecretKey(rawAesKey)
    console.log(aesKey)
    let rawdata = "username=" + formDataObj["username"] + "&password=" + formDataObj["password"]
```


<br>

<p>- Typed <code>code</code> in a terminal in the <code>CustomTooling-Buro.v.1.8 VM</code>.<br><br>
- Launched <code>VS Code Editor</code>.<br><br>

![image](https://github.com/user-attachments/assets/c8b927c5-f159-42a8-a432-ebc6a690ec05)

<br>

 
- Clicked <code>101Burp</code> > <code>src</code> > <code>main</code> > <code>java</code> > <code>BruteForce.java</code>.<br><br>

![image](https://github.com/user-attachments/assets/206e3da8-8eee-424b-bde6-63132e847d58)

<br>

- Ran <code>cd ~/101Burp/</code>code>.<br><br>

![image](https://github.com/user-attachments/assets/0ef1a435-9d6f-4eaf-9ccd-748d9b805ae8)

<br>

- Ran <code>gradle build</code>code>.

![image](https://github.com/user-attachments/assets/a139a821-72a4-44e2-8bcd-2e9bd678fc0f)

<br>

- Launched <code>Burp Suite</code>.<br><br>
- Clicked <code>Extensions</code> > <code>Add</code> > <code>Select file ...</code> > <code>/101Burp/build/libs/101Burp-1.0-SNAPSHOT.jar</code> > <code>Open</code>.<br><br>

![image](https://github.com/user-attachments/assets/0c1c38f6-dd16-448f-a1c4-1acff2c3ffe1)

<br>


- Clicked <code>Next</code>.<br><br>

![image](https://github.com/user-attachments/assets/a8fb40dc-7ee3-4f99-b3c2-fa197e765583)

<br>

- Clicked <code>this room</code> and started the second VM.<br><br>
- Second_IP is the second VM IP in my hands-on.<br><br>
- Typed <code>ecorp_user</code> for username, and the IP mentioned above followed by :8443.<br><br>

![image](https://github.com/user-attachments/assets/b351e886-a18b-4897-9c3a-26d36deb62a7)

<br>

- Clicked <code>Start Attack</code>.<br><br>
- <code>Brute Force Success</code>: <code>0007</code>.<br><br></p>

![image](https://github.com/user-attachments/assets/3b38d91b-601e-4266-baec-e91d3c5cb1cc)




```bash
Decryption Success: Welcome NFT member! Your secret code is THM{Breaking.Custom.Crypto.Is.Fun}. Your NFT wallet private key is: HOLD
Brute-force complete!
```

<br>
<br>


<h2>Task 5 . Modifying a Burp Extension</h2>

<br>
<br>

![image](https://github.com/user-attachments/assets/1777a0b0-ee34-46f6-9117-00d91b388553)


<br>

![image](https://github.com/user-attachments/assets/4159f3bf-86bb-4f4c-b033-6f1bfb06224f)


<br>


![image](https://github.com/user-attachments/assets/ceedb8c8-aee7-4509-8580-7ec7828e9527)

<br>


![image](https://github.com/user-attachments/assets/31b560fc-c974-401b-a00f-4bdd2c15e283)

<br>

![image](https://github.com/user-attachments/assets/fe8a37d6-01d1-4813-9857-613ef57d407f)

<br>

![image](https://github.com/user-attachments/assets/d600f78c-7f62-4961-a6e8-0baedd023924)


<br>
<br>

![image](https://github.com/user-attachments/assets/24e1243f-1861-418a-afa4-452b95c738d2)


<br>

![image](https://github.com/user-attachments/assets/59957c63-783a-4dc2-a5b9-31e16e470187)

<br>

![image](https://github.com/user-attachments/assets/a0005053-3699-4f5f-b73c-ff109efa1b62)

<br>

![image](https://github.com/user-attachments/assets/0cbf0d1d-79cb-4776-a91d-002efb8977bb)

<br>

![image](https://github.com/user-attachments/assets/a1c06e8e-95a2-4457-8aab-d65d659a6338)


<br>

![image](https://github.com/user-attachments/assets/c38730d4-ede9-4b3f-a9ea-4e652a73aeac)


<br>

<p>Secret was accepted and verified!</p>

![image](https://github.com/user-attachments/assets/ab00df1b-0373-46a5-bccf-4dbb18f8087f)


<br>

![image](https://github.com/user-attachments/assets/90175d17-5879-404c-826a-2f9ddf13eee9)

<br>


![image](https://github.com/user-attachments/assets/fcda5e66-cf4a-4b37-a543-6733b7a32eb1)

<br>

![image](https://github.com/user-attachments/assets/af595af9-3c76-4ed0-a019-d3f0d45e0c41)


<h2>Task 6 . Challenge</h2>

<h2>Task 7 . Conclusion</h2>
<h3>Mastering Plugins and Proxies</h3>
<p>Custom plugins within intercepting proxies are an essential skillset for any red teamer dealing with mobile applications or complex client-side protections. When traditional tools fall short due to custom cryptography or application hardening, custom plugins give you the power to intercept, decrypt, and modify requests and responses in real-time.
<br>
<br>


In this room, we explored why intercepting proxies like Burp Suite are so valuable—especially when paired with custom logic designed to reverse engineer and bypass protections. Rather than building an exploit from scratch, the goal here was to enable visibility and control, allowing your existing red teaming tools and techniques to shine.
<br>
<br>

Whether you're decrypting payloads, injecting modified parameters, or simply trying to understand how an application communicates with its API, building plugins directly into your proxy gives you a tactical advantage that can’t be overstated.
<br>
<br>

By combining solid intercepting proxy knowledge with scripting or plugin development skills, you'll be better equipped to deal with hardened applications, extract hidden data, and bypass defences—putting you one step ahead in any red team engagement.</p>

<br>

<h3 align="left">Answer the questions below</h3>


![image](https://github.com/user-attachments/assets/6f62b9ce-37c6-4f8e-acb3-98c1acf9bc3f)


![image](https://github.com/user-attachments/assets/0c2cc433-8e84-4c0c-b900-f4a824edf2f6)


![image](https://github.com/user-attachments/assets/d4ee3b72-9d51-4e8b-bce2-56d90b81a3bd)

![image](https://github.com/user-attachments/assets/8a13fb0a-7558-4ad6-9082-7a057b55fdb0)

![image](https://github.com/user-attachments/assets/dfe65d29-3704-4c81-9f7a-bb0547b3555a)

<br>
<br>

![image](https://github.com/user-attachments/assets/e3c01c94-d098-45dc-b6dc-43058542c4db)

<br>


![image](https://github.com/user-attachments/assets/53031ae0-e4f9-43f9-9a72-a2b2a12ff533)

<br>


![image](https://github.com/user-attachments/assets/fa5e43c0-8164-4a94-b891-38242688a33f)

<br>

![image](https://github.com/user-attachments/assets/d49db1b3-6f78-47fd-b7c1-e5067aa9a289)


<br>

![image](https://github.com/user-attachments/assets/4af21287-c969-418f-af16-c64a9cff5e4b)








