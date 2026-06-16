# 7. Calculate the number of characters and vowels in an inputted string.
text=(input("Enter the character :"))
vowels_count=0
character_count=0
for i in text:
    character_count=character_count+1
    if i.lower() in "aeiou":
        vowels_count=vowels_count+1

print("Vowel is",vowels_count)

print("Character is",character_count)        
