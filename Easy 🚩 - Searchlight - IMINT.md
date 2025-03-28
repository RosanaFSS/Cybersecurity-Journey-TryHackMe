
<p align="center">March 28, 2025<br>
Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{326}}$$-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>.<br><br>
  <img width="160px" src="https://github.com/user-attachments/assets/7a9af37b-cfd7-4fe1-92ca-3c04479abdf5"></p>

<h1 align="center">
  $$\textcolor{#3bd62d}{\textnormal{Searchlight - IMINT}}$$
</h1>
<p align="center">OSINT challenges in the imagery intelligence category. It is classified as an easy-level challenge,  and you can join it for 🆓 using your own virtual machine with openVPN or TryHackMe´s AttackBox if you are subscribed. Can be accessed clicking <a href="https://tryhackme.com/room/searchlightosint">here</a>.</p>
                                                              
<p align="center"> <img width="900px" src="https://github.com/user-attachments/assets/8bacd20e-b9e6-48fd-9bb4-b107bcc553b0"> </p>

<br>

<h2>Task 1 . Welcome to the Searchlight IMINT room</h2>
<p>In this room we will be exploring the discipline of IMINT/GEOINT, which is short for Image intelligence and geospatial intelligence. This room is suited for those of you who are just beginning your OSINT journey or those brand new to the field of IMINT/GEOINT.<BR>

This room will introduce you to several topics within IMINT, among them:<BR>

- Getting into the right mindset and how to be analytical<br>
- Visually extracting key data points from an image or video<br>
- Applying different tools to assist you in geolocation and answering context questions<br>
- When you have completed this room you should be comfortable applying tools and methodologies to geolocate and answer context questions based on visual
intelligence alone. This room will prepare you for harder CTF challenges in this category as well as real-world geolocation work.<br>

Any thoughts, feedback or issues can be forwarded to me directly on the THM or OSINT Curious Discord. You'll find me there as zewen.<br>

The flag format is: sl{flag}. This means that every answer needs to be submitted within the brackets, sl{your answer}. No capitalization is needed.<br>

If you are stuck or you want someone to discuss these challenges with, head on over to the OSINT Curious Discord server. You can also find me on Twitter if you have any questions!<br>

The answer to the question below is: ready.</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

> 1.1. <em>Did you understand the flag format?</em>.<a id='1.1'></a>
>> <code><strong>sl{ready}</strong></code><br><br>

<h2>Task 2 . Your first challenge</h2>

<h3>Your first geolocation challenge!</h3>
<p>Let's introduce you to your first tool - your eyes!<br>

Before we can apply a tool or a methodology for finding the location of an image, we should use our eyes to scan the image for important information. Extracting key data points from the image will allow you to apply the right tool, craft a good Google search or identify which part of the world the image might have been taken in.<br>

There are 5 elements of IMINT that you should consider when looking at an image, according to Geoint expert Benjamin Strick:<br>

- Context<br>
- Foreground<br>
- Background<br>
- Map markings<br>
- Trial and error<br><br>
A geolocation challenge like this lacks one important factor, which is the context or the source of the image. In real-world cases, you usually have a context in which the image was produced or shared, usually called context clues. Most of these challenges will not have context clues but you may find clues in the titles and descriptions, or if you're stuck you can use the hint function.<br>

Here are some questions you should ask yourself while looking at the upcoming challenges:<br>

- Are there any obvious data in the image that reveals the location, like a street name or storefront signs?<br>
- Can you determine the country or region of the image by, for instance, which side of the road they drive on, language or architectural characteristics that - may reveal a country or continent/region?<br>
- Do you recognize road sign styles, nature and environmental characteristics, or popular motor vehicle brands or vehicle types?<br>
- What is the quality of any visible infrastructure like? Is the road paved or do you see gravel roads?<br>
- Do you see any unique landmarks, buildings, bridges, statues or mountains that can help you geolocate the image?<br><br>
Download the attached image and answer the question below - good luck!</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

> 2.1. <em>What is the name of the street where this image was taken?</em>. Hint: Remember the flag format, sl{your answer}<a id='2.1'></a>
>> <code><strong>sl{carnaby street}</strong></code><br>

![image](https://github.com/user-attachments/assets/42402870-02f2-40f8-b618-28c4a8f4e32a)

<br>

<h2>Task 3 . Just Google it!</h2>


<p>The last challenge wasn't really a challenge, was it?<br>

Let me introduce you to your first tool, Google! If you see anything in the image that can be extracted into a keyword, phrase, a company name, telephone number or any other question you may have as a result of scanning the image up and down: GOOGLE IT!<br>

Here (https://osintcurio.us/2019/12/20/google-dorks/) is a short introduction to what we call 'dorking', the art of using Google search queries to have Google return specific types of data. The next challenges will require you to do some basic Googling in order to answer the questions. You can also practice dorking by joining the Google Dorking room (https://tryhackme.com/room/googledorking).<br>

When geolocating a picture finding the exact location is key, but we may need to answer other questions about the location or the image as well, usually referred to as context questions.<br>

The next few challenges will ask multiple questions that you need to answer based on the information you extract from the image.</p>


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

> 3.1. <em>Which city is the tube station located in?</em>. Hint: Remember the flag format, sl{your answer}<a id='3.1'></a>
>> <code><strong>sl{London}</strong></code><br>

![image](https://github.com/user-attachments/assets/826884dc-920b-4cad-8736-6bd4a1de217b)

<br>

![image](https://github.com/user-attachments/assets/b674ce67-0826-4465-96bb-0e94b91c0138)

<br>

> 3.2. <em>Which tube station do these stairs lead to?</em><a id='3.2'></a>
>> <code><strong>sl{Piccadilly Circus}</strong></code><br>

![image](https://github.com/user-attachments/assets/b674ce67-0826-4465-96bb-0e94b91c0138)

<br>

> 3.3. <em>Which year did this station open?</em><a id='3.3'></a>
>> <code><strong>sl{1906}</strong></code><br>

![image](https://github.com/user-attachments/assets/dc3b3128-b88e-4bac-bed1-27ea7499c2b6)


<br>

> 3.4. <em>How many platforms are there in this station?</em><a id='3.4'></a>
>> <code><strong>sl{4}</strong></code><br>

![image](https://github.com/user-attachments/assets/4604ba2f-92c4-497d-b1bd-f7ae811bee67)



<br>

<h2>Task 4 . Keep at it!</h2>

<p>Good job solving the last challenge! You were able to find the location of the image and by doing that, you could answer contextual questions about the location. This challenge will also require you to do some 'Google dorking' to answer the questions below.<br>

Scan the image for data and remember the questions from the introduction - Do you see anything in the image that can be used in a search query or help you narrow down the potential location?</p>



<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

> 4.1. <em>Which building is this photo taken in?</em><a id='4.1'></a>
>> <code><strong>sl{Vancouver International Airport}</strong></code><br>

![image](https://github.com/user-attachments/assets/89357fb6-67b4-4f0f-ba37-82d767ad2f4e)

<br>

![image](https://github.com/user-attachments/assets/2328c3af-ac82-46d6-a01d-a2b82e0ad336)

<br>

![image](https://github.com/user-attachments/assets/a0cf400a-9f3e-4904-be70-27cff81342a5)

<br>

> 4.2. <em>Which country is this building located in?</em><a id='4.2'></a>
>> <code><strong>sl{Canada}</strong></code><br>

<p>Discovered the answer in 4.1.</p>

<br>

> 4.3. <em>Which city is this building located in?</em><a id='4.3'></a>
>> <code><strong>sl{richmond}</strong></code><br>


![image](https://github.com/user-attachments/assets/6a8cab35-41e7-4b72-afc8-a7aaee3a34ab)

<br>

<h2>Task 5 . Keep at it!</h2>

<p>Now that you've started to learn some techniques I figured we could try and do some good while we hone our skills.<br>

A friend of mine contacted me asking if I could help them locate a coffee shop that is supposed to serve the best lunch there is. They told me the coffee shop is somewhere in Scotland, and he sent me these two pictures. Do you think you could locate it and answer the questions below for me?</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

> 5.1. <em>Which city is this coffee shop located in?</em>Hint: Remember the previous 'lessons'. Extract data from the text and the images and convert that to searchable information.<a id='5.1'></a>
>> <code><strong>sl{blairgowrie}</strong></code><br>

![image](https://github.com/user-attachments/assets/d71c7d78-5286-4820-87a9-e51e4e334bf0)

> 5.2. <em>Which street is this coffee shop located in?</em><a id='5.2'></a>
>> <code><strong>sl{allan street}</strong></code><br>

![image](https://github.com/user-attachments/assets/fa869b22-94d7-49c5-ba84-e361bf537ee3)

> 5.3. <em>What is their phone number?</em><a id='5.3'></a>
>> <code><strong>sl{+447878 839128}</strong></code><br>

<p>Discovered the answer in 5.2.</p>

<br>


> 5.4. <em>What is their email address?</em><a id='5.4'></a>
>> <code><strong>sl{theweecoffeeshop@aol.com}</strong></code><br>


![image](https://github.com/user-attachments/assets/e998301c-17b5-4660-836a-14a3c197a8d5)

<br>


> 5.5. <em>What is the surname of the owners?</em><a id='5.5'></a>
>> <code><strong>sl{cochrane}</strong></code><br>

![image](https://github.com/user-attachments/assets/93692c9d-3130-430b-a050-f9a80df73849)


<br>

<h2>Task 6 . Reverse your thinking</h2>

<p>...</p>


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

> 6.1. <em>Which restaurant was this picture taken at?</em>Hint: It has a famous nickname, which is what we're looking for.<a id='6.1'></a>
>> <code><strong>sl{katz's deli}</strong></code><br>

![image](https://github.com/user-attachments/assets/4ad7e931-8891-4fea-9fbf-139ccd0fc8be)

> 6.2. <em>What is the name of the Bon Appétit editor that worked 24 hours at this restaurant?</em>Hint: It has a famous nickname, which is what we're looking for.<a id='6.2'></a>
>> <code><strong>sl{andrew knowlton}</strong></code><br>

![image](https://github.com/user-attachments/assets/dc5d8a45-8f01-4958-ba71-e42781de976d)

<br>

<h2>Task 7 . Locate this sculpture</h2>

<p>This challenge will require you to apply some the techniques I have touched on so far: Scanning the image for visual clues, reverse image searching and Google dorking. Tools should not be your primary focus - don't underestimate how far you can get with dorking and scrolling search results.</p>


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

> 7.1. <em>What is the name of this statue?</em>Hint: "Og når det er vind og sno Blir han så kald på nesen, Så den lyser som en glo.".<a id='7.1'></a>
>> <code><strong>sl{rudolph the chrome nosed reindeer}</strong></code><br>

<p>The scukpture is located in Oslo.</p>

![image](https://github.com/user-attachments/assets/7a78c515-a5ad-4926-a1a3-e20d2c0cb01a)

<p>I translated the hint.</p>

![image](https://github.com/user-attachments/assets/5d467fe0-5980-4000-b67b-778777d7aec5)

<br>

![image](https://github.com/user-attachments/assets/2fb3071f-f60e-4dc9-bbcf-5fabf46ecbdc)


<br>

![image](https://github.com/user-attachments/assets/c41beec0-4151-4892-8117-e344140eaf90)


<br>

> 7.2. <em>What is the name of the Bon Appétit editor that worked 24 hours at this restaurant?</em>Hint: If you know the location of the statue you may want to visitoslo.<a id='7.2'></a>
>> <code><strong>sl{kjersti stensrud}</strong></code><br>

![image](https://github.com/user-attachments/assets/30434b5a-7f95-412a-856f-85b2a574ecf8)

<br>

![image](https://github.com/user-attachments/assets/9e15482e-f03f-4785-b676-123218b5e7db)

<br>

![image](https://github.com/user-attachments/assets/96d7901b-295c-435d-ad48-bb5869f78426)


<br>

<h2>Task 8 .... and justice for all</h2>

<p>This challenge is a step up in difficulty from the previous challenges and you shouldn't expect to solve this quickly, especially if you are new to IMINT. While you can certainly apply the techniques and tools you've used to s far, this challenge may force you to revise your thinking and your approach while you're working on solving this challenge.<br>

I highly recommend watching this Ted talk by Amy Herman on visual intelligence: "A lesson on looking" if you want a unique view on how you perceive visual data.</p>


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

> 8.1. <em>What is the name of the character that the statue depicts?</em>Hint: Check the title of the challenge.<a id='8.1'></a>
>> <code><strong>sl{lady justice}</strong></code><br>



![image](https://github.com/user-attachments/assets/19f24f10-46cd-44dd-a38b-9579a3accdad)

<br>

> 8.2. <em>where is this statue located?</em:Hint : the birthplace of a nation<a id='8.2'></a>
>> <code><strong>sl{alexandria, virginia}</strong></code><br>


![image](https://github.com/user-attachments/assets/44252d38-961d-432b-becc-06b998b30bc7)

<br>

![image](https://github.com/user-attachments/assets/94c6fdf2-b22d-473a-af8b-348bd3ab764d)

<br>

![image](https://github.com/user-attachments/assets/e4582235-0988-4a60-999f-149672b9717d)

<br>

> 8.3. <em>What is the name of the building opposite from this statue?</em>Hint : The quality of this establishment is shown with stars<a id='8.3'></a>
>> <code><strong>sl{The Westin Alexandria Old Town}</strong></code><br>

![image](https://github.com/user-attachments/assets/c703e5bb-fb98-42b8-8b24-403b501d2762)

<br>

![image](https://github.com/user-attachments/assets/c6509c0c-16d5-4158-bf61-0c332b51b1f8)


<br>

<h2>Task 9 . THe view from my hotel room</h2>

<p>Geolocating videos aren't much different from geolocating images. A video is just a string of images, usually played at 24 frames(or images) per second. In other words, a video will hold a whole lot more images that can be analyzed, reversed and scrutinized by you.<br>

Here's a good writeup by Nixintel on a tool called FFmpeg, which will help you extract the key images from the video that you may need to solve this challenge. Download the attached video and follow Nixintel's guide!<br>

You may have to apply other tools to solve this challenge as well!</p>


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

> 9.1. <em>What is the name of the hotel that my friend stayed in a few years ago?</em>Hint: There's a tool that will allow you to get the right perspective based on what you can see in the video.</em><a id='9.1'></a>
>> <code><strong>sl{novotel singapore clarke quay}</strong></code><br>


![image](https://github.com/user-attachments/assets/30b4aaad-2b91-4376-97e2-8ac47b21fe0f)

<br>

![image](https://github.com/user-attachments/assets/872db12c-b0c5-410b-8212-ef197efde110)

<br>

![image](https://github.com/user-attachments/assets/85614207-8416-404f-9e0a-e0486793c6dd)

<br>

<p>Clarke Quay, Singapore</p>

![image](https://github.com/user-attachments/assets/776299b2-0a3b-4eeb-98b5-4941b875b3a5)

<br>

![image](https://github.com/user-attachments/assets/5d698340-0956-4a67-af1e-cc5421d8a53b)

<br>

![image](https://github.com/user-attachments/assets/1c244460-85ba-445a-b0fb-959c3a6820fc)


<br>
<br>


<h1 align="center">$$\textcolor{#3bd62d}{\textnormal{Room Completed}}$$</h1>

<p align="center"> <img width="900px" src="https://github.com/user-attachments/assets/f35fc135-003d-4095-a44a-94bca5d4d122"> </p>

<p align="center"> <img width="900px" src="https://github.com/user-attachments/assets/cbaaa02e-b899-4c11-8b36-c9689885cbae"> </p>


<h1 align="center">
  $$\textcolor{#3bd62d}{\textnormal{My TryHackMe Journey}}$$
</h1>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          | WorldWide    | Brazil       | WorldWide   | Brazil     |          | Completed |           |
| March 28, 2025    | 326      |     336ᵗʰ    |        8ᵗʰ   |   358ᵗʰ     |     6ᵗʰ    |  89,266  |       632 |   59      |

</div>

<p align="center"> Global All Time:  336ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/0444d7c5-5d86-40e4-a845-fd3ed0818749"> </p>


<p align="center"> Brazil All Time: 8ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/a6d17ac3-38c8-4d55-a7bf-be428b0c5d5d"> </p>


<p align="center"> Global monthly: 358ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/bfcd54f8-6c63-4a95-b2bb-f88150551443"> </p>

<p align="center"> Brazil monthly: 6ᵗʰ<br><br><img width="900px" src="https://github.com/user-attachments/assets/d1b15ff4-5c53-40fa-b50d-1f3353aa4b9b"> </p>

