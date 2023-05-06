# სავარჯიშო 21. შეიყვანეთ ნებისმიერი სტრიქონი. იპოვეთ ყველაზე ხშირად განმეორებადი სიმბოლო და დაბეჭდეთ.
# Ask user for input
text = input("Enter a string: ")

char_count = {}
for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

most_common_char = max(char_count, key=char_count.get)

print(f"The most frequent character is '{most_common_char}', which appears {char_count[most_common_char]} times.")

