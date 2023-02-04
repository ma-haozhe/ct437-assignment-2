
seed1 = 0b11001010110011001010011010110010
str_seed1 = '11001010110011001010011010110010'
shifted = (seed1<<1)&1
print(bin(seed1))
print(bin(shifted))
print(len(str(bin(shifted))))