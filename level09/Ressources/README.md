LEVEL09
=======

1. `ls` to check what we have
2. `ltrace` on the binary and we see "don't try to reverse me" so obviously we try to reverse it
3. Figure out that it adds an offset on the ascii or byte for each char and then increment
4. Check token file -> see that it's a binary
5. Run the python script to reverse the offset and write it in another file
6. Get your flag and you win

