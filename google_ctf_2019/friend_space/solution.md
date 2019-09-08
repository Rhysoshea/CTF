### FriendSpaceBookPlusAllAccessRedPremium.com

`Tag: reversing emoji`

Having snooped around like the expert spy you were never trained to be, you found something that takes your interest: "Cookie/www.FriendSpaceBookPlusAllAccessRedPremium.com" But unbeknownst to you, it was only the 700nm Wavelength herring rather than a delicious cookie that you could have found. It looks exactly like a credential for another system. You find yourself in search of a friendly book to read.

Having already spent some time trying to find a way to gain more intelligence... and learn about those fluffy creatures, you (several)-momentarily divert your attention here. It's a place of all the individuals in the world sharing large amounts of data with one another. Strangely enough, all of the inhabitants seem to speak using this weird pictorial language. And there is hot disagreement over what the meaning of an eggplant is.

But not much Cauliflower here. They must be very private creatures. SarahH has left open some proprietary tools, surely running this will take you to them. Decipher this language and move forth!

## Solution

We are given two files **program** and **vm.py**. Executing program gives a long list of 'command not found' errors at first.

Running `python vm.py` says it is missing program, so I tried again while passing program to it this time `python vm.py program`. It then starts to print out a url, though it does take some time. (if you don't have the patience `http://emoji-t0anaxnr3nacpt4na.web.ctfcompetition.com`). This brings up an interesting website of cat pictures and their supposed feline friends. Though after traversing the site and checking out the assets in the Chrome inspector I couldn't find much of value.

I returned to the program and inspected its contents, which were a bunch of emojis that the vm.py script would read and execute accordingly. Reading through the different functions available in the script we can see that the program is mostly loading some numbers into a stack and xor'ing them with what appear to be prime numbers. We can see this by printing out the a and b numbers that are being sent to xor. The result of this is then input to chr() which returns the string of a Unicode integer, thus forming the url. It appears that the program is calculating primes (a) and it is taking longer and longer to do so, which is why the printing of the full url is taking so long.

Searching the first few prime numbers as a sequence reveals that they are a sequence of palindrome primes. So we need a way to easily access or generate these numbers.

The palindrome.py script breaks the vm.py down to its simplest form, printing the xor result of all numbers from program in reverse order. However this broke down part way through. Further investigation into program reveals that at the bottom of each set of numbers is a number that sets the index for the palindrome number sequence.

Finally the full url is revealed as `http://emoji-t0anaxnr3nacpt4na.web.ctfcompetition.com/humans_and_cauliflowers_network/`. Some browsing around this website shows the flag!

CTF{Peace_from_Cauli!}
