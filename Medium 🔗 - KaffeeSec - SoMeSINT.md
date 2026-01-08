<h1 align="center">KaffeeSec - SoMeSINT</h1>
<p align="center">2026, January 8 &nbsp; .  &nbsp; Hey! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>! Let´s learn together. Access this walkthrough room <a href="https://tryhackme.com/room/somesint">here</a>.<br><br><img width="1200px" src="https://github.com/user-attachments/assets/fdac9f63-4682-412c-a56e-6fb2e5bcb248"></p>


<br>
<h2>Task 1 . Overview</h2>
<p>In this room, you will be learning social media analysis and forensics. You will learn about google dorking, website archiving, social media enumeration/analysis, and the basic usage of OSINT techniques in the context of social media investigation. You don't need any previous knowledge of OSINT to do well in this room, but it definitely helps. I have included some resources in the " Resources " task at the bottom of the room that I encourage you to check out after completing this room!</p>

<h3>Prerequisites</h3>
<p>

- Critical Thinking.<br>
- A love ogf going deep into rabbit-holes<br>
- Basic understand of Google<br>
- Python 3.7+</p>

<p>When you have completed this room, you should be comfortable applying tools and methodologies to gather information through social media, and answer context-based questions concerning social media. The goal of this room is to prepare you for CTF challenges in this category, as well as real-world research. All tools in this room are optional, as you could technically get all of the information you need through a web browser and methodologies; however, the tools mentioned will make this room much more beginner-friendly.<br>

Sometimes, you will come across a question that requires a flag format.<br>

The format for this room's flags is ks{flag} . Flags are not case-sensitive but must be spelt right (copy/paste).<br>

