# სავარჯიშო 19. დაწერეთ პროგრამა, სადაც user შეიყვანს (input ბრძანებით) სასურველ პაროლს (ტექსტურ მონონაცემს). დაადგინეთ
# შესაძლებელია თუ არა იგი ვარგისი იყოს პაროლად. დაბეჭდეთ შესაბამისი პასუხი. გაითვალისწინეთ, პაროლი
# ვარგისია, თუ იგი შედგება მინიმუმ 8 სიმბოლოსგან, აუცილებლად უნდა მონაწილეობდეს სულ მცირე ერთი
# დიდი ლათინური სიმბოლო, პატარა ლათინური სიმბოლო, ციფრი და სპეციალური სიმბოლო !@#$%^&*()_+
import re

password = input("Enter a password: ")

uppercase_pattern = re.compile(r'[A-Z]')
lowercase_pattern = re.compile(r'[a-z]')
number_pattern = re.compile(r'[0-9]')
special_char_pattern = re.compile(r'[!@#$%^&*()_+]')


if len(password) < 8:
    print("Password is too short. It must be at least 8 characters long.")
elif not uppercase_pattern.search(password):
    print("Password is not strong enough. It must contain at least one uppercase letter.")
elif not lowercase_pattern.search(password):
    print("Password is not strong enough. It must contain at least one lowercase letter.")
elif not number_pattern.search(password):
    print("Password is not strong enough. It must contain at least one number.")
elif not special_char_pattern.search(password):
    print("Password is not strong enough. It must contain at least one special character (!@#$%^&*()_+).")
else:
    print("Password is strong and can be used.")
