def sum_of_substrings(s):
    n = len(s)
    total_sum = 0
    
    # Generate all contiguous substrings
    for i in range(n):
        for j in range(i, n):
            total_sum += int(s[i:j+1])  # Convert substring to integer and add to sum
            
    return total_sum

# Example usage
s = input().strip()  # Taking input dynamically
print(sum_of_substrings(s))