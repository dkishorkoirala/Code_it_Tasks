def count_vowel(text):
    count = 0

    for char in text:
        if char in "aeiouAEIOU":
            count += 1

    return count

text = input("Enter the sentence: ")
print(f"Vowel count: {count_vowel(text)}")