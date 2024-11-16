def count_vowels(vowel_word):
    result = 0
    vowels = ["a", "e", "i", "o", "u"]
    for i in vowel_word:
        if i.lower() in vowels:
                result += 1
    return result

vowel_word = "Palindrome"

print(count_vowels(vowel_word))