LEVEL09
======


Use LD_PRELOAD to Intercept ptrace
You can use the LD_PRELOAD mechanism to load a shared library that overrides the ptrace function. This method will intercept any call to ptrace before the actual system ptrace function is executed.

cp /tmp/no_ptrace.c /home/user/level09/

gcc -shared -fPIC -o /tmp/no_ptrace.so /tmp/no_ptrace.c


level09@SnowCrash:~$ LD_PRELOAD=./no_ptrace.so /home/user/level09/level09 token
tpmhr
