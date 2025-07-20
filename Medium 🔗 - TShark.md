<p>July 19, 2025 - Day 439</p>
<h1>TShark</h1>

<br>

<img width="1905" height="381" alt="image" src="https://github.com/user-attachments/assets/498c46ef-ae0c-4d61-8dc4-8d0efaa499a1" />


<br>

> 2.3. <em>Which A record was present the most?</em><br><a id='2.3'></a>
>> <strong><code>GRIMM.utelsystems.local</code></strong><br>
<p></p>

```bash
$ tshark -r dnsexfil.cap -Y "dns.qry.type == 1" -T fields -e dns.qry.name
www.netbsd.org
www.netbsd.org
GRIMM.utelsystems.local
GRIMM.utelsystems.local
GRIMM.utelsystems.local
GRIMM.utelsystems.local
```


<br>

> 3.4. <em>Which A record was present the most?</em><br><a id='3.4'></a>
>> <strong><code>MZWGCZ33ORUDC427NFZV65BQOVTWQX3XNF2GQMDVG5PXI43IGRZGWIL5</code></strong><br>
<p></p>

```bash
$ tshark -r dnsexfil.pcap -Y "dns.flags.response == 0"
    1   192.168.1.8 → 192.168.1.200  74 Standard query 0xbeef A M.m4lwhere.org
    4   192.168.1.8 → 192.168.1.200  74 Standard query 0xbeef A Z.m4lwhere.org
    7   192.168.1.8 → 192.168.1.200  74 Standard query 0xbeef A W.m4lwhere.org
   10   192.168.1.8 → 192.168.1.200  74 Standard query 0xbeef A G.m4lwhere.org
   13   192.168.1.8 → 192.168.1.200  74 Standard query 0xbeef A C.m4lwhere.org
   16   192.168.1.8 → 192.168.1.200  74 Standard query 0xbeef A Z.m4lwhere.org
   19   192.168.1.8 → 192.168.1.200  74 Standard query 0xbeef A 3.m4lwhere.org
   20   192.168.1.8 → 192.168.1.200  74 Standard query 0xbeef A 3.m4lwhere.org
   24   192.168.1.8 → 192.168.1.200  74 Standard query 0xbeef A O.m4lwhere.org
   26   192.168.1.8 → 192.168.1.200  74 Standard query 0xbeef A R.m4lwhere.org
   28   192.168.1.8 → 192.168.1.200  74 Standard query 0xbeef A U.m4lwhere.org
   30   192.168.1.8 → 192.168.1.200  74 Standard query 0xbeef A D.m4lwhere.org
   32   192.168.1.8 → 192.168.1.200  74 Standard query 0xbeef A C.m4lwhere.org
   34   192.168.1.8 → 192.168.1.200  74 Standard query 0xbeef A 4.m4lwhere.org
   36   192.168.1.8 → 192.168.1.200  74 Standard query 0xbeef A 2.m4lwhere.org
   39   192.168.1.8 → 192.168.1.200  74 Standard query 0xbeef A 7.m4lwhere.org
   41   192.168.1.8 → 192.168.1.200  74 Standard query 0xbeef A N.m4lwhere.org
   43   192.168.1.8 → 192.168.1.200  74 Standard query 0xbeef A F.m4lwhere.org
   45   192.168.1.8 → 192.168.1.200  74 Standard query 0xbeef A Z.m4lwhere.org
   47   192.168.1.8 → 192.168.1.200  74 Standard query 0xbeef A V.m4lwhere.org
   49   192.168.1.8 → 192.168.1.200  74 Standard query 0xbeef A 6.m4lwhere.org
   51   192.168.1.8 → 192.168.1.200  74 Standard query 0xbeef A 5.m4lwhere.org
   53   192.168.1.8 → 192.168.1.200  74 Standard query 0xbeef A B.m4lwhere.org
   54   192.168.1.8 → 192.168.1.200  74 Standard query 0xbeef A Q.m4lwhere.org
   58   192.168.1.8 → 192.168.1.200  74 Standard query 0xbeef A O.m4lwhere.org
   60   192.168.1.8 → 192.168.1.200  74 Standard query 0xbeef A V.m4lwhere.org
   62   192.168.1.8 → 192.168.1.200  74 Standard query 0xbeef A T.m4lwhere.org
   64   192.168.1.8 → 192.168.1.200  74 Standard query 0xbeef A W.m4lwhere.org
   66   192.168.1.8 → 192.168.1.200  74 Standard query 0xbeef A Q.m4lwhere.org
   68   192.168.1.8 → 192.168.1.200  74 Standard query 0xbeef A X.m4lwhere.org
   71   192.168.1.8 → 192.168.1.200  74 Standard query 0xbeef A 3.m4lwhere.org
   73   192.168.1.8 → 192.168.1.200  74 Standard query 0xbeef A X.m4lwhere.org
   75   192.168.1.8 → 192.168.1.200  74 Standard query 0xbeef A N.m4lwhere.org
   77   192.168.1.8 → 192.168.1.200  74 Standard query 0xbeef A F.m4lwhere.org
   79   192.168.1.8 → 192.168.1.200  74 Standard query 0xbeef A 2.m4lwhere.org
   81   192.168.1.8 → 192.168.1.200  74 Standard query 0xbeef A G.m4lwhere.org
   83   192.168.1.8 → 192.168.1.200  74 Standard query 0xbeef A Q.m4lwhere.org
   86   192.168.1.8 → 192.168.1.200  74 Standard query 0xbeef A M.m4lwhere.org
   88   192.168.1.8 → 192.168.1.200  74 Standard query 0xbeef A D.m4lwhere.org
   90   192.168.1.8 → 192.168.1.200  74 Standard query 0xbeef A V.m4lwhere.org
   92   192.168.1.8 → 192.168.1.200  74 Standard query 0xbeef A G.m4lwhere.org
   94   192.168.1.8 → 192.168.1.200  74 Standard query 0xbeef A 5.m4lwhere.org
   96   192.168.1.8 → 192.168.1.200  74 Standard query 0xbeef A P.m4lwhere.org
   99   192.168.1.8 → 192.168.1.200  74 Standard query 0xbeef A X.m4lwhere.org
  101   192.168.1.8 → 192.168.1.200  74 Standard query 0xbeef A I.m4lwhere.org
  103   192.168.1.8 → 192.168.1.200  74 Standard query 0xbeef A 4.m4lwhere.org
  105   192.168.1.8 → 192.168.1.200  74 Standard query 0xbeef A 3.m4lwhere.org
  107   192.168.1.8 → 192.168.1.200  74 Standard query 0xbeef A I.m4lwhere.org
  109   192.168.1.8 → 192.168.1.200  74 Standard query 0xbeef A G.m4lwhere.org
  111   192.168.1.8 → 192.168.1.200  74 Standard query 0xbeef A R.m4lwhere.org
  113   192.168.1.8 → 192.168.1.200  74 Standard query 0xbeef A Z.m4lwhere.org
  116   192.168.1.8 → 192.168.1.200  74 Standard query 0xbeef A G.m4lwhere.org
  118   192.168.1.8 → 192.168.1.200  74 Standard query 0xbeef A W.m4lwhere.org
  120   192.168.1.8 → 192.168.1.200  74 Standard query 0xbeef A I.m4lwhere.org
  122   192.168.1.8 → 192.168.1.200  74 Standard query 0xbeef A L.m4lwhere.org
  124   192.168.1.8 → 192.168.1.200  74 Standard query 0xbeef A 5.m4lwhere.org
```


