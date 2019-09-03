# Write a function that takes two equal-length buffers and produces their XOR combination
# To solve this challenge we must first get the buffers into a type that we can do bitwise operations on. In python we can cast the string to an int using the int constructor and providing the radix as the second parameter. Once we have the data in this format we just use the builtin bitwise operator ^ which is exclusive-or, a.k.a XOR.
#
#
# The last line simply formats result into hexadecimal.

def fixed_XOR(hex_a, hex_b):
    xored = int(hex_a, 16) ^ int(hex_b, 16)
    return '{:x}'.format(xored)

if __name__ == '__main__':
    print (fixed_XOR('1c0111001f010100061a024b53535009181c', '686974207468652062756c6c277320657965'))
