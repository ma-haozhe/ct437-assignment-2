# CT437 Assignment 2
# Haozhe Ma
# 19280083

# Problem 1, implementing a cipher using structure similar to A5/1
# but slight different feedback functions.
# A5/1 uses two LFSRs and two feedback functions.
# The output of the two LFSRs are combined to return a keystream to encrypt our plaintext later.

# delaring the two seeds we use for the stream cipher
# '0b' in python is used as a prefix to declare binary numbers.
seed1 = 0b11001010110011001010011010110010
str_seed1 = '11001010110011001010011010110010'
# the length of the seed is 32 bits
seed2 = 0b00110110111100101001010010011010

# define the function that calculate the bit


def feed_back_func(seed1, seed2, n):
    key = []
    for i in range(n):
        bit1 = ((seed1 >> 31) & 1) ^ ((seed1 >> 16) & 1) & 1
        # so the line above did several things, it is our first feedback function
        # 1. extract the most left digit in in the seed (most significant digit) and only take that digit
        # 2. extract the digit in the middle of the seed (both of them used '& 1' to do that)
        # 3. do bitwise XOR of the two by using '^' and get our first bit
        # print('seed1 = ', bin(seed1))
        bit2 = ((seed2 >> 31) & 1) ^ (
            (seed2 >> 3) & 1) ^ ((seed2 >> 10) & 1) & 1
        # this second feedback function is slightly different from the first one,
        # it uses XOR from three bits in the seed2, the most left, the third on the right and the 10th on the right.

        # print('seed2 = ', bin(seed2))
        # https://stackoverflow.com/a/24617938 : Python's integer type have arbitrary precision, which means that as you bit shift, it keeps getting bigger.
        # seed1 = (seed1 << 1) & (0xffffffff)

        seed1 = ((seed1 << 1) | (
            seed1 >> (len(str(str_seed1)) - 1))) & (0xFFFFFFFF)
        seed2 = ((seed2 << 1) | (
            seed2 >> (len(str(str_seed1)) - 1))) & (0xFFFFFFFF)
        # shift left 1 bit for both seed1 and seed2 and add the shifted bit to their right
        # The length of seed1 and seed2 is limited to 32 bits using & (0xFFFFFFFF)
        # 0xFFFFFFFF is in hex, its the same as 0b111111...11 (32 '1's) in binary.
        key.append(bit1 ^ bit2)
        # bitwise XOR of bit1 and bit2 is appended to the list "key".
    return key


# encryption returns a ciphertext string which is the XOR of each character in the plaintext and the corresponding element in the key list
def encryption(plaintext, key):
    ciphertext = ''
    # Iterate over each character in the plaintext string
    for i in range(len(plaintext)):
        # Get the current plaintext character
        plain = plaintext[i]
        # Convert the plaintext character to its integer representation using 'ord'
        # learnt: it can be similar to 'bytes()' but 'ord' only works with single character
        plain_in_int = ord(plain)
        # XOR the plaintext character with the corresponding key element to encrypt
        exor = plain_in_int ^ key[i]
        # convert the xor result back to a character and append it to the ciphertext string
        # you can't use str cause it will give you a bunch of binary numbers.
        ciphertext += chr(exor)
    return ciphertext

# decryption is similar to encryption, just do everything in reverse


def decryption(ciphertext, key):
    plaintext = ''
    for i in range(len(ciphertext)):
        cipher = ciphertext[i]
        cipher_in_int = ord(cipher)
        exor = cipher_in_int ^ key[i]
        plaintext += chr(exor)
    return plaintext


# call feedback function to generate a key with length of 40.
key = feed_back_func(seed1, seed2, 40)
print(key)

encrypted = encryption("hello hello this is haozhe", key)
print(encrypted)

# "iemln hdmln uiis!hr!h`nzie" is the cipher text we get from encryption.
# Decrypt the encrypted ciphertext using the key
decrypted = decryption("ielmn!idlmo uihs!ir haozhd", key)
print(decrypted)
