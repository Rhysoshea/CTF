# The hex encoded string:
#
# 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
#
# has been XOR'd against a single character. Find the key, decrypt the message.
#
# How? Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric. Evaluate each output and choose the one with the best score.
import math

character_frequencies = {'e': 12.70, 't': 9.06, 'a': 8.17, 'o': 7.51, 'i': 6.97, 'n': 6.75, 's': 6.33, 'h': 6.09, 'r': 5.99, 'd': 4.25, 'l': 4.03, 'c': 2.78, 'u': 2.76, 'm': 2.41, 'w': 2.36, 'f': 2.23, 'g': 2.02, 'y': 1.97, 'p': 1.93, 'b': 1.29, 'v': 0.98, 'k': 0.77, 'j': 0.15, 'x': 0.15, 'q': 0.10, 'z': 0.07}

def score(str_bytes):
    """Sums the character frequency for each character. If the given byte cannot be mapped to a character then it gets a score of -100. Rounded to 2 decimal places."""
    freq_score = sum([character_frequencies.get(chr(letter).lower(), -100) for letter in str_bytes])
    return math.ceil(freq_score * 100) / 100


def xor_single_char(str_bytes, key):
    """Performs an XOR between a byte array and an integer"""
    output = b''

    for char in str_bytes:
        output += bytes([char ^ key])

    return output


def crack_single_byte_XOR(cipher_text):
    candidates = list()
    cipher_bytes = bytes.fromhex(cipher_text)
    # print ("cipher bytes: ", cipher_bytes)

    for key_candidate in range(256):
        byte_candidate = xor_single_char(cipher_bytes, key_candidate)
        print ("key candidate: ", key_candidate)
        print ("score candidate: ", score(byte_candidate))

        candidates.append((key_candidate, score(byte_candidate), byte_candidate))

    # print (candidates)
    return max(candidates, key=lambda item: item[1])

if __name__ == '__main__':
    print (crack_single_byte_XOR("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"))
