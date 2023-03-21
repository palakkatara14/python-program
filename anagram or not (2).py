str1 = "race"
str2 =  "care"
str1 = str1.lower()
str2 = str2.lower()
if len(str1)==len(str2):
    str1_sorted = sorted(str1)
    str2_sorted = sorted(str2)
    if str1_sorted==str2_sorted:
        print("anagram")
    else:
        print("not anagram")