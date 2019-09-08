### STOP GAN (bof)

`Tag: pwn`

Success, you've gotten the picture of your lost love, not knowing that pictures and the things you take pictures of are generally two seperate things, you think you've rescue them and their brethren by downloading them all to your ships hard drive. They're still being eaten, but this is a fact that has escaped you entirely. Your thoughts swiftly shift to revenge. It's important now to stop this program from destroying these "Cauliflowers" as they're referred to, ever again.

## Solution
We are given two files, another ELF file named **bof** and a c program, **console.c**.

There is also a website *buffer-overflow.ctfcompetition.com 1337* which times out when trying to access. Not sure what this is for yet.

Opening the .c file shows a simple C script with the following comments at the beginning:

>
 * 6e: bufferflow triggering segfault  - binary, compile with:
 * gcc /tmp/console.c -o /tmp/console -static -s
 *
 * Console allows the player to get info on the binary.
 * Crashing bof will trigger the 1st flag.
 * Controlling the buffer overflow in bof will trigger the 2nd flag.

So it looks like we need to crash the bof (buffer overflow) program. First I compiled the program with the given instructions then executed. This presented a couple of problems and in this source code I could see that the bif file is executed with `qemu-mipsel-static`. After a few failed attempts of trying to install and run this program I resorted to running [Netcat](https://www.computerhope.com/unix/nc.htm) on the text that was provided, which is a server address.

This runs the same program that I tried to run locally. Two inputs are available `run` and `quit`. On selecting run we are able to provide some input. Since the task seems to be themed on overloading a buffer I input some very long text. This produced a message `Cauliflower systems never crash >>` a few times until I input a long enough string and finally crashed the system giving the flag.
