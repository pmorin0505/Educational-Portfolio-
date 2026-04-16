"""
Cybersecurity Programming – Password Strength Checker

This program evaluates password strength using common security rules:
- Minimum length requirement
- Uppercase and lowercase validation
- Numeric character requirement
- Special character requirement

This demonstrates:
- Input validation
- Pattern matching using regex
- Basic security enforcement logic
"""

import re


def check_password_strength(password):
    """
    Evaluates password strength based on security rules.
    Returns a string describing password quality.
    """

    if len(password) < 8:
        return "Weak: Password too short"

    if not re.search(r"[a-z]", password):
        return "Weak: Add a lowercase letter"

    if not re.search(r"[A-Z]", password):
        return "Weak: Add an uppercase letter"

    if not re.search(r"[0-9]", password):
        return "Weak: Add a number"

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Weak: Add a special character"

    return "Strong Password ✅"


if __name__ == "__main__":
    password = input("Enter a password to check: ")
    print(check_password_strength(password))
