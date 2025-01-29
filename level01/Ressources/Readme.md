LEVEL01
=======

1. **See all users in the VM**

    cmd: ```cat /etc/passwd```

    output: ```flag01:42hDRfypTqqnw:3001:3001::/home/flag/flag01:/bin/bash```

2. **Notice a flaw**

    The part after the username, here "flag01", is supposed to be 'x' wich means it's safely stored in ```/etc/shadow```. However the hashed password here can bee seen in plain view. Passwords aer only stored that way on old Lunix system but now it's deprecated.

3. **Brute force the password with John the Reaper**

    Register the hash in a text file with ```echo "flag01:42hDRfypTqqnw" > hash.txt```

    Use John to decrypt the hash using common library ```john --format=descrypt hash.txt```

    Get **'abcdefg'**
