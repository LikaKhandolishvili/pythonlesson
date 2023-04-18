# სავარჯიშო 11. text ცვლადს მიანიჭეთ სტრიქონი “Hello, this is example of string. Please, write this text and do
# some exercises.”.
# დაითვალეთ სტრიქონში სიტყვების რაოდენობა.

def count_words(text):
    words = text.split()
    return len(words)

text = "Hello, this is example of string. Please, write this text and do some exercises."
print(count_words(text))

