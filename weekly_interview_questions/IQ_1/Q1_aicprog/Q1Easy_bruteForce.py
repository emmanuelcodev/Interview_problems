""" Question
Given two strings, check to see if they are anagrams. An anagram is when the two strings can be written
using the exact same letters (so you can just rearrange the letters to get a different phrase or word).
consider characters only to be lowercase only a-z
Test Cases:
"public relations" is an anagram of "crap built on lies."
"clint eastwood" is an anagram of "old west action"
"""
# Running time is O(n log n) + O(n) = O(n log n)

def isAnagram(str1, str2):
    #check for null values 
    if (str1 is None) or (str2 is None):
        return "One or more missing strings"

    #check length
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    if len(str1) != len(str2):
        return False
    else:
        # python sort is akin to mergesort, which means that its run time on average is O(n log n)

        string1, string2 = list(str1), list(str2)
        string1, string2 = sorted(string1, reverse=True), sorted(string2, reverse=True)
        return test(string1, string2)

        # o(n)
def test(str1, str2):
    for a, b in zip(str1, str2):
        if a != b:
            return False
    return True


print(isAnagram("public relations", None))
print(isAnagram("clint eastwood", "old west action"))
print(isAnagram("ce", "old west action"))
