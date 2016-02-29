import gdb
import sys

sys.path.append('.')
import shoe

def get_t6t7(username):
	keypart1 = "0x123123" # whatever
	keypart2 = "0x123123" # whatever
	
	prog = "/home/eugenek/code/buhacknight/workshops/keygenme-400/keygenme32.elf"
	args = "{} {} {}".format(username, keypart1, keypart2)
	check_bp = "0x0804A125"

	gdb.execute("file " + prog)
	gdb.execute("b *" + check_bp)
	gdb.execute("r " + args)

	T6 = gdb.parse_and_eval("*(unsigned int*)$esp")
	T7 = gdb.parse_and_eval("*(unsigned int*)($esp + 4)")

	print("T6 = {} T7 = {}".format(T6,T7))
	return (T6, T7)

def crack_keys(T6, T7):
	keypart1 = T6 ^ 0x31333337
	keypart2 = (T7 & 0x000000FF) | (((T7 & 0x00FF0000) >> 16) << 8) | (((T7 & 0xFF000000) >> 24) << 16) | (((T7 & 0x0000FF00) >> 8) << 24) 
	return (keypart1, keypart2)

## Talk to the server and get what username it wants
## then send it back the cracked key
s = shoe.Shoe('localhost', 12123)
resp = s.read_until("\r\n") # Welcome msg
for i in range(0,10):
	resp = s.read_until("\n").decode('utf-8') # Username msg
	print(resp)
	#username = resp.lstrip("give me the password for ").rstrip()
	username = resp[-23:].rstrip()
	print(username)
	t6, t7 = get_t6t7(username)
	keypart1, keypart2 = crack_keys(t6, t7)

	ans = "{} {}\n".format(str(int(keypart1)), str(int(keypart2)))
	s.write(ans)
	resp = s.read_until("\n").decode('utf-8') # The smiley
	print(resp)

resp = s.read_until("\n") # Let's get our flag!
print(resp)
s.close()
