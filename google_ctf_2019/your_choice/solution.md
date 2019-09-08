### Your Choice!

Having found the information you were looking for, while detailed, it presents you with an interesting dilemma. There is a network of "computers" not completely dissimilar to your computrator-machine on your ship. You find yourself in possession of the credentials of an individual on the planet named "SarahH." Great, with these you can get right into the secret world of an earthling without them knowing you're there. You access "SarahH home network," to find two computers: "work" and "home." Not knowing what either of these are, you have to make a decision.


### Home Computer forensics

`Tag: forensics`

Blunderbussing your way through the decision making process, you figure that one is as good as the other and that further research into the importance of Work Life balance is of little interest to you. You're the decider after all. You confidently use the credentials to access the "Home Computer."

Something called "desktop" presents itself, displaying a fascinating round and bumpy creature (much like yourself) labeled  "cauliflower 4 work - GAN post."  Your 40 hearts skip a beat.  It looks somewhat like your neighbors on XiXaX3.   ..Ah XiXaX3... You'd spend summers there at the beach, an awkward kid from ObarPool on a family vacation, yearning, but without nerve, to talk to those cool sophisticated locals.

So are these "Cauliflowers" earthlings? Not at all the unrelatable bipeds you imagined them to be.  Will they be at the party?  Hopefully SarahH has left some other work data on her home computer for you to learn more.

## Solution

Two files are downloaded *note.txt* and *family.ntfs*.

The text file reads "If you're on MacOS, you can rename .ntfs to .dmg".

On Linux we can mount the folder by using `sudo mount family.ntfs /mnt`. This reveals a directory structure similar to that of someone's home computer. Time to see what we can find.

Every file is empty except for a file called credentials.txt located in Family/Documents/ which reads "I keep pictures of my credentials in extended attributes". This suggests there is some hidden data in the attributes of the file.

Running `getfattr credentials.txt` reveals that there is a hidden file in the metadata named 'FILE0'. https://linux.die.net/man/1/getfattr is the man page for getfattr which details an option to get the values of this file `--only-values`.

Piping the values into a file reveals the flag. The values were piped into a .png file because the data at the beginning of the file contain the png suffix.

`getfattr --only-values credentials.txt > flag.png`
