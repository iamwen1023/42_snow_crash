cmd: ls
output: level02.pcap

Share the file with the host so that we can analyze it by using Wireshark

in host:
ifconfig ---> to find the host ip
nc -l 1234 > level02.pcap  ---> listen the port 1234 for the file

in vm:
cmd : cp /home/user/level02/level02.pcap /tmp/
      cat /home/user/level02/level02.pcap | nc 10.24.3.2 1234 ---> host ip is 10.24.3.2

in wireshark:
use follow TCP Stream

output:
Password: ft_wandr...NDRel.L0L

we see . is 7x in hex:
"000000B9  66                                                 f
000000BA  74                                                 t
000000BB  5f                                                 _
000000BC  77                                                 w
000000BD  61                                                 a
000000BE  6e                                                 n
000000BF  64                                                 d
000000C0  72                                                 r
000000C1  7f                                                 .
000000C2  7f                                                 .
000000C3  7f                                                 .
000000C4  4e                                                 N
000000C5  44                                                 D
000000C6  52                                                 R
000000C7  65                                                 e
000000C8  6c                                                 l
000000C9  7f                                                 .
000000CA  4c                                                 L
000000CB  30                                                 0
000000CC  4c                                                 L
000000CD  0d                                                 ."

check hex '7f' in table ASCII is del

result:
ft_waNDReL0L


