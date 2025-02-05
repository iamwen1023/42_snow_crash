# LEVEL13
######

1. We have a binary file. When we execute it says "UID 2013 started us but we we expect 4242". It seems that the programm want to be executed with the role with the uid 4242.

2. Let's see what does the programm in detail by using `ltrace` on it. We basically see that `getuid()` is called two times and then print a that we are not 4242. We didn't get much information here and to get more we will use a decompiler, especialy the one at "https://dogbolt.org/"

3. We get more informations here. If the uid matches with 4242 a function `ft_des` is called. It takes a hard coded string as a parameter and does string manipulation to create and return what seems to be the flag. The first strategy here will be to use `gdb` to modify the return value of `getuid()` and set it to 4242.

4. Run the programm with `gdb ./level13`. Add a breakpoint at the `getuid()` function with `b getuid`. Run the programme with `run`. We see that wee stop at the call of `getuid`. We want to go to the next step, juste before the verification with `step`. We are now in the instructions that check the value of `getuid` and thus it's time to change it! The return value of function are stored in the `eax` register. We can check if it's the case here with `print $eax`. Indeed the return value is `$1 = 2023` because that's our uid. Now let's change it to 4242 with `set $eax = 4242` and see what appends. It works !

4-bis. There is another way to solve this level. Since we could see in clear the string that would go to the `ft_des` function we could try to recreate this function and pass it the same argument.