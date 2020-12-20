# convert array of 1's and 0's to binary, then to int

def binary_array_to_number(arr):
    binStr = ""
    for bit in arr:
        binStr += str(bit)
    return int(binStr, 2)
