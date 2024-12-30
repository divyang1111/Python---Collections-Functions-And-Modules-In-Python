'''Write a Python function that checks whether a passed string is 
palindrome or not  '''

def is_palindrome(s):
   
   
    normalized = ''.join(c.lower() for c in s if c.isalnum())
    
    
    return normalized == normalized[::-1]


string = "A man, a plan, a canal, Panama"
if is_palindrome(string):
    print(f'"{string}" is a palindrome.')
else:
    print(f'"{string}" is not a palindrome.')
