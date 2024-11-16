import re

def are_anagrams(string1, string2):
    string1_mod = string1.lower()
    string2_mod = string2.lower()
    
    string1_mod = re.sub(r'[^a-zA-Z]', '', string1_mod)
    string2_mod = re.sub(r'[^a-zA-Z]', '', string2_mod)
    
    string1_mod = sorted(string1_mod)
    string2_mod = sorted(string2_mod)

    if string1_mod == string2_mod:
        return True
    else:
        return False

string1 = "baba"
string2 = "ABBA"

print(are_anagrams(string1, string2))