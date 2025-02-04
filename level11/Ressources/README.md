# LEVEL11

######
 9
1. What do we have ?

    Inside the current directory we have a `.lua` file.
    >Lua is a programming language used to develop extensions for applications. The source code written in this language is saved in LUA format. These files allow you to customize existing applications. Among the best-known applications are the video games World of Warcraft and Dawn of War.

2. The code seems quit simple. It looks like a server listening on localhost:5151. The server then listen to the user input, hash it with **sha1sum** and comapre it with the hash "f05d1d066fb246efe0c6f7d095f909a7a0cf34a0" and send us a different message if it's the same.
    >**sha1sum** is dangerous to use because it has been proven in 2017 by Google that it is not resistant to collisions (two same document/text can have the same hash).

3. In the .lua file code we see that a function `io.popen` is used to execute system commands. Like other levels it's a command injection here. We will simply use `nc localhost 5151` and then `; getflag>/tmp/flag11` to inject our code and get our flag with `cat /tmp/flag11`