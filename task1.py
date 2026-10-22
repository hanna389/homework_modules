import random
import string

password_length = 5

characters = string.hexdigits + string.ascii_uppercase + string.punctuation

password = "".join(random.choice(characters) for _ in range(password_length))

print("згенерований пароль: ", password)