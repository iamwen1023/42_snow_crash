LEVEL12
=======

1. Same method, we check what we have in the directory. We have a perl file: a server is listening on port 4646, takes 2 arguments.

2. A subshell is executed here:

    ```
    @output = `egrep "^$xx" /tmp/xd 2>&1`;
    ```
    And this is where we are going to try an injection.

3. The main problem here is that our argument 'x' is modified by `$xx =~ tr/a-z/A-Z/;` and `$xx =~ s/\s.*//;`. The first one make all lowercase characters to uppercase and the second one remove everything that's found after a blank character. We will have to find a more creative solution than just `;getflag>/tmp/flag` like previous level because our command will become `;GETFLAG>/TMP/FLAG` and will not work.

4. I tried to inject an env var but it's not on the same shell so this solution does not work.

5. Is there another way to execute `getflag` ? Like every command there must be a path to it right ? We can find it out with `type -a getflag` and we get `getflag is /bin/getflag`. So if there is a path we can use a symbolic link to it ?

6. The idea here is to do something like `ln -s /bin/getflag /symbolic_link` but there is still a major problem: everything directory in the root of the machine are in lowercase and we can not create our own directory in that place so a symbolic link will not work because it will be transformed. So the question here is how can I get a path with no lowercase character ?

7. At first I tried to link the path to the getflag command with `/tmp/SYMBOLIC` and then I will use a **wildcard** to avoid the transformation in the beginning of the function. Also I will create a file to receive the flag as follow `touch /tmp/FLAG12` and with the same strategy I will use a **wildcard** to bypass the transformation and this is the result:
    `curl --data-urlencode 'x=;/*/SYMLINK>/*/FLAG12' --data-urlencode "y=nothing" "http://localhost:4646"`
    I tought that it would work but for a reason that I don't really understand it doesn't. However I could try something else because I found the key for the second problem that I had and the solution is the **wildcard**

8. Then I tried something easier. Maybe I could just put the code I want to be executed in a file and then just execute the file via a command substitution ? I created a script named `INJECTION` that executes `getflag>/tmp/flag12` and I pass the path to the script with a wildcard:

    `curl --data-urlencode 'x=$(/*/INJECTION\)' --data-urlencode "y=nothing" "http://localhost:4646`
    The part `$()` indicate that "a what the return value of the command inside" but for that, the command must be executed !