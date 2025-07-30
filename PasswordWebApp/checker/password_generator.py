import string
import random

def generate_password(length=12, use_special=True):
    characters = string.ascii_letters + string.digits
    if use_special:
        characters += string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))