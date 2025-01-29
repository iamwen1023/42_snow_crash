LEVEL02
=======

1. **See what' s in the directory**

      cmd: ```ls```
      output: ```level02.pcap```

2. **Share the file with the host so that we can analyze it by using Wireshark**

      - in host: ```ifconfig``` ---> to find the host ip
      - ```nc -l 1234 > level02.pcap```  ---> listen on the port 1234 for the file
      - in vm: cmd: ```cat /home/user/level02/level02.pcap | nc 10.24.3.2 1234``` ---> host ip is 10.24.3.2

3. **Analyse in Wireshark**

      Use the option "follow TCP Stream" in order to see all the joined data that are send in the TCP protocol

      output: ```Password: ft_wandr...NDRel.L0L```

      We see . is 7x in hex:
      "000000B9  66                                                f<br>
      000000BA  74                                                 t<br>
      000000BB  5f                                                 _<br>
      000000BC  77                                                 w<br>
      000000BD  61                                                 a<br>
      000000BE  6e                                                 n<br>
      000000BF  64                                                 d<br>
      000000C0  72                                                 r<br>
      000000C1  7f                                                 .<br>
      000000C2  7f                                                 .<br>
      000000C3  7f                                                 .<br>
      000000C4  4e                                                 N<br>
      000000C5  44                                                 D<br>
      000000C6  52                                                 R<br>
      000000C7  65                                                 e<br>
      000000C8  6c                                                 l<br>
      000000C9  7f                                                 .<br>
      000000CA  4c                                                 L<br>
      000000CB  30                                                 0<br>
      000000CC  4c                                                 L<br>
      000000CD  0d                                                 ."<br>

      Check hex '7f' in table ASCII is del. Since we receive all the user input we can see that some character were deleted so we remoce them in order to have the real password

      result:
      **ft_waNDReL0L**


