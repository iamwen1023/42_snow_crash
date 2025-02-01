LEVEL06
=======

1. Checking in the current directory and we can see one binary `level06` and a php file `level06.php`. We guess that the binary is the compiled code for the php file.

2. The code open a file a do string replacement based on some regex but there is a breach. The modifier `\e` execute php code and it's used here so we will exploite it.

3. We create a file and put `[x {${system(getflag)}}]` in it because the `\e` is used on the second member of the regex (everything after 'x'). '{}' will force interpretation inside and '${}' is the syntaxe to access a value of a variable. That way we force the `system(getflag)` to be executed.