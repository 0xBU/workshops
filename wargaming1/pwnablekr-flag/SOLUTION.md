# pwnable.kr flag

```
$ wget http://pwnable.kr/bin/flag
$ objdump -d flag
```
Returns nothing. Strange.

```
$ chmod +x flag; ./flag
I will malloc() and strcpy the flag there. take it.
```
Test that string as being the answer. Wrong - that'd have been too easy.
Okay so it does actually do something and is an executable. 

Why would objdump fail? If it's a malformed binary is the only reason.
That only happens due to some sort of corruption, most often man-made, in things
like malware. Malware is often obfuscated to make diassembly and detection harder.
This is actually a hard problem to figure out how something is packed, and to reverse it.
Luckily most malware authors, and people in general use popular tools at default settings.
UPX is the most popular packer, and the default setting leaves the string "UPX" in the binary.

```
$ strings flag
...
$Info: This file is packed with the UPX executable packer http://upx.sf.net $
$Id: UPX 3.08 Copyright (C) 1996-2011 the UPX Team. All Rights Reserved. $
...
UPX!
UPX!
```

Nice! It's UPX. Let's download a UPX unpacker

```
$ upx -d flag
$ gdb flag
$ b main
$ r
   0x401163 <frame_dummy+67>:	nop
   0x401164 <main>:	push   rbp
   0x401165 <main+1>:	mov    rbp,rsp
=> 0x401168 <main+4>:	sub    rsp,0x10
   0x40116c <main+8>:	mov    edi,0x496658
   0x401171 <main+13>:	call   0x402080 <puts>
   0x401176 <main+18>:	mov    edi,0x64
   0x40117b <main+23>:	call   0x4099d0 <malloc>
```

Nice a strcpy and malloc as promised!

```
# Inside of gdb:
$ n; n; n; n; n; n
=> 0x401184 <main+32>:	mov    rdx,QWORD PTR [rip+0x2c0ee5]        # 0x6c2070 <flag>
```

Oh, the flag is just in 0x6c2070

```
$ telescope 0x6c2070
0000| 0x6c2070 --> 0x496628 ("UPX...? sounds like a delivery service :)")
```
