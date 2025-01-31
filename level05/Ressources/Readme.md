LEVEL05
=======
> We actually get a hint if we connect directly with the SnowCrash VM but not with ssh: "You have a new mail"

1. We check if we have file in the directory but there is nothing. Then like in the first exercice we check if there are file with flag05 permission somewhere in this machine with `find / -type f -user flag05 2>/dev/null` and we find the file `openarenaserver`

2. Looking at the file we can see that it loop into all the files in the directory `/opt/openarenaserver/`, execute the commands inside them one by one wether the file is executable or not and then delete them

3. We can't execute the file `openarenaserver` but when we create a file in `/opt/openarenaserver/` after some time it disapears so it means the script is run by a crontab or something like that periodically.

4. Now we can create a file that contain `getflag>/tmp/flag05` with `echo "getflag>/tmp/flag05" > /opt/openarenaserver/file
` so that when it's executed we'll recover the flag with `cat /tmp/flag05`