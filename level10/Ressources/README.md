LEVEL10
=======

1. `ls` to check what we have. One binary file, `level10`, and one `token` file that we can't read or do anything else whit it.

2. By running the `level10` it tells us that we should use it like `./level10 file host` and that it "sends file to host if you have access to it". So let's try to run it with those arguments

3. Create a test file with `touch /tmp/test` and we run the script with testing arguments to see what happens `./level10 /tmp/test host`. It tells us "Connecting to host:6969 .. Unable to connect to host host" and that means that if we want to receive content we will have to have a server listening on the port 6969.

4. Its seems that there is two major steps to achieve this level:
    - Run a server listening on the right port 
    - Find a way to have the rights to send token with the programm

5. Create a server using a python script. We test is by sending a file we own `./level10 /tmp/test 192.168.144.5`

6. Now the hard part: find a way to send the token file. Let's see what happens when we send a file to our server with `ltrace ./level10 /tmp/test 192.168.144.5`. There are several function that are called. We check the man for each of them and something comes up for `access`: 

    "Warning: Using access() to check if a user is authorized to, for  example, open a file before actually doing so using open(2) creates a security hole, because the user  might  exploit  the  short  time  interval between  checking and opening the file to manipulate it."

    Indeed `open` is called much later and maybe lets us some time to exploit it.

7. The idea here is to create a normal file `/tmp/text.txt` and and symbolic link `/tmp/symlink` that will redirect alternatively and fast (very fast) between `/home/user/level10/token` and `/tmp/text.txt` using `ln -sf {target} {symlink}`. Also we will send a file using the symbolic link to our server also very fast and hope taht the `access` will check for the `file.txt` and the `open` will open the `token`. We will use a bash script for each of these two task because we whant them tun run fast and indefinetly.

8. Run the server. Run the changing symbolic link and then run the sending file script. After some time the rever receive the flag acheived a **Race Condition Vulnerability** ! Congrats !