import re

def check_password_strength(password):
    strength = 0
    remarks = []

    if len(password) >= 8:
        strength += 1
    else:
        remarks.append("Too short (min 8 characters).")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        remarks.append("Add lowercase letters.")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        remarks.append("Add uppercase letters.")

    if re.search(r"\d", password):
        strength += 1
    else:
        remarks.append("Add digits.")

    if re.search(r"[^A-Za-z0-9]", password):
        strength += 1
    else:
        remarks.append("Add special characters.")

    common = ['password', '123456', 'admin']
    if password.lower() in common:
        remarks.append("Very common password.")

    return strength, remarks