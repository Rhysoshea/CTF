### Arrival & Reconnaissance
Having successfully figured out this "coordinate" problem. The ship lurches forward violently into space. This is one of the moments when you realize that some kind of thought or plan would have been good, but typically for you and how you found yourself in this situation, you didn't think too much before acting. Only the stars themselves know where you'll end up.

After what seems like an eternity, or at least one full season of "Xenon's Next Top Galactic Overlord" you arrive in a system of 9 planetary bodies, though one of them is exceptionally small. You nostalgically remember playing explodatoid with your friends and hunting down planets like this. But this small planet registers a hive of noise and activity on your ships automated scanners. There's things there! Billions upon trillions of things, moving around, flying, swimming, sliding, falling.

Of particular interest may be the insect-like creatures flying around this planet, uniformly. One has the words "Osmium Satellites" written on it. Maybe this is a starting point to get to know what's ahead of you.

### Satellite networking

Placing your ship in range of the Osmiums, you begin to receive signals. Hoping that you are not detected, because it's too late now, you figure that it may be worth finding out what these signals mean and what information might be "borrowed" from them. Can you hear me Captain Tim? Floating in your tin can there? Your tin can has a wire to ground control?

Find something to do that isn't staring at the Blue Planet.

## Solution

Two files are downloaded, **README.pdf** and **init_sat**. The pdf details that we have arrived at Earth and bumped into a satellite. It also instructs us to open init_sat in the terminal.

Running init_sat we are asked to input the name of a satellite. Back to the pdf we see 'osmium' written on the side. Inputting this to init_sat we are given the following link `https://docs.google.com/document/d/14eYPluD_pi3824GAFanS29tWdTcKxP_XUxx7e303-3E`.

Navigating to the document gives the following *VXNlcm5hbWU6IHdpcmVzaGFyay1yb2NrcwpQYXNzd29yZDogc3RhcnQtc25pZmZpbmchCg==*. The '=' padding at the end tells us this is a base64 encoded message. https://www.lucidchart.com/techblog/2017/10/23/base64-encoding-a-visual-explanation/ is a good link explaining how this encoding works.

Decoding using a Base64 decoder online reveals the following message:

Username: wireshark-rocks
Password: start-sniffing!

This is a hint to use wireshark to monitor network packages. Searching through the data we come across the flag: `CTF{4efcc72090af28fd33a2118985541f92e793477f}`.
