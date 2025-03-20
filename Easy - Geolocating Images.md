<p align="center">December 8, 2024</p>
<p align="center">Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m genuinely excited to join you on this adventure.<br>
It´s part of my $$\textcolor{#FF69B4}{\textbf{216}}$$-day-streak in  <a href="https://tryhackme">TryHackMe</a>.</p>

<p align="center"> <img width="150px" src="https://github.com/user-attachments/assets/d2fc1f3d-09f0-47f0-8191-d8dfa7d89e92"></p>

<h1 align="center">
  $$\textcolor{#3bd62d}{\textnormal{Geolocating Images}}$$
</h1>
<p align="center">Room to understand how to geolocate images</p>
<p align="center">Access this FREE TryHackMe CTF Room clicking <a href="https://tryhackme.com/r/room/geolocatingimages">Geolocating Images</a>.</p>

                                                           
<p align="center">
  <img height="150px" hspace="20" src="https://github.com/user-attachments/assets/fbcf7a83-5f58-4b5a-ad94-7cd5e95f7014"> <br>
  <img width="700px" src="https://github.com/user-attachments/assets/49ef1d15-88cf-4e30-b480-d1498f486b62">
</p>

<br>

<h2>Task 1. Getting Started</h2>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>
<br>

> 1.1. <em>Download the zip file.</em><br><a id='1.1'></a>
>> <code><strong>No answer needed</strong></code>

<br>
<h2>Task 2. Getting our feet wet - where is this?</h2>
<p>Where is image 1?<br>

(Use Google Reverse Search and revel in all the airplanes it shows you, which by the way, isn't the right answer).<br>

Try Yandex Reverse Image search. Look at the differences!</p>
<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>
<br>

> 2.1. <em>Where in the world is image 1? The answer is the country name.</em><br><a id='2.1'></a>
>> <code><strong>China</strong></code>

<br>

![image](https://github.com/user-attachments/assets/83de5a21-4f06-4866-a8c2-cfffebab0e82)

<br>

![image](https://github.com/user-attachments/assets/69ae2721-3894-4d45-9da6-da8f3ba7c96f)


<br>

![image](https://github.com/user-attachments/assets/c20f824c-59ba-49dd-8422-f034089c9c7a)

<br>

![image](https://github.com/user-attachments/assets/8ea23026-ab70-43ae-863e-c2ec75aadc8f)

<br>

![image](https://github.com/user-attachments/assets/9c51bee7-037d-45e5-9174-fac20e88dd05)


<br>
<h2>Task 3. Geolocating Images 101?</h2>
<p>Okay, now we know what reverse image searching program to use. Let's try to actually look at the picture now to figure out where it is!<br>

Let's say we have a webcam we found on Shodan.io:<br>

https://padcam.liverpool.ac.uk/cgi-bin/guestimage.html</p>

<p>Where is this camera?<br>

The first thing we notice is the weird crest & title with a black bar (and possibly text) underneath it.<br>

Second thing is the logo, "Kaplan".<br>

The third thing is that there is a glass building next to a concrete building.<br>

And finally, we have what appears to be a highway next to the glass building. Because it's a webcam, we can see cars moving quickly!<br>

Putting this into a reverse image search program shows nothing.<br>

Now, something important to note is the name of the webcam. The URL points to Liverpool.ac.uk, which is a university in Liverpool.<br>

If we just had an IP address, we could try to geolocate it using an online tool, checking the ASN number or finding it on Shodan.<br>


Googling "Kaplan University of Liverpool" leads us to a news article about a new building. If we take a look at the image, it looks approximately similar to the one we saw.</p>

![image](https://github.com/user-attachments/assets/63b130c3-3bde-44e6-b9ec-8445c7cd607b)

<p>Rows of long glasses with a little bit of overhang.<br>

Luckily for us, Liverpool have captioned the image.<br>

"The proposed new Liverpool International College facility"<br>

If we google Liverpool International College we get:<br>


https://www.google.com/maps/place/University+of+Liverpool+International+College/@53.4062447,-2.9625347,17z/data=!4m5!3m4!1s0x487b211eda1b2f5f:0xc226c2ccfb209504!8m2!3d53.4060784!4d-2.9605928</p>

![image](https://github.com/user-attachments/assets/ad933fe0-0bd3-422f-9234-c7a0285a92bd)


<p>Which is our building! But it's not built yet... What gives?<br>


In the bottom right hand corner, Google tells us the image was captured in June 2019.</p>

![image](https://github.com/user-attachments/assets/3e72906b-c862-4831-8ed0-52e85632cff1)

<p>So Google maps hasn't updated yet.<br>


If we turn the camera around on Google maps, we can see where the live webcam should be.</p>

![image](https://github.com/user-attachments/assets/b16a40bc-d3bf-4a12-a663-ab78bdcf7644)

<p>Somewhere on this building!


When geolocating an image, we want to point out big landmarks we can easily find on a map. Road layouts, business names, The Empire States Building.</p>


<br>
<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>
<br>

> 3.1. <em></em><br><a id='2.1'></a>
>> <code><strong>No answer needed</strong></code>

<br>
<h2>Task 4. Now your turn</h2>
<p>Where was image 2 taken? Specifically, I'm looking for the name of the place that has likely set up the webcam. You'll know it when you see it!<br>

Please do not use reverse image searches for this!</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>
<br>

> 4.1. <em>Where was image 2 taken?</em><br><a id='4.1'></a>
>> <code><strong>Wrigleyville Sports</strong></code>

<p>I used the same method.</p>

<br>
<br>
<h2>Task 5. Helpful tips for geolocating</h2>
<p>Wow, congrats! I found a webcam on Shodan.io and took this screenshot, you just geolocated your first image 😎<br>

It's important to know what is and isn't likely to be in a country. For example, it is unlikely for a regular Catholic church to appear in places where Budhism / islam is the most popular religeion.<br>

The language used on the shops and vehicles matter too. We can use Google translate to predict what language it could be.<br>

Which side of the road the cars are on, the license plates (you normally can find out what country or state the license plate is from), the markings on the road (different countries have different markings), the style of traffic lights, the clothing choices of those walking around.<br>

To be good at geolocation, we've got to open our eyes to all that could be. In your country, for example, it may be common to wear coats during the winter periods. However, in other countries it may not be (think Australia).<br>

Even the smallest of things that we wouldn't normally think twice about can reveal to us the possible location.<br>

One of the more obvious ways we can geolocate an image is to look at the image details. Does it contain EXIF data?<br>


What about where it was posted - is there a location tagged on social media?</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>
<br>

> 5.1. <em>Read the above material</em><br><a id='5.1'></a>
>> <code><strong>No answer needed</strong></code>


<br>
<br>
<h2>Task 6. Your tunr again!</h2>


<p>Please do not try to use reverse image searches for this one! Pay close attention to what is in the image.<br>

I want you to answer with the name of the place the webcam is facing.<br>

Note: the name of this location on Google Maps is not the right answer. If you take that location name and paste it back into search, you'll find out there's about a million of them. To make this harder, I'm looking for the name that specifically identifies this location. When you enter this name, it'll be the only one that turns up on Google Maps.</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>
<br>

> 6.1. <em>Where was image 3 taken?</em><br><a id='6.1'></a>
>> <code><strong>Meudon Observatory</strong></code>


<br>
<br>
<h2>Task 7. Your turn, what can you see?</h2>
<p>Look at image 4. What do you see? What can you observe? </p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>
<br>

> 7.1. <em>Where is image 4 taken?</em><br><a id='7.1'></a>
>> <code><strong>Abbey Road</strong></code>


<br>

<br>
<br>
<h2>Task 8. You´re done!</h2>

<p>And that's it!<br>

Check out Bellingcat for more on geolocation:<br>

https://www.bellingcat.com/news/2020/01/21/geolocating-venezuelan-lawmakers-in-europe<br>

Alternatively, play a lot of Geoguesser!<br>


https://geoguessr.com/</p>

<br>
<br>
<h2>Room Complete</h2>
<p>Keep learning, keep growing!<br>

<h3 align="center"> <img width="900px" src="https://github.com/user-attachments/assets/3017011f-a0fd-40b6-9d59-b899f63ce810"> </h3>



<h2>My Journey<a id='3'></a></h2>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     |
| :---------------: | :------- | :----------- | :----------- | :---------- | :--------- | :------  | :-------- |
|                   |          | WorldWide    | Brazil       | WorldWide   | Brazil     |          | Completed |
| December 8, 2024  | 216      |     1,001 st |        21 st |    4,980 th |      51 st |  60,040  |       460 |

</div>

<h3 align="center"> <img width="900px" src="https://github.com/user-attachments/assets/1450993d-7f47-4ec7-bb38-03db236a2650"> </h3>
