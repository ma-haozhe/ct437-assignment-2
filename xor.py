
seed1 = 0b11001010110011001010011010110010
str_seed1 = '11001010110011001010011010110010'
shifted = (seed1<<1)&1
print(bin(seed1))
print(bin(shifted))
print(len(str(bin(shifted))))
print(bin(0xFFFFFFF))

0b11001010110011001010011010110010
0b10110010101100110010100110101100
0b110101100101100101011001100101
0b11111111111111111111111111111111
0b1111111111111111111111111111



def encrypt(plaintext, keystream):
    ciphertext = ''
    for plain, key in zip(plaintext, keystream):
        ciphertext += chr(ord(plain) ^ key)
    return ciphertext 