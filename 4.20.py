# სავარჯიშო 20.შეიყვანეთ სტრიქონი. სტრიქონში დატოვეთ მხოლოდ ლატინური სიმბოლოები დანარჩენი კი ამოშალეთ.

import re

text = input("Enter a string: ")

latin_pattern = re.compile(r'[a-zA-Z]')

# Use regex to filter out non-Latin characters
latin_only = ''.join(filter(latin_pattern.match, text))

# Print the resulting string
print(latin_only)