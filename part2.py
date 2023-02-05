# CT437 Assignment 2
# Haozhe Ma
# 19280083


def analyze(binary_list):
    # initialize counters
    zero_count = 0
    one_count = 0
    longest_zero_run = 0
    longest_one_run = 0
    run_lengths = {i: 0 for i in range(3, 7)}

    # loop through the binary list
    current_run = binary_list[0]
    current_run_length = 1
    for i in range(1, len(binary_list)):
        if binary_list[i] == current_run:
            current_run_length += 1
        else:
            if current_run == 0:
                zero_count += current_run_length
                longest_zero_run = max(longest_zero_run, current_run_length)
                if 3 <= current_run_length <= 6:
                    run_lengths[current_run_length] += 1
            else:
                one_count += current_run_length
                longest_one_run = max(longest_one_run, current_run_length)
                if 3 <= current_run_length <= 6:
                    run_lengths[current_run_length] += 1

            # reset for next run
            current_run = binary_list[i]
            current_run_length = 1

    # handle the last run
    if current_run == 0:
        zero_count += current_run_length
        longest_zero_run = max(longest_zero_run, current_run_length)
        if 3 <= current_run_length <= 6:
            run_lengths[current_run_length] += 1
    else:
        one_count += current_run_length
        longest_one_run = max(longest_one_run, current_run_length)
        if 3 <= current_run_length <= 6:
            run_lengths[current_run_length] += 1

    # print results
    print("Total length of LFSR stream: ", len(binary_list))
    print("Overall distribution of 0s and 1s:")
    print(f"\t0s: {zero_count}")
    print(f"\t1s: {one_count}")
    print("\nLongest runs:")
    print(f"\t0s: {longest_zero_run}")
    print(f"\t1s: {longest_one_run}")
    print("\nNumber of runs of i repetitions (3 <= i <= 6):")
    for i in range(3, 7):
        print(f"\t{i}: {run_lengths[i]}")


def lfsr(seed, iterations):
    print(bin(seed))
    binary_list = []
    for i in range(iterations):
        # this is one of the feedback function from problem 1.
        bit1 = (((seed >> 31) & 1) ^ ((seed >> 16) & 1)) & 1 
        binary_list.append(bit1)
        # Rotate the seed to the left.
        seed = ((seed << 1) | (seed >> 31)) & (0xFFFFFFFF)
    return binary_list

seed = [0b11001010110011001010011010110010, 0b00110110111100101001010010011010, 0b100101101101111001001010110010011, 0b011001010001001011011111010110110, 0b110011101010111010100010001110110]

# When doing testing, go through different seed in the list to see the different results.
# Since we're only doing five tests I didn't make it into a loop.
binary_list = lfsr(seed[4], 10**6)

analyze(binary_list)
