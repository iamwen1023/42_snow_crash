LEVEL08
======

when we run "./level08 token", we get output: "You may not access 'token'"

it seems that the program checks if the filename is exactly token and restricts access in that case like:
if (strcmp(filename, "token") == 0) {
    printf("You may not access '%s'\n", filename);
    exit(1);
}

so we can try bypass it with symbolic link with a different name

cmd: ln -s /home/user/level08/token /tmp/hidden
cmd: ./level08 /tmp/hidden