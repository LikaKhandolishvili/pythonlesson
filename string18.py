# სავარჯიშო 18. დაწერეთ პროგრამა, რომელშიც მომხარებელს შეაყვანინებთ რაიმე სტრიქონს. პროგრამამ უნდა დაითვალოს დიდი
# ლათინური ასოების, პატარა ლათინური ასოების და ციფრების რაოდენობა ცალ-ცალკე და დაბეჭდეთ მიღებული
# შედეგები. ასევე დაითვალეთ სტრიქონში გამოყენებული სპეციალური სიმბოლოების რაოდენობა როგორიცაა
# !@#$%^&*()_+

text = input("Enter a text: ")

upper_count = 0
lower_count = 0
number_count = 0
symbol_count = 0

for char in text:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1
    elif char.isnumeric():
        number_count += 1
    else:
        symbol_count += 1

print(f"text of uppercase letters: {upper_count}")
print(f"text of lowercase letters: {lower_count}")
print(f"text of numbers: {number_count}")
print(f"text of symbol: {symbol_count}")
