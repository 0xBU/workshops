# Welcome to the Stack Smashing Tutorial

## Background
*DO NOT LOOK AT SOLUTION.PY UNTIL YOU HAVE COMPLETED THE STACK SMASHING, doing so is cheating*
solution.py is how we generated the many compiled c files and is not part of the solution.

We compiled all the C files like so:
gcc -fno-stack-protector -z execstack -g -m32 -o program program.c


### -fno-stack-protector disables stack canaries 
Stack | Address
:-- | --:
local variables | 0x00000000
vulnerable buffer | 0x&ast;&ast;&ast;&ast;&ast;&ast;&ast;&ast;
canary value | 0x&ast;&ast;&ast;&ast;&ast;&ast;&ast;&ast; +  (buffersize)
return address |  0x&ast;&ast;&ast;&ast;&ast;&ast;&ast;&ast; +  (buffersize) + word_size
rest of file (heap, global variables, .text) | 0xffffffff

The reason we disable stack canaries is that we are overwriting the return address. With stack canaries on, we also overwrite that stack canarty in the process. There is no way to know what the stack canary is. When system goes jump, it checks that stack canary is correct. We can never guess the stack canary and it thwarts our attack. 

One way to bypass this is through memcpy. If the stack buffer is overwritten during memcpy, then the check of the canary is simply bypassed and the program will go to the default exception handler ... which can also be overwritten. 

### -z execstack
-z sets the stack executability parameters, we have set stack execution on. There are ret2libc attacks that you can leverage when this is off. Find out more (here)[https://blog.techorganic.com/2015/04/21/64-bit-linux-stack-smashing-tutorial-part-2/]

### ASLR (Address Space Layout Randomization)
You do not need to stop randomization of your address space, as many other tutorials on stack smashing suggest. Instead, we will be using gdb, which automatically turns off ASLR(address space layout randomization). This is important because, in order to jump in your code, you need to have a predictable place to jump, With randomization turned on, your jumping places are randomized, making this impossible. GDB automatically turns this off on execution of a program.

You can disable ASLR system wide with:
echo "0" > /proc/sys/kernel/randomize_va_space
However, we strongly caution against this, as it makes all of your system programs vulnerable. 
If you do do this, make sure you turn it off via rebooting your computer or running this command:
echo "2" > /proc/sys/kernel/randomize_va_space
Additionally, if you do not want to turn off randomization through GDB, you may use this command, although we are not sure if this works. 
setarch `uname -m` -R /.EXECUTABLE_HERE

### -g
Tells gcc to generate debugging information such as function names, local variable names, and other things are normally thrown out as they are not necessary but make using gdb far easier.

#### -m32
Compiles the program for 32-bit machines, simply makes everything a little easier to work with.


### -o program 
sets the compiled program name to "program"

## Getting Started
1. Git clone this repository
``git clone REPOLINK``
2. find the program that has a buffer overflow vulnerability
3. run gdb on the program with the vulnerability
    * do you notice anything strange or out of the ordinary? 
    * are able to notice any logic that may be overwrittent? (there should be!!)
4. find a suitable string to enter, that once inputted allows you to take over the flow of execution of the program
5. once you have found your flag, hash it with sha256 and check if it equals:
ef05b98c5c0b1a2b7e9312b9d4d87d3ceddfded2093a4b036d324df621aa1557
    * You may check this by typing "sha256 YOURFLAG" into duckduckgo.com
