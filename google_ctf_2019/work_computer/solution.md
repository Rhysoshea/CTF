### Work Computer

With the confidence of conviction and decision making skills that made you a contender for Xenon's Universal takeover council, now disbanded, you forge ahead to the work computer.   This machine announces itself to you, surprisingly with a detailed description of all its hardware and peripherals. Your first thought is "Why does the display stand need to announce its price? And exactly how much does 999 dollars convert to in Xenonivian Bucklets?" You always were one for the trivialities of things.

Also presented is an image of a fascinating round and bumpy creature, labeled "Cauliflower for cWo" - are "Cauliflowers" earthlings?  Your 40 hearts skip a beat - these are not the strange unrelatable bipeds you imagined earthings to be.. this looks like your neighbors back home. Such curdley lobes. Will it be at the party?

SarahH, who appears to be  a programmer with several clients, has left open a terminal.  Oops.  Sorry clients!  Aliens will be poking around attempting to access your networks.. looking for Cauliflower.   That is, *if* they can learn to navigate such things.

## Solution

We are given only some text this time

`readme.ctfcompetition.com 1337`

Using Netcap to connect to the server address we are logged in to some kind of terminal but with no obvious commands or files to target.
`ls` lists two files **ORME.flag** and **README.flag**. And `help` displays:

> Alien's shell
Type program names and arguments, and hit enter.
The following are built in:
  cd
  help
  exit
Use the man command for information on other programs.

`cd ..` reveals that we are in a larger directory structure. A lot of the content appeared to be empty files, though bin/ contained some working executables. After playing around with some I discovered one that could display the contents of the README.flag file. Running `makemime README.flag` displays the following
> Mime-Version: 1.0
Content-Type: multipart/mixed; boundary="2122381162-1799202820-1874582970"
--2122381162-1799202820-1874582970
Content-Type: application/octet-stream; charset=us-ascii
Content-Disposition: inline; filename="README.flag"
Content-Transfer-Encoding: base64
Q1RGezRsbF9ENDc0XzVoNGxsX0IzX0ZyMzN9Cg==
--2122381162-1799202820-1874582970--

Copying the second to last line to a base64 decoder reveals the flag! Trying to read the ORME.flag file using the same method gives a permission denied message.
