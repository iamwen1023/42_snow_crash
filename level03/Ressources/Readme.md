cmd: cat /etc/passwd

output: flag01:42hDRfypTqqnw:3001:3001::/home/flag/flag01:/bin/bash

do 'echo "flag01:42hDRfypTqqnw" > hash.txt'

do 'john --format=descrypt hash.txt'

get 'abcdefg'