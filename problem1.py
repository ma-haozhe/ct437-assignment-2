# CT437 Assignment 2
# Haozhe Ma
# 19280083

# Problem 1, implementing a cipher using structure similar to A5/1
# but slight different feedback functions.
# A5/1 uses two LFSRs and two feedback functions. 
# The output of the two LFSRs are combined to return a keystream to encrypt our plaintext later.


#delaring the two seeds we use for the stream cipher
# '0b' in python is used as a prefix to declare binary numbers.
seed1 = 0b11001010110011001010011010110010
str_seed1 = '11001010110011001010011010110010'
#print(len(str_seed1))
#the length of the seed is 32 bits
seed2 = 0b00110110111100101001010010011010

#Here are some experiment I did on how shifting operation works.
#shifted = seed1>>2
#print(bin(seed1))
#print(bin(shifted))
#print(len(str(bin(shifted))))

#define the function that calculate the bit
def feed_back_func(seed1, seed2):
    key = []
    for i in range(len(str_seed1)):
        bit1 = ((seed1 >> 31) & 1) ^ ((seed1 >> 16) & 1) & 1
        # so the line above did several things, it is our first feedback function
        # 1. extract the most left digit in in the seed (most significant digit) and only take that digit
        # 2. extract the digit in the middle of the seed (both of them used '& 1' to do that)
        # 3. do bitwise XOR of the two by using '^' and get our first bit
        print(bit1)
        bit2 = ((seed1 >> 31) & 1) ^ ((seed1 >> 3) & 1) ^ ((seed1 >> 10) & 1) & 1
        # this second feedback function is slightly different from the first one, 
        # it uses XOR from three bits in the seed2, the most left, the third on the right and the 10th on the right.
        