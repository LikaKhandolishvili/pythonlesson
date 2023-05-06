# სავარჯიშო 13. შეიტანეთ სტრიქონი. დაითვალეთ სტრიქონსი ხმოვნების რაოდენობა.

text = "Have a nice day"
vowels = "aeiou"
count = 0

for char in text:
    if char.lower() in vowels:
        count += 1

print("Number of vowels in the string:", count)