At any point along the way, you can ask for help in the <a href="https://discord.gg/yURS99AjEg">TryHackMe Discord</a> (in the #room-help channel).<br>

Any and all feedback is also welcome in the <a href="https://discord.gg/mVWYwmj">KaffeeSec</a> discord server.</p>

<p><em>Answer the question below</em></p>

<p>1.1. <em>I fully read and understand the overview, and understand flag format</em><br>
<code>No answer needed</code></p>

<br>
<h2>Task 2 . Story</h2>
<h3>Background Information:</h3>
<p><em>You are Aleks Juulut, a private eye based out of Greenland. You don't usually work digitally, but have recently discovered OSINT techniques to make that aspect of your job much easier. You were recently hired by a mysterious person under the moniker "H" to investigate a suspected cheater, named Thomas Straussman.<br>

After a brief phone-call with his wife, Francesca Hodgerint, you've learned that he's been acting suspicious lately, but she isn't sure exactly what he could be doing wrong. She wants you to investigate him and report back anything you find. Unfortunately, you're out of the country on a family emergency and cannot get back to Greenland to meet the deadline of the investigation, so you're going to have to do all of it digitally. Good luck!</em></p>

<p><em>Answer the questions below</em></p>

<p>2.1. <em>Who hired you?</em><br>
<code>ks{H}</code></p>

```bash
... recently hired by a mysterious person under the moniker "H" ...
```

<br>
<p>2.2. <em>Who are you investigating? (ks{firstname lastname})</em><br>
<code>ks{thomas straussman}</code></p>

```bash
... to investigate a suspected cheater, named Thomas Straussman.
```

<br>
<h2>Task 3 . Let´s get started!</h2>
<h3>Prerequisites:</h3>
<p>

- Patience, curiosity, and a passion for digging into rabbit holes.<br>
Firefox, Chrome, or another chromium-based browser (I recommend Brave).</p>

<p>How exciting! Through talking to people who know Thomas, you've found out that he has a very guessable online handle: <code>tstraussman</code>. With this handle, we can find his social media accounts, and start off this room.<br>

The overall process for finding information from social media accounts starts with finding the social media accounts themselves. Finding social media accounts from names or emails can be automated through a process called enumeration. This is usually done with CLI tools or scripts, but you can get similar effects with Google dorking. <a href="http://tryhackme.com/room/googledorking">Here</a> is a room on Google dorking; it's great reading material before you attempt this task and also includes a cheat sheet that comes in handy.<br>

<em><strong>Disclaimer</strong>: Before starting, I will preface this by saying the only places these accounts are found on are Twitter and Reddit. Please do not try to investigate further out-of-scope, as you will both meet a dead end and be snooping on accounts not involved with this CTF at all. I am not responsible for any actions/interactions made with an account outside of the sockpuppets created for this CTF. As a general rule, we're collecting PASSIVE information - there's no interacting directly with these accounts</em>.</p>

<p><em>Answer the questions below</em></p>

<p>3.1. <em>What is Thomas' favorite holiday?</em> Hint: Bio.<br>
<code>Christmas</code></p>

<img width="1268" height="364" alt="image" src="https://github.com/user-attachments/assets/374f9c2c-cad6-41a3-94f5-0691fea78cd0" />

<br>
<br>

<img width="1334" height="490" alt="image" src="https://github.com/user-attachments/assets/b1a1416c-35a5-4360-b120-ed3b77c085a5" />

<br>
<br>

<img width="1207" height="771" alt="image" src="https://github.com/user-attachments/assets/d689dd5f-f0ad-421e-922d-c4f2f3b90900" />

<br>
<br>
<br>
<p>3.2. <em>What is Thomas' birth date?</em> Hint: Tstraussman was very eager to celebrate his birthday on Reddit. Try looking at the source of the page if you can't find it out any other way. Format is MM-DD-YYYY<br>
<code>12-20-1990</code></p>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/31f49ae6-8e1c-48a4-866d-d9dad6633c2d"><br>Rosana´s hands-on</h6>

<p>Use <a href="https://trevorfox.com/reddit-post-date-finder/">TrevorFox</a> to discover the date of <code>Tstraussman</code> post on <strong>Reddit</strong>.</p>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/dc666b53-cd81-4ea8-9f29-33f27807e03c"><br>Rosana´s hands-on</h6>

<p>Or simply hover over the post title.</p>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/388998b4-b826-4170-a2c6-3751d099a043"><br>Rosana´s hands-on</h6>

<p>Subtract 30 years.</p>

<br>
<p>3.3. <em>What is Thomas' fiancee's Twitter handle?</em> Hint: Don't forget the @.<br>
<code>@fhodgelink</code>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/6db23343-ff6a-4dbf-ac2c-47a662610030"><br>Rosana´s hands-on</h6>

<br>
<p>3.4. <em>What is Thomas' background picture of?</em> Hint: Icon of a certain East Asian religion.<br>
<code>Buddha</code></p

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/af88ac99-42d2-46dd-886b-7fe8508641d8"><br>Rosana´s hands-on</h6>

<br>
<h2>Task 4 . Spider... what?</h2>
<h3>Requirements:</h3>
<p>

- Spiderfoot<br>
- Python 3<br>

First things first, make sure that you've downloaded the latest version of Python 3 . Then follow this guide to install the latest version of Spiderfoot (currently v3.3).</p>

<p> [ Video ] </p>

<p>Once it's installed correctly, run it by typing <code>python3 sf.py -l 127.0.0.1:5001</code>.<br>

You can access the web interface by navigating to <code>localhost:5001</code> in your browser.</p>

<p> [ Video ] </p>

<p>Click on "New Scan". In the "Scan Target" field, type in "Thomas Straussman" or "tstraussman"; then, under <code>By Use Case</code>, ensure that you checked the <code>All</code> option. Finally, press run.<br>

Looking at the results, you can figure out which are false positives by filtering out anything that isn't related to <code>Reddit</code> or <code>Twitter</code>.<br>

If you find a Twitter account that leads to <code>shadowban.eu</code>, click on the link.<br>

If you can't find anything related to Twitter, go to <code>Settings --> Account Finder</code> and set the highlighted option to <code>False</code>.</p>

<h6 align="center"><img width="800px" src="https://github.com/user-attachments/assets/0a121a2e-7c1b-4bfe-b584-9be2252373ad"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>


<p>After checking to see if the account exists, you can search their username on twitter (or go to <code>twitter.com/[username]</code>).</p>

<p><em>Answer the questions below</em></p>

<p>4.1. <em>What was the source module used to find these accounts?</em> Hint: Third column<br>
<code>sfp_accounts</code></p>

```bash
:/opt# git clone https://github.com/smicallef/spiderfoot.git
```

```bash
:/opt/spiderfoot# pip3 install -r requirements.txt --ignore-installed
```

```bash
:/opt/spiderfoot# ls
correlations             Dockerfile            LICENSE           setup.cfg  sfscan.py   THANKYOU
docker-compose-dev.yml   Dockerfile.full       modules           sfcli.py   sfwebui.py  VERSION
docker-compose-full.yml  docs                  README.md         sflib.py   spiderfoot
docker-compose.yml       generate-certificate  requirements.txt  sf.py      test
```

```bash
:/opt/spiderfoot# python3 sf.py -l 127.0.0.1:5001
```


<img width="889" height="267" alt="image" src="https://github.com/user-attachments/assets/c86a2166-e1b2-4dc0-b109-01fdf0a79ef1" />



<img width="983" height="343" alt="image" src="https://github.com/user-attachments/assets/0f0b0092-f8cf-4892-ab80-64b2659ee49f" />


<img width="981" height="766" alt="image" src="https://github.com/user-attachments/assets/ad04d136-69bd-48b7-a280-38d1cce5d410" />


<img width="972" height="506" alt="image" src="https://github.com/user-attachments/assets/68d979f0-bafa-4ea0-ab28-38d01ea13d86" />


<img width="972" height="681" alt="image" src="https://github.com/user-attachments/assets/b47260b1-cbc2-4263-80cd-5a3267195ba4" />

<img width="973" height="405" alt="image" src="https://github.com/user-attachments/assets/8b78e1e1-ed14-41df-a318-df62f5572f77" />


```bash
:~/KaffeeSec/spiderfoot-4.0# python3 ./sf.py -l 127.0.0.1:5001
```


 
<br>
<p>4.2. <em>Check the shadowban API. What is the value of "search"?</em> Hint: Flag format "tests": {"search": "COPYME"}<br>
<code>ks{1346173539712380929}</code></p>



<img width="1042" height="380" alt="image" src="https://github.com/user-attachments/assets/2593320c-519a-4680-92b9-5a4d563851a2" />

<img width="1063" height="542" alt="image" src="https://github.com/user-attachments/assets/42366de7-62df-4471-bfd3-4a86740d3bf9" />

<img width="1331" height="297" alt="image" src="https://github.com/user-attachments/assets/cb1bf1d3-56d0-4036-a563-f7f4c5daa938" />




<br>
<h2>Task 5 . Connections, connections..</h2>
<p>Now that you have Thomas' Reddit and Twitter accounts, you can do some cool stuff!<br>

At this point, consider downloading a reverse search extension for your browser, my favorite is RevEye, which lets you choose from a handful of great reverse search engines, or use all of them simultaneously.<br>

<a href="https://chrome.google.com/webstore/detail/reveye-reverse-image-sear/keaaclcjhehbbapnphnmpiklalfhelgf">Chrome</a> / <a href="https://addons.mozilla.org/en-US/firefox/addon/reveye-ris/">Firefox</a><br>

There are a few key types of information that we want to find from socials:<br>

- Images of places that contain clear identifiers like buildings, signs, monuments, or landmarks (For IMINT/GEOMINT purposes).<br>
- Clear images of the subject's face (For reverse image searches and possibly finding more accounts/sources of info).<br>
- Clear images of the subject in a group of people (Family photos, friend groups, other information that can give context to their relationship with the group).<br>
- Personal information in their bio, or other personal data from their profile itself (Where they grew up, currently live, went to school, etc..).<br>
- Relevant posts that may contain information on their whereabouts or personal habits (Do they smoke? Drink? Go to bars often? Love to vacation to specific places? All this information can help in an investigation.)<br>

Since you have gotten most useful information from Thomas' Twitter, it's time to "pivot" to his fiancee's account.<br>

What personal information can you find?<br>

NOTE: If you get stuck on the first flag, consider two things:<br>

- You can reverse image search landscapes / locations and most likely get a result.<br>
- You can look at the source of the website (ctrl + shift + c, then click on the image) and try to find some metadata from the image.</p>

<p><em>Answer the questions below</em></p>

<p>5.1. <em>Where did Thomas and his fiancee vacation to?</em> Hint: Format is: City, Country<br>
<code>Koblenz, Germany</code></p>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/02facd21-ca47-431c-8996-296f4f0b9182"><br>Rosana´s hands-on</h6>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/17f4ad31-e0f8-40e1-88a6-6be386852737"><br>Rosana´s hands-on</h6>


<br>
<p>5.2. <em>When is Francesca's Mother's birthday? (without the year)</em> Hint: Month XXth<br>
<code>December 25th</code></p>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/7a937d22-68d6-4153-ae8b-d4eb024e3187"><br>Rosana´s hands-on</h6>

<br>
<p>5.3. <em>What is the name of their cat?</em><br>
<code>Gotank</code></p>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/988932e4-2140-4ad7-a02f-a03e5d4662e6"><br>Rosana´s hands-on</h6>

<br>
<p>5.4. <em>What show does Francesca like to watch?</em><br>
<code>90 Day Fiancee</code></p>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/1c332553-f468-43ea-a512-6d1fce5c6c4f"><br>Rosana´s hands-on</h6>




<br>
<h2>Task 6 . Turn back the clock!!</h2>
<p>Now that we've gathered intel from Thomas and Francesca's Twitters, lets move to another platform - Reddit.<br>

For the sake of this investigation, we're going to be using Reddit in two different ways:<br>

- Use the old version (http://old.reddit.com/) for wayback machine purposes<br>
- Use the new version (https://www.reddit.com/) for other purposes (later on)<br>

First, you're going to want to install the <strong>WayBackMachine</strong> extension for your browser (you don't need it, but it'll make your life much easier).<br>

- Get it for <a href="https://addons.mozilla.org/en-US/firefox/addon/wayback-machine_new/">Firefox</a><br>
- Get it for <a href="https://chrome.google.com/webstore/detail/wayback-machine/fpnmgdkabkmnadcjpehmlllkndpkmiak?hl=en-US">Chrome</a><br>

Using Reddit's old site, navigate to Thomas' profile. Right click anywhere on the page and click on Wayback machine --> All Versions. You will see a calendar that shows all of the saved versions of the site, click through and take a look at each saved version (in this case there should be none).<br>

So it hasn't been saved yet... Nothing out of the ordinary, right?<br>

Next, go to Thomas' birthday post. Repeat the steps to find the first version of the site and..... Voila!<br>

We've discovered a coworker, which is another source of intel for us! But the question is... <strong><em>how much</em></strong> intel?</p>

<p><em>Answer the questions below</em></p>

<p>6.1. <em>What is the name of Thomas' coworker?</em> Hint: Format: Firstname Lastname<br>
<code>Hans Minik</code></p>


<img width="1062" height="603" alt="image" src="https://github.com/user-attachments/assets/26cafc0a-c13c-4896-a127-960b3d9ad16a" />


<br>
<br>
<br>
<p>6.2. <em>Where does his coworker live?</em> Hint: Format: City, Country<br>
<code>Nuuk, Greenland</code></p>

<img width="1014" height="630" alt="image" src="https://github.com/user-attachments/assets/4a89829a-6a5b-4940-8dc7-72f4878487e0" />


<img width="899" height="310" alt="image" src="https://github.com/user-attachments/assets/7efbd7bf-7a2f-40ef-a32a-f5b8332a4947" />


<img width="1318" height="427" alt="image" src="https://github.com/user-attachments/assets/115e9a96-3d1b-4b19-9dc5-1b086b7b39d9" />

<br>
<br>

<br>
<p>6.3. <em>What is the paste ID for the link we found? (flag format)</em> Hint: Stuck? Didn't find the link yet? - Did you use wayback machine on Hans' profile? If so, did you only look at the first saved version? Did you look at the Electric Boogaloo? If you have the link: - the flag is the string after the last / of the URL.<br>
<code>ks{ww4ju}</code></p>


<img width="1059" height="355" alt="image" src="https://github.com/user-attachments/assets/689888cc-b30c-4a05-9506-fd47eef058be" />

<img width="1057" height="356" alt="image" src="https://github.com/user-attachments/assets/6fee5b13-1eb7-461d-9d40-58c4dfadb417" />

<img width="1057" height="356" alt="image" src="https://github.com/user-attachments/assets/eca78c75-cbc8-4478-b9fc-b7ee8c98b8ea" />






<br>
<br>
<br>
<p>6.4. <em>Password for the next link? (flag format)</em> Hint: It's at the bottom of the paste :)<br>
<code>ks{1qaz2wsx}</code></p>

<img width="1821" height="738" alt="image" src="https://github.com/user-attachments/assets/8aa5535e-d103-4774-abfe-3726274e0c07" />

<br>
<br>
<br> 
<p>6.5. <em>What is the name of Thomas' mistress?</em> Hint: Format: Firstname Lastname<br>
<code>Emilia Moller</code></p>


<p>https://web.archive.org/web/20210323231456/https://ghostbin.com/paste/ww4ju</p>

<img width="1898" height="608" alt="image" src="https://github.com/user-attachments/assets/c4dadb65-ff9b-4e19-aefc-ff2a92aa3a20" />

<img width="1062" height="219" alt="image" src="https://github.com/user-attachments/assets/fd040a23-2582-4f9f-a7bd-6c7d0ded30db" />

<img width="1063" height="534" alt="image" src="https://github.com/user-attachments/assets/c37c0367-b4ad-4934-baab-ecb2a2898b5f" />


<br>
<br>
<br> 
<p>6.6. <em>What is Thomas' Email address?</em> Hint: Format: johndoe@example.com<br>
<code>straussmanthom@mail.com</code></p>

<img width="1327" height="444" alt="image" src="https://github.com/user-attachments/assets/c4950824-8c35-4bde-8286-178510c21c04" />



<br>
<h2>Task 7 . Resources</h2>
<p>Congrats on making it here! Below are a few resources that I encourage you to try after completing this room:<br>

Other TryHackMe Rooms:<br>

- <a href="https://tryhackme.com/room/searchlightosint">SearchLight IMINT</a><br>
- <a href="http://tryhackme.com/room/googledorking">Google Dorking</a><br>

Fancy some more challenges? Check out these CTFs:<br>

- <a href="https://ctf.cybersoc.wales/challenges">CyberSoc</a><br>
- <a href="https://sourcing.games/">Sourcing Games</a></p>

<p><em>Answer the questions below</em></p>

<p>7.1. <em>I´ll check these out!</em><br>
<code>No answer needed</code></p>

<br>
<p>7.2. <em>Hi Jayy#6024</em><br>
<code>No answer needed</code></p>

<br>
<br>
<h1 align="center">Completed</h1>

<p align="center"><img width="700px" src="https://github.com/user-attachments/assets/87af83e8-a57e-4894-810d-66adc7236928"><br>
                  <img width="700px" src="https://github.com/user-attachments/assets/98a62cc1-021d-4216-8b60-df1dd10ebc06"></p>




<h1 align="center">My TryHackMe Journey ・ 2026, January</h1>

<div align="center"><h6>

| Date<br><br>   | Room <br><br> |Streak<br><br>   |Global<br>All Time|Brazil<br>All Time|Global<br>Monthly|Brazil<br>Monthly|Points<br><br>|Rooms<br>Completed|Badges<br><br>|
|:------:|:--------------------------------------|:--------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|
|8      |Medium 🔗 - KaffeeSec - SoMeSINT      |7 |     98ᵗʰ  |     3ʳᵈ    |    2,847ᵗʰ   |       38ᵗʰ     |    137,052  |    1,062    |    84     |
|7      |Hard 🚩 - Hack Back                   |6 |     98ᵗʰ  |     3ʳᵈ    |    2,798ᵗʰ   |       37ᵗʰ     |    136,908  |    1,061    |    84     |
|7      |Hard 🚩 - Dead End?                   |6 |     99ᵗʰ  |     3ʳᵈ    |    2,924ᵗʰ   |       37ᵗʰ     |    136,788  |    1,060    |    84     |
|6      |Easy 🔗 - Linux Strength Training     |5 |     98ᵗʰ  |     3ʳᵈ    |    3,172ⁿᵈ   |       47ᵗʰ     |    136,608  |    1,059    |    84     |
|4      |Medium 🚩 - JVM Reverse Engineering   |3 |     96ᵗʰ  |     3ʳᵈ    |    3,031ˢᵗ   |       46ᵗʰ     |    136,450  |    1,058    |    84     |
|3      |Medium 🚩 - Carrotbane of My Existence|2 |     96ᵗʰ  |     3ʳᵈ    |    3,468ᵗʰ   |       49ᵗʰ     |    136,150  |    1,057    |    84     |
|2      |Easy 🔗 - Learn Rust                  |1 |     96ᵗʰ  |     3ʳᵈ    |    5,152ⁿᵈ   |       67ᵗʰ     |    136,030  |    1,056    |    84     |


</h6></div><br>

<p align="center">Global All Time:    98ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/3ed6d158-8f59-49b0-8221-1662748845c3"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/7dd0cead-adde-48ed-b4a9-998ee26a0782"><br><br>
                  Brazil All Time:      3ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/d5833623-0fd5-41d5-9859-f00d8a9be8af"><br><br>
                  Global monthly:    2,847ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/15801f3e-f836-4688-b2f0-c3ed1f4eb5b7"><br><br>
                  Brazil monthly:      38ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/7d9e8510-7a13-43ab-abda-dda4cb1cd1f5"></p>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
