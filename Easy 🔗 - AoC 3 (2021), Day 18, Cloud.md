<h1 align="center">Advent of Cyber 3 (2021) - Cloud - Day 18 -  Playing with containers</h1> 
<p align="center"><img width="200px" src="https://github.com/user-attachments/assets/b2513ced-a478-4916-8658-a58bc6e65af6"><br>Jun 5, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure, part of my 394-day-streak in  <a href="https://tryhackme.com">TryHackMe</a>
<br>Access Advent of Cyber 3 (2021) clicking <a href="https://tryhackme.com/room/adventofcyber3"</a>here.<br><br>
<img width="1000px" src="https://github.com/user-attachments/assets/b3f8f733-315c-479b-8d12-721dc52b44b2"></p>

<br>
<br>

<p>1.1. What command will list container images stored in your local container registry?<br>
<code>docker images</code><br></p>

![image](https://github.com/user-attachments/assets/fe9505b6-4d6d-4a0b-8246-ef808ddb2176)

<br>

<p>1.2. What command will allow you to save a docker image as a tar archive?<br>
<code>docker save</code><br></p>

![image](https://github.com/user-attachments/assets/6c65a9b8-a3ca-4887-968b-6017e9894b7d)

<br>

<p>1.3. What is the name of the file (including file extension) for the configuration, repository tags, and layer hash values stored in a container image?<br>
<code>manifest.json</code><br></p>

![image](https://github.com/user-attachments/assets/98898085-edf1-4e0d-8d13-42f623840d9d)

<br>

![image](https://github.com/user-attachments/assets/e97ca63d-fac8-4cd9-ba6c-f84fbf25b034)

<br>

![image](https://github.com/user-attachments/assets/0e195c61-a84e-45e4-93a7-4ca2aa05a061)


<br>

<p>1.4.What is the token value you found for the bonus challenge?<br>
<code>7095b3e9300542edadbc2dd558ac11fa</code><br></p>

![image](https://github.com/user-attachments/assets/3f3eef8d-832a-4912-90dc-ac2ed9ffb177)

<br>

![image](https://github.com/user-attachments/assets/9bd9e8ec-c5cd-4767-99f3-ca7719bf95b4)


```bash
root@ip-10-10-88-113:~/aoc# cat f886f00520700e2ddd74a14856fcc07a360c819b4cea8cee8be83d4de01e9787.json | jq
{
  "architecture": "amd64",
  "config": {
    "Hostname": "",
    "Domainname": "",
    "User": "newuser",
    "AttachStdin": false,
    "AttachStdout": false,
    "AttachStderr": false,
    "Tty": false,
    "OpenStdin": false,
    "StdinOnce": false,
    "Env": [
      "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
      "api_key=a90eac086fd049ab9a08374f65d1e977"
    ],
    "Cmd": null,
    "Image": "sha256:035522c2043f6036e879810cfffe0db9665ebb09e1852339231fd805daad5325",
    "Volumes": null,
    "WorkingDir": "/home/newuser",
    "Entrypoint": [
      "sh"
    ],
    "OnBuild": null,
    "Labels": null
  },
  "container": "7b422a5dd0a2a59167ae476fcc18f7ae9a094c02de40b4b4effd42a5d032bae4",
  "container_config": {
    "Hostname": "7b422a5dd0a2",
    "Domainname": "",
    "User": "newuser",
    "AttachStdin": false,
    "AttachStdout": false,
    "AttachStderr": false,
    "Tty": false,
    "OpenStdin": false,
    "StdinOnce": false,
    "Env": [
      "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
      "api_key=a90eac086fd049ab9a08374f65d1e977"
    ],
    "Cmd": [
      "/bin/sh",
      "-c",
      "#(nop) ",
      "ENTRYPOINT [\"sh\"]"
    ],
    "Image": "sha256:035522c2043f6036e879810cfffe0db9665ebb09e1852339231fd805daad5325",
    "Volumes": null,
    "WorkingDir": "/home/newuser",
    "Entrypoint": [
      "sh"
    ],
    "OnBuild": null,
    "Labels": {}
  },
  "created": "2021-10-21T20:31:17.236366166Z",
  "docker_version": "20.10.7",
  "history": [
    {
      "created": "2021-10-16T00:37:47.226745473Z",
      "created_by": "/bin/sh -c #(nop) ADD file:5d68d27cc15a80653c93d3a0b262a28112d47a46326ff5fc2dfbf7fa3b9a0ce8 in / "
    },
    {
      "created": "2021-10-16T00:37:47.578710012Z",
      "created_by": "/bin/sh -c #(nop)  CMD [\"bash\"]",
      "empty_layer": true
    },
    {
      "created": "2021-10-20T16:16:12.499990187Z",
      "created_by": "/bin/sh -c apt-get upgrade && apt-get update"
    },
    {
      "created": "2021-10-20T16:16:46.080121757Z",
      "created_by": "/bin/sh -c apt install curl -y"
    },
    {
      "created": "2021-10-21T20:22:41.837170259Z",
      "created_by": "/bin/sh -c apt install python3 -y"
    },
    {
      "created": "2021-10-21T20:23:42.130217528Z",
      "created_by": "/bin/sh -c apt install pip -y"
    },
    {
      "created": "2021-10-21T20:23:52.8316757Z",
      "created_by": "/bin/sh -c apt install git -y"
    },
    {
      "created": "2021-10-21T20:31:13.639594181Z",
      "created_by": "/bin/sh -c git clone https://github.com/hashicorp/envconsul.git root/envconsul/"
    },
    {
      "created": "2021-10-21T20:31:14.315738313Z",
      "created_by": "/bin/sh -c #(nop) WORKDIR /root/envconsul",
      "empty_layer": true
    },
    {
      "created": "2021-10-21T20:31:14.645450256Z",
      "created_by": "/bin/sh -c #(nop) ADD file:cba528c0d7ba7c0c89ad4ce3e550dc4b3128c2804d4dc75daaf1421759f6d664 in . "
    },
    {
      "created": "2021-10-21T20:31:15.914695012Z",
      "created_by": "/bin/sh -c useradd -ms /bin/bash newuser"
    },
    {
      "created": "2021-10-21T20:31:16.26981869Z",
      "created_by": "/bin/sh -c #(nop)  USER newuser",
      "empty_layer": true
    },
    {
      "created": "2021-10-21T20:31:16.617670519Z",
      "created_by": "/bin/sh -c #(nop) WORKDIR /home/newuser",
      "empty_layer": true
    },
    {
      "created": "2021-10-21T20:31:16.937450858Z",
      "created_by": "/bin/sh -c #(nop)  ENV api_key=a90eac086fd049ab9a08374f65d1e977",
      "empty_layer": true
    },
    {
      "created": "2021-10-21T20:31:17.236366166Z",
      "created_by": "/bin/sh -c #(nop)  ENTRYPOINT [\"sh\"]",
      "empty_layer": true
    }
  ],
  "os": "linux",
  "rootfs": {
    "type": "layers",
    "diff_ids": [
      "sha256:9f54eef412758095c8079ac465d494a2872e02e90bf1fb5f12a1641c0d1bb78b",
      "sha256:500cecccd300e0ed1d2cf9595c1b2d7c4367e21364c2db98ac8952d74c3f1fde",
      "sha256:4808c15f81e439b0593df34aea7c7f811f61bb676cf60cabbf4acf06ab95f41e",
      "sha256:60d27d4a42f954a96e48da0a44b01a75addfe378a9e7775217cf8b2f40216fdf",
      "sha256:9c2b4151672df710fc3b809e4d9ab7f84080edf9104be607302af0368475f08d",
      "sha256:6369024ddd8005bc8621c560ca0ec7a23fee9a5426598c8045de3695ecf07a61",
      "sha256:7b140605c39892e722cd0d18fb1fab4d50329d65a27902dda1b3ec46a742e49f",
      "sha256:33a4a349485916db832c7f6d71f3c2f1139fde6fca626206736fd310eedd392f",
      "sha256:f09c564596bc77e010a4bc4f56ba6f9b19b3bf46a333f9d68a6ef0efa1ee960e"
    ]
  }
}
root@ip-10-10-88-113:~/aoc# 
```

![image](https://github.com/user-attachments/assets/1b67b0c2-0e8a-420e-bbbd-5ddc8632749a)

<br>

![image](https://github.com/user-attachments/assets/0687631b-18df-48aa-9f74-42762bd94a74)

<br>

![image](https://github.com/user-attachments/assets/f316d548-47bb-44eb-96d9-0165ddc61725)

<br>
<br>

<h1 align="center">Challenge in Progress, 75%</h1>
<p align="center"> <img width="1000px" src="https://github.com/user-attachments/assets/8fd87011-8da8-4307-b0f0-79f5f18246cd"></p>


<h1 align="center">My TryHackMe Journey</h1>

<div align="center">

| Date<br>          |  Streak<br>|   All Time<br>Global   |   All Time<br>Brazil |  Monthly<br>Global   |  Monthly<br>Brazil   |  SHOGUN<br>points  |   Rooms<br>completed  |  Badges<br> |
| :---------------: | :--------: | :--------------------: | :------------------: | :------------------: | :------------------: | :----------------: | :-------------------: | :---------: |
| Jun 5, 2025       |     395    |          200ᵗʰ         |            4ᵗʰ       |        2,618ᵗʰ       |         36ᵗʰ        |       106,243       |             765       |    62       |

</div>

<p align="center"> Global All Time: 200ᵗʰ <br><img width="300px" src="https://github.com/user-attachments/assets/4d1ff9c5-6baa-4efd-bdf6-47b2c64371be" alt="Your Image Badge"><br>
                                              <img width="1000px" src="https://github.com/user-attachments/assets/c3644218-8e94-40ab-80fb-dd8f8753b535"><br><br>
                   Brazil All Time:   4ᵗʰ<br><img width="1000px" src="https://github.com/user-attachments/assets/fe2923df-745a-4249-99e0-82a97f6faee8"><br><br>
                   Global monthly: 2,618ᵗʰ<br><img width="1000px" src="https://github.com/user-attachments/assets/a00c157c-3c85-41f6-951a-3224d2d03fdf"><br><br>
                   Brazil monthly:   36ᵗʰ<br><img width="1000px" src="https://github.com/user-attachments/assets/d8739b3f-40c4-45cb-96ca-0efd217ddaa0"><br><br></p>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p> 
<br><br>
<h1 align="center">Thank you very much ben, ashu, tryhackme, cmnatic, timtaylor, strategos, umairalizafar, jcfarris, and wesladd for developinng this experience so that I could sharpen my skills!</h1>
