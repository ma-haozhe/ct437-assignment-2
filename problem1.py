#delaring the two seeds we use for the stream cipher
# '0b' in python is used as a prefix to declare binary numbers.
seed1 = 0b11001010110011001010011010110010
seed2 = 0b00110110111100101001010010011010

#define the function that calculate the bit
def feed_back_func(seed1, seed2):
    key = []
    for i in range(len(seed1)):
        bit1 = 0

for i in range(len(str(seed1))):
    print(str(seed1)[i])