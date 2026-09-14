# ==========================================
# USERNAME & PASSWORD VALIDATOR
# ==========================================

print("=" * 50)
print("       USERNAME & PASSWORD VALIDATOR")
print("=" * 50)

# Taking input
username = input("Enter username: ")
password = input("Enter password: ")

print("\n" + "=" * 50)
print("USERNAME VALIDATION")
print("=" * 50)

# Username validation
username_valid = True

# Check username length
if len(username) > 5:
    print("✓ Username length is valid.")
else:
    print("X Username must contain at least 5 characters.")
    username_valid = False

# Check username contains only letters and numbers
if username.isalnum():
    print("✓ Username contains only letters and numbers.")
else:
    print("X Username should contain only letters and numbers.")
    username_valid = False


print("\n" + "=" * 50)
print("PASSWORD VALIDATION")
print("=" * 50)

# Password validation
password_valid = True

# Check password length
if len(password) >= 8:
    print("✓ Password has at least 8 characters.")
else:
    print("X Password must contain at least 8 characters.")
    password_valid = False


# Check uppercase letter
has_upper = False

for char in password:
    if char.isupper():
        has_upper = True
        break

if has_upper:
    print("✓ Password contains an uppercase letter.")
else:
    print("X Password must contain an uppercase letter.")
    password_valid = False


# Check lowercase letter
has_lower = False

for char in password:
    if char.islower():
        has_lower = True
        break

if has_lower:
    print("✓ Password contains a lowercase letter.")
else:
    print("X Password must contain a lowercase letter.")
    password_valid = False


# Check digit
has_digit = False

for char in password:
    if char.isdigit():
        has_digit = True
        break

if has_digit:
    print("✓ Password contains a digit.")
else:
    print("X Password must contain a digit.")
    password_valid = False


# Check special character
special_characters = "@#$%!&*"

has_special = False

for char in password:
    if char in special_characters:
        has_special = True
        break

if has_special:
    print("✓ Password contains a special character.")
else:
    print("X Password must contain a special character.")
    password_valid = False


# ==========================================
# FINAL RESULT
# ==========================================

print("\n" + "=" * 50)
print("             FINAL RESULT")
print("=" * 50)

if username_valid:
    print("✓ Username is VALID")
else:
    print("X Username is INVALID")

if password_valid:
    print("✓ Password is VALID")
    print("🔐 Password Strength: STRONG")
else:
    print("X Password is INVALID")
    print("⚠️ Password Strength: WEAK")

print("=" * 50)