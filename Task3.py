import re

def check_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    digit_criteria = bool(re.search(r'\d', password))
    special_char_criteria = bool(re.search(r'[\W_]', password))  
    strength_score = sum([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_char_criteria])

    if strength_score == 5:
        return "Strong password! Your password meets all the criteria."
    elif 3 <= strength_score < 5:
        return "Moderate password. Consider adding more complexity by including uppercase letters, digits, and special characters."
    else:
        return "Weak password. Try making your password longer and including a mix of uppercase, lowercase, numbers, and special characters."

password = input("Enter your password to check its strength: ")
feedback = check_password_strength(password)
print(feedback)
