def string_palindrome_or_not(str):
    str2=str[::-1]
    if str==str2:
       print("palindrome")
    else:
        print("not palindrome")
str=input()
string_palindrome_or_not(str)