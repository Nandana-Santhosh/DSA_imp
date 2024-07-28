'''Find all duplicate characters in string'''
def dupli(string):
    chars={}
    for i in string:
        if i not  in chars:
            chars[i]=1
        else:
            chars[i]+=1
    duplicates = []
 
    # Iterate through the dictionary to find characters with count greater than 1
    for char, count in chars.items():
        if count > 1:
            duplicates.append(char)
 
    return duplicates
print(dupli("hello world"))