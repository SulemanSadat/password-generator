import random

uppercase = "QWERTYUIOPASDFGHJKLZXCVBNM"
lowercase = uppercase.lower()
numbers = "1234567890"
symbols = "@#$%^&*"

use = uppercase + lowercase + numbers + symbols
password_length = 12
print("Password List")
for a in range(100):
    password = "".join(random.sample(use,password_length))
    print(f"{password}")
