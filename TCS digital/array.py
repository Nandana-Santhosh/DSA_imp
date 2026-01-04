def max_fair_sequence_sum(n, arr):
    # Separate positive and negative numbers
    positives = [x for x in arr if x > 0]
    negatives = [x for x in arr if x < 0]

    # Sort positives in descending order and negatives in ascending order
    positives.sort(reverse=True)
    negatives.sort()

    # Initialize the result variables
    max_sum = 0
    i, j = 0, 0

    # Build the fair sequence with maximum sum
    while i < len(positives) and j < len(negatives):
        max_sum += positives[i] + negatives[j]
        i += 1
        j += 1

    return max_sum

# Input example
n = 5
arr = [21, 12, 13, -21, -2]

# Output the result
print(max_fair_sequence_sum(n, arr))