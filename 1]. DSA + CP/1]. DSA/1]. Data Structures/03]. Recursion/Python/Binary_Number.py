# Given a non-negative integer number n, convert n into equivalent binary number.
# take the floor division of the quotient and then take the remainder of the recursive function inputs ( dividing the no by half)
def toBinary(n):
    
    if n <= 1:
        return str(n)
    
    bin_n = toBinary(n // 2)
    bin_n += str(n % 2)
    return (''.join(map(str, bin_n)))

print(toBinary(10))
# OUTPUT: 1010
print(toBinary(5))
# OUTPUT: 101
print(toBinary(20))
# OUTPUT: 10100

# Time Complexity: O(logN)
# Space Complexity: O(1)
