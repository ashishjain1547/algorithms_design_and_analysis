"""
Iterate over the binary representation of the number N

"""

def binary_gap(N):
    b = bin(N)[2:]
    print(b)
    max_gap = 0
    current_gap = 0

    for i in b:
        if i == "0":
            current_gap += 1
        else:
            max_gap = max(current_gap, max_gap)
            current_gap = 0

    return max_gap

print(binary_gap(15))  # Example usage
            