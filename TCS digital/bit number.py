n=int(input())
s1=input().strip()
s2=input().strip()
if sorted(s1)==sorted(s2):
    print("YES")


'''
1. sort() Method (In-Place Sorting)
Used on lists only.
Modifies the original list in place.
Returns None.
eg:
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort() 
words.sort(key=len)


2. sorted() Function (Returns a New List)
Works on any iterable (lists, tuples, sets, dictionaries, etc.).
Returns a new sorted list without modifying the original iterable.

numbers = [3, 1, 4, 1, 5, 9, 2]
sorted_numbers = sorted(numbers)  # Returns a new sorted list
print(sorted_numbers)  # Output: [1, 1, 2, 3, 4, 5, 9]
print(numbers)  # Original list remains unchanged


'''