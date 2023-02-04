#delaring the two seeds we use for the stream cipher
# '0b' in python is used as a prefix to declare binary numbers.
seed1 = 0b11001010110011001010011010110010
str_seed1 = '11001010110011001010011010110010'
#print(len(str_seed1))
#the length of the seed is 32 bits
seed2 = 0b00110110111100101001010010011010

#some experiment on how shifting operation works.
#shifted = seed1>>2
#print(bin(seed1))
#print(bin(shifted))
#print(len(str(bin(shifted))))

#define the function that calculate the bit
def feed_back_func(seed1, seed2):
    key = []
    for i in range(len(str_seed1)):
        bit1 = seed1 >> 0