<br>

> 3.5. <em>Which A record was present the most?</em><br><a id='3.5'></a>
>> <strong><code>flag{th1s_is_t0ugh_with0u7_tsh4rk!}</code></strong><br>
<p></p>

<img width="1353" height="211" alt="image" src="https://github.com/user-attachments/assets/95140434-9217-492b-9ee4-e275f0a7c47c" />

<br>
<br>

<img width="1901" height="891" alt="image" src="https://github.com/user-attachments/assets/28635c89-5873-4caa-b7bf-af65c1644ef0" />

<img width="1898" height="893" alt="image" src="https://github.com/user-attachments/assets/2f77d695-98ca-4671-9e2f-b1623d06d4c9" />

<br>

<div align="center">

| Date              | Streak   | All Time     | All Time     | Monthly     | Monthly    | Points   | Rooms     | Badges    |
| :---------------: | :------: | :----------: | :----------: | :---------: | :--------: | :------  | :-------: | :-------: |
|                   |          |    Global    |    Brazil    |    Global   |   Brazil   |          | Completed |           |
| July 19, 2025     | 439      |     153rd    |      5ᵗʰ     |    163rd    |     7ᵗʰ    | 115,543 |    866    |    72     |

</div>

<img width="329" height="88" alt="image" src="https://github.com/user-attachments/assets/ddc6d054-981e-4c62-af4c-a6857570e2d0" />

<img width="1899" height="901" alt="image" src="https://github.com/user-attachments/assets/e84d74f7-0bb7-4a56-bf72-b97805b5c6c9" />

<img width="1886" height="888" alt="image" src="https://github.com/user-attachments/assets/39506f9c-9054-4b55-9d51-e6e4e69a86bd" />

<img width="1886" height="887" alt="image" src="https://github.com/user-attachments/assets/9c32f949-4fb5-4d39-92a3-8054341c427b" />

<img width="1893" height="889" alt="image" src="https://github.com/user-attachments/assets/40ee0417-efb1-4bcc-a965-c103e982e479" />


