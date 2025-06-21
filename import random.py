import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("🔐 Welcome to the Password Generator!")
user_length = int(input("Enter the desired password length: "))
new_password = generate_password(user_length)
print(f"Here is your secure password: {new_password}")
