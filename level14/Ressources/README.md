# LEVEL14
######


1. We first checke the current directory with `ls`: ntohing. Then as the previous flags with check wich files belong to the user flag14 with `find / -type f -user flag14 ` but again no result. Finally we check if there is any process running with the `flag14` role with the command `ps aux` but again no result. Maybe the final flag is to hack the `getflag` command itself ?

2. As the previous level we use the website "https://dogbolt.org/" to decompile the program. Here we can see there are two things that we must pay attention at. First is the `ptrace()` check. The programm checks if it is being reversed with this call so we will have to modyf the return value of this function. The second step will be to change the value of `getuid` with the same method as the previous level. To see what is our uid we can run `cat /etc/passwd` or simply run `id -u flag14`

3. We will use the same method as the previous level. We run `gdb` on getflag and set a breakpoint at `ptrace()` with `b ptrace`. We then go to the next step with `step` and we modify the return value of `ptrace()` that is stored in the register `eax` with `set $eax = 0`. We now achieved to bypass the reverse protection. Now it' s the same as before, we set a breakpoint at `getuid()` set the `eax` register at 3014 and we get our final flag !

Congratulations !