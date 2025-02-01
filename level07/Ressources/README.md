LEVEL07
=======

1. There is a binary in the current directory and the owner is flag07 so we try to run it to see what is does. It only print `level07` so not much informations. Let's run `ltrace` on it to see more clearly.

2. Two things should be noticed. There is a call to `gentenv` on the variable `LOGNAME` and a call to `system` with the hard written path to `echo` (we can't use the same strategy as before) and `level07` as an aurgment to the command. It appears that it's actually the value of `LOGNAME` so an injection is possible.

3. By changing the value of `LOGNAME` by `;getflag` with `export LOGNAME=";getflag"` we will be able to execute our command and get the flag