#Write a Python program to remove duplicates from a list.

def count_matching_strings(strings):
    count = 0
    for s in strings:
        if len(s) >= 2 and s[0] == s[-1]:
            count += 1
    return count


string_list = ["abc", "121", "aba", "xyz", "aa", "1221"]
result = count_matching_strings(string_list)
print(f"Number of strings matching the criteria: {result}")
